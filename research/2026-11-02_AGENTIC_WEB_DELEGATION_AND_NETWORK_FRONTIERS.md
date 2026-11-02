# Frontier scan VI: the Agentic Web, delegated communication, and agent-generated network load

**As-of date:** 2026-11-02. **Objective:** Discover additional *early-forming agent-native research fields* distinct from our prior scans on classic memory/planning, agent ecologies, scientific instruments, tool interface evolution, agent control, and agent-systems serving. This is a **field-selection** report, not an original-method proposal or results paper. "Less crowded" is only a qualitative, scoped reading, NOT a bibliometric finding.

## Core discovery and decision

**Primary exploratory field: Decentralized Agentic Web.** A user-side agent must cooperate with independently owned content/service agents. AgentWebBench (ICML 2026) provides an actual executable environment with 100 website-specific providers and 18.4M documents. Its user-agent / content-agent split defines a distinctive unit of study: *noncentralized access across providers with heterogeneous information and resource incentives*. Strong direct paper already exists, so claims of being first are explicitly ruled out. This is the best *new* candidate from today's search on feasibility and field specificity.

**Other new field-level opportunities:**
- Recipient-side acceptance and asymmetric consent to agent-mediated communication (requires ethical human research to claim actual adoption effects).
- Agent-induced network/compute traffic dynamics (measured SIGCOMM 2026, attractive rigorous engineering but systems venue and GPU costs).
- Adaptive information supply under agent-generated demand and iterative content optimization (CHASE, EcoGEO directly study it; very high competition on trivial methods).
- Consent/compensation for agent-mediated web access (agent-first web and terms.txt directly propose mechanisms; permission protocol is not fresh).

## Rank table (ordinal, qualitative not acceptance odds)

| Rank | Subfield | Emergent agent-native construct | Strength of direct prior art | Real experiment feasibility | Verdict |
| --- | --- | --- | --- | --- | --- |
| 1 | **Decentralized agentic-web cooperation between user and provider agents** | Independent website agents control what information is served; user agents must decide who to query, when, and how to combine partial evidence | **High:** AgentWebBench, established federated search, strategic information disclosure | **High-to-medium:** open code/data/API; external service, ClueWeb license and model costs | **Conditional GO for deeper field audit, NO new-method claim** |
| 2 | **Two-sided receptivity to delegated agent communication** | Autonomous send-side delegation is not the same as recipient willingness to interact | **Medium-to-high:** survey measurement paper, human-AI communication, platform recommender systems | **Low-medium** for real-world human outcomes; synthetic pilots cannot validate human preferences | **Conditional exploratory GO with HCI collaborators only** |
| 3 | **Agent-induced workload/network traffic dynamics** | A user task triggers endogenous calls via branch, retry, spawn and peer coordination, creating coupled queueing load | **High:** agentraffic, MAServeBench/TAO/TOPAS; classic networking | **Medium if GPU accessible**, low if not | **Conditional for systems, NOT generic traffic scheduler** |
| 4 | **Endogenous quality and diversity of agent-facing information ecosystems** | Providers repeatedly adapt content for agent ranking; feedback can erode quality/diversity while changing what agents choose | **High:** CHASE, EcoGEO, classic information retrieval, search economics | **Medium** with closed sandbox, harder with real web causal claims | **NO-GO on generic content optimization, conditional as field** |
| 5 | **Agent-access reciprocity, identity and compensation** | Websites may negotiate machine-readable access, permission, rate limits, terms, and delegated use | **High:** agent-first web, terms.txt and established access-control/legal frameworks | **Medium** for protocol benchmarks, high for ecosystem economics | **NO-GO generic new web-access file/protocol** |

## Grounding in primary research — closest competitors

### 1. Agentic Web (top candidate)

[AgentWebBench: Benchmarking Multi-Agent Coordination in Agentic Web](https://arxiv.org/abs/2604.10938) (April 13 2026; **ICML 2026** accepted according to public README) defines 100 website-specific content agents over 18.4 million documents and four evaluation tasks: web search, recommendation, question answering and deep research. Authors report decentralized coordination typically lags centralized access in retrieval, though its QA performance can be competitive as models scale; access to particular providers becomes concentrated. It is **already a genuine agent-specific benchmark**, not our discovery.

Public implementation independently inspected via GitHub:
- [cxcscmu/AgentWebBench](https://github.com/cxcscmu/AgentWebBench) verified live, main at **30a996e5eea5196e8881cd62272951da802b1462** (June 19 2026).
- README specifies 354 search, 281 recommendation, 53 QA and 331 deep-research test instances; per-task `test_1.json` smoke sets.
- Four preexisting strategies: centralized classical, embedding-selected website tools, prompt-selected website tools, and distributed content-agent coordination. A new method must beat strong centralized and distributed baselines at matched resources, and explain when decentralized participation helps/hurts.
- Dataset is derived from **ClueWeb22**; using the public Search API may require service availability, provider keys and compliance with ClueWeb22 terms. Public source code alone does not guarantee offline, cost-free reproducibility.

Parent disciplines: federated search/IR, strategic disclosure, privacy, mechanism design, query planning, federated services and economic intermediation. **Mere decentralization, planning and source trust are not novel.**

The most substantive possible field-level phenomenon: **co-evolution of the user agent's information-seeking policy and provider agents' independently constrained information policies**, with measurable impacts on successful final tasks, provider burden and access diversity. This has not been shown to be a literature gap. Existing parent methods may solve it.

### 2. Two-sided delegated communication

[Delegation Asymmetry in Agentic Recommender Systems](https://arxiv.org/abs/2608.18058) (August 18 2026, forthcoming WSDM 2027 according to author PDF) surveys active dating-platform users and distinguishes willingness to **delegate sending** vs **receive** agent-mediated communication. Paper reports roughly threefold mean deployment propensity vs engagement propensity and that only 4–13% of directed pairs in a modeled random-pairing counterfactual jointly satisfy the two conditions. These are **survey-derived/counterfactual estimates, NOT observed agent deployment success**.

Research field: two-sided design where the sender's autonomy interacts with the recipient's acceptance, privacy and fairness. Direct competition from reciprocal recommendation, classic matching, HCI and social delegation studies (e.g. [Social Media Clones](https://arxiv.org/abs/2509.07502) 2025). Specific decision to contact/when to disclose consent is NOT automatically new and may need real ethics-approved participants.

### 3. Agent-native network traffic/requests

[Towards Traffic Modelling of Multi-Agent Systems: The Role of Coordination Topology](https://arxiv.org/abs/2608.20494) (August 20 2026; ACM SIGCOMM NAIC 2026) measures 500 runs/topology for three different agent collaboration structures, finding topology-dependent non-Poisson burstiness and a log-normal reasoning-phase component. **The traffic phenomenon has already been quantified.**

Public code [dlamagna/agentraffic](https://github.com/dlamagna/agentraffic), main at **72896232df94399ef71ffad1ac87990174e2c36a** (Oct 13 2026), with Docker/AgentVerse/vLLM/instrumentation. The README explicitly requires NVIDIA GPU runtime for reproduction. A Docker mock or sampled arrival series does not reproduce real backend demand. Existing serving papers and classical queueing provide strong baselines. An original method would require measured **endogenous coordination control** (not just another queue priority rule), at fixed task correctness and actual device/network cost.

### 4. Evolving agent-facing information supply

[CHASE: How Content Ecosystems Are Reshaped When Ranking Is the Only Target](https://arxiv.org/abs/2608.30466) (Aug 31 2026; COLM 2026) simulates 20 rounds of optimizing content for a ranking signal and reports reduced quality-ranking alignment across six domains. Direct empirical incumbent for content homogenization and feedback ecology.

[EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents](https://arxiv.org/abs/2605.12887) (May 13 2026) already implements coordinated web evidence environment influence on agent browsing trajectories and recommendation outcomes. Therefore web-information **trajectory steering and document ecosystem optimization** are NOT blank-slate method ideas. Evaluating incentives/counterfactuals beyond these studies requires strong evidence and should not turn into optimizing deceptive content against real systems.

[Answering Without Referring](https://arxiv.org/abs/2607.07652) (July 2026) reports agentic/AI information intermediaries weaken outbound referral incentives. Its reported clickstream metrics are from one observational context and cannot be generalized without further data.

### 5. Autonomous web access and rights

[Towards an Agent-First Web](https://arxiv.org/abs/2606.19116) (June 2026) already proposes layered machine access, economics and agent-friendly content design, discussing recursive generated information and provenance.

[terms.txt: A Consent and Compensation Protocol for Agentic Web Access](https://arxiv.org/abs/2609.11152) (September 2026; primary original abstract found via alphaXiv, arXiv host intermittently blocked) describes provider-specified machine terms, delegated identities and signed authorization/receipts. Full original paper was **not reliably fetched from arXiv**, so exact guarantees remain unverified in this check.

Classical web permissions, signatures, HTTP 402, access-control lists, subscriptions and robots.txt are established. A small 'agent terms file' change is unlikely to justify a major algorithm paper.

## Falsification design: field #1 (DO NOT invent method yet)

**Unit:** independent test query / provider allocation / model seed. Source code and test conditions frozen before held-out evaluation. First reproduce at least one actually model-driven **AgentWebBench** sample using original public methods and API. Record exact original branch SHA, backend/model version, model calls and costs.

**Candidate factor to probe:** user-agent strategy in the presence of provider-specific constraints that vary independently (e.g. provider response budget, coverage, and transparent/no-disclosure policy), with a genuine resource or information allocation choice. The benchmark already covers static provider retrieval; do not rebrand ordinary federated search as a new problem.

**A/B controls:**
1. centralized global index when legitimate (best information-access upper bound; note privacy/ownership differences, not an always feasible deployment);
2. official embedding-tool/prompt-tool baselines;
3. original multi-agent content agents;
4. deterministic federated retrieval and classical budgeted allocation/coverage optimization;
5. matched-compute tool-using LM agent with direct task access;
6. only if strong failure remains, an original agent-protocol or allocation method.

**Outcomes:** independent task correctness, evidence support, coverage of diverse providers, provider query cost, total tokens/latency, and optional provider-side burden. Must predeclare the acceptable welfare/utility tradeoff and report false positives in benign cases. Distinguish provider fairness/economics from user task objective.

**Kill:** no accessible benchmark; obvious improvement comes only from more calls/tokens; effects vanish under deterministic federated search; performance gain arises solely from a toy misconfigured provider; task data leakage; no model-driven tool behavior; no improvement beyond baseline Pareto frontier.

## Falsification design: field #2

If recruiting human participants is feasible: test **send-side delegation × recipient opt-in** over ethically designed, realistic scenarios. Independent user judgments and behavioral measures, not LLM-simulated 'consent', must validate conclusions. Compare standard double-opt-in contact policy and transparent disclosure. Without participants, remain at the field-mapping stage.

## Important negatives

- **Not uncovered:** 'first multi-agent website retrieval', 'first generated-content feedback', 'first agent web-access protocol', 'first agent request-burst study', 'first two-sided acceptance effect'.
- A newly posted paper (even at a major venue) establishes *research activity*; it does not show that the adjacent subfield is underpopulated or that any new method exists.
- Agentic Web risks becoming federated information retrieval; network traffic risks networking/systems; two-sided receptivity risks HCI. To make an **agentic AI** paper, demonstrate a failure/advance involving autonomous adaptive action policies and model-driven decisions, not just generic service APIs.
- Human social outcomes need human data; synthetic "agents" cannot substitute for empirical human responses.
- All evaluations need strong classical baselines, independent task-level uncertainty and cost accounting.
- **No novel method or experiments were conducted** in this scan. Source verification was paper-level plus GitHub README/file inventories only; no external benchmark API was executed and no published result was replicated.

## Research decision

**Field-selection leader:** the **Decentralized Agentic Web** because there is an ICML 2026 paper, verified executable code and a distinctive multi-owner agent interaction setup. It is not a free novelty niche, and most naive ideas are already taken.

**Different disciplinary option:** two-sided agent-mediated communication, scientifically interesting and younger as an agent-specific platform topic but requires ethically appropriate human study.

**Systems option:** endogenous coordination-generated network load, with a ready measurement harness but GPU and classic network theory barriers.

**Do not lock a manuscript title.** Audit AgentWebBench and its closest provider-policy/federated-search competitors, reproduce a small real-agent baseline, then ask if there is any substantive agent-specific problem left before designing a method.
