# Frameworks Reference Card — AI Product Management

One-page summary of every framework introduced across the six modules. Use it as a lookup during exercises, a revision aid before the certification, and a mental checklist after the course.

---

## M1 — Drive AI-First Execution with Prompting

### Anatomy of a High-Quality Prompt
Five elements every production prompt should declare:

1. **Context** — who the AI is, what system it lives in, what it knows.
2. **Task** — the explicit instruction (verb-first).
3. **Constraints** — must-not-do, format requirements, scope boundaries.
4. **Output format** — schema, length, structure (markdown, JSON, table).
5. **Examples** (few-shot, when useful) — 1–3 ideal input/output pairs.

> Use it as: a checklist before you ship any system prompt. If any element is missing, your output will drift.

### The PM's AI Toolkit
Five tool categories every AI PM should have one of in their bookmarks:

- **Prompt-to-prototype** (e.g., Lovable, v0, Cursor)
- **LLM playground** (e.g., OpenAI Playground, Anthropic Console)
- **No-code agent builder** (e.g., Langflow, n8n)
- **Eval / observability** (e.g., LangSmith, Phoenix, Braintrust)
- **Repo + version control** (GitHub — your `juno-pm/` lives here)

### Prompting Strategy Matrix
Four core techniques and when to use each:

| Technique | Use when |
|---|---|
| **Zero-shot** | Simple instruction, model already knows the domain |
| **Few-shot** | You need a specific format or style; show 1–3 examples |
| **Chain-of-thought** | Multi-step reasoning required |
| **System prompt + role** | Persona, persistent guardrails, organisation context |

### The Optimization Decision Framework
Prompt vs. RAG vs. fine-tune — pick the cheapest answer that works:

1. **Prompt** — fastest, cheapest, no infra. Try first.
2. **RAG** — when grounding in your data matters. (M3 lives here.)
3. **Fine-tune** — when style/format/behaviour matters more than fact retrieval. Last resort.

---

## M2 — Validate AI Opportunities and Technical Feasibility

### Fake-Good vs. Boring Killer
A two-question filter for every AI feature pitch:

- *Does it ladder to a real value frame?* (cost, revenue, risk, delight)
- *Would you defend it under a 3x cost stress test?*

If both yes, it's a boring killer. If either no, it's a fake-good.

### Four AI Value Propositions
- **Cost reduction** — replace human labour.
- **Revenue generation** — new product surface, new willingness to pay.
- **Risk mitigation** — catch what humans miss.
- **User delight** — anticipate intent, reduce friction.

### The Three-Layer Model
- **Strategy** — bet + value frame + why now.
- **Mechanic** — product behaviour, user-facing feature.
- **Implementation** — prompt / RAG / fine-tune / agent.

### Jobs × Risk × Autonomy
The strategy lens for choosing autonomy:

- **Job** — what task.
- **Risk** — cost-of-wrong (reputation, regulation, revenue).
- **Autonomy** — suggest → draft → execute → operate.

Plot on a 2x2: high-risk jobs cap at *draft*; low-risk jobs can earn *execute* or *operate*.

### AI Solution Decision Matrix
A pressure-test on every proposed AI bet, scored 1–5 across five axes:

| Axis | Question |
|---|---|
| **Value clarity** | Does it ladder to a value frame? |
| **Technical feasibility** | Can current models actually do this well enough? |
| **Data availability** | Do we have / can we get the data corpus? |
| **Risk tolerance** | What's the cost of being wrong, and can we tolerate it? |
| **Strategic fit** | Does this earn company oxygen vs. other priorities? |

A bet that scores <3 average doesn't ship. A bet that scores 4+ on all five is a *boring killer*.

### AI Strategy One-Pager (anatomy)
A single page with seven blocks:

1. **The bet** — one sentence, the value frame it laddes to.
2. **The user / job** — who and what.
3. **The mechanic** — what the product does.
4. **The autonomy** — suggest / draft / execute / operate.
5. **The technical approach** — prompt / RAG / fine-tune / agent.
6. **The risk + guardrail** — what could go wrong, how you block it.
7. **The success metric** — how you'll know it works.

---

## M3 — Improve AI Product Requirements with RAG Architecture

### Prompt vs. Context Engineering
- **Prompt engineering** — words to the model.
- **Context engineering** — data assembled *around* the prompt. PMs own this.

### The RAG Process
1. **Index** — chunk your corpus, embed, store.
2. **Retrieve** — at runtime, fetch relevant chunks.
3. **Augment** — inject into the prompt.
4. **Generate** — model responds, grounded.

### The Three Key RAG Trade-offs
- **Cost** — embedding + storage + retrieval is not free.
- **Speed** — every retrieval step adds latency.
- **Accuracy** — *right context at the right time*, not more context.

### Architecture Decision Factors
- **Data freshness** — how stale can context be?
- **Corpus size** — fits in context window vs. must be retrieved?
- **Query latency budget** — how fast must this return?
- **Update cadence** — read-heavy vs. write-heavy?
- **Privacy / tenancy** — multi-tenant or per-user corpus?

### What's New in an AI PRD (vs. a traditional PRD)
A traditional PRD adds three sections for AI:

- **Data corpus + retrieval strategy** — what data, how indexed, how retrieved.
- **Eval plan** — golden set, success bar, regression cadence.
- **Failure modes + guardrails** — what can go wrong, what blocks it.

---

## M4 — Design AI-Native User Experiences

### Invisible by Design
The default for AI-native UX. The system anticipates intent and acts at the right moment instead of waiting at a chat box. *Chat-in-a-tab is the worst possible default.*

### Mapping Value to UX Treatment
| Value frame | UX treatment |
|---|---|
| Cost reduction | Background automation with audit trail |
| Revenue generation | Inline assist at the moment of decision |
| Risk mitigation | Proactive flag + reason, with one-click action |
| User delight | Anticipatory suggestion, dismissible without friction |

### The AI Iceberg
What the user sees (tip) vs. what runs underneath (everything else: prompt assembly, retrieval, tools, memory, eval, guardrails, fallback). PMs spec the iceberg.

### AI User Flow (the seven nodes)
1. **Trigger** — what initiates the flow.
2. **Capture** — what context the system gathers.
3. **Retrieve** — what data is pulled in.
4. **Reason** — what the model decides.
5. **Act** — what happens in the world (send / write / call).
6. **Surface** — what the user sees.
7. **Confirm / Correct** — how the user steers, accepts, or overrides.

### The AI-UX Readiness Check (the three trust gaps)
| Gap | Question | Mitigation |
|---|---|---|
| Black-box | Can the user see *why*? | Reasoning / citations / "show your work" |
| Hallucination | Could this confidently be wrong? | Confidence cues, source links, escape hatches |
| Control | Can the user steer or stop? | Undo, edit, regenerate, "don't suggest this again" |

### The Intelligence Tax
Extra latency or cognitive load the user must endure for AI value. Spec it down; never let it grow without a value-frame justification.

---

## M5 — Deploy Agentic Systems and Workflows

### The Agent Spectrum
Tool → Assistant → Agent → Autonomous Agent. Pick the lowest level that delivers the job. Higher levels need explicit handoff rules.

### Key Traits of Agency
- **Goals** — does it pursue a goal, not just respond?
- **Tool use** — can it call functions on the world?
- **Memory** — does state persist across turns / sessions?
- **Iteration** — does it observe results and re-plan?

### ReAct Loop
*Reason → Act → Observe → Reason → Act…* until the goal is met or a stop condition fires. Single-agent pattern.

### Planner-Executor Pattern
One agent decomposes the task into steps; one or many executors run them; planner re-plans on failure. Multi-agent pattern.

### Agentic Memory Types
| Type | Lifetime | Use for |
|---|---|---|
| Short-term | Within one task | Tool results, intermediate reasoning |
| Long-term | Across sessions | User preferences, learned facts |
| Episodic | Specific past events | "Last week the user said X" |
| Semantic | General knowledge | Org context, domain facts |

### Common Failure Modes
- **Hallucinated tool calls** — the agent invents an API.
- **Memory poisoning** — bad data persisted as fact.
- **Runaway loops** — no stop condition; cost explosion.
- **Silent handoff failure** — the agent should have escalated and didn't.
- **Drift across sessions** — long-term memory pulls behaviour off-spec.

### The PM's Agent Control Panel
The levers a PM specs and watches:
- **Triggers** — when does the agent activate?
- **Tools** — what can it call?
- **Memory scope** — what does it remember, for how long?
- **Stop conditions** — when does it hand back / shut down?
- **Observability** — logs, traces, eval surface.

### Agent Workflow Spec (AWSpec) — anatomy
The deliverable for M5:

1. **Goal** — one sentence.
2. **Trigger** — exact condition.
3. **Inputs** — required context.
4. **Tools available** — explicit list, with each tool's scope.
5. **Memory** — what's stored, where, for how long.
6. **Pattern** — ReAct or Planner-Executor (+ why).
7. **Stop conditions** — success, failure, escalation, timeout.
8. **Handoff rules** — when does Juno hand back to the PM?
9. **Eval hooks** — what gets logged for the M6 eval stack.

### The PM Decision Triangle
At every step of an agent workflow, the PM decides:
- **AI alone** — autonomy: full execute.
- **AI + human checkpoint** — draft + approve.
- **Human alone** — agent declines, escalates.

The triangle is the *boundary contract* between PM and agent.

---

## M6 — Measure AI Quality with Evals and Guardrails

### Why Vibe Checks Fail
A handful of "looks great" prompts is not a quality bar. You need a repeatable harness, a golden set, and a regression cadence.

### The 95% Accuracy Trap
The last 5% of errors is where the production risk lives. A 95% accurate eval pass is not a 95% safe product — it's a 5% liability surface.

### The AI Evals Stack
Three layers, always all three:

| Layer | Volume | Fidelity | What it tells you |
|---|---|---|---|
| **User feedback** | Highest | Lowest | What users do (thumbs, regen, abandon) |
| **Human evaluation** | Mid | High | What graders think (rubric scores) |
| **Automated evaluation** | Highest | Mid | What an LLM-judge or regression suite measures |

### Human Eval Rubric (anatomy)
1. **Dimension** — what you're scoring (accuracy, tone, completeness, safety, etc.)
2. **Scale** — 1–5 or pass/fail, with anchor descriptions.
3. **Examples** — one example per scale point.
4. **Disagreement protocol** — what to do when graders disagree.
5. **Sampling cadence** — how often, how many.

### The Governance Framework
Operationalising AI risks across four buckets:
- **Compliance** — regulatory (GDPR, EU AI Act, etc.)
- **Safety** — content, prompt injection, misuse
- **Reliability** — uptime, fallback paths
- **Reputation** — public failure scenarios + response playbook

### The Three Levers to Optimise AI Performance
When eval scores miss the bar, the cost-to-try ascending:

1. **Model** — swap, upgrade, fine-tune.
2. **Data** — improve the corpus, expand context.
3. **Architecture** — add RAG, decompose into agents, add guardrails.

Always try Model and Data before Architecture.

### The PM Execution Plan
The closing artifact of M6 — your `06-evals/eval-stack.md` plus the top-level `README.md` with:

- **Where Juno is today** (eval scores, known gaps)
- **What you ship next** (next 2 sprints)
- **What you watch** (the dashboard / cadence)
- **What blocks shipping** (the red lines)

---

## Course-wide cheat sheet

| If you're asked… | Reach for… |
|---|---|
| "Is this a real value driver?" | Four AI Value Propositions (M2) |
| "What level of autonomy?" | Jobs × Risk × Autonomy (M2) |
| "Should we ship this AI bet?" | AI Solution Decision Matrix (M2) |
| "How do I write the system prompt?" | Anatomy of a High-Quality Prompt (M1) |
| "Prompt or RAG or fine-tune?" | The Optimization Decision Framework (M1) |
| "How do I specify the data?" | RAG trade-offs + decision factors (M3) |
| "What goes in an AI PRD?" | The three new sections (M3) |
| "Where does the AI live in the UI?" | Mapping Value to UX Treatment (M4) |
| "What's the user flow?" | The seven AI user flow nodes (M4) |
| "Will users trust this?" | The three AI-UX trust gaps (M4) |
| "When does Juno act vs. ask?" | The PM Decision Triangle (M5) |
| "What goes in the Agent Workflow Spec?" | AWSpec anatomy (M5) |
| "How do I prove quality?" | The AI Evals Stack (M6) |
| "Eval score is below bar — what now?" | The Three Levers (M6) |
