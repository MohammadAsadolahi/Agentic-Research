# Verified real-library replay result — added November 2, 2026

**Executed GitHub Actions:** [run #41457189971](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41457189971), workflow commit [105c70e](https://github.com/MohammadAsadolahi/Agentic-Research/commit/105c70e2a784e4e8775fc4b3e10d5f9b378d1902). This result supersedes the earlier pending language below.

We pinned the **actual factory source at upstream LangChain commit 80b74090515a594cc8421fb2d82e98f4e256c29f** and installed its Python project in editable mode for both jobs. Only the Anthropic adapter release changed; the CI tests invoked real LangChain factory and provider serializer code, with no network model calls.

| Upstream factory source | Anthropic adapter | Local factory repair | Provider wire contract | Orphan result ids |
| --- | --- | --- | --- | --- |
| 80b740905 | 1.7.4 | PASS | **FAIL (expected)** | toolu_01ABC |
| 80b740905 | 1.7.5 | PASS | PASS | none |

Both jobs completed successfully: the affected job asserts **expected fail** and verifies the regression; the corrected job asserts **expected pass**. The provider emitted 0 tool_use ids versus 1 tool_result id on the affected version; emitted 1 matching tool_use and 1 tool_result on the corrected version. Machine-readable JSON is printed in each job log.

**Important provenance correction:** [initial CI run #41456902263](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41456902263) failed for the wrong reason: released langchain==1.4.2 did NOT expose the private factory helper. The original issue described **master source commit 80b740905**, alongside installed package version metadata. The experimental comparison MUST pin the source SHA, not infer that code is in PyPI version 1.4.2. The corrected CI therefore installed the same upstream factory source commit in both environments. Reported metadata prints 1.4.2 for the source project; treat it as package metadata, **not source provenance**.

**Scope:** A real source-level integration test reproduced a historical *cross-provider* defect and its correction; it did NOT call a live Anthropic endpoint. It has not shown failure of strong contemporary regression test selection: our deliberately path-only selector is not that. We still require unseen failures, strong method baselines and matched cost before proposing a novel mechanism.

---

# First falsification milestone: real-package test harness

Date: November 2, 2026. State: experimental setup; do not treat an expected result as observed.

## Independently documented historical failures

1. LangChain [PR #40530](https://github.com/langchain-ai/langchain/pull/40530) (2026-09-22) added a factory-level malformed-tool-call repair with local tests, in an AI-assisted patch. [Issue #40853](https://github.com/langchain-ai/langchain/issues/40853) reported a regression when the Anthropic provider serialized the repaired history: an orphan tool_result without a matching tool_use. [PR #40864](https://github.com/langchain-ai/langchain/pull/40864) (2026-09-27) added the provider-specific fix and new regression tests. The issue contains a real offline reproducer; the reporter used langchain 1.4.2 and langchain-anthropic 1.7.4, and a commenter verified the fix in 1.4.3/1.7.5.
2. [Issue #38351](https://github.com/langchain-ai/langchain/issues/38351) and [PR #38355](https://github.com/langchain-ai/langchain/pull/38355) document another cross-boundary error: graph routing could return the model destination after middleware injected synthetic ToolMessages even though the declared routing path_map omitted it. The merged fix includes a regression test.

## Experiments authored

- [Real package reproducer](../experiments/real_langchain_replay/reproduce_real_provider.py): calls the actual factory's repair helper and actual Anthropic serializer with a fake API key and no live API request. It checks the narrow local repair as well as the provider message contract, outputting a JSON record with exact installed package versions.
- [GitHub Actions matrix](../.github/workflows/real-langchain-replay.yml): affected 1.4.2 / 1.7.4 expects a contract failure; fixed 1.4.3 / 1.7.5 expects a pass. These are EXPECTED based on the issue report, not an observed workflow result until logs are checked.
- [Selector](../experiments/real_langchain_replay/test_selector.py): hand-written mapping of changed symbols in factory.py to the downstream provider and graph contracts. Six self-tests ran locally and passed. The graph test name is a placeholder, NOT implemented, and its mapping is based on knowing the failures in advance.

Local setup: Python compile check succeeded; real package installation was blocked by DNS to the package index in this environment. The prior eight-test synthetic protocol witness is not an upstream reproduction.

## Scientific stop conditions

This is **not yet a measured failure of strong existing testing methods**. The path-only baseline is intentionally weak; modern regression selection could include downstream tests if properly instrumented. A manual map to known repairs is retrospective and should NOT be passed off as zero-shot test discovery.

Next:
1. Inspect actual workflow logs and both installed-version outcomes. If setup fails, record it separately from the bug.
2. Compare the original test suites as they existed when PR #40530 merged with a true affected-code/coverage-based selector, not an illustrative baseline.
3. Assemble unseen historical cross-boundary regressions across independent frameworks, plus legitimate-change negatives.
4. Lock an edge/consumer-contract inference procedure BEFORE reading the held-out incident details.
5. Compare faults detected, false positives, runtimes and costs against static analysis, conventional integration tests and existing differential and mutation-based testing.

Only if there is a genuine residual defect-class that strong existing methods miss at matched budgets should an algorithmic contribution be attempted.
