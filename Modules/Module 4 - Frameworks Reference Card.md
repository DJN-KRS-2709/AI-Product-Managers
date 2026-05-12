# Module 4 — Frameworks Reference Card

Quick-lookup card for M4.

---

## Invisible by Design

Default for AI-native UX. System anticipates intent and acts at the right moment instead of waiting at a chat box.

---

## Mapping Value to UX Treatment

| Value frame | UX treatment |
|---|---|
| Cost | Background automation with audit trail |
| Revenue | Inline assist at moment of decision |
| Risk | Proactive flag + reason + one-click action |
| Delight | Anticipatory suggestion, dismissible |

---

## The AI Iceberg

| Tip (visible) | Underwater (invisible) |
|---|---|
| Trigger | Capture context |
| Surface | Retrieve |
| Confirm / Correct | Reason |
|  | Act |
|  | Log |
|  | Guardrail checks |
|  | Fallback paths |

---

## The Seven Nodes of an AI User Flow

1. **Trigger** — what initiates
2. **Capture** — what context is gathered
3. **Retrieve** — what data is pulled
4. **Reason** — what the model decides
5. **Act** — what happens in the world
6. **Surface** — what the user sees
7. **Confirm / Correct** — how the user steers

---

## The Three AI-UX Trust Gaps

| Gap | Question | Mitigation |
|---|---|---|
| Black-box | Can the user see *why*? | Reasoning / citations / show your work |
| Hallucination | Could this confidently be wrong? | Confidence cues / source links / escape hatches |
| Control | Can the user steer or stop? | Undo / edit / regenerate / suppress |

---

## The Intelligence Tax

Extra latency or cognitive load the user endures for AI value. Spec it down:

- p95 latency cap
- Streaming output on/off
- "Reasoning…" indicator on/off
- Kill feature if tax > value frame

---

## Reach-for-this-when…

| If you're asked… | Reach for… |
|---|---|
| "Where should the AI live in the UI?" | Mapping Value to UX Treatment |
| "What's the user flow?" | The seven nodes |
| "Will users trust this?" | The three trust gaps |
| "It feels too slow / heavy" | The intelligence tax |
| "Why don't we just add a chat box?" | Invisible by Design |
