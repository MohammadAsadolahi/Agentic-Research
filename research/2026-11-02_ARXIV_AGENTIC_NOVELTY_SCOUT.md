# November 2026 arXiv novelty scouting: find the paper, not another demo

**Date:** 2026-11-02. **Scope:** targeted search of 2026 arXiv and primary paper abstracts through November 2. This is an *adversarial candidate scan*, NOT a systematic review and NOT proof that a gap is absent/present. Search queries, paper abstracts and links were checked. Full paper methods/code have **not** been exhaustively reviewed across this list. Research goal remains a **publishable agentic AI contribution**, not a generic software checker.

## Decision summary

- **NO-GO** on a generic monitor-verifier algorithm, generic evolving-requirements benchmark, generic parallel-agent merge benchmark, agent research citation/evidence checker, or semantic tool-context invalidation mechanism. Strong near-neighbor papers already exist.
- **CONDITIONAL exploratory candidate:** **ShiftTogether: Measuring Interaction Failures in Parallel Coding Agents Under Mid-Execution Requirement Changes**. The candidate tests a *factorial interaction effect*, not a mere sum/combination. Its existence, magnitude, novelty and practical importance are **unmeasured**. Do not claim the first benchmark or new algorithm.
- **Kill quickly** if current benchmarks already contain the crossed intervention, or the experimental interaction is absent after realistic controls and real agent runs.

## Papers inspected by research dimension (direct arXiv record unless noted)

### A. Dynamic goals, requirements and histories — heavily occupied
1. [IntentDelta: A Human-Constructed Benchmark for Evolving User Intent](https://arxiv.org/abs/2610.33806), 2026-10-24: 638 trajectories; user intent revision, cumulative intention and action scores. Threatens "first evolving user intent" claim.
2. [DynaRev: Benchmarking Web Agents under Dynamic Goal Revision](https://arxiv.org/abs/2610.40133), 2026-10-29: 181 web-agent tasks, milestone-based revision. Threatens milestone intervention design.
3. [SWE-Shift: Evaluating Coding Agents in Evolving Workspaces](https://arxiv.org/abs/2610.32196), 2026-10-23: 120 scenario pairs, 12 workspace-change families, 9 intervention positions; key nearest coding-agent shift benchmark.
4. [SpecPath: Testing Coding Agents Across Contract-Equivalent Specification Histories](https://arxiv.org/abs/2608.09799), 2026-08-10: compares contract-equivalent requirement histories; first coding-agent path-sensitivity result is NOT novel.
5. [EvoCode-Bench: Evaluating Coding Agents in Multi-Turn Iterative Interactions](https://arxiv.org/abs/2605.24110), 2026-05: 26 persistent coding tasks, 227 rounds; longitudinal requirements not new.
6. [When Requirements Interact: Scaling Long-Horizon Coding via Interdependent Specifications](https://arxiv.org/abs/2610.40256), 2026-10-29: CodeSpecWeave provides substantial coupled-spec task generation and benchmarks.
7. [Revisable by Design: A Theory of Streaming LLM Agent Execution](https://arxiv.org/abs/2604.23283), 2026-04-25: reversibility, compensation and reactive revision absorber; generic rollback/compensation under revision is not a fresh theory.
8. [Serving a Revisable World: Versioned Execution for Interruptible Agents](https://arxiv.org/abs/2610.01160), 2026-10-01: old execution authority revocation and inherited valid KV state.
9. [When Users Change Their Mind: Evaluating Interruptible Agents in Long-Horizon Web Navigation](https://arxiv.org/abs/2604.00892), 2026-04-01: interruption and persistent state changes already studied.

### B. Parallel and multi-agent coordination — heavily occupied
10. [Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development](https://arxiv.org/abs/2609.25396), 2026-09-21: tests patch pairs individually and after merging; important nuance: one interference case in 834 runs on 417 real merged Django pairs, but constructed real-helper tasks show 97% interference. Avoid converting engineered failure rate into real-world incidence.
11. [Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems](https://arxiv.org/abs/2610.01042), 2026-10-01: ICR protocol distinguishes communication benefit from extra reasoning; a communication ablation must include no-message matched-compute control.
12. [GenCoord: Skill-Path Commitments under Private Information](https://arxiv.org/abs/2608.22055), 2026-08: executable handoff commitments under private information.
13. [When Should AI Agents Ask? Clarification Requests Under Limited Human Attention](https://arxiv.org/abs/2610.41129), 2026-10-30: coordinated ask/search decisions under shared human attention budget.

### C. Memory, stale evidence and cross-view state — heavily occupied
14. [When Agent Context Goes Stale: Incoherence in Volatile Agent Context](https://arxiv.org/abs/2610.05281), 2026-10: Concord source-linked observation invalidation, context refresh, and benchmark. "Version all tool observations" alone not new.
15. [When Context Changes: Understanding Update Failures in LLMs](https://arxiv.org/abs/2609.38866), 2026-09: controlled stale binding under changed facts.
16. [Toward User-Conditioned Evaluation of Personal LLM Agents under Temporal Interventions](https://arxiv.org/abs/2607.21635), 2026-07: position-paper benchmark design for cross-component temporal failures.

### D. Long-horizon critics, judges and evaluation — occupied
17. [AgentHorizon: Evaluating Agentic Judges for Long-Horizon Computer-Use Tasks](https://arxiv.org/abs/2610.11050), 2026-10: 1,373 instruction-trajectory pairs; long-horizon task/evidence audit not first.
18. [From Outcomes to Steps: Reliable Success-Aware Critic Learning for Long-Horizon Language Agents](https://arxiv.org/abs/2610.27623), 2026-10: success-aware critic; generic step-credit estimation novelty threat.
19. [Recursive Environment Scaling for General Long-Horizon Agents](https://arxiv.org/abs/2610.16397), 2026-10: systematically transforms benchmark environments while preserving goals.

### E. AI scientists and scientific evidence — rapidly occupied
20. [DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?](https://arxiv.org/abs/2609.33357), 2026-09: analysis/evidence verification and revised hypotheses.
21. [PAPERBENCHX: Can AI Reproduce Science Across Disciplines?](https://arxiv.org/abs/2610.39744), 2026-10-29: 93 expert-defined replayable scientific reproduction tasks.
22. [RECLAIM: Can Agents Reproduce the Claims of Machine Learning Papers?](https://arxiv.org/abs/2609.28850), 2026-09: 100 reproduction tasks with budget and external evidence.
23. [Beyond fabrication: Misattributed numbers in papers written by AI research agents](https://arxiv.org/abs/2610.38691), 2026-10-28: deterministic claim-to-evidence verification and misattribution analysis.
24. [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](https://arxiv.org/abs/2608.05179), 2026-06: evidence and novelty verification gap already formally surveyed.
25. [Can LLM Agents Discover? Evaluating Creativity on ML Engineering Tasks](https://arxiv.org/abs/2608.30047), 2026-08: P-creativity, H-creativity, usefulness.

### F. Agent control — already audited separately
See [primary-source ControlArena gate](2026-11-02_CONTROLARENA_PRIMARY_SOURCE_NOVELTY_GATE.md). Diff monitors, tool-using monitors, hierarchical cost-aware escalation and fixed-trajectory replay already implemented. Adaptive attacks, control budget and evaluation sabotage have substantial prior art.

## Opportunity ranking (investigator judgment, not estimated acceptance probability)

| Candidate | Specific residual hypothesis | Strongest visible threat | Decision |
| --- | --- | --- | --- |
| **ShiftTogether** | A measurable superadditive failure occurs **only** when concurrency and mid-execution revision coexist; standard peer-communication and single-agent replanning fail to remove it | Passes Alone Fails Together + SWE-Shift + CodeSpecWeave + SpecPath | **Conditional best for falsification; not novel yet** |
| Research-agent evidence integrity | Agents systematically misattribute experimental values after branching or repeated runs, detectable via causal provenance | Beyond fabrication (Oct 28) + DISCERN + RECLAIM | NO-GO on a general paper without distinctly new causal phenomenon |
| Stale shared tool evidence | Independent workers act on outdated observations after intervening edits | Concord + SWE-Shift + collaboration benchmarks | NO-GO on generic source invalidation |
| Oversight continuity | Artifact-level semantic canaries detect changes unseen by monitor | Weaver / trace tests / ControlArena tools | NO-GO on a novel algorithm without strong residual |
| Longitudinal agent architect | Meta-agent improves ability to preserve system design under evolving requirements | EvoCode-Bench, SWE-Shift, SpecPath, broad optimization/architect search | Still interesting long term, but NO-GO as presently specified |

## Final caution

The lead's *intersection* has not been proven unstudied. Recasting a pair of existing benchmarks as a 2x2 combination does not itself make a contribution. It must show a measurable agent-specific interaction beyond reasonable noise and ceiling effects, accompanied by at least one new mechanistic explanation or useful intervention beating synchronized-broadcast, serial, replan and matched-compute baselines. If not, report a negative result.

Do not turn selected historical bugs or a toy example into prevalence estimates. Do not use title wording implying discovery until the holdout evaluation actually supports it.
