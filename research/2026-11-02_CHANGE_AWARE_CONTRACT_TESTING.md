# Research pivot: change-triggered cross-boundary contract verification

**Date:** 2026-11-02  
**State:** conceptually motivated, existing literature overlaps strongly; a **dependency-free synthetic witness ran** (8/8 unit tests); **no real-package reproduction or LLM/baseline evaluation**.  
**Original objective:** assist a developer with continually improving a working agent design's prompts, tool contracts, routing and state without accidental changes in unrelated behavior.

## Result of the new search

Earlier ideas—RL design policy, decision-region evidence selection, evolving-spec benchmarks—have substantive precedents. A different evidence-driven direction appeared from *real agent application testing practices* and one verified historical PR/issue/PR chain: **after an edit, identify which producer-consumer interface obligations were affected, and run discriminating integration checks before accepting a persistent agent change**.

This is **NOT** a claim that agent unit tests, contracts, property tests, differential tests, metamorphic tests, mutation tests or test selection are new. The *possible* narrow gap is **change-conditioned selection and prioritization of cross-component executable assertions** at a fixed budget, and whether that approach catches *historical edit-induced regressions* at low cost.

## Most decisive new literature (primary-source links)

| Work | What is already established | Consequence for novelty |
| --- | --- | --- |
| [Tangent (ASE 2026)](https://arxiv.org/abs/2608.08413); [IBM summary](https://d3ccyth396mz21.cloudfront.net/publications/tangent-an-empirical-study-of-testing-practices-for-llm-based-agent-applications) | Manual coding of 2,572 tests / 240 modules, 23 testing patterns and 10 industry interviews: agent tests dominated by mocked unit-level cases, missing realistic interactions. | Provides independent empirical need, not a new mechanism. |
| [Grounding AI Agents in Contracts (SpecOps 2026)](https://research.google/pubs/grounding-ai-agents-in-contracts-an-empirical-evaluation-of-spec-driven-test-generation/) | Explicit preconditions/postconditions guide LLM test generation on Google production bugs. | No novelty for spec-first test generation. |
| [Automated structural testing of LLM-based agents](https://arxiv.org/abs/2601.18827) | Trace-first structural assertions, mocked reproducible agent execution, component tests. | No novelty for structural agent testing or trace assertions. |
| [AgentAssay (March 2026 technical report)](https://arxiv.org/abs/2603.02601) | Agent-specific mutants, metamorphic relations, adaptive statistical regression gate, behavioral fingerprints. | Strong competitor for agent-specific mutation + cost optimization; its claims are author-reported. |
| [MorphAgent (AITest 2026)](https://ieeexplore.ieee.org/abstract/document/11662476/) | Trace-based metamorphic relation checking of inter-agent interaction across benchmarks. | No novelty for metamorphic multi-agent checks. |
| [SGVEF-LOOP (ACL 2026)](https://aclanthology.org/2026.acl-long.1224/) | Coverage-driven topological exploration and metamorphic testing of MCP agents. | No novelty for coverage-guided tool graph exploration. |
| [Localizing Post-Wire Semantic Changes in MCP Agent Frameworks (Sep 2026)](https://arxiv.org/abs/2610.00182) | Differential test of consumer-visible semantic preservation through agent framework interfaces, 18 fixtures and 4 Python integrations. | **Most damaging nearby work**: directly tests semantic contract boundaries. Our proposed approach must differ in *edit-conditioned selection* and real regression-prevention evaluation. |
| [Action-Space Shaping / Tool-Schema Bias](https://arxiv.org/abs/2609.34971) | Same executable tool actions exposed through different schemas can strongly alter LLM performance; 9 operators and 11 models. | Interface invariance is itself an existing studied phenomenon. |
| [The Devil Is in the Interface](https://www.microsoft.com/en-us/research/publication/the-devil-is-in-the-interface-evaluating-how-tool-architecture-shapes-coding-agent-behavior/) | Controlled study of coding-agent tool architectures across 11,700 trajectories. | No novelty in measuring effects of tool interface design. |
| [SWE-Mutation (Findings ACL 2026)](https://aclanthology.org/2026.findings-acl.1976/) | Agent-generated complex mutants that fool test suites at repository level. | Mutation-generated test adequacy not new. |
| [Test-Aware Mutant Generation (ESEM 2026)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.49) | Generates mutations that survive existing base tests, verified on HumanEval/MBPP. | Test-aware mutation / hidden fault discovery is established. |
| [Evaluating LLM-Based Test Generation Under Software Evolution (2026)](https://arxiv.org/abs/2603.23443) | Evaluates LLM-generated test behavior over semantic and nonsemantic code changes. | Evolution-sensitive test evaluation is established. |
| [PRISM (Findings EMNLP 2026)](https://aclanthology.org/2026.findings-emnlp.1455/) | Failure-surface routing and prompt/tool-boundary middleware optimization; held-out improvements. | Repair-surface choice is established. |
| [Multi-Agent Change Impact Analysis / Test Optimization (2026)](https://ieeexplore.ieee.org/abstract/document/11662363) | Structural, semantic, retrieval and risk signals for budgeted test selection. | **Strong generic selection competitor**. Must match same budget and signal access. |

**Research posture:** The ingredients are prior art. The scoped search found a real, specific empirical question worth testing, NOT a demonstrated novel algorithm.

## Actual empirical anchor from GitHub PR history

- [LangChain PR #40530](https://github.com/langchain-ai/langchain/pull/40530) merged **2026-09-22**. The AI-assisted patch added a synthetic error `ToolMessage` for invalid tool calls in `create_agent` and unit tests in `test_invalid_tool_calls.py`.
- [Issue #40853](https://github.com/langchain-ai/langchain/issues/40853) filed **2026-09-27**. Reporter supplied an offline reproducer: after the patch, Anthropic received an outbound `tool_result` without an earlier matching `tool_use`. The initial tests did not establish provider serialization compatibility.
- [LangChain PR #40864](https://github.com/langchain-ai/langchain/pull/40864) merged **2026-09-27**. Added missing `tool_use` for invalid tool calls in `langchain_anthropic/chat_models.py` and tests confirming provider-level pairing and no duplicate IDs.

**Important:** A bug was reported and fixed, but the audit does not prove that a model rather than the overall development/review process caused it, nor that the original patch overfit prompts.

### Executable minimal witness — actually run in this investigation

Path: [experiments/change_aware_contracts/](../experiments/change_aware_contracts/). Uses Python standard library only. It is a **small synthetic model of the documented protocol behavior**, NOT the real LangChain implementation or a real provider API call.

Run:

```sh
cd experiments/change_aware_contracts
python -m unittest discover -v
python protocol_witness.py
```

Run result from 2026-11-02: **8/8 tests passed.** The witness's before-repair stage does not produce an orphan `tool_result`; the local-repair stage passes a unit assertion but fails the cross-provider contract with one orphan; the provider-fixed stage passes both. Unit tests check this expected *difference*.

| Synthetic state | Local repair check | Wire contract | Orphan result count |
| --- | --- | --- | --- |
| Before repair | Not applicable | Pass | 0 |
| Central local repair, provider unchanged | Pass | **Fail** | **1** |
| Central repair + provider fix | Pass | Pass | 0 |

The witness establishes only that the interaction invariant can discriminate the three designed states and that a local success check is insufficient in this specific abstraction. **It cannot establish empirical prevalence, effectiveness against real framework versions, missed bugs in live LLM agents, or new method novelty.**

## Candidate study: EDIT-EDGE (working label only)

**Research question:** Given a proposed persistent edit to a tool-using agent, can we automatically select the most useful *consumer-observable cross-boundary assertions* (and their tests) from the changed producer's affected edges, and do so more efficiently than strong existing baselines under identical test and execution budgets?

Distinguish the three tasks:
1. **Changed behavior scope**: producer changes messages, schemas, side-effect permissions, routing outputs, handoff state or tool-execution semantics.
2. **Consumer requirements**: downstream adapter's expectations about IDs, ordering, error flags, schema fields, state durability, permissions and acceptable evidence of completion.
3. **Executable mutation/check**: generate a synthetic or source-grounded affected-edge case, assert preservation of current obligations, and run a pinned real integration in an isolated sandbox.

A simple baseline can get much of this by static type checking and interface tests; do not assume an LLM is required. A legitimate research contribution must show that an edge-aware selection method exposes real defects missed by cheap strong comparators.

### Measured outcomes for a paper

- True historically grounded post-edit cross-boundary regressions detected *before* admission (as determined by independently reproduced defect chains).
- False alarms on correct changes / unchanged valid paths.
- Tests run, runtime, LLM token spend and human review cost at matched budgets.
- Cases where ordinary unit tests, all existing integration tests, general test-generation, change-based test selection, structural agent testing, AgentAssay-like mutation or MCP post-wire differential testing would catch the same defect.
- Transfer to entire unseen frameworks/application families; not just similar serialization bugs.

### Strong baseline suite (must be fair)

A. Existing tests run in CI, plus conventional affected-package test selection.  
B. Generic LLM-based integration test generator at same rollout/test budget.  
C. Existing structural/trace assertion and property-based test strategy.  
D. Differential post-wire testing à la Patodiya, with matched consumer requirements.  
E. Generic change-impact and mutant-oriented test selection under matched cost.  
F. Candidate change-aware edge-obligation selection, ablated without diff or consumer-obligation information.  
G. Exhaustive relevant integration tests (cost ceiling, not necessarily deployable).

**Kill gates:**
- If D/E match F at same cost and defect detection, no new method paper.
- If the benchmark consists mainly of our own injected bugs, no externally valid production-regression claim.
- If contracts require bespoke human effort for each case and dominate claimed savings, report total cost; the method may not scale.
- If findings do not transfer beyond provider message serialization, restrict the claim to that domain.
- If ordinary vendor contract tests suffice, build those tests instead of an ML optimizer.
- If no agent-specific difference from generic software contract regression remains, the topic is standard SE; label it accordingly.

## Next 3 executable milestones

1. **Real upstream reproduction:** Pin source and dependencies at PR #40530 and #40864 parent/merge SHAs, run the actual reporter's offline script from issue #40853, and record Python, package versions, outcomes, and logs. Current synthetic witness is NOT a substitute.
2. **Add real independent failure families:** route mapping [LangChain #38351 / PR #38355](https://github.com/langchain-ai/langchain/issues/38351), state fanout [LangGraph #9072](https://github.com/langchain-ai/langgraph/issues/9072), and approval-run lineage [OpenAI Agents SDK #5413](https://github.com/openai/openai-agents-python/issues/5413). Do not claim causal reproductions from open issues; validate before including.
3. **Empirically compare B/D/E/F**, with a predeclared fixed test-cost budget and actual PR-paired legitimate changes as negative controls. Only then decide whether to invest in LLM-generated edge assertions.

**Decision:** This is the strongest grounded route identified during the current turn, because it starts from a published empirical shortage of realistic agent tests and an inspectable historical cross-boundary regression. Its algorithmic novelty remains **UNKNOWN / high-risk**. Prior proposed generic architect/VOI/longitudinal benchmark novelty claims remain rejected.
