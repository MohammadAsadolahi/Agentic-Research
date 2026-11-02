# Deep research III: agent–human–environment frontier subfields

**Date:** 2026-11-02. **Scientific status:** literature-first opportunity map, no method/agent results, no originality claim. **Goal:** emerging and important *agentic* subfields, avoiding mature generic LLM planning/memory and overworked agent-society topics from earlier scans. **Method:** targeted 2026 arXiv searches, primary abstracts and some HTML texts; check direct methods and earlier conceptual parent fields. This is **not** bibliometric paper counting, a systematic review, or an estimate of paper-acceptance probability. Source claims below are authors' reports, not independent replications.

## Main decision

Do **not** select "agent-environment co-evolution" or "multi-agent human attention routing" as if they are new inventions. Both now have surveys/algorithms. The strongest *field-level* opportunities (not yet paper topics) are:

**A. Persistent mixed human–agent collective action:** humans and their agents work in lasting shared spaces with independent ownership, changing commitments, social context, and authority; novel *phenomena* still to be demonstrated rather than generic A2A protocols. High conceptual novelty potential, hard credible evaluation.

**B. Human-attention and judgment governance over parallel autonomous work:** the human's attention is shared, variable and costly while agents keep executing; require task-correct external actions, diverse human preferences, and comparison with optimal/classical scheduling. Highest small-team feasibility. **JarvisBench and the 30 October PCP algorithm are strong direct competitors.**

**C. Agent-native affordance and tool ecosystem adaptation:** interfaces change alongside diverse agent capabilities and workloads, not just training a fixed controller. Interesting, but **Agent S4 and VOIX have direct method claims**, and a co-evolution survey already covers the overall idea.

**D. Simulator/environment fidelity for evolving tool agents:** source-grounded, executable worlds and generalization; high impact, but WebAnything, SynthAPI and environment evolution are strong direct competitors with much larger compute.

## Source-checked opportunity matrix (qualitative judgments, not citation counts)

| Field | Why emerging specifically for autonomous agents | Most relevant recent work | Main novelty threat | Decision for small team |
|---|---|---|---|---|
| **A. Mixed human-agent persistent social networks** | Humans and independently owned agents coexist and take action asynchronously in persistent shared spaces; collective tasks need more than single-user chat | [DotSpace](https://arxiv.org/abs/2610.40674) Oct 23, [Multi-User LLM Agents](https://arxiv.org/abs/2604.08567), [JarvisBench](https://arxiv.org/abs/2608.14870) | DotSpace already proposes paradigm; authorization/delegation, groupware and CSCW are established | **Conditional highest field novelty, high user-study/methodology burden** |
| **B. Human attention as a shared agent-system resource** | Several agents ask, report, wait, search, or act while one human is sporadically available; safety vs time/utility tradeoff | [When Should AI Agents Ask?](https://arxiv.org/abs/2610.41129) Oct 30, [JarvisBench](https://arxiv.org/abs/2608.14870) Aug, [Just A Rather Very Intelligent Spoken Agent](https://arxiv.org/abs/2607.16610) | PCP solves a stylized scheduling model with guarantees; JarvisBench benchmarks bidirectional attention | **Best inexpensive direct agent experiment, but not first method** |
| **C. Agent-native affordance / tool-interface evolution** | Agents can select or build interfaces, and service operators can publish machine-readable operations rather than human GUI interactions | [Evolving Agent Interfaces / Agent S4](https://arxiv.org/abs/2610.28601) Oct 20, [VOIX](https://arxiv.org/abs/2511.11287), [Agent-First Tool API](https://arxiv.org/abs/2605.10555), [Co-Evolution survey](https://arxiv.org/abs/2608.10299) | Direct powerful current algorithm plus earlier declarative interface contracts | **Researchable but high baseline bar** |
| **D. Agent-environment realism and adaptive benchmark worlds** | Agents alter state and future feedback; simulations must support executing verifiable workflows with controllable drift | [WebAnything](https://arxiv.org/abs/2610.37786) Oct 27, [SynthAPI scaling](https://arxiv.org/abs/2610.37648) Oct 27, [Environment Evolution for Terminal Agents](https://arxiv.org/abs/2609.04128), [Environment engineering survey](https://arxiv.org/abs/2606.12191) | Strong environment generation methods and large-scale empirical training work already exist | **High scientific value, high compute and engineering cost; avoid naive simulator contribution** |
| **E. Measured environmental footprint of agentic behavior** | Open-ended agent trajectories use variable LLM inference, tools, retries and external compute; their task-level external energy cost is not static | [Environmental Impact of Generative and Agentic AI](https://arxiv.org/abs/2609.32960), [SAGE](https://fis.tu-dresden.de/portal/en/publications/small-footprint-big-intelligence-sage%2861bb6eff-4d3f-413d-a75a-abee018030a4%29.html) | Classic green computing and existing cost/energy optimizers; proxy energy estimates inadequate | **Method potential if direct measured energy and utility tradeoff; weaker for core agentic AI** |
| **F. Agent-skill supply-chain ecological compatibility** | Skill/tool dependencies, natural-language instructions, executable packages and service capabilities evolve independently | [Skills Are Not Islands](https://arxiv.org/abs/2607.01136), [LEGIT](https://arxiv.org/abs/2609.21325), [After the Party](https://arxiv.org/abs/2609.17274) | Dependency graphs, credentialing and large-scale registry studies already performed | **NO-GO generic dependency scanner, possible only new behavior-specific ecological dynamic** |
| **G. Decentralized agent service markets** | Agents strategically advertise and sell execution services with private capabilities and resource costs | [IEMAS](https://arxiv.org/abs/2603.17302), [Agent Bazaar](https://arxiv.org/abs/2605.17698), [Market matching](https://arxiv.org/abs/2610.31002) | Mechanism design/market theory extremely mature; direct distributed inference routing results | **NO-GO as default** |
| **H. Human–AI co-improvement in autonomous research** | Research agent ideation, experimental direction and feedback are jointly developed with human investigators | [Aligning Autoresearch](https://arxiv.org/abs/2610.38882) Oct 28, [Meta-Agent Challenge](https://arxiv.org/abs/2606.04455), [DISCERN](https://arxiv.org/abs/2609.33357) | Human-simulator training, research benchmark creation and reward-hacking safeguards studied in fresh paper | **Promising scientifically but major resources and strong directly related paper** |
| **I. Longitudinal production-agent science** | Real agents are often short-lived and heavily supervised; field claims based on simulated autonomous populations need deployment-grounded validity | [Measuring Agents in Production](https://arxiv.org/abs/2512.04123), [AgentDebugX](https://arxiv.org/abs/2607.18754) | Need access to production traces, careful consent/privacy, distinguish behavior from instrumentation | **Potentially valuable empirical paper, unlikely fast novel algorithm** |

## Check against the user's specific requirement: "early emerging and room for a new method"

**A is early as an agent-native form of human/AI networked collective action, not early as sociology/CSCW/multi-user computing.** The very new [DotSpace](https://arxiv.org/abs/2610.40674) is mostly a network paradigm/proposition; it is not proof that each constituent problem is unsolved. Method innovation must derive from empirically observed irreducible coordination/authority/partial-participation challenges that standard groupware/ACL/workflow systems cannot already solve.

**B is experimentally inexpensive but now has an explicitly matching recent algorithm.** [When Should AI Agents Ask?](https://arxiv.org/abs/2610.41129) already introduces a pairwise coordination policy (PCP), proves cases of optimality/bounded gap, and reports 864 synthetic tests. Any "when to ask"/"human approval queue" method must implement PCP and compare fairly. [JarvisBench](https://arxiv.org/abs/2608.14870) already contains 45 long-horizon agentic instances. A possible emerging *subproblem*, not checked for uniqueness, is consent-critical decisions with heterogeneous interruption cost and causal downstream decision quality; standard restless bandits/queueing and human-AI interaction literature may preempt it.

**C and D have high-impact tool/agent experiment infrastructure, but a *higher* computational and implementation barrier.** [Agent S4](https://arxiv.org/abs/2610.28601) already evolves interfaces from unlabeled trajectories. [WebAnything](https://arxiv.org/abs/2610.37786) assembles 244 executable websites; [SynthAPI](https://arxiv.org/abs/2610.37648) analyzes 458,752 tasks across 849 models. A small custom web simulator and “agent tool selection improves” is insufficient.

**E is early in actual agentic carbon/energy measurement but risks being a generic systems-metering paper.** The Sept 2026 sustainability paper supplies *order-of-magnitude estimates* without original hardware measurements. A rigorously measured outcome could be valuable, but access to trustworthy power counters and strong scheduling baselines matters more than a new acronym.

## Two shortest falsification paths — before naming an algorithm

### Field A: persistent hybrid human/agent societies
- Simulate 2–4 independent human principals (as fixed preference/approval oracles, not claims about real people) and 2–6 truly model-driven agents; provide an offline persistent shared task space and several separately owned resource/action APIs.
- Vary owner presence, changing intentions and agent autonomy; measure externally graded joint outcome, authorized effects, unresolved commitments, unnecessary interruptions and per-principal utility.
- Compare ordinary multi-user groupware, scoped ACL and two-phase approval, fixed workflow delegation, and a strong LLM multi-agent coordinator.
- **Kill** the new-method hypothesis if classical groupware and fixed rules handle it equally well. No claim about actual human experience without user study.

### Field B: human-attention governance
- Use JarvisBench-compatible real agent tasks or a small set of other genuine tool tasks, with protected oracle scoring. Fix exact user availability/approval model.
- Compare PCP, Jarvis mediator, FIFO, risk-priority, queueing/deadline schedulers, and a simple single central LLM coordinator, under matched tokens, human interruption budget and agent task success.
- Inspect where a *new phenomenon* remains (not just imperfect timing): delayed authorization changing future task possibilities, nonstationary availability, conflicting principals, etc. These are **hypotheses**, not demonstrated novelty.
- **Kill** if PCP or fixed queue rules match at equal utility and cost.

## Important negative results from the literature scan

1. Agent-environment *co-evolution itself* is **not** a newly discovered field; [Co-Evolution in Agentic Systems](https://arxiv.org/abs/2608.10299) surveyed it in August.
2. "Agent autonomously improves its tool interface" is **not new**; Agent S4 proposes an implemented solution with substantial scores.
3. "Synthesize executable web environments" is **not new**; WebAnything and SynthAPI provide major recent research.
4. "Optimize when a parallel agent asks a human" is **not new**; PCP directly supplies a strong method.
5. "A continuously available intermediary between agent and human" is **not new**; JarvisBench does exactly this.
6. "Shared skill dependency analysis" and "agent marketplace credentialing" already have 2026 dedicated research.
7. "Human researchers improve autoresearch agents" is demonstrated in an October 28 paper.

## Evidence audit

- **Primary verified abstracts:** DotSpace (Oct 23), PCP (Oct 30), Agent S4 (Oct 20), WebAnything/SynthAPI (Oct 27), Aligning Autoresearch (Oct 28), Co-Evolution survey, agent environment survey, Skills Are Not Islands, etc.
- **Primary full HTML sampled:** Agent S4 and WebAnything (methods and contribution framing, not full numerical replication).
- **Secondary only:** one research-institution energy tool page; do not rely on specific unverified quantitative energy claims.
- **Not performed:** systematic arXiv category counts, full-text close reading of all 20+ papers, executable reproduction of cited methods, independent remeasurement, controlled new agent experiments.
- **Criticality:** many fresh works are preprints and need strong skeptical review; field-first ranking deliberately refuses to call any candidate a 'new algorithm opportunity proven'.

## Decision and next scientific action

**First inquiry:** mixed human–agent networked collective work, with a narrow and measurable *interaction failure* not handled by ordinary groupware or current agent protocols.

**Second inquiry:** attention/oversight across several autonomously running agents, but with PCP/Jarvis mandatory baselines; this is the lowest-cost real-agent falsification study.

**Third inquiry:** tool-interface coevolution beyond individual-agent gains, if we can run Agent S4 and its fixed-interface competitors; high compute risk.

**Next step:** primary-source code and benchmark audit for DotSpace, JarvisBench, PCP; find one concrete failure vs strong baselines, not invent a title. The current report makes **no claim of novel scientific method, benchmark or acceptance readiness**.
