# Module 5 — Deploy Agentic Systems and Workflows (Shareable Notes)

A faithful expansion of the Module 5 slides. Individual format throughout.

By the end of this module you commit two artifacts to `05-agentic-workflows/`:

- `05-agentic-workflows/awspec.md` — the Agent Workflow Spec (M5 deliverable)
- `05-agentic-workflows/agent-control-panel.md` — the five-lever spec

Plus, optional post-class: `05-agentic-workflows/langflow-screenshots/` from the Langflow lab.

---

## 1. The Shift to Agentic Orchestration

- **Chat** (Year 1): model generates text. Human acts.
- **Copilot** (Year 2): model drafts, human approves, human acts.
- **Agent** (Year 3, now): model plans, calls tools, observes, iterates. **Model acts.**

The big change: "model acts." Up until now we've spec'd outputs. From here on we spec rules of action.

---

## 2. What is an agent?

### Key traits of agency

If a system has all four, it's an agent. If it has one or two, it's a tool or assistant.

- **Goals** — pursues a goal, not just responds.
- **Tool use** — calls functions on the world.
- **Memory** — state persists across turns or sessions.
- **Iteration** — observes results, re-plans.

### The Agent Spectrum

Pick the **lowest** level that delivers the job. Higher levels need explicit handoff rules.

| Level | Behaviour | Juno example |
|---|---|---|
| Tool | Does one thing on request | "Summarise this thread" |
| Assistant | Drafts, recommends | Juno suggests 3 risks; PM picks |
| Agent | Plans + calls tools + iterates | Juno triages P0s, opens Jira stubs, posts to #pm-daily |
| Autonomous Agent | Operates long horizons unsupervised | Not appropriate for Juno's risk profile |

### Examples in the wild

- **Devin (Cognition)** — autonomous software engineer.
- **Salesforce Agentforce** — customer service + sales workflows.
- **Klarna AI assistant** — resolves 2.3M customer queries/month.
- **Anthropic Computer Use** — controls a desktop to complete tasks.

Common pattern: bounded scope, explicit tools, human checkpoint at high-risk steps.

### The Hidden Costs of Autonomy

- **Cascading errors** — one wrong tool call → next step builds on it.
- **Cost blowup** — autonomous loops without stop conditions burn tokens.
- **Audit opacity** — "the agent decided" is not an audit log.
- **Drift** — long-term memory pulls behaviour off-spec over weeks.

The PM job: make these costs visible and bounded in the spec.

---

## 3. Agentic Design Patterns

### ReAct

*Reason → Act → Observe → loop.* Single-agent reasoning. Best for bounded, sequential tasks with feedback loops.

Juno triaging one P0 thread: read the thread, decide to query the strategy corpus, see the result, decide to query the ARR sheet, etc.

### Planner-Executor

One planner agent decomposes the task; one or many executors run the steps; the planner re-plans on failure. Best for multi-step tasks with parallelism.

Juno running the full daily risk pipeline across all `#escalations` channels.

For most PM purposes, ReAct is the workhorse. Planner-Executor enters when you have parallel sub-tasks or when a single agent's context window can't hold the whole plan.

---

## 4. Types of Agentic Memory

| Type | Lifetime | Use for |
|---|---|---|
| Short-term | Within one task | Tool results, intermediate reasoning |
| Long-term | Across sessions | User preferences, learned facts |
| Episodic | Specific past events | "Last week the user said X" |
| Semantic | General knowledge | Org context, domain facts |

Memory choices shape privacy, cost, and behaviour. **Spec each one explicitly** — including the no's. "Juno does not maintain long-term memory of customer-specific contracts" is a spec line worth writing.

---

## 5. Common Failure Modes

Spec for the failure, not just the success path.

- **Hallucinated tool calls** — the agent invents an API.
- **Memory poisoning** — bad data persisted as fact.
- **Runaway loops** — no stop condition; cost explosion.
- **Silent handoff failure** — should have escalated, didn't.
- **Drift across sessions** — long-term memory off-spec.

The AWSpec has explicit handling for each.

---

## 6. Managing the Agentic Handoff

### The PM's Agent Control Panel

Five levers a PM specs and watches:

- **Triggers** — when does the agent activate?
- **Tools** — what can it call?
- **Memory scope** — what does it remember, for how long?
- **Stop conditions** — when does it hand back / shut down?
- **Observability** — logs, traces, eval surface (M6).

> Use **`M5 - Agent Control Panel.html`** — spec each lever; declare the minimum viable rule; export to `05-agentic-workflows/agent-control-panel.md`.

### Agent Workflow Spec (AWSpec) — 9 sections

The M5 deliverable.

1. **Goal** — one sentence.
2. **Trigger** — exact condition.
3. **Inputs** — required context.
4. **Tools available** — explicit list, with each tool's scope.
5. **Memory** — what's stored, where, for how long.
6. **Pattern** — ReAct or Planner-Executor (+ why).
7. **Stop conditions** — success, failure, escalation, timeout.
8. **Handoff rules** — when does Juno hand back to the PM?
9. **Eval hooks** — what gets logged for the M6 eval stack.

> Use **`M5 - Agent Workflow Spec Builder.html`** — fill all 9 sections; export to `05-agentic-workflows/awspec.md`.

### The PM Decision Triangle

At every step of an agent workflow, the PM decides:

| Mode | When | Example for Juno |
|---|---|---|
| **AI alone** | Low risk, high earned trust | Auto-tagging P0/P1 |
| **AI + human checkpoint** | High-risk steps | Drafting a P0 spec |
| **Human alone** | Contracts, regulators, novel situations | Customer escalation calls |

The triangle is the **boundary contract** between PM and agent.

---

## 7. Individual Exercise — Write Juno's Agent Workflow Spec (30 min)

(Was previously a breakout group exercise. Now solo.)

1. Open `M5 - Agent Workflow Spec Builder.html`.
2. Take your M4 user-flow's **Act** node and turn it into an AWSpec.
3. Use ReAct as the default pattern unless you have a specific reason for Planner-Executor.
4. Be precise about stop conditions and handoff rules.
5. Copy as markdown → `05-agentic-workflows/awspec.md`.

### Self-review checklist

- Goal is one sentence and names the value frame.
- Trigger is a precise, testable condition.
- Tools are listed with scope (read-only? write?).
- Memory section names each of the 4 types as in-scope or out-of-scope.
- Stop conditions list at least 3 (success, failure, escalation).
- Handoff rules name a confidence threshold.

### AI-review prompt

Paste your `awspec.md` + this into ChatGPT/Claude/Cursor:

> *You are a staff engineer reviewing an Agent Workflow Spec. (a) Are the stop conditions precise enough to implement? (b) Is the handoff confidence threshold realistic, or is it aspirational? (c) Of the listed failure modes, which is most likely to bite this agent first, and is the spec defensive enough? Reply in 4 short paragraphs.*

### Async share

Commit, push, post link in `#ai-pm-cohort`.

---

## 8. Optional Post-Class Lab — Build Juno's Agentic Workflow in Langflow

Open `juno-project-template/05-agentic-workflows/Juno Agent.json`. Import into Langflow. Add an OpenAI API key. Run the workflow with a test P0 thread. Capture screenshots to `05-agentic-workflows/langflow-screenshots/`.

Requires Langflow + OpenAI API credits. Encourage radical experimentation — change the pattern, add a tool, remove memory and see what breaks.

---

## Key takeaways

1. Pick the lowest agent level that delivers the job.
2. Spec the four traits (goals, tools, memory, iteration) — including the no's.
3. ReAct is the default pattern. Planner-Executor for parallel/long.
4. The AWSpec has 9 sections. All of them required.
5. The PM Decision Triangle is the boundary contract.

---

## Before Module 6 (~20 min)

- Skim **`Module 6 - Pre-Read.md`** (AI Evals Stack).
- Re-read your AWSpec's **Eval hooks** section — M6 turns it into a real eval stack.
- Post your `05-agentic-workflows/` links in `#ai-pm-cohort`.

---

## Learning objectives (mapped to outcomes)

| LO | What you produced |
|---|---|
| Evaluate the transition to agentic orchestration | The agent-spectrum placement in `awspec.md` |
| Analyze the agentic reasoning stack | ReAct vs. Planner-Executor choice in `awspec.md` |
| Deconstruct common agentic design patterns | Pattern + memory sections of `awspec.md` |
| Construct a framework for human-agent collaboration | Handoff rules section of `awspec.md`; `agent-control-panel.md` |
| Apply technical orchestration principles to a functional system | Optional Langflow lab output |
