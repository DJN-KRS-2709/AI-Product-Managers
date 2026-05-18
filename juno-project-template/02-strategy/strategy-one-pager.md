# AI Strategy One-Pager — Juno Automated Prioritization

_Version 0.1 — placeholder. Replace via the **M2 AI Strategy One-Pager Builder** tool (Module 2 / Lab 2)._

Six sections. One page. The defensible doc that justifies the Juno bet to leadership and engineering.

---

## 1. Problem & Workflow

_The specific friction point + the bad decision Juno is explicitly preventing._

_(replace this with your Section 1 from the Builder)_

> Example seed: _The Problem — roadmap discussions at RocketShip are driven by the loudest voice in Slack rather than customer evidence. Prevention — Juno explicitly prevents 'opinion-driven prioritization': the bad decision of moving a feature up the backlog because of a strong post in #leadership instead of cited evidence._

---

## 2. Target Metrics

_The KPIs that prove the bet works. Measurable in ≤ 30 days. Which metric makes leadership say "don't touch it"?_

_(replace this with your Section 2 from the Builder)_

> Example seed: _Cycle time 2h → 30min (75% reduction). Reversal rate < 10% within a week. 90%+ of prioritised items have ≥ 2 cited sources._

---

## 3. Autonomy Level

_Assist / Copilot / Agent. State which level you're explicitly **avoiding** and why._

_(replace this with your Section 3 from the Builder)_

> Example seed: _Choice — Copilot. Avoiding Agent — letting Juno move sprint priorities autonomously is a one-way trust-erosion door._

---

## 4. Data & Model Approach

_Buy (LLM) / Ground (RAG) / Refine (Fine-tune). Define the shortcut you are intentionally **not** taking._

_(replace this with your Section 4 from the Builder)_

> Example seed: _Approach — Ground (RAG) over the RocketShip corpus. Avoiding generic LLM (Buy) — would hallucinate plausible priorities and invent customer signals._

---

## 5. Risks & Mitigations

_One scary one-way-door risk + the specific guardrail that protects trust. **One** risk, not a list._

_(replace this with your Section 5 from the Builder)_

> Example seed: _Risk — training-data lag: Juno over-weights enterprise escalations and under-weights SMB churn. Mitigation — hard 'evidence balance' eval gate; reject any priority list where < 20% of cited sources come from any one source type._

---

## 6. V1 Scope

_In/Out boundaries. Two specific OUT items prevent scope creep._

_(replace this with your Section 6 from the Builder)_

> Example seed: _In — ranking the existing backlog with cited evidence; surfacing under-cited items. Out — (1) hiring decisions, (2) customer-facing comms about deprioritisation. Both stay 100% with the PM._

---

## Self-review

- [ ] Section 1 names a single bad decision Juno is preventing
- [ ] Section 2 has a metric measurable in ≤ 30 days
- [ ] Section 3 names ONE level avoided + why
- [ ] Section 4 names ONE shortcut not taken + why
- [ ] Section 5 has ONE scary risk + a specific mitigation (not a list)
- [ ] Section 6 has ≥ 2 specific OUT items

## AI-review

Pasted my one-pager + the AI-review meta-prompt into _(ChatGPT / Claude / Cursor)_. Reviewer flagged: _(summary)_. I incorporated: _(what changed)_.

## Reference

Inline worked example available in the Builder tool: **Airbnb Smart Dispute Mediator** — same six-section anatomy, fully filled.
