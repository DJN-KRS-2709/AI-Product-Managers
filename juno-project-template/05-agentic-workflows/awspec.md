# Juno PM — Agent Workflow Spec (AWSpec)

_Version 0.1 — placeholder. Replace via `M5 - Agent Workflow Spec Builder.html`._

> The technical bridge for translating a high-level agentic feature into a structured, governable design that engineering can build and you can measure.

---

## 0. Carry-over from prior modules

- **Bet** _(from `02-strategy/strategy-one-pager.md`)_:
- **AI PRD** _(from `03-rag-prd/ai-prd.md`)_:
- **User flow** _(from `04-ai-ux/user-flow.md`)_:

---

## 1. Pillar 1 — Actors

**Goal**

_(one sentence; names the value frame: cost / revenue / risk / delight)_

**Trigger**

_(precise, testable condition — not "when needed")_

**Primary actor**

_(Agent autonomous / Agent + Human-in-the-loop / Human + Agent co-pilot / Planner + Executor agents)_

**Humans in the loop**

_(when does control pass back to a human? threshold, channel, owner)_

---

## 2. Pillar 2 — Pattern Plan

**Pattern:** _(ReAct / Planner-Executor / Hybrid)_

**Sequential steps**

_(2–5 steps; action verbs)_

1.
2.
3.

**Stop conditions**

- Success:
- Failure:
- Escalation:
- Timeout:

---

## 3. Pillar 3 — Memory

**Episodic — sequence of actions in this run**

_(in-scope or out-of-scope; lifetime)_

**Semantic — persistent behaviours / preferences**

_(in-scope or out-of-scope; lifetime; include the "no's")_

**Working / Contextual — live, in-flight data**

_(what is held in working context only)_

**External tools — sources of truth via APIs**

_(which APIs / databases the agent reads from for ground truth)_

---

## 4. Pillar 4 — Tools

**Tool inventory** (one per line, with scope)

- `tool.method(args)` — read-only
- `tool.method(args)` — write, requires confidence ≥ X%

**Schemas — what each tool returns**

- `tool.method` → `{...}`

**Read / write boundaries**

_(what the agent CAN and CANNOT touch)_

---

## Self-review

- [ ] Goal is one sentence and names the value frame.
- [ ] Trigger is a precise, testable condition.
- [ ] Pattern is chosen with a defensible reason (default: ReAct).
- [ ] At least 3 stop conditions, including escalation.
- [ ] Each memory type named (in or out).
- [ ] Every tool lists scope (read-only vs write) and a schema.
- [ ] Read/write boundaries match the AI PRD (M3) access control.
