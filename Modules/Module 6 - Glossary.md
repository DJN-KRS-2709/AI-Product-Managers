# Module 6 — Glossary

The terms you'll hear in M6.

**AI Evals Stack.** A three-layer evaluation system — user feedback + human evaluation + automated evals. All three together cover the production quality surface.

**Anchor.** A description tied to a specific scale point on a rubric ("3 = factually correct but missing one source"). Anchors are how graders calibrate.

**Automated eval.** A regression suite, LLM-judge, or programmatic check that runs on every push or nightly against a golden set.

**Build Insights.** The reflection you write at course-end: 1 friction, 1 learning, 1 aha. Lives in the README.

**Cadence (eval).** How often an eval runs. Per request / weekly / nightly / pre-release.

**Certification submission.** The URL of your finalised `juno-pm/` GitHub repo. Submitted within 7 days of cohort end.

**Compliance bucket.** Governance bucket covering regulatory risk (GDPR, EU AI Act).

**Disagreement protocol.** Rule that resolves grader disagreement on a rubric (third grader, PM tiebreak, throw out).

**Eval harness.** The code + data that runs your automated evals on every push.

**Eval Stack Designer.** The M6 tool — `M6 - Eval Stack Designer.html` — that produces `06-evals/eval-stack.md`.

**Final Project Deliverables Builder.** The M6 tool — `M6 - Final Project Deliverables Builder.html` — that assembles all six modules' artifacts into the top-level `README.md`.

**Golden set.** The fixed set of inputs you regress every model / prompt / architecture change against.

**Governance framework.** Four buckets — compliance, safety, reliability, reputation — that operationalise AI risk.

**Human eval.** Mid-volume, high-fidelity evaluation by trained graders using a rubric.

**Human Evaluation Rubric.** The M6 tool — `M6 - Human Evaluation Rubric.html` — that produces `06-evals/human-rubric.md`.

**LLM-judge.** Using an LLM (often a stronger one) to grade another LLM's outputs against a rubric.

**Optimization levers.** Three knobs to pull when eval scores miss the bar — model, data, architecture, in that order.

**Pass bar.** The numeric threshold an eval layer must hit to ship. Owned by the PM.

**PM Execution Plan.** The closing section of your `README.md` — where Juno is, what ships next, what you watch, what blocks shipping.

**Reliability bucket.** Governance bucket covering uptime, fallback, graceful degradation.

**Reputation bucket.** Governance bucket covering public-failure scenarios and response playbooks.

**Rubric.** A scored evaluation form. Five components: dimensions, scale, examples, disagreement protocol, sampling cadence.

**Safety bucket.** Governance bucket covering content safety, prompt injection, misuse.

**Sampling cadence.** How many items, how often, get sent to human graders.

**Three-layer eval stack.** See AI Evals Stack.

**Trace.** A single observability record of one AI invocation — input, retrieved context, tool calls, output, latency, tokens, cost.

**User feedback.** Highest-volume, lowest-fidelity eval layer. Thumbs / regenerate / abandon / explicit feedback.

**Vibe check.** Informal "it looks good in five prompts" testing. Not an eval strategy.

**95% accuracy trap.** The fallacy that 95% accuracy is good enough; at production volume, the 5% is where real risk lives.
