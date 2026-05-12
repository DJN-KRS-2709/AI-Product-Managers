# AI Product Management Certification — Course Architecture

**Product School | 6 modules × ~2 hours | Working PMs going AI-native | Individual format**

---

## Positioning

This is the certification for the PM whose roadmap is being eaten by a flood of signals — escalations, transcripts, tickets, exec asks — and who needs to *scale their own product judgment* with AI, not just slap a "summarize" button on a feature.

Where other AI PM courses teach you **about** AI, this one makes you **build** the copilot you'd actually use Monday morning — `Juno PM` — across all six modules, with one tangible artifact per module, all committed to your own GitHub repo.

We learn from the best material out there (Reforge, Maven, top Substacks, Product School's strategy course) and synthesize it into one coherent arc with our own opinionated take.

---

## Target Audience

Working product managers who already understand AI fundamentals (prompts, tokens, RAG-as-a-concept, agents-as-a-concept). They've shipped at least one AI feature or are about to. They are not founders, not researchers, not first-time PMs.

They take this course because they need a system — not vocabulary — for executing AI-native PM work: prompting as configuration, validating bets, specifying with RAG, designing AI-native UX, deploying agents, and proving quality with evals.

**This is not a foundations course. This is not an entrepreneurship course. This is an *applied execution* course.** Every participant builds Juno PM — their personal AI Associate PM — against the same RocketShip scenario, and ships it to a forkable GitHub repo.

**Format: 100% individual.** No group breakouts, no team deliverables, no group presentations. Every exercise is solo, every artifact is yours, every reflection is your own. Where peer feedback would have lived, we use **self-review checklists + AI-review prompts + async showcase in #ai-pm-cohort**.

---

## The Arc: Six Execution Questions

Each module answers one question a working AI PM actually has to answer to ship. The arc is sequential — each answer depends on the last.

| Module | Title | Execution Question |
|--------|-------|--------------------|
| M1 | **Drive AI-First Execution with Prompting** | What does an AI-native PM *do differently*, and how do I configure my first copilot? |
| M2 | **Validate AI Opportunities and Technical Feasibility** | Is this AI bet worth oxygen, and what level of autonomy can it actually have? |
| M3 | **Improve AI Product Requirements with RAG Architecture** | How do I write a PRD that an engineer can ship — with the right data, in the right place? |
| M4 | **Design AI-Native User Experiences** | How do I make a probabilistic system feel trustworthy and effortless? |
| M5 | **Deploy Agentic Systems and Workflows** | When should the copilot act on its own, and when must it hand back to me? |
| M6 | **Measure AI Quality with Evals and Guardrails** | How do I prove this is shippable — and keep it that way? |

### Why AI PM is different (name it in M1, reinforce every module)

Traditional PM assumes deterministic outputs, manual specs, command-driven UIs, sequential workflows, and ship-then-monitor. AI PM breaks all five:

| Traditional PM | AI PM |
|---|---|
| Outputs are deterministic | Outputs are probabilistic — drift, hallucination, variance |
| Spec is a doc | Spec is a doc + prompt + data corpus + eval set |
| UI is command-driven | UI is intent-driven and frequently invisible |
| Workflows are sequential | Workflows are agentic — branched, conditional, handed off |
| Ship and monitor with analytics | Ship with an eval harness + human rubric + guardrails |

Name the broken assumption in the first 2 minutes of each module. It's why this course exists.

### The underlying shifts (per module)

- **M1:** Deterministic execution → Probabilistic configuration (prompting as product config)
- **M2:** Feature lists → Validated AI bets (autonomy + decision matrix)
- **M3:** Static PRDs → Context-engineered PRDs (data corpus + RAG trade-offs)
- **M4:** Command-driven UI → Intent-driven, AI-native UX (closing the trust gaps)
- **M5:** Manual workflows → Agentic orchestration (with explicit handoff rules)
- **M6:** Ship + watch dashboards → Eval harness + human rubric + governance

---

## The Throughline Artifact: Juno PM in a GitHub Repo

The final project is not a slide deck submitted to an LMS. It is **a GitHub repo** — your `juno-pm` fork — with one folder per module, version-controlled, portable, and shareable Monday morning.

| Module | Folder | What it contains |
|---|---|---|
| M1 | `01-prompting/` | Anatomy prompt, system prompt for Juno, Lovable prototype link |
| M2 | `02-strategy/` | AI Solution Decision Matrix, AI Strategy One-Pager |
| M3 | `03-rag-prd/` | AI PRD for Juno with RAG architecture decisions |
| M4 | `04-ai-ux/` | AI user flow, AI-UX trust-gap mitigations, screenshots |
| M5 | `05-agentic-workflows/` | Agent Workflow Spec (AWSpec), agent control panel |
| M6 | `06-evals/` | Eval stack, human eval rubric, final pitch (`README.md`) |

The top-level `README.md` in the participant's fork is **the deliverable** — a single page summarising all 6 components with links to each, plus the final pitch slot. M6's final exercise finalises this README and the optional async demo.

**Participants don't leave with a certificate. They leave with a working artifact, in their account, that they can show on Monday.**

---

## Seven Design Principles

### 1. Build in every module

Every module produces something tangible committed to the participant's repo. Not a feeling — a file.

| Module | Build moment | Artifact in repo |
|---|---|---|
| M1 | Prompt-to-prototype Juno in Lovable + configure system prompt | `01-prompting/system-prompt.md` + Lovable link |
| M2 | Map Juno's strategic bet + write AI Strategy One-Pager | `02-strategy/decision-matrix.md` + `strategy-one-pager.md` |
| M3 | Improve Juno with RAG + specify in AI PRD | `03-rag-prd/ai-prd.md` |
| M4 | Architect Juno's core AI user flow + apply trust-gap mitigations | `04-ai-ux/user-flow.md` + screenshots |
| M5 | Write Juno's Agent Workflow Spec | `05-agentic-workflows/awspec.md` |
| M6 | Plan Juno's eval stack + finalise README | `06-evals/eval-stack.md` + top-level `README.md` |

By M6, the participant assembles a repo they've already built.

### 2. Individual-only, opinionated voice

Every exercise is solo. Every artifact is yours. We replace group dynamics with three explicit individual mechanics:

- **Self-review checklist** — 3–5 bullets you tick against your own artifact before moving on.
- **AI-review prompt** — an explicit prompt you paste, with your artifact, into ChatGPT/Claude/Cursor to get critique.
- **Async showcase** — commit your work, post the link in `#ai-pm-cohort`, instructor responds in-thread.

This format is more honest. AI PMs work alone-but-AI-augmented in their day jobs; the course mirrors that.

### 3. One scenario, repeated: RocketShip → Juno PM

Every module uses the same scenario: you are the AI PM at RocketShip, a hyper-growth B2B SaaS platform suffering **Signal Collapse** — too much data, no headcount, you've become the bottleneck. Across 6 modules you design and build **Juno PM**, an AI Associate PM that lives inside Slack/Notion/Jira (not as a standalone chat tab) and handles three pillars: *Synthesize insights, Draft specs, Prioritize risks.*

The scenario stays fixed. The exercises stack. By M6 you have a deployable AI Associate PM and a board-ready pitch.

### 4. Frameworks are mental models, not templates

Every framework in this course (Anatomy of a High-Quality Prompt, Three-Layer Model, Jobs × Risk × Autonomy, AI Solution Decision Matrix, AI Strategy One-Pager, RAG Architecture Decision Factors, AI Iceberg, AI-UX Readiness Check, Agent Spectrum, ReAct, Planner-Executor, Agent Workflow Spec, PM Decision Triangle, AI Evals Stack, Three Levers) is a thinking tool. The template gives you the starting shape. Your job is to adapt it to Juno + RocketShip.

If your artifact looks identical to the template, that's a smell.

### 5. AI PM is different — say it explicitly

Each module names the traditional PM assumption it breaks. M1 opens with the table. M2–M6 reference it. The course's opinion is: **you cannot PM AI products with a non-AI playbook.**

### 6. Tools that earn their keep

Every module ships 2–3 single-file HTML tools (Prompt Anatomy Builder, AI Solution Decision Matrix, RAG Architecture Decider, AI User Flow Architect, AWSpec Builder, Eval Stack Designer, etc.). Each tool has a **"Copy as markdown → paste into your repo"** button. Tools generate the artifact; the participant edits and commits it.

### 7. Use AI to evaluate your own AI strategy

The proof you internalised the frameworks: by M6 you can use an AI model to evaluate any future AI bet against all six lenses. The capstone includes an **AI-review prompt** you can reuse forever:

> *"Evaluate this AI product bet against: (1) Is it a real value driver vs. a fake-good feature? (2) Is the autonomy level appropriate for the risk? (3) Does the PRD specify the RAG architecture and trade-offs? (4) Are the AI-UX trust gaps explicitly closed? (5) Is the agent workflow spec'd with explicit handoffs? (6) Is there an eval stack with human + automated evaluation? Where is this strategy weakest, and what would you change first?"*

---

## Module Summaries

### M1: Drive AI-First Execution with Prompting

**Learning objective:** Move from chatting with AI to *configuring* it — by deconstructing the anatomy of a high-quality prompt and prototyping your AI copilot in under 30 minutes.

**Key content:**
- The AI-First Product Mindset — deterministic vs. non-deterministic systems
- How the AI-era PM role has evolved + the PM's AI toolkit
- Anatomy of a High-Quality Prompt — context, task, constraints, format
- Hands-on lab: prompt-to-prototype Juno PM in Lovable
- Prompting as product configuration — few-shot, chain-of-thought, hyperparameters, system prompts
- The Optimization Decision Framework — prompt vs. RAG vs. fine-tuning

**Build moment:** Prompt-to-prototype Juno in Lovable (individual lab) + configure Juno's system prompt to act as a risk watchdog (individual exercise — was group).

**Artifact committed:** `01-prompting/system-prompt.md` + Lovable prototype URL in `01-prompting/README.md`.

**Bridge to M2:** *"You can prototype Juno. M2 answers: is this even the right bet, and how autonomous should it be?"*

---

### M2: Validate AI Opportunities and Technical Feasibility

**Learning objective:** Validate AI bets the way a CPO will — using a strategic scorecard, an autonomy lens, and a one-page justification you can defend.

**Key content:**
- Fake good vs. boring killers — the four ways AI creates real value (cost, revenue, risk, delight)
- The Three-Layer Model — mapping strategic bets to product mechanics
- Jobs × Risk × Autonomy — choosing the right level of model independence
- AI Solution Decision Matrix — pressure-testing bets against technical reality
- Responsible AI as strategic guardrails
- AI Strategy One-Pager — anatomy and worked example

**Build moment:** Map Juno's strategic bet + draft Juno's AI Strategy One-Pager (both individual — were group).

**Artifact committed:** `02-strategy/decision-matrix.md` + `02-strategy/strategy-one-pager.md`.

**Bridge to M3:** *"You have a defensible bet. M3 answers: how do you write a spec an engineer can ship — with the right data, in the right place?"*

---

### M3: Improve AI Product Requirements with RAG Architecture

**Learning objective:** Write an AI PRD that goes beyond user stories — one that specifies the data corpus, retrieval strategy, and the three RAG trade-offs (cost, speed, accuracy).

**Key content:**
- Prompt engineering vs. context engineering — why PMs must own data
- RAG process overview — retrieval, augmentation, generation
- Hands-on lab: ground Juno in the RocketShip Strategy One-Pager corpus
- What's new in an AI PRD vs. a traditional PRD
- The three RAG trade-offs + architecture decision factors
- Tokens, context windows, data preparation, augmentation considerations

**Build moment:** Specify Juno's RAG architecture in your AI PRD (individual — was group).

**Artifact committed:** `03-rag-prd/ai-prd.md`.

**Bridge to M4:** *"You have a spec. M4 answers: how do you wrap this in an interface a user will actually trust?"*

---

### M4: Design AI-Native User Experiences

**Learning objective:** Design AI-native UX — invisible by default, intent-driven where visible, with the three trust gaps (black-box, hallucination, control) explicitly closed.

**Key content:**
- AI-UX implementations today — why "chat in a tab" is the wrong default
- Invisible by design — anticipating intent vs. waiting for commands
- Mapping value to UX treatment — the four AI value props × UX patterns
- Architecting the AI Iceberg — what users see vs. what runs underneath
- AI user flow walkthrough — HR Agent example
- The AI-UX readiness check — closing the black-box gap, hallucination gap, control gap
- Managing the intelligence tax (extra latency / cognitive load)

**Build moment:** Architect Juno's core AI user flow (individual — was group).

**Artifact committed:** `04-ai-ux/user-flow.md` + screenshots (`04-ai-ux/screenshots/`).

**Bridge to M5:** *"Users will trust the surface. M5 answers: when should Juno act on its own, and when does it hand back to you?"*

---

### M5: Deploy Agentic Systems and Workflows

**Learning objective:** Move Juno from a passive copilot to a controlled agent — by writing an Agent Workflow Spec that defines triggers, tools, memory, and the handoff line.

**Key content:**
- The evolution of value — from chat to autonomous task execution
- What is an agent? Key traits of agency + the agent spectrum
- Real-world example: how companies are deploying agents
- Agentic design patterns — ReAct and Planner-Executor
- Types of agentic memory (short-term, long-term, episodic, semantic)
- Common failure modes
- The PM's Agent Control Panel + Agent Workflow Spec (AWSpec)
- The PM Decision Triangle — autonomy vs. risk vs. handoff
- Optional post-class lab: build Juno's workflow in Langflow

**Build moment:** Write Juno's Agent Workflow Spec (individual — was group).

**Artifact committed:** `05-agentic-workflows/awspec.md` + `Juno Agent.json` (starter Langflow export).

**Bridge to M6:** *"You have an agent. M6 answers: how do you prove it's shippable, and keep it that way?"*

---

### M6: Measure AI Quality with Evals and Guardrails

**Learning objective:** Prove Juno is production-ready with a multi-layered eval stack — user feedback + human rubric + automated evals — and finalise the repo for an async showcase.

**Key content:**
- Why vibe checks fail in production + the 95% accuracy trap
- The AI Evals Stack — three layers: user feedback, human evaluation, automated evals
- How to build a human eval rubric — Google Assistant example
- The PM's role in evaluations
- Operationalising and measuring AI risks — the governance framework
- The Three Levers to optimise AI performance — model, data, architecture
- PM execution plan
- Final project deliverables — individual repo + optional async demo

**Build moment:** Plan Juno's eval stack (individual — was group) + finalise project deliverables (individual — was group).

**Artifact committed:** `06-evals/eval-stack.md` + `06-evals/human-rubric.md` + top-level `README.md` (final pitch).

**Async showcase:** Post your repo link + a 3-minute Loom in `#ai-pm-cohort`. Instructor responds in-thread within 5 days.

---

## What This Course Has That Nobody Else Does

1. **A repo, not a deck.** Other AI PM courses end with a slide deck submitted to an LMS. This course ends with a forkable GitHub repo with one folder per module — version-controlled, portable, real.
2. **The full execution stack in one program.** Reforge splits prompting / strategy / RAG / UX / agents / evals across 5–6 separate paid courses. This threads them into one coherent arc on the *same scenario* (RocketShip → Juno PM).
3. **Individual-only format.** No group breakouts to babysit, no team velocity drift. Solo execution with explicit self-review + AI-review + async share mechanics. Honest about how AI PMs actually work.
4. **Tools that emit your artifact.** Every module ships HTML tools with a "Copy as markdown" button — the tool generates your file, you commit it.
5. **The opinionated spine.** Most courses hedge. This one has a point of view: prompting is product configuration, autonomy is a strategic decision not an engineering one, RAG is a PM responsibility not a backend one, AI-UX is invisible by default, agents need explicit handoff lines, and evals are a product surface not a QA chore.

---

## Open Design Decisions

- [x] **Group → individual conversion:** RESOLVED. All breakout group exercises rewritten as individual exercises with self-review + AI-review + async share. Final showcase converted from live presentation to async Loom + repo link in `#ai-pm-cohort`.
- [x] **Throughline artifact:** RESOLVED. Forkable GitHub repo (`juno-project-template/`) with 6 module folders + top-level `README.md` as the dashboard.
- [x] **Scenario:** RESOLVED. RocketShip "Signal Collapse" → Juno PM (Associate PM in Slack/Notion/Jira). Same scenario across all 6 modules.
- [x] **Optional post-class labs:** KEEP (M4 Reimagine Juno as AI-Native; M5 Build Juno's Agentic Workflow in Langflow). Framed as optional, async, instructor responds in #ai-pm-cohort.
- [ ] **Cert grading rubric:** Inherit from old artefacts (Application of Concepts, Credibility & Reasoning, Clarity, Strategic Thinking — 1 Poor / 2 Sufficient / 3 Excellent). Reword to reference repo + README rather than deck.
