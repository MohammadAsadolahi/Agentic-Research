# November 2, 2026 — Critical literature reassessment

**Status:** Scoping literature audit extended. No new algorithm, benchmark, or experiment has been implemented. No novelty claim is established.

**Summary:** The initial motivating problem remains real, but the field already contains strong and increasingly direct methods for most proposed interventions. We should start with *failure attribution and matched-baseline experiments* and only propose a learned architect if simple safeguards leave a reproducible residual failure.

## What changed after the initial research state

### New or previously underweighted primary evidence

1. [Treude & Baltes, *How Do Coding-Agent Harnesses Self-Evolve?* (26 Oct 2026), arXiv:2610.34938](https://arxiv.org/abs/2610.34938): 30 Claude Code sessions, 125 retrospective proposals, 24 implemented; 12 adaptations evaluated on later issues. In 7 informative transfer evaluations, 2 eliminated targeted repeated actions, 1 reduced them, and 4 did not. Some generated additional unrelated work. **Caveat:** small, targeted, nonrandom transfer sample, measures repeated actions rather than broad task generalization. [Replication materials](https://doi.org/10.5281/zenodo.23653700).
2. [Yan et al., *When the Specification Emerges / SLUMP* (Findings EMNLP 2026)](https://aclanthology.org/2026.findings-emnlp.76/): 20 ML implementation projects, 371 atomic components and approximately 60 progressively revealed requests per project. ProjectGuard recovered 90% of Claude Code's measured faithfulness gap in their setting. **Implication:** persistent semantic/structural project state is not a novel intervention per se. **Caveat:** project type and scripted progression narrow external validity.
3. [Zou et al., *StateHarness* (Oct 2026)](https://arxiv.org/abs/2610.17616): records project understanding, decisions, and dependencies; improves several task metrics but pass-to-pass regressions increase in one sequential benchmark. **Implication:** remembering project decisions is not identical to preserving behavior.
4. [Huang et al., *BenchTrace* (2026)](https://arxiv.org/abs/2605.29225): 1,821 annotated episodes; low diagnostic-reflection performance for two tested models, forgetting and negative transfer between contexts. **Implication:** wrong failure diagnosis may be upstream of bad revisions.
5. [Wu et al., *ModularRSI* (Sept 2026)](https://arxiv.org/abs/2609.14857): contrasts successful/failed traces, modularly updates harness components, uses 2,000 benchmark-disjoint evolution tasks, reports cross-model/domain transfer. **Implication:** contrastive/generalization-aware modular refinement is already strongly occupied.
6. [Lin et al., *Harness Updating Is Not Harness Benefit* (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.2326/): distinguishes generating a useful harness from whether executing models load and follow updates. **Implication:** assess generation, activation, and runtime effect separately.
7. [Pan et al., *Evolving Agents in the Dark / RHO* (Findings EMNLP 2026)](https://aclanthology.org/2026.findings-emnlp.2439/): self-supervised trajectory resampling and self-preference to choose harness updates; reported one-round SWE-Bench Pro improvement is **author-reported** and not proof of generalization beyond the tested setting. **Implication:** unlabeled retrospective optimization is prior art.
8. [Chen et al., *HarnessFix* (2026 preprint)](https://arxiv.org/abs/2606.06324): transforms traces into provenance/control-flow-aware representation, diagnoses responsible harness layers, generates scoped patches and checks regressions. **Implication:** root-cause diagnosis + correct edit-surface selection has a close competitor.
9. [Mani et al., *Multi-Agent Change Impact Analysis and Test Optimization* (IEEE AITest 2026)](https://doi.org/10.1109/AITest70988.2026.00044): combines structural, semantic, retrieval and risk evidence for test selection, with mixed results and some single-signal baselines strongest. **Implication:** cross-component impact/test selection is not new by simple integration.
10. [Chawla & Koul, *Chronicle* (REALM 2026)](https://aclanthology.org/2026.realm-1.71/): cut-point replay converts recorded agent incidents into regression tests; benchmark is only 6 simulated-boundary failures. **Implication:** testing infrastructure exists; need broader validation.
11. [Cai et al., *Safe Harness Self-Evolution* (Sept 2026)](https://arxiv.org/abs/2609.08175): theoretical retention and finite-data admission rules under **fixed task-distribution assumptions**. **Implication:** do not promise universal guarantees across nonstationary user requirements.
12. [Zhang et al., *Guardrails Beat Guidance* (2026)](https://arxiv.org/abs/2604.11088): >5,000 coding-agent runs indicate that some random rule sets match curated instructions in the tested conditions, and added rules do not universally degrade results. **Implication:** prompt length/bloat is not an adequate standalone causal explanation.
13. [Ding et al., *Harness-Delta Attribution* (Oct 2026)](https://arxiv.org/abs/2610.22466): on the subset of 21 settings with significant search-set gains, attributes averages of 54% and 14% of gains to overfitting and additional inference-time compute respectively. **Implication:** strong transfer and matched-compute controls are mandatory.
14. [Deshpande et al., *RECAP* (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.1684/): strictly proactive continual prompt adaptation on evolving add/edit/delete constraints, with no significant overall gains for six methods under its reported protocol.
15. [Raghavendra et al., *SWE-Interact* (2026)](https://arxiv.org/abs/2606.30573): multi-turn user-driven software requirements with incomplete initial briefs; strong single-shot performance does not reliably carry over to conversational revisions.
16. [Liu, *More Is Not Always Better: Cross-Component Interference* (2026 preprint)](https://arxiv.org/abs/2605.05716): a limited factorial study suggests non-additive and model-dependent effects from combining scaffolding components. **Caveat:** narrow tasks/models; do not generalize exact interaction strengths to all systems.

### Revised causal taxonomy

A bad change may arise at six separate locations:

- **Interpretation:** user incident mistaken for a general rule, or approved supersession mistaken for an unintended regression.
- **Diagnosis:** wrong causal layer blamed (prompt, tool, routing, middleware, context, environment).
- **Proposal:** overly narrow, contradictory, or unnecessary revision.
- **Activation:** executing agent does not load or faithfully follow the revised harness.
- **Consequence:** local fix succeeds but causes downstream, cross-task, cost or safety regressions.
- **Admission/evaluation:** noisy tests or judge leakage allow a bad revision through, or reject a legitimate one.

**Do not equate all of these with "overfitting."** The right intervention depends on which mechanism is dominant.

## Updated novelty assessment

| Idea | Revised status |
| --- | --- |
| General-purpose AI agent architect | Valuable product goal; Tressoir and existing design assistants provide substantial prior art |
| Reinforcement learning or world model for agent design | Existing methods overlap; NO algorithmic novelty established |
| Long-term structured specification memory | ProjectGuard, StateHarness and Tressoir provide direct precedents |
| Automatic fault-localization into prompt/tool/harness layers | HarnessFix, PRISM, AgentRx and AHE provide direct precedents |
| Cross-component effect prediction + risk-aware test selection | Existing change-impact research is close; narrow causal/calibration question remains hypothetical |
| Continual preservation using regression gates | GRASP, Self-Harness, RECAP and theoretical results already address pieces |
| Distinguishing incident vs new requirement vs supersession in *agent-design revisions* | Reasonable evaluation hypothesis, but nearest requirements engineering and interactive coding benchmarks must be compared before novelty can be claimed |
| Measuring failure-mechanism prevalence in AI-assisted agent design over sequential changes | Potential empirical contribution IF existing datasets fail to capture the unit of analysis and we run a rigorous independent study |

**Research posture: no confirmed unique algorithmic contribution.**

## Best next experiment — why do revision attempts fail?

Build an **empirical fault-decomposition pilot** rather than an optimizer.

- Start from a small set of functioning agentic applications (research, coding, service workflows) with explicit, independently authored requirements.
- Construct revision events that vary feedback type (incident / approved addition / supersession / ambiguous), true failure layer, and likely downstream interactions.
- Control interventions where possible using known injected prompt, schema, routing or state faults, retaining legitimate no-change cases.
- Independently label whether a revision is needed, valid, sufficiently general, activated, and safe under old *still-applicable* requirements.
- Match models, prompts, test access, rollouts and cost; compare (A) direct editor, (B) editor + tests, (C) + explicit approved specification, (D) + impact-aware analysis.
- Use controlled clean-room replays and unaffected tasks. Hold out whole applications for any transfer claims, and use locked independent acceptance cases.
- Measure fix success, unintended regression, misdiagnosis, proposed change scope, unsupported new rules, activation, additional compute, and human review burden.

**Possible crucial experiment:** supply an *oracle-correct diagnosis* to an editor but keep generator and test access fixed. If errors largely disappear, upstream diagnosis dominates; if not, study proposal or execution effects. This is a control condition, not a deployable method.

**Release / stop rules:** If B equals C within meaningful uncertainty, do not claim structured specs add value. If C equals D, avoid extra impact machinery. Do not train an RL selector before a residual failure beyond D is demonstrated. A new model must outperform simple baselines on unseen application families and equal budgets.

## Evidence quality and immediate priorities

- Several studies above are preprints, self-reported evaluations, or small controlled samples. Published workshop papers are not automatically large-sample evidence.
- Published and preprint methods may differ in scope (prompt-only vs tool middleware vs fixed modular harness vs full architecture), so restrict comparisons to supported edit surfaces.
- The present repository does **not** contain new datasets, code, benchmark executions, or independent reproductions. All proposals remain untested.
- The replication package for the October 26 retrospective study is unusually actionable. First inspect its license/requirements, then reproduce one baseline and one transfer adaptation before creating a new framework.
- For each competing paper create a structured ledger of edit surfaces, feedback, baselines, statistical unit, data leakage protections, cost, code availability, and most important counterexample.
- Before submission, search the latest adjacent literature again; absence from a scoped search is not evidence of nonexistence.

## Overall decision

**Continue the investigation, NOT the original broad RL-architect pitch.** The priority is a controlled empirical study of failure mechanism and revision transfer. Promote only a measured, baseline-resistant residual problem into a new algorithm research question.
