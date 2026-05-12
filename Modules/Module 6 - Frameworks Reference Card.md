# Module 6 — Frameworks Reference Card

The four frameworks for production AI quality.

---

## 1. The AI Evals Stack (3 layers)

Always all three.

| Layer | Volume | Fidelity | Cadence | Cost | Catches |
|---|---|---|---|---|---|
| **User feedback** | Every request | Lowest | Per request | Free | What users do (thumbs / regenerate / abandon) |
| **Human evaluation** | Sampled (~50/wk) | Highest | Weekly | High | Subtle quality (tone, completeness, citation correctness) |
| **Automated evals** | Every push + nightly | Mid | CI + nightly | Mid | Regressions, format breakage, factuality on golden set |

Anti-pattern: shipping with only one layer.

---

## 2. The Human Eval Rubric (5 components)

A rubric is shippable only if all five exist.

1. **Dimensions** — what you score (accuracy, tone, completeness, safety, citation correctness).
2. **Scale** — 1–5 or pass/fail, with anchor descriptions per scale point.
3. **Examples** — one example per scale point so graders calibrate.
4. **Disagreement protocol** — what happens when graders disagree (third grader, PM tiebreak, throw out).
5. **Sampling cadence** — how often, how many, by whom.

Real-world: Google Assistant uses a 5-point rubric across 4 dimensions, sampled at ~50 utterances/week per intent.

---

## 3. The AI Optimization Levers (in order)

When eval scores miss the bar:

| # | Lever | When | Cost |
|---|---|---|---|
| 1 | **Model** | Behaviour problem | Low → high |
| 2 | **Data** | Grounding / context problem | Mid |
| 3 | **Architecture** | Pattern mismatch | High |

Always try model + data before architecture. Architecture is the most expensive lever — keep it last.

---

## 4. The AI Governance Framework (4 buckets)

Operationalise risk on one page of the README.

| Bucket | Risks | Metrics | Owner |
|---|---|---|---|
| **Compliance** | GDPR, EU AI Act, sector regs | Audit-pass rate, DSR latency | Legal + PM |
| **Safety** | Toxic content, prompt injection, misuse | Safety eval pass-rate, incident count | Security + PM |
| **Reliability** | Uptime, fallback, graceful degradation | SLO attainment, fallback hit-rate | SRE + PM |
| **Reputation** | Public failure, social-media incident | Time-to-public-response, sentiment delta | Comms + PM |

Each bucket gets one row in your `README.md` PM Execution Plan.

---

## How they compose

1. **Evals Stack** gives you the score.
2. **Rubric** turns "the score" into something defensible.
3. **Levers** decide what you change when the score misses the bar.
4. **Governance** decides what you ship under what risk envelope.

The four together = the closing surface of an AI product manager.
