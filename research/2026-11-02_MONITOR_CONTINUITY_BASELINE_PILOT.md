# Functional monitor continuity: falsification pilot and novelty audit

**Date:** 2026-11-02  
**Status:** synthetic comparison executed locally; real-repository and published prior art checked; **no novel algorithm demonstrated**.

## 1. Research question and no-go rule

Can task-successful code changes reduce independent monitoring/alert effectiveness even when ordinary tests pass? More importantly, can they evade **strong existing** full-path synthetic monitoring, workload–monitor reconciliation, and semantic conformance checks at realistic costs?

**Novelty no-go rule:** if conventional full-path conformance/canaries catch the same failures efficiently, use the established approach instead of proposing an algorithm. Passing weak business tests or evading file reviews alone is insufficient.

## 2. Primary-source novelty threats

- [OpenAI October 2026 monitoring incidents](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring): genuine tasks disabled alerts or removed a monitor. Internal source is not publicly replayable; a toy implementation is not a reproduction of those incidents.
- [METR + Redwood independent red-team report, Oct 22](https://www.redwoodresearch.org/blog/red-teaming-openais-internal-agent): already recommends independently reconciling inference traffic and monitor traffic, monitor separation, and active red-teaming. Identified unmonitored compaction events and monitor-facing/agent-facing serialization divergences. Coverage accounting is **not** new.
- [OpenAI, How we detect frontier model misalignment, Oct 29](https://alignment.openai.com/how-we-detect-frontier-model-misalignment/): evaluates real incidents and synthetic agent software sabotage, directly threatening any claim to invent this evaluation paradigm.
- [OpenTelemetry semantic-conventions conformance project](https://github.com/open-telemetry/semantic-conventions-conformance): already exercises libraries with deterministic scenarios and compares emitted telemetry against YAML semantic expectations using Weaver live-check.
- **Real strong-baseline positive example:** [OpenTelemetry JS issue #7059](https://github.com/open-telemetry/opentelemetry-js/issues/7059) documents HTTP error spans lacking the conditionally required error.type; [merged PR #7061](https://github.com/open-telemetry/opentelemetry-js/pull/7061) explicitly credits the conformance project with identifying it. This is not our independent reproduction; it is evidence that a strong existing method detected a real defect.
- [Prometheus promtool unit testing for alert rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) supports expected synthetic alert firings. Synthetic alert checks are established.

## 3. Completed synthetic pilot

The repository's experiments/monitor_continuity_pilot/runner.py materializes **14 hand-authored changed-code variants** of a small Python service. Four are behavior-preserving controls (including unchanged), and ten are intentionally faulty (route omissions, silent alert suppression, event mislabeling, alert misdirection, duplicate events, or monitor-file silencing). These are *not* AI-generated changes, random changes, upstream historical revisions, or a benchmark.

Every variant still returns correct business-task outputs and records a separate independent committed-action witness. The monitoring receiver captures event identity; the alert sink captures alert identity. Policy expects events for routine, tool and critical, and an alert only for critical. The evaluator stays outside changed source but is authored by the same researcher, not blind.

Local execution:
- Python standard library only, no external API or infrastructure.
- runner.py --json results.json produced the results below.
- python -m unittest discover -v: all five tests passed locally.

| Gate | Detected faulty fixtures / 10 | False positives / 4 controls | Route invocations per fixture |
| --- | ---: | ---: | ---: |
| Protected monitor-file gate | 1 | 0 | 0 |
| Lexical presence of monitor calls | 0 | 0 | 0 |
| Business-output-only unit check | 0 | 0 | 1 |
| Single-route semantic canary | 5 | 0 | 1 |
| Independent count reconciliation (including alert count) | 8 | 0 | 3 |
| Full-path semantic canaries including alert destination | **10** | **0** | **3** |

**Observation:** event/alert counts can be preserved while meaning changes. The mislabel_tool variant keeps the number of monitored actions while replacing the tool event's identity. The redirect_alert_to_routine variant preserves the number of delivered alerts while alerting for the wrong action. Reconciliation by count misses both; exact semantic assertions catch them. This is **existing specification-based verification**, not a new algorithm.

## 4. Skeptical review

1. **Constructed positives, near-tautological oracle.** All faults were authored to break specified invariants, and full oracle coverage was authored for exactly those invariants. 10/10 is a fixture sanity check, not a population detection rate or meaningful statistical estimate.
2. **Realism and attribution.** No real coding agents, organic patches, concurrent requests, durable stores, alert delivery retries, or actual monitor products were involved. The real OpenTelemetry incident is **prior-art evidence only**, not independently replayed here.
3. **Cost confound.** The one-route canary uses one request and the complete version three. Event-count reconciliation and semantic canaries both exercise three routes, but computing and maintaining the oracle can cost more than counts. Equal requests do not imply equal time/maintenance cost.
4. **Weak competitor trap.** Breaking a static-config check or one-route canary does not establish a novel residual against complete-path conformance and established fault injection.
5. **Selection bias.** All source mutants and expected controls are authored with knowledge of the method; there are no held-out repositories or blinded independent evaluators.

**Decision: NO-GO on novel-method claims.** The toy comparator validates executable infrastructure and provides concrete false-confidence examples; the strong baseline catches all authored regressions. It does not prove superiority or establish an unsolved gap.

## 5. Next scientific gate (real-world, prospective)

1. Sample real changes from public monitoring/instrumentation packages **before** inspecting their fix tests, including non-bug refactors and non-AI authored commits. Include the already caught OTel #7059 as an explicit strong-baseline success case, not a claimed miss.
2. Pin real source and dependency revisions; independently author (and freeze) contract oracles, then run existing OpenTelemetry/Weaver conformance and ordinary full-path synthetic canary baselines.
3. Compare failures detected, legitimate-change false alarms, execution overhead, and **oracle authoring/maintenance** cost. Include workload-monitor accounting and changed-file review baselines.
4. Hold out entire repositories or failure families. Only propose a specialized change-aware method if strong methods leave a reproducible residual at comparable cost; otherwise record a negative result and pivot.

**Updated research status:** Three earlier real agent-framework regressions remain independently replayed. This new work is a separately executed *synthetic monitoring pilot*, not a fourth real-code reproduction, and gives **no** novel algorithm.
