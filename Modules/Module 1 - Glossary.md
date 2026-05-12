# Module 1 — Glossary

Module-specific terms introduced in M1. See the cross-cutting `Glossary.md` for course-wide definitions.

---

**Anatomy of a High-Quality Prompt.** The 5-element checklist every production prompt must declare: Context, Task, Constraints, Output Format, Examples.

**Chain-of-thought (CoT) prompting.** A technique that instructs the model to reason step-by-step before answering. Use for multi-step reasoning tasks.

**Configuration (prompting as).** Treating the prompt not as a conversation but as a settings file — values you tune deliberately for predictable behaviour.

**Deterministic system.** Same input → same output. SQL queries, regex, traditional APIs.

**Few-shot prompting.** Including 1–3 example input/output pairs in the prompt to anchor format and style.

**Fine-tuning.** Adjusting model weights on your data. Powerful but inflexible. The last-resort optimisation in the framework.

**Hyperparameters.** Model-runtime settings: temperature, top-p, max tokens, frequency penalty, presence penalty. The two PMs should know: **temperature** and **max tokens**.

**Lovable.** Prompt-to-prototype tool used in the M1 hands-on lab. You paste a brief, it returns a working UI URL.

**Max tokens.** Cap on response length. Spec it. Long outputs hide failures.

**Non-deterministic system.** Same input → variable output. Every modern LLM.

**Optimization Decision Framework.** The three-lever model for improving AI output: Prompt → RAG → Fine-tune. Cheapest first.

**PM's AI Toolkit.** Five categories every AI PM should have one tool in: prompt-to-prototype, LLM playground, no-code agent builder, eval/observability, repo + version control.

**Prompt engineering.** Crafting the text instructions to the model. PM-owned in an AI-native team.

**Prompting Strategy Matrix.** Zero-shot / Few-shot / Chain-of-thought / System prompt + role — the four techniques.

**Refusal rule.** An explicit "must-not" the AI obeys (e.g., "do not invent ticket IDs"; "if data is missing, ask for it"). Lives in the Constraints element of the prompt anatomy.

**System prompt.** The persistent instruction that sets the AI's persona, scope, and guardrails. Configured once; in effect for every conversation.

**Temperature.** A hyperparameter from 0 to 2 controlling output randomness. Low = consistent; high = creative.

**Token.** The unit a language model reads/writes. Roughly 0.75 words of English.

**Zero-shot prompting.** Instruction only, no examples. Use when the model already knows the domain.
