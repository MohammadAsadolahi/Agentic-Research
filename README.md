# Agentic Research

> **Research status: discovery and hypothesis validation — November 2, 2026. No algorithmic novelty claim or experimental improvement is established.**

This repository tracks a research investigation into **AI-assisted design and continual maintenance of agentic systems**. The intended tool is an **AI systems architect**, not another orchestration framework: it should help a developer discover requirements, decide whether to use one or many agents, design prompts and tool contracts, choose workflow boundaries, and make evidence-backed revisions without overfitting to the latest reported failure.

## Start here

1. **[Current research state](research/RESEARCH_STATE.md)** — exact problem, what we have learned, decisions, hypotheses, uncertainties, and next actions.
2. **[Prior-art and novelty audit](research/PRIOR_ART.md)** — closest verified papers, overlaps, sources, and claims we must NOT make.
3. **[Experimental roadmap](research/EXPERIMENT_PLAN.md)** — falsification-first study, baseline conditions, metrics, data splits, and stop rules.
4. **[Practical systems and user feedback](research/PROJECTS_AND_FEEDBACK.md)** — existing agent architects, supporting tools, and evidence-quality caveats.

## Current conclusions

- The original developer pain point is credible: changing a prompt or tool specification to fix a local failure can damage behavior elsewhere. But its frequency, causes, and remedies have **not yet been measured by us**.
- Automatic prompt optimization, RL-trained meta-prompters, architecture/harness search, specification-based designs, counterfactual prompt edits, and regression gates **all have substantial prior art**.
- A general-purpose conversational architect with rigorously demonstrated long-term behavior preservation has **not been established by our scoped search**. That is an observation about evidence, **not proof of absence**.
- **Do not start with an RL model or world model.** First test whether explicit requirements, proper diagnosis, and conventional regression tests outperform ordinary editing. Introduce learning only if a measured residual problem justifies it.
- The nearest credible opportunities are (a) intent-aware adaptation to evolving requirements, (b) cross-component regression diagnosis/prediction, and (c) careful measurement of genuine generalization over sequential changes.

## Next research milestone

Run a small, reproducible **failure-mechanism study** comparing direct LLM edits, edits with regression tests, edits with independent structured specifications, and edits with change-impact reasoning. Hold out whole application families and keep acceptance tests independent of the editor. See the [experiment plan](research/EXPERIMENT_PLAN.md).

## Evidence policy

Distinguish **published and checked**, **preprint and checked**, **repository/documentation inspected**, **user report**, **working hypothesis**, and **unverified**. Cite primary sources for concrete claims. Do not infer production adoption from stars, untested demos, or organization names. Do not describe a proposed evaluation as completed work.

**Maintenance rule:** Update the state, prior-art log, experiment status, and dated decision record whenever a new paper or result changes the novelty assessment.
