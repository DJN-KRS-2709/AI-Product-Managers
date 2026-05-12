# Module 6 — Measure AI Quality with Evals and Guardrails (Shareable Notes)

A faithful expansion of the Module 6 slides. Individual format throughout. M6 closes the course.

By the end of M6 you commit three artifacts to `06-evals/` and finalise the top-level `README.md` of your `juno-pm/` fork:

- `06-evals/eval-stack.md` — the three-layer eval stack
- `06-evals/human-rubric.md` — the human evaluation rubric
- `README.md` (top-level) — your PM Execution Plan, the certification submission

Optional async: `06-evals/loom.md` — link to your 3-minute Loom walkthrough posted in `#ai-pm-cohort`.

---

## 1. Production-Grade Evaluation Requirements

### Why vibe checks fail

"It looks good in five prompts" is the most common AI-PM trap.

- A handful of successful prompts is not a quality bar.
- Production traffic exposes long-tail inputs no demo ever touches.
- Models drift; prompts decay; corpora go stale.
- Without a harness, you can't tell whether your change made things better.

Vibe checks are the QA strategy of a team that has not shipped yet.

### The 95% Accuracy Trap

95% accuracy on a golden set sounds great. Until you do the math at production volume:

- 1,000 P0 thread triages per day × 5% wrong = 50 wrong outputs per day.
- Some of those 50 are *silently* wrong (no PM correction).
- A single high-stakes wrong output can outweigh the value of the other 950.

**Eval design is the product surface that decides whether you can ship.**

---

## 2. Measuring AI-Powered Product Outputs

### The AI Evals Stack — three layers, always all three

| Layer | Volume | Fidelity | What it tells you |
|---|---|---|---|
| **User feedback** | Highest | Lowest | What users do (thumbs, regenerate, abandon) |
| **Human evaluation** | Mid | High | What graders think (rubric scores) |
| **Automated evals** | Highest | Mid | What an LLM-judge or regression suite measures |

You need all three. They answer different questions. Most teams ship one layer; two if mature; three is what shippable AI products do.

### Building a Human Eval Rubric

Five components:

1. **Dimensions** — what you're scoring (accuracy, tone, completeness, safety, citation correctness).
2. **Scale** — 1–5 or pass/fail, with anchor descriptions per scale point.
3. **Examples** — one example per scale point.
4. **Disagreement protocol** — what to do when graders disagree.
5. **Sampling cadence** — how often, how many.

Real-world: Google Assistant uses a 5-point rubric across 4 dimensions, sampled at ~50 utterances/week per intent.

> Use **`M6 - Human Evaluation Rubric.html`** — spec 3–5 dimensions, write anchors, set cadence, export to `06-evals/human-rubric.md`.

### PM's Role in Evaluations

- PM owns the rubric and the golden set.
- PM defines the pass bar.
- PM decides the regression cadence.
- PM acts on eval data — model swap, data fix, architecture change.

If you delegate evals to QA, you have outsourced your product surface.

### Individual Exercise — Plan Juno's Eval Stack (25 min)

(Was previously a breakout group exercise. Now solo.)

1. Open `M6 - Eval Stack Designer.html`.
2. Plan all three layers: user feedback, human eval, automated.
3. For each layer, name: **volume, cadence, pass bar, who acts on it**.
4. Copy as markdown → `06-evals/eval-stack.md`.

#### Self-review checklist

- All three layers specified.
- Each has a numeric pass bar.
- Each has a cadence (per-request / weekly / nightly).
- Each names who acts on it (PM / on-call / automated).
- The Human eval layer references the rubric in `human-rubric.md`.

#### AI-review prompt

Paste your `eval-stack.md` + this into ChatGPT/Claude/Cursor:

> *You are an AI ops engineer. (a) For each of the three eval layers, is the cadence realistic given the volume? (b) Where is the weakest layer for catching the 95%-accuracy-trap failures? (c) What single addition would make this eval stack production-ready? Reply in 3 short paragraphs.*

---

## 3. AI Levers for Optimization

When eval scores miss the bar, three knobs in this order:

| Lever | Try when | Cost |
|---|---|---|
| **Model** | Behaviour is the issue | Low (swap) → high (fine-tune) |
| **Data** | Grounding / context is the issue | Mid — your time + ops |
| **Architecture** | Pattern doesn't fit the problem | High — engineering time |

Try model and data before architecture.

### Operationalising AI Risks — the Governance Framework

Four buckets, each with metrics + owners:

- **Compliance** — regulatory (GDPR, EU AI Act).
- **Safety** — content, prompt injection, misuse.
- **Reliability** — uptime, fallback paths, graceful degradation.
- **Reputation** — public failure scenarios + response playbook.

Each bucket gets a row in your PM Execution Plan (in the README).

---

## 4. Individual Exercise — Finalise Your Project Deliverables (20 min)

(Was previously a breakout group exercise. Now solo.)

1. Open `M6 - Final Project Deliverables Builder.html`.
2. The tool pulls together one structured page covering all 6 modules' artifacts:
   - System prompt (M1)
   - AI Strategy One-Pager + Decision Matrix (M2)
   - AI PRD with RAG architecture (M3)
   - AI user flow + trust-gap mitigations (M4)
   - Agent Workflow Spec (M5)
   - Eval stack + human rubric (M6)
3. Add your **Build Insights** reflection: 1 friction point, 1 key learning, 1 aha moment.
4. Copy as markdown → top-level `README.md` of your `juno-pm/` fork.
5. Commit, push.

The README is the **pitch**. Make it the kind of page you'd want to send to a board.

---

## 5. Async Showcase — Demo Your Juno Copilot

The original course had a 30-minute live group presentation. We've converted it to async, individual, optional:

1. Record a **3-minute Loom** walkthrough of your `juno-pm/` repo.
2. Hit: the bet, the system prompt, the user flow, the AWSpec, the eval stack.
3. Post the repo URL + Loom in `#ai-pm-cohort`.
4. Instructor responds in-thread with feedback within ~5 days.

Optional. Not required for certification. Encouraged for portfolio.

---

## 6. Certification

- **Submit:** the URL of your finalised `juno-pm/` GitHub repo.
- **Window:** within 7 days of cohort end.
- **Graded on:** Application of Concepts, Credibility & Reasoning, Clarity, Strategic Thinking.
- **Scale:** 1 — Poor (0–49), 2 — Sufficient (50–79), 3 — Excellent (80–100).

The submission is the repo URL, not a deck.

---

## Key takeaways

1. Vibe checks fail in production.
2. The AI Evals Stack has three layers. Always all three.
3. The Human Eval Rubric needs anchors + a disagreement protocol.
4. When eval scores miss the bar: model → data → architecture.
5. Eval is product surface. PMs own the bar.
6. Your README is the pitch. Ship it.

---

## After the cohort

- Submit your repo within 7 days for certification.
- Post your Loom (optional) in `#ai-pm-cohort`.
- Re-run the M6 AI-review prompt on every future AI bet — it's the six-lens evaluator we built across the course.
- Fork the course repo if you want to evolve the materials for your own org.

---

## Learning objectives (mapped to outcomes)

| LO | What you produced |
|---|---|
| Critique the limitations of informal testing | The "why vibe checks fail" reflection in `eval-stack.md` |
| Construct a multi-layered evaluation strategy | `06-evals/eval-stack.md` |
| Formulate a plan for operationalizing AI risks | Governance row in your `README.md` PM Execution Plan |
| Demonstrate AI product knowledge through strategic justification | Async showcase (Loom + repo URL in #ai-pm-cohort) |
