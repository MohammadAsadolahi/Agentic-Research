# Critical ranking of emerging agentic AI subfields — independent adversarial research brief

**Date:** 2026-11-02. **Coverage:** all **111** named areas from the earlier **18-family working atlas**, of which E=74 emerging agent-specific, T=33 transitional/agentification of established fields, M=4 mature. This ranking **does not assert** all 111 are new or objectively separate fields. Counting taxonomy labels is not bibliometric science.

## Executive verdict / decision

**Best risk-adjusted experiment-first field:** **cross-organization private-state verification and evidence acquisition in A2A agent interactions**, not generic "agents verifying each other". A²-Failures [arXiv:2610.19342](https://arxiv.org/abs/2610.19342) supplies >2,500 trajectories / 488 scenarios with distinct principals and explicit lack of unprompted peer fact-checking in tested systems. This is unusually direct *agent-specific observed failure*. **BUT** [A2A-CaseVerify, 2609.33914](https://arxiv.org/abs/2609.33914) already implements offline provenance-support verification, and ordinary authenticated logs, attestations and Bayesian value-of-information are formidable. Need an actual model-driven and closed-loop selective evidence acquisition setting where existing solutions trade off cost/utility poorly. This is an **experiment recommendation, not novelty established**.

**Best alternative with a public multi-agent executable benchmark:** the **Agentic Web with independently owned provider agents**. [AgentWebBench, 2604.10938](https://arxiv.org/abs/2604.10938), published at ICML 2026, already has code and central versus decentralized baselines. The seemingly obvious contribution "decentralized web agents" is already taken; classical federated IR is powerful.

**Best higher-risk fundamental science:** agent-population/ecological stability under churn and shared-state interference, but [Ecology of AI Agents, 2610.12436](https://arxiv.org/abs/2610.12436), [ScaleMAS, 2610.16120](https://arxiv.org/abs/2610.16120), [SCARCE, 2610.21029](https://arxiv.org/abs/2610.21029) cover much of the immediate territory. Needs hard math, extensive model runs and better-than-queueing/epidemic-model novelty.

**Best specialist route:** autonomous experimental evidence validity, with [q-devBench, 2610.41717](https://arxiv.org/abs/2610.41717) (37 tasks) and AIMS. Requires a domain collaborator and full accessible benchmark; original qdevbench GitHub repository returned 404 in an earlier lookup, while instrMCP existed.

**Revised judgment on past repeatedly recommended directions:** Continual learning / planning / memory are competitive mature fields; BOTTLED and Agent S4 claim the straightforward versions of skill bottling and interface evolution. [BOTTLED, 2610.08775](https://arxiv.org/abs/2610.08775) already beats us to the basic framing and [Agent S4, 2610.28601](https://arxiv.org/abs/2610.28601) does for interface evolution. Cross-agent verification looks better risk-adjusted, not "easy".

## Method

This is an **ordinal triage ranking**, not data-driven acceptance odds. It combines scientific significance, novelty headroom after direct existing algorithms, access to actual LLM tool executions/independent outcome oracles, infrastructure cost, and the extent to which the problem is *agent-specific*. We have checked primary arXiv records and some code for a core group of contenders; we have **not read every paper for all 111 items**. **Ranks 1–15 are the most deliberate judgments; 16–40 are conditional; 41–111 are low-confidence screening order only. Do not overinterpret adjacent ranks or assume their probabilities differ.** For readers who prefer fewer arbitrary ranks, read three bands: 1–15 priority experiments, 16–40 research watchlist, 41–111 lower current project fit / less checked.

**Rating scales:**
- **Type:** E = emerging as agent-specific research; T = transitional, the agent version of established research; M = mature.
- **Crowd:** L sparse, M moderately active, H crowded with direct recent work, VH very crowded/mature parent; **qualitative**, no arXiv paper-count data.
- **D:** difficulty inventing *publishable distinct method*: 1 easy → 5 exceptional. Higher is harder.
- **F:** feasibility for a small team to run credible real-agent evaluations: 1 poor → 5 favorable.
- **Impact:** potential scientific importance, 1–5; not publication chance.
- **Conf:** H/M best-effort direct primary source or benchmark checks for top 40; L lower-confidence field-based priors for remainder.

The ranking **prioritizes** the practical combination of novelty opportunity, source-backed open question and doable evaluation over raw sparsity of papers. Highly crowded but reproducible topics may outrank sparse topics that require inaccessible robots/clinical users or lack independent outcome measurement.

## Critical reading of the first 40 ranks

1. **cross-organization private-state verification** — Security, privacy and trust. Closest threat: A²-Failures (2610.19342); A2A-CaseVerify (2609.33914); classical value-of-information, attestations. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

2. **multi-principal outcome/side-effect measurement** — Agent evaluation and measurement science. Closest threat: A²-Failures; ClashBench; causal attribution, multiobjective welfare. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

3. **user-agent ↔ content-provider-agent coordination** — Agentic Web and information ecosystems. Closest threat: AgentWebBench (2604.10938); federated search. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

4. **decentralized information access and provider diversity** — Agentic Web and information ecosystems. Closest threat: AgentWebBench; federated IR and query optimization. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

5. **local/hybrid/cloud deployment across personal devices** — Agent runtime, distributed systems and serving. Closest threat: AgBench (2609.38652); classic edge/cloud scheduling. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

6. **scientific evidence lifecycle and claim validity** — AI agents for scientific discovery. Closest threat: q-devBench (2610.41717); AIMS; experimental design. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

7. **instrument-centered experimental metrology** — AI agents for scientific discovery. Closest threat: q-devBench (2610.41717); AIMS; classical metrology. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

8. **longitudinal deployed-agent comparability and rater drift** — Agent evaluation and measurement science. Closest threat: Reliability of AI Agents (2610.07003); IRT, change-point detection. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

9. **agent capability bottling and workload amortization** — Capability production and adaptive agent ecosystems. Closest threat: BOTTLED (2610.08775); ASI, SpeedRunner, fixed distillation. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

10. **budget allocation between learning/building/serving** — Capability production and adaptive agent ecosystems. Closest threat: BOTTLED; Capability-Gated Planning (2608.05085); optimal stopping. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

11. **effects on non-users and third-party principals** — Autonomous action governance and safety. Closest threat: ClashBench; PAPC; externality theory. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

12. **causal ecology of persistent shared digital worlds** — Agent population ecology and institutions. Closest threat: ScaleMAS (2610.16120); SwarmWorld; UCC (2604.01350). **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

13. **changing commitments with multiple human principals** — Human–agent co-agency and organizations. Closest threat: DotSpace; classic multi-party workflow and ACL. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

14. **persistent mixed human-agent social networks** — Human–agent co-agency and organizations. Closest threat: DotSpace (2610.40674); CSCW and groupware. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

15. **causal transport from simulator to deployed agent outcomes** — Agent evaluation and measurement science. Closest threat: UserArena; off-policy evaluation and sim-to-real. **Research gate:** demonstrate a genuine real-agent failure not handled by relevant classical and published agent methods at matched cost.

16. **agent-specific actual measured energy and resource accounting** — Agent runtime, distributed systems and serving. Closest threat: Environmental Impact (2609.32960), direct-power metering/green AI. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

17. **dynamic delegation, revocation and changed-policy effects** — Autonomous action governance and safety. Closest threat: AIP (2603.24775); capability security and authorization. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

18. **agent-created public artifact exposure and copying** — Agentic Web and information ecosystems. Closest threat: UCC (2604.01350); ScaleMAS; wiki-copying studies. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

19. **resilience under membership churn** — Agent population ecology and institutions. Closest threat: ScaleMAS; Ecology of AI Agents (2610.12436). Lower-priority candidate until executable task access and a distinct baseline residual are shown.

20. **agent replacement and handoff semantics** — Long-lived and persistent agency. Closest threat: persistent-agent protocols; workflow orchestration. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

21. **agent-to-agent protocol compatibility and evolution** — Agent networking and interoperability. Closest threat: Internet of Agentic AI; protocol layers and A2A standards. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

22. **collective epistemic reliability and dissent** — Multi-agent collaboration and social learning. Closest threat: PerMIT, agent misinformation papers; distributed evidence. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

23. **agent norms and endogenous institutions** — Agent population ecology and institutions. Closest threat: SCARCE (2610.21029); classic institutional economics. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

24. **cross-agent capability transfer in open ecosystems** — Capability production and adaptive agent ecosystems. Closest threat: Transactive Memory (2606.19911); skill transfer. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

25. **proof-derived permissions and checkable action certificates** — Security, privacy and trust. Closest threat: Verifiable Agentic Infrastructure; proof-carrying code. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

26. **agent-generated communication load and topology-induced traffic** — Agent networking and interoperability. Closest threat: agentraffic; MAServeBench; queueing theory. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

27. **human-attention scheduling over parallel agents** — Human–agent co-agency and organizations. Closest threat: When Should AI Agents Ask? (2610.41129); priority scheduling. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

28. **public-sector procedural legitimacy and benchmark validity** — Sector-specific autonomous institutions. Closest threat: Public Sector Requirements (2601.20617); administrative law. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

29. **agent-generated information ecosystem drift** — Social science and environmental impacts. Closest threat: CHASE; EcoGEO; ranking feedback. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

30. **scientific facility capacity allocation and experiment queues** — AI agents for scientific discovery. Closest threat: Agentic Economies for Science; classic facility scheduling. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

31. **cross-platform agent discovery and invocation** — Agent networking and interoperability. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

32. **semantic capability advertisement and verification** — Agent networking and interoperability. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

33. **asymmetric consent to agent-mediated communication** — Human–agent co-agency and organizations. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

34. **agent-in-the-loop industrial digital twin operation** — Embodied agents, robots and cyber-physical systems. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

35. **population-level externalities and resource coexistence** — Agent population ecology and institutions. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

36. **goal abandonment, suspension, resumption under changing authority** — Long-lived and persistent agency. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

37. **persistent goals and commitments across runs** — Long-lived and persistent agency. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

38. **authorized state transitions across tool domains** — Autonomous action governance and safety. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

39. **agentic public-health evidence collection and surveillance** — Sector-specific autonomous institutions. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

40. **healthcare agent harness and longitudinal clinical workflows** — Sector-specific autonomous institutions. Closest threat: See field-level direct precedents in prior frontier atlas; full-paper nearest-method audit not yet done.. Lower-priority candidate until executable task access and a distinct baseline residual are shown.

## All 111 subfields — full ordered list with crowding and novelty difficulty

| # | Agentic AI research area | Type | Crowd | D (harder ↑) | F (easier ↑) | Impact | Conf |
|---:|---|:---:|:---:|---:|---:|---:|:---:|
| 1 | cross-organization private-state verification | E | M | 4 | 4 | 5 | H/M |
| 2 | multi-principal outcome/side-effect measurement | E | M | 4 | 4 | 5 | H/M |
| 3 | user-agent ↔ content-provider-agent coordination | E | M | 4 | 4 | 5 | H/M |
| 4 | decentralized information access and provider diversity | E | H | 4 | 4 | 4 | H/M |
| 5 | local/hybrid/cloud deployment across personal devices | E | M | 4 | 3 | 4 | H/M |
| 6 | scientific evidence lifecycle and claim validity | E | M | 5 | 2 | 5 | H/M |
| 7 | instrument-centered experimental metrology | E | M | 5 | 2 | 5 | H/M |
| 8 | longitudinal deployed-agent comparability and rater drift | E | M | 4 | 4 | 4 | H/M |
| 9 | agent capability bottling and workload amortization | E | H | 5 | 3 | 5 | H/M |
| 10 | budget allocation between learning/building/serving | E | H | 5 | 3 | 5 | H/M |
| 11 | effects on non-users and third-party principals | E | M | 5 | 3 | 5 | H/M |
| 12 | causal ecology of persistent shared digital worlds | E | M | 5 | 3 | 5 | H/M |
| 13 | changing commitments with multiple human principals | E | M | 5 | 3 | 5 | H/M |
| 14 | persistent mixed human-agent social networks | E | M | 5 | 2 | 5 | H/M |
| 15 | causal transport from simulator to deployed agent outcomes | E | H | 5 | 2 | 5 | H/M |
| 16 | agent-specific actual measured energy and resource accounting | E | M | 4 | 3 | 3 | H/M |
| 17 | dynamic delegation, revocation and changed-policy effects | E | H | 5 | 3 | 5 | H/M |
| 18 | agent-created public artifact exposure and copying | E | H | 4 | 4 | 4 | H/M |
| 19 | resilience under membership churn | E | M | 5 | 2 | 5 | H/M |
| 20 | agent replacement and handoff semantics | E | M | 4 | 3 | 4 | H/M |
| 21 | agent-to-agent protocol compatibility and evolution | E | H | 5 | 3 | 4 | H/M |
| 22 | collective epistemic reliability and dissent | E | H | 5 | 3 | 5 | H/M |
| 23 | agent norms and endogenous institutions | E | H | 5 | 3 | 5 | H/M |
| 24 | cross-agent capability transfer in open ecosystems | E | H | 5 | 3 | 4 | H/M |
| 25 | proof-derived permissions and checkable action certificates | E | H | 5 | 2 | 5 | H/M |
| 26 | agent-generated communication load and topology-induced traffic | T | H | 5 | 2 | 3 | H/M |
| 27 | human-attention scheduling over parallel agents | E | H | 5 | 4 | 4 | H/M |
| 28 | public-sector procedural legitimacy and benchmark validity | E | M | 4 | 3 | 4 | H/M |
| 29 | agent-generated information ecosystem drift | E | H | 5 | 3 | 4 | H/M |
| 30 | scientific facility capacity allocation and experiment queues | E | M | 5 | 2 | 4 | H/M |
| 31 | cross-platform agent discovery and invocation | E | H | 5 | 3 | 4 | H/M |
| 32 | semantic capability advertisement and verification | E | H | 5 | 3 | 4 | H/M |
| 33 | asymmetric consent to agent-mediated communication | E | M | 5 | 1 | 4 | H/M |
| 34 | agent-in-the-loop industrial digital twin operation | E | M | 5 | 2 | 4 | H/M |
| 35 | population-level externalities and resource coexistence | E | H | 5 | 2 | 5 | H/M |
| 36 | goal abandonment, suspension, resumption under changing authority | E | M | 4 | 3 | 4 | H/M |
| 37 | persistent goals and commitments across runs | E | H | 4 | 3 | 4 | H/M |
| 38 | authorized state transitions across tool domains | E | H | 5 | 3 | 5 | H/M |
| 39 | agentic public-health evidence collection and surveillance | E | M | 4 | 2 | 4 | H/M |
| 40 | healthcare agent harness and longitudinal clinical workflows | E | H | 4 | 2 | 5 | H/M |
| 41 | automatically adapting scientific-agent benchmarks | E | M | 5 | 3 | 4 | L |
| 42 | autonomous web access reciprocity, terms and compensation | E | M | 5 | 3 | 4 | L |
| 43 | benchmark contamination via agent web search | E | M | 5 | 3 | 4 | L |
| 44 | distributed agent workflow lifecycle and cross-org coordination | E | M | 5 | 3 | 4 | L |
| 45 | message reception/attention markets and inbox rules | E | M | 5 | 3 | 4 | L |
| 46 | agent-facing content optimization and answer-engine effects | T | H | 5 | 3 | 4 | L |
| 47 | search-time contamination, provenance and evidence quality | T | H | 5 | 3 | 4 | L |
| 48 | task-oracle reliability, evidence and reward hacking | T | H | 5 | 3 | 4 | L |
| 49 | trajectory, process and external-state evaluation | T | H | 5 | 3 | 4 | L |
| 50 | cumulative multi-agent safety under scaling populations | E | M | 5 | 3 | 4 | L |
| 51 | fluid agent organizations and institutional accountability | E | M | 5 | 3 | 4 | L |
| 52 | runtime-independent behavioral continuity | E | M | 5 | 3 | 4 | L |
| 53 | human-agent co-adaptation longitudinally | T | H | 5 | 3 | 4 | L |
| 54 | irreversible-action counterfactual selection | T | H | 5 | 3 | 4 | L |
| 55 | recovery from uncertain effectful actions | T | H | 5 | 3 | 4 | L |
| 56 | runtime guardrails and human escalation | T | H | 5 | 3 | 4 | L |
| 57 | stale skills/experience in changing environments | T | H | 5 | 3 | 4 | L |
| 58 | agent identity and provenance across delegation | E | H | 5 | 3 | 4 | L |
| 59 | AI scientist benchmark evolution and validity | E | M | 5 | 2 | 4 | L |
| 60 | composition safety of separately benign agent skills | E | H | 5 | 3 | 4 | L |
| 61 | independent agents adapting to evolving tools and services | E | M | 5 | 3 | 4 | L |
| 62 | population thresholds and ecological safety | E | M | 5 | 3 | 4 | L |
| 63 | privacy propagation and data externalities | E | H | 5 | 3 | 4 | L |
| 64 | reproducible laboratory-agent evaluation worlds | E | M | 5 | 2 | 4 | L |
| 65 | adaptive experiments and closed-loop wet/dry labs | T | H | 5 | 2 | 4 | L |
| 66 | autonomous hypothesis formation and discovery | T | H | 5 | 2 | 4 | L |
| 67 | executable skill induction and adaptive code artifacts | T | H | 5 | 3 | 4 | L |
| 68 | herding, cascades, collusion and network contagion | T | H | 5 | 3 | 4 | L |
| 69 | live adaptive cybersecurity agent-vs-agent testing | T | VH | 5 | 3 | 4 | L |
| 70 | prompt injection and persistent-artifact compromise | T | VH | 5 | 3 | 4 | L |
| 71 | skill provenance, dependency and supply-chain integrity | T | H | 5 | 3 | 4 | L |
| 72 | agent-society simulation process validity vs final outcomes | E | M | 5 | 3 | 4 | L |
| 73 | agent-specific insurance and risk accumulation | E | M | 5 | 3 | 4 | L |
| 74 | agent-to-agent payment, escrow and fulfillment | E | M | 5 | 3 | 4 | L |
| 75 | agent-tool wait and dynamic DAG-aware serving | E | H | 5 | 3 | 4 | L |
| 76 | autonomous service markets and contracts | E | M | 5 | 3 | 4 | L |
| 77 | autonomous-agent energy/water/carbon observability | E | M | 5 | 3 | 4 | L |
| 78 | coalition formation and collaborative discovery | E | M | 5 | 3 | 4 | L |
| 79 | collective social feedback and behavioral contagion | E | M | 5 | 3 | 4 | L |
| 80 | economic externalities of agent-mediated business actions | E | M | 5 | 3 | 4 | L |
| 81 | macro-social externalities and accountability of delegation | E | M | 5 | 3 | 4 | L |
| 82 | population-level evidence verification | E | M | 5 | 3 | 4 | L |
| 83 | principal-agent incentives and strategic delegation | E | M | 5 | 3 | 4 | L |
| 84 | stateful agent workflow workloads on inference backends | E | H | 5 | 3 | 4 | L |
| 85 | tool-interface evolutionary adaptation | E | H | 5 | 3 | 4 | L |
| 86 | cross-agent teaching and skill transfer | T | H | 5 | 3 | 4 | L |
| 87 | ecological risk of synthetic content and data recycling | T | H | 5 | 3 | 4 | L |
| 88 | heterogeneous specialist teams | T | H | 5 | 3 | 4 | L |
| 89 | resource auctions, quotas and agent-provider reputation | T | H | 5 | 3 | 4 | L |
| 90 | semantic agent transactions and durable effect logs | T | VH | 5 | 3 | 4 | L |
| 91 | task decomposition and manager-worker orchestration | M | VH | 5 | 3 | 4 | L |
| 92 | autonomous cyber defense audit-and-repair | E | H | 5 | 3 | 4 | L |
| 93 | longitudinal autonomy in CI/release maintenance | E | H | 5 | 3 | 4 | L |
| 94 | scientific software reproduction fidelity | E | H | 5 | 3 | 4 | L |
| 95 | education and assistive/accessible agents | T | H | 5 | 2 | 4 | L |
| 96 | finance, procurement and supply-chain operational agents | T | H | 5 | 2 | 4 | L |
| 97 | formal proofs jointly synthesized with executable code | T | VH | 5 | 3 | 4 | L |
| 98 | legal and regulatory workflow agents | T | H | 5 | 2 | 4 | L |
| 99 | multi-agent code review and merge conflicts | T | VH | 5 | 3 | 4 | L |
| 100 | repository coding agents and SWE task success | T | VH | 5 | 3 | 4 | L |
| 101 | agentic wireless digital twin calibration | E | M | 5 | 2 | 4 | L |
| 102 | embodied collective intelligence and multi-robot state sharing | E | M | 5 | 2 | 4 | L |
| 103 | federated robot fleet authority and recovery | E | M | 5 | 2 | 4 | L |
| 104 | connected autonomous production and predictive maintenance | T | H | 5 | 2 | 4 | L |
| 105 | robotic manipulation, navigation, real-world adaptation | T | H | 5 | 2 | 4 | L |
| 106 | causal tool-action models | T | VH | 5 | 3 | 4 | L |
| 107 | continual skill adaptation and forgetting | T | VH | 5 | 3 | 4 | L |
| 108 | open-ended curriculum/self-evolving agents | T | VH | 5 | 3 | 4 | L |
| 109 | memory retrieval and compression | M | VH | 5 | 3 | 4 | L |
| 110 | metacognition and self-correction | M | VH | 5 | 3 | 4 | L |
| 111 | tool-use planning and replanning | M | VH | 5 | 3 | 4 | L |

## High-value primary anchors and strongest blockers (sources verified this round or preceding scans)

**Cross-owner A2A and verifiable evidence**
- [A²-Failures](https://arxiv.org/abs/2610.19342) (Oct 14): >2,500 actual recorded agent runs / 488 scenarios, 20 failure types. Observation that tested agents did not spontaneously fact-check other agents is model-and-setting-specific, not a universal law.
- [A2A-CaseVerify](https://arxiv.org/abs/2609.33914) (Sept 27): existing *offline* case-level verification via deterministic evidence graphs and Merkle links, illustrated with one canonical bundle, 13 mutations and one SDK bundle. Distinguish this from online *choosing which independent claims to test*.
- [AIP](https://arxiv.org/abs/2603.24775) (Mar 25): authorization/identity/delegation with a technical implementation; verifying signatures and capability tokens is NOT our novelty.

**Distributed information and shared worlds**
- [AgentWebBench](https://arxiv.org/abs/2604.10938) (Apr, ICML): independently owned website agents and user agents; methods include central and distributed retrieval. Public [repo](https://github.com/cxcscmu/AgentWebBench) confirmed in preceding GitHub audit.
- [No Attacker Needed](https://arxiv.org/abs/2604.01350) (Apr): unintended cross-user contamination already measured.
- [ScaleMAS](https://arxiv.org/abs/2610.16120) (Oct): persistent shared substrate and fault tolerance already addressed.
- [Inbox as Coordination Primitive](https://arxiv.org/abs/2610.36264) (Oct): large-society read policies, recipient-side attention and pricing already methodized.
- [SCARCE](https://arxiv.org/abs/2610.21029) (Oct): emergent norms and institutional behavior studied in genuine coding-tool agent trajectories.
- [Ecology of AI Agents](https://arxiv.org/abs/2610.12436) (Oct): population threshold *theory* already exists; not an observed universal field threshold.

**Economics and capability production**
- [Agent in a Bottle](https://arxiv.org/abs/2610.08775) (Oct): workload-capability amortization, fixed distillation baselines, public [repo](https://github.com/aktsonthalia/bottled).
- [Capability-Gated Planning](https://arxiv.org/abs/2608.05085) (Aug): a formal method for long-horizon capability-building investment, an important classical/agentic counterexample to naive active experimentation.

**Action environments, measurement and human oversight**
- [AgBench](https://arxiv.org/abs/2609.38652) (Sept): personal devices vs cloud/hybrid agent execution, direct competing empirical work.
- [q-devBench](https://arxiv.org/abs/2610.41717) (Oct 30): 37 stateful virtual scientific tool tasks, measurement rubric 70–83% vs scientific analysis 28–46%—criterion rates, NOT overall task success.
- [Reliability of AI Agents](https://arxiv.org/abs/2610.07003) (Oct): 2,611 observational interviews and reviewer drift; not causal policy efficacy.
- [When Should AI Agents Ask?](https://arxiv.org/abs/2610.41129) (Oct 30): PCP scheduling policy already has formal approximation results; ordinary human-attention queue scheduling not blank slate.
- [Agent S4](https://arxiv.org/abs/2610.28601) (Oct): autonomous evolving interfaces already algorithmically demonstrated.
- [WebAnything](https://arxiv.org/abs/2610.37786) (Oct): source-grounded executable web worlds and many accepted tasks already addressed.
- [Public Sector Benchmark Requirements](https://arxiv.org/abs/2601.20617) (Jan): reports none of >1,300 existing benchmark papers meets all public-sector criteria, but this is benchmark-design evidence, NOT a novel method.

## Decision experiment: A2A cross-principal selective evidence acquisition

**Null hypothesis:** Strong standard methods—mandatory independent evidence checking, digitally signed/provenance-checked assertions, deterministic case verification, Bayesian risk/expected-value sampling, and a sufficiently competent LLM peer critic—achieve the same legitimate task success, accepted claim correctness, privacy and verification cost as any new policy in private-state A2A interactions.

**Pilot environment:** A controlled local service environment with multiple independently owned model-driven tool-using agent roles, each with private state and permission-restricted retrieval tools. Task families spanning schedule/commerce/customer support/technical service, with separate sealed ground truth for each principal. Agent B may claim a fact or completed action; Agent A must decide whether to rely on it, query a separate evidence source, request proof, or decline; all actual external state changes are verified independently.

**Outcomes:** end-to-end authorized outcome success, correctly accepted/rejected claims, third-party impact, privacy violations, verification queries/cost, cumulative latency and task success after verification. Report full Pareto frontier rather than only percent detected. Freeze holdouts across different service families and peer strategies; include all-honest cheap-claim controls, benign uncertainty, noisy but true claims and costs/verification access constraints. Avoid hidden oracle labels in the agent's prompt or verifier.

**Mandatory comparison:** no verification; always verify; signed attestation and deterministic A2A-CaseVerify where evidence available; Bayesian evidence acquisition / VOI; a model-mediated independent critic; simple risk/claim-priority rules; at least one *real A2A baseline* from A²-Failures contexts if executable; any proposed new mechanism. Match model calls, budgets, tools and task information. The main missing infrastructure is a verified re-runnable agent-harness/benchmark, NOT just log data.

**Kill gates:**
1. A real model-driven A2A agent baseline shows no substantial failures, or a standard existing method removes them under the same utility/verification budget.
2. A proposed method merely adds a signature, provenance chain, ACL, risk threshold, critic, or static check already provided by prior work.
3. Gains appear only against weak agents, one handcrafted test domain, or unblinded/evaluator-leaked fixtures.
4. Correctness improvement disappears once privacy, tool charges, delays, opportunity costs and useful task acceptance are included.
5. No stable independently verified outcome across different models/domains.

**Alternative #2 (Agentic Web):** replicate 1–2 source-backed AgentWebBench tasks with existing central/tool-selected/multi-agent methods at matched calls; then test genuinely independent provider policy constraints. **Kill** if deterministic federated query selection or existing agent methods already yield same utility/cost/provider coverage.

**Decision requested:** do not fund a novel algorithm yet. First fund pilot that establishes a **real, baseline-resistant agent-specific failure**. If no residual, change field—no commitment to a buzzword or repeated indefinite surveys.

## Self-critique and uncertainty

1. **No objective crowd counts.** Ratings are editorial and field-dependent. Absolute arXiv paper counts would require a preregistered query, disambiguation and coverage of other venues. None was done.
2. **No externally validated acceptance estimates.** Publication is a function of method, experimental evidence, reviewer fit and timing, not just field age.
3. **111 entries are not 111 new disciplines.** Many are adjacent, nested, or old computer science with agents applied. Types are assessor judgments and may be debated. This is precisely why the atlas includes old topics as negative controls.
4. **Novelty difficulty in the tail is deliberately pessimistic.** For entries 41–111 no exhaustive closest-method audit was performed. Those rows should be read as *screening judgments*.
5. **A²-Failures logs are evidence of failures, not proof that a freely usable executable live environment exists.** Verify licensing, assets and reproducibility before committing.
6. **Direct local model/API access, GPU and subject-matter expertise are unknown.** Pilot feasibility is relative. Our project already has GitHub Actions and model-independent CI, not an established full paid LLM test rig.
7. **Anthropomorphic descriptions of 'independent agents' need operational detail.** Separate principal private state/authorization and genuine model-directed tool choices are necessary; a single orchestrator simulating roles is not proof.
8. **Better specialty expertise could change rankings drastically.** A robotics lab might prioritize embodied fleets; a metrologist might favor experiment validity; a distributed-systems expert could exploit transaction semantics at much greater depth.
9. **Opportunity for novel method ≠ gap proven.** Cross-principal selective verification may be classical VOI with a new label. That is the top hypothesis to attack, not an assertion of firstness.
10. **Time sensitivity.** This ranking is current to November 2, 2026; new papers could invalidate the priority next week.

## Reproducibility of this screening document

The exhaustive 111-row map derives from the existing [master atlas](https://github.com/MohammadAsadolahi/Agentic-Research/blob/research/agentic-frontier-master-atlas-2026-11-02/research/2026-11-02_AGENTIC_AI_MASTER_FRONTIER_ATLAS.md). The top-40 positions were set by deliberate editorial synthesis from multiple prior frontier notes and this round's primary source audits. Rows 41–111 are ordered by a **rough family relevance prior**, then emerging/transitional/mature status and lexical tie-break; their linear order is **not** a measurement of quality, crowding or uniqueness.

**Current genuine result:** ranked methodological hypothesis and sourced decision-gate; **0 new agent experiments, 0 original algorithm, 0 validated publishable gap**.
