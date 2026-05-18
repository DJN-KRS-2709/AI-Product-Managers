"""Module 2 - Validate AI Opportunities and Technical Feasibility.

This file holds the full M2 deck implementation. Mirrors m1_v2.py's structure:
- Reuses shared helpers from gen_module_decks (hero, applied_work, takeaways, etc.)
- Reuses class_expectations / cameras_on / thank_you / section_divider from m1_v2
- Defines M2-specific visual helpers for each lecture / framework slide
- Exposes build_module_2() which returns (sections_inst, sections_share)

Voice: solo only. The two original "Breakout Group Exercises" - Mapping
Juno's Strategic Bet and Build Juno's AI Strategy One-Pager - are
converted to Individual Exercises (this is the project's solo-only rule).
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


def thank_you_m2() -> str:
    """Module 2 sign-off."""
    return """<section class="centered" data-title="Thank you">
  <div class="inner">
    <div style="font-size:80px; margin-bottom:20px;">&#x1F4A5;</div>
    <h2 style="font-size:64px; margin-bottom:12px;">Thank you</h2>
    <div class="subtitle" style="font-size:20px; max-width:560px;">Commit your Module 2 artefacts &mdash; <code>decision-matrix.md</code> + <code>strategy-one-pager.md</code>. See you in Module 3: Improve AI Product Requirements with RAG Architecture.</div>
  </div>
</section>
"""


TEMPLATE_REPO_URL = "https://github.com/DJN-KRS-2709/ai-product-management-template"
TEMPLATE_USE_URL = (
    "https://github.com/new?template_name=ai-product-management-template"
    "&template_owner=DJN-KRS-2709"
)


# ---------------------------------------------------------------------------
# Recall / final-project bookkeeping slides
# ---------------------------------------------------------------------------

def m2_repo_recall() -> str:
    """What you committed in M1, what M2 will add to your repo today."""
    m1_items = [
        ("01-prompting/system-prompt.md", "Juno's job description"),
        ("01-prompting/lovable-prototype.md", "V1 dashboard URL"),
    ]
    m2_items = [
        ("02-strategy/decision-matrix.md", "Three-Layer + autonomy mapping"),
        ("02-strategy/strategy-one-pager.md", "6-section strategy one-pager"),
    ]
    m1_html = "".join(
        f'<li style="font-size:13.5px; color:#cdd5e3; padding:6px 0 6px 22px; position:relative; line-height:1.55;">'
        f'<span style="position:absolute; left:0; top:8px; width:14px; height:14px; border-radius:50%; background:#34d399; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:9px; font-weight:900;">&check;</span>'
        f'<code style="font-size:0.92em; color:#79c0ff;">{p}</code> &mdash; {d}</li>'
        for p, d in m1_items
    )
    m2_html = "".join(
        f'<li style="font-size:13.5px; color:#cdd5e3; padding:6px 0 6px 22px; position:relative; line-height:1.55;">'
        f'<span style="position:absolute; left:0; top:8px; width:14px; height:14px; border-radius:50%; background:#d29922; color:#07162C; display:flex; align-items:center; justify-content:center; font-size:9px; font-weight:900;">&rarr;</span>'
        f'<code style="font-size:0.92em; color:#fcd34d;">{p}</code> &mdash; {d}</li>'
        for p, d in m2_items
    )
    return f"""<section data-title="Recall &middot; Repo so far">
  <div class="inner">
    <div class="demo-tag tag-debrief">Recall</div>
    <h2>What&rsquo;s in your <code>juno-pm</code> repo</h2>
    <div class="subtitle">Module 1 left two artefacts. Module 2 adds two more.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; max-width:880px; margin:24px auto 0;">
      <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#34d399; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:10px;">&check; Module 1 &middot; Committed</div>
        <ul style="margin:0; padding:0; list-style:none;">{m1_html}</ul>
      </div>
      <div style="background:rgba(217,142,34,0.06); border:1px solid rgba(217,142,34,0.3); border-radius:14px; padding:18px 22px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#fbbf24; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:10px;">&rarr; Module 2 &middot; Today</div>
        <ul style="margin:0; padding:0; list-style:none;">{m2_html}</ul>
      </div>
    </div>
    <p style="font-size:13px; color:#8899bb; margin-top:18px; text-align:center;">M1 was tactics. M2 is strategy. Same Juno. Bigger frame.</p>
  </div>
</section>
"""


def m2_final_project_progress() -> str:
    """Final project progress card - 7 deliverables, M2 covers 2."""
    deliv = [
        ("M1", "system-prompt.md", "done", "#34d399"),
        ("M1", "lovable-prototype.md", "done", "#34d399"),
        ("M2", "decision-matrix.md", "today", "#fbbf24"),
        ("M2", "strategy-one-pager.md", "today", "#fbbf24"),
        ("M3", "prd.md", "later", "#475569"),
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
    <h2>What you ship by the end of Module 2</h2>
    <div class="subtitle">Two of the seven certification deliverables. Both committed to <code>juno-pm/02-strategy/</code>.</div>
    <div style="display:flex; flex-direction:column; gap:5px; max-width:780px; margin:22px auto 0;">{rows}</div>
    <p style="font-size:13px; color:#8899bb; margin-top:18px; text-align:center; max-width:780px; margin-left:auto; margin-right:auto;">No Module 2, no certification. Both files have <em>Copy as markdown</em> in their tools &mdash; commit before you log off.</p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Syllabus + Agenda (M2-aware)
# ---------------------------------------------------------------------------

def syllabus_visual_m2() -> str:
    """Same six-module syllabus card, M2 highlighted."""
    items = [
        ("01", "Drive AI-First Execution with Prompting", "Adopt the new AI PM execution language to accelerate delivery and command outputs. Master the systematic use of context, parameters, and prompt engineering to guide AI behavior with precision.", "#3b82f6", False),
        ("02", "Validate AI Opportunities and Technical Feasibility", "Become an AI strategist capable of selecting and shaping AI bets that ship and move business metrics. Learn to evaluate feasibility and viability to prioritize features that deliver tangible value.", "#58a6ff", True),
        ("03", "Improve AI Product Requirements with RAG Architecture", "Bridge the gap between product specs and RAG systems. Understand how embeddings, vector stores, and retrieval impact product performance to define the technical requirements of a modern AI PRD.", "#d29922", False),
        ("04", "Design AI-Native User Experiences", "Design seamless user flows and AI features to unlock new ways for users to interact with your product. Use prototyping to validate experiences and transition from static interfaces to dynamic, intelligent systems.", "#bc8cff", False),
        ("05", "Deploy Agentic Systems and Workflows", "Transition from single prompts to autonomous agents and multi-step workflows. Configure reasoning paths and tool triggers to execute complex tasks and drive operational efficiency.", "#f85149", False),
        ("06", "Measure AI Quality with Evals and Guardrails", "Replace \"vibe checks\" with systematic evaluation harnesses to ensure production-grade performance. Build robust eval sets and safety guardrails to mitigate risk and embed trust into the user experience.", "#34d399", False),
    ]
    cells = "\n".join(
        f'    <div style="background:{("rgba(88,166,255,0.10)" if active else "rgba(255,255,255,0.04)")}; border:{("2px solid " + col if active else "1px solid rgba(255,255,255,0.08)")}; border-top:3px solid {col}; border-radius:12px; padding:22px; text-align:left; position:relative;">'
        f'{("<div style=" + chr(34) + "position:absolute; top:10px; right:14px; font-family:" + chr(39) + "Poppins" + chr(39) + ",sans-serif; font-size:9.5px; font-weight:900; color:#07162C; background:" + col + "; letter-spacing:0.14em; padding:3px 9px; border-radius:99px; text-transform:uppercase;" + chr(34) + ">You are here</div>" if active else "")}'
        f'<div style="font-family:\'Poppins\',sans-serif; font-weight:800; font-size:11px; letter-spacing:0.16em; color:{col}; margin-bottom:8px;">MODULE {n}</div>'
        f'<div style="font-size:16px; font-weight:700; color:#fff; line-height:1.3; margin-bottom:8px;">{t}</div>'
        f'<div style="font-size:13px; color:#8899bb; line-height:1.5;">{d}</div></div>'
        for n, t, d, col, active in items
    )
    return f"""<section data-title="AI Product Management Syllabus">
  <div class="inner">
    <div class="demo-tag tag-framework">Syllabus</div>
    <h2>AI Product Management Certification &mdash; six modules</h2>
    <div class="subtitle">Bridge product management and AI to build AI-powered products that create real customer value.</div>
    <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:16px; margin:24px 0;">
{cells}
    </div>
  </div>
</section>
"""


def agenda_4_m2() -> str:
    """Module 2 agenda - 4 sections."""
    items = [
        ("01", "Where Does AI Actually Fit In Your Product?"),
        ("02", "Balancing AI Bets With Autonomy"),
        ("03", "Making Product Decisions Based on Technical Needs"),
        ("04", "AI Strategy One-Pager"),
    ]
    cells = "\n".join(
        f'    <div style="display:flex; gap:24px; align-items:center; padding:20px 26px; background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.18); border-radius:14px;">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-weight:900; font-size:38px; color:#60a5fa; min-width:72px; line-height:1;">{n}</div>'
        f'<div style="font-size:18px; font-weight:700; color:#fff; line-height:1.3; text-align:left;">{t}</div></div>'
        for n, t in items
    )
    return f"""<section data-title="Agenda">
  <div class="inner">
    <div class="demo-tag tag-framework">Today</div>
    <h2>Agenda</h2>
    <div style="display:flex; flex-direction:column; gap:12px; margin:24px 0; max-width:760px;">
{cells}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 1 - Where Does AI Actually Fit In Your Product?
# ---------------------------------------------------------------------------

def fake_good_vs_boring_killer() -> str:
    """Side-by-side VS comparison: Fake Good vs Boring Killer."""
    return """<section data-title="Fake Good vs Boring Killer">
  <div class="inner">
    <div class="demo-tag tag-framework">Filter</div>
    <h2>Fake Good vs Boring Killer</h2>
    <div class="subtitle">Two filters keep a quarter from disappearing on demo-driven hype.</div>

    <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:14px; align-items:stretch; margin:24px 0;">

      <!-- Fake Good: shiny distraction -->
      <div style="background:linear-gradient(180deg, rgba(100,116,139,0.06), rgba(100,116,139,0.02)); border:1px dashed rgba(148,163,184,0.4); border-radius:14px; padding:18px 22px; text-align:left; opacity:0.92;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
          <div style="display:flex; align-items:center; gap:10px;">
            <div style="font-size:24px; filter:grayscale(0.3);">&#x1FA84;</div>
            <div style="font-family:'Poppins',sans-serif; font-size:12px; font-weight:900; color:#94a3b8; letter-spacing:0.13em; text-transform:uppercase;">Fake Good</div>
          </div>
          <span style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:800; color:#94a3b8; letter-spacing:0.16em; padding:3px 9px; background:rgba(148,163,184,0.12); border:1px solid rgba(148,163,184,0.25); border-radius:99px; text-transform:uppercase;">Shiny distraction</span>
        </div>
        <p style="font-size:13.5px; color:#cdd5e3; line-height:1.55; margin:0 0 12px;">Looks impressive in a demo. Provides little utility. Slapped on without respecting the user workflow. Ignored after novelty wears off.</p>
        <div style="background:rgba(0,0,0,0.28); border:1px dashed rgba(148,163,184,0.2); border-radius:8px; padding:10px 12px; font-family:'IBM Plex Mono',monospace; font-size:11px; color:#94a3b8; line-height:1.55; font-style:italic;">
          &ldquo;Generic chatbots on every screen that hallucinate or loop&rdquo; &middot; &ldquo;AI summary tools that just add words&rdquo;
        </div>
      </div>

      <!-- VS divider -->
      <div style="display:flex; align-items:center; justify-content:center; padding:0 4px;">
        <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:900; color:#60a5fa; letter-spacing:0.18em; text-transform:uppercase; padding:6px 12px; background:rgba(96,165,250,0.1); border:1px solid rgba(96,165,250,0.3); border-radius:99px;">VS</div>
      </div>

      <!-- Boring Killer: workflow engine -->
      <div style="background:linear-gradient(180deg, rgba(96,165,250,0.1), rgba(96,165,250,0.03)); border:1px solid rgba(96,165,250,0.45); border-radius:14px; padding:18px 22px; text-align:left; box-shadow:0 0 0 1px rgba(96,165,250,0.08), 0 12px 32px rgba(96,165,250,0.12), inset 0 0 24px rgba(96,165,250,0.04);">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
          <div style="display:flex; align-items:center; gap:10px;">
            <div style="font-size:24px;">&#x2699;</div>
            <div style="font-family:'Poppins',sans-serif; font-size:12px; font-weight:900; color:#60a5fa; letter-spacing:0.13em; text-transform:uppercase;">Boring Killer</div>
          </div>
          <span style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:800; color:#34d399; letter-spacing:0.16em; padding:3px 9px; background:rgba(52,211,153,0.14); border:1px solid rgba(52,211,153,0.3); border-radius:99px; text-transform:uppercase;">Workflow engine</span>
        </div>
        <p style="font-size:13.5px; color:#cdd5e3; line-height:1.55; margin:0 0 12px;">Silent, high-reliability AI that solves unglamorous problems. Removes friction, reduces error, accelerates the repetitive. Becomes essential.</p>
        <div style="background:rgba(0,0,0,0.34); border:1px solid rgba(96,165,250,0.18); border-radius:8px; padding:10px 12px; font-family:'IBM Plex Mono',monospace; font-size:11px; color:#79c0ff; line-height:1.55;">
          &ldquo;Auto-reconcile support tickets to CRM data&rdquo; &middot; &ldquo;Copilot that turns interview notes into PRD drafts&rdquo;
        </div>
      </div>
    </div>

    <p style="font-size:13px; color:#cdd5e3; text-align:center; margin:0; max-width:760px; margin-left:auto; margin-right:auto; padding:10px 18px; background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.18); border-radius:99px;">
      <span style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#60a5fa; letter-spacing:0.14em; text-transform:uppercase;">Punchline</span>
      &nbsp;&nbsp;If you can&rsquo;t map your AI feature to concrete leverage in a real workflow, it probably shouldn&rsquo;t be built.
    </p>
  </div>
</section>
"""


def boring_killer_solo_reflection() -> str:
    """Was: instructor-led Q&A. Now: solo reflection with Slack post."""
    return """<section data-title="Solo Reflection: Fake Good or Boring Killer?">
  <div class="inner">
    <div class="demo-tag tag-debrief">Solo Reflection &middot; 5 min</div>
    <h2>Fake Good or Boring Killer?</h2>
    <div class="subtitle">Sit with two questions. Post your answers in <code>#ai-pm-cohort</code>.</div>
    <div style="display:flex; flex-direction:column; gap:14px; margin:22px 0; max-width:780px; margin-left:auto; margin-right:auto;">
      <div style="background:rgba(148,163,184,0.06); border:1px dashed rgba(148,163,184,0.4); border-radius:0 12px 12px 0; border-left:3px solid #94a3b8; padding:16px 22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
          <span style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#94a3b8; letter-spacing:0.16em; text-transform:uppercase; padding:3px 9px; background:rgba(148,163,184,0.12); border-radius:99px;">&#x1FA84; Fake Good</span>
          <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#94a3b8; letter-spacing:0.08em; text-transform:uppercase;">Question 1</div>
        </div>
        <p style="font-size:15.5px; color:#e0e0f0; line-height:1.55; margin:0;">In your own experience managing or using AI-powered products, where has a flashy AI feature flopped &mdash; and why?</p>
      </div>
      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.3); border-radius:0 12px 12px 0; border-left:3px solid #60a5fa; padding:16px 22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
          <span style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#60a5fa; letter-spacing:0.16em; text-transform:uppercase; padding:3px 9px; background:rgba(96,165,250,0.12); border-radius:99px;">&#x2699; Boring Killer</span>
          <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#60a5fa; letter-spacing:0.08em; text-transform:uppercase;">Question 2</div>
        </div>
        <p style="font-size:15.5px; color:#e0e0f0; line-height:1.55; margin:0;">Where has a quiet automation become indispensable in your daily workflow &mdash; the thing you&rsquo;d riot if it disappeared?</p>
      </div>
    </div>
    <p style="font-size:13.5px; color:#8899bb; max-width:720px; margin:14px auto 0;"><strong style="color:#cdd5e3;">Takeaway:</strong> &ldquo;Boring killer&rdquo; sounds negative. It&rsquo;s key to building an AI strategy that ships, instead of chasing the next shiny demo.</p>
  </div>
</section>
"""


def ai_value_props_4() -> str:
    """Four ways AI creates value - 2x2 grid with company examples."""
    items = [
        ("&#x1F4B8;", "Automation", "#3b82f6", "Remove manual, repetitive work.",
         [("Zapier", "auto-connects tools so leads/data flow without human effort"),
          ("Zendesk AI", "auto-resolves ~40% of tickets before they hit a human")]),
        ("&#x1F680;", "Augmentation", "#79c0ff", "Make humans 2&ndash;10x faster or smarter.",
         [("GitHub Copilot", "suggests entire functions in context"),
          ("Glean &middot; Salesforce Agentforce", "kills the &ldquo;where is that doc&rdquo; tax")]),
        ("&#x1F50D;", "Insights", "#d29922", "Find patterns and signals in messy data.",
         [("Gong", "analyses sales calls to surface what top performers say"),
          ("Tableau Pulse &middot; Fullstory", "explains <em>why</em> users churn, not just <em>that</em> they did")]),
        ("&#x2728;", "Personalization", "#bcb1ff", "Adapt to each user in real time.",
         [("Spotify AI DJ", "synthetic voice + probabilistic models &mdash; unique per listener"),
          ("Netflix", "homepage adapts in real time to today&rsquo;s viewing intent")]),
    ]
    cells = "\n".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid rgba(255,255,255,0.08); border-top:3px solid {col}; border-radius:12px; padding:14px 18px; text-align:left;">'
        f'<div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">'
        f'<div style="font-size:22px;">{ic}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:14px; font-weight:900; color:{col}; letter-spacing:0.04em;">{t}</div></div>'
        f'<p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 8px;">{d}</p>'
        + "".join(
            f'<div style="display:flex; align-items:baseline; gap:8px; padding:5px 0; border-top:1px solid rgba(255,255,255,0.06);">'
            f'<code style="font-size:11px; color:{col}; font-weight:700; flex-shrink:0;">{co}</code>'
            f'<span style="font-size:11.5px; color:#cdd5e3; line-height:1.45;">{ex}</span></div>'
            for co, ex in examples
        )
        + "</div>"
        for ic, t, col, d, examples in items
    )
    return f"""<section data-title="Four Ways AI Creates Value">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>Four Ways AI Creates Real Value</h2>
    <div class="subtitle">If your bet doesn&rsquo;t ladder to one of these &mdash; it&rsquo;s probably a distraction.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; max-width:880px; margin:24px auto 0;">
{cells}
    </div>
    <p style="font-size:13px; color:#8899bb; text-align:center; margin-top:16px; max-width:760px; margin-left:auto; margin-right:auto;">As a PM, ask: which of these four can my bet turn into <em>high-leverage</em>? If none &mdash; kill it.</p>
  </div>
</section>
"""


def three_layer_model_visual() -> str:
    """Three-Layer Model with Juno example - stacked SVG-styled cards with downward arrows."""
    layers = [
        ("01", "User Workflow", "#3b82f6", "&#x1F464;",
         "Identify the specific Job-to-be-Done or friction point in the user&rsquo;s current journey.",
         "A PM needs to synthesise 10 user interviews into a strategy doc."),
        ("02", "Technical AI Solution", "#79c0ff", "&#x2699;",
         "Determine which technical solution (LLM &middot; RAG &middot; Agentic &middot; Multimodal) best addresses that step.",
         "Multimodal RAG &mdash; processes interview transcripts <em>and</em> screenshots."),
        ("03", "Business Outcome", "#34d399", "&#x1F4C8;",
         "Define the macro goal this bet moves &mdash; revenue, cost, or risk &mdash; with a measurable metric.",
         "Reduce discovery cycle time from 5 days to 4 hours per feature."),
    ]
    cards = []
    for i, (num, t, col, ic, desc, ex) in enumerate(layers):
        is_last = (i == len(layers) - 1)
        cards.append(
            f'<div style="background:linear-gradient(135deg, {col}1a, {col}05); border:1px solid {col}40; border-left:4px solid {col}; border-radius:12px; padding:14px 20px; text-align:left;">'
            f'<div style="display:flex; align-items:center; gap:14px; margin-bottom:6px;">'
            f'<div style="font-family:\'Poppins\',sans-serif; font-size:11px; font-weight:900; color:{col}; letter-spacing:0.16em; min-width:52px;">LAYER {num}</div>'
            f'<div style="font-size:20px;">{ic}</div>'
            f'<div style="font-family:\'Poppins\',sans-serif; font-size:16px; font-weight:800; color:#fff; letter-spacing:-0.005em;">{t}</div></div>'
            f'<p style="font-size:13px; color:#cdd5e3; line-height:1.55; margin:0 0 8px; padding-left:66px;">{desc}</p>'
            f'<div style="margin-left:66px; background:rgba(0,0,0,0.28); border:1px solid {col}30; border-radius:6px; padding:7px 12px; font-family:\'IBM Plex Mono\',monospace; font-size:11px; color:{col}; line-height:1.45;">'
            f'<strong style="color:#cdd5e3;">Juno:</strong> {ex}</div>'
            f'</div>'
        )
        if not is_last:
            cards.append(
                '<div style="display:flex; justify-content:center; padding:1px 0;">'
                '<div style="font-size:18px; color:#60a5fa; line-height:1;">&darr;</div></div>'
            )
    body = "\n".join(cards)
    return f"""<section data-title="The Three-Layer Model">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>The Three-Layer Model</h2>
    <div class="subtitle">Align three layers to get a green light. If you can&rsquo;t draw a straight line through all three, it&rsquo;s tech experimentation, not strategy.</div>
    <div style="display:flex; flex-direction:column; gap:0; max-width:880px; margin:22px auto 0;">
{body}
    </div>
    <p style="font-size:12.5px; color:#8899bb; text-align:center; margin-top:14px;">Stop &ldquo;solutioning&rdquo; from a cool capability. Work outside-in: friction &rarr; capability &rarr; metric.</p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 2 - Balancing AI Bets With Autonomy
# ---------------------------------------------------------------------------

def autonomy_levels_3() -> str:
    """Three autonomy levels - Assist / Copilot / Agent. Visual progression."""
    items = [
        ("&#x1F590;", "Assist", "#34d399", "Human in the driver&rsquo;s seat",
         "AI provides suggestions or nudges. Human acts. Safest starting point.",
         "Predictive search bar &middot; tag suggester &middot; spell-check",
         "Use when hallucination is high-risk and the user must own the data."),
        ("&#x1F9D1;&#x200D;&#x1F4BB;", "Copilot", "#60a5fa", "Human reviews and approves",
         "AI drafts content / proposes multi-step workflows. Human approves.",
         "PRD draft from research &middot; first-draft email &middot; code suggestions",
         "Use when 10x speed gains matter but accuracy is non-negotiable."),
        ("&#x1F916;", "Agent", "#bcb1ff", "End-to-end with guardrails",
         "Human sets the goal. AI orchestrates tools to finish the job.",
         "Updates CRM + project tools simultaneously &middot; multi-step workflows",
         "Use when the cost of error is bounded and guardrails are explicit."),
    ]
    cells = []
    for i, (ic, t, col, sub, desc, ex, when) in enumerate(items):
        # Add an autonomy slider visualisation (3 dots, the active one filled)
        dots = "".join(
            f'<div style="width:8px; height:8px; border-radius:50%; background:{col if j == i else "rgba(255,255,255,0.15)"}; box-shadow:{(f"0 0 8px {col}aa" if j == i else "none")};"></div>'
            for j in range(3)
        )
        cells.append(
            f'<div style="background:rgba(255,255,255,0.035); border:1px solid rgba(255,255,255,0.08); border-top:3px solid {col}; border-radius:14px; padding:14px 18px; text-align:left;">'
            f'<div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">'
            f'<div style="display:flex; align-items:center; gap:10px;">'
            f'<div style="font-size:24px;">{ic}</div>'
            f'<div>'
            f'<div style="font-family:\'Poppins\',sans-serif; font-size:15px; font-weight:900; color:{col}; letter-spacing:0.02em;">{t}</div>'
            f'<div style="font-size:11px; color:#8899bb; letter-spacing:0.04em;">{sub}</div></div></div>'
            f'<div style="display:flex; gap:5px;">{dots}</div></div>'
            f'<p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:8px 0 8px;">{desc}</p>'
            f'<div style="background:rgba(0,0,0,0.28); border-radius:6px; padding:6px 10px; font-family:\'IBM Plex Mono\',monospace; font-size:10.5px; color:{col}; line-height:1.5; margin-bottom:6px;">{ex}</div>'
            f'<p style="font-size:11.5px; color:#8899bb; line-height:1.5; margin:0; font-style:italic;">{when}</p>'
            f'</div>'
        )
    body = "\n".join(cells)
    return f"""<section data-title="Choosing Your Level of Autonomy">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>Choosing Your Level of Autonomy</h2>
    <div class="subtitle">Always ask: <em>what is the safest <strong>useful</strong> level here for this product?</em></div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:980px; margin:22px auto 0;">
{body}
    </div>
    <p style="font-size:12.5px; color:#8899bb; text-align:center; margin-top:14px; max-width:780px; margin-left:auto; margin-right:auto;">You don&rsquo;t always need an Agent. Sometimes a well-placed Assist is exactly what keeps the user in their flow.</p>
  </div>
</section>
"""


def strategy_lens_4quad() -> str:
    """Strategy Lens: Jobs x Risk x Autonomy 4-quadrant matrix with examples."""
    def cell(ic: str, tag: str, example: str, verdict: str, col: str) -> str:
        return (
            f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}55; border-radius:12px; padding:12px 16px; text-align:left; position:relative;">'
            f'<div style="position:absolute; top:0; left:0; right:0; height:3px; background:{col};"></div>'
            f'<div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">'
            f'<div style="font-size:20px;">{ic}</div>'
            f'<div style="font-family:\'Poppins\',sans-serif; font-size:10.5px; font-weight:900; color:{col}; letter-spacing:0.13em; text-transform:uppercase;">{tag}</div></div>'
            f'<p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 6px;">{example}</p>'
            f'<div style="font-family:\'Poppins\',sans-serif; font-size:12px; color:{col}; line-height:1.45;">{verdict}</div>'
            f'</div>'
        )
    tl = cell("&#x1F680;", "High Impact &middot; Low Risk",
              "Synthesizing 100+ raw feedback snippets into themes",
              "&rarr; Good candidate for <strong>Agent</strong>",
              "#34d399")
    tr = cell("&#x26A0;&#xFE0F;", "High Impact &middot; High Risk",
              "Auto-prioritising roadmap and changing live dates",
              "&rarr; Stay at <strong>Assist</strong>",
              "#fbbf24")
    bl = cell("&#x270D;&#xFE0F;", "Low Impact &middot; Low Risk",
              "Drafting routine stakeholder update emails",
              "&rarr; Good candidate for <strong>Copilot</strong>",
              "#60a5fa")
    br = cell("&#x1F480;", "Low Impact &middot; High Risk",
              "Automated deletion of &lsquo;inactive&rsquo; user accounts",
              "&rarr; <strong>Don&rsquo;t build.</strong>",
              "#f87171")
    label_high = '<div style="display:flex; align-items:center; justify-content:flex-end; padding-right:6px;"><div style="writing-mode:vertical-rl; transform:rotate(180deg); font-family:\'Poppins\',sans-serif; font-size:10px; font-weight:900; color:#60a5fa; letter-spacing:0.18em; text-transform:uppercase;">High Impact</div></div>'
    label_low = '<div style="display:flex; align-items:center; justify-content:flex-end; padding-right:6px;"><div style="writing-mode:vertical-rl; transform:rotate(180deg); font-family:\'Poppins\',sans-serif; font-size:10px; font-weight:900; color:#94a3b8; letter-spacing:0.18em; text-transform:uppercase;">Low Impact</div></div>'
    return f"""<section data-title="Strategy Lens: Jobs x Risk x Autonomy">
  <div class="inner">
    <div class="demo-tag tag-framework">Strategy Lens</div>
    <h2>Jobs &times; Risk &times; Autonomy</h2>
    <div class="subtitle">Cost-of-failure vs. scale-of-benefit. The matrix tells you the autonomy ceiling.</div>

    <div style="display:grid; grid-template-columns:48px 1fr 1fr; gap:10px; max-width:880px; margin:22px auto 0;">
      <div></div>
      <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#34d399; letter-spacing:0.16em; text-align:center; text-transform:uppercase; padding-bottom:4px;">&larr; Low Risk</div>
      <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#f87171; letter-spacing:0.16em; text-align:center; text-transform:uppercase; padding-bottom:4px;">High Risk &rarr;</div>

      {label_high}
      {tl}
      {tr}

      {label_low}
      {bl}
      {br}
    </div>
    <p style="font-size:12px; color:#8899bb; text-align:center; margin-top:14px; max-width:760px; margin-left:auto; margin-right:auto;">Start from a specific job-to-be-done. Ask: how risky if wrong? How impactful if right? Then pick the autonomy level.</p>
  </div>
</section>
"""


def strategic_scorecard_4() -> str:
    """Strategic Scorecard - 4 axes scored 1-5."""
    items = [
        ("&#x1F4BE;", "Data Readiness", "#3b82f6",
         "Logs, docs, and clean interaction data to fuel the AI?",
         "1: guessing", "5: structured + accessible today"),
        ("&#x1F3A8;", "UX Complexity", "#bcb1ff",
         "How hard to design a trustworthy interface for these flows?",
         "1: trivial UI tweak", "5: multi-step, high-stakes"),
        ("&#x2696;&#xFE0F;", "Risk &amp; Governance Load", "#fbbf24",
         "Regulatory, privacy, reputational risk requiring formal approval?",
         "1: no friction", "5: heavy compliance review"),
        ("&#x1F4C8;", "Potential Impact", "#34d399",
         "Will this move a core business metric &mdash; revenue, retention, quality?",
         "1: minor annoyance", "5: changes unit economics"),
    ]
    cells = "\n".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid rgba(255,255,255,0.08); border-top:3px solid {col}; border-radius:12px; padding:14px 18px; text-align:left;">'
        f'<div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">'
        f'<div style="font-size:22px;">{ic}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:13px; font-weight:900; color:{col}; letter-spacing:0.04em;">{t}</div></div>'
        f'<p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 8px;">{q}</p>'
        # 1-5 scale visualisation
        + '<div style="display:flex; gap:5px; margin-bottom:6px;">'
        + "".join(
            f'<div style="flex:1; height:6px; border-radius:3px; background:linear-gradient(90deg, {col}30, {col}80);"></div>'
            for _ in range(5)
        )
        + '</div>'
        + f'<div style="display:flex; justify-content:space-between; font-family:\'IBM Plex Mono\',monospace; font-size:10px; color:#8899bb;">'
        f'<span>{lo}</span><span>{hi}</span></div>'
        + '</div>'
        for ic, t, col, q, lo, hi in items
    )
    return f"""<section data-title="Strategic Scorecard">
  <div class="inner">
    <div class="demo-tag tag-framework">Audit</div>
    <h2>Strategic Scorecard &mdash; Which AI Bets Deserve Oxygen?</h2>
    <div class="subtitle">Filter signal from noise before a bet hits the roadmap. Score each axis 1&ndash;5.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; max-width:880px; margin:22px auto 0;">
{cells}
    </div>
    <p style="font-size:12.5px; color:#cdd5e3; text-align:center; margin:14px auto 0; max-width:780px; padding:8px 16px; background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.18); border-radius:99px;">
      <strong style="color:#60a5fa;">Sweet spot:</strong> High Impact + High Data Readiness + Manageable UX. <strong style="color:#f87171;">Filter out:</strong> Low Impact + High Risk &mdash; vanity features with massive liability.
    </p>
  </div>
</section>
"""


def responsible_ai_guardrails() -> str:
    """4 guardrails with 4 real-world stakes - Belgium, CNET, Amazon, Samsung."""
    items = [
        ("&#x1F91D;", "Human Oversight", "The Safety Valve", "#34d399",
         "AI supports decisions, not finalises them. Unmonitored autonomy &rarr; catastrophic outcomes.",
         "Belgium &middot; 2023",
         "A man tragically took his life after following advice from an unmonitored chatbot during a conversation about climate anxiety."),
        ("&#x1F50D;", "Transparency", "The Disclosure Label", "#60a5fa",
         "Distinguish human-verified from AI-generated. Hidden AI outputs destroy credibility on first error.",
         "CNET",
         "Published AI-generated finance articles with factual errors. Brand reputation hit once the lack of disclosure was revealed."),
        ("&#x2696;&#xFE0F;", "Bias Awareness", "The Equity Filter", "#fbbf24",
         "Audit training data. Biased models scale historical imbalances into legal and PR crises.",
         "Amazon",
         "AI recruitment tool penalised resumes containing the word &lsquo;women&rsquo;s&rsquo;, favouring male-coded language. Tool scrapped."),
        ("&#x1F512;", "Privacy", "The Digital Vault", "#bcb1ff",
         "Use only approved environments for proprietary data. Public LLMs are not private &mdash; leaks are permanent.",
         "Samsung",
         "Engineers leaked trade secrets by pasting confidential source code into a public LLM. Data became part of the global model."),
    ]
    cells = "\n".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-top:3px solid {col}; border-radius:12px; padding:14px 18px; text-align:left;">'
        f'<div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">'
        f'<div style="font-size:22px;">{ic}</div>'
        f'<div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:13px; font-weight:900; color:{col}; letter-spacing:0.04em;">{t}</div>'
        f'<div style="font-size:10.5px; color:#8899bb; letter-spacing:0.06em; font-style:italic;">{sub}</div></div></div>'
        f'<p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 10px;">{desc}</p>'
        f'<div style="background:rgba(0,0,0,0.32); border-left:2px solid #f87171; border-radius:0 6px 6px 0; padding:8px 12px;">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:9.5px; font-weight:900; color:#f87171; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:3px;">&#x26A0; Real-world stake &middot; {label}</div>'
        f'<p style="font-size:11.5px; color:#cdd5e3; line-height:1.5; margin:0;">{stake}</p></div>'
        f'</div>'
        for ic, t, sub, col, desc, label, stake in items
    )
    return f"""<section data-title="Responsible AI: Strategic Guardrails">
  <div class="inner">
    <div class="demo-tag tag-framework">Governance</div>
    <h2>Responsible AI &mdash; Strategic Guardrails</h2>
    <div class="subtitle">Governance is product strategy. If you don&rsquo;t bake this in now, you&rsquo;re building a corporate liability.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; max-width:980px; margin:22px auto 0;">
{cells}
    </div>
  </div>
</section>
"""


def run_through_matrix_4() -> str:
    """Run Your Bets Through the Matrix - 4 questions: Approach / Candidate / Strategy / Safety."""
    items = [
        ("&#x1F6E0;&#xFE0F;", "Approach", "#3b82f6",
         "Buy &middot; API &middot; Fine-tune &middot; RAG?",
         "Pick the technical lever for this bet.",
         "&ldquo;Copilot for PRDs &rarr; model API + RAG over research and strategy docs.&rdquo;"),
        ("&#x1F50C;", "Candidate", "#79c0ff",
         "Likely model / provider(s)?",
         "Map requirements (intelligence &middot; cost &middot; latency) to providers, not specific names.",
         "&ldquo;Need strong long context&rdquo; or &ldquo;Need image understanding for screen captures.&rdquo;"),
        ("&#x1F3D7;&#xFE0F;", "Strategy", "#fbbf24",
         "Own vs. outsource?",
         "Define what your team will operate vs. delegate to cloud / model providers.",
         "&ldquo;We own data pipelines + vector store; we outsource the base model.&rdquo;"),
        ("&#x1F6E1;&#xFE0F;", "Safety", "#34d399",
         "Key governance questions?",
         "Privacy boundaries, bias mitigation, human oversight gates &mdash; ship-readiness checks.",
         "&ldquo;What is our fallback UI if the model hallucinates? Does this data require SOC2?&rdquo;"),
    ]
    cells = "\n".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid rgba(255,255,255,0.08); border-left:3px solid {col}; border-radius:12px; padding:12px 18px; text-align:left;">'
        f'<div style="display:flex; align-items:center; gap:10px; margin-bottom:4px;">'
        f'<div style="font-size:20px;">{ic}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:13px; font-weight:900; color:{col}; letter-spacing:0.04em;">{t}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:11px; color:#8899bb; letter-spacing:0.04em;">&middot; {q}</div></div>'
        f'<p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 6px;">{desc}</p>'
        f'<div style="background:rgba(0,0,0,0.28); border-radius:6px; padding:7px 10px; font-family:\'IBM Plex Mono\',monospace; font-size:10.5px; color:{col}; line-height:1.45; font-style:italic;">{ex}</div>'
        f'</div>'
        for ic, t, col, q, desc, ex in items
    )
    return f"""<section data-title="Run Your Bets Through the Matrix">
  <div class="inner">
    <div class="demo-tag tag-framework">Pressure Test</div>
    <h2>Run Your Bets Through the Matrix</h2>
    <div class="subtitle">For each bet, answer four questions. First-pass strategy &mdash; not a full architecture review.</div>
    <div style="display:flex; flex-direction:column; gap:8px; max-width:880px; margin:22px auto 0;">
{cells}
    </div>
    <p style="font-size:12.5px; color:#8899bb; text-align:center; margin-top:14px;"><strong style="color:#cdd5e3;">Goal:</strong> a defensible story that justifies investment and path forward.</p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 4 - AI Strategy One-Pager
# ---------------------------------------------------------------------------

def one_pager_intro() -> str:
    """The one-pager is a strategic tool, not an idea deck. 3 outcomes."""
    items = [
        ("&#x1F6E1;&#xFE0F;", "Neutralize skepticism with evidence",
         "Treat it as the doc you send to a stakeholder looking for a reason to say no. Make the rationale undeniable.",
         "#34d399"),
        ("&#x1F4CD;", "Prioritize limited engineering resources",
         "Force a rigorous defence of every bet. AI features are expensive &mdash; oxygen is finite.",
         "#fbbf24"),
        ("&#x1F50E;", "Verify strategy under scrutiny",
         "Validation over inspiration. It&rsquo;s not what AI <em>could</em> do &mdash; it&rsquo;s what it <em>must</em> do to fix a real bottleneck.",
         "#60a5fa"),
    ]
    cells = "\n".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-left:3px solid {col}; border-radius:0 12px 12px 0; padding:14px 20px; text-align:left;">'
        f'<div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">'
        f'<div style="font-size:22px;">{ic}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:14px; font-weight:900; color:{col}; letter-spacing:-0.005em;">{t}</div></div>'
        f'<p style="font-size:13px; color:#cdd5e3; line-height:1.55; margin:0;">{d}</p>'
        f'</div>'
        for ic, t, d, col in items
    )
    return f"""<section data-title="AI Strategy One-Pager">
  <div class="inner">
    <div class="demo-tag tag-framework">Definition</div>
    <h2>An AI Strategy One-Pager is not an idea deck</h2>
    <div class="subtitle">It&rsquo;s a strategic tool to validate product direction &mdash; the filter between technical feasibility and business impact.</div>
    <div style="display:flex; flex-direction:column; gap:10px; max-width:880px; margin:24px auto 0;">
{cells}
    </div>
    <p style="font-size:12.5px; color:#8899bb; text-align:center; margin-top:14px; max-width:780px; margin-left:auto; margin-right:auto;">If you can&rsquo;t articulate the friction and the outcome on a single page, the project isn&rsquo;t ready for a production roadmap.</p>
  </div>
</section>
"""


def one_pager_anatomy_6() -> str:
    """6 sections of the one-pager with Grammarly worked example."""
    items = [
        ("&#x1F4DD;", "Problem &amp; Workflow", "#3b82f6",
         "The specific friction point in the user journey where manual effort hits a bottleneck.",
         "Professional writing is slow and prone to tone errors that damage credibility."),
        ("&#x1F4CA;", "Target Metrics", "#79c0ff",
         "The primary user and business KPIs that prove the AI is unblocking the team.",
         "Improved &lsquo;Time-to-Publish&rsquo; and &lsquo;Message Clarity Score&rsquo;."),
        ("&#x1F39A;&#xFE0F;", "Autonomy Level", "#bcb1ff",
         "Interaction model (Assist / Copilot / Agent). Sets clear UX expectations.",
         "Copilot &mdash; suggests rewrites, requires human approval to apply."),
        ("&#x1F5C2;&#xFE0F;", "Data &amp; Model Approach", "#fbbf24",
         "Buy (LLM) &middot; Ground (RAG) &middot; Refine (Fine-tune). Decides margins and accuracy.",
         "Hybrid &mdash; general LLMs grounded with company-specific style guides via RAG."),
        ("&#x26A0;&#xFE0F;", "Risks &amp; Mitigations", "#f87171",
         "Flag the one-way doors and the guardrails required to protect trust and data.",
         "Risk: hallucinated facts. Mitigation: scope to grammar/tone, not to factual content."),
        ("&#x1F6AA;", "V1 Scope", "#34d399",
         "In/Out boundaries. What the AI <em>won&rsquo;t</em> do is as critical as what it will.",
         "<strong>In:</strong> tone &amp; clarity edits. <strong>Out:</strong> drafting legal contracts or autonomous sending."),
    ]
    cells = "\n".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:11px 14px; text-align:left; position:relative; overflow:hidden;">'
        f'<div style="position:absolute; top:0; left:0; right:0; height:3px; background:{col};"></div>'
        f'<div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">'
        f'<div style="font-size:18px;">{ic}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:11.5px; font-weight:900; color:{col}; letter-spacing:0.06em;">{t}</div></div>'
        f'<p style="font-size:11.5px; color:#cdd5e3; line-height:1.45; margin:0 0 6px;">{d}</p>'
        f'<div style="background:rgba(0,0,0,0.28); border-radius:5px; padding:5px 9px; font-family:\'IBM Plex Mono\',monospace; font-size:10px; color:{col}; line-height:1.45;">'
        f'<span style="color:#cdd5e3; font-weight:700; font-style:normal;">Grammarly:</span> {ex}</div>'
        f'</div>'
        for ic, t, col, d, ex in items
    )
    return f"""<section data-title="One-Pager Anatomy">
  <div class="inner">
    <div class="demo-tag tag-framework">Anatomy</div>
    <h2>AI Strategy One-Pager &mdash; 6 sections</h2>
    <div class="subtitle">Past vague promises of &lsquo;intelligence&rsquo; into the reality of engineering constraints. Anchor: Grammarly.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; max-width:980px; margin:22px auto 0;">
{cells}
    </div>
    <p style="font-size:12.5px; color:#8899bb; text-align:center; margin-top:14px;">Six pillars of a defensible AI strategy. Skip one and the bet collapses under scrutiny.</p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Lab body content - reused by applied_work() helper
# ---------------------------------------------------------------------------

def _layer_card(num: str, label: str, color: str, what_to_write: str, juno_seed: str) -> str:
    """One Three-Layer Model card for the breakout 1 body."""
    return f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {color}40; border-left:4px solid {color}; border-radius:12px; padding:12px 16px; text-align:left;">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
    <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:{color}; letter-spacing:0.16em; min-width:54px;">LAYER {num}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:#fff;">{label}</div>
  </div>
  <p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 8px;">{what_to_write}</p>
  <div style="background:rgba(0,0,0,0.3); border-radius:6px; padding:7px 11px; font-family:'IBM Plex Mono',monospace; font-size:11px; color:{color}; line-height:1.5;"><strong style="color:#cdd5e3;">Juno seed:</strong> {juno_seed}</div>
</div>"""


THREE_LAYER_LAB_BODY = (
    """<p style="font-size:13.5px; color:#cdd5e3; line-height:1.5; max-width:780px; margin:0 auto 14px; padding:8px 14px; background:rgba(96,165,250,0.06); border-left:3px solid #60a5fa; border-radius:0 8px 8px 0; text-align:left;">
Assume Juno mastered the Opportunity Brief in M1. Now design the logic that turns those briefs into <strong>defensible prioritization decisions</strong>. <strong style="color:#fff;">The Three-Layer Model Mapper is your workspace</strong> &mdash; each layer has a Juno seed to pre-fill, edit, and copy.
</p>

<div style="display:flex; flex-direction:column; gap:10px; max-width:880px; margin:0 auto 12px;">
"""
    + _layer_card(
        num="01", label="User Workflow", color="#3b82f6",
        what_to_write="Where does signal collapse break decision-making today? One concrete prioritization pain point at RocketShip.",
        juno_seed="Roadmap discussions are driven by the loudest voice in Slack &mdash; not by customer evidence. The PM can&rsquo;t defend reasoning when leadership pushes back.",
    )
    + _layer_card(
        num="02", label="Technical AI Solution + Autonomy", color="#79c0ff",
        what_to_write="Pick LLM / RAG / Agentic / Multimodal &mdash; the minimum that solves the friction. Set the autonomy dial: Assist / Copilot / Agent.",
        juno_seed="<strong>RAG</strong> over the RocketShip corpus + bounded <strong>Agentic</strong> orchestration. Autonomy: <strong>Copilot</strong> &mdash; drafts a ranked backlog with reasoning; PM approves before publish.",
    )
    + _layer_card(
        num="03", label="Business Outcome", color="#34d399",
        what_to_write="One measurable metric that proves Juno&rsquo;s prioritization engine is unblocking the team.",
        juno_seed="Reduce average weekly roadmap prioritization time from <strong>2 hours to 30 minutes</strong>; cut the rate of decisions reversed within 1 week to under 10%.",
    )
    + """</div>

<p style="font-size:11.5px; color:#8899bb; max-width:780px; margin:8px auto 0; text-align:center;">
<strong>Self-review</strong> &mdash; the Mapper&rsquo;s built-in checklist. Run it before commit, then run the AI-review meta-prompt in ChatGPT/Claude.
</p>
"""
)


def _onepager_card(emoji: str, label: str, color: str, what_to_write: str, juno_seed: str) -> str:
    """One section card for the One-Pager Builder breakout body."""
    return f"""<div style="background:rgba(255,255,255,0.035); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:10px 13px; text-align:left; position:relative; overflow:hidden;">
  <div style="position:absolute; top:0; left:0; right:0; height:3px; background:{color};"></div>
  <div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">
    <div style="font-size:16px;">{emoji}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:{color}; letter-spacing:0.08em;">{label}</div>
  </div>
  <p style="font-size:11px; color:#cdd5e3; line-height:1.45; margin:0 0 6px;">{what_to_write}</p>
  <div style="background:rgba(0,0,0,0.28); border-radius:5px; padding:5px 8px; font-family:'IBM Plex Mono',monospace; font-size:9.5px; color:{color}; line-height:1.45;">{juno_seed}</div>
</div>"""


ONE_PAGER_LAB_BODY = (
    """<p style="font-size:13.5px; color:#cdd5e3; line-height:1.5; max-width:780px; margin:0 auto 12px; padding:8px 14px; background:rgba(96,165,250,0.06); border-left:3px solid #60a5fa; border-radius:0 8px 8px 0; text-align:left;">
Formalize Juno&rsquo;s prioritization engine into a <strong>defensible one-page strategy doc</strong>. Output: <code>02-strategy/strategy-one-pager.md</code>. <strong style="color:#fff;">The One-Pager Builder is your workspace</strong> &mdash; with seeds for each section, an inline Airbnb worked example, self-review, and AI-review.
</p>

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; max-width:880px; margin:0 auto 12px;">
"""
    + _onepager_card(
        emoji="&#x1F4DD;", label="Problem &amp; Workflow", color="#3b82f6",
        what_to_write="What bad decision is Juno explicitly preventing?",
        juno_seed="Prevent <em>opinion-driven</em> roadmap decisions where evidence is buried in 200+ Slack threads.",
    )
    + _onepager_card(
        emoji="&#x1F4CA;", label="Target Metrics", color="#79c0ff",
        what_to_write="Which metric would make leadership say &lsquo;don&rsquo;t touch it&rsquo;?",
        juno_seed="Cycle time 2h&rarr;30min. Reversal rate &lt; 10%.",
    )
    + _onepager_card(
        emoji="&#x1F39A;&#xFE0F;", label="Autonomy Level", color="#bcb1ff",
        what_to_write="Pick one and name what you&rsquo;re explicitly avoiding.",
        juno_seed="<strong>Copilot.</strong> Avoiding <em>Agent</em> &mdash; can&rsquo;t move headcount autonomously.",
    )
    + _onepager_card(
        emoji="&#x1F5C2;&#xFE0F;", label="Data &amp; Model", color="#fbbf24",
        what_to_write="Buy / Ground / Refine. Name the shortcut you&rsquo;re NOT taking.",
        juno_seed="<strong>Ground (RAG).</strong> Not generic LLM &mdash; would hallucinate priorities.",
    )
    + _onepager_card(
        emoji="&#x26A0;&#xFE0F;", label="Risks &amp; Mitigations", color="#f87171",
        what_to_write="One scary risk + one specific guardrail. Not a list.",
        juno_seed="Risk: AI weights latest squeaky-wheel signal. Mitigation: 7-day signal window.",
    )
    + _onepager_card(
        emoji="&#x1F6AA;", label="V1 Scope", color="#34d399",
        what_to_write="Two specific OUT items. Scope creep kills V1.",
        juno_seed="In: backlog. Out: hiring decisions, customer-facing comms.",
    )
    + """</div>

<div style="max-width:880px; margin:0 auto; background:rgba(124,140,255,0.06); border:1px solid rgba(124,140,255,0.25); border-radius:10px; padding:9px 14px; text-align:left;">
  <span style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#bcb1ff; letter-spacing:0.13em; text-transform:uppercase;">&#x1F4D6; Worked example inside the tool &middot;</span>
  <span style="font-size:12px; color:#cdd5e3;"> Airbnb&rsquo;s Smart Dispute Mediator &mdash; the same six-section anatomy, fully filled. Toggle it for inspiration on the &lsquo;explicitly avoiding&rsquo; phrasing.</span>
</div>

<p style="font-size:11.5px; color:#8899bb; max-width:780px; margin:8px auto 0; text-align:center;">
<strong>Self-review</strong> &mdash; on-tool checklist. Then AI-review: paste the markdown + meta-prompt into ChatGPT/Claude.
</p>
"""
)


# ---------------------------------------------------------------------------
# Resources & Templates
# ---------------------------------------------------------------------------

def m2_resources_templates() -> str:
    return f"""<section data-title="Resources &amp; Templates">
  <div class="inner">
    <div class="demo-tag tag-build">Resources</div>
    <h2>Resources &amp; Templates</h2>
    <div class="subtitle">Bonus &mdash; everything you need is one click away.</div>
    <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:16px; margin:24px 0; max-width:980px; margin-left:auto; margin-right:auto;">
      <a href="M2%20-%20Three-Layer%20Model%20Mapper.html" style="text-decoration:none;"><div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">Lab 1 &middot; Solo Exercise</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">Mapping Juno&rsquo;s Strategic Bet</div>
        <div style="font-size:13px; color:#8899bb;">&rarr; Open the Three-Layer Model Mapper</div>
      </div></a>
      <a href="M2%20-%20AI%20Strategy%20One-Pager%20Builder.html" style="text-decoration:none;"><div style="background:rgba(217,142,34,0.08); border:1px solid rgba(217,142,34,0.3); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#d29922; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">Lab 2 &middot; Solo Exercise</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">Build Juno&rsquo;s AI Strategy One-Pager</div>
        <div style="font-size:13px; color:#8899bb;">&rarr; Open the One-Pager Builder</div>
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
# Module 2 build - assembles all slides in the original PowerPoint flow
# ---------------------------------------------------------------------------

def build_module_2():
    sections_inst, sections_share = [], []
    add = _add_builder(sections_inst, sections_share)

    # Slide 1 - Title
    add(
        hero(
            title_lead="Validate AI Opportunities",
            title_accent="and Technical Feasibility",
            subtitle="Module 2 &middot; AI Product Management Certification",
            waypoints=[
                ("Where Does AI Actually Fit?", "Filter fake-good from boring-killer. Four value frames."),
                ("Balancing AI Bets With Autonomy", "Three-Layer Model + Jobs &times; Risk &times; Autonomy."),
                ("Making Decisions on Technical Needs", "Strategic scorecard + responsible-AI guardrails."),
                ("AI Strategy One-Pager", "Six sections that survive a board challenge."),
            ],
            out_line="You finish Module 2 with two artefacts: <code>02-strategy/decision-matrix.md</code> + <code>02-strategy/strategy-one-pager.md</code>.",
            module_n=2,
        ),
        note="Module 2: Validate AI Opportunities and Technical Feasibility. Open by reminding cohort: M1 was tactics, M2 is strategy. Same Juno PM scenario; bigger frame.",
    )

    # Slide 2 - Class Expectations (reused)
    add(class_expectations(), note="Same expectations as M1. Cameras-on for live cohort, async etiquette for solo learners. 100% solo course - no group work.")

    # Slide 3 - Recall: M1 deliverables in repo
    add(m2_repo_recall(), note="Make sure everyone has M1 committed before continuing. If not, give them 2 min to commit. M1 was tactics, M2 is strategy.")

    # Slide 4 - Final Project Progress (where M2 fits in the 7 deliverables)
    add(m2_final_project_progress(), note="Set the stakes: today produces 2 of the 7 final-project deliverables. Both must be committed by end of session.")

    # Slide 5 - Syllabus visual (M2 highlighted)
    add(syllabus_visual_m2(), note="Show progression. M1 (tactics) is done. M2 (strategy) is today. Each module's deliverable compounds into the final Juno copilot.")

    # Slide 6 - Agenda
    add(agenda_4_m2(), note="The four numbered sections of Module 2.")

    # ====== SECTION 1 - Where Does AI Actually Fit? ======
    add(section_divider("01", "Where Does AI Actually Fit In Your Product?"),
        note="Section 1 - establishing a critical eye for where AI actually belongs in a product.")

    # Slide 8 - Fake Good vs Boring Killer
    add(fake_good_vs_boring_killer(),
        note="Differentiate surface-level novelties from deep architectural leverage. Fake Good = hallucinating chatbots and circular summaries. Boring Killer = silent automation that becomes indispensable.")

    # Slide 9 - Solo Reflection: Fake Good or Boring Killer (was instructor-led Q&A)
    add(boring_killer_solo_reflection(),
        note="Solo reflection - converted from the original instructor-led Q&A. 5 minutes. Post in #ai-pm-cohort. The 'boring killer' framing is the punchline - chase the gears, not the magic wand.")

    # Slide 10 - Four Ways AI Creates Real Value
    add(ai_value_props_4(),
        note="Move from high-level business goals to specific value drivers. Force learners to label Juno's bet against one of these four. Anything that doesn't fit at least one is a distraction.")

    # Slide 11 - Three-Layer Model
    add(three_layer_model_visual(),
        note="The central mental model. Forces outside-in thinking - friction, then capability, then metric. Stops PMs from 'solutioning' from a cool capability backwards.")

    # ====== SECTION 2 - Balancing AI Bets With Autonomy ======
    add(section_divider("02", "Balancing AI Bets With Autonomy"),
        note="Section 2 - autonomy is a strategic decision, not a default. Cost of error skyrockets as autonomy rises.")

    # Slide 13 - Choosing Your Level of Autonomy
    add(autonomy_levels_3(),
        note="Three levels: Assist / Copilot / Agent. Always ask: what is the safest USEFUL level for this product? Don't reach for Agent when Assist solves it.")

    # Slide 14 - Strategy Lens: Jobs x Risk x Autonomy
    add(strategy_lens_4quad(),
        note="Four quadrants. The 'Don't Build' quadrant is the trap - low-impact + high-risk features that look like AI clean-up but carry massive liability.")

    # Slide 15 - Breakout 1 - Mapping Juno's Strategic Bet (SOLO)
    add(applied_work(
            title="Mapping Juno&rsquo;s Strategic Bet",
            goal="Apply the Three-Layer Model to Juno&rsquo;s Automated Prioritization engine - draw a straight line from friction to capability to metric.",
            body_html=THREE_LAYER_LAB_BODY,
            repo_path="juno-pm/02-strategy/decision-matrix.md",
            timer_min=25,
            tool_url="../Modules/M2%20-%20Three-Layer%20Model%20Mapper.html",
            tool_desc="Pre-seeded Juno prioritization engine. Layer 1 User Workflow &middot; Layer 2 AI Solution + Autonomy &middot; Layer 3 Business Outcome. Live preview, self-review, copy as markdown.",
        ),
        note="25-minute solo build. The original PowerPoint called this a 'Breakout Group Exercise' with permanent project teams - converted to a 100% individual exercise per the solo-only course design. Same scenario (RocketShip signal collapse, Automated Prioritization), different format.")

    # Slide 16 - Strategic Scorecard - 4 axes
    add(strategic_scorecard_4(),
        note="Use this scorecard to audit ideas before they hit the roadmap. Filter out: Low Impact + High Risk vanity features. Prefer: High Impact + High Data Readiness + Manageable UX.")

    # Slide 17 - Break (5 min)
    add(break_section(), note="5-minute break.")

    # Slide 18 - Cameras On reminder
    add(cameras_on(), note="Cameras-on reminder for live cohort.")

    # ====== SECTION 3 - Making Product Decisions Based on Technical Needs ======
    add(section_divider("03", "Making Product Decisions Based on Technical Needs"),
        note="Section 3 - not every AI opportunity should be built. Pressure-test against technical reality and responsible-AI guardrails.")

    # Slide 20 - Responsible AI Guardrails (4 with real-world stakes)
    add(responsible_ai_guardrails(),
        note="Governance is product strategy. Each guardrail has a real-world stake (Belgium, CNET, Amazon, Samsung) - use them to make the cost of getting this wrong concrete.")

    # Slide 21 - Run Your Bets Through the Matrix
    add(run_through_matrix_4(),
        note="First-pass strategy, not full architecture review. The goal is a defensible story that justifies investment.")

    # ====== SECTION 4 - AI Strategy One-Pager ======
    add(section_divider("04", "AI Strategy One-Pager"),
        note="Section 4 - the deliverable that survives a board challenge. Validation over inspiration.")

    # Slide 23 - One-Pager Intro
    add(one_pager_intro(),
        note="Reframe: this isn't a brainstorm doc. It's a strategic tool that filters technical feasibility against business impact.")

    # Slide 24 - One-Pager Anatomy (6 sections, Grammarly worked example)
    add(one_pager_anatomy_6(),
        note="Six pillars of a defensible AI strategy. Walk through Grammarly inline as the worked example - hybrid LLM + RAG approach is the punchline.")

    # Slide 25 - Breakout 2 - Build Juno's AI Strategy One-Pager (SOLO)
    add(applied_work(
            title="Build Juno&rsquo;s AI Strategy One-Pager",
            goal="Formalize Juno&rsquo;s prioritization engine into the 6-section one-pager. The defensible execution plan.",
            body_html=ONE_PAGER_LAB_BODY,
            repo_path="juno-pm/02-strategy/strategy-one-pager.md",
            timer_min=30,
            tool_url="../Modules/M2%20-%20AI%20Strategy%20One-Pager%20Builder.html",
            tool_desc="Six sections (Problem &amp; Workflow &middot; Target Metrics &middot; Autonomy Level &middot; Data &amp; Model &middot; Risks &amp; Mitigations &middot; V1 Scope). Juno seeds + inline Airbnb worked example. Self-review checklist. Copy as markdown straight to your repo.",
        ),
        note="30-minute solo build - the highest-stakes M2 deliverable. The original PowerPoint called this a 'Breakout Group Exercise' with permanent project teams - converted to 100% solo per the solo-only course design. Most learners get vague on the success metric - push for measurable in 30 days.")

    # Slide 26 - Key Takeaways
    add(takeaways(
            "Validate AI Opportunities and Technical Feasibility",
            [
                ("Three-Layer Model anchors AI to user friction.",
                 "Strategy/Mechanic/Implementation drift kills more bets than tech does. Workflow &rarr; Solution &rarr; Outcome."),
                ("Strategic scoping = identifying one-way doors.",
                 "Defining what the AI <em>won&rsquo;t</em> do is as critical as defining what it will."),
                ("Autonomy is a variable dial.",
                 "Assist / Copilot / Agent. Pick the lowest level that delivers the job."),
                ("The One-Pager aligns teams on architecture.",
                 "Six sections turn messy inputs into defensible decisions."),
            ],
        ),
        note="Recap. Two artefacts now committed for the final project.")

    # Slide 27 - Extra Practice
    add(extra_practice(
            [
                ("Map Your Own Straight Line", "Three-Layer Model",
                 "Pick a high-friction workflow in your current role. Apply the Three-Layer Model: identify the AI capability (LLM / RAG / Agentic / Multimodal) and the measurable business outcome that proves it unblocked your journey."),
                ("Set Your Personal Autonomy Dial", "Job &times; Risk",
                 "Choose a task you wish to automate. Define the interaction model (Assist / Copilot / Agent) and list the specific 'kill-switch' guardrails required for you to trust it without constant oversight."),
            ],
            "<strong>Next session: Module 3</strong> &mdash; <em>Improve AI Product Requirements with RAG Architecture</em>. Master RAG and context engineering to ground AI outputs in proprietary, verifiable data. Translate retrieval and ranking requirements into a structured AI PRD.",
        ),
        note="Extra practice is optional. Encourage learners to apply the frameworks to their own work, not just Juno.")

    # Slide 28 - Resources & Templates
    add(m2_resources_templates(),
        note="Both lab tools surfaced + Final Project Brief + one-click template create.")

    # Slide 29 - Q&A
    add(qa_section(), note="Async-only Q&A. Park unresolved questions in #ai-pm-cohort. Instructor responds in-thread within ~5 days.")

    # Slide 30 - Thank You
    add(thank_you_m2())

    return sections_inst, sections_share

