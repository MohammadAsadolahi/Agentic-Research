# Research state and decision log

> **ADVERSARIAL NOVELTY VERDICT (2026-11-02):** [Deep audit](2026-11-02_ADVERSARIAL_NOVELTY_VERDICT.md) identifies a decisive old mathematical precedent: Javdani et al., **AISTATS 2014**, decision-region determination (DRD/HEC), already selects tests that separate hypotheses only enough to choose an acceptable decision. Thus **repair-disagreement-guided ask/probe is NOT a novel decision principle**. CONTRA, SAGE-Agent, CAMP, DAAF, KPHarness, ASE 2026 authority APR, ReqClarifyBench/SWE-Clar, RECAP/EvoHarnessBench and Iter-T/CoHarden further constrain novelty. **No algorithmic novelty established; at most a high-risk, narrowly scoped joint longitudinal empirical/benchmark gap remains.** This supersedes the optimistic interpretation of the candidate below.

> **Focused candidate (2026-11-02):** [Repair-decision identifiability](2026-11-02_REPAIR_DECISION_IDENTIFIABILITY.md) is now the leading *untested* novelty hypothesis. The proposed method selects evidence based on disagreement among authorized durable repairs under uncertain stakeholder intent and technical causes. CONTRA, FixedBench, ImpasseBench, DAAF, DoVer, KPHarness and counterfactual repair work already establish most individual mechanisms; only a new combined protocol plus demonstrated baseline-resistant algorithm could justify novelty. **No algorithmic results yet.**

> **Evidence pilot (2026-11-02):** We inspected 12 purposively sampled GitHub issues across major agent frameworks and identified a concrete linked AI-assisted patch/regression/fix chain: [LangChain PR #40530](https://github.com/langchain-ai/langchain/pull/40530) → [issue #40853](https://github.com/langchain-ai/langchain/issues/40853) → [PR #40864](https://github.com/langchain-ai/langchain/pull/40864). Many other reports are deterministic cross-component contract defects, not evidence of prompt overfitting. [Read pilot](REAL_WORLD_INCIDENT_PILOT_2026-11-02.md). **No independent issue reproduction or baseline experiment has been run.** Next milestone: reproduce the cross-provider sequence and audit a less-biased sample of revisions.

> **Further adversarial audit (2026-11-02):** DAAF, DoVer, KPHarness, SAGE-Agent, Drift-Bench++, SpecPath, and related work eliminate almost every generic mechanism we previously proposed. The remaining candidate is a *joint decision/evaluation problem*: when a failure report underdetermines **both** stakeholder intent and technical cause, should an AI systems architect ask, probe, edit, retain, or escalate before making persistent changes? **This is not an established novel algorithm.** See [gap-discovery audit](2026-11-02_GAP_DISCOVERY_LOOP.md). Prior priorities below are historical; do not treat them as confirmed novelty.

> **Important new reassessment (2026-11-02):** The latest literature review adds direct empirical evidence from Treude & Baltes (Oct 26), SLUMP/ProjectGuard, StateHarness, BenchTrace, ModularRSI, HarnessFix, and IEEE change-impact research. These further weaken novelty claims around structured project memory, scoped failure diagnosis and impact-aware test selection. **Read [Critical reassessment](2026-11-02_REASSESSMENT.md) before starting an algorithm or writing a novelty claim.** Original hypotheses below remain a historical research log, not an assertion of unresolved novelty.


**Last updated:** 2026-11-02  
**Stage:** problem clarification and prior-art audit; empirical study NOT started  
**Current novelty confidence:** LOW for the original broad idea; UNDETERMINED for the narrowly stated hypotheses.

## 1. The actual problem (do not lose this)

We want a *conversational AI systems architect*. A developer describes an incomplete idea, and over a series of conversations the system helps discover intended requirements, challenges unnecessary complexity, designs agent roles, prompts, tools, interfaces, workflow stages, and failure policies. Later, after an observed failure or new requirement, it should adapt the design without turning one example into an unconditional rule or silently damaging unrelated behavior.

This is NOT simply:
- an agent orchestration SDK such as LangGraph;
- a CLI that implements a preselected architecture;
- a prompt rewriter optimized on a small visible dataset;
- a system that assumes the user already knows the agent decomposition.

The original pain point is AI coding agents editing existing prompts and tools to satisfy the most recent complaint, producing edge-case rules, prompt bloat, altered examples, and degraded generality. **This is the motivating observation, not yet our measured scientific finding.**

## 2. Research framing and vocabulary

Distinguish three objects:
1. **Intended specification:** what the developer actually means, including approved requirements, accepted changes, priorities, uncertainties, prohibited behavior, and who may resolve conflicts.
2. **System design:** prompts, tool descriptions and implementations, schemas, routing, agent topology, state and recovery logic.
3. **Evaluated behavior:** real outcomes of generated/edited agents under tasks, tools, state, models, and environment changes.

Two policies are conceptually possible: an **execution policy** performs user tasks, while a **design policy** proposes revisions to the system implementing the execution policy. This is a valid optimization framing, not a claim of novelty. A scalar reward is an incomplete proxy for future intended behavior; a score-predicting model is a *surrogate* unless sequential world dynamics and planning value are established.

Distinguish an **observed failure** from a **new approved requirement** and from **supersession** of an old requirement. Retaining an obsolete behavior is not successful preservation.

## 3. Findings we currently accept

### F1. General systems already design and evolve agent architectures

Tressoir (ACM CAIS 2026) proposes human-readable interpretable blueprints covering prompts, architecture, tools and invariants, online/offline adaptation, and human feedback. Meta Agent Search (ICLR 2025) and related automated design methods search over agent programs. Therefore "an AI designs agent workflows/tools/prompts from a blueprint" is not novel on its own.

### F2. Learned optimization policies and performance surrogates already exist

COMPASS (REALM 2026) trains a metapolicy to improve prompts from reward and critiques. MESH-Harness (October 2026 preprint) uses a LinUCB-based bandit and surrogate representations to optimize recombinations of modules within fixed interfaces. GEPA (ICLR 2026) uses language reflection and evolutionary search. "Apply RL/bandits/world-model-like prediction to agent design" is not new by itself.

### F3. Regression-safe optimization and targeted repair are also prior art

PRISM (EMNLP Findings 2026) routes failure repairs to prompts, tool middleware, or both. GRASP (EMNLP 2026) uses held-out acceptance and regression budgets for skill edits. The continual-optimization study "Do Agent Optimizers Compound?" (2026 preprint) investigates whether repeated improvements retain previous capabilities. Adding a regression suite to a search loop is therefore not a new algorithm.

### F4. Overfitting and poor transfer are substantiated risks

PROSE (EMNLP Findings 2026) studies shortcut learning in prompt optimization. Harness-Delta Attribution (October 2026 preprint) found substantial search-set gains explained by overfitting and test-time computation *in its reported significant-gain subset*. RECAP (EMNLP 2026) tested proactive adaptation under changing constraints and found no significant overall improvement among six evaluated methods. These results motivate measurement, not an assumption that our preferred design will work.

### F5. Prediction of change effects is already partly studied

CHIVE (2026) uses real counterfactual prompt edits and studies models trained to predict behavioral effects; AHE (2026 preprint) records proposed harness changes and predictions checked against later results. A predictive "world model" of edits alone is not sufficient novelty. The possibly narrower gap is calibration and intervention selection across interacting components and changing requirements — NOT YET ESTABLISHED.

### F6. Human-facing architects exist, but production-quality evidence is uneven

The GitHub agent-architecture skill explicitly supports requirements discovery, architecture audit, and design checks, but not implementation. BMad Builder and AutoAgent generate agent/workflow artifacts in various ways. They are product precedents, not substitutes for an independent quality study; see PROJECTS_AND_FEEDBACK.md.

## 4. What is already covered versus still uncertain

| Claim or capability | State |
| --- | --- |
| Automatically optimizing prompts | Established |
| RL-trained metaprompt generator | Established (COMPASS) |
| Bandit-guided modular harness search | Established (MESH-Harness) |
| Blueprint-based conversational agent evolution | Substantial precedent (Tressoir) |
| Prompt-versus-tool middleware repair selection | Established (PRISM) |
| Regression-gated incremental improvement | Established in related settings (GRASP, continual optimization) |
| Counterfactual prediction of prompt changes | Established in a related setting (CHIVE) |
| Reliable intent-aware handling of failure vs requirement change vs supersession across whole agent systems | Candidate gap; evidence incomplete |
| Calibrated cross-component regression prediction for prompt/tool/topology edits | Candidate gap; evidence incomplete |
| Generalization across held-out agent *applications* and many sequential design revisions | Evaluation gap to test; cannot assert absence |
| A single industrially validated general-purpose autonomous agent architect with strong preservation guarantees | Not established by this scoped investigation; **not proven nonexistent** |

## 5. Current candidate research questions (hypotheses, not contributions yet)

**RQ1 / Intent-aware adaptation.** Does representing the uncertainty and authority behind incoming design feedback (failure observation, correction, requirement addition, supersession) reduce unjustified edits and unintended regressions beyond a strong LLM editor with the SAME regression tests?

**RQ2 / Cross-component impact.** Can explicitly modeling dependencies and collecting controlled intervention traces predict which accepted behaviors will regress when editing prompts, tool contracts, or topology better than a code diff, trace-based critic, and conventional test selection?

**RQ3 / Evaluation validity.** How much of an apparent improvement in AI-assisted agent design is explained by task-family leakage, test contamination, altered evaluator semantics, or additional test-time computation? Does it persist after multiple independent revisions?

**RQ4 / Transfer (high novelty risk).** Does a learned intervention policy add value on entire withheld application families beyond retrieved design examples and a strong LLM selector?

Priority: investigate RQ1 and RQ2 empirically; RQ3 is essential methodology. Do NOT pre-commit to RQ4 or to RL.

## 6. What we must NOT claim

- "First AI agent architect" or "first system to jointly design prompts, tools, and topology."
- "First RL-based agent-design policy," "first contextual-bandit harness optimizer," or "first world-model-guided optimization."
- "First regression-aware continual agent optimizer."
- "Adding structured specifications automatically solves prompt overfitting."
- "A better benchmark score implies real generalization" without held-out and compute-attribution checks.
- "Current projects do not exist" because no one project satisfies every wish-list requirement.
- "Guaranteed non-regression": finite tests cannot guarantee semantic correctness for unseen open-domain inputs.

## 7. Dated decision record

| ID | Date | Decision | Reason / reopening condition |
| --- | --- | --- | --- |
| D-001 | 2026-11-02 | Focus on an AI **designer** rather than an execution framework | Original user need concerns discovering architecture, prompts, and tools. |
| D-002 | 2026-11-02 | Treat design intent separately from prompts and implementations | Needed to distinguish legitimate change from drift; not asserted as novel. |
| D-003 | 2026-11-02 | Reject broad RL / world-model novelty pitch | COMPASS, MESH, prior architecture search and surrogate methods overlap. |
| D-004 | 2026-11-02 | Reject "add regression tests" as standalone novelty | PRISM, GRASP, RECAP and continual agent-optimizer work overlap. |
| D-005 | 2026-11-02 | Prefer causal, falsification-first analysis before proposing an optimizer | Need to identify which failure existing methods leave unresolved. |
| D-006 | 2026-11-02 | Preserve independent, locked acceptance tests | Candidate generator should not be permitted to silently modify its judge. |
| D-007 | 2026-11-02 | Compare equally informed simple baselines before complex training | If a specification plus tests works, RL/world models may not be warranted. |
| D-008 | 2026-11-02 | No claim of empirical success or confirmed paper novelty | No controlled experiments have been run by this project. |

## 8. Immediate next actions

1. Build an evidence spreadsheet/table for each nearest paper: exact search space, target tasks, training feedback, baselines, splits, costs, held-out distribution, limitations, and code availability. Prioritize Tressoir, PRISM, AHE, GRASP, CHIVE, RECAP, MESH, COMPASS, HDA.
2. Reproduce or at least run a small controlled revision task with a plain coding agent and regression tests; collect actual failure cases.
3. Prepare a dataset of genuine requirement changes versus local failure reports; label intended supersessions.
4. Pre-register evaluation criteria and select independent held-out task families.
5. Execute experiment conditions A–D in EXPERIMENT_PLAN.md, then decide whether an additional learned policy (E) is justified.
6. Update this state file whenever an experiment or new paper changes a decision.

## 9. Evidence and uncertainty policy

"Checked" in PRIOR_ART.md means a primary publication page was re-opened or found during this documentation pass; it does NOT mean independently reproduced. Other papers and product/user reports from earlier conversations remain useful leads but require direct rechecking. Details such as current stars, deployment adoption, bug status, and comparative performance should never be asserted without a dated source. This is a living working log, not a completed systematic literature review.
