# Broad research pivot and third real-source reproduction

**Updated:** 2026-11-02  
**Purpose:** deliberately break anchoring on "RL architect", "prompt overfitting" and "change-aware contract tests".  
**Current status:** three historically grounded *mechanisms* independently reproduced with real pinned source and simulated external dependencies, but **no novel method or strong-baseline failure discovered**. This is NOT a complete systematic literature review.

## 1. Verified third real-source result (different repository)

**OpenAI Agents SDK issue [#4615](https://github.com/openai/openai-agents-python/issues/4615)** describes a completed and approved tool action that is retained in the in-memory RunState/public replay but lost from the durable Session after an injected atomic write failure. [PR #4630](https://github.com/openai/openai-agents-python/pull/4630) implements recovery. The issue links a provider-neutral deterministic reproducible script.

**We actually executed this against pinned upstream Python source** using [GitHub Actions run #41472661002](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41472661002). The workflow used a no-API-key `ScriptedModel`, a fail-once Session, and an approval-gated `charge` tool with deterministic externally observed side effect.

| Exact SDK source | Side-effect executions | Public replay call/output | Durable Session call/output | Outcome |
| --- | --- | --- | --- | --- |
| [v0.22.0 SHA 4df9ecfa](https://github.com/openai/openai-agents-python/commit/4df9ecfae1761ca6fea67cc5a20b383c1d492024) | 1 | 1/1 | **1/0** | Historical failure reproduced |
| [merged fix SHA 787f9d6c](https://github.com/openai/openai-agents-python/commit/787f9d6cc280b476f0367a788077ca7e400d59c1) | 1 | 1/1 | **1/1** | Historical repair reproduced |

Both workflow jobs completed successfully because the pre-fix case correctly *expected* a broken durable Session. Workflow logs print exact call/output counts and `Verified: broken/fixed`. No external model request or charge occurred. Reproducer: [source](../experiments/real_openai_agents_replay/reproduce_session_recovery.py); [workflow](../.github/workflows/openai-agents-replay.yml).

**Method correction and transparency:** The first run [#41472419323](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41472419323) failed on a syntax error from an escaped header in our script. After correction, run #41472661002 verifies the actual behavior. This is a script error, not a framework defect. Dependency subpackages were resolved online by the runner and should be pinned completely for a formal result.

**Critical near-neighbor:** [PR #4630](https://github.com/openai/openai-agents-python/pull/4630) was followed by [issue #4646](https://github.com/openai/openai-agents-python/issues/4646) documenting another persistence failure on a different interruption path. That makes further *branch-completeness/fault-injection* studies plausible, but it doesn't create new mathematics.

## 2. Broad research landscape: adversarial opportunity map

We expanded beyond prompt design into six substantially different literatures and sought the *strongest novelty threat* for each.

| Field | Demonstrated problem / primary source | Already covered: novelty threat | Residual testable question (unproven) |
| --- | --- | --- | --- |
| **Monitoring integrity under routine agent software changes** | [OpenAI Oct 2026 incidents](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring): normal coding edits weakened security alerts / monitor integrations | [Perfect Crime](https://arxiv.org/abs/2609.30266) establishes trace tampering; [ASE APR authority](https://doi.org/10.1145/3843776.3844673) protects verification witnesses; [OpenAI monitor eval](https://openai.com/index/how-we-detect-frontier-model-misalignment/) replays incidents; protected CI and end-to-end canaries are old | Do *routine, apparently successful code changes* silently reduce the effectiveness/coverage of independent oversight even when static file/test-change gates pass? Can a **semantic oversight-continuity probe** beat strong CI+codeowners+normal synthetic alerts at matched cost? |
| **Durable state, side effects and false success** | Our reproduced OpenAI SDK #4615 and two LangChain boundary defects | [LIMBO / Where Does Exactly-Once Live?](https://www.microsoft.com/en-us/research/publication/where-does-exactly-once-live-model-harness-and-tool-contract-effects-on-duplicate-side-effects-in-llm-agents/), Ledger, existing transaction and distributed-systems theory. | Does *cross-view evidence divergence* under faults have a real, unaddressed residual after transactionally correct idempotency and conventional end-to-end state assertions? |
| **Risk-aware cost and calibration across trajectories** | [MAP, ICML 2026](https://proceedings.mlr.press/v306/pan26a.html): practitioners report reliability as top challenge | [ACL survey](https://aclanthology.org/2026.findings-acl.1330/), [TC-ECE](https://arxiv.org/abs/2609.07395), [AISI capability curves](https://www.aisi.gov.uk/blog/more-compute-more-capability-why-ai-agent-evals-need-to-account-for-test-time-compute), [HAL Reliability](https://hal.cs.princeton.edu/reliability/). | Do release decisions from step/trajectory risk estimates fail under *joint* environment/model/tool upgrades with costs held fixed? Is there evidence not covered by existing calibration and cost papers? |
| **Cross-organization delegated authorization** | [npj 2026 seven challenges](https://www.nature.com/articles/s44387-026-00128-9) and [Google Security SoK 2026](https://research.google/pubs/sok-security-vulnerabilities-in-agentic-ai-systems/) flag provenance and authority laundering | [Authorization Architectures (2026)](https://arxiv.org/abs/2609.15906), [Microsoft least privilege](https://www.microsoft.com/en-us/security/blog/2026/07/16/least-privilege-for-ai-agents-identity-access-and-tool-binding/), signed delegation/OAuth are established. | Can realistic **mixed-trust multi-hop agent tool chains** violate end-user intent under correct per-tool OAuth/scopes? Need model beyond access control and reproducible violation. |
| **Long-term memory provenance & poisoning** | [COLLABMEM, EMNLP 2026](https://aclanthology.org/2026.emnlp-main.1194/) exposes role/provenance/authority/retention errors | [SMSR](https://arxiv.org/abs/2606.12703), [origin-bound memory defense](https://arxiv.org/abs/2606.24322), [MAPLE-Guard](https://github.com/xiong-wenjun/MAPLE-Guard) cover much of provenance/poisoning | No candidate advanced here; too crowded without a specific new adversary and formally distinct trust property. |
| **Agent tool-result trust and silent corruption** | [SilentProbe](https://arxiv.org/abs/2609.00035), [Loud vs Quiet Failure](https://arxiv.org/abs/2610.10062) find plausible wrong results accepted as valid | [RetryRealistic](https://gunkaynar.com/publications/fabricate.html), [Traverse](https://arxiv.org/abs/2609.17930) and verification-first monitors already measure and repair | Build on existing fault injection to test systematic, *testable* trust boundary not covered; not simply "detect silent tool errors." |

### Critical external signals

- [MAP ICML 2026](https://proceedings.mlr.press/v306/pan26a.html): 20 detailed case studies and 86 surveyed practitioners, 26 domains, with reliability the most-cited engineering challenge (within this study).
- [OpenAI Oct 2026 monitor-change incidents](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring) provide real case narratives, but internal source code is not available for a public executable reproduction. Any recreation using a toy repository is a *model of the case*, not independent reproduction of its exact mechanism.
- [LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266) means "agents can delete logs" is NOT new.
- [Whose Oracle Is It?](https://doi.org/10.1145/3843776.3844673) means separating agent-editable tests from authorized acceptance evidence is NOT new.
- [All Smoke, No Alarm](https://arxiv.org/abs/2606.18168) already quantifies weak/no oracle signals in agent-authored test patches. Test integrity itself is not novel.
- [Where Does Exactly-Once Live?](https://www.microsoft.com/en-us/research/publication/where-does-exactly-once-live-model-harness-and-tool-contract-effects-on-duplicate-side-effects-in-llm-agents/) explicitly addresses externally committed effects, lost acknowledgements and self-reported false success. Do not claim first agent side-effect/evidence audit.

## 3. Research selection: two independent tracks, not one forced theory

**Track A (broader high-impact SE/security, higher novelty potential but hard to establish): Functional integrity of oversight under benign automated code evolution.**

Potential unit: original app + independent monitor (event -> capture -> detection -> required alert delivery). Ask coding agents to modify unrelated business features or migrate infrastructure without changing authorized security behavior. Evaluate *semantic monitor liveness* in external protected sandbox, not presence of config/strings or claims in PR summaries. Include legitimate authorized monitor migration and harmless refactor negatives. Compare codeowners + protected path gate, static/log configuration diff, ordinary full integration tests, independently authored canary/synthetic alert tests, and candidate change-triggered monitor-continuity checks at matched cost. If existing end-to-end canaries work just as well, the research algorithm has no novelty. The evaluator must not be writable by the coding agent. Keep it ethical and sandbox-only.

**Track B (real, immediately reproducible empirical SE): Cross-view contract consistency and fault-injection at agent runtime persistence/approval transitions.**

Three historical cases already independently replicated in actual source:
- LangChain factory -> Anthropic provider serialization ([CI](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41457528866)).
- LangChain middleware -> graph routing (same CI).
- OpenAI Agents SDK approval -> durable session vs public replay ([CI](https://github.com/MohammadAsadolahi/Agentic-Research/actions/runs/41472661002)).

Build a **prospectively selected** set of additional historical failure paths and compare *existing* tests and strong realistic chaos/fault-injection methods. If conventional state-machine/property tests catch all important defects at low cost, call the result an engineering lesson, not novel agent AI.

**Warning against selection bias:** Do not mine only issue tickets with interesting failures and then estimate prevalence. Sample successful merges too. Do not create "detectable" mutations from our chosen method and claim unseen generalization. Hold out entire fault families/repositories and lock tests before exposing fix commits.

## 4. What would persuade a skeptical reviewer?

- At least 3 independent systems and failure families, including non-LLM and legitimate-change negative controls.
- A predeclared strong comparator (particularly a conventional synthetic monitor canary and ordinary state-machine testing).
- Independent, executable task-level *and* safety/oversight outcome checks; false-positive and maintenance cost reporting.
- Quantitative advantage that survives held-out repositories and controlled compute budgets.
- A specific new mechanism uniquely causing the advantage; ablate without it.
- A clear claim about the construct measured: no blanket "agents are unsafe" conclusions from purposive failures.

## 5. Next actions

1. Begin Track A with an audit of public source-backed monitor-disable incidents and ordinary refactor PRs, not a prematurely invented algorithm; identify available monitor endpoints, canary baselines and reproducible independent assertions.
2. Continue Track B with a fourth *different* failure type or the follow-up OpenAI SDK issue #4646, but first ask whether traditional state-machine testing already catches it.
3. Record a baseline comparison dataset before expanding a novel mechanism. We cannot claim a new algorithm today.
4. Re-audit current competing papers (monitor integrity, active system testing, policy-as-code, protected oracles) immediately before any paper introduction.

## Scientific verdict

The broad-search result is **a pivot in hypothesis priority**, not discovery of a unique algorithm. Prefer **functional preservation of independent oversight under code evolution** as the most interesting *new* experimental direction; retain **cross-view state and side-effect inconsistency** as the proven reproducible infrastructure track. Avoid promoting either until a strong-baseline residual is actually measured.
