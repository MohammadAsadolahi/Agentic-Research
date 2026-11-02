# Frontier scout V — agent capability economics, organizations, execution, and serving

**Research date:** November 2, 2026. **Aim:** search for additional agentic-AI-native subfields *not already treated as our primary candidates* (agent ecology, persistent human/agent networks, scientific instrument metrology, generic memory/planning). The user specifically wants a **difficult early-forming field with potential room for a publishable novel method**, not established continual-learning/planning or obscure easy bugs.

**Method/evidence tier:** targeted searches (multiple query families) on arXiv; inspected full HTML for BOTTLED, MAServeBench, TAO and parts of agent-native organization/smart-contract papers, plus related papers' abstracts and GitHub repository README/source inventories. This is **not** a systematic review, quantitative paper-count ranking, complete code reproduction, or proof of a research gap. Numerical claims below are *reported by the respective authors* and not independently rerun. All maturity/novelty judgments are subjective and conditioned on small-team feasibility.

## Executive decision

A qualitatively **different emerging agent-native research subject** appears especially actionable:

**A. Agent capability economics / workload-scale amortization:** An autonomous tool-using agent must choose whether and how to *invest* finite inference/compute into creating a reusable specialized solver, versus doing the workload directly. What matters is **quality at total deployment cost**, not one-shot accuracy or generic reusable skill learning. This is already named and benchmarked as "bottling"; **the problem itself is not our novelty**. The *method* window is conditional and could be rapidly closing. Public executable code available.

**B. Agent-native organizational design and governance** appears younger at the level of **executable, independently evaluated changing organizations**, but existing formal organizational design, workflow and MAS literature create a huge classic baseline burden, and the prominent August work is an architecture/prototype with limited empirical evaluation.

**C. Multi-agent serving semantics** has strong public benchmarks and published optimization methods but is **already method-crowded by late October** (TAO, Helium, TOPAS, PackServe, HexAGenT, etc.). Great for hardware/systems expertise, not a shortcut to NeurIPS method novelty.

**D. Agentic transactions / semantic runtime consistency** and **E. compositional skill ecosystems** are direct 2026 method territory with unusually strong rivals. NO-GO as our default.

**F. Real-world agent marketplace registry trust** has original observational data but reputation verification and anti-Sybil economics are classical and multiple modern papers already address it. NO-GO for a generic "build reputation" method.

## Ranked field table — cautious relative assessment

| Rank | Agent-native subfield | Primary research unit | Newest strong competitor | Falsifiable experimental object | What kills a method |
| --- | --- | --- | --- | --- | --- |
| 1 | **Capability bottling & workload investment** | Agent allocates a fixed budget across inspection, labeling, compiling, testing, training and serving a whole batch | [BOTTLED, Oct 6](https://arxiv.org/abs/2610.08775), [ABCAgent, Oct 4](https://arxiv.org/abs/2610.04824), [SpeedRunner, Aug](https://arxiv.org/abs/2608.11338) | Real agents deciding *how much* to invest in reusable solver vs direct work; end-to-end accuracy/cost and deployment break-even | fixed decision rule, distillation or ASI/ABCAgent matches under same tokens/compute, no novel agent decision mechanism |
| 2 | **Agent-native organizational reconfiguration** | Persistent commitments plus temporary worker groups, separately controlled authority and lifecycle under dynamic work | [Fluid Structure, Rigid Record, Aug 9](https://arxiv.org/abs/2608.08516), [Manager Agent, 2025](https://arxiv.org/abs/2510.02557), [Contract-Centered Architecture, Aug](https://arxiv.org/abs/2608.27086) | Real human/agent or simulated multi-principal organization adapts to tasks without losing authorized commitments, at budget | classical workflow engine + ACL/role-based permission and standard manager agent solve just as well |
| 3 | **Agentic serving as a first-class workload** | GPU/CPU serving a stateful graph of tool waits and dependent model calls | [MAServeBench, Oct 29](https://arxiv.org/abs/2610.40293), [TAO, Oct 27](https://arxiv.org/abs/2610.37230), [TOPAS, Aug](https://arxiv.org/abs/2608.25523) | Legitimate task success, tail completion time, GPU utilization, KV state, tool readiness | classical or existing serving scheduler equals method; results only from simulated replay not actual GPU/model system |
| 4 | **Semantic agent transactions** | Dynamically generated actions are proposed, accepted, logged and compensated across tools | [Agentic Transaction, Aug](https://arxiv.org/abs/2608.13900), [Mnemosyne/ATP, June](https://arxiv.org/abs/2607.00269) | Multi-step goal success, violated execution guarantees, latency/cost under real agents | ordinary transactions/sagas, and these 2026 agent methods already match |
| 5 | **Compositional capability supply chains** | Individually allowed skill packages can create forbidden composite outcomes | [CoSA, Oct](https://arxiv.org/abs/2610.35082), [SkillCorpus, July](https://arxiv.org/abs/2607.15557), [SkillsVote, May](https://arxiv.org/abs/2605.18401) | Real agents combining skills, permission leakage, task utility, transfer | existing cross-skill guard and information flow baseline already solve |
| 6 | **Economic trust in actual deployed agent registries** | Claimed provider capability vs real functional endpoint, attestations and strategic identity | [ERC-8004 empirical study, June](https://arxiv.org/abs/2606.26028), [interagent trust comparison 2025](https://arxiv.org/abs/2511.03434) | Independent valid services, provider success and verified reputation versus onchain claims | existing identity verification and proven anti-Sybil incentives match |

## Evidence and direct novelty threats

### A. Amortized autonomous capability production

- [Agent in a Bottle](https://arxiv.org/abs/2610.08775), October 6. Across **10 evaluated models and 3 batch tasks**, **48/60** bottling runs scored below the lower confidence bound of per-item zero-shot performance, and **31/60** failed to beat the strongest fixed-budget small-model distillation baseline. These counts are *not* a prevalence estimate for all agent deployments. It reports that large cost savings can be achieved with quality loss on one task. The paper provides an explicit resource-bounded agent sandbox and a *strong* distillation comparator. The authors already claim ownership of the **bottling problem**, so we must never say "first agent to turn knowledge into a cheap program".
- Verified public MIT source: [aktsonthalia/bottled](https://github.com/aktsonthalia/bottled), root contains `agent_eval.py`, `distill.py`, `zeroshot_eval.py`, `configs`, `src`; current `main` head checked **5a810d4be1e27333d04c51fa5870d4fcc8ce7120** (October 7). README: **OpenRouter API** currently required; original runs assume **A100 GPU, 8 CPUs, 64GB RAM** and agents running for up to 10 hours. Simple unit tests are not equivalent to actual BOTTLED replication; budget cost could be high.
- Direct prior methods on reusable executable skills:
  - [Inducing Programmatic Skills for Agentic Tasks / ASI](https://arxiv.org/abs/2504.06821) (2025) already introduces online induced and verified programmatic skills.
  - [Better, Faster, Stronger / SpeedRunner](https://arxiv.org/abs/2608.11338) (August 2026) already learns cost-reducing programs and tests distribution shift.
  - [ABCAgent](https://arxiv.org/abs/2610.04824) (October 4) represents agent behavior as editable programmatic specifications, evaluates latency and cost.
  - [Skill Learn Bench / continuous skills](https://arxiv.org/abs/2604.20087) and [SkillsVote](https://arxiv.org/abs/2605.18401) already establish agent skill learning/evolution.
  - [TrackRL](https://arxiv.org/abs/2610.25126) already provides randomized evidence of individual skill marginal contribution in RL. Its claimed public GitHub repository `xizhu1022/TrackRL` returned GitHub 404 on this audit; do not assume accessible code.

**Conditional open scientific questions, unverified**:
1. Can an agent predict *when* creating a reusable artifact will be worthwhile (and recognize workload classes for which it won't) **under hidden labels and a non-stationary workload**?
2. How should it allocate a finite budget among data inspection, teacher labels, program induction, validation and direct per-item fallback?
3. Can a distinct policy achieve a better *quality vs amortized total cost* frontier than fixed-budget distillation, ASI, ABCAgent, SpeedRunner, and classical bandit/optimal-stopping rules on independent held-out task classes?

**Critical self-critique:** This is closely related to the mature fields of active learning, AutoML, compiler design, metareasoning and online decision theory. An improvement from adding a decision threshold or program cache is not automatically new or agent-specific. We should favor a *real method* only if it exhibits a measurable capability not covered by these, with live agent decisions.

**Lowest-risk first activity:** run the public BOTTLED harness's no-agent data and budget integrity tests, then a small real-model baseline. Preserve original task and cost semantics; a cheaper custom workload is useful for feasibility but not evidence of improvement over the paper. Precommit a stop gate when distillation/program specialists equal any candidate at equal cost.

### B. Agent-native organizations

- [Fluid Structure, Rigid Record](https://arxiv.org/abs/2608.08516) (August 9): proposes enduring governance/record layer with dynamically formed temporary agent teams; paper itself says large empirical validation is incomplete.
- [Orchestrating Human-AI Teams: Manager Agent](https://arxiv.org/abs/2510.02557) (October 2025) already defines workflow management as a partially observable stochastic game and has open MA-Gym environment.
- [Contract-Centered Architecture](https://arxiv.org/abs/2608.27086) (August) proposes separation of skill/harness/scaffold/data and a falsifiable measurement procedure; no completed empirical results claimed in original August abstract.
- [Agentic Transaction / ACID agent framework](https://arxiv.org/abs/2608.13900) is an immediate technical competitor for semantic durability.

**Why still explore as a field:** The gap between a *roleplay multi-agent chat* and organizations with legally/operationally scoped commitments, changing task groups, and externally checked effects has rich scientific questions. But this is directly adjacent to decades of organizational theory and multi-agent systems. Distinct experimental outcomes must matter beyond source-code elegance.

### C. Agentic serving semantics

- [MAServeBench](https://arxiv.org/abs/2610.40293), October 29: traces genuinely hierarchical agent collaboration as a serving workload; authors explicitly distinguish native model execution from fixed trace replay and synthetic token demos.
- GitHub verified public [ShengxuanQiu/MAServeBench](https://github.com/ShengxuanQiu/MAServeBench), head **22483ab5df5eff562061953d564aac47a9423c2f** (October 29). README documents CPU-only synthetic quick start and full vLLM GPU serving. **CPU-only successful tests do not constitute hardware benchmark reproduction.**
- [TAO](https://arxiv.org/abs/2610.37230), October 27: actual tool-ready joint GPU session placement/scheduling; reports up to 26.8% reduced latency in 12 settings.
- [Helium](https://arxiv.org/abs/2603.16104), [TOPAS](https://arxiv.org/abs/2608.25523), [PackServe](https://arxiv.org/abs/2609.33224), [HexAGenT](https://arxiv.org/abs/2605.16637) and [Tail-aware Release](https://arxiv.org/abs/2609.10964) provide additional scheduling and cache competitors.

**No-go:** New "DAG-aware caching", "tool-aware serving", "GPU queue prioritization" is already active method territory, not an uncontested discovery. Better to investigate only if hardware access and a very specific mechanism beyond these can be validated.

### D. Semantic agent transactions

- [Agentic Transaction](https://arxiv.org/abs/2608.13900) already formalizes Semantic Atomicity/Consistency/Isolation/Durability and reports performance improvements.
- [Mnemosyne: Agentic Transaction Processing](https://arxiv.org/abs/2607.00269) develops deterministic admission, bounded repairs, log, compensation, formal properties and multi-model pilots. Sagas, CRDTs, transactional outboxes and idempotency are mature foundations.
- [Agent-Diff](https://arxiv.org/abs/2602.11224) uses task state diffs over enterprise APIs and publicly exposes harness [agent-diff-bench/agent-diff](https://github.com/agent-diff-bench/agent-diff). Thus even independent external state correctness is a baseline.

**No-go:** generic transaction wrappers or replay logs have direct methods and mature CS analogues.

### E. Compositional skill safety

- [CoSA](https://arxiv.org/abs/2610.35082) shows otherwise permissible skills can interact to form unauthorized information/action flows, with 288 task benchmark and a guard in the reported evaluation. This directly kills a broad "first cross-skill policy guard" claim.
- [SkillCorpus](https://arxiv.org/abs/2607.15557), [SkillsVote](https://arxiv.org/abs/2605.18401) and [TrackRL](https://arxiv.org/abs/2610.25126) already treat quality, selection, skill contribution and lifecycle.
- Research could still explore environment/authority-dependent composition at *large* scale, but classical information-flow analysis and direct CoSA guard are strong baselines. No current specific method recommendation.

### F. Authenticity of online agent marketplaces

- [ERC-8004 Decentralized Ecosystem Empirical Study](https://arxiv.org/abs/2606.26028) already studies three on-chain registries and offchain validity, observing that many listings are placeholders and rating trails can be dominated by suspected Sybil clusters.
- [Inter-Agent Trust Models](https://arxiv.org/abs/2511.03434) compares claim/proof/stake/reputation/constraint options. These plus classical secure identity and incentive mechanisms make generic trust-score design likely incremental.

## Falsification-first mini-protocol for the strongest remaining field

For **A (workload investment)**, preselect a few task families (not just one benchmark), define the actual total cost (C = C_{agent-control}+C_{teacher-labels}+C_{specialist-build}+C_{validation}+C_{serving}+C_{fallback}). Preserve original task outcome metric and forbid using hidden test labels in artifact design.

**Conditions:** (1) baseline zero-shot per instance; (2) fixed-budget distillation; (3) existing program-skill method, e.g. ASI/SpeedRunner; (4) BOTTLED agent unmodified; (5) simple hand-authored budget rule or contextual bandit/optimal stopping; (6) *only if residual exists*, a new agent decision method.

**Dependent outcomes:** correctness/F1 with confidence intervals, true end-to-end cost, per-workload break-even point, robustness to workload mix changes and held-out domains, proportion of budget spent before committing to a specialist, and number of real model-directed tool actions. Report both absolute quality and quality-cost Pareto frontier.

**Reject method thesis if:** fixed distillation/bandit is as good at matched quality/cost, artifacts get hidden-label leakage, results rely on one artificial domain, agent isn't truly making method choices, or claimed gains disappear once GPU and model API calls are fully charged. New `algorithm` cannot be decided just by the field map.

## Hard general conclusions

- "Super hard and easy to publish" are generally conflicting objectives. We can improve odds by choosing **newly measurable, important agent phenomena with runnable code and adequate strong baselines**, not by minimizing the number of paper titles.
- The 2026 arXiv search **repeatedly uncovered direct precedents**, even for areas that sounded new; do not coin a name and treat it as novelty.
- The most actionable newly scouted field **capability economics** already has BOTTLED, ABCAgent and programmatic skill competitors. At best **conditional**, not a no-competition field.
- The agent serving field has excellent open-source tools but **many competing schedulers** and needs GPU validation.
- The organizational field may be younger in its specific multi-agent implementation but not as a scientific discipline and requires substantial methodology to avoid conventional workflow claims.

**Actual research status:** 0 new LLM experiments, 0 novel method established, 0 model baselines reproduced in this track. This is a literature-and-repository feasibility audit, not an empirical paper.
