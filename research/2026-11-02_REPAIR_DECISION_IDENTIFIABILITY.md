# Repair-decision identifiability for continual agent-system design

**Date:** 2026-11-02  
**Status:** strongest *working research hypothesis* after adversarial literature search; not a verified first-of-kind concept, not an implemented optimizer, no baseline result.  
**Goal:** identify a publishable, defensible research unit for the user's original conversational architect: it designs roles/prompts/tool interfaces/workflows, and subsequently revises those durable assets without generalizing from one incident to a harmful global rule.

## Executive result: what survives

The strongest remaining candidate is **repair-decision identifiability under two kinds of uncertainty and lasting design consequences**.

> Given an agentic system, a failure complaint, and incomplete observations, can a system architect select the cheapest sufficiently authoritative evidence (ask the stakeholder, diagnose the runtime, run a cross-component contract test, or escalate) *because it discriminates among otherwise plausible permanent changes*, and then make only an authorized, evaluated change that preserves still-active obligations?

A phrase like "ask/probe/edit/no-change/escalate" is NOT new. The possibly publishable distinction is **action-conditioned evidence selection across competing permanent design changes**, where (a) human authority cannot be inferred from environment probes; (b) runtime correctness cannot be established by a user preference; (c) each change has a vector of downstream effects on current requirements; (d) prior and future edits alter the context. This integrates known ideas, so **the method must outperform a strong composed nonlearned baseline to claim algorithmic novelty**.

## Strongest new novelty threats found in this round

| Prior art | Concrete overlap | What its documented experiments do not by themselves establish for our question |
| --- | --- | --- |
| [CONTRA](https://arxiv.org/abs/2610.01769), Oct 2026 | Discovers behavior-changing requirement clarifications using alternative programs and shared-input execution; learns when to stop asking. [Partial Python code](https://github.com/fangz-cs/Contra). | Joint *authorization + technical diagnosis* for long-lived prompt/tool/workflow edits with preserved obligations. **Do not claim behavior-based contrastive clarification is new**. |
| [FixedBench / Coding Agents Don't Know When to Act](https://arxiv.org/abs/2605.07769), May 2026 | 200 human-verified already-fixed issues; reports 35–65% undesirable edits in evaluated model/harness conditions. Simple reproduce-first abstention can miss partially fixed issues. | Persistent system-design change under uncertain contract and cause; nevertheless no-change action bias is established. |
| [ImpasseBench / Knowing When to Stop](https://arxiv.org/abs/2610.31895), Oct 2026 | Escalation in coding agents after sufficient evidence of environment blockers; 19,371 trajectories across eight models; explicit escalation tool reduces reported budget exhaustion 34.0% to 6.7%. | Joint intent/cause evidence for *permanent system architecture revisions*; nevertheless escalation is old. |
| [DAAF](https://arxiv.org/abs/2609.32498), Sept 2026 | Learns effect of replacing registered prompt/routing/knowledge assets, selects repair target/no-change/unresolved. | Open-ended edit generation, latent mutable authority, and costed ask-versus-probe. Very close persistent-asset attribution. |
| [DoVer](https://arxiv.org/abs/2512.06749), ICLR 2026 | Verifies technical fault hypotheses by intervening in multi-agent traces. | Permission to change intended contract, or acceptance of long-lived design revisions. |
| [KPHarness](https://arxiv.org/abs/2610.27417), Oct 2026 | Co-evolves diagnostic probing and frozen-model harness recovery knowledge; held-out-task transfer in gaming tasks. | Explicit competing *human normative* interpretations and their authorization constraints; very close otherwise. |
| [SAGE-Agent](https://aclanthology.org/2026.findings-acl.2028/), 2026 | Specification/model uncertainty and expected-value-of-information clarification. | Longitudinal prompt/tool/topology repair consequences; however value of information itself is prior art. |
| [SpecPath](https://arxiv.org/abs/2608.09799), Aug 2026 | Same final contract reached by different requirement histories affects coding-agent output. | Fixed observed prefix with *different hidden* intent/technical cause, and priced evidence actions. Do not claim all path-dependence studies are missing. |
| [Minimal Repair Family Recovery / GCJR](https://arxiv.org/abs/2608.29228), Aug 2026 | Counterfactual joint repair-set recovery via dependency-graph replay; identifies minimal repair families. | Normative authorization + enduring design consequence. Do not claim set-valued counterfactual repair is new. |
| [Causal Agent Replay](https://arxiv.org/abs/2606.08275), Jun 2026 | Counterfactual attribution to agent execution steps, interacting effects. | Persistent architecture editing under changing intended requirements. |
| [CAMP](https://doi.org/10.1016/j.infsof.2026.108282), 2026 | Combines domain intended behavior context, requirement clarification and root-cause analysis for program repair. | Important integrative competitor: must recheck full methods and compare the actual unit before claiming novelty. |
| [THEMIS](https://aclanthology.org/2026.realm-1.0/) (find actual paper before citation) | Requirement-to-repair audit traces and relation graphs reported at REALM 2026 workshop (see ACL workshop index). | A trace/graph alone cannot be claimed new; verify URL and full paper before formal paper inclusion. |
| [Harness-Delta Attribution](https://arxiv.org/abs/2610.22466), Oct 2026 | Distinguishes overfitting/test-time compute from generalizable harness gains. | Essential evaluation controls; not a solution for evidence selection. |

**Reassessed novelty:** none of the separate mechanisms is new. This is *not yet a confirmed new algorithm*. The remaining testable contribution is whether **repair-disagreement-guided, authority-typed evidence selection** yields a measurable benefit under sequential agent-design edits, beyond simply combining prior techniques.

## Proposed distinctive computational mechanism: obligation-conditioned repair disagreement

Represent a hypothesis world `w = (s, f, env)` with:
- `s`: active, human-authorized requirements with supersession lineage;
- `f`: technical cause(s): prompt/tool contract, routing, state, provider boundary, or no bug;
- `env`: tool/runtime variation.

Given the incident and observed trace, maintain a plausible hypothesis set `H` or calibrated posterior `p(w|h)`. A language model proposes bounded candidate edits `E`: prompt, tool spec/implementation, routing, topology, or **retain/escalate**. For each edit, estimate a vector of *obligation-level* outcomes with sandbox replays and targeted regression probes; do NOT trust an LLM's imagined outcome as a measurement.

Define regret of edit `e` under world `w`:

```
regret(e,w) = loss(e,w) - min_{e' in authorized candidate edits} loss(e',w)

loss(e,w) = [hard unauthorized-action penalty,
             missed active requirement / unintended regression,
             unfixed reported issue, runtime+maintenance cost]
```

This is conceptually lexicographic: authorization cannot be traded away for a marginal task-success gain. For uncertain worlds, an edit has a **repair-disagreement footprint**: in which plausible worlds it is authorized and non-regressing relative to the best available candidate. If the same edit is acceptable under all supported worlds at the chosen risk tolerance, asking questions is unnecessary even if there is high entropy about root causes.

Otherwise, compare evidence actions `q`: stakeholder clarification, read-only technical probe, cross-boundary contract test, or escalation. Value a query by its expected **reduction in *decision regret*** rather than generic uncertainty reduction, minus user-interruption/test cost. A user response can update normative `s` (subject to authority) but cannot establish technical `f`; a tool probe can update `f` but cannot authorize changing `s`.

The executor only commits when the evidence supports an authorized change, the independently authored current-contract checks pass, and remaining risk is acceptable. Otherwise ask/probe/escalate.

### Why this might actually work (without magical guarantees)

- Uncertainty is decision-relevant only if different plausible worlds justify *different edits*. This avoids wasting calls on ambiguities that cannot change the repair.
- A concrete **set of admissible edits**, rather than only an LLM's confidence score, makes hallucinated authorization harder to overlook.
- Distinguishing sources of evidence prevents a frequent category mistake: confusing "the tool can perform X" with "the stakeholder has authorized X".
- Counterfactual replay and cross-component contracts reveal consequences that a local failure example cannot.
- Locked independent tests and matched compute measure whether gains come from actual behavior rather than judge manipulation or additional inference.

**WARNING:** expected value of information, robust policy selection, causal replay and requirement provenance are established ideas. These reasons establish conceptual plausibility, NOT novelty of the mathematics. The core contribution would be a new tractable *repair-disagreement approximation* plus *new empirical evidence* in this specific joint longitudinal task.

### Minimal implementable algorithm (first use heuristics, no RL)

1. Parse incumbent design + active obligation register, including approved supersessions.
2. Enumerate a bounded set of materially different intent/cause worlds consistent with the public trace; retrieve source evidence and tests.
3. Generate a small change set; include `retain` and `escalate`.
4. Use differential sandboxes to measure edit-by-obligation consequences where feasible; mark unknown cells explicitly.
5. Compute whether all plausible worlds allow the same acceptable edit(s). If yes, act using ordinary regression safeguards.
6. If not, choose the cheapest *authorized* ask/probe/test action predicted to separate the competing **repair decisions**, not merely world descriptions.
7. After observing evidence, update hypothesis set and rerun the change decision. Commit only after independent acceptance testing.
8. Log both accepted and rejected changes; on each new requirement, update active obligations with approval-provenance rather than blindly accumulating old tests.

Start with a short tree search over 2–4 evidence steps and explicit budgets; learn a policy only if search is meaningfully better than the strong LLM heuristic on held-out applications and too costly to deploy as-is.

## Crucial evaluation design: paired-world episodes plus real revisions

**Unit:** a versioned agent application, one ambiguous incident report, the public trace, hidden independently established `s` and `f`, the allowed evidence APIs, and real patch/test artifacts.

Construct paired worlds with byte-identical public observations yet *different justified durable edits*. Contrasting worlds alone are insufficient: include resolved incidents where correct action is immediate edit, false/stale incidents where correct action is retain, legitimate user supersession, half-fixed issues, root causes requiring two concurrent edits, cases in which neither ask nor probe can resolve uncertainty, and cases where **both** are needed.

Control both interventions via a 2x2 factorial: **stakeholder contract variant (S0/S1) x technical cause (F0/F1)**. Vary the information source cost to prevent trivial always-ask/probe. The same approved contract may require multiple valid patches; score acceptable repair sets, not a single gold text diff.

**Primary evaluation:** (a) authorized task resolution, (b) rate/severity of unintended changes to still-active requirements, (c) total question+diagnostic+rollout cost, (d) false persistent-edit rate, (e) repair-decision regret against a stronger privileged oracle, (f) transfer to whole held-out agent families, (g) longitudinal stability after 3–6 revisions.

**Controls:**
- Strong direct editor, editor+ordinary tests, editor+approved specs, editor+specs+impact tests.
- Strong **composed** LLM baseline with *exactly the same* ask/probe/edit/retain/escalate APIs, tests, costs and budgets. Include simple fixed rules (always ask, probe first, no change when unreproduced).
- CONTRA-style selective clarification + DoVer-style probing + DAAF-style repair targeting + conventional acceptance gate: adapted with care to equal action spaces.
- Ablations: remove stakeholder authority; remove cross-component tests; replace repair-disagreement selection with entropy gain/normal VoI; remove persistence; remove supersession; remove independent evaluator.
- Upper controls: oracle intent, oracle cause, oracle both; check whether oracle intervention corrects failure at all.

**Most important falsifier:** if the composed existing baseline performs as well as the proposed decision-disagreement method with the same evidence/cost, abandon algorithmic novelty. Benchmark validity can still be valuable if the tasks are independently grounded.

## First empirically grounded scenario (source inspection, NOT reproduced)

[LangChain PR #40530](https://github.com/langchain-ai/langchain/pull/40530) (merged Sept 22 2026) introduced synthetic error `ToolMessage` objects for malformed tool calls in the central agent factory, plus agent-side tests. [Issue #40853](https://github.com/langchain-ai/langchain/issues/40853) reports that Anthropic serialization then emitted a `tool_result` without a parent `tool_use`. [PR #40864](https://github.com/langchain-ai/langchain/pull/40864) (merged Sept 27) added the missing Anthropic `tool_use` serialization and provider tests. Code diffs and issue reproduction have been inspected using GitHub.

This example motivates **cross-boundary consequence testing**, NOT "ask the user": the stakeholder authorization is not uncertain, so a technical contract test is the right evidence. If an ordinary integration test catches the issue, that is the correct baseline and no novel learned module is needed. Other episodes must have genuine stakeholder-uncertainty to show that a joint decision mechanism is warranted.

## Stop/go checklist — must pass before a paper claim

1. The benchmark does not leak hidden worlds through filenames, formatting or metadata; independent human reviewers agree on acceptable changes.
2. There are credible stakeholder authority and technical fault alternatives, not arbitrary manufactured labels.
3. Existing composed methods fail for a **documented** reason, even at matched actions, information and compute.
4. The proposed mechanism reduces *false permanent edits and/or severe regressions* at comparable task success and cost, with confidence intervals across held-out application families.
5. Ablation specifically shows *repair-disagreement/authority typing* matters beyond a generic asking policy, ordinary tests and root-cause diagnosis.
6. Train/validation/test remain separate; cost increases and benchmark search overfitting are attributed with HDA-style controls.
7. No unnecessary RL: only train when a residual task and transfer benefit are measured.

## Immediate next steps

1. Verify the full texts of **CONTRA, KPHarness, DAAF, SAGE-Agent, DoVer, SpecPath, CAMP, and minimal repair families**, specifically whether any combine **normative and technical competing worlds with persistent architecture edits**. Do not infer absence from abstracts.
2. Build 12–20 paired-world prototypes grounded in **two real runnable applications** (one retrieval/router, one tool/handoff); review them manually and use provider-boundary examples.
3. Implement an ordinary LLM composer with all evidence actions **first**; preregister the costs and admissible action sets.
4. Implement an explicit repair-disagreement heuristic with a truthful unknown category for untested edit consequences. Avoid simulated probabilities presented as calibration.
5. Compare policies in small independent executions. If no residual failure, record negative result and redirect to product engineering or measurement research.

## Interpretation and novelty confidence

- High confidence that the generic ideas (clarification, active diagnosis, no-change, escalation, repair-set recovery, regression gates, continual optimization) are prior art.
- Moderate confidence that the *joint* longitudinal agent-architect decision problem has less direct empirical coverage in the **scoped sources** examined; this is NOT proven absence of prior research.
- Low confidence that the proposed algorithm beats a strong composed baseline: **untested**.
- Strong conceptual reason why *decision-sensitive evidence* can outperform generic uncertainty reduction in a crafted controlled task; real-world advantage is a falsifiable hypothesis.

**Proposed working title:** *When Should an AI Architect Change Its Agents? Decision-Aware Evidence Acquisition for Persistent Agent Design*.
