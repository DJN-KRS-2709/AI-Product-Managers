# Module 4 — Pre-Read

10–15 minutes. Skim before the live session.

---

## What you'll do in M4

Two artifacts committed to `04-ai-ux/`:

- `04-ai-ux/user-flow.md` — Juno's AI user flow for one pillar, with 7 nodes
- `04-ai-ux/trust-gaps.md` — three trust gaps scored, with explicit mitigations

Optional, post-class: `04-ai-ux/screenshots/` — updated Juno surfaces.

---

## The shift M4 makes

You walked in with an AI PRD. You walk out knowing exactly **where the AI lives in the UI** and **why users will trust it**.

The biggest mistake AI PMs make: design the model, ship the chat box. We will not do that.

---

## Two principles to internalise

### 1. Invisible by design

AI-native UX anticipates intent and acts at the right moment, instead of waiting at a chat box for the user to type.

The chat box is the worst possible default. It puts the entire cognitive load on the user (figure out what to ask, how to phrase it, when to ask), and turns the AI into a tool rather than a partner.

For Juno: the *right* surface is a proactive risk panel in `#escalations` that appears when a P0 thread crosses 5 messages — not a side-panel chat the PM has to remember exists.

### 2. The three trust gaps

A probabilistic system feels safe only when three gaps are explicitly closed.

| Gap | Question | Mitigation |
|---|---|---|
| **Black-box** | Can the user see *why*? | Reasoning, citations, "show your work" |
| **Hallucination** | Could this confidently be wrong? | Confidence cues, source links, escape hatches |
| **Control** | Can the user steer or stop? | Undo, edit, regenerate, "don't suggest this again" |

If any gap is open, you've shipped an AI feature users won't use.

---

## The AI Iceberg in 60 seconds

What the user sees (the *tip*) is a small fraction of what runs (the *underwater*). PMs design both:

- **Tip:** Trigger / Surface / Confirm-Correct.
- **Underwater:** Capture / Retrieve / Reason / Act / Log / Guardrails / Fallback.

Each node gets one specific line in the AI user flow.

---

## Bring to M4

- One screenshot of an AI UX that frustrates you. We'll start the session by sharing examples.
- Your `03-rag-prd/ai-prd.md` — the user flow we design today implements that PRD.
- Optional: a Juno Lovable URL you can update during the optional post-class lab.

---

## Format reminder

100% individual. No groups. Self-review + AI-review + async share in `#ai-pm-cohort`.
