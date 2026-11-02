# New agent-native subfields: frontier arXiv scan, November 2, 2026

**Decision level: choose a field, NOT a manuscript title.** Source base: targeted 2026 arXiv abstract/HTML inspection on 2026-11-02, focused on agent populations, agent-to-agent attention, and knowledge commons; not a systematic review, full-paper code audit, or a publication probability estimate. A *young* field does not make a novel method or acceptance easy. Parent sciences (ecology, networks, control theory, distributed systems, queuing, game theory, institutional economics) are mature and must be compared.

## Revised field ranking

### A. Ecological dynamics and resilience of persistent AI-agent populations — preferred foundational field

**Different unit of analysis:** the population changes as agents enter, exit, specialize and modify shared state; effects can be nonlinear in density, coupling and diversity. Different from a fixed-size multi-agent task benchmark.

**Primary arXiv anchors:**
- [Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff](https://arxiv.org/abs/2610.12436), submitted **Oct 8 2026**. Models ecological safety using population growth and collaboration-induced threshold. **Direct theoretical novelty threat**: population threshold and Allee effect already studied, do not call them first.
- [SwarmWorld: Stigmergic technological evolution in societies of language-model agents](https://arxiv.org/abs/2608.26081), **Aug 26 2026**. Agents evolve durable artifacts, differentiated roles, and functional portfolios. **Direct empirical novelty threat**: spontaneous differentiation and persistent artifacts already shown.
- [AI Agent Economics: Can Autonomous Economic Behavior Emerge among AI Agents under Minimal External Conditions?](https://arxiv.org/abs/2608.03076), **Aug 4 2026**. Verified productive work and allocation rights produce autonomous economic organization; emergent institutions not new by itself.
- [Sustained Heterogeneity: an emergent collective mechanism in LLM-driven traffic](https://arxiv.org/abs/2608.29174), **Aug 29 2026**. Critical penetrations/collective instability in a physically coupled controller system, proof population dynamics can already be studied at phase-transition level.
- [SCARCE](https://arxiv.org/abs/2610.21029), **Oct 15 2026**. Long-horizon multi-agent coding and endogenous informal institutions. Does not study varying autonomous population as central unit, but strong threat to broad agent-society novelty.

**Why scientifically hard:** nonlinear feedback, finite resources, endogeneity, causal interventions on agent density/turnover/network structure, distinction between scripted emergence and model-driven behavior, and generalization across populations and models. Need reliable state-level outcomes, controls, phase-transition uncertainty, and not just pretty swarm visualizations.

**Possible residual research areas, all unverified:** resilience to churn of useful agent populations, early-warning indicators for collapse of cooperation under endogenous role turnover, causal links from shared infrastructure dependencies to population-level tipping points, or safety/utility boundaries for scaling non-adversarial agents. The October ecology paper already studies takeoff in a cybersecurity capability setting; *do not assume* benign resilience is open without a detailed closest-paper audit.

**Falsification probe before any method:** Simulate 3–5 functional, independently verifiable tool domains in a small reproducible multi-agent world. Gradually vary N, agent churn, communications and shared tool contention while holding per-agent capabilities/model budget fixed; measure task throughput, inequality, externality rate, sustained survival of useful workflows, network connectivity and reliability. Compare deterministic scheduling, scripted multi-agent policies, simple population-dynamics models, strong model-based coordinators, and LLM tool-using agents. Precommit predictions; replicate at held-out population ranges. Kill claim if phenomenon is fully explained by classical queueing/capacity and no agent-specific mechanism remains.

### B. Attention governance and message-reception economics for agent societies — best for practical new-method feasibility

**Different scarce resource:** recipients have finite context/tokens and must decide what to read, not only how messages are routed. Open-ended agent-to-agent communication naturally creates overload, contention and strategic incentives.

**Direct anchors:**
- [The Inbox as a Coordination Primitive for LLM Agent Societies](https://arxiv.org/abs/2610.36264), submitted **Oct 26 2026**, explicitly frames receiver-governed message intake, retention, sender pricing and reply terms; simulated up to 16k agents. **Very strong, immediate competitor**. Inbox/pull, prioritization, refundable deposits and sender-price policy **not** new.
- [Agentic Societies Need a Social Harness](https://arxiv.org/abs/2609.17527), revised **Oct 24 2026**, addresses honest agent coordination failures, malicious communication, and layers of social interaction management. **Social harness concept already proposed**.
- [Selective and Hybrid-State Communication for Latent Multi-Agent Systems](https://arxiv.org/abs/2610.37779), **Oct 27 2026**, selective latent communication optimizing context-transfer efficiency; distinct representation but matters to costs.
- [Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems](https://arxiv.org/abs/2610.01042), **Oct 1 2026**, matched-compute communication intervention, important experimental control.
- [SwarmWorld](https://arxiv.org/abs/2608.26081) shows persistent shared-environment communication without messaging can also coordinate agents; need nonmessage baseline.

**Why difficult:** adversarial messages, deadlines, hidden task dependencies, nonstationary senders, constrained context, information value of messages depends on later actions, network effects. Novelty could require a distinct policy or guarantees concerning *multi-task recipient utility* and *network-level fairness*, not merely filtering/ranking inbox messages. Must compare to the Inbox paper, priority queues, deficit-round-robin, standard queueing and bandit information selection, and a tool-using LM controller.

**Feasibility probe:** Run model-driven negotiation/task-discovery agents in a finite inbox environment, with different traffic rates, noise, deadline distributions and asymmetric message relevance. Verify tasks by oracle. Compare FIFO, random, static rank, refundable deposits, explicit inbox policies, sender throttling, classical quota scheduling, and agent-specific selection. Measure completed legitimate negotiations per token and wall time, starved principals, total compute and failures under held-out traffic. Do NOT invent an algorithm until closest baselines have weaknesses.

### C. Epistemic commons and information contagion in agent populations — interesting but strong direct incumbents

**Research object:** public agent-generated experience, claims and methods can change behavior of other agents, potentially causing runaway spread of bad rules or emergent correction.

**Direct anchors:**
- [A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms](https://arxiv.org/abs/2609.04170), **Sep 3 2026**: 100 agents, spontaneous exploit diffusion via shared library and messaging, and unprompted auditing/whistleblowing. **Direct evidence and competing phenomenon**.
- [Memory Contagion](https://arxiv.org/abs/2606.23195), **June 22 2026**: biased evaluator influence propagates through agent memory even with idealized consolidation.
- [PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust](https://arxiv.org/abs/2610.28987), **Oct 20 2026**: verification gate, trust aggregation and shared community memory up to 90 agents. **Strong method competitor to naive validation/consensus.**
- [Where Reliability Lives](https://arxiv.org/abs/2609.03192), **Sep 2 2026**: controlled epistemic institutional interventions and fixed institutional enforcement under swapped cognition. **Do not claim institution/cognition disentanglement first.**

**Viable if** a new population-level transmission/control mechanism survives PerMIT (integrity checking), sealed validators, standard quorum/consensus methods, restricted information flow and classical epidemic threshold predictions, with actual agent decisions rather than programmed infection. Likely higher expense and security nuance.

## Rejected default directions despite sounding new

- Generic "agent societies form norms": SCARCE, AI Agent Economics, SwarmWorld, [Behavior Is Not Enough](https://arxiv.org/abs/2609.26481) and POLIS already study social mechanisms.
- Generic reputation and agent advertising: established proposals and evaluations.
- Generic memory contagion or community checking: Memory Contagion and PerMIT.
- Generic latency/token efficient agent communication: inbox, social harness and latent communication direct papers.
- Generic ecological population threshold: October 2026 ecology theory already introduces it.

## Provisional field decision

**Best match to 'very hard, early-stage, broad room for distinct findings': A, population ecology of autonomous agents.** Not a low-effort project: likely publishable only with careful causal experiments, calibrated population dynamics, strong non-LLM controls and more than one environment/model. A theoretical novelty may require ecology/control-theory sophistication.

**Best match to 'new algorithm feasible for a small team': B, agent-society attention governance.** Strong 26 Oct direct paper preempts simplistic ideas; specific method remains **unknown**.

**Third:** C, epistemic commons, if distinct mechanism beyond PerMIT and related institutional work can be isolated.

**Proposed research sequence:** Review the FULL methods, benchmarks and open source code of the 2 strongest papers in each top track; reproduce a baseline on real model-driven agents; define a falsifiable *new phenomenon* before inventing a method. Conduct an independent external novelty attack then either pick a method or kill the track.

## Honesty controls

No field can be described as 'easy to publish'. No new agentic method, benchmark, real agent experiment, or empirical result is established by this paper scan. This report is not a paper. Relative crowding was judged qualitatively from scoped recent-source search and could be wrong. No acceptance probability is assigned.
