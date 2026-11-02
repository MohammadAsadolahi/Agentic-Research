# Emerging research fields in agentic AI (field-first scan, November 2, 2026)

**Scope:** distinguish developing research *fields* from specific paper ideas. The goal is to select a broad scientific direction before searching for a contribution. This is a targeted exploration of public recent arXiv primary sources, **not** a systematic census, bibliometric count, novelty guarantee or funding/acceptance probability. Scores below are qualitative investigator judgments, not statistics. "Emerging" refers to an emerging agentic instantiation of a sometimes decades-old topic (causal inference, continual learning, governance, institutions, etc.).

## Nine main fields (plus a boundary field)

| Field in LLM/tool-using agents | Core research object | Maturity of the agent-specific subfield | Researcher competition (rough, not counted) | Feasibility with open-source environments |
| --- | --- | --- | --- | --- |
| Causal world models & intervention learning | Learning action effects, preconditions and counterfactuals from tool responses | Developing | Medium; direct algorithmic competitors | High |
| Continual skill/experience learning | Acquiring new skills while preserving older ones under nonstationary task streams | Rapidly growing | High | High |
| Open-ended goal/skill discovery | Choosing new problems and building reusable skills without fixed task curricula | Rapidly growing | Medium–high | Medium |
| Social learning and collective improvement | Transfer of skills/knowledge between agents pursuing possibly different objectives | Early developing | Medium | Medium–high |
| Collective epistemic reliability | How errors, evidence, dissent, and beliefs propagate through agent populations | Growing | Medium–high | High |
| Persistent agent identity and long-term autonomy | Continuity of goals, authority, knowledge and behavior across runtime/model/harness replacement | Early developing | Medium | Medium–high |
| Autonomous goal regulation | How agents decide what to pursue, suspend, stop and reprioritize under uncertainty | Developing; foundation is old | Medium | High |
| Evolutionary safety of self-modifying agents | Safety properties across successive self-modifications and evaluator changes | Rapidly growing | Medium–high | Medium |
| Agent societies/institutions | Endogenous rules, reputation, reciprocity, role formation and governance | Early developing | Medium | Medium |
| Longitudinal human–agent co-adaptation (boundary field) | Reciprocal changes to user and agent policies over weeks/months | Early developing at agentic scale | Medium | Lower without human participants |

### Why these fields qualify as *emerging*, with primary evidence

**1. Causal action/world models.** Tool agents increasingly operate across modular services with interacting state transitions. Distinguish observational pattern prediction from predictions under interventions. [When Do Causal World Models Help Modular LLM Agents](https://arxiv.org/abs/2610.00012) already develops a relevant causal framework and theory. **It is not an empty area; a new mechanism would require beating causal planning baselines.** Good science because outcomes can be independently observed in real tool environments.

**2. Continual nonparametric agent learning.** Experience can update prompt, skill files, controller code or memory without base-model training. [Are Self-Evolving Agents Continual Learners?](https://arxiv.org/abs/2610.25858) finds stability/plasticity tradeoffs, cross-task interference and memory retrieval collisions under task-stream drift. [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) proves the broad area is already crowded. **Interesting open phenomena are inside the field, not a generic first-to-do-continual-learning claim.**

**3. Open-ended curricula and skill formation.** Agents choose useful learning goals and build reusable skills, rather than merely execute externally selected tasks. [CODE-SHARP](https://arxiv.org/abs/2602.10085) discovers/evolves hierarchical skill rewards; [SESA](https://arxiv.org/abs/2607.29468) co-evolves problem generation and skill memory. It is an active, more crowded area than a superficial query might suggest.

**4. Social learning among agents.** Key research question: can population-level information sharing create useful new knowledge beyond independent agent work, *at matched inference cost*? [From Solo to Social Learning](https://arxiv.org/abs/2609.38516) studies recursive social improvement and finds that peer copying often improves efficiency without improving peak capability over independent learners. [ShareMem](https://arxiv.org/abs/2609.32511) studies cross-user experience transfer with preference interference. Distinguish same-objective team workflows from agents learning through social information over time.

**5. Distributed epistemics and collective evidence reliability.** Agents share evidence that may be uncertain or wrong, even when all agents are benign. [Misinformation Propagation in Benign Multi-Agent Systems](https://arxiv.org/abs/2606.16710) shows peer contamination and nuanced effects of consensus vs voting. [When Truth Is Distributed](https://arxiv.org/abs/2608.03421) studies false testimony adopted and propagated after a deceiver exits. **Do not rebrand debate or fact-checking as new.** The field studies population-level knowledge formation and evidence lineage.

**6. Durable/persistent agency and identity.** An agent that runs across hosts, model/harness changes, and task boundaries creates identity, memory, workflow and attribution issues. [Runtime-Independent Persistent Agents](https://arxiv.org/abs/2609.00546) gives continuity substrate and protocol; [AstronOS](https://arxiv.org/abs/2608.16381) studies multi-session state/handoff; [AI Identity: Standards, Gaps, and Research Directions](https://arxiv.org/abs/2604.23280) diagnoses lifecycle risks. This is **not** simply storing a chat history; work must separate behavioral continuity from mechanical state restoration.

**7. Autonomous goal regulation.** Study stopping, persistence, abandonment, resumption and goal conflict in agents executing lengthy tasks. [Push Your Agent](https://arxiv.org/abs/2605.23574) finds persistent goal-completion failures; [Artificial Id](https://arxiv.org/abs/2609.11911) examines autonomous persistence drive. **Classical decision theory, hierarchical RL, and rational metareasoning already cover many general questions.** Emerging part is empirically grounded ongoing autonomy with real tools and changing feedback.

**8. Evolutionary safety and verification.** If an agent updates its own policies, memory, heuristics or evaluator, errors can persist and selection feedback may become unreliable. [Evolutionary Safety](https://arxiv.org/abs/2609.31186) formalizes a taxonomy; [Self-Authored Verification Is Unreliable](https://arxiv.org/abs/2607.24300) directly provides an exogenous verifier protocol; [VeriFine](https://arxiv.org/abs/2610.08761) studies policy-curriculum-judge co-evolution. **Hard novelty baseline:** external sealed acceptance is known; "verify changes" is not new.

**9. Agent populations, institutions and emergent governance.** Long-lived multi-agent systems can develop cooperative norms, exclusionary coalitions, reputation, and self-governance. [SCARCE](https://arxiv.org/abs/2610.21029) observes norms around sharing compute in coding tasks; [Emergence World](https://arxiv.org/abs/2606.08367) provides prolonged simulation of agent populations. **Do not call first agent societies, first negotiation, or first institutional emergence.** Distinguish what is actually measured in simulation from external-world behavior.

**10. Human–agent co-adaptation.** Study how an assistant's autonomy changes human decision habits and how human oversight/preferences reshape agents across repeated sessions. A month-long human study [Does My Chatbot Have an Agenda?](https://arxiv.org/abs/2601.22452) analyzes co-constructed agency; accessibility and user-aligned ongoing assistance can be adjacent. Meaningful claims often require IRB/consent, participants and HCI expertise; unsuitable as a quick purely synthetic agent benchmark.

## Do not mistake established parent disciplines for new fields

Causal inference, reinforcement learning, continual learning, multi-agent game theory, distributed systems, trust, and sociology are old. What has become research-active in 2025–26 is their **agent-specific instantiation** with LLM-based model decisions, stateful tools, self-edited scaffolds, and persistent cross-task effects.

## Field-first shortlist for this project

**Tier A: strong science + independent experiments without specialized hardware**
1. **Causal action learning in digital tool environments.** Tests can compare observed next states and counterfactual/action predictions; real model-driven agents feasible. Competing causal world-model methods exist.
2. **Continual skill learning under distribution shift.** Natural repeated-task experiments and measurable regressions; field comparatively crowded so must find a *much narrower* scientific question later.
3. **Collective epistemic reliability.** Controllable information asymmetries, independent truth oracles, repeated agent interactions. Already has misinformation benchmarks, requiring a substantive new mechanism or scope.

**Tier B: high scientific ambition but more difficult evaluation**
4. **Social learning of reusable knowledge across independent agents.** Test whether populations gain net useful skill at fixed tokens/time and avoid homogenized search.
5. **Long-lived autonomy and goal governance.** Challenge: meaningful long-term agency rather than restart/persistence engineering; require significant time/deployed environments.
6. **Agent institution formation.** Need causal experimental design to distinguish truly endogenous rules from prompt-induced roleplay.

**Tier C: high interest but special constraints or direct strong incumbents**
7. Open-ended curricula (strong active algorithm competition).
8. Evolutionary safety (external acceptance and validator separation already studied; computationally heavy).
9. Longitudinal human–agent coadaptation (participants and ethical oversight).
10. Generic self-evolving "agent becomes smarter" (crowded; insufficient conceptual specificity).

## Selection criteria for next research turn

Do **not** invent a research title now. A credible field must satisfy:
- The primary phenomenon is agentic (learned decision-making, self-directed action, multiple interactors, persistence across tasks).
- There is a measurable, independently verifiable outcome rather than solely LLM-as-a-judge scores.
- Experimental settings can be reproduced with actual agents and nonleaky holdouts.
- The field is substantial enough to matter and not just an API edge case.
- Strong nearest-method competitors can be run or reconstructed without changing the threat model.
- Any "less crowded" claim is provisional until a broad systematic literature search.

**Recommended next discussion:** choose 2–3 *fields* for structured mapping of taxonomy, key scientific questions, evaluation infrastructure and feasibility. Do not prematurely commit to a paper proposal.

## Key epistemic cautions

This is a targeted scan, not a systematic review. Maturity and relative-crowdedness labels are subjective, and an emerging research field can already host dozens or hundreds of recent papers. Some arXiv records are preprints, and their claims have not all been independently replicated. References are evidence that these fields are active, not evidence that any specific question is genuinely novel. No model experiments were run for this report.
