# Glossary — AI Product Management

Definitions you will encounter across the certification. One line each; longer treatments live in the per-module glossaries and the Concepts Primer.

---

## A

**Agent.** A system that pursues a goal by reasoning, calling tools, observing results, and iterating. (M5)

**Agent Spectrum.** Tool → Assistant → Agent → Autonomous Agent. The autonomy continuum. (M5)

**Agentic memory.** State persisted across turns or sessions. Four flavours: short-term, long-term, episodic, semantic. (M5)

**Agent Workflow Spec (AWSpec).** The product spec for an agent: goal, trigger, tools, memory, pattern, stop conditions, handoffs, eval hooks. (M5)

**AI Evals Stack.** Three layers: user feedback, human evaluation, automated evaluation. Always all three. (M6)

**AI Iceberg.** The mental model that the UI is the tip; everything else (retrieval, tools, memory, guardrails, evals) is underwater. PMs spec the iceberg. (M4)

**AI PM Toolkit.** Prompt-to-prototype, LLM playground, no-code agent builder, eval/observability, repo + version control. (M1)

**AI PRD.** A traditional PRD plus three AI-specific sections: data corpus + retrieval, eval plan, failure modes + guardrails. (M3)

**AI Solution Decision Matrix.** A 5-axis pressure-test for AI bets: value clarity, technical feasibility, data availability, risk tolerance, strategic fit. (M2)

**AI Strategy One-Pager.** Seven-block one-page artifact justifying an AI bet to leadership. (M2)

**AI-UX Readiness Check.** Test for the three trust gaps (black-box, hallucination, control). (M4)

**Anatomy of a High-Quality Prompt.** Context + Task + Constraints + Output Format + (Examples). (M1)

**Async showcase.** This course's replacement for live group demos: post repo link + 3-minute Loom in `#ai-pm-cohort`; instructor responds in-thread. (M6)

**Autonomy levels.** Suggest → Draft → Execute → Operate. (M2)

## B

**Black-box gap.** User doesn't know *why* the AI decided. Closed with reasoning / citations / "show your work." (M4)

**Boring killer.** A feature that doesn't demo flashy but ladders cleanly to a real value frame and survives a 3x cost stress test. The opposite of a fake-good. (M2)

## C

**Chain-of-thought (CoT).** A prompting technique that instructs the model to reason step-by-step before answering. (M1)

**Context engineering.** Assembling the *data around* the prompt so the model has the right ground truth. PMs own this. (M3)

**Context window.** How many tokens a model can consider in one call. (Primer)

**Control gap.** User doesn't know how to steer or stop the AI. Closed with undo, edit, regenerate, "don't suggest this again." (M4)

## D

**Decision triangle, PM.** At each step of an agent flow: AI alone / AI + human / human alone. (M5)

**Deterministic system.** Same input → same output. (Primer)

**Drift.** When model output changes over time without code changes. (M6)

## E

**Embedding.** A vector representation of text used for similarity search in RAG. (M3)

**Episodic memory.** Memory of specific past events ("user said X yesterday"). (M5)

**Eval harness.** The infra that runs evals on a cadence: golden set, runner, scorer, dashboard. (M6)

**Execute (autonomy).** The agent acts on the world without per-action approval. (M2)

## F

**Failure mode.** A specific way an AI feature can fail. Spec these in your AI PRD. (M3)

**Fake-good.** A feature that demos well but doesn't ladder to a real value frame and dies under cost stress. (M2)

**Few-shot prompting.** Including 1–3 example input/output pairs in the prompt. (M1)

**Fine-tuning.** Adjusting model weights on your data. Last-resort optimisation. (M1)

**Four AI Value Propositions.** Cost reduction, revenue generation, risk mitigation, user delight. (M2)

## G

**Golden set / golden dataset.** A curated set of inputs with known-correct outputs, used as the canonical eval reference. (M6)

**Governance framework.** Compliance + safety + reliability + reputation. (M6)

**Guardrail.** A runtime check that blocks unsafe / out-of-scope behaviour. (M3, M6)

## H

**Hallucination.** A confident, plausible, but wrong output. (Primer)

**Hallucination gap.** The trust gap that arises because confident output may be wrong. Closed with confidence cues, citations, escape hatches. (M4)

**Handoff rules.** Explicit conditions under which the agent stops and hands back to the human. Lives in the AWSpec. (M5)

**Human-in-the-loop (HITL).** Workflow that requires human approval at a checkpoint. (M2, M5)

**Human evaluation rubric.** A structured grading guide with dimensions, scales, anchors, disagreement protocol, and sampling cadence. (M6)

**Hyperparameters.** Model-runtime settings — temperature, top-p, max tokens, etc. (M1)

## I

**Individual Exercise.** This course's only exercise type. No group breakouts. Every exercise has self-review + AI-review + async share. (course-wide)

**Intelligence tax.** Extra latency or cognitive load the user must endure for AI value. (M4)

**Intent-driven UI.** UI that infers what the user wants and acts; the opposite of command-driven UI. (M4)

**Invisible by design.** AI-native UX default — anticipates intent, acts at the right moment, never sits at a chat box. (M4)

## J

**Jobs × Risk × Autonomy.** The strategy lens for choosing autonomy levels. (M2)

**Juno PM.** The AI Associate PM you build across the course. Lives inside Slack/Notion/Jira, handles synthesise / draft / prioritise pillars. (course-wide)

## L

**Langflow.** A no-code agent builder. Used in the optional post-class lab for M5. (M5)

**LLM.** Large Language Model. (Primer)

**LLM-as-a-judge.** Using a model to evaluate the output of another model against a rubric. (M6)

**Long-term memory.** State persisted across sessions. (M5)

**Lovable.** Prompt-to-prototype tool used in M1 to create the Juno UI. (M1)

## M

**Memory poisoning.** When bad data gets persisted as fact in agentic memory. (M5)

## N

**Non-deterministic system.** Same input → variable output. Every modern LLM. (Primer)

## O

**One-pager, AI Strategy.** See *AI Strategy One-Pager*.

**Operate (autonomy).** Highest autonomy level — the agent operates over long horizons without check-ins. (M2)

**Optimization Decision Framework.** Prompt → RAG → Fine-tune. Cheapest first. (M1)

## P

**Planner-Executor.** Multi-agent pattern where one agent plans steps and one or many executors run them. (M5)

**PM Decision Triangle.** AI alone / AI + human / human alone — at every step of an agent flow. (M5)

**Prompt engineering.** Crafting the text instructions to the model. (M1)

**Prompting Strategy Matrix.** Zero-shot, few-shot, chain-of-thought, system-prompt+role. (M1)

## R

**RAG (Retrieval-Augmented Generation).** Retrieve relevant data before generation; inject into prompt. Reduces hallucination, adds cost/latency. (M3)

**RAG trade-offs.** Cost, speed, accuracy. Right context at the right time beats more context. (M3)

**ReAct.** *Reason → Act → Observe → loop.* Single-agent reasoning pattern. (M5)

**Red lines.** What blocks shipping — explicit in the PM execution plan. (M6)

**Responsible AI.** The strategic guardrails — bias, transparency, accountability, safety. (M2)

**RocketShip.** The fictional B2B SaaS company in the course scenario. Suffering "Signal Collapse." (course-wide)

## S

**Self-review checklist.** The 3–5 bullets you verify against your own artifact before moving on. (course-wide)

**Semantic memory.** General knowledge memory (domain facts, org context). (M5)

**Shadow AI.** Unsanctioned AI tools used inside the org. (M6 governance)

**Short-term memory.** State within one task / one turn. (M5)

**Signal Collapse.** The state RocketShip is in — too much data, no headcount, the PM is the bottleneck. (course-wide)

**Strategic Scorecard.** See *AI Solution Decision Matrix*.

**Suggest (autonomy).** Lowest autonomy level — the AI proposes, the human decides. (M2)

**System prompt.** The persistent instruction that sets the AI's persona, scope, and guardrails. (M1)

## T

**Three-Layer Model.** Strategy / Mechanic / Implementation. (M2)

**Three Levers to Optimise.** Model, Data, Architecture. (M6)

**Token.** The unit a language model reads/writes. Roughly 0.75 words. (Primer)

**Tool (in agent context).** A callable function the agent can invoke (API, DB query, file write). (M5)

**Trigger.** The condition that activates an agent workflow. (M5)

**Trust gaps.** Black-box, hallucination, control. (M4)

## U

**User feedback (eval layer).** Thumbs, regenerate, abandonment — highest volume, lowest fidelity. (M6)

## V

**Vibe check.** Eyeballing a few prompts and calling it good. Fails in production. (M6)

**Value clarity.** The first axis of the AI Solution Decision Matrix — does it ladder to a value frame? (M2)

## Z

**Zero-shot prompting.** No examples; instruction-only. (M1)
