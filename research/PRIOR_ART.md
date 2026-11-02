# Prior art, overlap, and source ledger

**Audit date:** 2026-11-02. This is a *scoping prior-art log*, not a complete systematic review or proof of novelty. Primary-source pages below were checked during the documentation update where marked CHECKED. Link presence alone is not empirical reproduction.

## 1. Highest-priority direct competitors — CHECKED primary sources

| Work / source | What it actually covers | Implication for our proposed research | Status |
| --- | --- | --- | --- |
| [Tressoir (CAIS 2026)](https://doi.org/10.1145/3786335.3813143) | Interpretable blueprints with architectures, prompts, tools, invariants; online/offline/human-guided design and evolution. | Extremely close to holistic AI architect concept. Do NOT claim first blueprint designer. Formal evaluation of the full long-term HIL cycle is limited in the paper. | CHECKED, published |
| [RECAP (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.1684/) | Proactive adapt-then-test prompt adaptation under changing constraints; forgetting, transfer, regression. | Continual behavior preservation is an established evaluation problem. | CHECKED, published |
| [PRISM / Beyond Prompts (Findings EMNLP 2026)](https://aclanthology.org/2026.findings-emnlp.1455/) | Resource-bounded harness selection; constrained prompt edits and guarded tool-boundary middleware repairs; held-out reliability metrics. | "Decide prompt or tool middleware" is not new. Scope does NOT include arbitrary runtime redesign. | CHECKED, published |
| [Harness-Delta Attribution (Oct 2026)](https://arxiv.org/abs/2610.22466) | Separates overfitting, test-time compute and residual gains from harness evolution; evaluates held-out transfer. | Benchmark gain alone does not prove generalization; use HDA-like controls. | CHECKED, preprint |
| [Agentic Harness Engineering (Apr 2026)](https://arxiv.org/abs/2604.25850) | Trace-based evolution of harness components; paired edit predictions and verified next-round outcomes. | Revision-impact prediction and auditable edit records are existing ideas; investigate cross-component limitations. | CHECKED, preprint |
| [GRASP (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.452/) | Gated incremental skill edits with balanced held-out probes and hard regression budget. | Basic preservation-aware acceptance gates are existing research. | CHECKED, published |
| [PROSE (Findings EMNLP 2026)](https://aclanthology.org/2026.findings-emnlp.1712/) | Semantic reflection and multiobjective optimization against prompt shortcut/case enumeration. | Principle-based prompt optimization is existing research. | CHECKED, published |
| [CHIVE / counterfactual edits (2026)](https://alignment.anthropic.com/2026/chive/) | Runs actual prompt-edit counterfactual experiments and trains models to predict behavioral effects. | Counterfactual prompt edit prediction is not first-of-its-kind for us. | CHECKED, research article |
| [Do Agent Optimizers Compound? (Jul 2026)](https://arxiv.org/abs/2607.14004) | Sequential evaluation of GEPA, Meta-Harness, RELAI-VCL with regression-aware retention. | Continual improvement + regression control is not novel per se. | CHECKED, preprint |
| [MESH-Harness (Oct 2026)](https://arxiv.org/abs/2610.05300) | LinUCB bandit, performance surrogate and evolution of modular harness implementations under fixed module interfaces. | Directly overlaps learned intervention selection; fixed interfaces limit its demonstrated design scope. | CHECKED, preprint |
| [COMPASS (REALM 2026)](https://aclanthology.org/2026.realm-1.77/) | RL-trained prompt/metapolicy generator using reward and critique feedback. | Do NOT claim first RL design prompter. | CHECKED, published workshop |
| [GEPA (ICLR 2026)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0e9e708b6f48e14fd0ac29e167413f76-Abstract-Conference.html) | Reflective, evaluator-guided prompt evolution, including compound programs; strong comparison to GRPO on its reported tasks. | Strong sample-efficient non-RL baseline. | CHECKED, published |
| [GitHub Agent Architecture skill](https://github.com/github/awesome-copilot/blob/main/skills/agent-architecture/SKILL.md) | Requirements-discovery, design-first agent architecture selection, audits and verification planning; excludes implementation. | Strong product baseline for requirements/architecture assistance. | CHECKED, repository documentation |

**Interpretation notes:** HDA's often-cited 54% and 14% figures refer to *21 experimental settings with significant search-set gains*, not universal prevalence. RECAP's no-significant-improvement finding applies to its evaluated proactive protocol. PRISM's edits are constrained at tool boundaries. MESH's module slots have defined interfaces. Do not erase these limitations when citing results.

## 2. Important additional leads from previous discussion — RECHECK before asserting details

These were discussed during the investigation but were not individually revalidated against their full texts in this documentation pass. Treat as reading queue, not verified novelty clearance.

| Family | Papers / projects to inspect | What to check |
| --- | --- | --- |
| Architecture search | [Meta Agent Search / ADAS (ICLR 2025)](https://arxiv.org/abs/2408.08435), [AFlow](https://arxiv.org/abs/2410.10762), [MASS](https://research.google/pubs/multi-agent-design-optimizing-agents-with-better-prompts-and-topologies/), [OFA-MAS](https://github.com/Shiy-Li/OFA-MAS), AgentSquare | Whether architecture/topology actually changes, tool creation scope, held-out transfer and code |
| Meta-learning and self-evolution | [HyperAgents](https://github.com/facebookresearch/HyperAgents), [Meta-Skill](https://github.com/qiancheng-apodex/MetaSkill-AI4AI), Meta-Harness, DAGO, MASPOB, GRASP alternatives | Learned designer vs nonparametric search; actual train/test unit |
| Requirements and intent | [SpecBench / Buddy](https://arxiv.org/abs/2606.20585), [R2ABench](https://arxiv.org/abs/2604.06683), agent specification/traceability research | Intent ambiguity, change supersession, architecture fidelity, human validation |
| Tools and harnesses | [JTPRO](https://aclanthology.org/2026.findings-acl.2017/), [AutoAgent](https://github.com/HKUDS/AutoAgent), [Agent Lightning](https://github.com/microsoft/agent-lightning), HarnessBank, self-healing harness | Exact edit surface and safety/evaluation controls |
| Other anti-overfitting | TRAS, RELAI-VCL, feedback curation, self-generated test-set contamination | Success-preservation vs real continual generalization |
| World models | Agent World Model, PathWise, predictive agent configuration models | Whether dynamics are learned or only final score surrogates, calibration and data requirements |

This queue is deliberately separate from the CHECKED ledger. Check titles/identifiers/release dates before copying claims into a paper.

## 3. Novelty claims rejected

- Automatic prompt improvement: APE, OPRO, ProTeGi, GEPA, PROSE, COMPASS.
- An AI that architects other agents: Meta Agent Search, Tressoir and related ADAS systems.
- Jointly modifying prompts and tool interfaces: JTPRO and PRISM.
- Bandit selection of harness modules: MESH-Harness and related work.
- Regression-gated continual improvement: GRASP, RELAI-VCL, RECAP-related methods.
- World-model/surrogate performance prediction as a generic idea: established in optimization; CHIVE already studies counterfactual prompt-edit effect prediction.
- Merely packaging these elements together: may create a useful tool, but algorithmic novelty is unproven.

## 4. Candidate distinct questions (unverified gaps)

1. **Intent vs incident vs supersession:** When new feedback arrives, can we distinguish an isolated failure from an intentional change to the target specification, under uncertainty, and demonstrate improvement over a simple LLM with tests?
2. **Cross-component causal regression:** Can controlled interventions predict effects of prompt/tool/topology revisions on downstream obligations more accurately than static dependencies and direct testing?
3. **Design-level longitudinal transfer:** Can improvements persist across many revisions and transfer to whole unseen application families, not merely held-out examples within one task family?
4. **Evaluator validity:** Can we identify and prevent revisions that improve apparent reward by modifying or exploiting the evaluator, tests, or compute budget?

Each becomes a research contribution only AFTER existing baselines fail and ablation shows why a proposed mechanism helps.

## 5. Next literature-audit steps

For each paper, record: exact task definition; editable artifact types; whether the search is trained or nonparametric; feedback signal; costs; source release/code state; train/val/test boundaries; number of sequential updates; whether intent is mutable; regression/transfer measurements; known caveats; and reproducibility. Use primary papers and source repositories. Perform backward/forward citation tracking on Tressoir, PRISM, RECAP, AHE, GRASP, CHIVE and MESH. Revisit this ledger before claiming novelty.
