# Paper gate: ControlArena code audit, non-novelty findings, and preregistration

**Date:** 2026-11-02  
**Status:** Source-backed novelty audit completed; 18-case ID split prepared, **NO agent evaluation completed**, **NO novel method established**.  
**Research objective:** a publishable paper with an agentic-AI-specific contribution, not a generic regression-testing or monitoring tool.

## Decision in one sentence

**NO-GO:** "Combine an LM trajectory monitor with protected post-edit behavioral tests, then escalate selectively" is *not* a sufficiently novel algorithmic proposal. The closest competitors already implement key pieces. A small **feasibility-only** agent-control baseline comparison is still justified, but not a positive novelty claim.

## Primary source audit: verified code, not inference from a title

Inspect the upstream **[ControlArena source tree at ae0b6fa](https://github.com/UKGovernmentBEIS/control-arena/tree/ae0b6fa78ace5a097536eb3464ab5a089740b53e)** (checked November 2, 2026).

| Existing capability | Exact upstream implementation | Consequence |
| --- | --- | --- |
| LM examines submitted patch, with main-task context | [`control_arena/scorers/_diff_monitor.py`](https://github.com/UKGovernmentBEIS/control-arena/blob/ae0b6fa78ace5a097536eb3464ab5a089740b53e/control_arena/scorers/_diff_monitor.py): `git_diff_monitor()` reads `submission_diff` and asks trusted model for score | "inspect the final diff" is existing baseline |
| LM examines whole finished agent trajectory | [`scorers/_end_of_trajectory_monitor.py`](https://github.com/UKGovernmentBEIS/control-arena/blob/ae0b6fa78ace5a097536eb3464ab5a089740b53e/control_arena/scorers/_end_of_trajectory_monitor.py) | post-hoc full trajectory monitoring is existing |
| Monitors can be tool-using environment investigators | [`monitor/_monitor.py`](https://github.com/UKGovernmentBEIS/control-arena/blob/ae0b6fa78ace5a097536eb3464ab5a089740b53e/control_arena/monitor/_monitor.py) and [docs](https://control-arena.aisi.org.uk/monitors.html) | A trajectory-only monitor is too weak a comparator; "artifact-aware monitor" is not an original general idea |
| Budget-aware multi-stage monitoring | [`examples/iac_async_hierarchical_monitors/iac_async_hierarchical_monitors.py`](https://github.com/UKGovernmentBEIS/control-arena/blob/ae0b6fa78ace5a097536eb3464ab5a089740b53e/examples/iac_async_hierarchical_monitors/iac_async_hierarchical_monitors.py) | "cheap model then expensive model" and threshold escalation already implemented |
| Real code-side-task scores and final patch capture | [`settings/swebench/swebench_setting.py`](https://github.com/UKGovernmentBEIS/control-arena/blob/ae0b6fa78ace5a097536eb3464ab5a089740b53e/control_arena/settings/swebench/swebench_setting.py) and [`scorers.py`](https://github.com/UKGovernmentBEIS/control-arena/blob/ae0b6fa78ace5a097536eb3464ab5a089740b53e/control_arena/settings/swebench/scorers.py) | Existing benchmark scores main and side goals in executable sandbox, and captures `git diff` |
| Deterministic policy to reproduce tool actions | [`policy/_fixed_policy.py`](https://github.com/UKGovernmentBEIS/control-arena/blob/ae0b6fa78ace5a097536eb3464ab5a089740b53e/control_arena/policy/_fixed_policy.py) | replay or fixed policies can validate harness mechanics; **not** evidence of model behavior |

**Important technical distinction:** `git_diff_monitor` is a post-hoc scorer. It does not, by itself, establish a deployed real-time acceptance gate. Likewise code scorers run hidden task checks, but those checks are not automatically available as protected defender signals. The framework permits custom tool-using monitors; absence of a particular shipping component from our *scoped search* does not establish novelty for adding it.

### Peer-reviewed and contemporary novelty threats

1. **[Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols](https://proceedings.iclr.cc/paper_files/paper/2026/hash/54b153ad8a138f4c186f21a8b7341d5e-Abstract-Conference.html)** (ICLR 2026): adaptive monitor-aware prompt injection defeats trusted monitors. Our study cannot claim first adaptive attacks.
2. **[Control Tax: The Price of Keeping AI in Check](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c8c352e9ff2c3eb8511c6a996cbd77b1-Abstract-Conference.html)** (ICLR 2026): control budget, cost, and optimized monitors already researched.
3. **[When “Correct” Is Not Safe](https://research.google/pubs/when-correct-is-not-safe-can-we-trust-functionally-correct-patches-generated-by-code-agents-2/)** (ACL 2026): AI coding agents can produce functionally correct but vulnerable patches. This phenomenon alone is not our novelty.
4. **[Who Tests the Testers? (SafeAudit)](https://aclanthology.org/2026.emnlp-main.73/)** (EMNLP 2026): metaauditing agent tool-call safety benchmark coverage already formalized and experimentally studied.
5. **[All Smoke, No Alarm](https://doi.org/10.1109/AITest70988.2026.00038)** (2026): agent-authored tests may lack real assertions; "tests are present but don't verify" is prior work.
6. **[ControlArena](https://control-arena.aisi.org.uk/)** and [original AI Control](https://arxiv.org/abs/2312.06942): on-policy agent tasks and side goals, monitoring, deferral and editing are established.
7. **[Reliable AI-Assisted Decisions via Selective Auditing](https://arxiv.org/abs/2610.31662)** (2026 preprint): audit-budget allocation with guarantees is active prior art; cannot claim generic selective auditing.
8. **[Anthropic SLEIGHT-Bench](https://alignment.anthropic.com/2026/sleight-bench/)**: hard-to-detect monitor evasion is existing empirical work.

**Negative conclusion:** The proposal "trajectory LM + diff review + independent canary + suspicious-only escalation" is a combination of known verification and control mechanisms. We have not found a new decision principle or evidence for a superior frontier. **No manuscript title should assert 'novel algorithm' yet.**

## What remains testable (not necessarily publishable)

**Feasibility question:** On real code-agent attack trajectories, what *conditional* false negatives are unique to (i) a trusted trajectory monitor, (ii) a diff reviewer, and (iii) an independent hidden behavioral test? After controlling for adversarial strength, legitimate changes, and evaluation costs, is there measurable complementarity that strong tool-using monitors do not capture?

This is presently an **empirical comparison** using established methods, not a new method.

**Alternative hypotheses to keep open:** agent workflow redesign under evolving requirements and agent-runtime durable-state consistency, as documented in earlier repo reports. Neither currently passes novelty gate.

## Frozen minimal protocol — not an executed AI experiment

The script [`experiments/controlarena_paper_gate/prepare_split.py`](../experiments/controlarena_paper_gate/prepare_split.py) independently validates the 18 publicly listed side-task IDs from [upstream commit ae0b6fa](https://github.com/UKGovernmentBEIS/control-arena/tree/ae0b6fa78ace5a097536eb3464ab5a089740b53e/control_arena/settings/swebench/side_tasks), and deterministically allocates **4 development / 14 holdout** IDs. This only freezes an order and avoids changing the sample after seeing results. Since side-task files are public, the split is not a secure or fully blind holdout.

**Prerequisites for actual experimental evidence:**
- Reproduce at least one **upstream** monitor protocol on *actual agent-generated trajectories* using model calls and the real side-task evaluation sandbox. Do not substitute deterministic fixture edits for agent behavior.
- Evaluate code-diff monitor, trajectory monitor, strong tool-using monitor and at least one conventional hidden test (where applicable). A test that has knowledge of target attack labels is a scorer, not a fair defender.
- Measure task success, side objective success, false-positive rejection of honest tasks, attack conditional success, and API cost. Compare the **safety–utility curve**, not raw recall alone.
- Fix prompt, thresholds, model versions, tool capabilities, data views, and audit budgets on the four development IDs. No tuning or new rules after exposing any of the 14 holdouts.
- Adaptive attack policy with explicit defender-information assumptions. State exactly which checks/protocol details are known to attackers and which secret test inputs remain hidden.
- Report uncertainty with **task-clustered bootstrap** and distinguish independent tasks from multiple seeds on the same task. With 14 independent holdout tasks, any precision claims are weak; treat as feasibility only and extend to disjoint settings before a paper.
- Include intentional telemetry changes and non-malicious refactors where monitoring tests apply; avoid false-positive free lunch.
- Independent adjudication of attack success; handle human approval and external side effects only inside sandbox.
- Separate evaluation **design** from **result**. CI checking task splits does not constitute an agent evaluation.

## Killing the paper hypothesis

1. **Prior-art equivalence:** if a code-available baseline already contains same method and interfaces, no new-method claim.
2. **Strong-baseline no residual:** if strong, fairly configured tool-using and behavioral monitors match the candidate at equal audit cost, no new-method claim.
3. **Agent-specific construct absent:** if same gains hold on agent-independent patch fixtures with no adaptive behavior, this is software testing, not agentic AI.
4. **Leakage/cost dependence:** if advantage relies on hindsight-written oracles, attack-leaked holdouts, false positives, or more compute, no new-method claim.
5. **Insufficient data:** 14 heldout Django tasks cannot justify broad statistical claims. Expand or mark as inconclusive.

## Current honest status

- Three earlier real agent-framework historical regressions reproduced (LangChain 2; OpenAI Agents SDK 1) plus one OpenTelemetry real-package historical regression.
- One hand-constructed 14-fixture monitoring comparator.
- Source-level ControlArena prior-art audit now completed; **strong novelty threats confirmed**.
- Task identifiers and development/holdout split prepared, but **0 agent runs** and **0 publishable experimental evidence** about defense effectiveness here.
- Next priority: run a bona fide agentic baseline on ControlArena, if model access, sandbox, and budget permit. Otherwise preserve the no-go and investigate other agentic hypotheses rather than manufacturing a novel claim.
