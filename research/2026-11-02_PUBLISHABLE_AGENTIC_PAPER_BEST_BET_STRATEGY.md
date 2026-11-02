# Strategy gate: choose a field first, discover a failure mechanism, then propose a method

**Date: 2026-11-02. Decision: prioritize continual learning in tool-using agents, with causal action understanding as a possible mechanism, NOT an asserted new algorithm.**

## Why this field rather than the shortest literature gap?

We need to maximize the joint probability of finding (1) a substantive agent-specific phenomenon, (2) an implementable distinct mechanism, (3) credible existing benchmarks and strong baselines, (4) reproducibility and measured generalization. For our present research workflow, we can run real tool-using agents on software/service simulation tasks, and can build environment-state ground truth without robotics hardware or costly human studies.

Long-run self-improvement, skill transfer, interference and knowledge revision are scientifically meaningful even if a particular method fails. Conversely an obscure, cheap testing edge case can be relatively uncrowded but yield only an engineering note.

**Primary scientific question:** When a tool-using agent accumulates experience and then encounters changed action effects or preconditions, how does it distinguish applicable knowledge from obsolete or misleading experience, with limited safe experimentation?

This is a *candidate question*, not yet a distinctive research contribution. Do **not** call the combination of causal learning and continual skills novel by itself.

## Prior art that sharply constrains a method proposal (primary abstract checks)

- [Are Self-Evolving Agents Continual Learners?](https://arxiv.org/abs/2610.25858): self-modification vs memory retrieval, stability–plasticity tradeoff and retrieval collision.
- [ContinualSkillBench](https://arxiv.org/abs/2608.03874): test whether accumulated experience really produces transferable skills; in-context approaches often rival explicit skill libraries.
- [SkillLearnBench](https://arxiv.org/abs/2604.20087): feedback, skill generation, open-source baseline benchmark, and limits of skill improvement.
- [When Not to Imitate: Boundary-Aware Skill Memory](https://arxiv.org/abs/2608.22339): inapplicable skills and skill-boundary conditions are ALREADY methodized; no claim that applying precondition tags is new.
- [Scope Before You Persist](https://arxiv.org/abs/2609.29144): family-scoped persistent retrieval and external admission; scoped retrieval is ALREADY methodized.
- [Coalition-Aware Skill Reliability](https://arxiv.org/abs/2608.22610): skill utility interactions and removal of harmful memory, not fresh territory.
- [Compile Away Uncertainty / SkillCompiler](https://arxiv.org/abs/2610.39508): compiled reusable procedural skills; deterministic skill execution is not first.
- [When Do Causal World Models Help Modular LLM Agents?](https://arxiv.org/abs/2610.00012): cross-module causal world models and action-time value of interfaces.
- [CausaLab](https://arxiv.org/abs/2605.26029): interventional causal discovery environment separates outcome success from mechanism recovery.
- [Active Causal Discovery Benchmark](https://arxiv.org/abs/2609.31675): limited-intervention active discovery with strong non-LLM statistical baselines.
- [Hierarchical Experimentalist Agents (HExA)](https://arxiv.org/abs/2606.29315): active experimentation and distilled reusable skills already combined.
- [Model Discovery Agent](https://arxiv.org/abs/2608.09696): Bayesian experiment design and causal mechanism discovery, strong algorithmic rival.
- [CausalFlow](https://arxiv.org/abs/2605.25338): causal attribution and counterfactual agent-trace repair.
- [Capability-Gated Planning](https://arxiv.org/abs/2608.05085): cost-to-go planning vs myopic information-gain exploration.

This is a competitive field; these references demonstrate activity and novelty risk, not a verified gap.

## The scientific workflow (stop at each gate)

**Gate 0 — choose reproducible baselines, not a title.**
Find executable code/data for 2–3 methods from SkillLearnBench, ContinualSkillBench, BASM, Scoped-ORC, HExA, and/or a non-causal strong ReAct baseline. Record commit SHA, environment, model/token budget and evaluation protocol. Verify license and compute. If all relevant code is unavailable, reconstruct faithfully and label the reconstruction.

**Gate 1 — replicate at least one actual agent failure.**
Agents must make model-driven decisions, execute real sandboxed tools, receive real observations and choose subsequent actions. Compare an unchanged environment and controlled intervention that changes tool precondition/effect. Evaluate held-out task success as well as behavior under changed dynamics. Predeclare task oracle and intervention schedule; include benign tool edits, unrelated task-family changes, and unchanged controls. Do not count handcrafted traces as agent runs.

**Gate 2 — explain a failure that strong baselines cannot already repair.**
Diagnose whether failure is retrieval collision, stale world model, over-generalized skill applicability, or unrecognized effect change. Test BASM conditions, scoped retrieval, active experiment selection, deterministic tool-contract checks, random safe probes, and replan-from-scratch. If any strong conventional mechanism fixes it at equal cost, method claim NO-GO. If no measurable problem, stop.

**Gate 3 — only then derive an original mechanism.**
A hypothetical idea might use an *uncertainty-calibrated, task-directed diagnostic policy* that decides when a tool model needs an intervention rather than blindly applying a retrieved skill. This exact idea is NOT pre-cleared: MDA, ACDB, HExA and FedCausalCompose are direct novelty threats. Require nontrivial distinction in observable interface, objective, decision rule or guarantees. Make ablations that separately remove each genuinely distinct part.

**Gate 4 — rigorous agents and generalization.**
At least two agent backbones if feasible; several repositories/tool domains; independent held-out task families and change types; matched tokens, tool calls, wall-clock time and success thresholds; baselines on a frontier curve. Estimate task-family clustered uncertainty. Report model/tool access and data leakage. Reward both retention of old tasks and adaptation to new tasks.

**Gate 5 — submission-quality result.**
Evidence for a *new method* requires nontrivial improvement over the closest algorithmic rivals at matched utility/cost, no hidden-oracle leakage, failure-mode understanding, and meaningful transfer. Otherwise a principled empirical finding or benchmark may still be publishable but needs separate novelty review. No numerical acceptance probabilities are defensible in advance.

## Reasons to abandon this direction

1. Existing method (BASM/Scoped-ORC/HExA/MDA/FedCausalCompose) already solves the same exact setting; no meaningful remaining algorithmic distinction.
2. Baseline advantage disappears once tool schema validation, deterministic retries or matched compute are included.
3. A claimed learning improvement is just longer context, more trials, or memorizing task-specific state.
4. Significant gains exist only in tiny invented state machines or unblinded test families.
5. Evaluation never runs real model-directed tool choices.
6. Confidence intervals on held-out tasks are too broad to support contribution claim.

## Practical prioritization

- **First 1–2 weeks (decision goal, not promised duration):** audit code and replicate one benchmark baseline plus one failure mode.
- **Only after that:** identify residual and design a method; use the external LLM judge before implementation.
- **No manuscript title now.** A scientific title should name the mechanism or verified phenomenon, not a rebranded combination of existing research areas.

**Research state on writing:** no novel continual-learning algorithm demonstrated, no baseline replicated in this track, no real model experiment for this question.
