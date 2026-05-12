# Module 4 — Glossary

Module-specific terms from M4.

---

**AI Iceberg.** The mental model that the UI is the tip; everything else (retrieval, tools, memory, eval, guardrails) is underwater. PMs spec the iceberg.

**AI user flow.** A 7-node specification of how an AI feature moves from trigger to confirm/correct.

**Anticipatory UX.** UI that infers user intent and acts proactively rather than waiting for input.

**Audit trail.** The visible record of background AI actions, surfaced so the user can review and override.

**Background automation.** UX treatment where the AI does work without showing itself, but logs everything for review.

**Black-box gap.** The trust gap arising when the user cannot see *why* the AI decided. Closed with reasoning, citations, "show your work."

**Capture (node).** Step 2 of an AI user flow — gathering context the system needs.

**Confidence cue.** A visual signal of how certain the AI is. Closes part of the hallucination gap.

**Confirm / Correct (node).** Step 7 of an AI user flow — how the user steers, accepts, or overrides.

**Control gap.** The trust gap arising when the user cannot steer or stop. Closed with undo, edit, regenerate, "don't suggest this again."

**Escape hatch.** Any UI affordance that lets the user opt out of the AI path mid-flow.

**Hallucination gap.** The trust gap arising because confident-looking output may be wrong. Closed with confidence cues, source links, escape hatches.

**HR Agent example.** The reference user flow walkthrough used in M4 to illustrate the seven nodes.

**Inline assist.** UX treatment where the AI shows up at the exact moment of decision. Used for revenue value frames.

**Intelligence tax.** The extra latency or cognitive load the user must endure for AI value. Spec it down.

**Intent-driven UI.** UI that infers what the user wants and acts; opposite of command-driven UI.

**Invisible by design.** The AI-native UX default — anticipates intent, acts at the right moment, never sits at a chat box.

**Proactive flag.** UX treatment where the AI surfaces a finding the user didn't ask for. Used for risk value frames.

**p95 latency.** 95th-percentile response time. Standard SLO; spec it explicitly for AI features.

**Reason (node).** Step 4 of an AI user flow — the model call that decides.

**Reasoning surface.** UI element that shows the AI's chain of thought. Closes the black-box gap.

**Retrieve (node).** Step 3 of an AI user flow — pulling relevant context from the corpus.

**Source link.** A clickable citation pointing to the underlying data. Closes part of the hallucination gap.

**Streaming output.** Showing tokens as they're generated. Single biggest perceived-latency win.

**Surface (node).** Step 6 of an AI user flow — what the user sees.

**Three trust gaps.** Black-box, Hallucination, Control.

**Tip (of the iceberg).** The visible part of the AI user flow — Trigger, Surface, Confirm/Correct.

**Trigger (node).** Step 1 of an AI user flow — what initiates the flow.

**Underwater (of the iceberg).** The invisible part of the AI user flow — Capture, Retrieve, Reason, Act, Log, Guardrails, Fallback.

**UX treatment.** The choice of how AI shows up in the UI. Mapped from value frame.
