# Module 2 — Validate AI Opportunities and Technical Feasibility (Shareable Notes)

A faithful expansion of the Module 2 slides. Read in sequence. Individual format throughout.

By the end of this module you will commit two artifacts to your `juno-pm/` fork:

- `02-strategy/decision-matrix.md` — Three-Layer mapping + Job × Risk × Autonomy + AI Solution Decision Matrix scores
- `02-strategy/strategy-one-pager.md` — the seven-block one-page justification

---

## 1. The traditional assumption M2 breaks

Traditional PM ranks features by ICE / RICE / WSJF and ships. AI breaks this:

- The same feature can be a *fake-good* (great demo, dies in production) or a *boring killer* (looks dull, prints money).
- The right autonomy level is a strategic decision, not an engineering one.
- Bets fail more often than they succeed — your job is to kill bad bets fast and cheap.

**You don't have feature lists. You have bets.**

---

## 2. Where does AI actually fit?

### Fake-Good vs. Boring Killer

| Fake-Good | Boring Killer |
|---|---|
| Demos brilliantly | Looks dull on a slide |
| No clear value frame | Ladders to a real value frame |
| Loses to a platform feature in 6 months | Survives a 3x cost stress test |
| "Generate a summary" | "Cut on-call escalations by 40%" |

A feature is a *boring killer* only if it passes both filters:

1. Does it ladder to a real value frame?
2. Would it survive a 3x cost stress test?

### The Four AI Value Propositions

Every shippable AI bet ladders to one of these:

- **Cost reduction** — replace human labour, lower OPEX per unit of work.
- **Revenue generation** — new product surfaces, new willingness to pay.
- **Risk mitigation** — catch what humans miss (compliance, fraud, escalation).
- **User delight** — anticipate intent, reduce friction, surprise positively.

If your AI bet doesn't ladder cleanly to one of these, it's a fake-good.

### The Three-Layer Model

PMs own three layers. Most fail at the Mechanic layer.

| Layer | Question | For Juno PM |
|---|---|---|
| **Strategy** | Which bet? Why now? What value frame? | Risk mitigation — RocketShip is in Signal Collapse |
| **Mechanic** | What does the product actually do? | Synthesize + draft + prioritize, inside Slack/Notion/Jira |
| **Implementation** | How is it built? | System prompt + RAG over RocketShip corpus + bounded agent |

---

## 3. Balancing AI Bets with Autonomy

### Jobs × Risk × Autonomy

The strategy lens for choosing how independently an AI feature can act.

- **Job** — what task is the AI doing?
- **Risk** — what's the cost of a wrong output? (reputation, regulation, revenue)
- **Autonomy** — how independently can it act?

As autonomy increases, the cost of an error skyrockets. **High-risk jobs cap at Draft.**

### The Autonomy Levels

| Level | Behaviour | Where Juno's pillars live |
|---|---|---|
| **Suggest** | AI proposes; human decides | Prioritise Risks (early — until trust is built) |
| **Draft** | AI drafts v0.1; human edits + approves | Draft Specs (medium-risk, must be PM-edited) |
| **Execute** | AI acts; human reviews after | Synthesize Insights (low-risk, high-volume) |
| **Operate** | AI runs long horizons | Not appropriate for Juno's risk profile |

For Juno: each pillar lives at a different autonomy level. That's healthy.

### Individual Exercise (Was breakout group, now solo) — Map Juno's Strategic Bet (25 min)

This is the first M2 deliverable.

1. Open `M2 - Three-Layer Model Mapper.html`.
2. For each Juno pillar (Synthesize / Draft / Prioritize): score Job × Risk; place at Suggest / Draft / Execute / Operate.
3. Copy as markdown → `02-strategy/decision-matrix.md` (Three-Layer + autonomy section).
4. **Self-review checklist** (on the tool):
   - Each pillar has a clear Job statement.
   - Risk is explicit (financial / reputational / regulatory).
   - The Autonomy level is justified, not aspirational.
   - At least one pillar is at a lower autonomy than feels comfortable.
5. **AI-review prompt:**

> *You are a senior AI PM reviewer. For each of these three Juno pillars, evaluate whether the assigned autonomy level matches the Job × Risk score. Identify any pillar that has been over-granted autonomy. Suggest one guardrail per pillar that would let it stay at its current autonomy level safely.*

6. **Async share:** commit, push, post the link in `#ai-pm-cohort`.

---

## 4. Making Product Decisions Based on Technical Needs

### The AI Solution Decision Matrix

Pressure-test every proposed AI bet on five axes, scored 1–5.

| Axis | Question | Score 1 (red flag) | Score 5 (boring killer) |
|---|---|---|---|
| **Value clarity** | Does it ladder to a value frame? | Vague | Quantified outcome ($$ saved / leads gained / risk cut) |
| **Technical feasibility** | Can current models actually do this well enough? | Novel research required | Standard pattern, off-the-shelf |
| **Data availability** | Do you have / can you get the corpus? | No corpus | Clean labelled corpus exists |
| **Risk tolerance** | Can you tolerate wrong outputs? | Regulatory / reputational | Internal, reversible |
| **Strategic fit** | Does it earn company oxygen? | Pet project | Directly serves a top-3 priority |

**Score &lt;3 average = don't ship. Score 4+ on all five = boring killer.**

> Use **`M2 - AI Solution Decision Matrix.html`** — sliders, live verdict, export to `02-strategy/decision-matrix.md` (matrix section).

### Responsible AI as Strategic Guardrails

Risk is a strategic lever, not a checklist. Four buckets:

- **Compliance** — regulatory (GDPR, EU AI Act, sector-specific).
- **Safety** — content, prompt injection, misuse.
- **Reliability** — uptime, fallback paths, graceful degradation.
- **Reputation** — public failure scenarios + response playbook.

Each guardrail you commit to is a sales asset for enterprise buyers — not just a cost.

---

## 5. The AI Strategy One-Pager

Seven blocks. One page. The second M2 deliverable.

1. **The bet** — one sentence, with the value frame it ladders to.
2. **The user / job** — who and what.
3. **The mechanic** — what the product actually does.
4. **The autonomy** — Suggest / Draft / Execute / Operate.
5. **The technical approach** — prompt / RAG / fine-tune / agent.
6. **The risk + guardrail** — what can go wrong + how you block it.
7. **The success metric** — how you'll know it works (measurable in 30 days).

### Individual Exercise (Was breakout group, now solo) — Build Juno's AI Strategy One-Pager (30 min)

1. Open `M2 - AI Strategy One-Pager Builder.html`.
2. Fill in the 7 blocks for Juno PM.
3. Copy as markdown → `02-strategy/strategy-one-pager.md`.
4. **Self-review checklist** (on the tool):
   - The bet is one sentence, naming a value frame and a quantified outcome.
   - The mechanic answers "what does this product do?" in a way a non-PM understands.
   - The autonomy level is justified against Job × Risk.
   - The technical approach ladders to the M1 Optimization Framework (prompt → RAG → fine-tune).
   - The success metric is measurable in the first 30 days.
5. **AI-review prompt:**

> *You are the CFO of RocketShip. Read this AI Strategy One-Pager and challenge it. (a) Is the success metric specific enough to defund the bet if missed? (b) Is the autonomy level appropriate for the risk? (c) Is the technical approach the cheapest path? (d) What's the single weakest block? Reply in 5 bullets.*

6. **Async share:** commit, push, post the link in `#ai-pm-cohort` with a 1-paragraph reflection on how the AI-review changed your one-pager.

---

## Key takeaways

1. Most AI features are fake-good. Use the four value frames to filter.
2. Strategy / Mechanic / Implementation — own all three.
3. Autonomy is a strategic decision. Job × Risk → Autonomy.
4. The AI Solution Decision Matrix is your reusable rubric for any future bet.
5. The AI Strategy One-Pager fits on a page and survives a board challenge.

---

## Before Module 3 (~20 min)

- Skim **`Module 3 - Pre-Read.md`** (context engineering + RAG primer).
- Identify what corpus Juno would need to do its job for RocketShip. (Slack history? Notion docs? Jira metadata? Support tickets? Strategy one-pagers?)
- Post your `02-strategy/` links in `#ai-pm-cohort` if you haven't.

---

## Learning objectives (mapped to outcomes)

| LO | What you produced |
|---|---|
| Evaluate AI opportunities within a product ecosystem | The bet block of `strategy-one-pager.md` + four-value-frame filter |
| Analyze the relationship between risk and model independence | The autonomy section of `decision-matrix.md` |
| Formulate product decisions using the AI Solution Decision Matrix | The 5-axis scores in `decision-matrix.md` |
| Synthesize complex technical and strategic data into a concise technical one-page document | `strategy-one-pager.md` |
