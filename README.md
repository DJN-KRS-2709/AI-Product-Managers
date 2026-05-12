# AI Product Management Certification

> A GitHub-native AI Product Management course. Six modules. One forkable project (Juno PM). Production-grade artifacts you ship to your own GitHub repo as the certification submission.

This is the source repo for the **AI Product Management Certification** — slides, notes, frameworks, glossaries, pre-reads, 16 interactive tools, a forkable project template, and a landing site.

Mirrors the same pattern as the [AI Product Strategy](https://github.com/DJN-KRS-2709/Product-School---AI-Product-Strategy) repo: HTML for presentations, Markdown for everything else, interactive single-file HTML tools, repo-as-portfolio submission.

## Start here

- [**`index.html`**](index.html) — landing page; the place to start.
- [**Course Overview**](AI%20Product%20Management%20-%20Course%20Overview.html) — the course on one page.
- [**Curriculum Map**](Curriculum%20Map.html) — every module, exercise, tool, artifact.
- [**Final Project Brief**](Final%20Project%20Brief.html) — scenario, deliverables, grading, individual-async showcase.
- [**Tools Overview**](Tools%20Overview.html) — every interactive tool indexed by module.

## The course arc

**Bet → Decide → Specify → Trust → Orchestrate → Prove**

| Module | Title | Execution Question |
|---|---|---|
| M1 · Bet | Drive AI-First Execution with Prompting | What does an AI-native PM do differently? |
| M2 · Decide | Validate AI Opportunities and Technical Feasibility | Is this bet real, and can we ship it? |
| M3 · Specify | Improve AI Product Requirements with RAG Architecture | How do I write a spec engineers can build from? |
| M4 · Trust | Design AI-Native User Experiences | How do I close the three trust gaps? |
| M5 · Orchestrate | Deploy Agentic Systems and Workflows | When do I let the system act on its own? |
| M6 · Prove | Measure AI Quality with Evals and Guardrails | How do I prove this is shippable and stay shippable? |

## Repo structure

```
AI-Product-Managers/
├── README.md                                   # you are here
├── index.html                                  # landing page
├── AI Product Management - Course Overview.html
├── Curriculum Map.html
├── Final Project Brief.html
├── Tools Overview.html
├── course-architecture.md
├── storyline.md
├── course-status.md
├── .cursor/rules/                              # repo conventions
├── Modules/
│   ├── Concepts Primer (Pre-Read).md           # cross-cutting
│   ├── Frameworks Reference Card.md
│   ├── Glossary.md
│   ├── Module {1-6} - Slides.html              # instructor
│   ├── Module {1-6} - Slides (Shareable).html
│   ├── Module {1-6} - Notes (Shareable).md
│   ├── Module {1-6} - Frameworks Reference Card.md
│   ├── Module {1-6} - Glossary.md
│   ├── Module {1-6} - Pre-Read.md
│   ├── M1 - Prompt Anatomy Builder.html        # interactive tools
│   ├── M1 - PM Toolkit Picker.html
│   ├── M1 - System Prompt Configurator.html
│   ├── M2 - AI Solution Decision Matrix.html
│   ├── M2 - Three-Layer Model Mapper.html
│   ├── M2 - AI Strategy One-Pager Builder.html
│   ├── M3 - RAG Architecture Decider.html
│   ├── M3 - AI PRD Builder.html
│   ├── M4 - AI-UX Trust Gap Checker.html
│   ├── M4 - AI User Flow Architect.html
│   ├── M5 - Agent Workflow Spec Builder.html
│   ├── M5 - Agent Control Panel.html
│   ├── M6 - Eval Stack Designer.html
│   ├── M6 - Human Evaluation Rubric.html
│   └── Final Project Deliverables Builder.html
├── Pitch/
│   ├── AI Product Management - Pitch Deck.html
│   └── Gamma Prompt.md
├── scripts/                                    # content extraction
│   ├── requirements.txt
│   ├── extract_pptx.py
│   ├── extract_pdf.py
│   └── build_slides_html.py
├── juno-project-template/                      # learners fork this
│   ├── README.md
│   ├── 01-prompting/
│   ├── 02-strategy/
│   ├── 03-rag-prd/
│   ├── 04-ai-ux/
│   ├── 05-agentic-workflows/                   # Juno Agent.json starter
│   └── 06-evals/
└── Old artefacts AI Product Manager /          # legacy source (read-only)
```

## Three audiences for this repo

1. **Learners** — fork [`juno-project-template/`](juno-project-template/), follow [`Final Project Brief.html`](Final%20Project%20Brief.html), commit one artifact per module.
2. **Instructors** — open `Modules/Module {N} - Slides.html`, teach, point learners at the tools and the template.
3. **Course owners** — open `course-architecture.md`, `storyline.md`, `course-status.md` for the operating philosophy and asset inventory.

## Conventions (see `.cursor/rules/`)

- **Individual-only voice.** No groupwork, no breakouts. Every exercise has self-review + AI-review + async share.
- **Slide pattern.** Dark theme, scroll-snap, full-viewport sections, progress bar + nav dots.
- **Interactive tool pattern.** Single-file, vanilla JS, localStorage, two-pane, copy-as-markdown.
- **File naming.** Strict naming for slides, notes, frameworks, glossary, pre-reads, tools.

## Setup (for re-extraction only)

The HTML/Markdown content is hand-authored. The Python scripts in `scripts/` are for re-extracting source content from `Old artefacts AI Product Manager /` when needed.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -i https://pypi.org/simple -r scripts/requirements.txt
python scripts/extract_pptx.py
python scripts/extract_pdf.py
```

Outputs land in `scripts/_out/` (gitignored).

## License

Course content © Dejan K. (and contributors). Use for your own cohort, internal training, or learning — credit appreciated.
