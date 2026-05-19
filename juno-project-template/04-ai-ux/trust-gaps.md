# Juno PM — Trust-Gap Audit

_Module 4 **optional** post-class deliverable. Replace seed text with output from `Modules/M4 - Juno AI-Native Lab.html` (post-class lab) or `Modules/M4 - AI-UX Trust Gap Checker.html` (audit a feature)._

---

## Option A — Optional post-class lab output

Output from `M4 - Juno AI-Native Lab.html` after running Path 1 or Path 2 in Lovable.

### What you ran

- **Path:** _(Path 1 — Strategic Trust Ladder / Path 2 — Frictionless Architect / both)_
- **Lovable prototype URL:** _(paste post-upgrade URL)_

### Black-box gap — what changed

_(How does Juno now make its reasoning verifiable in under 3 seconds? Citations? Confidence meter? Logic map?)_

### Hallucination gap — what changed

_(How does Juno signal uncertainty? How does the user edit just the wrong parts without rewriting from scratch?)_

### Control gap — what changed

_(What kill switch / manual override / fail-safe did you add? The user is always the final authority.)_

### Forever takeaway

> _(One sentence about AI-native UX you'll never forget.)_

---

## Option B — Audit a real product (M4 - AI-UX Trust Gap Checker)

Use this when you want to score Juno (or any feature in your real product) against the three trust gaps + the intelligence tax.

### Feature audited

_(Name + 1-line description of the feature.)_

### Scores (1 = wide open, 5 = closed)

| Gap | Score | Mitigation |
|---|---|---|
| **Black-box gap** | _/5 | _(specific UI / UX / logic change to ship)_ |
| **Hallucination gap** | _/5 | _(specific UI / UX / logic change to ship)_ |
| **Control gap** | _/5 | _(specific UI / UX / logic change to ship)_ |
| **Intelligence tax** | _/5 | _(streaming, breadcrumbs, p95 cap, privacy badge)_ |

**Average:** _/5
**Lowest gap:** _/5

### Verdict

- [ ] **Shippable** — all gaps ≥ 4. Trust posture passes.
- [ ] **Hold** — at least one gap is 2 or 3. Close before shipping or down-scope to validator UI.
- [ ] **Unsafe** — at least one gap = 1. Re-spec from AI-UX Readiness Checklist Level 1.

---

## Self-review

- [ ] Each mitigation is specific (UI / UX / logic), not aspirational.
- [ ] Every gap that scored ≤ 3 has a closure plan with an owner.
- [ ] Forever takeaway is one sentence — not a list.
- [ ] If you ran Option A: Lovable prototype URL works in incognito.
