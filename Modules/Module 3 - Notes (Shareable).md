# Module 3 — Improve AI Product Requirements with RAG Architecture (Shareable Notes)

A faithful expansion of the Module 3 slides. Individual format throughout.

By the end of this module you will commit two artifacts to `03-rag-prd/`:

- `03-rag-prd/before-after-rag.md` — diagnostic from the hands-on lab
- `03-rag-prd/ai-prd.md` — Juno's AI PRD with explicit RAG architecture (the M3 deliverable)

---

## 1. The Power of Context and Context Engineering

The big shift in M3:

| Prompt engineering | Context engineering |
|---|---|
| Words to the model | Data assembled *around* the prompt |
| Shared between engineer and PM | **PM-owned** |
| Tunes behaviour | Grounds output in *your* reality |

Engineers own retrieval mechanics. **PMs own what should be retrieved and why.** If you don't take this, no one does.

---

## 2. Overview: The RAG Process

Retrieval-Augmented Generation in 4 steps:

1. **Index** — chunk your corpus, embed each chunk, store in a vector DB.
2. **Retrieve** — at runtime, fetch relevant chunks for the query.
3. **Augment** — inject retrieved chunks into the prompt as context.
4. **Generate** — model responds, grounded in your data.

Reduces hallucination. Adds cost + latency. The PM trade-off is **what to retrieve and when**.

### How RAG works in practice

- **Chunking** — break long docs into 500–1500 token chunks. Smaller = more precise; larger = more context.
- **Embedding** — convert each chunk to a vector. Pick a model (OpenAI text-embedding-3, Cohere, voyage-3).
- **Vector store** — Pinecone, Chroma, pgvector, Weaviate. PM-irrelevant unless cost matters.
- **Retrieval strategy** — top-k similarity, hybrid (keyword + vector), reranker on top of k.

You do not need to operate the vector DB. You need to know the levers exist.

---

## 3. Hands-On Lab: Improve Juno's Capabilities With RAG (25 min, individual)

1. Open your Juno Lovable prototype (from M1).
2. Ground Juno in the **RocketShip Strategy One-Pager** corpus — paste the doc into Lovable's context, or use the lab's seed corpus.
3. Ask Juno: *"What are the top 3 risks for our Q3 enterprise tier launch, with citations?"*
4. Compare the answer **before** grounding vs. **after**.
5. Save both answers in `03-rag-prd/before-after-rag.md`.

**Goal:** see *"no longer guessing, now citing."*

---

## 4. Mapping RAG To Your AI PRD

### What's new in an AI PRD?

A traditional PRD plus **three new sections**:

1. **Data corpus + retrieval strategy** — what data, indexed how, retrieved how.
2. **Eval plan** — golden set, success bar, regression cadence (M6 fills this).
3. **Failure modes + guardrails** — what can go wrong, what blocks it.

Skip these and you ship a probabilistic system with no idea how it will fail.

### The Three Key RAG Trade-offs

| Trade-off | Lever | Watch |
|---|---|---|
| **Cost** | Embedding model size, storage volume, retrieval calls/query | $/query at production scale |
| **Speed** | k, reranker on/off, hybrid retrieval, parallelism | p95 latency budget |
| **Accuracy** | Chunk size, retrieval k, reranker quality, query rewriting | Eval score on golden set (M6) |

**The right context at the right time beats more context every time.**

---

## 5. RAG Costs, Control, and Trade-offs

### Architecture Decision Factors (5 questions)

1. **Data freshness** — how stale can context be? (Seconds / hours / days)
2. **Corpus size** — fits in context window vs. must be retrieved?
3. **Query latency budget** — how fast must this return?
4. **Update cadence** — read-heavy or write-heavy?
5. **Privacy / tenancy** — multi-tenant or per-user corpus?

For Juno PM at RocketShip: stale up to 1 hour is OK; corpus too big to fit in context; p95 ≤4s; write-heavy on tickets; per-team tenancy.

> Use **`M3 - RAG Architecture Decider.html`** — answer the five questions, get a recommended architecture (chunk size, retrieval, reranker, refresh cadence). Export to your PRD.

### Tokens and context windows — the hard ceiling

- Model context windows: 8k → 128k → 1M tokens.
- Cost per million tokens × usage volume = your AI margin line.
- Bigger windows are **not** free. Latency and "needle in a haystack" recall both degrade with size.

The 1M-token era doesn't kill RAG. It changes the trade-off.

### Data Preparation — the PM corpus-readiness checklist

- **Source identification** — which docs, channels, tickets, transcripts?
- **Quality bar** — minimum freshness, accuracy, completeness.
- **PII / sensitive-content handling** — redact, exclude, or pseudonymise.
- **Permissions** — does the corpus respect user-level access?
- **Update cadence** — how often does the index refresh?

---

## 6. Individual Exercise — Specify Juno's RAG Architecture in Your AI PRD (30 min)

This is the M3 deliverable. (Was previously a breakout group exercise. Now solo.)

1. Open `M3 - AI PRD Builder.html`.
2. Carry over the bet / mechanic / autonomy from your M2 one-pager.
3. Fill the **Data corpus + retrieval strategy** section using output from the RAG Architecture Decider.
4. Fill the **Failure modes + guardrails** section.
5. Leave the **Eval plan** as a stub — M6 fills it.
6. Copy as markdown → `03-rag-prd/ai-prd.md`.

### Self-review checklist

- Data corpus section names **specific** sources (not "internal docs").
- Retrieval strategy specifies chunk size, top-k, and rerank on/off.
- Failure modes lists **at least 3 concrete** scenarios.
- Each failure mode has a **paired guardrail** (refusal, citation, escalation).
- Eval plan stub points to M6.

### AI-review prompt

Paste your `ai-prd.md` + this into ChatGPT / Claude / Cursor:

> *You are a staff engineer reviewing an AI PRD. (a) Is the data corpus specific enough to scope an indexing job from? (b) Is the retrieval strategy a defensible choice given the architecture decision factors? (c) Of the failure modes listed, which one is most likely to bite Juno first in production, and is its guardrail strong enough? Reply in 4 short paragraphs.*

### Async share

Commit, push, and post the link to `03-rag-prd/ai-prd.md` in `#ai-pm-cohort` with a 1-paragraph reflection on which failure mode you nearly missed.

---

## Key takeaways

1. Prompt engineering ends where context engineering begins. PMs own context.
2. An AI PRD has 3 new sections vs. a traditional PRD.
3. The right context at the right time beats more context.
4. RAG trade-offs: cost / speed / accuracy.
5. You now have a real AI PRD for Juno with explicit architecture choices.

---

## Before Module 4 (~20 min)

- Skim **`Module 4 - Pre-Read.md`** (AI-UX trust gaps + iceberg).
- Pick a real AI product whose UX you find clunky. Bring one screenshot to M4.
- Post your `03-rag-prd/ai-prd.md` link in `#ai-pm-cohort` if you haven't.

---

## Learning objectives (mapped to outcomes)

| LO | What you produced |
|---|---|
| Evaluate the strategic shift from prompt engineering to context engineering | `03-rag-prd/before-after-rag.md` |
| Apply retrieval-augmented generation to enhance model intelligence | Grounded Juno prototype (hands-on lab) |
| Construct an AI PRD that incorporates retrieval-augmented generation | `03-rag-prd/ai-prd.md` |
| Formulate technical architecture decisions based on product constraints | RAG Architecture Decider output in `ai-prd.md` |
