# Real GitHub incident pilot — what failures actually occur?

**Dated:** 2026-11-02  
**Type:** Qualitative, purposively selected, *source-linked* issue/PR audit  
**State:** Real issue/PR documents collected and classified; NO issue reproduced by our own environment; NO LLM editing experiments; NO prevalence inference; NO new causal algorithm.

## Why this pilot was necessary

Prior literature-only discussions repeatedly treated "prompt overfitting" or "wrong evidence source" as the generic root cause of agent design regressions. The sample below checks what is actually reported in maintained agent frameworks. Cases originate from GitHub issue/PR pages in LangChain, LangGraph, OpenAI Agents SDK, and AutoGen. They were deliberately searched using terms for tool, routing, state, regression, and handoff defects and are **not a random sample**.

**Machine-readable case table:** [incident_pilot_2026-11-02.csv](../data/incident_pilot_2026-11-02.csv).

## A directly evidenced sequence: an AI-assisted fix triggers a cross-provider defect

1. [LangChain PR #40530](https://github.com/langchain-ai/langchain/pull/40530), **merged 2026-09-22**, describes an Open SWE / model-assisted repair: it adds synthetic error ToolMessages to make malformed tool-call histories resumable.
2. [LangChain issue #40853](https://github.com/langchain-ai/langchain/issues/40853), **opened 2026-09-27**, supplies a reproducible incompatibility: Anthropic serialization omits the matching parent tool_use for the synthetic tool_result. The issue specifically identifies the earlier repair as introducing this interaction.
3. [LangChain PR #40864](https://github.com/langchain-ai/langchain/pull/40864), **merged 2026-09-27**, is also identified as Open SWE / model-assisted. It adapts the Anthropic serializer so invalid tool calls have a matching tool_use and avoids duplicate IDs. A commenter later reports verifying the fix with a then-current package release.

**What is established:** a documented prior AI-assisted patch, an incompatible second serialization boundary, a subsequent merged repair, and relevant code/test/reproduction descriptions.  
**What is NOT established:** that an LLM specifically caused the mistake rather than author/reviewer/test coverage; that prompt instructions were overfit; production prevalence; a model-level success rate; that we independently reproduced all three revisions.

**Research implication:** a fix can pass a local repair rationale yet violate a neighboring provider-specific contract. This is a better-motivated test target than an artificially ambiguous complaint. However, a comprehensive integration test could catch it without a novel learning policy.

## Other cases and what they do — and do not — prove

| Case | Primary GitHub evidence | Provisional failure mechanism | Confidence and caveat |
| --- | --- | --- | --- |
| LC-02 | [LangChain #38351](https://github.com/langchain-ai/langchain/issues/38351) / [merged PR #38355](https://github.com/langchain-ai/langchain/pull/38355) | Route label produced by conditional edge lacked a declared destination, causing KeyError under synthetic tool-message middleware | Strong issue-to-merged-fix chain; deterministic API invariant rather than prompt overfitting |
| LG-01 | [LangGraph #9072](https://github.com/langchain-ai/langgraph/issues/9072) | Parent Command.update dropped when Send fan-out is reconstructed; later investigation also describes multiple-parent-command runner behavior | Runnable reporter reproduction; claimed production loop unverified; [PR #9303](https://github.com/langchain-ai/langgraph/pull/9303) was **not merged** and did not resolve all reported variants |
| LC-03 | [LangChain #36411](https://github.com/langchain-ai/langchain/issues/36411) | A failing return_direct tool could terminate loop despite error status | Open, reproducer described; [PR #36465](https://github.com/langchain-ai/langchain/pull/36465) **not merged** in inspected state |
| LC-04 | [LangChain #40422](https://github.com/langchain-ai/langchain/issues/40422) | Mixed structured-output and ordinary tool calls can trigger premature exit after invalid output | User-provided reproduction; issue auto-closed for issue-template metadata; **closed does not mean fixed** |
| OA-01 | [OpenAI Agents SDK #5413](https://github.com/openai/openai-agents-python/issues/5413) | Reused call IDs and stale approval object may transfer authorization between runs | Open; multiple users reported offline scripted reproduction when same Agent object reused; not independently reproduced |
| OA-02 | [OpenAI Agents SDK #5416](https://github.com/openai/openai-agents-python/issues/5416) | Async in-flight tool state not reflected in immediate interruption response | Open; reporter's controlled observations, not independently verified; distinguish *claims* of action completion from actual execution |
| OA-03 | [OpenAI Agents SDK #5443](https://github.com/openai/openai-agents-python/issues/5443) | Tool descriptions can unintentionally inherit stdlib/generated docstrings instead of intended callable documentation | Open; deterministic metadata-generation claim; no model behavior or regression measured |
| OA-04 | [OpenAI Agents SDK #1430](https://github.com/openai/openai-agents-python/issues/1430) | Possible orchestrator vs subagent tool exposure, context forwarding, or user configuration issue | Ambiguous question; **closed as stale**, no verified root cause |
| LG-02 | [LangGraph #6064](https://github.com/langchain-ai/langgraph/issues/6064) | User-wait/handoff ownership appears lost across turns under provided graph configuration | Closed question; proposed fixes are community commentary, not established library defects |
| AG-01 | [AutoGen #2893](https://github.com/microsoft/autogen/issues/2893) | A specific local model/tool setup reportedly invokes registered tools on unrelated tasks | Single report, model/config confounds; not evidence that a persistent editing patch caused regression |
| AG-02 | [AutoGen #7851](https://github.com/microsoft/autogen/issues/7851) | MCP tool errors reportedly abort a run; feature request for isolation | Proposal with concrete motivation, not an independently proven regression rate |

**Evidence taxonomy:** merged PR linked to a concrete issue > independently repeated offline reproductions reported by multiple users > single detailed reproducible report > ambiguous usage question > feature proposal. All require independent reproduction for strong causal claims.

## What we found — and what surprised us

**Finding 1 — Many reports are contract/implementation defects, not instruction overfitting.** The sample contains routing-map mismatch, invalid serialized messages, state-loss across handoffs, approval-run lineage, erroneous stop/error logic, and accidental tool metadata. Writing a longer system prompt is not a credible universal repair.

**Finding 2 — Evidence often crosses components and execution contexts.** PR #40530/#40853/#40864 is a concrete before/reported-regression/after sequence across a core repair and provider serialization. #9072 exposes a handoff-state path where the representation changes in transit.

**Finding 3 — Not all ambiguous issue reports are true latent-intent uncertainty.** #1430 is undecided partly because information/reproduction is insufficient. It cannot count as evidence for "stakeholder intention and technical cause jointly unknown" without additional validated data.

**Finding 4 — Repository state is not scientific ground truth.** GitHub "closed" may mean merged fix (#38351, #40853), automated template closure (#40422), or inactivity (#1430). A PR can claim Fixes while not merged (#9303, #36465).

**Finding 5 — We STILL have no direct dataset of repeated AI architect edits driven by successive *stakeholder requirement changes*.** These issues mostly concern framework implementation/runtime, so they do not establish the frequency or impact of the original "AI keeps adding edge-case prompt rules" problem.

**Finding 6 — New benchmark prior art covers the easier retention framing.** [EvoHarnessBench](https://arxiv.org/abs/2609.04280) evaluates fixed-model behavior under externally expanding pools of tools/skills/agents across 17 staged harness streams (802 unique tasks, 520 tools, 42 skills, 62 agents). It reports previously accessible competence degrading under harness expansion *even without self-directed edit optimization*. [Rethinking the Evaluation of Harness Evolution](https://arxiv.org/abs/2607.12227) warns that extra search compute and benchmark leakage can explain apparent harness-evolution improvements. Therefore distinguish (i) new capability burden, (ii) underlying runtime bug, (iii) editor choice and implementation, and (iv) evaluation artifacts.

## Updated gap decision

This pilot does NOT establish that ASK/PROBE/EDIT selection is the dominant problem. In several cases the right intervention is a deterministic integration/contract test, not human clarification, architecture search, or RL.

The **most useful surviving empirical question** is:

> For real persistent agent-design revisions, how often do negative outcomes arise from (a) misunderstanding stakeholder intent, (b) choosing the wrong edit surface, (c) cross-component contract interaction, (d) incomplete regression coverage, or (e) runtime and stochastic changes? And which can a strong existing editor + established testing already prevent?

This is a *hypothesis for a prospective study*, not a confirmed new research gap. The current issue sample illustrates categories but **cannot estimate their frequency**. Quantitative statements would be invalid due to purposive selection, repository concentration, unresolved cases and mixed evidence quality.

## What we should do NEXT: reproducible focused pilot

### 1. Reproduce the most informative real case (LC-01)

- Pin LangChain/LangChain-Anthropic at three points: before merged PR #40530; after #40530 but before #40864; after #40864.
- Run the original minimal malformed-tool-call replay with a fake model, tracking (a) required parent tool_use ID for every tool_result, (b) provider-specific serialization, (c) ability to resume the dialogue; avoid requiring API credentials where possible.
- Compare at least two provider adapters or their recorded protocol encoders; do not infer model accuracy from serializer validity.
- Write a minimal, independent contract test with the invariant "each tool_result references an emitted tool_use in the serialized transcript". Check it across edits.
- Determine whether the existing unit tests before #40864 covered the failure, rather than assuming "missing tests" without inspection.
- Record environment/version/dependencies and exact pass/fail output.

### 2. Build a small, non-anecdotal case collection

- Define a sampling frame upfront (e.g., 2026 merged PRs that modify prompts, tool descriptions, tool schemas, routing/handoffs, or persistence).
- Stratify across projects; sample *changes*, not only issues filed after failures; include successful changes to avoid survivorship bias.
- Pair source PR -> changed artifact -> subsequent issue or review/revert -> follow-up patch -> tests. Classify "caused by change" only when temporal, code and reproduction evidence jointly support it.
- Two independent reviewers label cases blind to the final hypothesis; adjudicate disagreements. Use cause categories as nonexclusive labels.
- Critically separate **model-generated changes**, human-reviewed/merged changes, and wholly human changes; do not infer causation from Open SWE attribution alone.
- Record whether regression was user-intent-related, technical-contract-related, or evidence/verification-related.

### 3. Test a baseline, not a new optimizer

Try a capable coding editor with the relevant source and same budget under:
- existing unit tests only;
- unit tests + cross-boundary protocol contract tests;
- unit tests + contract tests + explicit design/requirements document.

Measure *final held-out behavior* and cost. Use independent tests never accessible for repeated optimizer probing.

Only if a genuine residual failure survives should we investigate new cause-aware test selection, change-impact prediction, or a learned design policy.

## Predeclared negative outcomes

- If ordinary targeted integration tests catch the cross-provider regression, do **not** claim novelty for detecting it with an AI critic.
- If the cases mostly reflect SDK implementation defects rather than AI-generated edits under uncertain user requirements, do **not** claim intent-aware continual design as established by this evidence.
- If a strong editor + test suite solves the sampled problems, a new RL selector is unjustified.
- If no meaningful post-merge change-to-regression chains survive review, discontinue the regression prevalence hypothesis or broaden data sources before making causal claims.
- If gains are not cost-effective over future task horizons, prioritize ordinary repair instead of evolving a reusable harness.

**Conclusion:** This pilot uncovered one well-linked AI-associated cross-component regression chain and multiple plausible contract/hand-off defects. It narrows, rather than confirms, the research gap. It justifies reproducing LC-01; it does not justify publishing a first-of-its-kind optimizer.
