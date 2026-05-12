# 05 — Agentic Workflows (Module 5)

Commit two artifacts here:

- `awspec.md` — from **M5 - Agent Workflow Spec Builder.html**
- `control-panel.md` — from **M5 - Agent Control Panel.html**

Plus one optional file we've provided:

- `Juno Agent.json` — a starter Langflow export for the optional M5 post-class lab. Import into Langflow, plug in your OpenAI API key, and run it against a sample P0 thread.

> **Tools:** `M5 - Agent Workflow Spec Builder.html`, `M5 - Agent Control Panel.html`.

## Self-review checklist (M5)

- AWSpec has all 9 sections filled
- Tools list scope (read-only / write) for each tool
- Memory section names all 4 memory types (in or out)
- ≥3 stop conditions including escalation
- Handoff rule names a numeric confidence threshold
- Eval hooks defined (this is what M6 wires up)

## AI-review prompt

> *You are a staff engineer reviewing an Agent Workflow Spec. (a) Are the stop conditions precise enough to implement? (b) Is the handoff confidence threshold realistic, or is it aspirational? (c) Of the five common failure modes (hallucinated tool calls, memory poisoning, runaway loops, silent handoff failure, drift), which is the least defended in this spec? Reply in 4 short paragraphs.*

## Optional: run the Langflow lab

1. Install [Langflow](https://docs.langflow.org/).
2. Import `Juno Agent.json`.
3. Add your `OPENAI_API_KEY` as a Langflow env variable (~$5 credit is enough).
4. Replace the `RAG retriever (placeholder)` node with a real vector store.
5. Run it against a sample P0 thread.
6. Adjust the confidence threshold in the guardrail node based on your eval data (M6).
