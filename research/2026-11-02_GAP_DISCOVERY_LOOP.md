# Adversarial research-gap discovery loop — 2026-11-02

**Research state:** A *specific evaluation gap* has survived a scoped adversarial literature audit, but neither novelty of an algorithm nor publication acceptance is established. We have NOT executed or benchmarked a method.

## 0. Keep the original user need visible

We seek a conversational AI *architect* for agentic systems: it discovers intended requirements; chooses and explains architecture, prompts, tool contracts, state, and workflow; and revises those artifacts over time without blindly encoding the latest single incident into brittle permanent rules. It is NOT just a LangGraph-like framework, prompt optimizer, or coding agent.

### Proposed research question — deliberately narrow

> When a developer reports an agent-system failure, can a design assistant reliably decide whether to **clarify stakeholder intent**, **probe the technical environment**, **make a persistent design edit**, **keep the current design**, or **escalate**, under bounded information and evaluation budgets, so that changes fix real problems with fewer unintended regressions?

Working name: **design-change identifiability and evidence-seeking evolution**. The term is only a research shorthand. DO NOT claim the general principle of identifiability, active probing, clarification, EVPI, abstention, or continual evolution is new.

## 1. Adversarial elimination: what NOT to pitch as new

| Rejected as generic novelty | Closest work / why it overlaps |
| --- | --- |
| Learn to choose which versioned prompt/tool/routing asset to repair; allow no-change/unresolved | [DAAF (2026)](https://arxiv.org/abs/2609.32498): learns registered replacement effects from replays; returns repair target, no-change, or unresolved |
| Active fault probing before changing an agent | [DoVer (ICLR 2026)](https://arxiv.org/abs/2512.06749): targeted interventions; validated/refuted debugging hypotheses |
| Co-evolve probing and harness revision | [KPHarness (Oct 2026)](https://arxiv.org/abs/2610.27417): knowledge–probing co-evolution and held-out Minecraft task evaluation |
| Ask user clarification under uncertainty using value of information | [SAGE-Agent (Findings ACL 2026)](https://aclanthology.org/2026.findings-acl.2028/): structured specification vs model uncertainty, EVPI, tool-parameter disambiguation; [Ask or Assume? (EMNLP 2026)](https://aclanthology.org/2026.findings-emnlp.15/) for coding agents; [CIGAsk (EMNLP 2026)](https://aclanthology.org/2026.findings-emnlp.314/) for RL clarification |
| Track shifting human intent through long conversations | [Drift-Bench++ (Sept 2026)](https://arxiv.org/abs/2609.38604): interactive intent shifts/miscommunication; [IntentFlux](https://arxiv.org/abs/2609.32520); [IntentDelta](https://arxiv.org/abs/2610.33806) |
| Evaluate differences due solely to requirements revision paths | [SpecPath (Aug 2026)](https://arxiv.org/abs/2608.09799): **same** final contract, **different** histories; existing specification-path invariance experiment |
| Compile spec into prompt with hidden tests | [Test-Driven AI Agent Definition (Mar 2026)](https://arxiv.org/abs/2603.08806) |
| Blueprint-based agent design & evolution | [Tressoir (CAIS 2026)](https://doi.org/10.1145/3786335.3813143) |
| Prompt vs middleware repair choice | [PRISM (Findings EMNLP 2026)](https://aclanthology.org/2026.findings-emnlp.1455/); [HarnessFix](https://arxiv.org/abs/2606.06324) |
| Learning how to optimize harnesses and preserve improvements | [MESH-Harness](https://arxiv.org/abs/2610.05300), [GRASP](https://aclanthology.org/2026.emnlp-main.452/), [RECAP](https://aclanthology.org/2026.emnlp-main.1684/), [GEPA](https://arxiv.org/abs/2507.19457) |
| "There are two gaps" between human wishes and execution evidence | [Reality Is the Final Verifier (Sept 2026)](https://arxiv.org/abs/2609.12039): requirements gap versus environment-model gap and allocation of human/computation resources |
| Counterfactual intervention data and act-vs-info-gather-vs-escalate selection | [SURE-Act (Oct 2026)](https://arxiv.org/abs/2610.24194): learns decisions for **runtime tool-using agents**, not persistent agent-system design |
| Measuring clarification/planning/code repair as stages | [SWE-RPG (Aug 2026)](https://arxiv.org/abs/2608.09072) diagnoses implicit requirements, plans and patches on repositories |
| Measuring overfitting, spec drift and regression | [Harness-Delta Attribution](https://arxiv.org/abs/2610.22466), [SLUMP/ProjectGuard](https://aclanthology.org/2026.findings-emnlp.76/), [SpecPath](https://arxiv.org/abs/2608.09799) |

**Most damaging near-neighbors to our candidate:** KPHarness (evidence-seeking harness evolution), SAGE-Agent (structured uncertainty/EVPI for intent), DoVer (experimental intervention diagnosis), Drift-Bench++ (interactive evolving intent), Tressoir (whole design). A reviewer can reasonably propose combining them. Our gap must survive that *composed baseline*, not only individual papers.

## 2. The possibly missing evaluation unit

We have NOT identified a verified peer-reviewed study evaluating **both** of these uncertainties in a **persistent agent-design revision** with real prompt/tool/architecture artifacts:

- **Intent uncertainty:** what should the agent accomplish, and has the stakeholder legitimately superseded an old contract?
- **Technical uncertainty:** why did a reported run fail; was it prompt selection, tool coverage/schema, routing, environment, or no actual bug?

The architect must decide *which kind of evidence to acquire*, or to abstain, **before** modifying a long-lived artifact. This is narrower than generic intent tracking, runtime debugging, or active harness evolution. It remains a candidate gap in the searched evaluation settings, NOT verified absence of all prior art.

### Paired-world counterexamples

Construct worlds $W_A,W_B$ with exactly the same observed prompt/history/trace $h$ but different latent intended contracts and/or environment faults, so the justified permanent change differs. Without informative action, any deterministic immediate-edit policy maps $h$ to the same edit in both worlds. This elementary indistinguishability observation is NOT a novel theorem; it motivates a benchmark with measured costs of extra evidence.

Example: a research agent misses a paper. In one world the developer expects a private approved corpus, in another the external specialized index has incomplete venue coverage, in another routing incorrectly chooses an otherwise adequate search tool. The same report is consistent with different interventions.

**Distinct from SpecPath:** SpecPath varies observed history while holding the final specification constant; our candidate fixes the *observed* history while varying the hidden stakeholder/world state. Both are valuable; neither construction's abstract logic is new.

## 3. First paper-worthy deliverable (if the study proves informative)

An **executable benchmark and empirical characterization** of *repair-identifiability* for agent-system designers:

- Use actual versioned stage prompts, tool schemas, routing/workflow code and test environments.
- Write independently approved intent/contract versions; include intentional supersession, false-premise complaints, real faults and no-change cases.
- Build *paired* ambiguous worlds with equivalent initial observable evidence and different optimal design actions.
- Allow two distinct read-only information actions: clarification with a stakeholder oracle and controlled non-destructive environment diagnostic; allow patch, retain, or escalate.
- Keep question and probe costs explicit; simulate stakeholder replies only from preapproved human-authored structured worlds; human-validate sample realism.
- After a patch, evaluate on targeted task, previously successful still-required behaviors, withheld inputs, side effects, cost/latency, and multiple sequential revisions.
- Split by entire **application families** and revision histories; use independent locked evaluation. Prevent self-generated tests from silently replacing approved contracts.
- Demonstrate real indistinguishability by checking that paired cases have exactly equal observations before information actions; otherwise the benchmark leaks its answer.
- Report first with simple existing methods; DO NOT precommit to a new learned policy.

**Illustrative metrics:** excess loss/regret versus oracle with hidden state; correct evidence-source choice; information efficiency; false irreversible edit rate; unnecessary questions; fix success; unintended regression per accepted revision; cross-family transfer; calibration.

## 4. Baselines necessary before claiming novelty

1. Strong direct coding/agent-design LLM with all available artifacts and fixed budget.
2. Design skill + approved persistent spec + ordinary regression tests.
3. DAAF-like registered-asset attribution/no-change decision, adapted fairly to available assets.
4. DoVer-style active technical intervention; KPHarness-style probe+repair (appropriately scoped).
5. SAGE-Agent-style clarification / information-value selection; Drift-Bench++-style interaction evaluation.
6. **Strong composed nonlearned baseline:** one LLM selects ask-vs-probe-vs-edit using ordinary prompting, *same* action set, budget, information, tests and artifacts. This is the real null hypothesis.
7. Oracle-intent and oracle-technical-cause diagnostic controls to localize bottlenecks.

Comparisons across papers with differing action spaces or original domains are not one-to-one; reproduce within the same benchmark where possible, report limitations of adaptation.

## 5. Algorithm hypothesis ONLY if empirical baselines leave a gap

A risk- and cost-aware evidence-selection policy over $(	ext{ask user},	ext{probe environment},	ext{edit},	ext{retain},	ext{escalate})$, estimating how each query changes the set of justified permanent edits and their *per-obligation* regression risk. The human question cannot reveal a technical fault; a sandbox tool probe cannot authorize a change to user intent. A decision rule should use both and prefer low-risk reversible information gathering when evidence is genuinely underdetermined. Start with a simple heuristic and independent tests; introduce a learned selector only if transfer gains exceed strong composed baseline.

**Novelty caveat:** this still resembles generalized value-of-information / active diagnosis; changing the application domain does not by itself create a new algorithm. A novel method needs a specific mechanism and convincing ablation.

## 6. Falsification and kill gates

- If a strong composed LLM+tests+spec baseline does equally well, **no algorithmic novelty**; an empirical/benchmark contribution may still be worth pursuing if benchmark validity is strong.
- If target worlds are artificial, implausible, or solvable from accidental formatting artifacts, **benchmark contribution is weak**.
- If a user question always suffices, the method is just ordinary clarification; if a tool probe always suffices, it is ordinary debugging.
- If a static "ask before every edit" policy does as well at comparable human cost, an adaptive learning policy adds no value.
- If the method always keeps the current design to avoid regressions, measure missed legitimate improvements and reject it.
- If gains disappear on held-out application families, or extra test-time computation explains gains, **no generalization claim**.
- If exact existing literature already implements and evaluates this full joint design-revision problem, **close or redirect this research claim immediately**.

## 7. Status and confidence

**High:** Broad AI architecture search, RL metapolicies, regression gates, static specifications, active probing, clarification, and harness co-evolution have direct prior art.

**Moderate (scoped):** The joint *persistent agent-design revision* benchmark with hidden intent AND hidden technical cause, and costed competing evidence actions, appears under-tested in the primary works reviewed. A missing comprehensive study is a legitimate research motivation, not proof of novelty.

**Low / unknown:** A new learned algorithm would outperform strong existing combinations; no code or result yet. Publication readiness, strong novel algorithm, and production generalization are NOT established.

## 8. Immediate execution plan

- Read full original methods and failure cases from DAAF, KPHarness, DoVer, SAGE-Agent, Drift-Bench++, Tressoir and SpecPath.
- Build 12-20 validated *paired worlds* in two realistic agent applications, with real stage prompts, tools, routing and deterministic simulator components.
- Run a direct LLM and a strong composed ask/probe/edit baseline; if no residual failure, **stop proposing a new algorithm**.
- Pre-register cost, correctness and generalization measures before expanding.
- Scale to distinct agent application families only if the pilot reproduces a real unexplained gap.
- Re-audit prior art before a paper claim; do not assert that a bounded search proves no other work exists.

*This document is a skeptical research hypothesis log, not a literature review establishing a first-of-its-kind result.*
