# 05 — Agentic Workflows (Module 5)

Commit two artifacts here:

- `awspec.md` — Agent Workflow Spec, from **`M5 - Agent Workflow Spec Builder.html`**. The four pillars: Actors, Pattern Plan, Memory, Tools.
- `agent-control-panel.md` — companion to AWSpec, from **`M5 - Agent Control Panel.html`**. Four levers + four rules of engagement.

Plus one optional file we've provided:

- `Juno Agent.json` — a starter Langflow export for the optional M5 post-class lab. Import into Langflow, plug in your OpenAI API key, and run it against a sample P0 thread.

> **Tools:** `M5 - Agent Workflow Spec Builder.html`, `M5 - Agent Control Panel.html`, `M5 - Juno Langflow Walkthrough.html`.

## Self-review checklist (M5)

- AWSpec covers all four pillars (Actors, Pattern Plan, Memory, Tools).
- Trigger is a precise, testable condition.
- Pattern is chosen with a reason (default: ReAct).
- ≥ 3 stop conditions, including escalation.
- Each memory type named (in-scope or out-of-scope).
- Every tool lists scope (read-only / write) and a schema.
- Read/write boundaries match the AI PRD (M3) access control.
- Control panel names a numeric `max_steps`, confidence threshold, and a North Star sentence.

## AI-review prompt

> *You are a staff engineer reviewing an Agent Workflow Spec. (a) Are the stop conditions precise enough to implement? (b) Is the human-handoff threshold realistic, or aspirational? (c) Of the four common failure modes (silent failures, reasoning drift, infinite loops, latency tax), which is least defended in this spec? Quote the offending lines and propose tighter wording. Reply in 4 short paragraphs.*

## Optional post-class — Build Juno's workflow in Langflow

Walkthrough: open `Modules/M5 - Juno Langflow Walkthrough.html` for a guided 6-step build. Two paths:

- **Path 1 — Import** the starter `Juno Agent.json` (~15 min).
- **Path 2 — Rebuild** the graph node-by-node from your AWSpec (~45 min).

Either way, capture screenshots into `05-agentic-workflows/langflow-screenshots/` and a one-paragraph reflection in `05-agentic-workflows/langflow-notes.md` on what surprised you compared to your AWSpec.
