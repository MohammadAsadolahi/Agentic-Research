# Deep frontier scan: agent-native research opportunities (2026-11-02)

**Purpose:** identify emerging *fields* in agentic AI that could eventually support an original scientific **method**, not just build an app or rediscover existing verification. **Evidence:** targeted review of 2026 original arXiv abstracts and available full-text, one peer-reviewed ACM/Springer journal article, an actual shared-wiki incident reconstruction, and older parent-discipline concepts; citations are links below. **Not** a systematic arXiv census, exhaustive full-text audit, originality proof, or estimate of acceptance probability.

**Verdict:** Most high-level "AI agent populations" first papers have ALREADY appeared in 2026. The strongest actionable next field is **causal ecology of agent-created shared environments**, followed by **cross-principal externality accounting** and **independent cross-principal verification**. Even these have serious direct competitors and are *unverified novelty openings*, not free wins.

## What is DIFFERENT from the previous literature scan?

Earlier research prioritized general agent-population ecology and inbox attention. This broader search exposes the importance of:
- agents leaving changes in **external shared state** that outlive their sessions, and those changes affecting independently owned future agents, even without a direct communication channel;
- differences between a *local task success*, each *principal's utility*, and a *third party's outcome*, especially across A2A services;
- **causal identification** of agent-induced external effects: observational archives often lack read/access logs and independently measured task outcomes;
- systems of agent interaction across **trust boundaries and separate private environments**, beyond orchestrator-worker benchmarks.

These are research fields/subfields, not yet titles or methods.

## Ranked opportunity map (subjective, relative ratings)

| Priority | Field-level area | Why emerging and hard | Direct novelty blockers | Feasibility / decision |
| --- | --- | --- | --- | --- |
| **A1** | **Causal ecology of agent-created shared environments** (external artifacts, public knowledge, persistent downstream behavior) | Separate agents can alter each other's *environment* without direct messages; nonlinear effects, selection biases, observation vs causation | Copying Explains (Sept), Mechanics of a Swarm (Sept), No Attacker Needed (Apr), SkillRelayGuard (Oct), information contagion, classical information cascades | **Best first empirical probe** with contained stateful tool sandbox, independent task oracles; conditional GO |
| **A2** | **Agent ecosystem externality accounting** (who benefits, who bears hidden costs) | Successful individual agents can harm other principals, later users and shared infrastructure in ways that ordinary task metrics do not capture | A²-Failures (Oct), agent bullwhip (May), ClashBench, Agent Bazaar, PNAS whistleblower, established externality economics | Conditional GO only if task/third-party counterfactuals are causally identified, not one more scalar ethics score |
| **A3** | **Cross-principal verification economics** (independent evidence acquisition between agents with different owners) | Private state and unverifiable factual claims across agent organizations; audit is costly, potentially strategic | A²-Failures (Oct; 2,500+ runs), A2A protocol mechanism design (Aug), current formal contract/payout work, classic costly verification | Conditional GO for actionable study; no generic "peer checks" or certificate method claim |
| **B1** | **Population resilience and recovery under churn** (retirement, restart, replacement, network fragmentation) | Fitness/population is endogenous; population can collapse or recover with network externalities | Ecology of AI Agents (Oct), Population Physics (Sept), SwarmWorld, TerraLingua and older ecology | Deep science, expensive real agents, strong phase-transition/stat-physics baselines |
| **B2** | **Agent-driven economic infrastructure and economic recourse** (authorization→payment→fulfillment over providers) | Separate authorities, settlement and delivered outcomes; partial failure, delays, contractual losses | Formal Analysis of Agent Payment Protocols (Aug), PACT IETF draft, Agent Bazaar, Matching Tasks to Agents (Oct) | Serious distributed systems/security; specific protocol properties may be highly publishable but not "easy" |
| **B3** | **Agent attention and communication markets under private interests** | Message triage with asymmetric sender/recipient utilities, dependency graphs, deadlines | Inbox Primitive (Oct 26) already tests pull, deposits, read/retain/pricing; Social Harness, communication verification | Promising implementation but generic inbox/protocol method NO-GO |
| **B4** | **Self-organized institutional robustness** (endogenous norm effects under evolving membership, adversarial capture) | Institution-level feedback, causal counterfactuals, heterogeneous role structures | SCARCE (Oct), When Do Institutions Beat Intelligence? (Aug), AI Agent Economics (Aug), classical mechanism design | High-methodology burden, direct strong papers |
| **C1** | **Information cascades, misinformation and collective epistemic resilience** | Feedback propagates false evidence and consensus, even without attacker | Herding and Runaway Cascades (Oct), When Truth Is Distributed (Aug), PerMIT, existing social influence/contagion methods | **Do not claim general phenomenon new**; find markedly new causal intervention first |
| **C2** | **Generic market stability / Sybil agents** | Autonomous trades and coordination under strategic identities | Agent Bazaar (May) already has collapse, Sybil fraud and trained intervention; matching contracts (Oct) | Generic claim NO-GO |
| **C3** | **Generic agent benchmark contamination and verification** | Public search can leak answers; agent may optimize its judge | Search-Time Contamination (June), A Trust Layer (Oct), Rethinking Verification (Oct) | Strong established immediate baselines, generic claim NO-GO |
| **C4** | **Generic temporal tool state/agent drift, memory contamination** | Stale events, cross-session inappropriate reuse | No Attacker Needed (Apr); SkillRelayBench (Oct); several durable-agent methods | Generic claim NO-GO |
| **C5** | **Infrastructure-agent one-task reliability** | Operational state, distributed invariants, unsafe side-effects | InfraBench (Aug), InfraDev (Oct), existing distributed systems controls | Unless population-scale externality, not priority |

## Critical source matrix (direct arXiv records; status from abstract, NOT independent replication)

### Agents create persistent shared worlds

1. [The Mechanics of a Swarm: A Reproducible External Reconstruction of an Unintended Agent-Coordination Episode on a Third-Party Wiki](https://arxiv.org/abs/2609.12748) (Sept 2026). Externally reconstructed 14,591 revisions, 3,103 user names and around 876 inferred agent episodes; **missing successful-read logs, harness messages and ground-truth task outcomes prevent causal outcome attribution**. Key missing infrastructure: observation/exposure + impact measurements.
2. [Copying explains the collective behavior of AI agents in the wild](https://arxiv.org/abs/2609.09150) (Sept). Models agent conventions on the same wiki as copying from visible local state. **Does NOT establish an original idea to study copying**; this is direct observational competitor. Reconstructed exposure is not an intervention.
3. [No Attacker Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents](https://arxiv.org/abs/2604.01350) (Apr). Shows benign shared persistence can silently contaminate other users; artifact carryover is already studied. Distinguish **independently operated agents sharing external world** from one agent's shared memory; not a guarantee of distinct novelty.
4. [Understanding and Mitigating Cross-Session Attacks via Persistent Artifacts in Agent Skill Composition](https://arxiv.org/abs/2610.13227) (Oct). SkillRelayBench and provenance-sensitive SkillRelayGuard already cover malicious persistent skill artifacts across sessions. New work on provenance tags alone is NO-GO.
5. [Search-Time Contamination in Deep Research Agents](https://arxiv.org/abs/2606.05241) (June). Benchmark metadata/answer retrieval inflates evaluation. General contamination detection already studied.

### Cross-principal agent interaction and externalities

6. [Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States](https://arxiv.org/abs/2610.19342) (Oct). More than 2,500 runs, 488 cases, and 20 A2A failure classes, across private agent states and separate principals. Critically reports that tested agents do not spontaneously fact-check peers. **Direct baseline/dataset**, not an unmeasured hypothesis.
7. [Reliability and Effectiveness of Autonomous AI Agents in Supply Chain Management](https://arxiv.org/abs/2605.17036) (May). Agent bullwhip effect: feedback amplification of decision unreliability, with mechanism and RL mitigation. Network-level effects not newly identified by our project.
8. [Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces](https://arxiv.org/abs/2605.17698) (May). Model-based markets with crash and Sybil deception, welfare/accuracy metrics, and trained 9B model intervention; generic agent market collapse and market-alignment methods **already demonstrated**.
9. [Whistleblowers can contain the unethical externalities of human–AI delegation](https://doi.org/10.1073/pnas.2536668123) (PNAS, July). Human principal and agent misalignment externalities under actual incentive experiments; third-party effect is not our new construct.
10. [Matching Tasks to Agents: Mechanism Design for Multi-Agent Contracts](https://arxiv.org/abs/2610.31002) (Oct 22). Strong theoretical prior work on hidden effort and success-contingent principal-agent assignment. Beware confusing **economics' generic "agents"** with experimental LLM tool agents: paper is contract theory, not necessarily an LLM evaluation.
11. [Do LLM Agents Negotiate Rationally? A Mechanism-Design Framework for Verifiable Multi-Agent Interaction over A2A/MCP](https://arxiv.org/abs/2608.14613) (July). Structural protocol and verification already researched in modern agent context.

### Agent economics, population dynamics and institutions

12. [A Formal Analysis of Agent Payment Protocols](https://arxiv.org/abs/2609.00060) (Aug 30). Formalizes x402, MPP, ACP, AP2 with Tamarin, 86 verification cases and 40 newly documented formal consistency findings. Formal A2A payment lifecycle is not untouched territory.
13. [AI Agent Economics](https://arxiv.org/abs/2608.03076) (Aug). Emergent transfers and institutions without prescribed economic roles on productive-task worlds; emergent market formation is directly studied.
14. [Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff](https://arxiv.org/abs/2610.12436) (Oct 8). Population threshold ecology theory already developed, focused on autonomous cyber capability; we must not claim first Allee-effect/population tipping point.
15. [Population Physics, Population Problems](https://arxiv.org/abs/2609.33871) (Sept). Population self-organization/phase-transition-like signatures across scenarios. Generic phase-transition observation is not new.
16. [SCARCE](https://arxiv.org/abs/2610.21029) (Oct). Persistent agent institutions and coalitions in long-horizon coding work.
17. [When Do Institutions Beat Intelligence?](https://arxiv.org/abs/2608.11357) (Aug). Controlled artificial ecologies isolate where institutional structure helps vs better reasoners. A paper simply comparing institution and model capability is preempted.
18. [The Inbox as a Coordination Primitive](https://arxiv.org/abs/2610.36264) (Oct 26). Receiver-governed attention, message retention, sender deposits/pricing and reply rules already studied at large simulated scales.
19. [LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades](https://arxiv.org/abs/2610.30769) (Oct 22). Social influence can create nonlinear recommendations among LLM agents: information herding not first demonstrated.

### Benchmark/verifier counterweights

20. [Rethinking Verification in Agent Harnesses](https://arxiv.org/abs/2610.34577) (Oct 25). Compares 17 independent-review and lifecycle verification configurations on coding/visual tasks; "add critic to verify" not new.
21. [A Trust Layer for Agent Evaluation](https://arxiv.org/abs/2610.07274) (Oct). Separates earned performance, claimed performance and repeatability; avoid claiming a novel general evaluator.
22. [InfraBench](https://arxiv.org/abs/2608.11234) (Jul/Aug). Agent infrastructure tasks exhibit broken distributed invariants, unsafe side effects and incomplete cleanup.
23. [InfraDev](https://arxiv.org/abs/2610.36589) (Oct 27). Hidden probes for real large infrastructure changes. Generic protected tests and agent-produced infra artifacts are increasingly strong prior art.

## Three most useful research hypotheses to *investigate*, not to publish yet

**H-A1: Persistent external-world interference, without adversarial intent.**
A task-successful agent writes legitimate information/artifacts to a shared external service. An unrelated later agent, with different instructions and principal, reads this state and changes its own action. Can we causally measure the *marginal downstream outcome* of the first agent's write under controlled interventions, and predict or prevent harmful interference **without destroying useful knowledge sharing**? This is cross-agent, cross-principal, and *externally shared world state*, not simply poisoning the memory of the same model.

- **Strong non-LLM baselines:** perfect namespace isolation, scoped ACL/least authority, snapshot-and-restore state, time/owner version tagging, read/write quarantine, standard conflict-free replicated data types, transactional isolation, source attribution/provenance, no-sharing oracle. New algorithm must improve on at least one task-utility/externality frontier rather than beat a weak prompt.
- **Controls:** shared-data transfer that is genuinely beneficial; harmless agent writes; changed task that legitimately should read new info; independent contemporaneous user writes; no-write counterfactual; equal budget and correct-oracle checks. Blind experiment condition labels.
- **Immediate kill:** safety solved by ordinary permission/snapshot rules at same utility; behavior just prompt injection (SkillRelayGuard); only fixture-hand-authored agents; no effect from real model-driven actors.

**H-A2: Multi-principal externality measurements and repair.**
Several agent-owned tasks succeed individually, while imposing measurable cost on third parties. Can a causal metric of *responsibility for joint changes in feasible actions* illuminate failure missed by each principal's task score, and does a distinct agent policy improve overall outcomes? Crucial control: standard weighted-sum utilitarian welfare optimization, veto/ACL and transaction scheduling. Without new causal insight or strong optimization advantage, this is economics/SE application, not novel method.

**H-A3: Adaptive cross-principal evidence checking.**
Autonomous buyer/seller/scheduler agents hold separate private observations. They must decide whether to verify a counterpart's claims at tool cost; no centrally trusted shared log. Compare explicit source checks, independent cross-provider probes, signed attestations, Bayesian decision-theoretic value of information and mandatory verification. A generic "always fact check" is preempted by A²-Failures and classical decision theory. Need a distinct bounded-budget decision mechanism on genuine heterogeneous LLM agent actions.

## One minimal *decisive* study for H-A1 (not yet run)

A small multi-session closed system (e.g. internally hosted knowledge/task board + a local API service) with two or three genuinely *independent agent principals*, plus invisible ground-truth task oracles. First agent receives a legitimate edit/research task and may create an external artifact; second agent later receives another legitimate task and can encounter the shared artifact; third-party service state is measured independently.

Matched conditions across task families:
- isolated state / separate namespaces;
- shared state without control;
- shared state with conventional ACL/transaction/snapshot and owner-scoped visibility;
- shared state with a strong tool-using review policy;
- only if residual remains, experimental new candidate method.

For each actual LLM run record: action trace, successful reads and writes, independently graded final outcomes for *both* agents, third-party effects, the downstream task's exposure counterfactual, observed causal estimate of sharing, tokens/tool calls/latency. Run randomized order and seeds; hold out independent tool tasks and environments. No public external websites or unsafe writes.

**GO for a future method ONLY IF:** external-world interference is substantial in real agent runs; ordinary isolation is overly restrictive to beneficial use; provenance, standard ACLs and strong artifact-aware LM reviews cannot achieve comparable safe sharing; and the effect generalizes across tools. A small demo is not a publishable result.

## Most serious limitations of this search

1. These domains are not paper-sparse in 2026. Some "early" subfields have dozens of strong near-neighbors already. Relative ranking is researcher judgment from a focused sample, not an arXiv paper-count analysis.
2. The strongest causal observational source (public wiki) **lacks successful-read and independent final-outcome evidence**, therefore it does not prove causal benefit or harm. This missing observability motivates controlled experiments but does not automatically imply a new theoretical discovery.
3. Classical database isolation, access control, mechanism design, causal inference and social contagion may make the proposed methods redundant.
4. No actual new multi-agent experiment or novel algorithm was built or tested in this scan.
5. For publication, choose a problem important to *agentic behavior*, not just a distributed database tool; genuine model-driven tool actions, heterogeneous principals and transfer must matter.
6. Keep the hypothesis alongside the strongest competing work; when contradicted, kill or pivot without a sunk-cost argument.

## Research decision

**Recommend narrowing two fields for method-oriented follow-up:**
- **Primary:** causal ecology of autonomous agents sharing *external worlds* across sessions, principals and ownership boundaries.
- **Secondary:** cross-principal verification and externality accounting, with A²-Failures as available agent-run data.

**Do not call this a discovered novel paper yet.** The value of this report is a better controlled field-selection gate and direct, recent novelty blockers.
