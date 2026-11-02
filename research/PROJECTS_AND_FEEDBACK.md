# Practical agent-design software and external feedback

**Status:** catalogue of previously investigated leads; NOT an endorsement or production-readiness certification. One GitHub design skill was checked again on 2026-11-02; adoption, issue status and community sentiment for other entries should be independently rechecked before publication.

## 1. Differentiate design systems from implementation frameworks

The user wants a tool that *helps discover* the appropriate architecture, prompts, tools and behavior through conversation and iteration, **not** an SDK that assumes the structure is already known.

| Project | Relevance to the real requirement | Caution / evidence status |
| --- | --- | --- |
| [GitHub awesome-copilot: agent-architecture skill](https://github.com/github/awesome-copilot/blob/main/skills/agent-architecture/SKILL.md) | Requirements discovery, choose simplest viable architecture, audit/diagnose design errors, produce design and verification plan. | Checked 2026-11-02. Explicitly excludes implementation; documented skill behavior does not prove generated-design quality. |
| [BMad Builder](https://github.com/bmad-code-org/bmad-builder) | Conversational construction of agents, workflows and prompt artifacts; structured quality checks. | Previously investigated. Verify stable vs preview releases, actual output quality and regression testing independently. |
| [HKUDS AutoAgent](https://github.com/HKUDS/AutoAgent) | Natural-language agent/tool/workflow editors and runnable generated tools. | Previously investigated. Reports of editor failures and isolation issues require current issue/status check; do not assume production readiness. |
| [Microsoft Copilot Studio architect agent](https://github.com/microsoft/copilot-studio-plugin/blob/main/agents/copilot-studio-architect.md) | Decides between instructions, tools, skills and deterministic logic and generates platform configuration. | Platform-specific; generated artifacts are not evidence of broad generalization. |
| [Alireza's Claude skills](https://github.com/alirezarezvani/claude-skills) | Modular agent designer, workflow, tool-schema and regression-evaluation skills. | Skills are not verified unified end-to-end system; check independent use. |
| [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) | Broader requirements/planning workflow; unreleased Toolsmith effort previously discussed. | Keep stable builder vs unreleased features distinct. |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) and [GitHub Spec Kit](https://github.com/github/spec-kit) | Specification/change management and implementation planning, useful supporting infrastructure. | Not agentic architecture researchers or automatic prompt/tool designers out of the box. |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | Multi-role planning and software artifact generation from broad requests. | Software-building focus; not evidence of preservation across agent-design revisions. |

**Supporting infrastructure, not the sought product:** [LangGraph](https://github.com/langchain-ai/langgraph) (execution), [DSPy](https://github.com/stanfordnlp/dspy) and [GEPA](https://github.com/gepa-ai/gepa) (program/prompt optimization), [Opik](https://github.com/comet-ml/opik), [Promptfoo](https://github.com/promptfoo/promptfoo), [Langfuse](https://github.com/langfuse/langfuse) (tracing/evaluations). These can be components of a designer but are not themselves evidence of an autonomous systems architect.

## 2. Developer experience themes (qualitative leads, NOT survey estimates)

Earlier conversations surfaced community discussions about BMad-like workflows and GitHub issue reports about AutoAgent/BMad. Common themes were:
- **Positive:** guided requirements discovery, clearer project structure, more deliberate architecture choices.
- **Negative:** excessive process and token costs, slow small changes, generated tests that share the implementation's assumptions, incomplete changes, brittle tool generation and configuration.
- **Research implication:** a design tool needs independent acceptance criteria, no-change/clarification actions, and measurable maintenance quality, not just well-structured output files.

Examples to recheck before quoting in a paper:
- [Reddit: BMad discussion](https://www.reddit.com/r/ClaudeAI/comments/1mmn41s/)
- [Reddit: experience building an entire project with BMad](https://www.reddit.com/r/BMAD_Method/comments/1tn2c6j/)
- [Reddit: compare BMAD, GSD, Superpowers](https://www.reddit.com/r/ClaudeCode/comments/1rk537t/)
- [AutoAgent issue tracker](https://github.com/HKUDS/AutoAgent/issues)
- [BMad Builder issue tracker](https://github.com/bmad-code-org/bmad-builder/issues)

These are anecdotal and may include outdated fixed bugs, self-selection, or unclear project/version labels. No verified usage prevalence, reliability rate, or broad adoption rate is established here.

## 3. Product quality verification to do later

For each candidate, independently install a pinned release and run the SAME agent-design brief and sequential change requests. Inspect generated prompts, tool contracts, architecture rationale, runnable validity, revision preservation, permission boundaries, and cost. Record exact commit/version, setup friction, time, and failures. Do not substitute stars, demos or a well-known organization logo for this trial.

**Present working conclusion:** there are genuine conversational designer and artifact-generator precedents, but this audit has not established that one automatically maintains fully general behavior over successive heterogeneous agent design revisions.
