# Module 3 — Glossary

Module-specific terms from M3. See course-wide `Glossary.md` for general terms.

---

**AI PRD.** A traditional PRD plus three AI-specific sections: data corpus + retrieval strategy, eval plan, failure modes + guardrails.

**Architecture Decision Factors.** Five questions that pick your RAG architecture: data freshness, corpus size, query latency, update cadence, privacy / tenancy.

**Augmentation.** Step 3 of RAG — injecting retrieved chunks into the prompt.

**Chunk size.** How long each piece of indexed text is. 500–1500 tokens is the typical range.

**Chunking.** Breaking long documents into smaller pieces for indexing and retrieval.

**Context engineering.** The PM-owned discipline of assembling the data *around* the prompt so the model has the right ground truth.

**Context window.** The maximum number of tokens a model can consider in one call. 8k → 128k → 1M tokens, model-dependent.

**Corpus.** The body of text/data your RAG system retrieves from. Your `data corpus + retrieval strategy` section names it.

**Embedding.** A vector representation of a chunk of text used for similarity search.

**Embedding model.** The model that produces embeddings (text-embedding-3-large, Cohere embed-v3, voyage-3).

**Failure modes + guardrails.** The third new section of an AI PRD — a list of what can go wrong, each paired with a runtime check that blocks the failure.

**Generation.** Step 4 of RAG — the model's grounded response.

**Golden set.** A curated set of inputs with known-correct outputs, used to measure retrieval and generation quality (M6).

**Grounding.** Anchoring an AI output in retrieved data rather than the model's parametric memory.

**Hybrid retrieval.** Combining keyword search (BM25) with vector similarity for better recall.

**Index.** Step 1 of RAG — the chunk-and-embed pipeline that prepares your corpus for retrieval.

**Latency budget.** The maximum acceptable response time (p95 / p99). Drives RAG architecture choices.

**Multi-tenant.** A corpus shared across multiple customers/teams with access controls.

**p95 latency.** The 95th-percentile response time. Standard SLO target.

**Permissions (RAG).** The rule that retrieval respects user-level access (no one sees chunks they shouldn't).

**Reranker.** A second-pass model that re-orders the top-k retrieved chunks for better relevance. Adds cost + latency but improves accuracy.

**Retrieval.** Step 2 of RAG — fetching relevant chunks for a query.

**Retrieval strategy.** The combination of chunk size, top-k, hybrid/vector, and reranker. Specified in the AI PRD.

**Three Key RAG Trade-offs.** Cost / Speed / Accuracy.

**Top-k.** The number of chunks retrieved per query. Higher k = more context, more cost, more latency.

**Update cadence.** How often the index refreshes. Drives architecture choices (real-time vs. batch).

**Vector store.** The database that stores embeddings and serves nearest-neighbour search. Pinecone, Chroma, pgvector, Weaviate.
