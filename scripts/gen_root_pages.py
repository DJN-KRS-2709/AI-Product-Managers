"""Generate root-level HTML pages with the same visual identity as the module decks.

Pages:
- AI Product Management - Course Overview.html
- Curriculum Map.html
- Final Project Brief.html
- Tools Overview.html
- Pitch/AI Product Management - Pitch Deck.html

Run from repo root:
    python3 scripts/gen_root_pages.py
"""
from __future__ import annotations
from pathlib import Path

from gen_module_decks import (
    CSS, JS, MODULES_META,
    hero, how_it_runs, course_arc, lecture_table, lecture_cards, two_column,
    section_break, applied_work, case_study, takeaways, extra_practice, bridge,
    synthesis, break_section, qa_section, notes_block, takeaway_block,
    render_page, _add_builder, recall_section,
    LOGO_REL,
)

REPO_ROOT = Path(__file__).resolve().parent.parent

# Notes:
# - Root pages live at the repo root, so the logo path needs adjusting.
# - The `LOGO_REL` from gen_module_decks is "../Design/..." (used from Modules/).
# - For the repo root, we use "Design/...".
ROOT_LOGO = "Design/Minimalist shield with glowing _P_.png"
PITCH_LOGO = "../Design/Minimalist shield with glowing _P_.png"


def _patch_logo_path(html: str, logo_path: str) -> str:
    return html.replace('src="../Design/Minimalist shield with glowing _P_.png"',
                        f'src="{logo_path}"')


def render_root_page(title: str, body_sections: list[str], logo_path: str = ROOT_LOGO) -> str:
    body = "\n\n".join(body_sections)
    body = body.replace('src="../Design/Minimalist shield with glowing _P_.png"',
                        f'src="{logo_path}"')
    body = body.replace('href="M', 'href="Modules/M').replace('href="Modules/Modules/', 'href="Modules/')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>

<div class="progress-bar" id="progressBar"></div>
<nav class="nav-dots" id="navDots"></nav>

{body}

<div class="help-hint">↑ ↓ navigate · K skip section · M section sorter</div>
<div class="skip-badge" id="skip-badge" title="Click to unskip (K)">SKIPPED</div>
<div class="slide-sorter" id="slide-sorter">
  <div class="sorter-header">
    <div><div class="sorter-title">Section Sorter</div><div class="sorter-subtitle">Click a section to jump · Toggle skip to hide during presentation</div></div>
    <button class="sorter-close" onclick="closeSorter()" title="Close (M / Esc)">✕</button>
  </div>
  <div class="sorter-grid" id="sorter-grid"></div>
</div>

<script>{JS}</script>
</body>
</html>
"""


def how_this_course_runs() -> str:
    """Course-level expectation grid (vs. how_it_runs() which is module-level).

    Same six expect-cards as the per-module version, but headlined "How This
    Course Runs" so the section makes sense at the Course Overview / pitch level.
    """
    cards = [
        ("⏱", "~12 hours total, async-friendly", "Six modules. ~2 hours each. Self-paced. Async-first."),
        ("👤", "100% individual", "No groups. No partner work. You own every deliverable."),
        ("🛠", "Open the tool", "Each module has 1–4 single-file HTML tools. Vanilla JS. localStorage."),
        ("✅", "Self-review", "Each tool ships with a 4–6 item checklist. Run before you commit."),
        ("🤖", "AI-review", "Paste your artifact + the verbatim prompt into ChatGPT or Claude."),
        ("📂", "Async share", "Commit to your <code>juno-pm/</code> fork. Optional Loom in <code>#ai-pm-cohort</code>."),
    ]
    cells = "\n".join(
        f'      <div class="expect-card"><div class="expect-icon">{ic}</div>'
        f'<div class="expect-title">{t}</div><div class="expect-desc">{d}</div></div>'
        for ic, t, d in cards
    )
    return f"""<section class="centered" data-title="How This Course Runs">
  <div class="inner">
    <div class="section-label">Ground Rules</div>
    <h2>How This Course Runs</h2>
    <div class="expect-grid">
{cells}
    </div>
  </div>
</section>
"""


def hero_root(lead: str, accent: str, subtitle: str, waypoints: list[tuple[str, str]],
              out_line: str, label: str, logo_path: str = ROOT_LOGO) -> str:
    waypoints_html = "\n".join(
        f'  <div class="waypoint"><div class="waypoint-num">{i+1}</div>'
        f'<div class="waypoint-text"><div class="wt-title">{wt}</div>'
        f'<div class="wt-desc">{wd}</div></div></div>'
        for i, (wt, wd) in enumerate(waypoints)
    )
    return f"""<section class="hero" data-title="{lead} {accent}">
  <div class="hero-logo"><img src="{logo_path}" alt="Product School logo"/></div>
  <div class="section-label">{label}</div>
  <h1>{lead} <span>{accent}</span></h1>
  <p class="subtitle">{subtitle}</p>
  <div class="waypoints" style="max-width:640px;">
{waypoints_html}
  </div>
  <p style="font-size:15px; color:#8899bb; margin-top:8px;">{out_line}</p>
  <div class="scroll-hint">Scroll to explore<span>&#8595;</span></div>
</section>
"""


# ─────────────────────────────────────────────────────────────────────────────
# COURSE OVERVIEW
# ─────────────────────────────────────────────────────────────────────────────

def build_course_overview() -> list[str]:
    sections = []

    sections.append(hero_root(
        "AI Product Management", "Certification",
        "Six modules. One living copilot. The repo is the certificate.",
        [("Bet & Decide", "M1 prompting · M2 strategy · pressure-test the bet."),
         ("Specify & Trust", "M3 RAG/PRD · M4 AI-UX · spec the data, close the trust gaps."),
         ("Orchestrate & Prove", "M5 agentic · M6 evals · ship a system that proves itself.")],
        "Out: a forkable juno-pm/ repo with six committed components and a finalised README.",
        "Course Overview · 2026 cohort"))

    sections.append(how_this_course_runs())
    sections.append(course_arc(0))  # 0 = no module active; this just renders without active node

    # Strategic arc as cards
    sections.append(lecture_cards(
        "The Strategic Arc",
        "Bet → Decide → Specify → Trust → Orchestrate → Prove. One verb per module.",
        [("M1", "Bet · Prompting", "Stop chatting with AI. Start configuring it."),
         ("M2", "Decide · Strategy", "From AI tactics to product strategy your CFO can sign off on."),
         ("M3", "Specify · RAG/PRD", "Write specs an LLM can actually execute."),
         ("M4", "Trust · AI-UX", "Make uncertainty feel safe — without hiding it."),
         ("M5", "Orchestrate · Agentic", "Hand work to agents — without losing the room."),
         ("M6", "Prove · Evals", "Prove it works. Catch it when it doesn't.")],
        footer="Each module commits one folder to <code>juno-pm/</code>. By M6 you ship the README.",
        tag_label="Framework"))

    # The Juno scenario
    sections.append(case_study(
        "Scenario",
        "RocketShip is in Signal Collapse",
        "<strong>RocketShip</strong> · B2B SaaS for Enterprise Data Teams · You are the AI PM.",
        "Wall of P0 escalations · thousands of stalled tickets · sales deals frozen · zero new headcount.",
        "You can't scale yourself. You scale your <strong>judgment</strong>. You build <strong>Juno PM</strong> — across six modules.",
        footer="One scenario carries the entire course. You leave with a real artifact."))

    # The throughline — Juno
    sections.append(lecture_cards(
        "The Throughline — Juno PM",
        "An AI Associate PM that lives <em>inside</em> Slack, Notion, and Jira.",
        [("🔍", "Synthesise", "Wall of escalations &rarr; structured, evidence-backed clarity."),
         ("📝", "Draft", "Raw findings &rarr; v0.1 PRDs. Start with a draft, not a blank page."),
         ("⚠️", "Prioritise", "Risk watchdog. Flags edge cases, technical debt, risky assumptions.")],
        footer="By M6 you commit four artifacts: PRD · system prompt · data + retrieval · eval set.",
        tag_label="Lecture"))

    # Format
    sections.append(lecture_table(
        "Format",
        "100% individual. The repo is the deliverable. Submission is the URL.",
        ["Aspect", "How it works"],
        [["Format", "Self-paced async + optional live cohort. ~2 hours per module."],
         ["Deliverable", "One artifact per module, committed to <code>juno-project-template/</code> fork."],
         ["Self-review", "Each tool ships with a 4–6 item checklist. Run before commit."],
         ["AI-review", "Each tool ships with a verbatim LLM prompt. Run after commit."],
         ["Async share", "Optional 3-min Loom + repo URL in <code>#ai-pm-cohort</code>."],
         ["Submission", "Repo URL. Within 7 days post-cohort. Graded on 4 dimensions."]],
        caption="No groups. No partner work. No live presentation required.",
        tag_label="Framework"))

    # What you walk away with
    sections.append(lecture_cards(
        "What You Walk Away With",
        "Reusable artifacts — long after the cohort ends.",
        [("📦", "A scored bet template", "5-axis matrix you reuse for every future AI bet."),
         ("📋", "An AI PRD pattern", "Doc + corpus + retrieval + eval + failure modes."),
         ("🌊", "An AI Iceberg flow", "7-node pattern for any AI feature on your roadmap."),
         ("🛡", "An AWSpec", "9-section agent contract that bounds the liability."),
         ("✅", "An eval stack", "3-layer template — user feedback · human · automated."),
         ("📂", "Your Juno PM repo", "Forkable. Yours. The pitch.")],
        tag_label="Lecture"))

    sections.append(qa_section())

    return sections


# ─────────────────────────────────────────────────────────────────────────────
# CURRICULUM MAP
# ─────────────────────────────────────────────────────────────────────────────

def build_curriculum_map() -> list[str]:
    sections = []

    sections.append(hero_root(
        "Curriculum", "Map",
        "Six modules. One arc. One repo.",
        [("Topics + frameworks", "What gets taught and what frameworks anchor it."),
          ("Tools per module", "Which interactive tools you use and what they emit."),
          ("Deliverables", "What you commit to your juno-pm/ fork.")],
        "Out: clarity on every module's input, output, and tools.",
        "Curriculum Map · 2026 cohort"))

    sections.append(course_arc(0))

    rows = [
        ["<strong>M1 · Prompting</strong>",
         "Anatomy of a high-quality prompt · Optimization Decision Framework",
         "Toolkit Picker · Prompt Anatomy Builder · System Prompt Configurator",
         "<code>system-prompt.md</code> · <code>anatomy-prompt.md</code> · <code>lovable-prototype.md</code> · <code>toolkit.md</code>"],
        ["<strong>M2 · Strategy</strong>",
         "Four AI Value Frames · Three-Layer Model · 5-axis Decision Matrix · 7-block One-Pager",
         "AI Solution Decision Matrix · Three-Layer Model Mapper · AI Strategy One-Pager Builder",
         "<code>decision-matrix.md</code> · <code>strategy-one-pager.md</code>"],
        ["<strong>M3 · RAG / PRD</strong>",
         "Context engineering · RAG process · 5 architecture questions · 3 trade-offs",
         "RAG Architecture Decider · AI PRD Builder",
         "<code>ai-prd.md</code> · <code>before-after-rag.md</code>"],
        ["<strong>M4 · AI-UX</strong>",
         "Invisible by design · AI Iceberg (7 nodes) · 3 trust gaps · intelligence tax",
         "AI User Flow Architect · AI-UX Trust Gap Checker",
         "<code>user-flow.md</code> · <code>trust-gaps.md</code>"],
        ["<strong>M5 · Agentic</strong>",
         "Four traits of agency · Agent Spectrum · ReAct · Planner-Executor · 4 memory types · PM Decision Triangle",
         "Agent Workflow Spec Builder · Agent Control Panel",
         "<code>awspec.md</code> · <code>agent-control-panel.md</code>"],
        ["<strong>M6 · Evals</strong>",
         "AI Evals Stack (3 layers) · Human Eval Rubric · 3 optimisation levers · governance buckets",
         "Eval Stack Designer · Human Evaluation Rubric · Final Project Deliverables Builder",
         "<code>eval-stack.md</code> · <code>human-rubric.md</code> · root <code>README.md</code>"],
    ]

    sections.append(lecture_table(
        "Module-by-Module",
        "Topics · Tools · Deliverables.",
        ["Module", "Topics + frameworks", "Interactive tools", "Repo deliverables"],
        rows,
        caption="Every module commits at least one artifact to <code>juno-project-template/</code>.",
        tag_label="Framework"))

    sections.append(lecture_cards(
        "Pre-Reads · Glossary · Frameworks",
        "Everything you need outside the modules.",
        [("📘", "Concepts Primer (Pre-Read)",
          "15-min onboarding. Read once before M1."),
         ("📚", "Frameworks Reference Card",
          "One-page summary of every framework taught."),
         ("🔤", "Glossary",
          "Single-line definitions for AI Product Management terms."),
         ("📂", "juno-project-template/",
          "Forkable repo with one folder per module — pre-filled READMEs.")],
        tag_label="Lecture"))

    sections.append(qa_section())
    return sections


# ─────────────────────────────────────────────────────────────────────────────
# FINAL PROJECT BRIEF
# ─────────────────────────────────────────────────────────────────────────────

def build_final_project_brief() -> list[str]:
    sections = []

    sections.append(hero_root(
        "Final Project", "Brief",
        "Submit your juno-pm/ fork. Within 7 days post-cohort. Solo.",
        [("Six artifacts", "One per module. All committed to your fork."),
         ("Build Insights", "1 friction · 1 learning · 1 aha moment."),
         ("Optional async showcase", "3-min Loom + repo URL.")],
        "Out: a finalised, certifiable juno-pm/ repo.",
        "Final Project Brief · 2026 cohort"))

    sections.append(lecture_table(
        "What You Submit",
        "The repo URL. That's the submission. Not a deck. Not a doc.",
        ["Aspect", "Detail"],
        [["Format", "Public or private GitHub repo. Forked from <code>juno-project-template/</code>."],
         ["Window", "Within 7 days of cohort end."],
         ["Voice", "Solo. Individual repo per learner."],
         ["Live demo?", "<strong>No.</strong> Optional 3-min Loom in <code>#ai-pm-cohort</code> only."],
         ["Instructor response", "Async, in-thread, within ~5 days."]],
        tag_label="Framework"))

    sections.append(lecture_table(
        "What's In the Repo",
        "Six folders + one root README. All from the modules.",
        ["Folder / file", "Module", "Artifact"],
        [["<code>01-prompting/</code>", "M1", "system-prompt.md · anatomy-prompt.md · lovable-prototype.md · toolkit.md"],
         ["<code>02-strategy/</code>", "M2", "decision-matrix.md · strategy-one-pager.md"],
         ["<code>03-rag-prd/</code>", "M3", "ai-prd.md · before-after-rag.md"],
         ["<code>04-ai-ux/</code>", "M4", "user-flow.md · trust-gaps.md"],
         ["<code>05-agentic-workflows/</code>", "M5", "awspec.md · agent-control-panel.md (Juno Agent.json optional)"],
         ["<code>06-evals/</code>", "M6", "eval-stack.md · human-rubric.md"],
         ["<code>README.md</code> (root)", "M6", "PM Execution Plan · the pitch · Build Insights"]],
        tag_label="Framework"))

    sections.append(lecture_cards(
        "Grading Rubric",
        "Four dimensions. Three-point scale. The repo is the evidence.",
        [("📋", "Application of Concepts", "How well M1–M6 frameworks land in your artifacts."),
         ("🧠", "Credibility & Reasoning", "Whether your decisions hold up to scrutiny."),
         ("✏️", "Clarity", "Whether a stranger could read your README and \"get\" Juno."),
         ("🎯", "Strategic Thinking", "Whether the bet, the bar, and the trade-offs are coherent.")],
        footer="Scale: 1 — Poor (0–49) · 2 — Sufficient (50–79) · 3 — Excellent (80–100).",
        tag_label="Framework"))

    sections.append(lecture_cards(
        "Submission Walkthrough",
        "Five steps to certify.",
        [("①", "Fork", "Fork <code>juno-project-template/</code> as <code>juno-pm/</code>."),
         ("②", "Build", "Commit each module's artifact to its folder."),
         ("③", "Finalise", "Open <code>Final Project Deliverables Builder.html</code>. Generate the root README."),
         ("④", "Reflect", "Add 1 friction · 1 learning · 1 aha to the README."),
         ("⑤", "Submit", "Post the repo URL in <code>#ai-pm-cohort</code> within 7 days. Optional Loom.")],
        footer="That's it. No deck. No live demo. No group. The repo is the certificate.",
        tag_label="Lecture"))

    sections.append(qa_section())
    return sections


# ─────────────────────────────────────────────────────────────────────────────
# TOOLS OVERVIEW
# ─────────────────────────────────────────────────────────────────────────────

def build_tools_overview() -> list[str]:
    sections = []

    sections.append(hero_root(
        "Interactive Tools", "Index",
        "16 single-file HTML tools. Vanilla JS. localStorage. \"Copy as markdown\" everywhere.",
        [("Auto-save", "Every input persists locally."),
         ("Live preview", "See the markdown render as you type."),
         ("Self + AI review", "Each tool ships with a verbatim review prompt.")],
        "Out: every artifact you need, exported to your juno-pm/ fork.",
        "Tools Overview · 2026 cohort"))

    sections.append(lecture_table(
        "Module 1 · Prompting",
        "Three tools. The system prompt is the final-project deliverable.",
        ["Tool", "Output", "Repo path"],
        [["<a href=\"Modules/M1 - PM Toolkit Picker.html\" style=\"color:#60a5fa;\">PM Toolkit Picker</a>",
          "5-category stack you commit to.", "<code>01-prompting/toolkit.md</code>"],
         ["<a href=\"Modules/M1 - Prompt Anatomy Builder.html\" style=\"color:#60a5fa;\">Juno Prototype Prompt Builder</a>",
          "Pre-filled Role/Task/Constraints/Format with Option A (Build Your Own) and Option B (Juno Baseline) presets. Outputs a single block ready to paste into Lovable.", "<code>01-prompting/lovable-prompt.md</code>"],
         ["<a href=\"Modules/M1 - System Prompt Configurator.html\" style=\"color:#60a5fa;\">System Prompt Configurator</a>",
          "Persona · scope · refusal rules · format.", "<code>01-prompting/system-prompt.md</code>"]],
        tag_label="Framework"))

    sections.append(lecture_table(
        "Module 2 · Strategy",
        "Three tools. Decision matrix + one-pager are final-project deliverables.",
        ["Tool", "Output", "Repo path"],
        [["<a href=\"Modules/M2 - AI Solution Decision Matrix.html\" style=\"color:#60a5fa;\">AI Solution Decision Matrix</a>",
          "5-axis pressure test, scored 1–5.", "<code>02-strategy/decision-matrix.md</code>"],
         ["<a href=\"Modules/M2 - Three-Layer Model Mapper.html\" style=\"color:#60a5fa;\">Three-Layer Model Mapper</a>",
          "Strategy · Mechanic · Implementation per pillar.", "<code>02-strategy/decision-matrix.md</code> (extends)"],
         ["<a href=\"Modules/M2 - AI Strategy One-Pager Builder.html\" style=\"color:#60a5fa;\">AI Strategy One-Pager Builder</a>",
          "Seven blocks · CFO-ready.", "<code>02-strategy/strategy-one-pager.md</code>"]],
        tag_label="Framework"))

    sections.append(lecture_table(
        "Module 3 · RAG / PRD",
        "Two tools. The AI PRD is the final-project deliverable.",
        ["Tool", "Output", "Repo path"],
        [["<a href=\"Modules/M3 - RAG Architecture Decider.html\" style=\"color:#60a5fa;\">RAG Architecture Decider</a>",
          "5 questions &rarr; opinionated architecture.", "(paste into AI PRD)"],
         ["<a href=\"Modules/M3 - AI PRD Builder.html\" style=\"color:#60a5fa;\">AI PRD Builder</a>",
          "Traditional PRD + 3 new AI sections.", "<code>03-rag-prd/ai-prd.md</code>"]],
        tag_label="Framework"))

    sections.append(lecture_table(
        "Module 4 · AI-UX",
        "Two tools. The user flow is the final-project deliverable.",
        ["Tool", "Output", "Repo path"],
        [["<a href=\"Modules/M4 - AI User Flow Architect.html\" style=\"color:#60a5fa;\">AI User Flow Architect</a>",
          "Seven nodes · tip vs underwater.", "<code>04-ai-ux/user-flow.md</code>"],
         ["<a href=\"Modules/M4 - AI-UX Trust Gap Checker.html\" style=\"color:#60a5fa;\">AI-UX Trust Gap Checker</a>",
          "Three gaps scored · mitigations specced.", "<code>04-ai-ux/trust-gaps.md</code>"]],
        tag_label="Framework"))

    sections.append(lecture_table(
        "Module 5 · Agentic",
        "Two tools. The AWSpec is the final-project deliverable.",
        ["Tool", "Output", "Repo path"],
        [["<a href=\"Modules/M5 - Agent Workflow Spec Builder.html\" style=\"color:#60a5fa;\">Agent Workflow Spec Builder</a>",
          "Nine sections · the rules of engagement.", "<code>05-agentic-workflows/awspec.md</code>"],
         ["<a href=\"Modules/M5 - Agent Control Panel.html\" style=\"color:#60a5fa;\">Agent Control Panel</a>",
          "Five levers · minimum-viable rules.", "<code>05-agentic-workflows/agent-control-panel.md</code>"]],
        tag_label="Framework"))

    sections.append(lecture_table(
        "Module 6 · Evals",
        "Three tools. The eval stack is the final-project deliverable. Final builder generates the root README.",
        ["Tool", "Output", "Repo path"],
        [["<a href=\"Modules/M6 - Eval Stack Designer.html\" style=\"color:#60a5fa;\">Eval Stack Designer</a>",
          "3-layer eval plan · cadence · pass bar.", "<code>06-evals/eval-stack.md</code>"],
         ["<a href=\"Modules/M6 - Human Evaluation Rubric.html\" style=\"color:#60a5fa;\">Human Evaluation Rubric</a>",
          "Dimensions · anchors · disagreement protocol.", "<code>06-evals/human-rubric.md</code>"],
         ["<a href=\"Modules/Final Project Deliverables Builder.html\" style=\"color:#60a5fa;\">Final Project Deliverables Builder</a>",
          "Pulls every artifact into one root README.", "Top-level <code>README.md</code> of fork"]],
        tag_label="Framework"))

    sections.append(qa_section())
    return sections


# ─────────────────────────────────────────────────────────────────────────────
# PITCH DECK (lives in /Pitch/)
# ─────────────────────────────────────────────────────────────────────────────

def build_pitch_deck() -> list[str]:
    sections = []

    sections.append(hero_root(
        "AI Product Management", "Certification — Pitch",
        "The story of why this course exists, and what it ships.",
        [("The shift", "Every PM is now an AI PM."),
         ("The arc", "Bet → Decide → Specify → Trust → Orchestrate → Prove."),
         ("The artifact", "A repo, not a deck. The juno-pm/ fork is the certificate.")],
        "Out: a 6-week course every AI-curious PM can finish in evenings.",
        "Pitch Deck · Internal", logo_path=PITCH_LOGO))

    sections.append(lecture_table(
        "The Five Shifts",
        "AI broke five PM assumptions. Each shift maps to one module.",
        ["Old PM assumption", "What AI broke", "Module"],
        [["Outputs are deterministic", "Outputs are probabilistic", "M1"],
         ["Spec is a doc", "Spec is doc + prompt + corpus + evals", "M2 + M3"],
         ["UI is command-driven", "UI is intent-driven, often invisible", "M4"],
         ["Workflows are sequential", "Workflows are agentic", "M5"],
         ["Ship + monitor with analytics", "Ship + eval harness + human rubric + guardrails", "M6"]],
        tag_label="Framework"))

    sections.append(lecture_cards(
        "What Makes This Course Different",
        "Three deliberate choices.",
        [("📂", "Repo, not deck",
          "Submission is the URL of a forkable repo. Six committed artifacts. README is the pitch."),
         ("👤", "100% individual",
          "No groups. No partner work. No live presentation. Each exercise has self-review + AI-review."),
         ("🛠", "Bespoke tools",
          "16 single-file HTML tools. Each one emits a markdown artifact straight into the fork.")]))

    sections.append(lecture_cards(
        "The Strategic Arc",
        "One verb per module.",
        [("M1", "Bet — Prompting", "Stop chatting. Configure."),
         ("M2", "Decide — Strategy", "From tactics to a CFO-ready bet."),
         ("M3", "Specify — RAG/PRD", "Spec an LLM can execute."),
         ("M4", "Trust — AI-UX", "Make uncertainty feel safe."),
         ("M5", "Orchestrate — Agentic", "Hand work to agents — bounded."),
         ("M6", "Prove — Evals", "Vibe checks fail. Evals don't.")],
        tag_label="Framework"))

    sections.append(lecture_table(
        "Distribution",
        "How learners actually use this.",
        ["Surface", "Use"],
        [["GitHub Pages site", "All slides and interactive tools — public, indexable, shareable."],
         ["<code>juno-project-template/</code>", "Forkable repo. One folder per module. Pre-filled READMEs."],
         ["<code>#ai-pm-cohort</code>", "Async share + instructor in-thread response within ~5 days."],
         ["Submission", "Repo URL within 7 days post-cohort. No deck."]],
        tag_label="Framework"))

    sections.append(qa_section())
    return sections


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    pages = [
        ("AI Product Management - Course Overview.html",
         "AI Product Management — Course Overview",
         build_course_overview(), ROOT_LOGO, REPO_ROOT),
        ("Curriculum Map.html",
         "AI Product Management — Curriculum Map",
         build_curriculum_map(), ROOT_LOGO, REPO_ROOT),
        ("Final Project Brief.html",
         "AI Product Management — Final Project Brief",
         build_final_project_brief(), ROOT_LOGO, REPO_ROOT),
        ("Tools Overview.html",
         "AI Product Management — Tools Overview",
         build_tools_overview(), ROOT_LOGO, REPO_ROOT),
    ]

    for filename, title, sections, logo, parent in pages:
        out = parent / filename
        out.write_text(render_root_page(title, sections, logo_path=logo), encoding="utf-8")
        print(f"  ✓ wrote {filename} ({out.stat().st_size//1024} KB)")

    pitch_dir = REPO_ROOT / "Pitch"
    pitch_dir.mkdir(exist_ok=True)
    pitch_path = pitch_dir / "AI Product Management - Pitch Deck.html"
    pitch_html = render_root_page(
        "AI Product Management — Pitch Deck",
        build_pitch_deck(),
        logo_path=PITCH_LOGO,
    )
    pitch_path.write_text(pitch_html, encoding="utf-8")
    print(f"  ✓ wrote Pitch/{pitch_path.name} ({pitch_path.stat().st_size//1024} KB)")


if __name__ == "__main__":
    main()
