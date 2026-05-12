# Juno PM — Eval Stack

_Version 0.1 — placeholder. Replace via M6 Eval Stack Designer._

## Layer 1 · User feedback

- **Signals captured:** _(thumbs / regen / suppress / freetext)_
- **Cadence:** _(per request)_
- **Pass bar:** _(numeric — e.g., ≥80% thumbs-up)_
- **Who acts on it:** _(PM / on-call PM)_

## Layer 2 · Human evaluation

- **What gets sampled:** _(volume + stratification)_
- **Rubric:** see `06-evals/human-rubric.md`
- **Cadence:** _(weekly batch)_
- **Pass bar:** _(numeric — mean score across dimensions)_
- **Who grades:** _(graders + tiebreaker)_

## Layer 3 · Automated evals

- **Golden set:** _(size, location, refresh cadence)_
- **Eval checks:** _(LLM-judge, format, citation, refusal)_
- **Cadence:** _(per PR + nightly)_
- **Pass bar:** _(numeric — golden-set accuracy + format/citation/refusal)_
- **Who acts on it:** _(CI fails the PR; PM owns the bar)_
