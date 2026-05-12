# Module 5 — Frameworks Reference Card

Quick-lookup card for M5.

---

## The Agent Spectrum

Tool → Assistant → Agent → Autonomous Agent. Pick the lowest level that delivers the job.

---

## Four Traits of Agency

- Goals
- Tool use
- Memory
- Iteration

If a system has all four, it's an agent.

---

## ReAct (single-agent pattern)

*Reason → Act → Observe → loop.* Best for bounded, sequential tasks with feedback loops.

---

## Planner-Executor (multi-agent pattern)

Planner decomposes; executors run; planner re-plans on failure. Best for parallel / long tasks.

---

## Agentic Memory (four types)

| Type | Lifetime |
|---|---|
| Short-term | Within one task |
| Long-term | Across sessions |
| Episodic | Specific past events |
| Semantic | General knowledge |

Spec each as in-scope or out-of-scope.

---

## Common Failure Modes (spec for these)

- Hallucinated tool calls
- Memory poisoning
- Runaway loops
- Silent handoff failure
- Drift across sessions

---

## The PM's Agent Control Panel (5 levers)

- Triggers
- Tools (with scope)
- Memory scope
- Stop conditions
- Observability

---

## Agent Workflow Spec (AWSpec) — 9 sections

1. Goal
2. Trigger
3. Inputs
4. Tools available
5. Memory
6. Pattern (ReAct / Planner-Executor)
7. Stop conditions
8. Handoff rules
9. Eval hooks

---

## The PM Decision Triangle

At each step: **AI alone / AI + human / human alone.** The boundary contract.

---

## Reach-for-this-when…

| If you're asked… | Reach for… |
|---|---|
| "Is this really an agent?" | Four Traits of Agency |
| "What level of autonomy?" | The Agent Spectrum + the lowest-level rule |
| "Which pattern?" | ReAct (default) vs. Planner-Executor |
| "What does the agent remember?" | The four memory types |
| "Where might this fail?" | The five common failure modes |
| "What goes in the spec?" | AWSpec — 9 sections |
| "Who decides at this step?" | The PM Decision Triangle |
