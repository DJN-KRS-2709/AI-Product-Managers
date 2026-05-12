# Module 1 — Drive AI-First Execution with Prompting (Shareable Notes)

A faithful expansion of the Module 1 slides. Read in sequence. Use as revision or as a substitute if you missed the live session. Individual format throughout.

---

## 1. Course Introduction

This course is a six-module certification in AI Product Management. It is fully **individual**: no group breakouts, no team deliverables, no group presentations. Every exercise comes with three solo mechanics:

- **Self-review checklist** — bullets you tick against your own artifact.
- **AI-review prompt** — paste your artifact + a prompt into ChatGPT / Claude / Cursor for critique.
- **Async share** — commit to your `juno-pm/` repo fork and post the link in `#ai-pm-cohort`. The instructor responds in-thread within ~5 days.

Certification is based on your individual repo submission within 7 days of cohort end.

### The scenario

You are the AI PM at **RocketShip**, a hyper-growth B2B SaaS platform for Enterprise Data Teams. On paper the company is winning; in reality you are the bottleneck. P0 escalations stack up, support sits on thousands of tickets, sales velocity stalls. The org has innovation budget but **zero** for headcount.

You will spend the course designing and building **Juno PM** — an AI Associate PM that lives inside your existing tools (Slack, Notion, Jira) and handles three pillars:

1. **Synthesize Insights** — transform the multi-channel roar of transcripts, tickets, and calls into structured, evidence-backed clarity.
2. **Draft Specs** — turn raw findings into high-fidelity "Version 0.1" PRDs.
3. **Prioritize Risks** — flag unclear edge cases, technical debt, and risky assumptions.

The deliverable across the course is your **`juno-pm/` GitHub repo fork** — six folders (`01-prompting/` through `06-evals/`) plus a top-level `README.md` that is your one-page pitch.

---

## 2. The AI-First Product Mindset

The PM role is bending around a single technical fact: **AI outputs are non-deterministic.** Same input, variable output. Drift, hallucination, variance.

Every PM craft you know — specs, UX, QA, launch — has to bend around that. This table is the spine of the course. Each module reinforces one row.

| Traditional PM assumption | What AI broke |
|---|---|
| Outputs are deterministic | Outputs are probabilistic — drift, hallucination, variance |
| Spec is a doc | Spec is a doc + prompt + data corpus + eval set |
| UI is command-driven | UI is intent-driven and often invisible |
| Workflows are sequential | Workflows are agentic — branched, conditional, handed off |
| Ship + monitor with analytics | Ship + eval harness + human rubric + guardrails |

### The PM's dual role

You are the broker between probabilistic behaviour and human trust.

- **Inward** — translate non-determinism into product specs your team can build against (prompt, RAG, eval, guardrail).
- **Outward** — translate non-determinism into user expectations the product can honour (trust UX, confidence cues, escape hatches).

Engineers will not own the user-trust side. Designers will not own the eval side. You do.

### The PM's AI toolkit

Five tool categories every AI PM should have one of in their bookmarks:

| Category | Pick one | Use for |
|---|---|---|
| Prompt-to-prototype | Lovable, v0, Cursor | Build a working UI in minutes |
| LLM playground | OpenAI Playground, Anthropic Console | Tune prompts + hyperparameters |
| No-code agent builder | Langflow, n8n | Wire agents and tool calls |
| Eval / observability | LangSmith, Phoenix, Braintrust | Score, trace, regress |
| Repo + version control | GitHub | Your `juno-pm/` lives here |

> Use **`M1 - PM Toolkit Picker.html`** to commit your toolkit choices to `01-prompting/toolkit.md`.

---

## 3. The Anatomy of a High-Quality Prompt

Every production prompt declares **five elements**. If any is missing, output will drift.

1. **Context** — who the AI is, what system it lives in, what it knows.
2. **Task** — the explicit instruction (verb-first).
3. **Constraints** — must-not-do, format requirements, scope boundaries.
4. **Output format** — schema, length, structure (markdown / JSON / table).
5. **Examples** (few-shot, when useful) — 1–3 ideal input/output pairs.

> Use **`M1 - Prompt Anatomy Builder.html`** to assemble live. Copy the result as markdown to `01-prompting/anatomy-prompt.md` in your repo.

---

## 4. Hands-On Lab: Prompt-to-Prototype Your Copilot with Lovable

**Format: individual, 25 minutes.**

1. Open Lovable, sign in (free tier is enough).
2. Paste this seed prompt:

```
Build a web app called "Juno PM". It is the homepage for an AI Associate PM that lives inside Slack, Notion, and Jira. The homepage has:
- A hero strip with the tagline "Scale your judgment, not yourself"
- A three-column section explaining the pillars: Synthesize Insights, Draft Specs, Prioritize Risks
- A chat-style input at the bottom with placeholder text "Paste a wall of escalations..."
- A side panel showing the last 3 risks Juno flagged

Use a calm professional palette — deep navy, off-white, one accent color. No emojis.
```

3. Iterate **once** — change the UI shape, palette, or copy.
4. Copy the shareable URL.
5. Commit the URL to `01-prompting/README.md` in your `juno-pm/` fork.

**Goal:** a functional URL by end of timebox. Not a polished product.

---

## 5. Prompting as Product Configuration

Once you treat the prompt as **configuration**, every technique becomes obvious.

### The Prompting Strategy Matrix

| Technique | Use when |
|---|---|
| Zero-shot | Simple instruction; the model already knows the domain |
| Few-shot | You need a specific format or style — show 1–3 examples |
| Chain-of-thought | Multi-step reasoning required |
| System prompt + role | Persona, persistent guardrails, organisation context |

### Hyperparameters — the two PM dials

- **Temperature.** 0 ≈ deterministic. 1+ = creative. Spec for the job. Juno-as-risk-watchdog = low temperature. Juno-as-brainstorm-partner = higher.
- **Max tokens / response length.** Cap it. Long outputs hide failures. Short outputs force prioritisation.

Top-p, frequency penalty, presence penalty — nice-to-have, not must-have for PM-side decisions.

---

## 6. Individual Exercise — Configure Juno's System Prompt

**Format: individual, 30 minutes.** (This was previously a breakout group exercise. Now solo.)

This is the **M1 deliverable** for the final project.

### Steps

1. Open `M1 - System Prompt Configurator.html` in the `Modules/` folder.
2. Fill in: **persona**, **scope**, **guardrails**, **output format**, **refusal rules**.
3. Click **Copy as markdown** → save to `01-prompting/system-prompt.md` in your repo.

### Self-review checklist

- Persona names the role and the operating context.
- Scope boundaries explicit (e.g., "only act on Slack escalations tagged P0").
- At least 3 guardrails, including 1 explicit refusal rule.
- Output format declared (markdown, schema, length cap).
- An example for the trickiest case.

### AI-review prompt

Paste this into ChatGPT / Claude / Cursor along with your system prompt:

> *You are a senior AI PM reviewer. Critique this Juno PM system prompt against the 5-element prompt anatomy (Context, Task, Constraints, Output Format, Examples). Identify the three places it will drift in production. Suggest one specific change for each.*

### Async share

Commit, push, and post the link to your `01-prompting/system-prompt.md` in `#ai-pm-cohort` with a 1-paragraph reflection on what you cut, what you kept, and what you'd add if you had another hour.

---

## 7. The Optimization Decision Framework

Three levers. Cheapest first.

| Lever | Try when | Cost / time |
|---|---|---|
| **Prompt** | The model already knows the domain — behaviour needs tuning, not knowledge | Minutes. Almost free. |
| **RAG** | You need to ground the model in *your* data (M3) | Days. Real infra cost. |
| **Fine-tune** | Style/format/behaviour matters more than retrieval. Last resort. | Weeks. Real training cost. |

**If you can fix it with the prompt, do not build infra.**

### The Role of Fine-Tuning — mostly: don't

- Fine-tuning bakes behaviour into weights. Powerful, but inflexible.
- Fine-tunes drift: base models update, your fine-tune doesn't.
- Use when: format / tone / persistent behaviour at scale, and you have 1000+ high-quality examples.
- Do not use when: facts change weekly, you don't have an eval harness yet, or a system prompt + few-shot would work.

Most working PMs will never own a fine-tune. Know the decision criteria so you can push back when an engineer suggests it prematurely.

---

## 8. From PRDs to Prompts

In an AI-native team, the PRD is no longer the only source of truth. The full spec is now:

- The **PRD** (what & why)
- The **system prompt** (how the AI behaves) — M1
- The **data corpus + retrieval rules** (what it knows) — M3
- The **eval set** (how we know it's working) — M6

You will commit all four to your `juno-pm/` repo by M6.

---

## Key takeaways

1. Prompting is configuration, not chat.
2. Every prompt declares context, task, constraints, output format, examples.
3. Optimization order: prompt → RAG → fine-tune. Cheapest first.
4. You have a working Lovable URL for Juno + a committed system prompt.
5. Next: M2 — is this bet worth oxygen, and how autonomous can it be?

---

## Before Module 2 (~20 min)

- Skim **`Module 2 - Pre-Read.md`** (Three-Layer Model + AI Strategy One-Pager).
- Confirm your `juno-pm/` fork exists and contains the M1 artifacts (`system-prompt.md`, `anatomy-prompt.md`, `toolkit.md`, Lovable URL).
- Post your M1 reflection in `#ai-pm-cohort` if you haven't.
- Bring **one real AI bet from your day job** to M2. We will pressure-test it.

---

## Learning objectives (mapped to outcomes)

| LO | What you produced |
|---|---|
| Evaluate the strategic evolution of the PM role in the AI era | `01-prompting/README.md` reflection on the PM dual-role |
| Deconstruct the core components of a professional prompt | `01-prompting/anatomy-prompt.md` |
| Apply rapid prototyping techniques to validate AI product concepts | Lovable URL committed to `01-prompting/README.md` |
| Construct complex product behaviors using structured prompting strategies | `01-prompting/system-prompt.md` |
