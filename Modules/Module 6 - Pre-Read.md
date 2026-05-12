# Module 6 — Pre-Read (15 min)

> The AI Evals Stack — why three layers, what each one catches, and the 95% accuracy trap.

This pre-read prepares you for the final module of the course. You'll close with three artifacts in `06-evals/` and a finalised top-level `README.md` for your `juno-pm/` fork — the certification submission.

---

## 1. The PM problem M6 solves

You've built Juno through five modules. The system prompt works on the demo cases. The RAG retrieves the right docs most of the time. The agent triages P0 threads. The UX has trust signals.

Now you have to answer:

- **Is this shippable?**
- **At what bar?**
- **What happens when it isn't?**
- **What do we monitor?**
- **What's our response when it fails?**

Without evals, every answer is "it feels right." That's not a defensible position to a CISO, a board, or a customer.

---

## 2. Why vibe checks fail

"It looks good in five prompts" is the most common AI-PM trap.

- A handful of successful prompts is not a quality bar.
- Production traffic exposes long-tail inputs no demo ever touches.
- Models drift; prompts decay; corpora go stale.
- Without a harness, you can't tell whether your change made things better.

Vibe-checked AI features pass the demo and lose the customer.

---

## 3. The 95% Accuracy Trap

95% accuracy on a golden set sounds great. Then you do the math at production volume.

- 1,000 P0 triages / day × 5% wrong = **50 wrong outputs / day**.
- Some are silently wrong — no PM correction signal.
- A single high-stakes wrong output can outweigh the value of the other 950.

The 5% is where the risk lives. **Eval design is the product surface that decides whether you can ship.**

---

## 4. The three-layer Eval Stack

Always all three.

| Layer | Volume | Fidelity | What it catches |
|---|---|---|---|
| **User feedback** | Highest | Lowest | What users *do* — thumbs, regenerate, abandon |
| **Human evaluation** | Mid | Highest | Subtle quality — tone, completeness, citation correctness |
| **Automated evals** | Highest | Mid | Regressions, format breakage, golden-set factuality |

Most teams ship with one layer. Two if mature. Three is what shippable AI products do.

---

## 5. What you'll do in M6

Three artifacts in `06-evals/` + the final README:

- `06-evals/eval-stack.md` — the three-layer eval plan
- `06-evals/human-rubric.md` — the human eval rubric
- `README.md` (top-level) — the PM Execution Plan
- *(optional)* `06-evals/loom.md` — 3-min walkthrough link, posted in `#ai-pm-cohort`

The README is the **pitch**. Make it the kind of page you'd want to send to a board.

---

## 6. Concepts to land before class

- **Evals layer mismatch.** Each layer answers a different question. Don't shop for one tool to cover all three.
- **Anchors.** A rubric without anchored examples is a survey, not an eval.
- **Pass bar.** PM owns the numeric threshold. Engineers don't.
- **Optimization order.** When you miss the bar, try model → data → architecture. Architecture last; it's the most expensive lever.
- **Eval is product surface.** It's not QA. It's how you ship.

---

## 7. Five-minute prep

1. Skim `Module 6 - Frameworks Reference Card.md` — the four frameworks of M6.
2. Glance at `M6 - Eval Stack Designer.html` — the tool you'll fill in class.
3. Have your `juno-pm/` repo open and pulled to latest.
4. Note the three areas of your AWSpec / PRD where you're least sure about quality — those are your highest-priority eval candidates.

You're ready. Go ship Juno.
