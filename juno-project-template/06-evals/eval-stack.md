# Juno PM — Eval Stack

_Version 0.1 — placeholder. Replace via the M6 — Eval Stack Designer tool._

> Three layers. Always all three. They answer different questions. Plan each layer with signals/checks, cadence, pass bar, and a named owner.

## Layer 1 · User feedback (online · highest volume)

**Signals captured:**
- Active: _(e.g. thumbs up/down on each Juno output, regenerate button, free-text feedback when thumbs-down)_
- Passive: _(e.g. dismiss/suppress, time-to-first-action, abandon rate, edit-before-send)_

- **Cadence:** _(e.g. per request real-time + weekly aggregate review)_
- **Pass bar:** _(numeric — e.g. ≥80% thumbs-up; regenerate rate ≤15%)_
- **Owner:** _(e.g. PM reviews weekly; on-call PM triages ≥2 thumbs-down on same intent within 24h)_

## Layer 2 · Human evaluation (system-level · highest fidelity)

**What gets sampled (with stratification):**
- _(e.g. 50 P0 triage runs / week, stratified across confidence buckets, 100% of hand-off cases included)_

- **Rubric:** see `06-evals/human-rubric.md`
- **Cadence:** _(e.g. weekly batch — Friday afternoon)_
- **Pass bar:** _(numeric — e.g. ≥4.0/5 mean on accuracy + safety; 0 critical safety fails)_
- **Who grades + disagreement protocol:** _(e.g. 2 graders + PM tiebreak per disagreement protocol)_

## Layer 3 · Automated assessment (component-level · highest scale)

**Golden set (versioned):**
- _(e.g. 200 anonymised P0 threads with PM-curated expected top-3 risks, versioned in `06-evals/golden-set/`, refreshed quarterly and after every major incident)_

**Eval checks (LLM-judge + format/safety):**
- _(LLM-judge scores accuracy against rubric)_
- _(Format check: valid markdown table with required columns)_
- _(Citation check: each risk cites a message index that exists)_
- _(Refusal check: contracts/legal language triggers refusal)_

- **Cadence:** _(every PR — CI gate + nightly cron)_
- **Pass bar:** _(numeric — e.g. ≥90% golden-set accuracy; 100% format/citation/refusal pass)_
- **Owner:** _(e.g. CI fails the PR; Eng owns format/citation; PM owns the accuracy bar)_

## PM execution plan · hard vs. soft gates

**Hard gates (auto-block release):**
- _(e.g. 0% PII leakage; 0 critical safety fails; citation-check fail ⇒ block)_

**Soft gates (require PM sign-off):**
- _(e.g. P99 latency >5s requires PM justification; off-brand tone flags >2% require PM review)_
