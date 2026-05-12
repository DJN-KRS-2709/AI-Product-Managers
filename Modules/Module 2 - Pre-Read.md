# Module 2 — Pre-Read

10–15 minutes. Skim before the live session. M2 builds on M1's Optimization Decision Framework — if that wasn't crisp, re-read it in `Module 1 - Frameworks Reference Card.md`.

This pre-read is a condensed version of the original `AI Product Management M2 - Three-Layer Model & AI Strategy` reference, rewritten for the individual format.

---

## What you'll do in M2

By the end of the 2-hour session you will commit two artifacts to `02-strategy/` in your `juno-pm/` fork:

- `02-strategy/decision-matrix.md` — Three-Layer mapping + Jobs × Risk × Autonomy + AI Solution Decision Matrix scores
- `02-strategy/strategy-one-pager.md` — the seven-block one-page justification

These are the second and third pieces of your final repo (after M1's `system-prompt.md`).

---

## The shift M2 makes

You walked into M1 with a feature mindset. You walk out of M2 with a **bet mindset**.

- A feature is shippable; a bet is testable.
- A feature is approved; a bet is funded.
- A feature ships when it works; a bet ships when its decision matrix score crosses the bar.

This re-framing is more honest. Most AI features fail. The PM's job is to kill the bad ones fast and cheap, and to justify the good ones in a way leadership can sign off on.

---

## Four AI Value Propositions

Every shippable AI bet ladders to one of these:

- **Cost reduction** — replace human labour.
- **Revenue generation** — create new product surfaces.
- **Risk mitigation** — catch what humans miss.
- **User delight** — anticipate intent, reduce friction.

If your bet doesn't ladder cleanly to one of these, it's a *fake-good* — flashy demo, no business case.

For **Juno PM** at RocketShip, the primary value frame is **Risk Mitigation** (catching escalations that would otherwise drop), with secondary **Cost Reduction** (no new headcount needed). Knowing this matters: the success metric and the autonomy level both flow from the value frame.

---

## The Three-Layer Model

PMs own three layers. Most teams operate at the Strategy and Implementation layers and skip the Mechanic.

| Layer | Question | Most common failure |
|---|---|---|
| Strategy | Which bet? Why now? Value frame? | Skipped — "AI for AI's sake" |
| Mechanic | What does the product actually *do*? | Hand-waved — "an AI assistant" |
| Implementation | How is it built? | Over-engineered — fine-tunes when prompts would work |

Spend the most time at the Mechanic layer. That's where the product judgement lives.

---

## Jobs × Risk × Autonomy

For any AI feature, the autonomy you grant is a function of:

- **Job** — what task is the AI doing?
- **Risk** — what's the cost of a wrong output?
- **Autonomy** — how independently can it act? (Suggest → Draft → Execute → Operate)

**Rule:** as autonomy increases, the cost of an error skyrockets. High-risk jobs cap at *Draft*.

For Juno:
- *Synthesize insights* — low risk, high volume → can earn *Execute*.
- *Draft specs* — medium risk, must be PM-edited → *Draft*.
- *Prioritize risks* — high stakes, low trust at first → *Suggest*, graduating to *Draft* once you've shipped enough cycles.

Different autonomy per pillar is healthy. Don't pick one autonomy for the whole product.

---

## The AI Solution Decision Matrix (preview)

The matrix scores every bet 1–5 on five axes. You'll do the scoring live in M2 using `M2 - AI Solution Decision Matrix.html`. Pre-read just enough to recognise the axes:

1. Value clarity
2. Technical feasibility
3. Data availability
4. Risk tolerance
5. Strategic fit

Verdict: <3 average = don't ship. 4+ on all five = boring killer.

---

## Format reminder

100% individual. No groups. Every M2 exercise produces an artifact you commit, self-review, AI-review, and share in `#ai-pm-cohort`.

---

## Bring to M2

- Your `01-prompting/system-prompt.md` from M1 (the bet you're configuring).
- **One real AI bet from your day job** (set up in the M1 pre-read). You'll run it through the Decision Matrix in parallel to Juno.
- A guess at what value frame Juno serves (Cost / Revenue / Risk / Delight). We'll pressure-test it.
