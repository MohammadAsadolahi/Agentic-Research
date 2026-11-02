# ShiftTogether — prespecified agentic-AI falsification pilot

**Status 2026-11-02:** Candidate research title only. **No model runs; no novel algorithm or empirical interaction demonstrated.** Closest papers: [stale](https://arxiv.org/abs/2609.25396), [SWE-Shift](https://arxiv.org/abs/2610.32196), [CodeSpecWeave](https://arxiv.org/abs/2610.40256), [SpecPath](https://arxiv.org/abs/2608.09799).

## Proposed title

**ShiftTogether: Measuring Interaction Failures in Parallel Coding Agents Under Mid-Execution Requirement Changes**

Do NOT claim first concurrent coding benchmark, first dynamic-requirements benchmark, or first test of coordination. This is an **interaction-specific** question; the intersection may already be in an unexamined paper.

## Unit of study and hypothesis

One real repository, baseline revision, coding task, precommitted test oracle, specific tested final contract, model, and random seed make a *blocked unit*. From the same saved starting workspace and task, run the matched 2×2 conditions:
- **00:** one coding agent, unchanged instruction/requirements.
- **10:** two coding agents working in parallel on split, interacting changes, unchanged requirements.
- **01:** one coding agent, requirement revision introduced during execution.
- **11:** two coding agents, same revision distributed mid-execution to both through the same authorized interface.

Evaluation uses the same **final effective specification**, with a justified comparison for unchanged vs revised task. The planned revision must be defined ahead of time, not selected after seeing a failure. We must define task utility so cases with revised objectives are compared meaningfully; main comparison may need to be within revised vs unchanged matched task families, not a literal identical final contract for both (see confounds).

Let p(cr) be the per-block probability of independently verified final-contract failure under concurrency c and revision r. Test the **risk-scale interaction**:

    I = p(11) - p(10) - p(01) + p(00)

H0: I = 0. H1: I > 0 (superadditive failure, not presumed true).

**Key confound:** independent requirement changes naturally alter final objective difficulty. Use both a contemporaneous *consolidated-current-instruction* counterfactual and an outcome definition tied to the applicable contract. Distinguish environment-shift effect from final-contract difficulty. Stratify by task/revision family.

If I is positive only because parallel workers have less total inference budget or late revision was delivered differently, it's not an agent coordination mechanism.

## What we can ethically and practically evaluate

- Offline, sandboxed coding tasks with no production write, exfiltration, billing or privilege granting.
- Paired real code tasks with a shared source branch, authorized requirements updates and protected hidden tests.
- Main outcome: executable final-contract success. Secondary: per-commit contract violations, isolated patch success, merged patch success, discarded work, token/cost budgets, revision event timing.
- Hard negative controls: independent parallel edits, benign revision that does not affect peer's interface, authorized contract migration, and non-coding deterministic baseline.
- Independent oracle: human or preregistered tests not editable by the agent, and established before candidate patches. Train/dev and held-out repositories separate.

## Strong competitors and ablations (must implement before novel method)

1. **Serial single agent** with same total token budget and effective final requirements.
2. **Two agents with ordinary synchronization:** send a completion message and changed-contract summary to the other worker; this is essential because stale finds such a message fixes many constructed failures.
3. **Replan/restart from the consolidated current contract**, with preserved or reset workspace as appropriate (SWE-Shift, DynaRev).
4. **Versioned contract broadcast plus premerge integrated tests** (conventional engineering baseline). This is not a new algorithm.
5. **Same-compute no-communication control** as demanded by ICR communication auditing.

Any proposed new method must outperform these under fixed model, tokens, latency, test execution, and maintenance cost. An untested versioned-handoff method is a hypothesis, not a contribution.

## Sampling, uncertainty and stop rules

**Feasibility:** first acquire 4-8 independent, repository-backed tasks, each with four conditions and multiple random seeds; demonstrate that all four cells are runnable without test leakage. This is not a publishable n.

**Study target:** a predeclared set of at least 30 independent task families spanning multiple repositories, with two agent backbones if feasible. No promise of statistical power from the nominal sample count: calculate detectable effect/CI precision before claiming generalization.

Fix model, prompt, tool access, CI, seeds, agent architecture, latency budget, revision event triggers, and test verifiers before a held-out phase. Use task-level clustered bootstrap and report individual failure rates as well as I. Do not interpret a high interaction when p11 is at ceiling and other cells have no dynamic range.

**Immediate NO-GO if:**
- A primary paper already evaluates the equivalent interaction and intervention;
- Paired tasks cannot maintain comparable problem difficulty and cost;
- I is near zero or too imprecise to distinguish from zero in properly grounded agent runs;
- Conventional synchronization/replanning removes the effect equally well;
- Apparent gains emerge only in constructed cases designed for our method;
- The effect also appears in non-agent scripts or generic workload scheduling without specific agent reasoning.

If a real interaction survives, the first paper contribution could be a **factorial agent-behavior benchmark and diagnostic account**, not necessarily a novel algorithm. A new adaptive mechanism would require a separate strong-baseline study.

## Test artifacts to collect per paired block

CSV rows: `task_id,block_id,parallel,revision,failure,main_task_success,cost_usd` (four rows per block). Block IDs combine task, seed and model. Record per-condition executable acceptance evidence and unmodified raw tool trajectories. No final paper claim from the analysis script alone.

The analysis script is **pre-registration infrastructure**, not an experiment. It should fail when any block lacks one of the four cells; it reports a task-clustered bootstrap interval, not a p-value manufactured from repeated runs on the same task.
