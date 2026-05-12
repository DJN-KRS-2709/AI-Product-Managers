# Module 1 — Frameworks Reference Card

Quick-lookup card for the frameworks introduced in M1. Pair with `Module 1 - Notes (Shareable).md` for context.

---

## The AI-First Product Mindset table

The course's spine. Memorise it; reference it in every module.

| Traditional PM assumption | What AI broke |
|---|---|
| Outputs are deterministic | Outputs are probabilistic — drift, hallucination, variance |
| Spec is a doc | Spec is a doc + prompt + data corpus + eval set |
| UI is command-driven | UI is intent-driven and often invisible |
| Workflows are sequential | Workflows are agentic — branched, conditional, handed off |
| Ship + monitor with analytics | Ship + eval harness + human rubric + guardrails |

---

## The PM's dual role

- **Inward** — translate non-determinism into specs the team can build (prompt, RAG, eval, guardrail).
- **Outward** — translate non-determinism into user expectations the product can honour (trust UX, confidence cues, escape hatches).

---

## The PM's AI Toolkit (5 categories)

| Category | Pick one | Use for |
|---|---|---|
| Prompt-to-prototype | Lovable / v0 / Cursor | Build a working UI in minutes |
| LLM playground | OpenAI / Anthropic Console | Tune prompts + hyperparameters |
| No-code agent builder | Langflow / n8n | Wire agents and tool calls |
| Eval / observability | LangSmith / Phoenix / Braintrust | Score, trace, regress |
| Repo + version control | GitHub | Your `juno-pm/` lives here |

---

## Anatomy of a High-Quality Prompt (5 elements)

1. **Context** — who the AI is, what system it lives in, what it knows.
2. **Task** — the explicit instruction (verb-first).
3. **Constraints** — must-not-do, format requirements, scope boundaries.
4. **Output format** — schema, length, structure.
5. **Examples** (few-shot when useful) — 1–3 ideal pairs.

> If any element is missing, output drifts.

---

## Prompting Strategy Matrix

| Technique | Use when |
|---|---|
| Zero-shot | Simple instruction; model knows the domain |
| Few-shot | You need specific format/style — show 1–3 examples |
| Chain-of-thought | Multi-step reasoning |
| System prompt + role | Persona, persistent guardrails, org context |

---

## Hyperparameters (the two PM dials)

- **Temperature.** 0 ≈ deterministic; 1+ = creative. Spec for the job.
- **Max tokens.** Cap it. Long outputs hide failures.

Top-p, frequency penalty, presence penalty — nice to know, not must to spec.

---

## The Optimization Decision Framework

| Lever | Try when | Cost / time |
|---|---|---|
| **Prompt** | Behaviour needs tuning, not knowledge | Minutes. Almost free. |
| **RAG** | You need *your* data grounded (M3) | Days. Real infra cost. |
| **Fine-tune** | Style/format at scale; last resort | Weeks. Training cost. |

**Rule:** if you can fix it with the prompt, do not build infra.

---

## Reach-for-this-when…

| If you're asked… | Reach for… |
|---|---|
| "How do I write the system prompt?" | Anatomy of a High-Quality Prompt |
| "Should we add training data?" | Optimization Decision Framework |
| "What's the right temperature?" | Hyperparameters — pick a job, pick a number |
| "What's missing from our AI spec?" | The five-element prompt anatomy + the eval set + the data corpus |
| "What stack do I need?" | The PM's AI Toolkit (5 categories) |
