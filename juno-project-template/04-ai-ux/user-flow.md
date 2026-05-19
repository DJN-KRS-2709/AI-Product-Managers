# Juno PM — AI User Flow

_Module 4 final-project deliverable. Replace seed text with output from `Modules/M4 - AI User Flow Architect.html`._

---

## 0. Carry-over from prior modules

- **Bet** _(from `02-strategy/strategy-one-pager.md`)_:
- **Autonomy level** (Assist / Copilot / Agent) _(from `02-strategy/decision-matrix.md`)_:
- **Retrieval strategy** _(from `03-rag-prd/prd.md`)_:

---

## 1. Pillar 1 — The Trigger

**Signal type:** _(File / Message / Page-load / Meeting end / Time-based / User action / Threshold / Other)_

**Specific signal in Juno**

_(Describe the earliest moment data enters the system — e.g. "A new P0 customer transcript is uploaded to the Raw Input column.")_

**Surface response — what the user sees instantly**

_(The status badge / breadcrumb / animation that fires before the model finishes — e.g. "Juno is reading your transcript…" pill appears, columns dim to 40%.)_

---

## 2. Pillar 2 — The Processing State

**Hidden logic — major underwater steps**

_(2–4 steps. e.g. RAG retrieval over Strategy One-Pager → comparison logic → risk + alignment scoring → confidence check.)_

**Handshake breadcrumbs — surface status messages**

_(Turn latency into transparency. e.g. "Scanning Strategy One-Pager…" → "Cross-referencing 1 transcript with 4 strategic pillars…" → "Synthesising priorities…")_

**Router decision (if multi-path)**

_(Skip if single-path. Otherwise spell out: Path A (X) → Y. Path B (X) → Z. How does the system decide?)_

---

## 3. Pillar 3 — The Presentation

**Placement maneuver:** _(Inline & Embedded / Floating & Contextual / Full-Page Canvas / Hybrid)_

**Generated output — what the user actually sees**

_(Be specific. e.g. "Three Insight Cards in column 2 with P0–P3 badge, evidence quote from the transcript, and a Strategic Traceability footer citing the strategic pillar.")_

**Why this maneuver — the value it wraps**

_(Link the placement back to the M2 value prop: Automation / Augmentation / Insights / Personalization. e.g. "Augmentation → user reviews + edits, doesn't create from blank.")_

---

## 4. Pillar 4 — The Feedback Loop

**Kill switch — how the user overrides Juno**

_(Every automated decision must have a one-click override or undo. e.g. "Manual Override button on every priority card.")_

**Captured training signal — what gets logged back**

_(Every accept / edit / reject is a training signal. e.g. "Manual demote → logged as 'strategic-alignment correction' → tightens future scoring.")_

**Fail-safe — what happens when the underwater logic fails**

_(RAG returns nothing, API errors, low confidence — the surface always offers a clean human path. "If Strategy Doc missing → Juno surfaces 'cautious mode' warning + drops priority confidence to N/A.")_

---

## Self-review

- [ ] Trigger fires on the earliest possible signal — no manual "Start AI" click.
- [ ] At least one breadcrumb message turns latency into transparency.
- [ ] Maneuver matches the M2 value prop (Automation / Augmentation / Insights / Personalization).
- [ ] Every automated decision has a working kill switch.
- [ ] Fail-safe path is explicit. No dead end with a bad AI result.
- [ ] Hidden logic references M3 PRD specs (Top-K, latency target, knowledge base).

## AI-review

Paste this section + the meta-prompt from `M4 - AI User Flow Architect.html` into ChatGPT or Claude. Save the critique into a follow-up commit.
