'use strict';
/*
Real published OpenTelemetry packages. Two releases span SDK 2.x -> 3.x:
DO NOT interpret an observed difference as an isolated causal effect of PR #7061.
This is a hypothesis-confirming historical case, NOT a blinded novel-method benchmark.
*/
const assert = require('node:assert/strict');
const fs = require('node:fs');
const { SpanKind, SpanStatusCode } = require('@opentelemetry/api');
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');
const tracePackage = process.env.TRACE_PKG;
if (!['@opentelemetry/sdk-trace-base', '@opentelemetry/sdk-trace'].includes(tracePackage)) {
  throw new Error('TRACE_PKG must identify a pinned SDK tracing package');
}
const { InMemorySpanExporter, SimpleSpanProcessor } = require(tracePackage);
const exporter = new InMemorySpanExporter();
const sdk = new NodeSDK({
  autoDetectResources: false,
  // SDK trace 3.x changed this constructor to an options object.
  spanProcessors: [new SimpleSpanProcessor(
    tracePackage === '@opentelemetry/sdk-trace' ? { exporter } : exporter
  )],
  instrumentations: [new HttpInstrumentation()],
});
sdk.start(); // IMPORTANT: register before importing node:http
const http = require('node:http');

function request(port, status) {
  return new Promise((resolve, reject) => {
    const req = http.get({ hostname: '127.0.0.1', port, path: '/status/' + status },
      res => {
        const chunks = [];
        res.on('data', chunk => chunks.push(chunk));
        res.on('end', () => resolve({ status: res.statusCode, body: Buffer.concat(chunks).toString('utf8') }));
      });
    req.on('error', reject);
  });
}

function errorType(span) {
  return Object.prototype.hasOwnProperty.call(span.attributes, 'error.type')
    ? span.attributes['error.type'] : null;
}

async function main() {
  // Read the installed package metadata without assuming package.json is exported.
  const path = require('node:path');
  let packageDir = path.dirname(require.resolve('@opentelemetry/instrumentation-http'));
  while (!fs.existsSync(path.join(packageDir, 'package.json'))) {
    const parent = path.dirname(packageDir);
    if (parent === packageDir) throw Error('Cannot locate installed package metadata');
    packageDir = parent;
  }
  const version = JSON.parse(fs.readFileSync(path.join(packageDir, 'package.json'), 'utf8')).version;
  const expectedMissing = Number(process.env.EXPECTED_MISSING);
  if (!Number.isInteger(expectedMissing)) throw Error('EXPECTED_MISSING required');
  const server = http.createServer((req, res) => {
    const status = Number((req.url || '').split('/').pop());
    res.statusCode = status;
    res.end('response:' + status);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = server.address().port;
  const rows = [];
  try {
    for (const status of [200, 404, 500]) {
      exporter.reset();
      const output = await request(port, status);
      assert.deepEqual(output, { status, body: 'response:' + status },
        'business behavior must remain correct');
      await new Promise(resolve => setTimeout(resolve, 60));
      const spans = exporter.getFinishedSpans()
        .filter(s => s.attributes['http.response.status_code'] === status);
      const client = spans.filter(s => s.kind === SpanKind.CLIENT);
      const serverSpans = spans.filter(s => s.kind === SpanKind.SERVER);
      assert.equal(client.length, 1, 'exactly one client span for ' + status);
      assert.equal(serverSpans.length, 1, 'exactly one server span for ' + status);
      const c = client[0], s = serverSpans[0];
      const expectedClientError = status >= 400;
      const expectedServerError = status >= 500;
      assert.equal(c.status.code, expectedClientError ? SpanStatusCode.ERROR : SpanStatusCode.UNSET);
      assert.equal(s.status.code, expectedServerError ? SpanStatusCode.ERROR : SpanStatusCode.UNSET);
      rows.push({ status, business: 'pass', span_count: 2,
        client_error_type: errorType(c), server_error_type: errorType(s),
        client_status_code: c.status.code, server_status_code: s.status.code });
    }
  } finally {
    await new Promise(resolve => server.close(resolve));
    await sdk.shutdown();
  }
  const expected = [
    { status: 200, client: null, server: null },
    { status: 404, client: '404', server: null },
    { status: 500, client: '500', server: '500' },
  ];
  const mismatches = rows.flatMap((row, i) =>
    ['client', 'server'].flatMap(kind =>
      row[kind + '_error_type'] === expected[i][kind] ? [] :
        [String(row.status) + ':' + kind]));
  const gates = {
    business_http_success: rows.every(r => r.business === 'pass'),
    span_count_success: rows.every(r => r.span_count === 2),
    span_status_success: true,
    semantic_error_type_success: mismatches.length === 0,
  };
  assert.equal(mismatches.length, expectedMissing,
    'release behavior changed; review rather than silently reclassifying it');
  const data = { kind: 'historical_installed_package_replay',
    version, trace_package: tracePackage,
    expected_missing: expectedMissing, mismatches, gates, rows,
    design_warning: '0.223.0 and 0.300.0 differ in many ways including SDK major version; no isolated PR causality or representative detection rate.' };
  const target = process.env.RESULT_FILE || 'results.json';
  fs.writeFileSync(target, JSON.stringify(data, null, 2) + '\n');
  console.log(JSON.stringify(data, null, 2));
}
main().catch(err => { console.error(err); process.exitCode = 1; });
