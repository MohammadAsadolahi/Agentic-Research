# Second adversarial audit: does the remaining longitudinal benchmark gap survive?

**As-of:** 2026-11-02  
**Result:** **NO-GO as a broad new longitudinal benchmark or as a new evidence-selection algorithm.** A highly scoped **agent-architect intervention-decision study** remains an *unconfirmed* empirical possibility. No method implemented, controlled trials run, or unique algorithm established.
**Method:** targeted searches across coding evolution, specification/clarification, agent harness/architecture evolution, benchmark integrity; primary paper HTML inspected where available, linked GitHub readmes checked. This is a scoping audit, not an exhaustive systematic review.

## Executive correction

Our previous narrative treated three benchmark properties as potentially distinctive: (i) persistent edits across sequential requests; (ii) changing/superseded stakeholder requirements, with only still-active obligations counted; (iii) locked regression tests. **They are NOT distinct.**

[**EvoCode-Bench (May 22 2026)**](https://arxiv.org/abs/2605.24110) does *all three in detail*, plus explicit correction/conflict cases, authors' review of active obligations, contract/document-driven styles, and continuous workspace evaluation. [Primary HTML](https://arxiv.org/html/2605.24110v1) §3.1–3.4, Appendix B.5. Its reported sample has 26 tasks, 227 rounds, 5–15 rounds each, with 3 spec-evolution tasks / 22 rounds. Its main protocol is fail-stop and fixed-script rather than adaptive ask/probe. **We must not cite cumulative tests or supersession as originality.**

[**FeatureArc (Oct 27 2026)**](https://arxiv.org/abs/2610.37434) evaluates 73 human-reviewed same-feature histories of 2–10 stages with validated new-behavior F2P and previously-correct P2P tests, using the agent's OWN evolving code. Under its L4 protocol, the user provides new stages but no feedback on prior failures or rollback. Reported pooled success falls from 62.7% first-stage to 28.5% whole-feature, but these are their results, not replicated.

[**TDAD (Mar 9 2026)**](https://arxiv.org/abs/2603.08806) already compiles tool-using *agent prompts* from behavioral specifications with visible/hidden tests, semantic mutation, and v1→v2 spec evolution retaining held-out prior invariants. Its four-agent-spec, 24-trial experimental scale limits generalization, but it eliminates the claim that agent prompt design with spec evolution, anti-gaming, and regression checks is new. [Code](https://github.com/f-labs-io/tdad-paper-code).

Further direct prior art: [SWE-Milestone (ICML 2026)](https://proceedings.mlr.press/v306/deng26d.html) has executable milestone DAGs, preserved workspace and error accumulation; [LoopsBench (2026)](https://arxiv.org/abs/2608.00267) has 112 long-horizon tasks and >5,300 development units with independent persistent regression obligations; [EvoWeb (Oct 2026)](https://arxiv.org/abs/2610.16402) contains 320 cumulative requests across 32 browser-tested applications; [EvoHarnessBench](https://arxiv.org/abs/2609.04280) covers expansion of tools, skills and agents under retained task evaluation.

## 1. Competitive evidence table (originality relative to our proposed benchmark)

| Existing work | Sequential evolving artifact? | Requirement correction/supersession? | Locked/independent retention evaluation? | Agent-specific design modification? | Interactive intent/technical diagnosis? |
| --- | --- | --- | --- | --- | --- |
| EvoCode-Bench (preprint) | YES, one workspace 5–15 rounds | YES, correction/conflict and active-spec tracing | YES, cumulative independent verifier | General program, sometimes agent software; NOT architecture-oriented by construction | NO adaptive ask/probe; scripted rounds |
| FeatureArc (preprint) | YES, same-feature history | Extensions of same feature, contracts | YES F2P/P2P, whole-chain gate | General software features | NO prior-stage feedback or live clarification |
| TDAD (preprint) | v1→v2 prompt | YES, changed policy and new branches | YES hidden prior invariants | YES agent prompt/tool descriptions; limited topology implementation | Assumes supplied specification |
| SWE-Milestone (ICML) | YES, milestone release trajectories | Changing feature requirements | YES F2P/P2P | General software | NO special authority-aware ask/probe |
| LoopsBench (preprint) | YES, dependency DAG | Mainly incremental development | YES watcher and maintained regression obligations | General coding loop | NO requirement-authority decisions |
| EvoWeb (preprint) | YES 10 requests per web app | Cumulative features | Browser functional and integration checks | Web app | No technical diagnostic channel selection |
| EvoHarnessBench (preprint) | YES staged harness tools/skills/agents | Harness expansion, not human contract supersession | YES previous-cohort retention | YES harness, but externally controlled exposure | NO interactive intent + cause decision |
| SWE-Interact (preprint) | YES, multi-turn repo coding | YES iterative new constraints | Task-level evaluation | General codebase | YES simulated user; not explicitly agent-architect repair decisions |
| ReqClarifyBench (preprint) | Pre-coding dialogue | Simulated persona requirements can change | Requirement-document/code evaluation | General app | Clarification, not persistent agent-system maintenance |
| SWE-Clar (preprint) | Clarify then implementation | Original client requirements incomplete | Independent understanding/implementation assessment | General app | Clarification, not post-release agent design |
| SpecPath (preprint) | Equivalent requirement histories | YES active contract varies by revision path | Paired verifier | General software | No active diagnosis action selection |
| Tressoir (2026) | Agent blueprints and evolution | Human-guided spec/feedback | Golden cases and invariants as architectural parts | YES prompts/tools/workflows | Partial human-in-loop; need full text for exact protocol |
| PRISM (Findings EMNLP 2026) | Harness optimization search | Fixed selected evaluation tasks | Held-out reliability, repeatability/cost | YES prompt/middleware | Failure-surface diagnosis; no arbitrary architecture |
| PULSE (ICML 2026) | Evaluates agent design choices | Not sequential requirement history | Real human satisfaction / ML pseudo-label | YES design choices | Measures actual user response, not permission to edit |

**Caution:** broad YES/NO labels summarize paper-defined protocols, not full reproduction. Even if no row contains every column, that **does not** prove novelty for the conjunction.

## 2. Important new evaluation-integrity discovery

The [EvoCodeBench repository README](https://github.com/UniPat-AI/EvoCodeBench) states that **June 20 2026** results re-release **superseded** previous results. The team found an evaluation-integrity leak in Harbor's shared verifier mode (agents could access grader code in their turn), one contaminated task, and **11** task/test defects; reran evaluations under a patched harness. The legacy paper runner and original MT@4/SR results are kept for reproducibility. Do **NOT** indiscriminately combine arXiv v1 paper scores with current leaderboard as though same experiment; cite exact version/harness and re-release note. This is direct primary developer documentation, not independent replication.

A new benchmark claiming independence must pass an actual **read-permission audit** (can agent see tests, gold labels, or oracle files?), leakage probes, reference-suite QA, and differential evaluation across changes. Merely writing "hidden test" in an experiment plan is insufficient.

Other methodological threats: [Rethinking the Evaluation of Harness Evolution](https://arxiv.org/abs/2607.12227) and [Harness-Delta Attribution](https://arxiv.org/abs/2610.22466) warn that search/validation contamination and extra inference-time compute can mimic generalization. [PULSE](https://proceedings.mlr.press/v306/chen26da.html) demonstrates that human satisfaction with agent design can disagree with benchmark performance.

## 3. Why our remaining generic claims are not novel

- **"Longitudinal evaluation with same workspace":** EvoCode-Bench, FeatureArc, SWE-Milestone, LoopsBench, EvoWeb.
- **"Preserve only still-approved requirements, not deleted/overridden rules":** EvoCode-Bench explicit change-types + active contract auditing and cumulative verifier updates; SpecPath.
- **"Hidden tests and safe prompt revisions":** TDAD.
- **"Interactive goal discovery under changing requirements":** SWE-Interact, ReqClarifyBench, SWE-Clar, CONTRA/SAGE-Agent.
- **"Design an agent's prompt/topology/tool APIs":** Tressoir, MASS, ADAS, PRISM and MESH.
- **"Question vs probe based on different optimal repairs":** Javdani et al. decision-region determination, AISTATS 2014; DoVer/SAGE/DAAF/KPHarness.
- **"A benchmark of tool failure/agent recovery and regeneration":** agent evaluation/recovery benchmarks already abundant.

Do NOT claim that a combination automatically constitutes a first scientifically novel benchmark.

## 4. What precisely MAY survive (and its strongest objection)

**Question:** Is there a measurable failure specifically in **persistent agent-architect intervention decisions**—deciding whether to change a stage prompt, a tool description/implementation, routing, topology or deterministic middleware—when the evidence could refer either to a new *authorized* behavior requirement or a technical incident?

Specific unit: (a) existing runnable *agent application*, with actual prompts/tools/state/routing artifacts; (b) a complaint, trace, and versioned authority-approved obligation set; (c) a choice among ask/probe/edit/no-change/escalate; (d) same design used through further revisions; (e) independently executable per-obligation acceptance cases.

This would be stronger than treating a general coding feature change as an "agent design" change, but **its validity depends on whether the change choice and cross-component effects are an empirically distinct, difficult construct**.

**Falsifier A:** Run simple off-the-shelf coding/agent-design editors with the same tools and independent tests on a small carefully selected set. If most changes are caught by ordinary integration/regression tests, specialized agent-design evaluation adds limited insight.

**Falsifier B:** Compare against Tressoir-like blueprint updating + PRISM-style prompt/tool diagnosis + a strong general coding editor. If the candidate setting does not expose novel failure mechanisms or meaningful ranking changes, the remaining "gap" is product integration only.

**Falsifier C:** If a claimed novelty is just decision-aware active information acquisition, adapted DRD/HEC is a correct baseline and likely the whole mechanism. Don't pitch it as new RL.

**Falsifier D:** If stakeholder intent is always the same as scripted instruction labels, apparent uncertainty is synthetic. Obtain actual human-labeled ambiguity or show hard behavioral variation across independently validated contracts.

**Falsifier E:** If a benchmark must construct wholly artificial hidden worlds with deliberately different gold repairs, any success could be a byproduct of author-created puzzle structure. Include authentic incidents and varied acceptable repair sets.

**Falsifier F:** If the novel metric is only pass/fail over cumulative tests, EvoCode/FeatureArc already cover it. Need a substantively new endpoint, such as *correct architecture-change decision at matched downstream reliability and authority constraints*, justified empirically.

**Verdict:** This is *not* enough for a standalone high-confidence paper yet. It is a **small-scoped feasibility hypothesis**, not evidence of an unoccupied topic.

## 5. Better research strategy than authoring another benchmark from scratch

The shortest credible path is **targeted replication + augmentation**:

1. **Choose a released benchmark and freeze its version** (EvoCode-Bench post-2026-06-20 corrected harness or TDAD code and test suites); inspect license, dependencies, accepted task tests, and whether agent can access the verifier.
2. Pick 2–3 existing tool-using agent applications, including one reproducible cross-provider contract regression based on [LangChain #40530 → #40853 → #40864](https://github.com/langchain-ai/langchain/issues/40853) and one explicit stakeholder-intent change.
3. Build **one short intervention decision set** rather than a brand-new giant benchmark. Include ordinary fix, provider incompatibility, obsolete complaint, approved supersession, and truly ambiguous intent. Preserve alternative valid patches.
4. Compare baseline (strong LLM editor+tests), (same with approved spec), (composed clarification+probe+testing), and (agent-design-specific decision protocol). Keep tools, tokens, generated candidates and evaluation spend matched.
5. Human-verify original and amended requirements; have independent annotators label original issue and acceptable outcomes; avoid relying solely on AI-created hidden worlds.
6. Report two outcome families: (i) architectural decision correctness, including unnecessary changes and downstream side effects; (ii) task outcome under still-applicable contract. Use blinded evaluator and per-obligation traces, not only self-reported "thoughts".
7. Reuse the existing benchmark harness wherever feasible; do NOT report invented model results or presume a novel algorithm.
8. **NO-GO** if there is no meaningful new failure taxonomy, ranking reversal, or baseline-resistant error. **GO** only if a reproducible, independently judged residual mechanism appears.

**This is an empirical study proposal, not a certified new ML research contribution.**

## 6. Researcher's bottom line

- **NO-GO:** "First benchmark for agent revisions with evolving/superseded requirements"; "first agent spec-to-prompt evolution with hidden invariants"; "first long-term regression retention"; "repair-disagreement VOI algorithm".
- **Conditional feasibility:** real *agent-designer* edit-surface decisions under authority + causal uncertainty may warrant an applied software-engineering/agent-evaluation study if those choices cause measurable downstream differences beyond standard development.
- **No evidence:** that a general-purpose learned designer, surrogate or world model would improve the study; no training planned.
- **Next milestone:** replicate/extend an existing benchmark or real cross-boundary incident, not build a shiny new framework.

## Primary-source ledger

- EvoCode-Bench arXiv: https://arxiv.org/abs/2605.24110 ; HTML: https://arxiv.org/html/2605.24110v1 ; corrected/re-release README: https://github.com/UniPat-AI/EvoCodeBench
- FeatureArc: https://arxiv.org/abs/2610.37434
- TDAD + code: https://arxiv.org/abs/2603.08806 ; https://github.com/f-labs-io/tdad-paper-code
- SWE-Milestone: https://proceedings.mlr.press/v306/deng26d.html
- LoopsBench + code: https://arxiv.org/abs/2608.00267 ; https://github.com/microsoft/Loopsbench
- EvoWeb: https://arxiv.org/abs/2610.16402
- EvoHarnessBench: https://arxiv.org/abs/2609.04280
- SWE-Interact: https://arxiv.org/abs/2606.30573
- ReqClarifyBench: https://arxiv.org/abs/2610.13022
- SWE-Clar: https://arxiv.org/abs/2610.31854
- SpecPath: https://arxiv.org/abs/2608.09799
- Tressoir: https://doi.org/10.1145/3786335.3813143
- PRISM: https://aclanthology.org/2026.findings-emnlp.1455/
- MASS: https://research.google/pubs/multi-agent-design-optimizing-agents-with-better-prompts-and-topologies/
- PULSE: https://proceedings.mlr.press/v306/chen26da.html
- Decision-region active learning: https://proceedings.mlr.press/v33/javdani14.html
- HDA: https://arxiv.org/abs/2610.22466
- Rethinking harness evolution: https://arxiv.org/abs/2607.12227

*Audit limitations:* not exhaustive, no direct computational reproduction, and all reported model-performance numbers are author-reported. Preprint versus peer-reviewed status matters; independent verification pending.
