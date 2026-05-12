# Module 3 — Frameworks Reference Card

Quick-lookup card for M3.

---

## Prompt → Context Engineering

| Prompt engineering | Context engineering |
|---|---|
| Words to the model | Data assembled *around* the prompt |
| Shared owner | **PM-owned** |
| Tunes behaviour | Grounds output in *your* reality |

---

## The RAG Process (4 steps)

1. **Index** — chunk, embed, store.
2. **Retrieve** — fetch top-k chunks for the query.
3. **Augment** — inject chunks into the prompt.
4. **Generate** — model responds, grounded.

---

## RAG implementation levers (PMs spec these, engineers tune)

- **Chunk size** — 500–1500 tokens.
- **Embedding model** — text-embedding-3, Cohere, voyage-3.
- **Vector store** — Pinecone / Chroma / pgvector / Weaviate.
- **Retrieval strategy** — top-k, hybrid (keyword + vector), reranker.

---

## What's New in an AI PRD (3 sections)

1. Data corpus + retrieval strategy
2. Eval plan (filled in M6)
3. Failure modes + guardrails

---

## Three RAG Trade-offs

| Trade-off | Lever | Watch |
|---|---|---|
| Cost | Embedding, storage, retrieval calls | $/query at scale |
| Speed | k, reranker, hybrid, parallelism | p95 latency |
| Accuracy | Chunk size, k, reranker, query rewrite | Eval score on golden set |

> Rule: right context at right time > more context.

---

## Architecture Decision Factors (5 questions)

1. Data freshness — how stale can context be?
2. Corpus size — fits in context window vs. retrieve?
3. Query latency budget
4. Update cadence — read- or write-heavy?
5. Privacy / tenancy — multi-tenant or per-user?

---

## PM Corpus-Readiness Checklist (5 items)

- Source identification
- Quality bar (freshness, accuracy, completeness)
- PII / sensitive-content handling
- Permissions (respect user-level access)
- Update cadence

---

## Reach-for-this-when…

| If you're asked… | Reach for… |
|---|---|
| "Should we use RAG?" | RAG Process (4 steps) — yes, if grounding in your data matters |
| "How big should chunks be?" | RAG implementation levers + accuracy trade-off |
| "What's the latency budget?" | Architecture Decision Factors (3rd question) |
| "What goes in the AI PRD vs. traditional PRD?" | The 3 new sections |
| "How do we control cost at scale?" | The three RAG trade-offs (cost row) |
| "Is our corpus ready?" | PM Corpus-Readiness Checklist |
