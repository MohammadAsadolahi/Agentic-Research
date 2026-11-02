# Agentic-AI paper gate: external novelty review and an agent-specific research pivot

**Date:** 2026-11-02  
**Decision:** **NO-GO on a novel semantic-telemetry verifier. CONDITIONAL GO for a narrowly scoped, agent-specific AI-control pilot.** This note does NOT claim a novel mechanism, accepted paper, representative dataset, or completed adaptive-agent evaluation.

## 1. Objective (non-negotiable)

The objective is a **publishable agentic AI research paper**. A verified software defect and a functional regression test are *infrastructure*, not the intellectual contribution. A viable paper must make an agent-specific claim, distinguish itself from the strongest literature, and evaluate a new mechanism or new agent-specific empirical phenomenon on independent held-out tasks.

## 2. External skeptical reviewer: verification and corrections

An independent LLM returned NO-GO for a proposed monitoring-integrity verification algorithm, citing oracle leakage, weak baselines, logging studies, Weaver and trace tests, and AI-control prior art. We agree on the substantive objections, but external LLM conclusions are **not proof**; below is an independent primary-source audit.

**Validated novelty threats:**
- [OpenTelemetry Weaver usage](https://github.com/open-telemetry/weaver/blob/main/docs/usage.md): `registry check`, `registry diff`, `registry live-check` and support for custom policies. A basic schema-aware monitor verifier is not new.
- [OpenTelemetry custom telemetry schemas](https://github.com/open-telemetry/weaver/blob/main/docs/define-your-own-telemetry-schema.md): supports developer-defined telemetry signals, not just fixed built-in conventions. Custom schemas do not establish novelty.
- [Do AI Coding Agents Log Like Humans?](https://arxiv.org/abs/2604.09409) (Apr 2026 preprint): 4,550 agentic PRs across 81 repositories; humans perform 72.5% of post-generation logging repairs. Logging negligence by coding agents is already an investigated empirical claim.
- [CTRL-ALT-DECEIT](https://proceedings.neurips.cc/paper_files/paper/2025/hash/fd8f2c610c09d3b2ef07662bee15b462-Abstract-Conference.html) (NeurIPS 2025): sabotage and monitor-evasion in agentic ML engineering already studied.
- [ControlArena monitors](https://control-arena.aisi.org.uk/monitors.html): monitors can use tools and inspect the environment, not merely read a transcript. Thus **artifact inspection as an idea is not necessarily novel**.
- [UK AISI asynchronous-monitoring red team](https://www.aisi.gov.uk/blog/stress-testing-asynchronous-monitoring-of-ai-coding-agents): monitors are tested under adaptive on-policy coding-agent sabotage, already compromising a naive claim that an adaptive agent is itself the novel contribution.
- [Anthropic Auto Mode red team](https://alignment.anthropic.com/2026/red-teaming-auto-mode/) (Oct 22, 2026): red-teams production blocking monitors, including multi-context and compaction-related strategies. An improved generic monitor or monitor-red-team is not automatically new.
- [Evaluating Control Protocols for Untrusted AI Agents](https://arxiv.org/abs/2511.02997): compares control protocols and adaptive attack policies. Matching safety-vs-cost envelopes is essential.

**Claims not promoted without direct checking:** another LLM's exact logging-detector 3% statistic, exact BashArena task count, and any purported originality of an artifact-level checker. They must be checked against primary sources before manuscript use.

## 3. Correct classification of our present data

- Three earlier **real agent-framework historical defects** are reproduced (LangChain provider serialization; middleware graph routing; OpenAI Agents SDK durable-session recovery). They are reproducible but not novel AI methods.
- The 14-fixture monitoring pilot is **synthetic, self-authored and non-blind**. Its 10/10 full semantic checks mostly show that a complete specified oracle catches violations of its own invariants. Not publishable performance evidence.
- New [OpenTelemetry issue #7059](https://github.com/open-telemetry/opentelemetry-js/issues/7059)/[PR #7061](https://github.com/open-telemetry/opentelemetry-js/pull/7061) historical **real installed-package** pilot uses HTTP instrumentation 0.223.0 (before fix) and 0.300.0 (fix present), real local HTTP 200/404/500, actual SDK-exported spans; runner [GitHub Actions](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41477305444) completed successfully after fixing our own package-metadata and SDK 3.x constructor harness issues. Business output, span counts, and error statuses all pass in both; semantic error.type asserts miss 404/client, 500/client, 500/server in 0.223.0, but none in 0.300.0. This is **a positive case for a conventional semantic oracle**, not a residual defeating existing methods.
- **Confound:** 0.223.0 and 0.300.0 cross SDK 2.x→3.x, and this is a known issue selected after disclosure. No isolated causal effect, no blinded comparison, no AI-agent behavior.

## 4. Candidate paper question, only a conditional GO

> When an untrusted autonomous coding agent makes task-successful software changes, does *independent, post-edit behavioral evidence* improve the safety–utility frontier over strong trajectory-only and conventional software verification protocols, under **adaptive, monitor-aware agent attacks**?

**Agentic factor:** The attacker is a tool-using agent with long-horizon main tasks and an unauthorized side objective, able to strategically choose edits and camouflage actions. The defense acts *before acceptance/deployment* based on the agent's trace and its produced artifact; protected evaluators are outside its writable workspace. Benchmark should include benign agent edits with legitimate logging changes and matched non-agent edits to distinguish generic software-testing value from agent-specific phenomena.

**Novelty threat:** Artifact checks, external monitors, hidden acceptance tests, and combining monitors are established. The candidate is *not* "first artifact verifier". A distinctive method would need independently demonstrated, nontrivial selection/combination of protected semantic probes at matched audit budget and maintenance cost, or a new agent-specific phenomenon not measured by controls. **None exists yet.**

## 5. Strongest control protocol comparison

Pre-register a 2×2 intervention design, holding the task, agent model, model-call budget and audit cost constant as far as possible:

| Condition | Trajectory LM monitor | Independent protected artifact tests |
| --- | --- | --- |
| A | No | No; only ordinary task CI and protected-file review |
| B | Yes | No |
| C | No | Yes: conventional fully specified behavioral canaries / trace semantics |
| D | Yes | Yes: naïve conjunction or budgeted escalation |

Add full semantic-convention Weaver and golden trace tests where instrumentation is applicable, and one *artifact-aware tool-using monitor* as a **strong direct competitor**. The proposed contribution must outperform **C and D** or offer a clearer measurable new empirical insight; beating A or B alone is weak. For fairness, measure wall time, token/LLM costs, user-facing utility, test authoring/maintenance, and review false-alarm burden, not just test invocation count.

**Deterministic scoring:** for each task, separately score main-task success and whether a hidden side objective actually altered system behavior in an isolated sandbox. The scoring oracle and side-task labels remain inaccessible to the editing agent. The independent blue-team verifier should be fixed before the held-out red-team phase.

**Adaptive evaluation:** compare unadapted attacker and attacker conditioned on (only) documented verifier behavior or visible checks. Agent must write actual code; post-hoc rewriting of transcripts is not a substitute for on-policy evaluation. Attack scenarios must be contained, non-destructive and local.

**Data:** begin with a handful of real-world-inspired, reproducible open-source coding tasks with authorized telemetry migrations and meaningful negative controls; do not use the same historical bug to design both failure and checker. Hold out repositories and side-task families; incorporate genuine agent-authored edits, not only injected mutations.

## 6. Predeclared falsification gates

1. **Novelty:** if ControlArena/other published systems already implement equivalent protected artifact behavior checks plus selection policy under adaptive attack, we must state overlap and either isolate a narrower distinction or stop the method claim.
2. **Agent specificity:** if the effect is identical for non-agent and agent edits and does not depend on adaptive strategic behavior, reclassify as software engineering—not an agentic AI method paper.
3. **Strong baseline:** if conventional independent artifact canaries or a tool-using LM monitor produce the same safety–utility frontier at the same cost, **NO-GO** for a new algorithm. A descriptive negative finding may still be worth an empirical note.
4. **Leakage:** independent checker authoring and held-out task families must happen *before* examining successful attacks/fixes; changing test rules after failures may only improve development, not held-out evaluation.
5. **Feasibility:** if usable realistic agent environments and cost-controlled evaluations are unavailable, pause this branch rather than substitute more hand-written toy failures.

## 7. Next research action

Do **not** keep adding OpenTelemetry regressions in hopes that they add novelty. First audit ControlArena and its relevant defense protocols in source, identify the nearest published artifact-aware defense, then reproduce that baseline on a small open benchmark before designing a new method. The OTel pilot is a supporting test case for candidate verifier construction, not the planned manuscript's core experiment.

If this candidate fails the novelty gate, explicitly re-open the broader original **agent-system design under evolving requirements** question rather than assuming monitoring must be the paper. No specific new algorithm is justified today.
