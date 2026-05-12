# Module 4 — Design AI-Native User Experiences (Shareable Notes)

A faithful expansion of the Module 4 slides. Individual format throughout.

By the end of this module you commit two artifacts to `04-ai-ux/`:

- `04-ai-ux/user-flow.md` — Juno's AI user flow for one pillar, with 7 nodes specified
- `04-ai-ux/trust-gaps.md` — the three trust gaps scored, with explicit mitigations

(Optional, post-class) `04-ai-ux/screenshots/` — updated Juno surfaces from the AI-native rework.

---

## 1. Intent-Driven AI Design Systems

The UX we've come to accept but shouldn't have:

- Chat boxes everywhere → cognitive load.
- "Magic wand" buttons with unclear scope.
- No confidence cues → user can't tell when to trust.
- No escape hatches → user can't steer or stop.

You can have the best model, the cleanest RAG, the tightest evals — and still lose to a competitor whose UX:

- Reveals reasoning when it matters.
- Surfaces confidence visually.
- Lets the user steer in one click.
- Gets out of the way when the AI is wrong.

UX is where trust is built or destroyed. Spec it like a feature, not a polish task.

---

## 2. Designing Invisible UI for AI-Native Outcomes

**Invisible by design** is the default for AI-native UX. The system anticipates intent and acts at the right moment instead of waiting at a chat box.

| Wrong default | Right default |
|---|---|
| Juno is a chat tab in the sidebar. PM must remember it exists, open it, type. | Juno surfaces a prioritised risk panel in Slack #escalations the moment a P0 thread crosses 5 messages. |

### Mapping Value to UX Treatment

Pick UX patterns by value frame, not aesthetic.

| Value frame | UX treatment | Juno example |
|---|---|---|
| Cost reduction | Background automation with audit trail | Auto-tag P0/P1 on incoming Slack threads |
| Revenue generation | Inline assist at the moment of decision | "Draft spec from this thread" button in Slack |
| Risk mitigation | Proactive flag + reason + one-click action | Daily top-3 risks panel in #pm-daily |
| User delight | Anticipatory suggestion, dismissible | "Looks like this thread is going P0 — want a summary?" |

For Juno (Risk-mitigation primary), the dominant UX treatment is **proactive flag + reason + one-click action.**

---

## 3. How to Architect an AI User Flow

### The AI Iceberg

| Tip (what users see) | Underwater (what runs) |
|---|---|
| Trigger | Capture context |
| Surface | Retrieve from corpus |
| Confirm / Correct | Reason (model call) |
|  | Act (tool calls, writes) |
|  | Log (evals, traces) |
|  | Guardrail checks |
|  | Fallback paths |

Most PMs design the tip and hand-wave the underwater. **Spec both.** The underwater is engineering territory, but PMs spec what happens at each step (when to retrieve, what to log, what fallback).

### The Seven Nodes

Every AI user flow has these seven nodes:

1. **Trigger** — what initiates the flow.
2. **Capture** — what context the system gathers.
3. **Retrieve** — what data is pulled in.
4. **Reason** — what the model decides.
5. **Act** — what happens in the world (send / write / call).
6. **Surface** — what the user sees.
7. **Confirm / Correct** — how the user steers, accepts, overrides.

> Use **`M4 - AI User Flow Architect.html`** — spec all 7 nodes for one Juno pillar; mark tip vs. underwater per node; export to `04-ai-ux/user-flow.md`.

### Individual Exercise — Architect Juno's Core AI User Flow (30 min)

This is the M4 deliverable. (Was previously a breakout group exercise. Now solo.)

1. Pick **one** Juno pillar to flow first (recommendation: Prioritize Risks).
2. Open `M4 - AI User Flow Architect.html`.
3. Spec the 7 nodes. Be specific (e.g., Trigger = "new P0 tagged in #escalations and ≥5 messages in 10 min").
4. Mark tip vs. underwater per node.
5. Copy as markdown → `04-ai-ux/user-flow.md`.

#### Self-review checklist

- The user flow names a real trigger (not "user opens app").
- Each of the 7 nodes has one specific line.
- Tip vs. underwater is marked per node.
- The Act node names specific tool calls.
- The Surface node specifies where (Slack channel / Notion / Jira block).

#### AI-review prompt

Paste your `user-flow.md` + this into ChatGPT/Claude/Cursor:

> *You are an AI-UX designer. Read this AI user flow for Juno PM. (a) Is the trigger specific enough to test? (b) Are the underwater nodes specced thinly enough that engineering knows what to build, but not so thickly that the PM is doing eng's job? (c) Which node creates the most user trust risk, and what would you add? Reply in 4 short paragraphs.*

#### Async share

Commit, push, post link in `#ai-pm-cohort` with a 1-paragraph reflection.

---

## 4. The PM's Playbook for Closing AI Trust Gaps

Three gaps. Close all three or you don't ship.

| Gap | Question | Mitigation |
|---|---|---|
| **Black-box** | Can the user see *why*? | Reasoning, citations, "show your work" |
| **Hallucination** | Could this confidently be wrong? | Confidence cues, source links, escape hatches |
| **Control** | Can the user steer or stop? | Undo, edit, regenerate, "don't suggest this again" |

> Use **`M4 - AI-UX Trust Gap Checker.html`** — score each gap, write mitigations, add intelligence-tax row, export to `04-ai-ux/trust-gaps.md`.

### Managing the Intelligence Tax

The extra latency or cognitive load the user must endure for AI value is a product surface.

- Spec the maximum acceptable latency (p95).
- Decide whether to stream output (perceived latency drops dramatically).
- Decide whether to show "Juno is reasoning…" (transparency vs. distraction).
- If the intelligence tax exceeds the value frame, kill the feature.

---

## 5. Optional Post-Class Lab (Individual) — Reimagine Juno as an AI-Native Copilot

- Move Juno out of a standalone chat tab.
- Embed it directly into Slack/Jira/Notion — proactive surfaces, not reactive chat.
- If the user never had to type a prompt, how would Juno still deliver value?
- Update your Lovable URL or commit a screenshot to `04-ai-ux/screenshots/`.

Async-share-only. Instructor responds in `#ai-pm-cohort` thread.

---

## Key takeaways

1. Chat-in-a-tab is the wrong default.
2. Invisible by design — anticipate intent.
3. Map value → UX treatment. Don't pick UX patterns by aesthetic.
4. The AI Iceberg has 7 nodes. Spec all of them.
5. Close all three trust gaps before shipping.

---

## Before Module 5 (~20 min)

- Skim **`Module 5 - Pre-Read.md`** (agent spectrum, ReAct, Planner-Executor, memory).
- Re-read your `04-ai-ux/user-flow.md`'s **Act** node — M5 turns it into an Agent Workflow Spec.
- Post your AI-UX links in `#ai-pm-cohort` if you haven't.

---

## Learning objectives (mapped to outcomes)

| LO | What you produced |
|---|---|
| Evaluate the evolution of AI design systems | The "wrong vs. right default" reflection in `user-flow.md` |
| Analyze the strategic placement of AI interactions | Value-to-UX mapping in `trust-gaps.md` |
| Construct a comprehensive AI user flow | `04-ai-ux/user-flow.md` (7 nodes, tip+underwater) |
| Formulate a strategy to mitigate AI trust gaps | `04-ai-ux/trust-gaps.md` (three gaps + intelligence tax) |
