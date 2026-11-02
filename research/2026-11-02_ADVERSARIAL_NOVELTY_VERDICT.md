# Adversarial novelty audit: does repair-decision identifiability survive?

**Date:** 2026-11-02  
**Status:** **BROAD ALGORITHMIC NOVELTY FAILS. A narrow evaluation hypothesis remains, with uncertain originality.**  
**Evidence:** primary conference/proceedings pages and arXiv records checked; no algorithm implemented or benchmark executed. This is a skeptical scoping audit, not a claim of exhaustive coverage.  
**Supersedes as a novelty assessment (not as historical notes):** [repair-decision candidate](2026-11-02_REPAIR_DECISION_IDENTIFIABILITY.md).

## 1. Main finding — decisive mathematical precedent

Our earlier proposal selected clarification/probes based on whether they separate plausible worlds that justify different permanent edits. This is **decision-region determination** (DRD), an established active learning problem.

**Primary precedent:** Javdani et al., [*Near Optimal Bayesian Active Learning for Decision Making*](https://proceedings.mlr.press/v33/javdani14.html), **AISTATS 2014, PMLR 33:430–438** (**not ICML**). It selects costly tests to reach overlapping decision regions; its algorithms seek decision sufficiency rather than full state identification. Older equivalence-class determination literature is relevant too.

Mapping:

| Proposed object | Established DRD counterpart |
| --- | --- |
| Plausible stakeholder-intent + technical-cause world | Hypothesis/state |
| Candidate permissible durable repair(s) | Decision region(s), possibly overlapping |
| Ask stakeholder / probe tool / run contract test | Costly test with observable outcome |
| Stop when worlds justify a common repair | Version space contained in a decision region |
| Minimize cost of evidence | Adaptive decision-region test selection |

**Result:** "repair-disagreement-guided evidence collection" is not new mathematics. A new algorithm must have a genuinely different capability, objective, guarantee, or approximation that outperforms **DRD/HEC adapted to the exact same task**, not merely an agentic application.

## 2. Other direct overlapping precedents (newly checked)

| Claim previously proposed as new | Closest primary sources and actual scope | Novelty implication |
| --- | --- | --- |
| Generate clarification only when alternative outputs differ | [CONTRA (Oct 2026)](https://arxiv.org/abs/2610.01769), program execution under alternative answers; [code repository](https://github.com/fangz-cs/Contra) | Already directly studied. Code release omits published benchmark/tasks, execution-verification drivers and transcripts; a full independent reproduction is NOT available there. |
| Distinguish stakeholder specification uncertainty from prediction/model uncertainty, use value of information | [SAGE-Agent (ACL Findings 2026)](https://aclanthology.org/2026.findings-acl.2028/) | Already explicit. |
| Clarify intended program behavior, then perform root-cause diagnosis and repair | [CAMP (Information and Software Technology 2026)](https://doi.org/10.1016/j.infsof.2026.108282) | Very close conceptual composition. Full methods should be checked via accessible author manuscript; publisher abstract checked but full-text access restricted. |
| Separate authority over requirements/tests from evidence of patch correctness | [*Whose Oracle Is It?* (ASE APR 2026)](https://conf.researchr.org/details/ase-2026/apr-2026-papers/6/Whose-Oracle-Is-It-The-Authority-Problem-in-Deployed-Agentic-Program-Repair) | Direct prior art for independently authorized repair witnesses and protected versus editable tests; "typed authority" is not enough. |
| Decide which versioned persistent agent asset to replace; allow no-change | [DAAF (Sep 2026)](https://arxiv.org/abs/2609.32498) | Very close to target semantics; DAAF chooses **registered replacements** and does not generate arbitrary edits online. |
| Co-evolve active probes and enduring harness improvements | [KPHarness (Oct 2026)](https://arxiv.org/abs/2610.27417) | Very close; gaming environment, a single backbone, limited cross-domain generalization as author-reported. |
| Prove which interacting components of a failed trajectory require joint changes | [Minimal Repair Family Recovery (Aug 2026)](https://arxiv.org/abs/2608.29228); [DoVer (ICLR 2026)](https://arxiv.org/abs/2512.06749) | Targeted intervention and counterfactual repair are established. |
| Recognize when no change or escalation is right | [FixedBench (May 2026)](https://arxiv.org/abs/2605.07769), 200 already-fixed issues; [ImpasseBench (Oct 2026)](https://arxiv.org/abs/2610.31895) | Even these behaviors have named benchmarks; no-change is not new. |
| Interactive whole-project clarification benchmark | [ReqClarifyBench (Oct 2026)](https://arxiv.org/abs/2610.13022), 341 tasks; [SWE-Clar (Oct 2026)](https://arxiv.org/abs/2610.31854), 100 real-client commissions | Repository/project-level clarification already has data, simulators and isolated downstream evaluations. |
| Evaluate evolving requirements/persistent harnesses | [RECAP (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.1684/), [SpecPath](https://arxiv.org/abs/2608.09799), [EvoHarnessBench](https://arxiv.org/abs/2609.04280), [Evo-Bench](https://arxiv.org/abs/2608.09096) | Longitudinal constraints and harness adaptation are well represented. Not first such benchmark. |
| Avoid overfitted patches with counterexamples or generated tests | [Iter-T (IEEE TSE 2026)](https://doi.org/10.1109/tse.2026.3671416), [CoHarden (2026)](https://www.microsoft.com/en-us/research/publication/beyond-fail-to-pass-iterative-hardening-of-co-generated-bug-reproduction-tests-and-fixes/), [APCA-in-the-Loop (ESEM 2026)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.77) | A test that discriminates repairs is not new. |
| Empirically establish patch-evaluation bottlenecks in agentic software repair | [ISSTA 2026 traceability study](https://d3ccyth396mz21.cloudfront.net/publications/understanding-automated-program-repair-agents-through-the-lens-of-traceability-an-empirical-study), 500 tasks, 5 repair agents | Already substantiates overfitting, test generation/selection bottlenecks in its domain; do not claim those as our discovery. |
| Broad agentic architecture evolution | [Tressoir](https://doi.org/10.1145/3786335.3813143), ADAS, PRISM | Existing prior art; our end-to-end product vision can be useful but is not an algorithmic contribution on its own. |

### Important conceptual correction

An uncertainty source ("user" versus "tool") is a **test-channel constraint** in a partially observable decision problem. Normative/authorization constraints matter to engineering safety, but adding them to the state does not alone change the foundational active learning problem. A lexicographic authorization penalty is a reasonable design choice, not inherently a new learning algorithm.

## 3. Attempts to falsify the benchmark novelty

**Original 2x2 benchmark idea:** fixed public observation, hidden stakeholder contract S0/S1 and technical fault F0/F1; ask, probe or edit with costs, persistent artifact and regression checks.

- **Too easy / circular danger:** If constructed worlds are exactly indistinguishable without oracle questions, any policy must sometimes ask/probe. Showing that "immediate-edit" fails proves a logical impossibility under hidden information, not a new empirical discovery.
- **Simulator leakage:** A language-model stakeholder may accidentally provide inconsistent clues, reveal scenario labels, or favor models from the same training family. ReqClarifyBench and SWE-Clar already show the importance of realistic user oracles and independent evaluation.
- **Artificial alternative patch danger:** A benchmark can make the correct answer a single text diff. Real repairs may have several valid implementations; score equivalence classes or approved behavior, not exact changes.
- **Integration-only novelty:** A reviewer may combine CONTRA+SAGE for intent, DoVer+DAAF+KPHarness for technical diagnosis/repair, DRD/HEC for decision-sensitive test selection, and protected independent tests for admission. Our method MUST beat this combined, equal-budget baseline.
- **Real incidents rarely prove dual uncertainty:** The verified [LangChain patch→issue→patch chain](https://github.com/langchain-ai/langchain/issues/40853) is technical boundary violation, *not* stakeholder intent ambiguity. We must not pass such examples off as support for a joint-latent-intent algorithm.
- **Static vs dynamic artifacts:** A finite benchmark with one edit is already covered by many cited task settings; to make meaningful long-term claims, test legitimate requirement supersession, active obligation provenance and 3+ subsequent changes, with independent human validation.

## 4. What is still plausibly unmeasured (SCOPED, NOT VERIFIED ABSENT)

A prospective **joint, longitudinal, application-level agent-design revision protocol** in which:

1. **Both** the hidden *authorized* requirement and the technical cause can vary independently.
2. A developer/architect can choose between *human clarification* and *sandbox diagnosis*, or abstain, under explicit costs and authority constraints.
3. The candidate modification is a **persistent edit** to actual stage prompts, tool schemas, routing or handoff logic, not a one-off runtime rescue.
4. A series of real, semantically close requirement **supersessions** is evaluated against an independent still-active contract.
5. Test-time budget, test editing authority and application-family holdouts are controlled.

Our scoped audit has not found a study simultaneously demonstrating **all five** with actual long-lived agent design artifacts. However, all individual ingredients and most two- or three-way combinations are established; absence of a perfect match does **not** establish a new scientific contribution.

**Most defensible possible paper class:** rigorous *empirical/benchmark characterization* of failure modes, not a new RL/decision-aware algorithm. The bar remains high, since benchmarks for clarification, evolution, and abstention already exist.

## 5. What could be a genuinely distinct algorithm later?

Only after measuring a residual deficiency beyond an adapted DRD/HEC + composed agent baseline, for example:
- an efficient **online approximation** for large, structured, nonenumerable repair sets under changing authorized constraints that uses measured counterfactual effects rather than imagined oracle outcomes;
- calibrated risk bounds for an **independent downstream obligation vector** under distribution shift with specified assumptions and demonstrably useful refusal/abstention;
- a new approach to **test-oracle corruption when requirements legitimately change**, beyond ASE APR 2026's existing protected witness model.

All are high-risk hypotheses. The general formulations inherit known active learning, conformal/risk control, program verification and authority literature. Do NOT advertise as new until a specific mechanism/guarantee and nontrivial empirical superiority emerge.

## 6. Why it *conceptually could work* without being novel

Decision-sensitive evidence acquisition can reduce unnecessary questions when different world explanations lead to the **same** admissible repair; it can reduce harmful immediate edits when different plausible worlds require **different** repairs. Independent locked contract tests can catch regressions within their coverage. These are reasonable deductions under honest models/oracles and informative tests.

They do **not** guarantee success when:
- the true interpretation or cause is absent from the hypothesis set;
- user and probe responses are noisy or unavailable;
- a "reasonable" but wrong patch passes limited tests;
- requirements contradict or lack a clear authority;
- real stochastic agent effects make counterfactual outcomes unstable;
- cost of diagnostic search exceeds future savings.

## 7. Revised research direction and decisive minimal experiment

**Candidate title:** *When Is an Agent-Design Revision Justified? A Longitudinal Study of Intent, Diagnosis, and Cross-Component Consequences*.

1. **First collect evidence**: sample both successful and problematic agent-configuration revisions (do not sample only issue failures). Independent annotators assign contract lineage and technical cause; separate AI-generated from human changes.
2. **Run two real application families** with 12–20 *human-vetted* episodes only as a feasibility pilot; one includes authentic tool/serialization boundaries like LangChain #40853; another includes approved changing research retrieval/authorization requirements.
3. Include paired private worlds, but also **natural non-ambiguous cases**, stale or partially fixed complaints, multiple valid repairs, diagnosis-only technical problems, and cases requiring either/both/no evidence sources.
4. Baselines at equal tool, token and test budgets: strong direct editor, +spec and regression, **SAGE/CONTRA+DoVer/DAAF composed**, **DRD/HEC decision-region selection**, simple always-ask/probe/no-change; oracle intent/cause controls.
5. Main metrics: **unauthorized permanent edit rate, still-active obligation regressions, successful justified revisions, question/probe cost**, longitudinal performance after 3–6 changes. Compare meaningful utility/cost Pareto curves, not only scalar win-rate.
6. **Pre-register kill gate:** If adapted DRD/HEC and the composed LLM are competitive with our method, mark algorithm novelty as rejected; if realistic human-vetted episodes do not distinguish existing methods, benchmark novelty also rejected.
7. Only if a concrete residual failure survives: design the smallest mechanistic fix and ablate it, without presupposing RL.

## 8. Final novelty assessment (2026-11-02)

| Contribution claim | Verdict |
| --- | --- |
| New principle of ask/probe based on repair disagreement | **REJECTED**: DRD/HEC 2014 |
| Distinguish normative/user intent from technical root cause | **NOT NOVEL alone**: SAGE-Agent, CAMP, authority APR |
| Active probing, minimal repair, or permanent harness evolution | **NOT NOVEL alone**: DoVer, DAAF, KPHarness, GCJR |
| Clarification based on observable behavioral divergence | **NOT NOVEL**: CONTRA |
| Test-gated regression safety or specification revisions | **NOT NOVEL**: Iter-T, CoHarden, RECAP, TDAD |
| Comprehensive interactive durable agent-design evaluation under both latent uncertainties | **POSSIBLE SCOPED EMPIRICAL GAP; originality unverified** |
| A learning algorithm that materially beats HEC + a composed modern agent | **UNKNOWN; no evidence or implementation** |

**GO** for small independent empirical falsification study. **NO-GO** for a paper claiming that repair-disagreement, value-of-information or an RL selector is a new algorithm. The broader conversational agent architect remains an engineering/product goal.

## 9. Research integrity notes

This audit rechecked publication pages and arXiv summaries, plus accessible methods for a subset. **It is not a full-text exhaustive review of all papers.** In particular, CAMP publisher full text was inaccessible; do not make granular claims about it. Experimental results quoted elsewhere are author-reported, not reproduced by us. The strongest theoretical precedent is published at **AISTATS** (not ICML); correct any earlier references. Commit this revised decision instead of letting the old more optimistic proposal silently persist.
