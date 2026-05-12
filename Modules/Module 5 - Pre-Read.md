# Module 5 — Pre-Read

10–15 minutes. Skim before the live session.

---

## What you'll do in M5

Two artifacts committed to `05-agentic-workflows/`:

- `05-agentic-workflows/awspec.md` — the Agent Workflow Spec (M5 deliverable)
- `05-agentic-workflows/agent-control-panel.md` — the five-lever spec

Optional, post-class: `05-agentic-workflows/langflow-screenshots/`.

---

## The shift M5 makes

You walked in with an AI user flow (M4). You walk out with an **Agent Workflow Spec** — the rules of engagement for letting an AI *act*, with explicit handoff lines.

The previous modules spec'd outputs (what the AI produces). M5 specs **actions** (what the AI does in the world). The cost of a bad spec doubles.

---

## Three things to read first

### 1. The four traits of agency

If a system has all four, it's an agent:

- **Goals** — pursues a goal, not just responds.
- **Tool use** — calls functions on the world.
- **Memory** — state persists across turns or sessions.
- **Iteration** — observes results and re-plans.

When vendors say "AI agent," ask which traits are present. Most "agents" in pitch decks are mid-spectrum.

### 2. ReAct vs. Planner-Executor

- **ReAct** — *Reason → Act → Observe → loop.* Single-agent. Default pattern.
- **Planner-Executor** — planner decomposes; executors run; planner re-plans. Multi-agent. Use when sub-tasks are parallel or the plan doesn't fit in one context window.

For most M5 work, default to ReAct.

### 3. The Agent Workflow Spec — 9 sections

The deliverable. Memorise the section names:

1. Goal
2. Trigger
3. Inputs
4. Tools available
5. Memory
6. Pattern
7. Stop conditions
8. Handoff rules
9. Eval hooks

---

## Bring to M5

- Your `04-ai-ux/user-flow.md` from M4 — M5 turns the **Act** node into an AWSpec.
- A guess at which agent pattern Juno needs (ReAct vs. Planner-Executor).
- Optional: a Langflow account + OpenAI API key for the post-class lab.

---

## Format reminder

100% individual. Self-review + AI-review + async share in `#ai-pm-cohort`.

---

## Optional reading

- Anthropic — *Building effective agents.* The single best primer on patterns and pitfalls.
- LangChain — *Multi-agent systems.* If you're considering Planner-Executor.
- *Cognition's Devin retrospective* — what worked, what didn't.

Not required to pass M5.
