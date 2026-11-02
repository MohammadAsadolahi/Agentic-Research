# Course correction — search for emergent agent-native disciplines, not mature AI topics

**2026-11-02. Status: field-selection research only. No method proposed or experimentally demonstrated.**

## The user constraint (binding)

We want an original, important, **agentic AI** paper; avoid mature, hypercompetitive fields where contributions are crowded. Previous assistant priority "continual learning plus causal tool models" was not responsive: decades-old parent fields, with many direct recent agent papers, are difficult as entry points. **Withdraw that as the default recommendation.** Its detailed novelty audit remains useful as a NO-GO baseline, not the main research track.

## New organizing principle

Study **agent-native research fields created by deployment of many independent, tool-using agents that cross organizational boundaries, maintain state and change shared environments**. Do not treat a new name or young subcommunity as proof of novelty. Historical theories of multi-agent systems, economics, governance, distributed systems and HCI remain the strong intellectual baselines.

### 1. Agent ecosystem externalities and non-user consequences — leading exploratory field

**What it studies:** what a successful goal-directed agent does to shared state, other people, other agents and the global environment when those outcomes are outside its objective/reward; cascades through tool workflows and delayed effects.

**Evidence of emerging agent-specific empirical activity:**
- [ClashBench: Evaluating Resource Conflicts in Autonomous Agents](https://arxiv.org/abs/2609.19892) studies destructive preemption of incumbent tasks.
- [PAPC](https://arxiv.org/abs/2609.19226) models and mediates privacy propagation externalities in agent workflows; explicit **direct method competitor** for data-sharing harms.
- [Socially-Weighted Alignment](https://arxiv.org/abs/2602.14471) introduces a group-welfare weighting in congestion games, a **direct technical competitor** for utility-based externality mitigation.
- [Multi-Agent AI Safety as an Institutional Design Problem (POLIS)](https://arxiv.org/abs/2608.09828) offers runnable institutional intervention studies, a **direct competitor** for governance methods.

**Why the field may be interesting:** unlike standard single-task benchmarks, it naturally needs *jointly measured user success and non-user external effects*, and agents that choose and compose real tool actions. It is nascent as a **research community/agenda**, NOT a novel conceptual idea. A generic weighted objective or access policy is likely not novel. Choose settings with effects that cannot be trivially eliminated by ACL or standard scheduling.

**Big no-go threat:** this can simply become moralized conventional workflow side-effect prevention. A publishable method must exploit a distinctive agentic causal or planning structure and beat safeguards on utility, not just block all actions.

### 2. Open agent ecosystems and cross-boundary interoperability — early field, fast-moving protocols

**What it studies:** independently operated and heterogeneous agents discover one another, exchange work, and evolve capabilities across providers.

**Closest established work:**
- [AIDIP IETF discovery/invocation proposal](https://www.ietf.org/archive/id/draft-cui-ai-agent-discovery-invocation-02.html) and [InterSAGE](https://arxiv.org/abs/2608.13030) show agent discovery, identity, capabilities, verifiable delegation are actively being specified.
- [Capability Advertisement as a Market for Lemons](https://arxiv.org/abs/2606.03034), [AgentReputation](https://arxiv.org/abs/2605.00073), and [Skill-Conditional Reputation](https://arxiv.org/abs/2606.14200) already model unreliable, drifting skill claims, screening and conditional reputation. **No "first trustworthy agent selection/reputation" claims.**
- [Intelligent AI Delegation](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/intelligent-ai-delegation/Intelligent_AI_Delegation.pdf) provides influential framing.

**Research potential:** systems that fail in cross-organization settings despite each participant following local rules. **However:** protocols and agent-reputation papers have multiplied; for a small research team this may require deeper distributed-systems rigor and genuine heterogeneous agent measurements.

### 3. Experimental institutional science for persistent agent communities — early, but not unoccupied

**What it studies:** how collective outcomes change when the *rules*, rather than model prompts, change: governance, entry, exits, reputation, interaction structure, and conflict resolution under autonomous population dynamics.

**Strong existing works:** [SCARCE](https://arxiv.org/abs/2610.21029), [POLIS](https://arxiv.org/abs/2608.09828), [The Delegation Dilemma](https://arxiv.org/abs/2610.21746) and [Moltbook Observatory Archive](https://arxiv.org/abs/2605.13860). Thus there are empirical, formal and observational strands **already**. A simulator of agents talking is not original.

**Research potential:** controlled, independently replicable institutional interventions that reveal a *new* phenomenon plus an original mechanism, rather than unvalidated emergence narratives. **Difficulty:** separating prompt artifacts from genuine autonomous behavior; need controlled randomization, real model-driven agents and external welfare measures.

### 4. Agent ecological dynamics in real autonomous populations — especially early empirical methodology

**What it studies:** actual populations of long-running agents, their interactions, lifespan, niches, clustering, trust, operator influence and platform adaptation.

**Direct existing competitors:** [Moltbook Observatory Archive](https://arxiv.org/abs/2605.13860), [Moltbook Illusion](https://arxiv.org/abs/2602.07432), [Silicon-Based Societies](https://arxiv.org/abs/2602.02613). Field is recent, but already several analyses exist. Pure network descriptions have low prospects for a new algorithmic paper. Strong claims need data access, counterfactual interventions and robust operator-vs-autonomy attribution.

### 5. Long-lived agent delegation obligations and external action commitments — tentative/high overlap

**What it studies:** agent obligations that outlive a model run, are reassigned among independently operated agents, and interact with real events after original principal or environment changes.

**High-coverage obstacles:** [AgentBound](https://arxiv.org/abs/2606.30970), [HDP](https://arxiv.org/abs/2604.04522), [Mandato](https://arxiv.org/abs/2608.14074), [InterSAGE](https://arxiv.org/abs/2608.13030) and classic distributed transaction semantics. Novelty on generic permission delegation and audit is **already NO-GO**. Only look further if a truly different agent decision/behavior construct is found, not a provenance ledger.

## The correct selection before we discuss a paper title

**1st exploratory track:** agent-ecosystem externalities and third-party effects. It is close to observable real tool-use behavior and permits reproducible tests. However PAPC, SWA, ClashBench and POLIS are required direct baselines; no algorithm proposal yet.

**2nd exploratory track:** experimental institutional dynamics in long-lived autonomous agent communities. Potentially deeper, but harder to make causal, agent-specific and reproducible; SCARCE/POLIS direct rivals.

**Watchlist:** agent discovery/interoperability; quickly becoming protocol-saturated, with multiple reputation models.

**Don't select solely by small paper count.** Selection also requires important outcome, new mechanism opportunity, access to a reproducible environment, strong existing code baselines, actual LLM agents and a feasible independent oracle.

## Next 3 gates, no algorithm claims

1. Build a real *scoped field map* for two tracks: identify labs, seminal works, benchmarks, competing methods and missing infrastructure, and evaluate activity trajectory, not arbitrary paper counts.
2. Select a causal phenomenon measurable with real tool-using agents. Run baseline protocols *before* designing our mechanism. Show outcomes on legitimate task utility and third-party effects with hard benign controls.
3. Ask an external skeptical LLM to attack the distinctiveness and non-agentic substitutes. If a strong prior method already solves the same thing, pivot without attachment.

**Novel result status:** none. **Research direction status:** emerging field hypothesis; literature scan not exhaustive and not a publication guarantee.
