# Concepts Primer — AI Product Management

A 15-minute pre-read for the certification. Skim before Module 1. Bookmark for the rest of the course. This is the assumed vocabulary; you do not need to memorise it — you need to recognise it.

If you have already taken AIPC or the equivalent, this is mostly review.

---

## The shift in one paragraph

Traditional product management assumes a deterministic system: given the same input, you get the same output. AI products are **non-deterministic** — given the same input, the output varies, can be wrong, can drift, and can hallucinate. Every PM craft you know (specs, UX, QA, launch) bends around that one fact. This course is the bend.

---

## The Juno scenario (you will see this in every module)

You are the AI PM at **RocketShip** (B2B SaaS, Enterprise Data Teams). The company has hit "Signal Collapse" — too much data, too many P0s, no headcount. You are building **Juno PM**, an AI Associate PM, that handles three pillars: *synthesize insights, draft specs, prioritize risks.* Juno lives inside Slack, Notion, and Jira — not as a standalone chat tab. Every module's exercise commits a real artifact to your `juno-pm/` repo fork.

---

## Core concepts you will use across all six modules

### 1. Deterministic vs. non-deterministic systems

- **Deterministic** — same input → same output. Example: a SQL query.
- **Non-deterministic** — same input → variable output. Example: every modern LLM.

### 2. Tokens and context windows

- **Token** — the unit a language model reads and writes. Roughly 0.75 words of English.
- **Context window** — how many tokens a model can consider in one call. Bigger windows ≠ better outputs; they make architecture decisions (RAG, summarisation, chunking) more flexible.

### 3. The four ways AI creates real value (the value frame)

- **Cost reduction** — replace work that currently costs humans.
- **Revenue generation** — create new product surfaces that drive willingness to pay.
- **Risk mitigation** — catch what humans miss (compliance, fraud, escalation).
- **User delight** — anticipate intent, remove friction, surprise positively.

A feature that doesn't ladder cleanly to one of these is a *fake-good* — flashy demo, no business case.

### 4. The Three-Layer Model (M2)

- **Strategy layer** — *which* bet, *why now*, what value frame.
- **Mechanic layer** — *what* the product actually does (the feature mechanic).
- **Implementation layer** — *how* it's built (prompt vs. RAG vs. fine-tune vs. agent).

PMs own all three, but spend most of their language at the top two.

### 5. Jobs × Risk × Autonomy (M2)

For any AI feature, the autonomy you grant is a function of:
- **Job** — what task is the AI doing?
- **Risk** — what's the cost of a wrong output? (reputational, financial, regulatory)
- **Autonomy** — how independently can it act? (suggest → draft → execute)

Higher autonomy + higher risk = explicit handoff rules required (see M5 PM Decision Triangle).

### 6. Prompt engineering vs. context engineering (M3)

- **Prompt engineering** — what you write into the model.
- **Context engineering** — what data you assemble *around* the prompt so the model has the right ground truth.

PMs own context engineering. Engineers own the retrieval mechanics; PMs own *what* should be retrieved and *why*.

### 7. RAG (Retrieval-Augmented Generation) (M3)

A pattern where, before the model generates, you retrieve relevant data from a known corpus and inject it into the prompt. Reduces hallucination, grounds outputs in your data, but adds cost, latency, and architectural complexity.

The three RAG trade-offs:
- **Cost** — embedding, storage, retrieval are not free.
- **Speed** — every retrieval step adds latency.
- **Accuracy** — the right context at the right time beats more context every time.

### 8. The AI Iceberg (M4)

What the user sees (the UI) is the tip. Beneath the surface: prompt assembly, retrieval, tool calls, memory writes, eval logging, guardrails, fallback paths. PMs design the tip; PMs *spec* the iceberg.

### 9. The three AI-UX trust gaps (M4)

- **Black-box gap** — user doesn't know how the AI decided.
- **Hallucination gap** — output looks confident, but might be wrong.
- **Control gap** — user doesn't know how to steer or stop the AI.

All three must be closed for a probabilistic system to feel safe.

### 10. Agents and the agent spectrum (M5)

- **Tool** — does one thing on request (a function call).
- **Assistant** — chats, recommends, drafts. No execution.
- **Agent** — plans, calls tools, observes results, iterates. Can execute.
- **Autonomous agent** — operates over long horizons without check-ins.

Most "AI agents" you ship will live mid-spectrum and require explicit handoff rules.

### 11. ReAct and Planner-Executor (M5)

- **ReAct** — *Reason → Act → Observe → loop.* Single-agent reasoning pattern.
- **Planner-Executor** — one agent plans the steps, another (or many) executes them. Multi-agent pattern.

You pick a pattern in your Agent Workflow Spec.

### 12. Agentic memory (M5)

- **Short-term** — within one task / one turn.
- **Long-term** — across sessions; the agent remembers the user.
- **Episodic** — specific past events (this user said X yesterday).
- **Semantic** — general knowledge (RocketShip is a B2B SaaS).

Memory choices shape privacy, cost, and behaviour.

### 13. The AI Evals Stack (M6)

Three layers, in order of fidelity ascending and volume descending:

1. **User feedback** — thumbs, regenerate, abandonment. Highest volume, lowest fidelity.
2. **Human evaluation** — graders applying a rubric. Mid volume, high fidelity.
3. **Automated evals** — LLM-as-a-judge, regression suites, golden datasets. Highest volume, mid fidelity.

You always need all three. The 95% accuracy trap (M6): the last 5% is where the production risk lives.

### 14. The three optimisation levers (M6)

When AI performance is below bar, you have three knobs:
- **Model** — swap, upgrade, or fine-tune.
- **Data** — improve the corpus, clean inputs, expand context.
- **Architecture** — change the pattern (add RAG, decompose into agents, add guardrails).

In that order of cost-to-try (model ≪ data ≪ architecture).

---

## Reading list (optional, ordered by relevance)

1. **Anthropic — Building effective agents.** Best primer on patterns and pitfalls.
2. **OpenAI — Prompt engineering guide.** The reference.
3. **Eugene Yan — *Patterns for building LLM systems.*** Engineering view; PMs benefit.
4. **Lenny's Newsletter — interviews with AI PMs at Notion, Linear, Intercom.** Field reports.
5. **Hamel Husain — *Your AI product needs evals.*** The blog post the M6 module is built around.

You do not need to read these to take the course. They give you ammo for the AI-review prompts.

---

## Tools you'll touch in this course

- **Lovable** — prompt-to-prototype tool used in M1. Free tier works.
- **ChatGPT** / **Claude** / **Cursor** — used for AI-review prompts in every module.
- **GitHub** — your `juno-pm/` repo lives here. You'll fork `juno-project-template/` at the start of M1.
- **Langflow** (optional, M5 post-class) — no-code agent builder. Free tier requires an OpenAI API key.

---

## Format reminder

This course is **100% individual**. No group breakouts. No team deliverables. Every exercise is solo, with:

1. A **self-review checklist** to verify your artifact.
2. An **AI-review prompt** to paste into an LLM for critique.
3. An **async share** — commit to your fork, post in `#ai-pm-cohort`, instructor responds in-thread.
