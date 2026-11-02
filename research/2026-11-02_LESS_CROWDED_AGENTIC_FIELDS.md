# Wider field scan: relatively less-saturated agentic-AI paper opportunities

**Updated 2026-11-02.** Research aim: publish a rigorously novel agentic-AI paper rather than build more generic developer tooling.

**Evidence level:** targeted exploratory search of recent 2025–2026 primary arXiv abstracts and selected accepted papers, not exhaustive bibliometrics. "Less crowded" below is a *relative, subjective estimate for a narrow subproblem*, not a count of papers, citation-adjusted density or demonstrated absence of prior work. All proposed titles are **working hypotheses**, NOT verified novel claims.

## Summary recommendation

Choose **two exploratory pilots in parallel**, no algorithms yet:
- **A. AccessibleAct:** accessibility-aligned *execution* and user-verification burden for task-completing assistive agents, not automated WCAG defect detection.
- **B. CoexistBench / PreserveFirst:** non-destructive *continuation after resource conflict* by concurrent tool-using agents, not just identifying destructive preemption. **However SCARCE (October 2026) already studies persistent agent negotiation/institutions in shared compute, so negotiation itself is not novel.**

A relatively low-cost second pilot is **C. TimeShiftAgents**: time/locale metamorphic invariance of agentic *executed external actions*, as opposed to benchmark QA over calendars. This is promising only if the agent-specific mechanism remains after correct deterministic time conversion and conventional scheduling baselines.

Also maintain **D. FairAgentQuota** and **E. MultiPrincipalConsent** as medium-risk leads, not top choices.

## Ranked opportunities with strongest identified novelty threats

| Rank | Narrow field / working title | Why worth testing | Closest prior art & gap blocker | Priority |
| --- | --- | --- | --- | --- |
| 1 | **AccessibleAct: Verification-Aware Autonomous Assistance for Blind and Low-Vision Users** | Test whether an apparently task-successful agent imposes unusable verification, unsafe undo or inaccessible interaction costs; compare sighted-optimized and accessibility-aware policies under identical goal-state checks | [Assistive Agents Need Accessibility Alignment](https://arxiv.org/abs/2605.13579) explicitly names the problem; [VIABench](https://arxiv.org/abs/2607.14660), [InterA11y](https://arxiv.org/abs/2610.39488) and [agentic WCAG auditing](https://arxiv.org/abs/2609.09379) cover adjacent assistance/automated audits. **Novelty risk high** if merely reiterating the position paper. | Conditional GO for executable task-level evaluation with appropriate user expertise |
| 2 | **PreserveFirst: Can Agents Preserve Incumbent Tasks While Completing New Work?** | Test safe, non-destructive replanning, deferral, negotiation and permission, including utility to *both* incumbent and new tasks | [ClashBench](https://arxiv.org/abs/2609.19892) already has 268 executable cases, 55 resource types, 17 models and measures destructive preemption. [multi-user agents](https://arxiv.org/abs/2604.08567), [CalBench](https://arxiv.org/abs/2605.09823), [deconfliction for power grids](https://arxiv.org/abs/2604.09823), and crucially [SCARCE](https://arxiv.org/abs/2610.21029) already covers agents negotiating shared compute over long coding-task sequences. These cover much of simple coordination and negotiation. Need surpass simple OS isolation, deterministic scheduling, protected incumbent tasks. | Conditional GO only on new adaptive policy/baseline advantage |
| 3 | **TimeShiftAgents: Temporal-Invariance Testing of Autonomous Workflows** | Metamorphic paired tasks with same instant under changing timezone/DST/locale, actions scheduled through ≥2 stateful services; correctness judged by external state and deadline invariants, not string answers | [PEARL/CalConflictBench](https://aclanthology.org/2026.acl-long.1547/), [ClawsBench](https://arxiv.org/abs/2604.05172), [REALM-Bench](https://doi.org/10.1145/3770854.3785692), existing timezone-aware software testing and calendar APIs. Scoped keyword search did not find a directly matching recent paper, but this is NOT evidence of absence. Must compare deterministic zoneinfo transformations; otherwise a calendar software-testing note, not agentic AI. | Cheap scoping pilot, higher risk of insufficient generality |
| 4 | **FairAgentQuota: Agent Task Fairness under Shared Tool Quotas** | Task-level success/fairness/SLO when heterogeneous tool-using agents share CPU, API quota, sandbox slots or human-approval queues; study strategic tool selection under contention, not GPU kernel scheduling | [Not All AI Agents Are Equal](https://www.microsoft.com/en-us/research/publication/not-all-ai-agents-are-equal-characterizing-resource-and-performance-dynamics/), [AgentSysBench](https://arxiv.org/abs/2608.15127), [PackServe](https://arxiv.org/abs/2609.33224), [CATS](https://research.google/pubs/cost-effective-agent-test-time-scaling/) and classic queueing/scheduling. Show improvement over weighted fair queuing and work-conserving schedulers with outcomes, not merely latency. | Medium priority, strong systems competitors |
| 5 | **MultiPrincipalConsent: Joint-Action Authorization for Agents Serving Several Users** | Split consent across independently authorized principals; can the agent preserve privacy and legitimate goals when one user revises their authorization? | [Multi-User Large Language Model Agents](https://arxiv.org/abs/2604.08567), [CalBench](https://arxiv.org/abs/2605.09823), [Authorization-Closure Graph](https://arxiv.org/abs/2609.32428), [Root-Scoped Quiescence](https://arxiv.org/abs/2609.21284), [Residual Authority Replay](https://arxiv.org/abs/2609.33910). Need residual not captured by normal ACL/multi-signature or known consent revision. | Medium priority / high formalism burden |
| 6 | **Repairable Handoffs for Blocked Coding Agents** | Evaluate machine-verifiable unfinished-state/verification obligations passed to fresh model after a blocker | [ImpasseBench](https://arxiv.org/abs/2610.31895), [HSC-Bench](https://arxiv.org/abs/2610.36523), [Handoff Debt](https://arxiv.org/abs/2606.02875), [CFRC](https://arxiv.org/abs/2609.13800), [workflow constraint erosion](https://arxiv.org/abs/2608.24569). Very recent direct neighbors occupy much of the obvious contribution. | NO-GO unless an unaddressed distinct construct is found |
| 7 | **Agent Memory Deletion/Forgetting** | Cross-tier deletion and subsequent reuse across workflows | [MemCut](https://arxiv.org/abs/2610.21405), [Deployment-Time Memorization](https://arxiv.org/abs/2606.10062), [execution-state unlearning](https://arxiv.org/abs/2609.04875). Direct papers already target exactly these properties. | NO-GO generic |
| 8 | **Authorization Revocation / Tool Schema Drift** | Cancel delegated effects or enforce tool version continuity | [Root-Scoped Quiescence](https://arxiv.org/abs/2609.21284), [ACG](https://arxiv.org/abs/2609.32428), [ToolContractGate](https://arxiv.org/abs/2610.33108), [ToolDriftBench](https://ieeexplore.ieee.org/abstract/document/11677805/). Direct method competitors, with historical close neighbors and contracts. | NO-GO generic |

### Additional late-discovered novelty threat

**[SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems](https://arxiv.org/abs/2610.21029)** (October 2026) investigates eight models and 1,500+ trajectories of coding agents negotiating shared tool access, including fairness/exclusionary coalitions. This directly reduces novelty potential of any 'agent resource negotiation' or 'emergent norms' concept. Relative ranking now favors accessibility-aligned execution and the temporal-invariance scoping pilot. It further weakens FairAgentQuota unless focused on a distinct systems or agent-level capability.

## A. AccessibleAct — minimal credible, independently verifiable experiment

**Hypothesis (not yet demonstrated):** Agent task-success metrics overstate *usable, independently verifiable completion* for blind/low-vision users; a verified-accessibility-aware execution/confirmation protocol produces higher usable-completion at controlled time and interaction cost than strong ordinary agents and accessible-interface baselines.

**Unit:** real task environment with assistive accessible interface, accessible action affordances, user intention, independent end-state oracle and user-verification action burden. Avoid using user disability labels as a proxy for skill; test actual environmental constraints and capabilities.

**Pilot:** choose 6–10 open-source, simulated state-changing web tasks (e.g., send/request confirmation, modify a document, reschedule an appointment), each with paired visual and accessibility-tree-only tool views. Compare: ordinary accessible UI automation, screen-reader/keyboard-aware baseline, agent policy with protected confirmations, and an oracle-guided policy. Evaluate completion, irreversible incorrect actions, verification steps, requests for help, repairability, and task time. Ideally co-design with accessibility experts and users; without that, claim only an accessibility-constraint *simulation*, not real user benefit. Use held-out task families.

**Kill:** if ordinary accessibility-tree agents plus existing protected confirmation match any proposed policy; if evaluation measures WCAG violations rather than end-user agent assistance; if no independent accessible end-state validator or credible user involvement.

## B. PreserveFirst — minimal credible experiment

**Hypothesis:** An agent can avoid destructive preemption by jointly satisfying incumbent and new task obligations through permitted replanning; distinguish end-state preservation from merely reaching a negotiated allocation. **This is not the discovery of the problem (ClashBench), nor the discovery of emergent negotiation (SCARCE).**

**Pilot:** fork a small sample of [ClashBench](https://github.com/TarferSoul/CLASHBench) cases; preserve both incumbent and new task health checks. Add legitimate waiting, alternate-resource and permission-controlled resolution opportunities. Compare: strong agent baseline with instruction to preserve, read-only tool limits, OS reservations/isolation, deterministic conflict resolver, and a candidate agent negotiation/replan policy. Score joint task success, incumbent protection, legitimate authorized preemption, delays, false denials, cost. Evaluate multiple model backbones and real tool calls. Do not invent an algorithm until strong baselines tested.

**Kill:** deterministic resource scheduling/protected permissions achieve equal or better joint utility and safety; no agent-specific advantage over generic process scheduling; cost/fairness confound.

## C. TimeShiftAgents — minimal scoping and strong no-go risks

**Hypothesis:** Under semantically equivalent timezone/locale representations, tool-using agents produce inconsistent external scheduled outcomes even when conventional language tests pass. The evaluation contribution is a *controlled metamorphic agent behavior* benchmark with time correctness, not a timezone library.

**Pilot:** author 10 paired schedule/recurrence/deadline scenarios crossing two simulated services with robust timezone-aware reference implementation; choose DST transitions and ambiguous/nonexistent local times as explicit policy cases; match final UTC instants and authorized intent; compare deterministic scheduler, tool-using agent, tool-using agent plus explicit zone conversions and final external-state checks. Freeze cases before running agents and report false-positive classifications for intentionally changed policy/time zones.

**Kill:** deterministic middleware solves all observed issues without agent-specific failure; no real models; domain narrow to trivial calendar formatting; existing metamorphic tests already evaluate the exact agent task.

## D. FairAgentQuota — pilot

Use a deterministic shared tool capacity simulation and real agents in two action domains; vary contention and task-priority disclosure. Baselines MUST include standard weighted-fair and deadline-aware schedulers, agent-only local budget prompts, and centralized exact scheduler. The agent-specific hypothesis is about *strategic cooperative deferral and information handling* under incomplete knowledge, not resource allocation by itself. Weak baseline results cannot support algorithm novelty.

## E. MultiPrincipalConsent — pilot

Two principals with independent rights to a shared operation, revocable midway; preserve unaffected authorization. Compare explicit deterministic two-party consent, hierarchical per-tool ACL, ACG-style incremental authorization graph and a plan-aware policy. Track unauthorized effects and unnecessary reapproval. If conventional ACL + scoped dual signatures suffices, kill method claim.

## Cross-cutting policy

- Target an **agentic AI paper**, not generic software tool integration; one clearly specified and demonstrably distinct phenomenon or method.
- Evaluate real model-driven agents with independent state-based graders. Never elevate toy mutational checks to model results.
- Minimum strong baselines, deliberate hard negatives, held-out settings, compute and human-verification costs, uncertainty intervals at independent task level.
- Record how "less crowded" was judged: scoped sample of closest papers, **not statistically representative counts**. An arXiv result can be posted yesterday and supersede the rationale tomorrow.
- Do not label a topic "novel" until exact competing protocols, code, measured results, and differentiating mechanism have been compared.

## Most efficient immediate decision

**Primary:** choose AccessibleAct if user-centric accessibility expertise and collaboration are available.  
**Secondary:** TimeShiftAgents is inexpensive to test but high risk of being an ordinary deterministic software-correctness problem.  
**Third:** PreserveFirst has an open benchmark but is now **more crowded than initially assessed** because SCARCE studies long-horizon negotiation over shared computation; explore only with a clearly separate question and strong SCARCE baseline.

**Current results:** *zero experiments on these five candidates*. This is a research scouting/prior-art artifact only, not evidence that a new method works.
