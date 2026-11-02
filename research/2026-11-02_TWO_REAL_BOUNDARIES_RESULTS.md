# Verified real-code boundary regression pilot — two distinct mechanisms

**As-of:** November 2, 2026  
**Execution status:** four source/version-pinned replay jobs completed successfully on GitHub Actions. These are historical, known-defect reproductions, **not** unseen fault discovery, a strong-baseline comparison, or a novel algorithm.

**Run and independently inspectable logs:** [GitHub Actions #41457528866](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41457528866). All four jobs are green **because each explicitly asserts the historical expected result**, including expecting the older code to fail its downstream contract. Green does not mean the original bug is absent.

## Observed measurements

| Boundary / provenance | Local behavior | Downstream contract | Concrete output |
| --- | --- | --- | --- |
| Factory at [80b740905](https://github.com/langchain-ai/langchain/commit/80b74090515a594cc8421fb2d82e98f4e256c29f) + Anthropic 1.7.4 | PASS — synthetic tool result generated | **FAIL** | 1 tool_result with 0 tool_use; orphan toolu_01ABC |
| Same factory snapshot + Anthropic 1.7.5 | PASS | PASS | 1 matching tool_result and tool_use; 0 orphans |
| Graph factory at [5893459c](https://github.com/langchain-ai/langchain/commit/5893459c4f2bfac6c8d3262cae1e3f2246d9287f) | PASS — middleware synthesized tool result | **FAIL** | KeyError('model') on conditional graph route |
| Graph factory at [382bace0](https://github.com/langchain-ai/langchain/commit/382bace06c90c3013186f17788ed15af69ce5b55) | PASS | PASS | Same fake-model, middleware and tool scenario completes |

### Evidence provenance

**Provider chain:** [initial AI-assisted PR #40530](https://github.com/langchain-ai/langchain/pull/40530) → [issue #40853](https://github.com/langchain-ai/langchain/issues/40853) → [provider fix PR #40864](https://github.com/langchain-ai/langchain/pull/40864). Actual core factory source was pinned at 80b740905 from the issue, because the initial attempt installing langchain 1.4.2 *from PyPI alone* did not contain the private repair function. The corrected CI used an editable install from the pinned upstream source, varying the provider adapter package version only.

**Routing chain:** [issue #38351](https://github.com/langchain-ai/langchain/issues/38351) → [fix PR #38355](https://github.com/langchain-ai/langchain/pull/38355). CI installed editable LangChain source from the pull request's documented pre-change and post-change commits and exercised the issue's fake-model and synthetic middleware scenario. Dependency subpackages were resolved at workflow execution time; a later reproduction should lock a complete dependency snapshot for publication.

**No external model API calls** were made. These tests execute actual framework code rather than our earlier dependency-free model. They use preknown historical failure inputs, not an unseen benchmark.

### Important failed first attempt (do not delete)

[Run #41456902263](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41456902263) failed from ImportError for _patch_invalid_tool_calls on the 1.4.2 PyPI package; it was an **invalid experimental setup**, not detection of the historical bug. [Corrected run #41457189971](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41457189971) pinned the source SHA and verified the provider defect. The final [four-job run](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41457528866) also tested the graph routing chain.

## Minimum plausible intervention: boundary contract checks (non-novel)

The changes can be checked with simple interface assertions:

1. **Message lineage:** every serialized tool_result must reference a preceding matching tool_use in that provider's outgoing message representation.
2. **Routing closure:** every router result reachable under the current middleware configuration must belong to the graph edge's declared destination set.

A hand-authored [test selector](../experiments/real_langchain_replay/test_selector.py) maps changed factory symbols to the appropriate check. Its six locally executed unit tests pass, but this mapping was created **after** viewing the postmortems. It proves only that a small interface is implementable; it is **not a generalization result**, nor a novel mechanism.

### Are strong existing methods shown to fail?

**Not yet.** What was measured: local functional behavior succeeded while cross-boundary behavior failed on two real historical revisions. We have NOT run or disproved a strong modern coverage-based regression-test selector, existing provider integration suites, differential MCP testing, structural agent testing, AgentAssay, or generic change-impact methods. Conventional integration tests might catch both defects with no new research algorithm. Do not frame the weak path-local selector as the best established testing baseline.

The examples show *that* such bugs exist, not their incidence rate, whether they disproportionately affect AI-generated changes, or how much automatic testing would prevent them.

## Next decisive research gate — must succeed before algorithm work

1. Define a **prospectively locked** test-selection method without seeing held-out postmortems, and obtain 8–12 independent confirmed bugs + 8–12 legitimate changes from several repositories/frameworks, spanning tool serialization, route labels, handoff state, approval/run binding, and other real contracts. License-check and independently reproduce each.
2. Record all relevant pre-change tests and their execution behavior, including full/affected-package/coverage-based selection at the original code revision. Use actual test coverage tracing when feasible.
3. Compare at equal total cost (test discovery + generation + execution + false alarms): full relevant integration suite, coverage/change-impact selection, static/trace/contract and differential baselines, and only then a proposed change-aware boundary method.
4. Use source snapshots BEFORE a bug fix when asking a method which contracts to test. Never expose the later fix or issue description to the selector. Audit leakage through filenames, training data, and test selection.
5. Evaluate defect recall, precision/false alarms, fault-severity weighted detection, human inspection and wallclock cost; hold out entire repository/failure families.
6. **Stop** algorithm novelty claims if ordinary dependency/coverage or established differential techniques catch these cases equally efficiently. No RL, world model or large agent architect until a genuine baseline-resistant deficit appears.

**Milestone verdict:** We now have a valid two-boundary, real-source *historical feasibility reproduction*. It is useful research infrastructure and a credible grounding example, but not yet evidence of a novel or superior automated method.
