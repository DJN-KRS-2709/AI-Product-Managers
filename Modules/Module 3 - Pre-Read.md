# Module 3 — Pre-Read

10–15 minutes. Skim before the live session. This pre-read summarises the RAG fundamentals so M3 can move fast into the trade-offs and the PRD work.

---

## What you'll do in M3

Two artifacts committed to `03-rag-prd/`:

- `03-rag-prd/before-after-rag.md` — diagnostic showing Juno before vs. after grounding
- `03-rag-prd/ai-prd.md` — Juno's AI PRD with explicit RAG architecture (M3 deliverable)

---

## The shift M3 makes

You walked in with an AI Strategy One-Pager from M2. You walk out with an **AI PRD** — a real spec an engineer can scope from.

The single biggest change vs. a traditional PRD: you, the PM, own the **data corpus** and the **retrieval strategy**. Engineers will build the vector DB. They will not decide *what* gets indexed or *when* it refreshes. That's product judgement.

---

## What RAG actually is (in PM-speak)

Retrieval-Augmented Generation: before the model generates, you retrieve relevant snippets from a known corpus and inject them into the prompt as context. Three benefits, three trade-offs.

**Benefits**
- Hallucinations drop dramatically (the model now has facts to ground in).
- The output cites sources, which closes the M4 black-box trust gap.
- You can update the data without retraining anything.

**Trade-offs**
- **Cost** — embeddings, storage, retrieval calls per query.
- **Speed** — every retrieval step adds latency.
- **Accuracy** — the right context at the right time beats more context every time.

> **Rule:** more context is not always better. The point is the *right* context.

---

## The four steps in 60 seconds

1. **Index** — break docs into chunks (~1000 tokens), embed each chunk into a vector, store in a vector DB.
2. **Retrieve** — at query time, look up the top-k chunks closest in vector space.
3. **Augment** — paste those chunks into the prompt as context.
4. **Generate** — model produces the grounded response.

You do not need to operate any of this. You need to *specify* it: chunk size, top-k, reranker on/off, refresh cadence.

---

## What "AI PRD" means

A traditional PRD (problem, goal, users, scope, out of scope, open questions) plus three new sections:

1. **Data corpus + retrieval strategy** — what data, indexed how, retrieved how.
2. **Eval plan** — golden set, success bar, regression cadence. (M6 fills this in.)
3. **Failure modes + guardrails** — what can go wrong, what blocks it.

If your PRD doesn't have all three, you're shipping a probabilistic system with no idea how it will fail.

---

## Bring to M3

- Your `02-strategy/strategy-one-pager.md` from M2 (the bet you're now specifying).
- A guess at the corpus Juno needs: Slack #escalations? Notion product wiki? Jira tickets? Customer transcripts? The RocketShip strategy one-pager?
- The Lovable URL from M1 — the hands-on lab will ground it in a real corpus.

---

## Format reminder

100% individual. No groups. Self-review + AI-review + async share in `#ai-pm-cohort`.

---

## Optional reading (if you want more depth)

- Anthropic — *Best practices for context windows.*
- Microsoft Research — *Adaptive RAG: choosing retrieval depth dynamically.*
- LlamaIndex docs — *Hybrid search and reranking.*

You do not need these to pass M3. They're ammo for the AI-review prompt.
