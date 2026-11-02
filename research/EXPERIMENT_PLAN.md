# Falsification-first experimental plan

**Status:** planned; NO experiments run, NO dataset constructed, NO benchmark result claimed.  
**Goal:** determine *what causes behavioral regression* when an AI assistant revises prompts, tools, or workflow components, before proposing a learned optimizer.

## 1. Scientific questions

- **RQ1:** Does the editor mistake an observed failure for an unconditional requirement or improperly preserve superseded requirements?
- **RQ2:** Are most regressions due to inadequate test coverage, misdiagnosis of the intervention surface, specification drift, or stochastic execution?
- **RQ3:** At matched evaluation budgets, does an explicit, independently approved specification add benefit beyond a strong LLM + ordinary regression tests?
- **RQ4:** Does dependency-aware impact analysis improve outcomes beyond explicit specifications and the same tests?
- **RQ5 (conditional):** After A–D, does a learned intervention selector improve held-out results sufficiently to justify training?

## 2. Experimental unit and data

An **application** contains: user/stakeholder-validated goals and nonfunctional requirements; working architecture; stage prompts; tools and tool schemas; runnable environment or simulator; and independent acceptance tests.

A **revision event** contains: a fresh user complaint or requirement change, initial execution trace if applicable, the intended interpretation (bug / new capability / requirement supersession / ambiguous), acceptable and forbidden outcomes, and an independent evaluation bundle.

**Pilot target (proposal, not data already gathered):** several applications across research, coding, service workflows and data processing; multiple sequential revision events per application. Expand only after a feasibility pilot and power analysis. Include no-change and clarification-required cases. Avoid automatically generated examples that merely repeat the optimizer's own assumptions.

**Split by entire application family** when claiming transfer; split sequential history in time for continual claims. Keep a locked final evaluator unavailable to any candidate-generating model or training routine. Record model/versions, prompts, temperatures, seeds if possible, tool revisions, API cost, wall-clock time and execution environments.

## 3. Matched conditions

| Arm | Available information | Mechanism |
| --- | --- | --- |
| A. Direct editor | Issue + source artifacts | Strong coding agent directly proposes change |
| B. Editor + regression suite | Same + pre-existing approved tests | Conventional test-driven change acceptance |
| C. + explicit specification | B + structured intent/requirements with approval status | Test whether intent representation adds value |
| D. + impact analysis | C + explicit dependency mapping and counterexamples | Test whether change-target analysis adds value |
| E. Learned selector (ONLY if justified) | Same information and test access as D | Select change type/no-change/clarify via contextual bandit or policy |

B versus C isolates specification value; C versus D isolates impact analysis; D versus E isolates benefit of learning. Different arms should not receive extra hidden tests or greater compute unless the difference is explicitly priced. Record whether an intervention is approved by the correct human authority.

**Strong external baselines to consider where applicable:** a design skill (GitHub agent-architecture), GEPA, PRISM for prompt/tool middleware, a Tressoir-like blueprint designer, MESH for modular harnesses, and GRASP for gated skill edits. Their action spaces differ: make only valid like-for-like comparisons.

## 4. Safe editing and evaluation

1. Snapshot accepted baseline (artifacts, tests, runtime, dependencies, evaluation versions).
2. Classify reported feedback: observed failure vs new requirement vs intentional supersession vs ambiguous. Capture uncertainty and authority.
3. Generate a proposed diff with a **change hypothesis** and expected affected behaviors; allow "no change" or "clarify".
4. Apply candidate in an isolated copy. Tool execution must be sandboxed; external side effects need explicit approval.
5. Run task-level evaluation, previous-success probes, neighboring metamorphic cases, and stateful tool traces.
6. Evaluate independent locked cases only for final reporting, never as a repeatedly consulted optimizer signal.
7. Distinguish intended supersessions from regressions. Rejection/rollback must not silently discard approved new requirements.
8. Retain both accepted and rejected changes plus prediction/evidence for later causal analysis.

Do not allow the editor to modify locked tests, evaluation scoring code, or the specification authority register. If test generation is delegated to the editor, those tests are advisory only until independently approved.

## 5. Metrics and analysis

**Primary outcomes**
- Unintended behavioral regressions per accepted revision (with an approved, versioned specification as reference).
- New-failure resolution / requirement compliance on independent tests.
- Transfer to held-out application families after sequential revisions.

**Secondary**
- Correct change-surface classification (prompt / tool description / tool implementation / topology / deterministic code / no change / ask).
- Changes to unrelated components; unsupported assumptions; contradictions.
- Tool selection and arguments; state transitions; side effects; cost/latency.
- Calibration of predicted regression risk; precision/recall and false-negative rate at a fixed test budget.
- Human review workload and failure severity.

Use paired comparisons on identical cases, repeated executions where stochastic, and uncertainty intervals. Cluster analysis by application or change sequence rather than treating all correlated examples as independent. Report fixed compute budgets and test-time overhead. Compare with Harness-Delta Attribution principles so test-time scaling and search overfitting are not called generalization.

## 6. Ablations and kill criteria

- **If A ≈ B:** first investigate inadequate tests or evaluation quality.
- **If B ≈ C:** the structured specification has not demonstrated incremental value; avoid claiming it as a contribution.
- **If C ≈ D:** dependency/impact machinery is not justified.
- **If D ≈ E:** do not pursue RL or a learned intervention selector.
- **If a world-model surrogate does not improve final quality at matched evaluation cost:** do not add one.
- **If gains vanish on whole held-out applications:** describe task-specific optimization, not transferable design intelligence.
- **If improvements come from relaxing tests, changed judges, or extra inference budget:** fail the novelty/generalization claim.

The equalities here mean "no meaningful evidence of improvement under adequately powered analysis", not a literal equivalence of observed point estimates. Pre-register a practically meaningful effect size and budget before reviewing outcome data.

## 7. Possible second-stage ML research (only after first-stage diagnosis)

**Hypothesis B1:** Controlled change experiments plus architecture dependencies improve predictions of *which obligations* regress versus a strong trace-only model and static dependency tests.

**Hypothesis C1:** A policy that jointly models approved intent changes and failure hypotheses chooses safer interventions on previously unseen application families than direct LLM selection.

Neither model should be called causal without a valid intervention design, nor called a world model unless it genuinely predicts sequential transition dynamics and provides measurable planning benefit.

## 8. Research artifacts to create next

- Applications and independently validated requirement histories.
- Dataset cards, permissions, environment Dockerfiles, tool mocks.
- Baseline revision traces and before/after behavior.
- Evaluator specification and locked-test protocol.
- Pre-registration / statistical analysis plan.
- Ablation table and honest null-result reporting.
- Paper-reproduction ledger with links to upstream code and known limitations.

**First milestone:** finish and audit a small A–D pilot, and write down what empirically failed before writing any RL training code.
