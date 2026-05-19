"""Module 3 - Improve AI Product Requirements with RAG Architecture.

This file holds the full M3 deck implementation. Mirrors m1_v2 / m2_v2:
- Reuses shared helpers from gen_module_decks (hero, applied_work, takeaways, etc.)
- Reuses class_expectations / cameras_on / section_divider from m1_v2
- Defines M3-specific visual helpers for each lecture / framework slide
- Exposes build_module_3() which returns (sections_inst, sections_share)

Voice: solo only. The original "Breakout Group Exercise - Specifying Juno's
Architecture in Your AI PRD" is converted to an Individual Exercise. There is
no thank-you slide (matches M1/M2 final convention).
"""

from gen_module_decks import (
    hero,
    applied_work,
    takeaways,
    extra_practice,
    qa_section,
    break_section,
    notes_block,
    _add_builder,
)
from m1_v2 import (
    section_divider,
    class_expectations,
    cameras_on,
)


TEMPLATE_REPO_URL = "https://github.com/DJN-KRS-2709/ai-product-management-template"
TEMPLATE_USE_URL = (
    "https://github.com/new?template_name=ai-product-management-template"
    "&template_owner=DJN-KRS-2709"
)


# ---------------------------------------------------------------------------
# Recall / final-project bookkeeping slides
# ---------------------------------------------------------------------------

def m3_repo_recall() -> str:
    """What's in the repo so far (M1 + M2), and what M3 adds today."""
    prior = [
        ("01-prompting/system-prompt.md", "Juno&rsquo;s job description"),
        ("01-prompting/lovable-prototype.md", "V1 dashboard URL"),
        ("02-strategy/decision-matrix.md", "Three-Layer + autonomy mapping"),
        ("02-strategy/strategy-one-pager.md", "6-section strategy one-pager"),
    ]
    today = [
        ("03-rag-prd/prd.md", "AI PRD with RAG architecture spec"),
    ]
    prior_html = "".join(
        f'<li style="font-size:13px; color:#cdd5e3; padding:5px 0 5px 22px; position:relative; line-height:1.5;">'
        f'<span style="position:absolute; left:0; top:7px; width:14px; height:14px; border-radius:50%; background:#34d399; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:9px; font-weight:900;">&check;</span>'
        f'<code style="font-size:0.92em; color:#79c0ff;">{p}</code> &mdash; {d}</li>'
        for p, d in prior
    )
    today_html = "".join(
        f'<li style="font-size:13px; color:#cdd5e3; padding:5px 0 5px 22px; position:relative; line-height:1.5;">'
        f'<span style="position:absolute; left:0; top:7px; width:14px; height:14px; border-radius:50%; background:#d29922; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:9px; font-weight:900;">&rarr;</span>'
        f'<code style="font-size:0.92em; color:#fcd34d;">{p}</code> &mdash; {d}</li>'
        for p, d in today
    )
    return f"""<section data-title="Recall &middot; Repo so far">
  <div class="inner">
    <div class="demo-tag tag-debrief">Recall</div>
    <h2>What&rsquo;s in your <code>juno-pm</code> repo</h2>
    <div class="subtitle">Modules 1 + 2 left four artefacts. Module 3 adds the spec that ties data to decisions.</div>
    <div style="display:grid; grid-template-columns:1.4fr 1fr; gap:18px; max-width:880px; margin:24px auto 0;">
      <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#34d399; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:10px;">&check; M1 + M2 &middot; Committed</div>
        <ul style="margin:0; padding:0; list-style:none;">{prior_html}</ul>
      </div>
      <div style="background:rgba(217,142,34,0.06); border:1px solid rgba(217,142,34,0.3); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#fbbf24; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:10px;">&rarr; Module 3 &middot; Today</div>
        <ul style="margin:0; padding:0; list-style:none;">{today_html}</ul>
      </div>
    </div>
    <p style="font-size:13px; color:#8899bb; margin-top:18px; text-align:center;">M2 said <em>what</em> Juno bets on. M3 specifies <em>which data</em> proves the bet &mdash; and how to retrieve it.</p>
  </div>
</section>
"""


def m3_final_project_progress() -> str:
    """Final project progress card - 7 deliverables, M3 covers 1."""
    deliv = [
        ("M1", "system-prompt.md", "done", "#34d399"),
        ("M1", "lovable-prototype.md", "done", "#34d399"),
        ("M2", "decision-matrix.md", "done", "#34d399"),
        ("M2", "strategy-one-pager.md", "done", "#34d399"),
        ("M3", "prd.md", "today", "#fbbf24"),
        ("M4", "user-flow.md + trust-gaps.md", "later", "#475569"),
        ("M5", "awspec.md + control-panel.md", "later", "#475569"),
        ("M6", "eval-stack.md + human-rubric.md + final README", "later", "#475569"),
    ]
    rows = "".join(
        f'<div style="display:flex; align-items:center; gap:12px; padding:7px 12px; background:rgba(255,255,255,0.025); border-left:2px solid {col}; border-radius:0 6px 6px 0;">'
        f'<span style="font-family:\'Poppins\',sans-serif; font-size:10px; font-weight:900; color:{col}; letter-spacing:0.14em; min-width:24px;">{m}</span>'
        f'<code style="font-size:11.5px; color:#cdd5e3; flex:1;">{p}</code>'
        f'<span style="font-family:\'Poppins\',sans-serif; font-size:9.5px; font-weight:800; color:{col}; letter-spacing:0.14em; text-transform:uppercase; padding:2px 8px; background:{col}1a; border-radius:99px;">{s}</span></div>'
        for m, p, s, col in deliv
    )
    return f"""<section data-title="Final-Project Progress">
  <div class="inner">
    <div class="demo-tag tag-build">Final Project &middot; Progress</div>
    <h2>What you ship by the end of Module 3</h2>
    <div class="subtitle">One of the seven certification deliverables &mdash; the AI PRD with explicit RAG architecture choices. Committed to <code>juno-pm/03-rag-prd/</code>.</div>
    <div style="display:flex; flex-direction:column; gap:5px; max-width:680px; margin:22px auto 0;">
      {rows}
    </div>
    <p style="font-size:12.5px; color:#8899bb; text-align:center; margin-top:14px;">Strategy committed. Now the spec &mdash; including the data corpus, retrieval logic, and trust requirements.</p>
  </div>
</section>
"""



# ---------------------------------------------------------------------------
# Syllabus visual + agenda
# ---------------------------------------------------------------------------

def syllabus_visual_m3() -> str:
    """6-card syllabus, M3 highlighted, M1 + M2 marked done."""
    modules = [
        (1, "Drive AI-First Execution with Prompting",
         "Master systematic context, parameters, and prompt engineering to guide AI behavior with precision.",
         "done"),
        (2, "Validate AI Opportunities and Technical Feasibility",
         "Evaluate feasibility and viability to prioritize features that ship and move business metrics.",
         "done"),
        (3, "Improve AI Product Requirements with RAG Architecture",
         "Bridge product specs and RAG systems. Define embeddings, vector stores, and retrieval logic in a modern AI PRD.",
         "current"),
        (4, "Design AI-Native User Experiences",
         "Design seamless flows that unlock new ways for users to interact. Prototype to validate.",
         "future"),
        (5, "Deploy Agentic Systems and Workflows",
         "Move from single prompts to autonomous agents and multi-step workflows.",
         "future"),
        (6, "Measure AI Quality with Evals and Guardrails",
         "Replace vibe checks with eval harnesses, golden sets, and safety guardrails.",
         "future"),
    ]
    cells = []
    for n, title, desc, state in modules:
        if state == "done":
            tint, label_color, label = "rgba(52,211,153,0.05)", "#34d399", "&check; Done"
            border = "rgba(52,211,153,0.25)"
        elif state == "current":
            tint, label_color, label = "rgba(217,142,34,0.10)", "#fbbf24", "&rarr; Today"
            border = "rgba(217,142,34,0.5)"
        else:
            tint, label_color, label = "rgba(255,255,255,0.025)", "#8899bb", f"M{n}"
            border = "rgba(255,255,255,0.08)"
        cells.append(f"""<div style="background:{tint}; border:1px solid {border}; border-radius:12px; padding:14px 16px; text-align:left; min-height:130px; position:relative;">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
    <span style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:{label_color}; letter-spacing:0.16em; text-transform:uppercase;">Module {n}</span>
    <span style="font-family:'Poppins',sans-serif; font-size:9px; font-weight:800; color:{label_color}; letter-spacing:0.12em; text-transform:uppercase; padding:2px 8px; background:rgba(0,0,0,0.25); border-radius:99px;">{label}</span>
  </div>
  <div style="font-family:'Poppins',sans-serif; font-size:13.5px; font-weight:700; color:#fff; margin-bottom:6px; line-height:1.3;">{title}</div>
  <p style="font-size:11.5px; color:#cdd5e3; line-height:1.5; margin:0;">{desc}</p>
</div>""")
    return f"""<section data-title="Syllabus">
  <div class="inner">
    <div class="demo-tag tag-debrief">Syllabus</div>
    <h2>AI Product Management Certification</h2>
    <div class="subtitle">Six modules. Each compounds into the final Juno copilot. You are here.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1040px; margin:24px auto 0;">
      {''.join(cells)}
    </div>
  </div>
</section>
"""


def agenda_4_m3() -> str:
    """M3 agenda - four numbered sections."""
    items = [
        ("01", "The Power of Context and Context Engineering",
         "Why prompts plateau and how PMs own the data inputs.", "#3b82f6"),
        ("02", "Hands-On Lab &mdash; Improve Juno&rsquo;s Capabilities with RAG",
         "Refactor Juno to ground its prioritization in RocketShip&rsquo;s strategy.", "#fbbf24"),
        ("03", "Mapping RAG To Your AI PRD",
         "Translate retrieval and ranking levers into structured PRD requirements.", "#79c0ff"),
        ("04", "RAG Costs, Control, and Trade-offs",
         "Tokens, context windows, and the architecture choice that fits the bet.", "#34d399"),
    ]
    cards = "".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-left:4px solid {col}; border-radius:12px; padding:18px 22px; text-align:left;">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:34px; font-weight:900; color:{col}; line-height:1; margin-bottom:6px;">{n}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:15px; font-weight:700; color:#fff; margin-bottom:6px; line-height:1.3;">{title}</div>'
        f'<p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0;">{desc}</p>'
        f'</div>'
        for n, title, desc, col in items
    )
    return f"""<section data-title="Agenda">
  <div class="inner">
    <div class="demo-tag tag-debrief">Agenda</div>
    <h2>Today&rsquo;s flow</h2>
    <div class="subtitle">Two solo labs anchor the day. Theory gets unpacked between.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; max-width:980px; margin:24px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 1 - The Power of Context and Context Engineering
# ---------------------------------------------------------------------------

def prompt_vs_context_engineering() -> str:
    """VS comparison: Prompt Engineering vs Context Engineering."""
    rows = [
        ("Focus",
         "Instructions, formatting, and wording.",
         "Designing data inputs &mdash; documents, chunks, and metadata."),
        ("Levers",
         "System prompts, few-shot examples, hyperparameters.",
         "Ingestion, chunking, embeddings, and vector search."),
        ("Strengths",
         "Fast UX experimentation. Early-stage prototyping.",
         "High reliability, maintainability, and cost control."),
        ("Weaknesses",
         "Struggles with factual grounding and scaling proprietary data.",
         "Architectural complexity. Higher initial latency."),
    ]
    pe_cells = "".join(
        f'<div style="padding:11px 14px; border-top:1px solid rgba(255,255,255,0.06);">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:10.5px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:4px;">{label}</div>'
        f'<p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;">{val}</p></div>'
        for label, val, _ in rows
    )
    ce_cells = "".join(
        f'<div style="padding:11px 14px; border-top:1px solid rgba(96,165,250,0.18);">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:10.5px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:4px;">{label}</div>'
        f'<p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;">{val}</p></div>'
        for label, _, val in rows
    )
    return f"""<section data-title="Prompt vs Context Engineering">
  <div class="inner">
    <div class="demo-tag tag-debrief">Lecture &middot; Frame</div>
    <h2>From prompt&hairsp;<span style="opacity:0.5;">&rarr;</span>&hairsp;context engineering</h2>
    <div class="subtitle">Prompts shape behaviour. Context shapes <em>truth</em>. Real products run on both.</div>
    <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:0; max-width:1040px; margin:22px auto 0; align-items:stretch;">
      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.10); border-radius:14px; overflow:hidden; text-align:left;">
        <div style="padding:14px 18px; background:rgba(255,255,255,0.04);">
          <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase;">Prompt Engineering</div>
          <div style="font-family:'Poppins',sans-serif; font-size:18px; font-weight:800; color:#fff; margin-top:4px;">Words to the model</div>
        </div>
        {pe_cells}
      </div>
      <div style="display:flex; align-items:center; justify-content:center; padding:0 16px; min-width:60px;">
        <div style="font-family:'Poppins',sans-serif; font-size:34px; font-weight:900; color:#475569; letter-spacing:0.05em; transform:rotate(-2deg);">VS</div>
      </div>
      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.3); border-radius:14px; overflow:hidden; text-align:left;">
        <div style="padding:14px 18px; background:rgba(96,165,250,0.10);">
          <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase;">Context Engineering</div>
          <div style="font-family:'Poppins',sans-serif; font-size:18px; font-weight:800; color:#fff; margin-top:4px;">Data <em>around</em> the prompt</div>
        </div>
        {ce_cells}
      </div>
    </div>
    <p style="font-size:13px; color:#cdd5e3; max-width:780px; margin:18px auto 0; padding:11px 18px; background:rgba(217,142,34,0.06); border-left:3px solid #fbbf24; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">You need both to be an AI PM</strong> &mdash; but context engineering is where systems become <em>real products</em>.
    </p>
  </div>
</section>
"""


def rag_process_overview() -> str:
    """Three-step RAG: Retrieve / Augment / Generate."""
    steps = [
        ("01", "Retrieve",
         "Before answering, the model searches a defined knowledge base for context relevant to the user&rsquo;s query.",
         "#3b82f6"),
        ("02", "Augment",
         "Within the knowledge base, the system selects the most relevant snippets to wrap around the original query.",
         "#fbbf24"),
        ("03", "Generate",
         "The model uses the retrieved context together with the query to produce a factually grounded answer.",
         "#34d399"),
    ]
    cards = "".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:18px 20px; text-align:left; position:relative;">'
        f'<div style="position:absolute; top:0; right:0; bottom:0; width:4px; background:{col};"></div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:34px; font-weight:900; color:{col}; line-height:1; margin-bottom:8px;">{n}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:18px; font-weight:800; color:#fff; margin-bottom:8px;">{title}</div>'
        f'<p style="font-size:13px; color:#cdd5e3; line-height:1.55; margin:0;">{desc}</p>'
        f'</div>'
        for n, title, desc, col in steps
    )
    return f"""<section data-title="RAG Process Overview">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; RAG</div>
    <h2>RAG &mdash; Retrieval-Augmented Generation</h2>
    <div class="subtitle">A technical pattern that combines an LLM with a targeted search over <em>your</em> proprietary data.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1040px; margin:24px auto 0;">
      {cards}
    </div>
    <p style="font-size:13px; color:#cdd5e3; max-width:780px; margin:18px auto 0; padding:11px 18px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <span style="font-size:16px; margin-right:6px;">&#x1F9E0;</span>
      <strong style="color:#fff;">Keep in mind:</strong> the quality of the final answer depends entirely on how well <em>you</em>&rsquo;ve curated the library it&rsquo;s searching from.
    </p>
  </div>
</section>
"""


def rag_in_practice_diagram() -> str:
    """How RAG works in practice - data preparation + RAG pipeline diagram.

    The Vector DB sits as the visual bridge: offline pipeline ends at it,
    online pipeline starts from it. The "D" arrow makes the handoff explicit
    (matches the original PowerPoint).
    """
    return """<section data-title="How RAG Works In Practice">
  <div class="inner">
    <div class="demo-tag tag-debrief">Lecture &middot; Pipeline</div>
    <h2>How RAG works in practice</h2>
    <div class="subtitle">Offline preparation feeds the same Vector DB the online flow queries. The bridge is <strong style="color:#fff;">D</strong>.</div>

    <!-- OFFLINE PIPELINE -->
    <div style="max-width:1080px; margin:18px auto 0; background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:12px 18px; text-align:left;">
      <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#bcb1ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px;">&#x1F4E6; Step 0 &middot; Data Preparation (offline, runs once + on refresh)</div>
      <div style="display:grid; grid-template-columns:1fr auto 1fr auto 1fr auto 1fr; gap:8px; align-items:center;">
        <div style="background:rgba(124,140,255,0.10); border:1px solid rgba(124,140,255,0.4); border-radius:10px; padding:8px 10px; text-align:center;">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#bcb1ff; letter-spacing:0.1em; margin-bottom:3px;">A</div>
          <div style="font-size:12px; color:#fff; font-weight:700;">Raw data sources</div>
          <div style="font-size:10px; color:#8899bb; margin-top:2px;">Slack, Drive, tickets, transcripts</div>
        </div>
        <div style="font-family:'Poppins',sans-serif; font-size:18px; color:#475569;">&rarr;</div>
        <div style="background:rgba(124,140,255,0.10); border:1px solid rgba(124,140,255,0.4); border-radius:10px; padding:8px 10px; text-align:center;">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#bcb1ff; letter-spacing:0.1em; margin-bottom:3px;">B</div>
          <div style="font-size:12px; color:#fff; font-weight:700;">Extract</div>
          <div style="font-size:10px; color:#8899bb; margin-top:2px;">OCR, PDF parse, crawl</div>
        </div>
        <div style="font-family:'Poppins',sans-serif; font-size:18px; color:#475569;">&rarr;</div>
        <div style="background:rgba(124,140,255,0.10); border:1px solid rgba(124,140,255,0.4); border-radius:10px; padding:8px 10px; text-align:center;">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#bcb1ff; letter-spacing:0.1em; margin-bottom:3px;">C</div>
          <div style="font-size:12px; color:#fff; font-weight:700;">Chunk</div>
          <div style="font-size:10px; color:#8899bb; margin-top:2px;">Split + tag metadata</div>
        </div>
        <div style="font-family:'Poppins',sans-serif; font-size:18px; color:#475569;">&rarr;</div>
        <div style="background:rgba(124,140,255,0.18); border:1px solid rgba(124,140,255,0.6); border-radius:10px; padding:8px 10px; text-align:center;">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#bcb1ff; letter-spacing:0.1em; margin-bottom:3px;">D</div>
          <div style="font-size:12px; color:#fff; font-weight:700;">Embed</div>
          <div style="font-size:10px; color:#8899bb; margin-top:2px;">Convert chunks to vectors</div>
        </div>
      </div>
    </div>

    <!-- D BRIDGE - explicit hand-off from offline to online (same as the original slide) -->
    <div style="max-width:1080px; margin:8px auto 0; position:relative; height:46px;">
      <svg viewBox="0 0 1080 46" preserveAspectRatio="none" style="width:100%; height:100%; display:block;" aria-hidden="true">
        <defs>
          <marker id="ragD-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
            <path d="M0,0 L10,5 L0,10 z" fill="#bcb1ff" />
          </marker>
        </defs>
        <!-- Curve from D box (offline, ~88% across, top) down-and-left to Vector DB (online, ~32%) -->
        <path d="M 945,0 C 945,28 280,18 280,40" stroke="#bcb1ff" stroke-width="2" fill="none" stroke-dasharray="0" marker-end="url(#ragD-arrow)" />
      </svg>
      <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); background:rgba(124,140,255,0.20); border:1px solid rgba(124,140,255,0.55); color:#fff; font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; letter-spacing:0.16em; padding:4px 14px; border-radius:99px; box-shadow:0 4px 12px rgba(7,22,44,0.6); white-space:nowrap;">D &middot; embedded chunks &rarr; Vector DB</div>
    </div>

    <!-- ONLINE FLOW - Vector DB is the same artifact created by D -->
    <div style="max-width:1080px; margin:0 auto; background:rgba(96,165,250,0.05); border:1px solid rgba(96,165,250,0.25); border-radius:14px; padding:12px 18px; text-align:left;">
      <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px;">&#x1F501; Online &middot; Retrieve &rarr; Augment &rarr; Generate (every user query)</div>
      <div style="display:grid; grid-template-columns:auto 1fr auto 1fr auto 1fr auto 1fr auto; gap:6px; align-items:center;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; color:#a0aec0; font-weight:900; letter-spacing:0.1em;">User</div>
        <div style="background:rgba(59,130,246,0.15); border:1px solid rgba(59,130,246,0.5); border-radius:8px; padding:7px 10px; text-align:center;">
          <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#60a5fa; letter-spacing:0.1em;">1</div>
          <div style="font-size:11.5px; color:#fff; font-weight:700; margin-top:2px;">Query</div>
        </div>
        <div style="font-family:'Poppins',sans-serif; font-size:16px; color:#475569;">&rarr;</div>
        <div style="background:rgba(124,140,255,0.22); border:2px solid rgba(124,140,255,0.7); border-radius:8px; padding:7px 10px; text-align:center; box-shadow:0 0 0 3px rgba(124,140,255,0.10);">
          <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#bcb1ff; letter-spacing:0.1em;">2</div>
          <div style="font-size:11.5px; color:#fff; font-weight:700; margin-top:2px;">Vector DB</div>
          <div style="font-size:9px; color:#bcb1ff; margin-top:1px; font-style:italic;">populated by D</div>
        </div>
        <div style="font-family:'Poppins',sans-serif; font-size:16px; color:#475569;">&rarr;</div>
        <div style="background:rgba(217,142,34,0.15); border:1px solid rgba(217,142,34,0.5); border-radius:8px; padding:7px 10px; text-align:center;">
          <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#fbbf24; letter-spacing:0.1em;">3 &middot; 4</div>
          <div style="font-size:11.5px; color:#fff; font-weight:700; margin-top:2px;">Relevant chunks + Query</div>
        </div>
        <div style="font-family:'Poppins',sans-serif; font-size:16px; color:#475569;">&rarr;</div>
        <div style="background:rgba(52,211,153,0.15); border:1px solid rgba(52,211,153,0.5); border-radius:8px; padding:7px 10px; text-align:center;">
          <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#34d399; letter-spacing:0.1em;">5</div>
          <div style="font-size:11.5px; color:#fff; font-weight:700; margin-top:2px;">LLM &rarr; Response</div>
        </div>
        <div style="font-family:'Poppins',sans-serif; font-size:11px; color:#a0aec0; font-weight:900; letter-spacing:0.1em;">User</div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-top:10px; font-size:10.5px; color:#cdd5e3;">
        <div><strong style="color:#60a5fa;">1. Retrieve</strong> &mdash; query becomes an embedding, similarity-search the vector DB.</div>
        <div><strong style="color:#fbbf24;">2. Augment</strong> &mdash; top-K relevant chunks are stitched into the prompt as factual context.</div>
        <div><strong style="color:#34d399;">3. Generate</strong> &mdash; the LLM synthesises a response grounded in the retrieved evidence.</div>
      </div>
    </div>
  </div>
</section>
"""


def rag_workplace_solo_reflection() -> str:
    """Solo reflection (was Q&A discussion in original PowerPoint)."""
    return """<section data-title="Solo Reflection &middot; RAG In Your Workplace">
  <div class="inner">
    <div class="demo-tag tag-debrief">Solo Reflection &middot; 5 min</div>
    <h2>RAG in <em>your</em> workplace</h2>
    <div class="subtitle">Convert the abstract into the personal. The point is the prompt, not the answer.</div>

    <div style="max-width:780px; margin:22px auto 0; background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.3); border-radius:14px; padding:22px 26px; text-align:left;">
      <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#79c0ff; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:10px;">&#x270D;&#xFE0F; The prompt</div>
      <p style="font-size:18px; color:#fff; font-weight:600; line-height:1.45; margin:0;">What is one messy set of documents or workflows you wish you could &ldquo;talk to&rdquo; using this exact RAG method?</p>
    </div>

    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:880px; margin:20px auto 0;">
      <div style="background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px 14px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#34d399; letter-spacing:0.14em; margin-bottom:6px;">&#x1F4DD; Capture</div>
        <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">Name the corpus + the query you wish you could ask it.</p>
      </div>
      <div style="background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px 14px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#fbbf24; letter-spacing:0.14em; margin-bottom:6px;">&#x1F50D; Pressure-test</div>
        <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">Is the answer a fact or a judgement call? RAG only helps with facts.</p>
      </div>
      <div style="background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px 14px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#bcb1ff; letter-spacing:0.14em; margin-bottom:6px;">&#x1F4AC; Share</div>
        <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">Drop a one-liner in <code style="font-size:0.9em; color:#79c0ff;">#ai-pm-cohort</code>.</p>
      </div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 2 - Hands-On Lab 1: Improve Juno's Capabilities with RAG
# ---------------------------------------------------------------------------

def lab1_outcome_preview() -> str:
    """Preview the deliverable - 4-column UI with Strategy column added."""
    return """<section data-title="Lab Outcome Preview">
  <div class="inner">
    <div class="demo-tag tag-build">Lab 1 &middot; Outcome</div>
    <h2>What you&rsquo;ll ship in Lab 1</h2>
    <div class="subtitle">Juno evolves from a 3-column generic dashboard into a 4-column RAG-grounded copilot that cites your strategy.</div>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; max-width:1040px; margin:22px auto 0;">

      <div style="background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.10); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">Before &middot; M1 Juno</div>
        <div style="font-family:'Poppins',sans-serif; font-size:16px; font-weight:800; color:#fff; margin-bottom:10px;">Generic 3-column dashboard</div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:5px; margin-bottom:10px;">
          <div style="background:rgba(255,255,255,0.03); border:1px dashed rgba(255,255,255,0.15); border-radius:6px; padding:6px 4px; text-align:center; font-size:9.5px; color:#a0aec0;">Transcript</div>
          <div style="background:rgba(255,255,255,0.03); border:1px dashed rgba(255,255,255,0.15); border-radius:6px; padding:6px 4px; text-align:center; font-size:9.5px; color:#a0aec0;">Insights</div>
          <div style="background:rgba(255,255,255,0.03); border:1px dashed rgba(255,255,255,0.15); border-radius:6px; padding:6px 4px; text-align:center; font-size:9.5px; color:#a0aec0;">PRD draft</div>
        </div>
        <p style="font-size:11.5px; color:#cdd5e3; line-height:1.5; margin:0;">Hardcoded mock priorities. Treats &ldquo;dark mode&rdquo; and &ldquo;CSV crash&rdquo; equally. No way to defend its reasoning.</p>
      </div>

      <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.35); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#34d399; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">After &middot; RAG-grounded Juno</div>
        <div style="font-family:'Poppins',sans-serif; font-size:16px; font-weight:800; color:#fff; margin-bottom:10px;">4-column copilot with citations</div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:5px; margin-bottom:10px;">
          <div style="background:rgba(52,211,153,0.18); border:1px solid rgba(52,211,153,0.55); border-radius:6px; padding:6px 4px; text-align:center; font-size:9.5px; color:#34d399; font-weight:700;">+ Strategy</div>
          <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.30); border-radius:6px; padding:6px 4px; text-align:center; font-size:9.5px; color:#cdd5e3;">Transcript</div>
          <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.30); border-radius:6px; padding:6px 4px; text-align:center; font-size:9.5px; color:#cdd5e3;">Insights + P0&ndash;P3</div>
          <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.30); border-radius:6px; padding:6px 4px; text-align:center; font-size:9.5px; color:#cdd5e3;">PRD with citations</div>
        </div>
        <p style="font-size:11.5px; color:#cdd5e3; line-height:1.5; margin:0;">Uses RocketShip&rsquo;s strategy as ground truth. Cites the doc. Flags &ldquo;not recommended&rdquo; with reasons.</p>
      </div>
    </div>

    <p style="font-size:12.5px; color:#8899bb; max-width:780px; margin:14px auto 0; text-align:center;">
      <strong style="color:#fbbf24;">The unlock:</strong> Juno stops guessing. It starts citing.
    </p>
  </div>
</section>
"""


def _rag_step_card(num: str, title: str, desc: str, color: str) -> str:
    return f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {color}40; border-radius:10px; padding:11px 14px; text-align:left;">
  <div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">
    <div style="width:24px; height:24px; border-radius:50%; background:{color}; color:#07162C; display:flex; align-items:center; justify-content:center; font-family:'Poppins',sans-serif; font-size:11px; font-weight:900;">{num}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#fff;">{title}</div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{desc}</p>
</div>"""


JUNO_RAG_LAB_BODY = (
    """<p style="font-size:13px; color:#cdd5e3; line-height:1.5; max-width:820px; margin:0 auto 12px; padding:8px 14px; background:rgba(96,165,250,0.06); border-left:3px solid #60a5fa; border-radius:0 8px 8px 0; text-align:left;">
Reopen your Juno Lovable prototype from M1 and evolve it into a RAG-grounded copilot. <strong style="color:#fff;">The Juno RAG Lab Walkthrough is your workspace</strong> &mdash; pre-loaded with both refactor prompts, the test transcript, and the RocketShip strategy doc. Click-to-copy each step.
</p>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; max-width:880px; margin:0 auto 10px;">
"""
    + _rag_step_card("1", "Re-baseline in Lovable", "Open Juno, paste Artifact 1 transcript. Note that priorities are still generic mock data.", "#3b82f6")
    + _rag_step_card("2", "Refactor for strategy ingestion", "Paste the <strong>RAG Refactor Prompt</strong>. Adds a 4th column for the strategy document and removes hardcoded pillars.", "#fbbf24")
    + _rag_step_card("3", "Wire the RAG backend", "Paste the <strong>Logic Ingestion Prompt</strong>. Click <em>Approve</em> when Lovable Cloud asks &mdash; otherwise Juno stays in mock mode.", "#bcb1ff")
    + _rag_step_card("4", "Test with + without strategy", "Process the transcript twice: once empty (Quality Mode), once with the RocketShip Strategy One-Pager pasted (Strategy Mode). Save the diff.", "#34d399")
    + """</div>

<p style="font-size:11.5px; color:#8899bb; max-width:820px; margin:6px auto 0; text-align:center;">
<strong>Deliverable:</strong> Updated Lovable prototype URL committed to <code>03-rag-prd/prd.md</code> &middot; before/after answer captured under <em>Eval &middot; Diagnostic Diff</em>.
</p>
"""
)


# ---------------------------------------------------------------------------
# Section 3 - Mapping RAG To Your AI PRD
# ---------------------------------------------------------------------------

def ai_prd_pillars_7() -> str:
    """7 new pillars in an AI PRD."""
    pillars = [
        ("&#x1F4E6;", "Model Requirements", "Provider, context window, latency targets, modality, open vs proprietary.", "#3b82f6"),
        ("&#x1F4DA;", "Data Requirements", "Sources, chunking strategy, metadata tags, freshness SLAs.", "#fbbf24"),
        ("&#x1F4DD;", "Prompt Requirements", "System prompt, prohibited content, behavioural guardrails (brand voice).", "#79c0ff"),
        ("&#x1F91D;", "AI User Experience", "Trust through citations + user education on model limits.", "#34d399"),
        ("&#x1F9EA;", "AI Testing &amp; Measurement", "Golden Dataset as ground truth. Thresholds for accuracy, bias, robustness.", "#bcb1ff"),
        ("&#x26A0;&#xFE0F;", "AI Risks &amp; Mitigations", "Failure modes (PII leakage, drift). Hard eval gates that block release.", "#f87171"),
        ("&#x1F4B0;", "AI Costs &amp; Latency", "Variable opex from token usage + acquisition costs for proprietary data.", "#fb923c"),
    ]
    cards = "".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:10px; padding:11px 14px; text-align:left; position:relative; overflow:hidden;">'
        f'<div style="position:absolute; top:0; left:0; right:0; height:3px; background:{col};"></div>'
        f'<div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">'
        f'<div style="font-size:16px;">{emoji}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:11px; font-weight:900; color:{col}; letter-spacing:0.08em;">{title}</div>'
        f'</div>'
        f'<p style="font-size:11px; color:#cdd5e3; line-height:1.45; margin:0;">{desc}</p>'
        f'</div>'
        for emoji, title, desc, col in pillars
    )
    return f"""<section data-title="What's New in an AI PRD">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>What&rsquo;s new in an AI PRD?</h2>
    <div class="subtitle">Beyond user stories: an AI PRD defines <em>statistical boundaries</em> for a probabilistic system.</div>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:8px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
    <p style="font-size:12.5px; color:#cdd5e3; max-width:780px; margin:18px auto 0; padding:10px 18px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">Traditional PRD:</strong> if-then rules. <strong style="color:#fff;">AI PRD:</strong> statistical thresholds. The model must hit numbers before it talks to your customers.
    </p>
  </div>
</section>
"""


def rag_into_requirements_4() -> str:
    """How RAG maps to the four PRD sections (Data Prep, Retrieve, Augment, Generate)."""
    rows = [
        ("0", "Data Preparation",
         "Define the &ldquo;SLA of Truth&rdquo; &mdash; how fast a new doc on a server becomes an answer in the AI.",
         "Data Requirements",
         "<em>Sync the Legal repo every 4 hours so policy changes propagate.</em>",
         "#bcb1ff"),
        ("1", "Retrieve",
         "Mandate hybrid search so the system handles both SKU codes <em>and</em> &ldquo;shipping delays.&rdquo;",
         "Model Requirements",
         "<em>Hybrid search must recognise exact product SKU codes + natural-language queries.</em>",
         "#3b82f6"),
        ("2", "Augment",
         "Set Top-K caps. Limit retrieved segments to keep latency tight and prevent hallucinations from token bloat.",
         "AI Costs &amp; Latency",
         "<em>Limit retrieval loop to top 5 segments. Maintain p95 &lt; 2s.</em>",
         "#fbbf24"),
        ("3", "Generate",
         "Require grounded citations + define failure logic when no relevant data is found.",
         "AI User Experience",
         "<em>Every output cites a source link. If retrieval is empty, AI must say so &mdash; not hallucinate.</em>",
         "#34d399"),
    ]
    cells = "".join(
        f"""<div style="display:grid; grid-template-columns:auto 1.4fr 1fr 1fr; gap:14px; padding:11px 14px; align-items:start; border-bottom:1px solid rgba(255,255,255,0.06);">
  <div style="font-family:'Poppins',sans-serif; font-size:24px; font-weight:900; color:{col}; line-height:1; padding-top:2px; min-width:34px;">{n}</div>
  <div style="text-align:left;">
    <div style="font-family:'Poppins',sans-serif; font-size:13.5px; font-weight:800; color:#fff; margin-bottom:3px;">{stage}</div>
    <p style="font-size:11.5px; color:#cdd5e3; line-height:1.45; margin:0;">{obj}</p>
  </div>
  <div style="text-align:left;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:{col}; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:3px;">PRD Section</div>
    <div style="font-size:11.5px; color:#fff; font-weight:600;">{prd_loc}</div>
  </div>
  <div style="background:rgba(0,0,0,0.25); border-radius:6px; padding:7px 10px; font-family:'IBM Plex Mono',monospace; font-size:10.5px; color:{col}; line-height:1.5; text-align:left;">{example}</div>
</div>"""
        for n, stage, obj, prd_loc, example, col in rows
    )
    return f"""<section data-title="How to Incorporate RAG Into Your Requirements">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>How to incorporate RAG into your requirements</h2>
    <div class="subtitle">Each RAG step has a PM strategic objective + a specific home in the PRD.</div>
    <div style="max-width:1080px; margin:22px auto 0; background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.10); border-radius:14px; overflow:hidden;">
      <div style="display:grid; grid-template-columns:auto 1.4fr 1fr 1fr; gap:14px; padding:10px 14px; background:rgba(255,255,255,0.04); font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase;">
        <div style="min-width:34px;">Step</div>
        <div style="text-align:left;">PM Strategic Objective</div>
        <div style="text-align:left;">PRD Location</div>
        <div style="text-align:left;">Example Requirement</div>
      </div>
      {cells}
    </div>
  </div>
</section>
"""


def rag_tradeoffs_3() -> str:
    """Three core RAG trade-offs."""
    items = [
        ("Accuracy vs Cost",
         "Higher Top-K means more facts retrieved.",
         "Operational Cost",
         "Increased token consumption every query.",
         "#fbbf24"),
        ("Latency vs Reasoning",
         "Smaller / faster models keep UX snappy.",
         "Sophistication",
         "Lower reasoning depth on complex logic.",
         "#3b82f6"),
        ("Control vs Speed",
         "Self-hosted infra means total data sovereignty.",
         "Time-to-Market",
         "Slower rollout from heavy engineering lift.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:16px 18px; text-align:left; position:relative; overflow:hidden;">
  <div style="position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(90deg, {col}, {col}80);"></div>
  <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:#fff; margin-bottom:10px;">{title}</div>
  <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:8px; padding:8px 11px; margin-bottom:8px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#34d399; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:3px;">&check; You prioritize</div>
    <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.45;">{prio}</p>
  </div>
  <div style="background:rgba(248,113,113,0.06); border:1px solid rgba(248,113,113,0.25); border-radius:8px; padding:8px 11px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#f87171; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:3px;">&minus; You sacrifice</div>
    <div style="font-family:'Poppins',sans-serif; font-size:12.5px; font-weight:700; color:#fff; margin-bottom:3px;">{sac_label}</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.45;">{sac_desc}</p>
  </div>
</div>"""
        for title, prio, sac_label, sac_desc, col in items
    )
    return f"""<section data-title="Three RAG Trade-offs">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>The three key RAG trade-offs</h2>
    <div class="subtitle">Decision boundaries that go in <em>Model Requirements</em> + <em>AI Costs</em>. Every benefit has a price tag.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1040px; margin:22px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 4 - RAG Costs, Control, and Trade-offs
# ---------------------------------------------------------------------------

def data_preparation_responsibilities() -> str:
    """PMs main responsibilities + questions for data prep."""
    return """<section data-title="Data Preparation">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>Data preparation &mdash; deciding what the AI is allowed to know</h2>
    <div class="subtitle">Defining the &ldquo;Knowledge Library&rdquo; means deciding which data types &mdash; policies, contracts, tickets, wiki pages &mdash; ground your AI.</div>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; max-width:1040px; margin:22px auto 0;">

      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.30); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:10px;">PM Main Responsibilities</div>
        <ul style="margin:0; padding:0; list-style:none;">
          <li style="font-size:12.5px; color:#cdd5e3; padding:7px 0 7px 22px; position:relative; line-height:1.5;">
            <span style="position:absolute; left:0; top:8px; width:14px; height:14px; border-radius:50%; background:#60a5fa; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:9px; font-weight:900;">&check;</span>
            Define <strong>authoritative documents</strong> &mdash; the &ldquo;source of truth&rdquo; that prevents AI contradictions.
          </li>
          <li style="font-size:12.5px; color:#cdd5e3; padding:7px 0 7px 22px; position:relative; line-height:1.5;">
            <span style="position:absolute; left:0; top:8px; width:14px; height:14px; border-radius:50%; background:#60a5fa; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:9px; font-weight:900;">&check;</span>
            Set <strong>freshness SLAs</strong> &mdash; how live the data must be, balanced against ingestion cost.
          </li>
          <li style="font-size:12.5px; color:#cdd5e3; padding:7px 0 7px 22px; position:relative; line-height:1.5;">
            <span style="position:absolute; left:0; top:8px; width:14px; height:14px; border-radius:50%; background:#60a5fa; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:9px; font-weight:900;">&check;</span>
            Capture <strong>ingestion rules</strong> &mdash; supported file types, excluded folders, viewing access &mdash; in your PRD.
          </li>
        </ul>
      </div>

      <div style="background:rgba(217,142,34,0.06); border:1px solid rgba(217,142,34,0.30); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#fbbf24; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:10px;">PMs Must Be Able To Answer</div>
        <ul style="margin:0; padding:0; list-style:none;">
          <li style="font-size:12.5px; color:#cdd5e3; padding:7px 0 7px 22px; position:relative; line-height:1.5;">
            <span style="position:absolute; left:0; top:8px; width:14px; height:14px; border-radius:50%; background:#fbbf24; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:900;">?</span>
            Which specific systems (Drive, Confluence, HRIS) act as the source?
          </li>
          <li style="font-size:12.5px; color:#cdd5e3; padding:7px 0 7px 22px; position:relative; line-height:1.5;">
            <span style="position:absolute; left:0; top:8px; width:14px; height:14px; border-radius:50%; background:#fbbf24; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:900;">?</span>
            How often must the system update &mdash; daily, weekly, sync-on-change?
          </li>
          <li style="font-size:12.5px; color:#cdd5e3; padding:7px 0 7px 22px; position:relative; line-height:1.5;">
            <span style="position:absolute; left:0; top:8px; width:14px; height:14px; border-radius:50%; background:#fbbf24; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:900;">?</span>
            Who is authorised to view which documents (external vs internal)?
          </li>
        </ul>
      </div>
    </div>

    <p style="font-size:12.5px; color:#cdd5e3; max-width:780px; margin:18px auto 0; padding:10px 18px; background:rgba(248,113,113,0.06); border-left:3px solid #f87171; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">The risk:</strong> if the AI indexes three different versions of an expense policy, it <em>will</em> eventually give the wrong answer. Permissions are a product decision &mdash; spec them.
    </p>
  </div>
</section>
"""


def augmentation_considerations() -> str:
    """Filters / Top-K / Re-Ranking."""
    levers = [
        ("&#x1F50D;", "Filters",
         "Hard rules on metadata so the AI never retrieves restricted or outdated data.",
         "<em>If user.region == EU &rarr; restrict to region=EU docs.</em>",
         "#3b82f6"),
        ("&#x1F4CA;", "Top-K",
         "Exact number of segments to include. High for synthesis. Low for fast, cheap responses.",
         "<em>Synthesise 50 interviews? K=10. Quick how-to? K=3.</em>",
         "#fbbf24"),
        ("&#x1F3C6;", "Re-Ranking",
         "Tell the system which sources outrank others when they conflict.",
         "<em>Latest doc wins. Legal-approved trumps draft.</em>",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:12px; padding:14px 16px; text-align:left;">
  <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
    <div style="font-size:18px;">{emoji}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:#fff;">{title}</div>
  </div>
  <p style="font-size:12px; color:#cdd5e3; line-height:1.5; margin:0 0 6px;">{desc}</p>
  <div style="background:rgba(0,0,0,0.28); border-radius:6px; padding:6px 10px; font-family:'IBM Plex Mono',monospace; font-size:10.5px; color:{col}; line-height:1.5;">{example}</div>
</div>"""
        for emoji, title, desc, example, col in levers
    )
    return f"""<section data-title="Augmentation Considerations">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>Augmentation &mdash; packaging facts into the prompt</h2>
    <div class="subtitle">The transition from prompt engineering to context engineering. Three levers you spec in the PRD.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1040px; margin:22px auto 0;">
      {cards}
    </div>
    <p style="font-size:12.5px; color:#cdd5e3; max-width:820px; margin:16px auto 0; padding:10px 18px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">Where this lands in the PRD:</strong> Model + Data Requirements. You&rsquo;re specifying the &ldquo;physics&rdquo; of the prompt &mdash; preventing hallucinations and managing token costs.
    </p>
  </div>
</section>
"""


def physics_of_rag() -> str:
    """Tokens and Context Windows."""
    return """<section data-title="The Physics of RAG">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Physics</div>
    <h2>The physics of RAG &mdash; tokens + context windows</h2>
    <div class="subtitle">Every token costs money. Every byte in the context window competes for the model&rsquo;s attention.</div>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; max-width:1040px; margin:22px auto 0;">

      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.30); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px;">&#x1FA99; Token</div>
        <div style="font-family:'Poppins',sans-serif; font-size:16px; font-weight:800; color:#fff; margin-bottom:8px;">The fundamental unit of compute</div>
        <p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 10px;">A token is a word, part of a word, or punctuation. <strong>Roughly 1 token &asymp; 0.75 words.</strong></p>
        <div style="background:rgba(0,0,0,0.28); border-radius:6px; padding:8px 12px; font-family:'IBM Plex Mono',monospace; font-size:11px; color:#79c0ff; line-height:1.55;">
          <strong style="color:#cdd5e3;">Cost per query =</strong><br/>
          tokens(prompt) + tokens(retrieved chunks) + tokens(response)
        </div>
      </div>

      <div style="background:rgba(217,142,34,0.06); border:1px solid rgba(217,142,34,0.30); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#fbbf24; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px;">&#x1F9E0; Context Window</div>
        <div style="font-family:'Poppins',sans-serif; font-size:16px; font-weight:800; color:#fff; margin-bottom:8px;">The model&rsquo;s short-term memory</div>
        <p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 10px;">Limit per session. Stuffing too much causes the <em>&ldquo;lost in the middle&rdquo;</em> problem &mdash; AI ignores key facts buried mid-prompt.</p>
        <div style="background:rgba(0,0,0,0.28); border-radius:6px; padding:8px 12px; font-family:'IBM Plex Mono',monospace; font-size:11px; color:#fbbf24; line-height:1.55;">
          <strong style="color:#cdd5e3;">Top-K constraint =</strong><br/>
          your token budget &amp; speed lever per query
        </div>
      </div>
    </div>

    <p style="font-size:12.5px; color:#cdd5e3; max-width:880px; margin:18px auto 0; padding:11px 18px; background:rgba(52,211,153,0.06); border-left:3px solid #34d399; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">PM job:</strong> define the token ceiling in the PRD. Example: <em>&ldquo;This feature must resolve queries using fewer than 4,000 tokens to maintain our $0.05 per-query cost target.&rdquo;</em>
    </p>
  </div>
</section>
"""


def rag_architecture_choices_3() -> str:
    """Long Context vs RAG vs Hybrid."""
    items = [
        ("Long Context Only",
         "A large frontier model processes all relevant docs directly via a massive context window.",
         "Speed to prototype. Limited data volume.",
         "High &ldquo;token tax&rdquo; on every query. Risk of facts buried mid-prompt.",
         "#3b82f6"),
        ("RAG",
         "A mid-sized model uses a vector DB to retrieve only the most relevant segments per query.",
         "Accuracy + citations + cost predictability.",
         "Higher engineering complexity to build and maintain the retrieval pipeline.",
         "#34d399"),
        ("Hybrid",
         "RAG identifies the right files; long context lets the model read them in full.",
         "Mature products. Global search + deep reasoning.",
         "More system complexity + higher latency from the loop.",
         "#fbbf24"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:16px 18px; text-align:left; position:relative; overflow:hidden; display:flex; flex-direction:column;">
  <div style="position:absolute; top:0; left:0; right:0; height:4px; background:{col};"></div>
  <div style="font-family:'Poppins',sans-serif; font-size:16px; font-weight:800; color:#fff; margin-bottom:8px;">{title}</div>
  <p style="font-size:11.5px; color:#cdd5e3; line-height:1.5; margin:0 0 10px;">{desc}</p>
  <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:8px; padding:7px 11px; margin-bottom:7px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#34d399; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:2px;">&#x1F947; Best when</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.45;">{best}</p>
  </div>
  <div style="background:rgba(248,113,113,0.06); border:1px solid rgba(248,113,113,0.20); border-radius:8px; padding:7px 11px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#f87171; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:2px;">&#x26A0;&#xFE0F; Main downside</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.45;">{down}</p>
  </div>
</div>"""
        for title, desc, best, down, col in items
    )
    return f"""<section data-title="Choosing Your RAG Architecture">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>Choosing your RAG architecture</h2>
    <div class="subtitle">Not always about a &ldquo;smarter&rdquo; model. Each choice steers your unit economics + UX.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0; align-items:stretch;">
      {cards}
    </div>
  </div>
</section>
"""


def architecture_decision_factors_3() -> str:
    """Where / How / Scale - the three architecture decision factors."""
    factors = [
        ("&#x1F4E1;", "The &ldquo;Where&rdquo; of your data",
         "RAG: dynamic, frequently updated. Updates the index, not the model.",
         "Long Context: static, deep narrative thread that gets lost in chunks.",
         "#3b82f6"),
        ("&#x1F3AF;", "The &ldquo;How&rdquo; of the user task",
         "RAG: pinpoint retrieval. <em>&ldquo;Which SKU on the October order?&rdquo;</em>",
         "Long Context: holistic analysis. <em>&ldquo;Compare these three 50-page scripts.&rdquo;</em>",
         "#fbbf24"),
        ("&#x1F4CF;", "The &ldquo;Scale&rdquo; of the product",
         "RAG: massive libraries (10,000+ docs).",
         "Long Context / Hybrid: focused sessions with user-specific data.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:12px; padding:14px 16px; text-align:left;">
  <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
    <div style="font-size:18px;">{emoji}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#fff;">{title}</div>
  </div>
  <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:8px; padding:7px 10px; margin-bottom:6px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#34d399; letter-spacing:0.13em; margin-bottom:2px;">&rarr; RAG WHEN</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.5;">{rag_case}</p>
  </div>
  <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:8px; padding:7px 10px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#79c0ff; letter-spacing:0.13em; margin-bottom:2px;">&rarr; LONG CONTEXT WHEN</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.5;">{lc_case}</p>
  </div>
</div>"""
        for emoji, title, rag_case, lc_case, col in factors
    )
    return f"""<section data-title="Architecture Decision Factors">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>Your architecture decision factors</h2>
    <div class="subtitle">Three levers that define unit economics + user trust. Engineers ask <em>which</em> trade-offs you accept.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Lab 2 body - Specifying Juno's Architecture in Your AI PRD (SOLO)
# ---------------------------------------------------------------------------

def _prd_card(emoji: str, label: str, color: str, what_to_write: str, juno_seed: str) -> str:
    """One PRD-section card for the Lab 2 body."""
    return f"""<div style="background:rgba(255,255,255,0.035); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:10px 13px; text-align:left; position:relative; overflow:hidden;">
  <div style="position:absolute; top:0; left:0; right:0; height:3px; background:{color};"></div>
  <div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">
    <div style="font-size:16px;">{emoji}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:{color}; letter-spacing:0.08em;">{label}</div>
  </div>
  <p style="font-size:11px; color:#cdd5e3; line-height:1.45; margin:0 0 6px;">{what_to_write}</p>
  <div style="background:rgba(0,0,0,0.28); border-radius:5px; padding:5px 8px; font-family:'IBM Plex Mono',monospace; font-size:9.5px; color:{color}; line-height:1.45;">{juno_seed}</div>
</div>"""


JUNO_PRD_LAB_BODY = (
    """<p style="font-size:13px; color:#cdd5e3; line-height:1.5; max-width:820px; margin:0 auto 12px; padding:8px 14px; background:rgba(96,165,250,0.06); border-left:3px solid #60a5fa; border-radius:0 8px 8px 0; text-align:left;">
Take Juno&rsquo;s &ldquo;evidence engine&rdquo; concept and formalize the RAG architecture into <strong>buildable AI PRD snippets</strong>. Output: <code>03-rag-prd/prd.md</code>. <strong style="color:#fff;">The AI PRD Builder is your workspace</strong> &mdash; with Juno seeds for each section, an inline Airbnb worked example, self-review, and AI-review.
</p>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; max-width:880px; margin:0 auto 12px;">
"""
    + _prd_card(
        emoji="&#x1F9EE;", label="Data Requirements", color="#3b82f6",
        what_to_write="Which sources + quantity ground Juno&rsquo;s decisions? + Sync frequency.",
        juno_seed="Sources: RocketShip strategy doc + last 90 days Slack/tickets. Sync on change.",
    )
    + _prd_card(
        emoji="&#x1F4D0;", label="Model Requirements", color="#79c0ff",
        what_to_write="Long Context, Modular RAG, or Hybrid? Justify against How / Where / Scale.",
        juno_seed="<strong>Hybrid.</strong> RAG indexes the corpus; long context handles single-doc deep reads.",
    )
    + _prd_card(
        emoji="&#x1F4B0;", label="AI Costs &amp; Latency", color="#fbbf24",
        what_to_write="Top-K limit + retrieval pattern (Semantic / Keyword / Hybrid). Latency target.",
        juno_seed="Top-K = 8. Hybrid retrieval. p95 &lt; 3s for prioritization.",
    )
    + _prd_card(
        emoji="&#x1F91D;", label="AI User Experience", color="#34d399",
        what_to_write="How Juno presents evidence + behaviour when no data is retrieved.",
        juno_seed="Every priority cites the strategy clause. Empty retrieval &rarr; flag &ldquo;insufficient evidence&rdquo;, escalate.",
    )
    + """</div>

<div style="max-width:880px; margin:0 auto; background:rgba(124,140,255,0.06); border:1px solid rgba(124,140,255,0.25); border-radius:10px; padding:9px 14px; text-align:left;">
  <span style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#bcb1ff; letter-spacing:0.13em; text-transform:uppercase;">&#x1F4D6; Worked example inside the tool &middot;</span>
  <span style="font-size:12px; color:#cdd5e3;"> Airbnb&rsquo;s Smart Dispute Mediator &mdash; the same four sections, fully filled. Toggle for inspiration on the &ldquo;justification&rdquo; phrasing.</span>
</div>

<p style="font-size:11.5px; color:#8899bb; max-width:820px; margin:8px auto 0; text-align:center;">
<strong>Self-review</strong> &mdash; on-tool checklist. Then AI-review: paste markdown + meta-prompt into ChatGPT/Claude. Final: commit to <code>03-rag-prd/prd.md</code>.
</p>
"""
)


# ---------------------------------------------------------------------------
# Resources & Templates
# ---------------------------------------------------------------------------

def m3_resources_templates() -> str:
    return f"""<section data-title="Resources &amp; Templates">
  <div class="inner">
    <div class="demo-tag tag-build">Resources</div>
    <h2>Resources &amp; Templates</h2>
    <div class="subtitle">Bonus &mdash; everything you need is one click away.</div>
    <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:16px; margin:24px 0; max-width:980px; margin-left:auto; margin-right:auto;">
      <a href="M3%20-%20Juno%20RAG%20Lab.html" style="text-decoration:none;"><div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">Lab 1 &middot; Solo Exercise</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">Improve Juno&rsquo;s Capabilities with RAG</div>
        <div style="font-size:13px; color:#8899bb;">&rarr; Open the Juno RAG Lab Walkthrough</div>
      </div></a>
      <a href="M3%20-%20AI%20PRD%20Builder.html" style="text-decoration:none;"><div style="background:rgba(217,142,34,0.08); border:1px solid rgba(217,142,34,0.3); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#d29922; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">Lab 2 &middot; Solo Exercise</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">Specifying Juno&rsquo;s Architecture in Your AI PRD</div>
        <div style="font-size:13px; color:#8899bb;">&rarr; Open the AI PRD Builder</div>
      </div></a>
      <a href="../Final%20Project%20Brief.html" style="text-decoration:none;"><div style="background:rgba(124,140,255,0.06); border:1px solid rgba(124,140,255,0.25); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#bcb1ff; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">AI PM Certification</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">Final Project Brief &amp; Deliverables</div>
        <div style="font-size:13px; color:#8899bb;">&rarr; View resource</div>
      </div></a>
      <a href="{TEMPLATE_USE_URL}" target="_blank" rel="noopener" style="text-decoration:none;"><div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#34d399; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">Project Template &middot; One-click</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">ai-product-management-template</div>
        <div style="font-size:13px; color:#8899bb;">&rarr; Create your fork now &uarr;</div>
      </div></a>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Module 3 build - assembles all slides in the original PowerPoint flow
# ---------------------------------------------------------------------------

def build_module_3():
    sections_inst, sections_share = [], []
    add = _add_builder(sections_inst, sections_share)

    # Slide 1 - Title
    add(
        hero(
            title_lead="Improve AI Product Requirements",
            title_accent="with RAG Architecture",
            subtitle="Module 3 &middot; AI Product Management Certification",
            waypoints=[
                ("Context Engineering", "PMs own the data inputs &mdash; not just the prompt."),
                ("Lab &middot; Improve Juno with RAG", "Refactor Juno to ground decisions in RocketShip strategy."),
                ("Mapping RAG &rarr; AI PRD", "Translate retrieval levers into structured PRD requirements."),
                ("RAG Costs, Control, Trade-offs", "Tokens, context windows, the architecture choice."),
            ],
            out_line="You finish Module 3 with one artefact: <code>03-rag-prd/prd.md</code> &mdash; the AI PRD with explicit RAG architecture spec.",
            module_n=3,
        ),
        note="Module 3: Improve AI Product Requirements with RAG Architecture. Open by reframing: the spec now includes the data corpus, not just the user stories.",
    )

    # Slide 2 - Class Expectations
    add(class_expectations(), note="Same expectations as M1/M2. Cameras-on for live cohort, async etiquette for solo learners. 100% solo course - no group work.")

    # Slide 3 - Recall: M1 + M2 deliverables in repo
    add(m3_repo_recall(), note="Confirm M1+M2 commits. Anyone missing - 2 min to commit. M2 said WHAT Juno bets on. M3 specifies WHICH data proves it.")

    # Slide 4 - Final Project Progress (where M3 fits)
    add(m3_final_project_progress(), note="Set the stakes: today produces 1 of the 7 final-project deliverables - the AI PRD. Must be committed by end of session.")

    # Slide 5 - Syllabus visual (M3 highlighted)
    add(syllabus_visual_m3(), note="Show progression. M1+M2 done. M3 today. Each module's deliverable compounds into the final Juno copilot.")

    # Slide 6 - Agenda
    add(agenda_4_m3(), note="The four numbered sections of Module 3.")

    # ====== SECTION 1 - The Power of Context and Context Engineering ======
    add(section_divider("01", "The Power of Context and Context Engineering"),
        note="Section 1 - PMs move from prompt-tuners to data-strategists. Context engineering is where systems become real products.")

    # Slide 8 - Prompt vs Context Engineering
    add(prompt_vs_context_engineering(),
        note="Earlier in this course, prompt engineering was the new PM execution language. Still true - but it can only get you so far. Context engineering is where AI becomes a real product.")

    # Slide 9 - RAG Process Overview (3-step)
    add(rag_process_overview(),
        note="Quick review of RAG. Three steps: Retrieve, Augment, Generate. The library you curate determines the answer quality.")

    # Slide 10 - How RAG Works in Practice (technical diagram)
    add(rag_in_practice_diagram(),
        note="Two loops: offline data prep (A-D) + online RAG (1-5). PMs own what goes into the library. Engineers own how it's stored and retrieved.")

    # Slide 11 - Solo Reflection: RAG In Your Workplace
    add(rag_workplace_solo_reflection(),
        note="Solo reflection - converted from the original instructor-led Q&A. 5 minutes. Drop a one-liner in #ai-pm-cohort. Forces personal application.")

    # ====== SECTION 2 - Hands-On Lab: Improve Juno's Capabilities with RAG ======
    add(section_divider("02", "Hands-On Lab &mdash; Improve Juno&rsquo;s Capabilities with RAG"),
        note="Section 2 - the Lovable refactor. Evolve Juno from generic assistant into RAG-grounded copilot.")

    # Slide 13 - Lab Outcome Preview
    add(lab1_outcome_preview(),
        note="Sneak peek of what students build. Before: 3-column generic. After: 4-column RAG-grounded with citations. The unlock is the 'no longer guessing - now citing' moment.")

    # Slide 14 - Lab 1 (SOLO): Improve Juno's Capabilities with RAG
    add(applied_work(
            title="Improve Juno&rsquo;s Capabilities with RAG",
            goal="Evolve Juno from a generic assistant into a judgment-scaling PM copilot grounded in RocketShip&rsquo;s strategy.",
            body_html=JUNO_RAG_LAB_BODY,
            repo_path="juno-pm/03-rag-prd/prd.md (lab section: Diagnostic Diff)",
            timer_min=30,
            tool_url="../Modules/M3%20-%20Juno%20RAG%20Lab.html",
            tool_desc="4-step Lovable walkthrough &middot; Pre-loaded RAG Refactor + Logic Ingestion prompts &middot; Test transcript + RocketShip strategy &middot; Click-to-copy each step.",
        ),
        note="30-minute solo build. The original PowerPoint already framed this as an Individual Exercise - the tool replaces the walkthrough doc. Watch for: students must click 'Approve' for Lovable Cloud or Juno stays in mock mode.")

    # ====== SECTION 3 - Mapping RAG To Your AI PRD ======
    add(section_divider("03", "Mapping RAG To Your AI PRD"),
        note="Section 3 - turn RAG mechanics into structured PRD requirements that engineers can build from.")

    # Slide 16 - What's New in an AI PRD (7 pillars)
    add(ai_prd_pillars_7(),
        note="Traditional PRD = if-then rules. AI PRD = statistical thresholds. Walk through the 7 new pillars - this is the framework that survives engineering review.")

    # Slide 17 - How to Incorporate RAG Into Your Requirements (4-step mapping)
    add(rag_into_requirements_4(),
        note="Each RAG step maps to a specific PRD section. This is the 'how do I write this down?' answer. Step 0 is Data Prep - PM-owned. Without it, no Retrieval works.")

    # Slide 18 - Three Key RAG Trade-offs
    add(rag_tradeoffs_3(),
        note="Every benefit has a price tag. Document trade-offs explicitly in the PRD - what the system values and what it gives up.")

    # Slide 19 - Break (5 min)
    add(break_section(), note="5-minute break.")

    # Slide 20 - Cameras On reminder
    add(cameras_on(), note="Cameras-on reminder for live cohort.")

    # ====== SECTION 4 - RAG Costs, Control, and Trade-offs ======
    add(section_divider("04", "RAG Costs, Control, and Trade-offs"),
        note="Section 4 - the economics + governance of RAG. Tokens, context windows, architecture choice.")

    # Slide 22 - Data Preparation Responsibilities
    add(data_preparation_responsibilities(),
        note="PMs own what the AI is allowed to know. Authoritative sources + freshness SLAs + ingestion rules. Permissions are a product decision.")

    # Slide 23 - Augmentation Considerations (Filters / Top-K / Re-Ranking)
    add(augmentation_considerations(),
        note="The transition from prompt to context engineering. Three levers - all spec'd in the PRD.")

    # Slide 24 - Physics of RAG (Tokens + Context Windows)
    add(physics_of_rag(),
        note="Tokens are the unit of compute. Context window is the model's short-term memory. PM defines the token ceiling in the PRD.")

    # Slide 25 - Choosing Your RAG Architecture (Long Context vs RAG vs Hybrid)
    add(rag_architecture_choices_3(),
        note="Each choice steers unit economics + UX. Long Context = V1 fast. RAG = scale. Hybrid = mature products.")

    # Slide 26 - Architecture Decision Factors (Where / How / Scale)
    add(architecture_decision_factors_3(),
        note="The three levers Engineering will press you on. Where = data dynamics. How = user task. Scale = library size.")

    # Slide 27 - Lab 2 (SOLO): Specifying Juno's Architecture in Your AI PRD
    add(applied_work(
            title="Specifying Juno&rsquo;s Architecture in Your AI PRD",
            goal="Define the technical infrastructure for Juno&rsquo;s &lsquo;Evidence Engine&rsquo; &mdash; the RAG architecture, search logic, and cost trade-offs that justify prioritization decisions with verifiable data.",
            body_html=JUNO_PRD_LAB_BODY,
            repo_path="juno-pm/03-rag-prd/prd.md",
            timer_min=30,
            tool_url="../Modules/M3%20-%20AI%20PRD%20Builder.html",
            tool_desc="Four sections (Data &middot; Model &middot; Costs/Latency &middot; UX) with Juno seeds + inline Airbnb worked example. Self-review checklist. Copy as markdown straight to your repo.",
        ),
        note="30-minute solo build - the M3 final-project deliverable. The original PowerPoint called this a 'Breakout Group Exercise' - converted to 100% solo per the solo-only course design. Push back on anyone who skips justifications - 'Hybrid' alone is not an answer.")

    # Slide 28 - Key Takeaways
    add(takeaways(
            "Improve AI Product Requirements with RAG Architecture",
            [
                ("Context engineering is where AI becomes real products.",
                 "Prompts shape behaviour. Context shapes truth. PMs own the data inputs."),
                ("Strategic PMs tune Top-K, latency, and accuracy trade-offs.",
                 "These technical choices directly impact unit economics and UX."),
                ("Define ingestion, chunking, and metadata in the AI PRD.",
                 "Bridge the gap between high-level specs and a real RAG knowledge library."),
                ("Architecture choice = implementation speed vs cost vs control.",
                 "RAG, Long Context, or Hybrid - pick the trade-off that fits the bet."),
            ],
        ),
        note="Recap. The AI PRD is now committed - one of the seven final-project deliverables.")

    # Slide 29 - Extra Practice
    add(extra_practice(
            [
                ("Prompt-to-RAG Prototype", "From a real workplace corpus",
                 "Identify one high-value Knowledge Source from your real-world job &mdash; your team&rsquo;s PRD folder, an API doc set, or your last 5 customer transcripts. Rewrite the example System Prompt with citation + grounding instructions. Define your Top-K to prevent hallucinated company facts."),
                ("Real-World PRD Snippet", "A RAG-backed feature you wish existed",
                 "Draft a Model + Data requirement snippet for a feature in your current product. Use the four sections from today&rsquo;s lab (Data, Model, Costs, UX) to spec a RAG-backed feature for your own product."),
            ],
            "<strong>Next session: Module 4</strong> &mdash; <em>Design AI-Native User Experiences</em>. Master AI-native UX principles to move beyond chat interfaces and design systems that prioritize user agency and trust.",
        ),
        note="Extra practice is optional. Encourage learners to apply the AI PRD framework to a real workplace bet - not just Juno.")

    # Slide 30 - Resources & Templates
    add(m3_resources_templates(),
        note="Both lab tools surfaced + Final Project Brief + one-click template create. No thank-you slide - matches M1/M2 final convention.")

    # Slide 31 - Q&A
    add(qa_section(), note="Async-only Q&A. Park unresolved questions in #ai-pm-cohort. Instructor responds in-thread within ~5 days.")

    return sections_inst, sections_share
