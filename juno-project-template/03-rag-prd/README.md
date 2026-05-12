# 03 — RAG / AI PRD (Module 3)

Commit one artifact here:

- `prd.md` — from **M3 - AI PRD Builder.html**, with RAG decisions from **M3 - RAG Architecture Decider.html**

> **Tools:** `M3 - RAG Architecture Decider.html`, `M3 - AI PRD Builder.html`.

## Self-review checklist (M3)

- All three new AI PRD sections present: **data corpus + retrieval strategy**, **eval plan**, **failure modes + guardrails**
- The RAG decision is justified against cost / speed / accuracy
- A failure mode exists for *each* hallucination type you can imagine
- The eval plan is testable (not "we'll measure quality")
- Retrieval strategy specifies chunking + top-k + similarity threshold

## AI-review prompt

> *You are a staff engineer reading this AI PRD. (a) Could you scope a sprint from it without further conversation? (b) Where does the data corpus section leave ambiguity? (c) Of the failure modes listed, which one is missing a concrete guardrail? Reply in 3 short paragraphs.*
