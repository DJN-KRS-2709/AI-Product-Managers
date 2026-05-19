"""Module 6 - Measure AI Quality with Evals and Guardrails.

Mirrors m1_v2 / m2_v2 / m3_v2 / m4_v2 / m5_v2 structure:
- Reuses shared helpers from gen_module_decks
- Reuses class_expectations / cameras_on / section_divider from m1_v2
- Defines M6-specific visual helpers
- Exposes build_module_6() returning (sections_inst, sections_share)

Voice: solo only. The two source breakouts ("Plan Your Eval Stack for
Juno" and "Prepare & Finalize Your Project Deliverables Deck") are
converted to individual exercises. The "Demo Your Juno Copilot" group
showcase is kept but reframed as the individual final-project
submission (repo URL into LMS within 7 days). No thank-you slide.

Source fidelity rule (RULE 0): every slide here maps 1:1 to the source
PowerPoint M6_ Measure AI Quality with Evals and Guardrails.pptx
(28 source slides). No invented slides or framings.
"""

from gen_module_decks import (
    hero,
    applied_work,
    takeaways,
    extra_practice,
    qa_section,
    break_section,
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
# Shared visual primitives (mirror M5 vocabulary exactly).
# ---------------------------------------------------------------------------
# M5 cards have a colored gradient header band (number + optional icon + name)
# followed by a body section, with optional sub-blocks separated by horizontal
# dividers. See m5_v2.evolution_of_value(), control_panel(), awspec_blueprint().

def _m5_card(n, col, name, body_html, sub_blocks=None, icon=""):
    """Card with colored gradient header (number + name) + body + optional sub-blocks.

    Mirrors the card pattern used across m5_v2.py (evolution_of_value,
    real_world_agents, control_panel, etc.) so M5 and M6 share one
    visual vocabulary.
    """
    sub_html = "".join(
        f"""<div style="padding:13px 20px; border-top:1px solid rgba(255,255,255,0.06);">
  <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:{col}; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:4px;">{label}</div>
  <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">{content}</p>
</div>"""
        for label, content in (sub_blocks or [])
    )
    icon_html = f'<div style="font-size:22px; line-height:1;">{icon}</div>' if icon else ""
    return f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; overflow:hidden; text-align:left; display:flex; flex-direction:column;">
  <div style="padding:16px 20px; background:linear-gradient(135deg, {col}22 0%, transparent 70%); border-bottom:1px solid {col}30;">
    <div style="display:flex; align-items:center; gap:10px;">
      <div style="font-family:'Poppins',sans-serif; font-size:30px; font-weight:900; color:{col}; line-height:1;">{n}</div>
      {icon_html}
      <div style="font-family:'Poppins',sans-serif; font-size:17px; font-weight:800; color:#fff; line-height:1.3;">{name}</div>
    </div>
  </div>
  <div style="padding:13px 20px;">
    {body_html}
  </div>
  {sub_html}
</div>"""


def _m5_annotation(col: str, label: str, body_html: str) -> str:
    """Side annotation box like M5 react_pattern (Mechanism / Value / Cost)."""
    return f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:12px; padding:14px 18px;">
  <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:{col}; font-weight:900; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:6px;">{label}</div>
  <p style="font-size:13px; color:#cdd5e3; margin:0; line-height:1.6;">{body_html}</p>
</div>"""


def _m5_callout(body_html: str) -> str:
    """Bottom purple-tinted PM-rule callout used throughout M5."""
    return f"""<p style="font-size:12px; color:#bcb1ff; max-width:880px; margin:18px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
  {body_html}
</p>"""


# ---------------------------------------------------------------------------
# Source slide 3 - Syllabus
# ---------------------------------------------------------------------------

def syllabus_visual_m6() -> str:
    """6-card syllabus, M6 highlighted (current), M1-M5 marked done."""
    modules = [
        (1, "Drive AI-First Execution with Prompting",
         "Master systematic context, parameters, and prompt engineering to guide AI behavior with precision.",
         "done"),
        (2, "Validate AI Opportunities and Technical Feasibility",
         "Evaluate feasibility and viability to prioritize features that ship and move business metrics.",
         "done"),
        (3, "Improve AI Product Requirements with RAG Architecture",
         "Bridge product specs and RAG systems. Define embeddings, vector stores, and retrieval logic.",
         "done"),
        (4, "Design AI-Native User Experiences",
         "Design seamless flows that unlock new ways for users to interact. Prototype to validate.",
         "done"),
        (5, "Deploy Agentic Systems and Workflows",
         "From single prompts to autonomous agents and multi-step workflows. Configure reasoning paths and tool triggers.",
         "done"),
        (6, "Measure AI Quality with Evals and Guardrails",
         "Replace vibe checks with eval harnesses, golden sets, and safety guardrails to ship production-grade AI.",
         "current"),
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
    <div class="subtitle">Five modules done. Today &mdash; build the trust architecture that turns prototype into product.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1040px; margin:24px auto 0;">
      {''.join(cells)}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Source slide 4 - Agenda
# ---------------------------------------------------------------------------

def agenda_6() -> str:
    """4 numbered sections — mirrors M5 agenda_5 visual rhythm (M5 colour-strip
    cards). Source has 4 items; rendered as 2x2 to keep card breathing room
    consistent with M5 (3 cards in a row at the same density)."""
    items = [
        ("01", "Production-Grade Evaluation Requirements",
         "Why vibe checks fail in production. The 95% accuracy trap. The gap between lab and reality.", "#3b82f6"),
        ("02", "Measuring AI-Powered Product Outputs",
         "The AI Eval Stack. Build a Human Eval Rubric. Real-world example: Google Assistant.", "#fbbf24"),
        ("03", "AI Levers for Output Optimization",
         "Operationalising AI risks. Governance framework. Three levers: Prompt &middot; Model &middot; Data.", "#34d399"),
        ("04", "Final Project Showcase: Demo Your Juno Copilot",
         "Solo course adaptation: finalise your repo, record an optional Loom, submit URL to LMS within 7 days.", "#bcb1ff"),
    ]
    cards = "".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-left:4px solid {col}; border-radius:12px; padding:16px 22px; text-align:left;">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:32px; font-weight:900; color:{col}; line-height:1; margin-bottom:6px;">{n}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:14.5px; font-weight:700; color:#fff; margin-bottom:6px; line-height:1.3;">{title}</div>'
        f'<p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0;">{desc}</p>'
        f'</div>'
        for n, title, desc, col in items
    )
    return f"""<section data-title="Agenda">
  <div class="inner">
    <div class="demo-tag tag-debrief">Agenda</div>
    <h2>Today&rsquo;s flow</h2>
    <div class="subtitle">Two solo labs anchor the day &mdash; plan your Eval Stack, then finalise your project repo.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
    {_m5_callout('<strong style="color:#fff;">Solo course adaptation:</strong> the &ldquo;group showcase&rdquo; in section 04 becomes an individual repo submission &mdash; an optional 3-min Loom recording is encouraged but not required.')}
  </div>
</section>
"""



# ---------------------------------------------------------------------------
# Section 01 - Production-Grade Evaluation Requirements
# ---------------------------------------------------------------------------

def vibe_checks_fail() -> str:
    """Source slide 6 - Why "Vibe Checks" Fail in Production.

    3-card layout mirroring M5 evolution_of_value: gradient header band
    + body + sub-block per card.
    """
    cards = [
        ("01", "#3b82f6", "&#x1F4A1;", "Invisible Failures",
         "A single successful output proves an AI <em>can</em> perform a task &mdash; not that it <em>will</em> reliably across 1,000 different intents.",
         "Without systematic measurement, high-stakes hallucinations and edge cases stay invisible until they reach the end user."),
        ("02", "#fbbf24", "&#x1F441;&#xFE0F;", "The Subjectivity Trap",
         "Relying on &ldquo;does this look good?&rdquo; creates a vibe-check culture that can&rsquo;t scale or provide objective data.",
         "There&rsquo;s no defensible Go / No-Go signal &mdash; just opinions in a meeting room."),
        ("03", "#34d399", "&#x1F30A;", "The Performance Gap",
         "Trust is earned through consistent, measurable performance in a live environment.",
         "Not through a curated set of successful examples shown in a demo."),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>',
                 sub_blocks=[("Why it hurts", punch)],
                 icon=icon)
        for n, col, icon, name, desc, punch in cards
    )
    return f"""<section data-title="Why Vibe Checks Fail">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>Why &ldquo;vibe checks&rdquo; fail in production</h2>
    <div class="subtitle">A successful demo is not a quality bar. Three reasons evals are non-negotiable.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards_html}
    </div>
  </div>
</section>
"""


def accuracy_trap() -> str:
    """Source slide 7 - The 95% Accuracy Trap.

    Two-card comparison using M5 header-band card pattern. No "VS" badge
    in the middle — M5 keeps comparisons clean with the colour contrast
    alone (cf. m5_v2.evolution_of_value()).
    """
    lab_body = """<p style="font-size:13px; color:#cdd5e3; margin:0 0 8px; line-height:1.6;">
      Standard benchmarks are excellent for static datasets in controlled environments &mdash; but blind to the nuanced failures in user experience and trust.
    </p>"""
    eval_body = """<p style="font-size:13px; color:#cdd5e3; margin:0 0 8px; line-height:1.6;">
      Evals look beyond lab scores to measure the specific friction &mdash; latency, bias, inconsistency &mdash; that leads to product failure and loss of trust.
    </p>"""
    cards_html = (
        _m5_card("01", "#3b82f6", "Accuracy &middot; Precision &middot; Recall &middot; F1",
                 body_html=lab_body,
                 sub_blocks=[("Maths example",
                              "<strong style=\"color:#fff;\">1,000 calls/day &times; 5% wrong = 50 wrong outputs/day.</strong> Some silent. One high-stakes wrong outweighs the other 950.")],
                 icon="&#x1F9EA;")
        + _m5_card("02", "#34d399", "User experience &middot; Trust &middot; Safety",
                   body_html=eval_body,
                   sub_blocks=[("Product example",
                                "A &ldquo;95% accurate&rdquo; medical bot still fails if the 5% includes a wrong dosage recommendation.")],
                   icon="&#x1F4DD;")
    )
    return f"""<section data-title="The 95% Accuracy Trap">
  <div class="inner">
    <div class="demo-tag tag-framework">Mental model</div>
    <div style="font-family:'Poppins',sans-serif; font-size:10.5px; color:#fbbf24; font-weight:900; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:6px;">The gap between lab and reality</div>
    <h2>The 95% accuracy trap</h2>
    <div class="subtitle">Lab metrics measure the model. Evals measure the product.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; max-width:1080px; margin:22px auto 0;">
      {cards_html}
    </div>
    {_m5_callout('<strong style="color:#fff;">PM rule:</strong> never quote model accuracy without quoting the eval bar next to it. &ldquo;95% accurate at extracting risks&rdquo; means nothing without the failure taxonomy of the missing 5%.')}
  </div>
</section>
"""



# ---------------------------------------------------------------------------
# Section 02 - Measuring AI-Powered Product Outputs
# ---------------------------------------------------------------------------

def eval_stack_visual() -> str:
    """Source slide 9 - The AI Eval Stack.

    Three-layer pyramid (Automated/Component, Human/System, User Feedback/Online).
    SVG on the left, M5-style annotation column on the right (mirrors
    m5_v2.react_pattern Mechanism / Value / Cost rhythm).
    """
    annotations = (
        _m5_annotation("#79c0ff", "03 &middot; Online evals",
                       "<strong style=\"color:#fff;\">User feedback.</strong> The final reality check &mdash; regeneration rates, task completion, thumbs &mdash; confirms the product is delivering value.")
        + _m5_annotation("#fbbf24", "02 &middot; System-level evals",
                         "<strong style=\"color:#fff;\">Human evals.</strong> Where experts use structured rubrics to judge nuance, tone, and helpfulness &mdash; and provide the calibration the rest of the system depends on.")
        + _m5_annotation("#34d399", "01 &middot; Component-level evals",
                         "<strong style=\"color:#fff;\">Automated assessment.</strong> Machine-detectable tests that filter obvious failures, check formatting, and measure speed and accuracy at scale.")
    )
    return f"""<section data-title="The AI Eval Stack">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>The AI Eval Stack</h2>
    <div class="subtitle">Three layers. Always all three. They answer different questions.</div>

    <div style="max-width:1080px; margin:18px auto 0;">
      <div style="display:grid; grid-template-columns:1.1fr 1fr; gap:18px; align-items:stretch;">

        <!-- Pyramid SVG -->
        <div style="background:rgba(7,22,44,0.55); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:14px;">
          <svg viewBox="0 0 460 360" preserveAspectRatio="xMidYMid meet" style="width:100%; height:auto; display:block;">
            <defs>
              <linearGradient id="evalUF" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(96,165,250,0.30)"/><stop offset="100%" stop-color="rgba(96,165,250,0.10)"/></linearGradient>
              <linearGradient id="evalHE" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(251,191,36,0.30)"/><stop offset="100%" stop-color="rgba(251,191,36,0.10)"/></linearGradient>
              <linearGradient id="evalAU" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(52,211,153,0.30)"/><stop offset="100%" stop-color="rgba(52,211,153,0.10)"/></linearGradient>
            </defs>

            <!-- Layer 1 (top): User Feedback -->
            <polygon points="180,20 280,20 320,90 140,90" fill="url(#evalUF)" stroke="#79c0ff" stroke-width="1.6"/>
            <text x="230" y="46" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="13" font-weight="900">USER FEEDBACK</text>
            <text x="230" y="62" text-anchor="middle" fill="#79c0ff" font-family="Poppins,sans-serif" font-size="9" font-weight="800" letter-spacing="2.2">ONLINE EVALS</text>
            <text x="230" y="78" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="10">What do users do?</text>

            <!-- Layer 2 (middle): Human Evals -->
            <polygon points="140,98 320,98 365,190 95,190" fill="url(#evalHE)" stroke="#fbbf24" stroke-width="1.6"/>
            <text x="230" y="128" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="13" font-weight="900">HUMAN EVALUATION</text>
            <text x="230" y="144" text-anchor="middle" fill="#fbbf24" font-family="Poppins,sans-serif" font-size="9" font-weight="800" letter-spacing="2.2">SYSTEM-LEVEL EVALS</text>
            <text x="230" y="162" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="10">What do graders think?</text>
            <text x="230" y="180" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="10">Calibrated rubric scores</text>

            <!-- Layer 3 (base): Automated Assessment -->
            <polygon points="95,198 365,198 420,330 40,330" fill="url(#evalAU)" stroke="#34d399" stroke-width="1.6"/>
            <text x="230" y="232" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="13" font-weight="900">AUTOMATED ASSESSMENT</text>
            <text x="230" y="248" text-anchor="middle" fill="#34d399" font-family="Poppins,sans-serif" font-size="9" font-weight="800" letter-spacing="2.2">COMPONENT-LEVEL EVALS</text>
            <text x="230" y="270" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="10">Did this change regress anything?</text>
            <text x="230" y="288" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="10">LLM-as-judge &middot; format checks</text>
            <text x="230" y="306" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="10">Speed &amp; accuracy at scale</text>

            <!-- Volume / fidelity axes -->
            <text x="430" y="34" text-anchor="end" fill="#8899bb" font-family="Poppins,sans-serif" font-size="8" font-weight="800" letter-spacing="1.5">HIGHEST</text>
            <text x="430" y="46" text-anchor="end" fill="#8899bb" font-family="Poppins,sans-serif" font-size="8" letter-spacing="1.5">VOLUME</text>
            <text x="430" y="312" text-anchor="end" fill="#8899bb" font-family="Poppins,sans-serif" font-size="8" font-weight="800" letter-spacing="1.5">HIGHEST</text>
            <text x="430" y="324" text-anchor="end" fill="#8899bb" font-family="Poppins,sans-serif" font-size="8" letter-spacing="1.5">FIDELITY</text>
            <line x1="430" y1="60" x2="430" y2="290" stroke="#8899bb" stroke-width="0.8" stroke-dasharray="3,3" opacity="0.5"/>
            <polygon points="427,290 433,290 430,298" fill="#8899bb" opacity="0.5"/>
          </svg>
        </div>

        <!-- Layer annotations (M5 react_pattern side-callout pattern) -->
        <div style="display:flex; flex-direction:column; gap:10px;">
          {annotations}
        </div>

      </div>
    </div>

    {_m5_callout('<strong style="color:#fff;">PM oversight:</strong> a multi-layered evaluation plan balances speed, cost, and depth of insight. Skip a layer and you skip a class of failure.')}
  </div>
</section>
"""



def rubric_phases() -> str:
    """Source slide 10 - How to Build a Human Eval Rubric.

    5 numbered steps in M5 header-band card pattern, with a Phase tag
    in the sub-block (Create / Calibrate / Monitor). This keeps the
    phase information from the source slide without forcing an awkward
    3-cluster grid.
    """
    steps = [
        ("01", "#3b82f6", "Value Proposition",
         "Define the core user needs and product promises your AI must fulfil.",
         "Phase 1 &middot; Create assessment"),
        ("02", "#3b82f6", "Evaluation Criteria",
         "Define the specific dimensions &mdash; factuality, tone, logic &mdash; that measure those promises.",
         "Phase 1 &middot; Create assessment"),
        ("03", "#3b82f6", "Scalable Questions",
         "Use binary yes/no or 1&ndash;5 scale questions to turn qualitative &ldquo;vibes&rdquo; into quantitative data.",
         "Phase 1 &middot; Create assessment"),
        ("04", "#fbbf24", "Calibrate Reviewers",
         "Create prototypical assessments so all reviewers are trained on the same expectations.",
         "Phase 2 &middot; Calibrate"),
        ("05", "#34d399", "Continually Validate",
         "Have reviewers justify their ratings to identify edge cases and rubric drift.",
         "Phase 3 &middot; Monitor"),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>',
                 sub_blocks=[("Phase", phase)])
        for n, col, name, desc, phase in steps
    )
    return f"""<section data-title="How to Build a Human Eval Rubric">
  <div class="inner">
    <div class="demo-tag tag-framework">Step-by-step</div>
    <h2>How to build a human eval rubric</h2>
    <div class="subtitle">Convert subjective human judgement into an objective system-level signal.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr 1fr; gap:10px; max-width:1100px; margin:22px auto 0;">
      {cards_html}
    </div>
    {_m5_callout('<strong style="color:#fff;">&#x270D;&#xFE0F; Build your own:</strong> the M6 &mdash; Human Evaluation Rubric tool walks you through all five steps and exports the result to <code>06-evals/human-rubric.md</code>.')}
  </div>
</section>
"""


def google_assistant_example() -> str:
    """Source slide 11 - Real-World Example: Human Evaluation at Google Assistant.

    6 cards (Context · Goal · Method · Training · Assessment · Outcome)
    in M5 header-band card pattern. Colour grouping signals the phase
    (define / build / observe).
    """
    items = [
        ("01", "#3b82f6", "Context",
         "Google was building a human-in-the-loop personal assistant product that combined humans and AI to fulfil complex user tasks."),
        ("02", "#3b82f6", "Goal",
         "They needed to assess task-fulfilment quality &mdash; quantify how the product delivered real-world value."),
        ("03", "#fbbf24", "Method",
         "The rubric consisted of 26 questions and included simple technical criteria, specific desired outcomes, and subjective human evaluations."),
        ("04", "#fbbf24", "Training",
         "The rubric was calibrated across Product, UX, and UXR &mdash; then used to train a dedicated team of manual reviewers."),
        ("05", "#34d399", "Assessment",
         "After each conversation, the transcript was sent to a reviewer to evaluate the system&rsquo;s end-to-end performance."),
        ("06", "#34d399", "Outcome",
         "The data identified specific failure modes, allowing the team to eliminate launch blockers and improve the experience."),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>')
        for n, col, name, desc in items
    )
    return f"""<section data-title="Real-World Example">
  <div class="inner">
    <div class="demo-tag tag-realworld">Real-world example</div>
    <h2>Human evaluation at Google Assistant</h2>
    <div class="subtitle">A concrete reference implementation of the AI Eval Stack&rsquo;s human-eval layer.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1080px; margin:22px auto 0;">
      {cards_html}
    </div>
    {_m5_callout('<strong style="color:#fff;">PM lift-out:</strong> they ran human evals on every conversation &mdash; not a sample. For your scale, sample with stratification (high / mid / low confidence).')}
  </div>
</section>
"""


def pm_role_evals() -> str:
    """Source slide 12 - The PM's Role in Evaluations.

    3 M5 header-band cards with the ownership line in the sub-block.
    """
    cards = [
        ("01", "#3b82f6", "&#x1F4CB;", "Drafting the Definition of Quality",
         "Your primary deliverable isn&rsquo;t a feature spec &mdash; it&rsquo;s a rubric defining exactly what a &ldquo;perfect&rdquo; response looks like for your specific user.",
         "You own the gold standard"),
        ("02", "#fbbf24", "&#x1F6A6;", "Setting the Pass Thresholds",
         "You work with engineering to determine which failure modes are minor annoyances and which are launch blockers that stop a release.",
         "You decide the acceptability gap"),
        ("03", "#34d399", "&#x2696;&#xFE0F;", "Auditing the Automated Judges",
         "You periodically audit the automated and &ldquo;LLM-as-a-judge&rdquo; layers to ensure the machine&rsquo;s version of quality hasn&rsquo;t drifted away from human reality.",
         "You provide the ground truth"),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.6;">{desc}</p>',
                 sub_blocks=[("PM ownership", own)],
                 icon=icon)
        for n, col, icon, name, desc, own in cards
    )
    return f"""<section data-title="The PM's Role in Evaluations">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>The PM&rsquo;s role in evaluations</h2>
    <div class="subtitle">PMs own the bar. Engineering runs the harness. QA can&rsquo;t.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards_html}
    </div>
  </div>
</section>
"""



# ---------------------------------------------------------------------------
# Source slide 13 - Lab body (originally Group Breakout, now Solo)
# ---------------------------------------------------------------------------

JUNO_EVAL_STACK_LAB_BODY = """<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; max-width:1040px; margin:0 auto;">

  <div style="background:rgba(96,165,250,0.05); border:1px solid rgba(96,165,250,0.30); border-radius:12px; padding:14px 18px; text-align:left;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">Setup</div>
    <p style="font-size:12.5px; color:#cdd5e3; margin:0 0 8px; line-height:1.55;">
      Open the <strong style="color:#fff;">M6 &mdash; Eval Stack Designer</strong> tool. Treat Juno as the whole product you&rsquo;ve built across M1&ndash;M5. Pre-loaded with a Juno P0 Triage starter you can adapt.
    </p>
  </div>

  <div style="background:rgba(251,191,36,0.05); border:1px solid rgba(251,191,36,0.30); border-radius:12px; padding:14px 18px; text-align:left;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#fbbf24; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">Output</div>
    <p style="font-size:12.5px; color:#cdd5e3; margin:0 0 8px; line-height:1.55;">
      &rarr; <code style="color:#fbbf24;">06-evals/eval-stack.md</code> &mdash; three layers, each with signals, cadence, pass bar, and owner.
    </p>
  </div>

  <div style="grid-column:span 2; background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:14px 18px;">
    <ol style="text-align:left; max-width:920px; margin:0; padding-left:20px; font-size:12.5px; color:#cdd5e3; line-height:1.7;">
      <li><strong style="color:#fff;">Start with User Feedback (online).</strong> Define <em>two</em> mechanisms &mdash; one active (e.g. thumbs / regenerate / suppress) and one passive (e.g. abandon rate, time-on-result).</li>
      <li><strong style="color:#fff;">Move to Human Evaluation (system-level).</strong> Spec 3 rubric questions a Senior PM would use to grade Juno&rsquo;s output. Anchors per scale point are non-negotiable.</li>
      <li><strong style="color:#fff;">Finish with Automated Assessment (component-level).</strong> Identify <em>one</em> binary metric to automate via a script or LLM-as-a-judge &mdash; e.g. format check, citation check, refusal trigger.</li>
      <li>Add cadence + numeric pass bar + named owner for each layer.</li>
      <li>Copy as markdown &rarr; commit to <code style="color:#34d399;">06-evals/eval-stack.md</code>. Add the link to your final deliverables README.</li>
    </ol>
  </div>

</div>"""


# ---------------------------------------------------------------------------
# Section 03 - AI Levers for Output Optimization
# ---------------------------------------------------------------------------

def operationalize_risks() -> str:
    """Source slide 15 - Operationalizing and Measuring AI Risks.

    Four M5 header-band cards (Blocked Request Rate, Hallucination Rate,
    Human Override Rate, Model Drift & Latency). Measurement formula +
    example in the sub-blocks (mirrors M5 control_panel pattern).
    """
    cards = [
        ("01", "#3b82f6", "&#x1F6AB;", "Blocked Request Rate",
         "The frequency at which automated safety filters trigger to stop a response.",
         "Total Denied Prompts / Total User Inputs",
         "Finding that 15% of finance queries are being blocked, indicating your guardrails are too sensitive and hurting the UX."),
        ("02", "#fbbf24", "&#x1F4CA;", "Hallucination Rate",
         "The percentage of responses containing factually incorrect or ungrounded claims.",
         "Total Hallucinations / Total Responses",
         "Monitoring if a medical bot&rsquo;s error rate rises above 1% triggers an immediate rollback to a previous version."),
        ("03", "#34d399", "&#x270D;&#xFE0F;", "Human Override Rate",
         "The rate at which a human-in-the-loop must correct the AI before the user sees the output.",
         "Total Human Edits / Total AI Outputs",
         "A customer-service tool where experts rewrite 40% of AI drafts signals the model isn&rsquo;t saving time yet."),
        ("04", "#bcb1ff", "&#x1F4C9;", "Model Drift &amp; Latency",
         "The monitoring of performance degradation and response speed over time.",
         "Change in Accuracy + P99 Latency",
         "Identifying that a model has become 10% less accurate or 5s slower after a vendor updated the underlying LLM."),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>',
                 sub_blocks=[
                     ("Measurement", f'<code style="font-family:\'IBM Plex Mono\',monospace; color:#fff; font-size:11px;">{metric}</code>'),
                     ("Example", example),
                 ],
                 icon=icon)
        for n, col, icon, name, desc, metric, example in cards
    )
    return f"""<section data-title="Operationalizing AI Risks">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>Operationalising and measuring AI risks</h2>
    <div class="subtitle">Use these performance signals as your dashboard to monitor live AI product quality and safety.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; max-width:1120px; margin:22px auto 0;">
      {cards_html}
    </div>
  </div>
</section>
"""


def governance_framework() -> str:
    """Source slide 16 - Strategic Logic / The Governance Framework.

    Four M5 header-band cards with example sub-block.
    """
    items = [
        ("01", "#3b82f6", "Hard vs. Soft Gates",
         "Determine which failures must <em>automatically</em> block a release versus those that only require a manual PM sign-off.",
         "A safety failure triggers an automatic block; high latency only requires a PM justification to release."),
        ("02", "#fbbf24", "Zero-Tolerance Metrics",
         "For hard gates, establish the specific numerical thresholds that trigger an immediate production block.",
         "0% PII leakage to ensure the system never reveals sensitive data like employee salaries."),
        ("03", "#34d399", "Grounding for Trust",
         "Define specific output requirements that provide users with evidence of the AI&rsquo;s reasoning.",
         "The model must provide direct citations or links to the HR policy it used to answer the question."),
        ("04", "#bcb1ff", "Build a Failure Taxonomy",
         "Categorise potential AI failures into a clear document to align technical and business stakeholders on risk priority.",
         "A severity vs. frequency map prioritises fixing hallucinations in vacation policies over minor &ldquo;off-brand&rdquo; tone issues."),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>',
                 sub_blocks=[("Example", example)])
        for n, col, name, desc, example in items
    )
    return f"""<section data-title="The Governance Framework">
  <div class="inner">
    <div class="demo-tag tag-framework">Strategic logic</div>
    <h2>The governance framework</h2>
    <div class="subtitle">Four governance strategies that turn evals into production guardrails.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards_html}
    </div>
    {_m5_callout('Dive deeper into each governance strategy in Product School&rsquo;s <em>AI Evals Certification</em>.')}
  </div>
</section>
"""


def three_levers() -> str:
    """Source slide 17 - Three Levers to Optimize AI Product Performance.

    Three M5 header-band cards. Tag (Behavior&Logic / Intelligence&Cost /
    Knowledge&Accuracy) lives in the first sub-block; example in the
    second. Mirrors M5 evolution_of_value (two-row sub-blocks).
    """
    cols = [
        ("01", "#3b82f6", "&#x270D;&#xFE0F;", "The Prompt", "Behavior &amp; Logic",
         "Adjust the instructions or formatting to influence the AI&rsquo;s output.",
         "Few-shot, chain-of-thought prompting, or adding delimiters to structure your data."),
        ("02", "#fbbf24", "&#x1F916;", "The Model", "Intelligence &amp; Cost",
         "Swap models or versions to find the best balance of quality, speed, and price.",
         "Comparing Gemini Pro vs. Flash for different task types or adjusting hyperparameters."),
        ("03", "#34d399", "&#x1F4DA;", "The Data", "Knowledge &amp; Accuracy",
         "Refine the information the AI accesses to ensure relevant and accurate responses.",
         "Cleaning the RAG dataset, adding more diverse data points, or fine-tuning the model."),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.6;">{desc}</p>',
                 sub_blocks=[
                     ("Trade-off axis", tag),
                     ("Try", example),
                 ],
                 icon=icon)
        for n, col, icon, name, tag, desc, example in cols
    )
    return f"""<section data-title="Three Levers">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>Three levers to optimise AI product performance</h2>
    <div class="subtitle">When evaluations signal a quality gap, these are the three levers you pull.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards_html}
    </div>
    {_m5_callout('<strong style="color:#fff;">PM rule of thumb:</strong> try Prompt &rarr; Model &rarr; Data. Architecture last. Most teams reach for architecture first &mdash; it&rsquo;s the slowest and most expensive lever.')}
  </div>
</section>
"""


def pm_execution_plan() -> str:
    """Source slide 18 - The PM Execution Plan.

    Four M5 header-band cards with key-decision sub-block. Matches M5
    awspec_blueprint rhythm (4 cards in a row with a uniform secondary
    block).
    """
    items = [
        ("01", "#3b82f6", "Build Your Eval Plan",
         "Define exactly what to measure, how often to test, and assign a clear quality owner for the final score.",
         "Speed vs. Certainty"),
        ("02", "#fbbf24", "Set Your Gatekeepers",
         "Compare systematic results against your gold standard. Reject any launch based on a &ldquo;good demo&rdquo; if the data fails the bar.",
         "Brand Protection vs. Hype"),
        ("03", "#34d399", "Add Production Guardrails",
         "Determine when the system must block a response, degrade to a safe script, or escalate to a human reviewer.",
         "Safety vs. Utility"),
        ("04", "#bcb1ff", "Evolve Your Roadmap",
         "Use performance gaps to decide whether to pivot your strategy or update your roadmap with new goals.",
         "Feature vs. Data"),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>',
                 sub_blocks=[("Key decision", f'<strong style="color:#fff;">{decision}</strong>')])
        for n, col, name, desc, decision in items
    )
    return f"""<section data-title="The PM Execution Plan">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>The PM execution plan</h2>
    <div class="subtitle">Four steps that turn evals into a production decision &mdash; with the trade-off named on each one.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; max-width:1100px; margin:22px auto 0;">
      {cards_html}
    </div>
  </div>
</section>
"""



# ---------------------------------------------------------------------------
# Source slide 19 - Lab body (originally Group Breakout, now Solo)
# ---------------------------------------------------------------------------

JUNO_FINAL_DELIVERABLES_LAB_BODY = """<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; max-width:1040px; margin:0 auto;">

  <div style="background:rgba(96,165,250,0.05); border:1px solid rgba(96,165,250,0.30); border-radius:12px; padding:14px 18px; text-align:left;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">Setup</div>
    <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">
      Open the <strong style="color:#fff;">Final Project Deliverables Builder</strong>. The tool aggregates your six modules into one shareable README + executive page.
    </p>
  </div>

  <div style="background:rgba(251,191,36,0.05); border:1px solid rgba(251,191,36,0.30); border-radius:12px; padding:14px 18px; text-align:left;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#fbbf24; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">Output</div>
    <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">
      &rarr; <code style="color:#fbbf24;">README.md</code> at the root of your <code>juno-pm</code> fork. The repo URL is your LMS submission.
    </p>
  </div>

  <div style="grid-column:span 2; background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:14px 18px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#bcb1ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px;">Source-slide checklist (slides 5&ndash;11 of the original deliverables deck)</div>
    <ol style="text-align:left; max-width:920px; margin:0; padding-left:20px; font-size:12px; color:#cdd5e3; line-height:1.7;">
      <li><strong style="color:#fff;">Final System Message</strong> &mdash; from M1, including few-shot examples.</li>
      <li><strong style="color:#fff;">AI Strategy One-Pager</strong> &mdash; high-level overview + shareable link to the full artifact.</li>
      <li><strong style="color:#fff;">RAG Architecture &amp; Data Strategy</strong> &mdash; how Juno is grounded in RocketShip data.</li>
      <li><strong style="color:#fff;">Juno UX Design</strong> &mdash; 1&ndash;2 high-fidelity screenshots of the Lovable interface.</li>
      <li><strong style="color:#fff;">Agentic Workflow (AWSpec)</strong> &mdash; high-level overview + shareable link to the full artifact.</li>
      <li><strong style="color:#fff;">Eval Stack Plan</strong> &mdash; human rubric questions + the automated hard-gate threshold.</li>
      <li><strong style="color:#fff;">Build Insights</strong> &mdash; biggest strategic friction points and your &ldquo;aha&rdquo; moments.</li>
    </ol>
    <p style="font-size:11.5px; color:#bcb1ff; margin:10px 0 0; line-height:1.55;">
      <strong style="color:#fff;">Solo course adaptation:</strong> there&rsquo;s no shared deck and no group-vs-individual copy split &mdash; the README of your fork is the deliverable. The optional 3-min Loom is encouraged but not required for certification.
    </p>
  </div>

</div>"""


# ---------------------------------------------------------------------------
# Source slide 20 - Learner Journey (course recap)
# ---------------------------------------------------------------------------

def learner_journey() -> str:
    """6-module recap with mindset shift + win per module.

    Source slide 20. Reads top-to-bottom in chronological order: M1 -> M6.
    """
    rows = [
        ("01", "#3b82f6", "Drive AI-First Execution with Prompting",
         "<strong style=\"color:#fff;\">The mindset shift:</strong> moving from deterministic rules to governing probabilistic systems.",
         "<strong style=\"color:#fff;\">The win:</strong> mastering prompt anatomy to move beyond basic chat and establish reliable, system-level logic for AI-native features."),
        ("02", "#3b82f6", "Validate AI Opportunities and Technical Feasibility",
         "<strong style=\"color:#fff;\">The strategic lens:</strong> shifting from shiny distractions to boring killer features that prioritise business scale.",
         "<strong style=\"color:#fff;\">The win:</strong> writing the AI strategy one-pager to bridge technical feasibility and business impact &mdash; forcing a rigorous defence of every bet."),
        ("03", "#fbbf24", "Improve AI Product Requirements with RAG Architecture",
         "<strong style=\"color:#fff;\">The context shift:</strong> moving from stateless prompts to context-aware systems that ground AI outputs in verifiable data.",
         "<strong style=\"color:#fff;\">The win:</strong> defining an AI PRD to specify needs and own technical trade-offs through precise retrieval requirements."),
        ("04", "#fbbf24", "Design AI-Native User Experiences",
         "<strong style=\"color:#fff;\">The interface evolution:</strong> moving from static menus to invisible UIs that proactively surface tools based on needs.",
         "<strong style=\"color:#fff;\">The win:</strong> architecting the AI iceberg flow &mdash; mapping hidden logic and system triggers to build magical experiences that maintain trust through transparency."),
        ("05", "#34d399", "Deploy Agentic Systems and Workflows",
         "<strong style=\"color:#fff;\">The autonomy dial:</strong> moving from reactive to autonomous systems that interpret intent, make decisions, and execute multi-step tasks.",
         "<strong style=\"color:#fff;\">The win:</strong> developing the AWSpec to scale product judgement with reasoning patterns for resilient, goal-driven systems."),
        ("06", "#bcb1ff", "Measure AI Quality with Evals and Guardrails",
         "<strong style=\"color:#fff;\">The validation shift:</strong> replacing subjective vibe checks with systematic evaluation for reliability at scale.",
         "<strong style=\"color:#fff;\">The win:</strong> engineering a multi-layered eval stack to establish hard-gate thresholds that protect and maintain trust in a live environment."),
    ]
    rows_html = "".join(
        f"""<div style="display:grid; grid-template-columns:auto 1fr 2fr 2fr; gap:14px; align-items:center; padding:11px 14px; background:rgba(255,255,255,0.025); border:1px solid {col}30; border-left:3px solid {col}; border-radius:10px;">
  <div style="font-family:'Poppins',sans-serif; font-size:24px; font-weight:900; color:{col}; line-height:1; padding-right:6px;">{n}</div>
  <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:700; color:#fff; line-height:1.3;">{title}</div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{shift}</p>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{win}</p>
</div>"""
        for n, col, title, shift, win in rows
    )
    return f"""<section data-title="Learner Journey">
  <div class="inner">
    <div class="demo-tag tag-debrief">Course recap</div>
    <h2>Your learner journey</h2>
    <div class="subtitle">Six mindset shifts. Six wins. One coherent body of work in your fork.</div>
    <div style="display:flex; flex-direction:column; gap:8px; max-width:1080px; margin:18px auto 0;">
      {rows_html}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Source slide 23 - Final Project Showcase title (adapted for solo course)
# ---------------------------------------------------------------------------

def final_showcase_title() -> str:
    return """<section class="centered" data-title="Final Project Showcase">
  <div class="inner">
    <div class="demo-tag tag-debrief">Final project</div>
    <h2 style="font-size:46px; margin-top:8px;">Final Project Showcase</h2>
    <p style="font-family:'Poppins',sans-serif; font-size:24px; font-weight:800; color:#fbbf24; margin-top:14px;">Demo Your Juno Copilot</p>
    <p style="font-size:14px; color:#cdd5e3; max-width:720px; margin:18px auto 0; line-height:1.65;">
      Solo course adaptation: instead of a group demo, you ship the repo. Your <code>juno-pm</code> fork &mdash; with its README polished &mdash; <em>is</em> the demo.
    </p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Source slide 24 - LMS submission reminder
# ---------------------------------------------------------------------------

def lms_reminder() -> str:
    return """<section data-title="Important Reminder">
  <div class="inner">
    <div class="demo-tag tag-recall">Important reminder</div>
    <h2>Submit to qualify for certification</h2>
    <div class="subtitle">Upload your own copy of the final project deliverables in the LMS within 7 days of course completion.</div>

    <div style="max-width:880px; margin:24px auto 0; background:rgba(7,22,44,0.55); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:24px 28px;">
      <div style="display:grid; grid-template-columns:auto 1fr; gap:18px; align-items:center;">
        <div style="font-size:48px;">&#x1F680;</div>
        <div style="text-align:left;">
          <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#fbbf24; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:4px;">What to submit</div>
          <p style="font-family:'Poppins',sans-serif; font-size:16px; font-weight:700; color:#fff; margin:0 0 8px; line-height:1.4;">
            The URL of your finalised <code style="color:#34d399;">juno-pm</code> fork (with the polished README) &mdash; pasted into the LMS upload field.
          </p>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">
            No deck. No video required. Just a repo URL that a stranger could open and &ldquo;get&rdquo; what you built.
          </p>
        </div>
      </div>
    </div>

    <p style="font-size:12px; color:#bcb1ff; max-width:880px; margin:18px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">Window:</strong> 7 days post-course. Late submissions don&rsquo;t qualify for certification &mdash; the artifacts in your fork are still yours forever.
    </p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Source slide 25 - Presentation Kick-Off (adapted for solo course)
# ---------------------------------------------------------------------------

def presentation_kickoff() -> str:
    """Three paths for the solo showcase. M5 header-band card pattern with
    'Best when' as the sub-block."""
    paths = [
        ("01", "#3b82f6", "&#x1F39D;&#xFE0F;", "Volunteer to demo live",
         "Cohorts have ~10-min demo slots. First-come, first-served via Slack. Get live, actionable feedback from peers and the instructor.",
         "Path A &middot; live cohort &mdash; you want real-time sharpening."),
        ("02", "#fbbf24", "&#x1F4F9;", "Record a 3-min Loom",
         "Walk through your repo &mdash; bet, system prompt, user flow, AWSpec, eval stack. Post in <code>#ai-pm-cohort</code>; instructor responds in-thread within ~5 days.",
         "Path B &middot; async &mdash; you want feedback you can replay."),
        ("03", "#34d399", "&#x1F4DD;", "Just submit the URL",
         "The README is enough. If a stranger can read it and understand Juno&rsquo;s bet, the bar, and the trade-offs &mdash; you&rsquo;ve passed.",
         "Path C &middot; minimum &mdash; the README is the certificate."),
    ]
    cards_html = "".join(
        _m5_card(n, col, name,
                 body_html=f'<p style="font-size:12px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>',
                 sub_blocks=[("Best when", when)],
                 icon=icon)
        for n, col, icon, name, desc, when in paths
    )
    return f"""<section data-title="Your Time to Shine">
  <div class="inner">
    <div class="demo-tag tag-debrief">Your time to shine</div>
    <h2>Present, record, or just submit &mdash; your call</h2>
    <div class="subtitle">Three paths, all valid for certification. Pick the one that fits your learning style.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards_html}
    </div>
    {_m5_callout('<strong style="color:#fff;">Important:</strong> you have 7 days after course completion to submit. The repo URL is the certificate.')}
  </div>
</section>
"""



# ---------------------------------------------------------------------------
# Source slide 27 - Resources & Templates
# ---------------------------------------------------------------------------

def m6_resources_templates() -> str:
    eval_url = "../Modules/M6 - Eval Stack Designer.html"
    rubric_url = "../Modules/M6 - Human Evaluation Rubric.html"
    final_url = "../Modules/Final Project Deliverables Builder.html"
    cards = [
        ("&#x270D;&#xFE0F; In-Class Lab Tool", "Plan Juno&rsquo;s Eval Stack",
         "M6 &mdash; Eval Stack Designer",
         "Three-layer eval planner. User feedback &middot; Human eval &middot; Automated. Live SVG stack + JSON / markdown export to <code style=\"font-size:0.9em; color:#3b82f6;\">06-evals/eval-stack.md</code>.",
         eval_url, "#3b82f6"),
        ("&#x1F4DD; Companion Tool", "Build Juno&rsquo;s Human Eval Rubric",
         "M6 &mdash; Human Evaluation Rubric",
         "Dimensions, anchors per scale point, sampling cadence, and disagreement protocol. Exports to <code style=\"font-size:0.9em; color:#fbbf24;\">06-evals/human-rubric.md</code>.",
         rubric_url, "#fbbf24"),
        ("&#x1F680; Final Lab Tool", "Finalise the Project Deliverables",
         "Final Project Deliverables Builder",
         "Aggregates M1&ndash;M6 artefacts into one polished <code style=\"font-size:0.9em; color:#34d399;\">README.md</code> + Build Insights reflection.",
         final_url, "#34d399"),
        ("&#x1F4DA; Project Repo Template", "Use the <code style=\"font-size:0.9em; color:#bcb1ff;\">juno-pm</code> template",
         "ai-product-management-template",
         "One-click create your project fork (if you haven&rsquo;t already).",
         TEMPLATE_USE_URL, "#bcb1ff"),
    ]
    cards_html = "".join(
        f'<a href="{url}" target="_blank" style="text-decoration:none;">'
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:12px; padding:14px 16px; text-align:left; height:100%; display:flex; flex-direction:column;">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:9.5px; color:{col}; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:5px;">{tag}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:14px; font-weight:800; color:#fff; margin-bottom:4px; line-height:1.3;">{title}</div>'
        f'<p style="font-size:11.5px; color:#cdd5e3; margin:0 0 8px; line-height:1.5;">{desc}</p>'
        f'<div style="margin-top:auto; padding-top:6px; border-top:1px dashed {col}40; font-family:\'IBM Plex Mono\',monospace; font-size:10.5px; color:{col};">&rarr; {sub}</div>'
        f'</div></a>'
        for tag, title, sub, desc, url, col in cards
    )
    return f"""<section data-title="Resources &amp; Templates">
  <div class="inner">
    <div class="demo-tag tag-debrief">Resources &amp; templates</div>
    <h2>Resources &amp; templates</h2>
    <div class="subtitle">All M6 tools live in <code>/Modules/</code>. Deliverables commit to <code>06-evals/</code> &mdash; final README at the repo root.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; max-width:1040px; margin:22px auto 0;">
      {cards_html}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build_module_6():
    """Build (instructor_sections, share_sections) for Module 6."""
    sections_inst, sections_share = [], []
    add = _add_builder(sections_inst, sections_share)

    # Source slide 1 - Hero
    add(hero(
        title_lead="Measure AI Quality with",
        title_accent="Evals and Guardrails",
        subtitle="Module 6 &middot; AI Product Management Certification",
        waypoints=[
            ("Production-Grade Evaluation Requirements", "Why vibe checks fail. The 95% accuracy trap."),
            ("Measuring AI-Powered Product Outputs", "The AI Eval Stack &middot; human rubric &middot; PM&rsquo;s role."),
            ("AI Levers for Output Optimization", "Risks &middot; governance &middot; three levers &middot; PM execution plan."),
        ],
        out_line="You finish Module 6 with the final deliverables: <code>06-evals/eval-stack.md</code>, <code>06-evals/human-rubric.md</code>, and the polished <code>README.md</code> of your <code>juno-pm</code> fork.",
        module_n=6,
    ))

    # Source slide 2 - Class Expectations
    add(class_expectations(),
        note="Source slide 2. Set ground rules: cameras-on for live cohort sessions, async etiquette for solo learners. Solo course &mdash; all interactions go through #ai-pm-cohort.")

    # Source slide 3 - Syllabus
    add(syllabus_visual_m6(),
        note="Source slide 3. AI Product Management Syllabus, M6 highlighted (the final module).")

    # Source slide 4 - Agenda
    add(agenda_6(),
        note="Source slide 4. Four sections + the final showcase. Two solo labs anchor the day.")

    # ----- Section 01 -----
    add(section_divider("01", "Production-Grade Evaluation Requirements"),
        note="Section 1 &mdash; from vibe checks to systematic measurement.")

    add(vibe_checks_fail(),
        note="Source slide 6. Three reasons vibe checks fail: Invisible Failures, Subjectivity Trap, Performance Gap.")

    add(accuracy_trap(),
        note="Source slide 7. The 95% Accuracy Trap. Lab metrics measure the model; evals measure the product. Use the math example to sell the point.")

    # ----- Section 02 -----
    add(section_divider("02", "Measuring AI-Powered Product Outputs"),
        note="Section 2 &mdash; the AI Eval Stack and the PM&rsquo;s role in defining quality.")

    add(eval_stack_visual(),
        note="Source slide 9. The three-layer AI Eval Stack pyramid. PMs oversee a multi-layered plan that balances speed, cost, and depth of insight.")

    add(rubric_phases(),
        note="Source slide 10. Five steps grouped into three phases (Create / Calibrate / Monitor). The rubric must convert subjective judgement into an objective signal.")

    add(google_assistant_example(),
        note="Source slide 11. Real-world example: Google Assistant 26-question rubric. PM lift-out: stratified sampling beats every-conversation review at scale.")

    add(pm_role_evals(),
        note="Source slide 12. Three PM responsibilities: Drafting Quality, Setting Pass Thresholds, Auditing Automated Judges. PMs own the bar.")

    # Source slide 13 - Lab (originally Group, converted to solo)
    add(applied_work(
            title="Plan Your Eval Stack for Juno",
            goal="Build the trust architecture required to scale your judgement and move Juno from a prototype to a reliable product. Plan all three eval layers &mdash; user feedback, human evaluation, and automated assessment.",
            body_html=JUNO_EVAL_STACK_LAB_BODY,
            repo_path="juno-pm/06-evals/eval-stack.md",
            timer_min=25,
            tool_url="../Modules/M6%20-%20Eval%20Stack%20Designer.html",
            tool_desc="Three-layer planner with live SVG stack visualisation. Pre-loaded with a Juno P0 Triage starter. Exports straight to <code>06-evals/eval-stack.md</code>.",
        ),
        note="Solo lab (originally a group exercise). Output committed to 06-evals/eval-stack.md. Big M6 deliverable.")

    # ----- Section 03 -----
    add(section_divider("03", "AI Levers for Output Optimization"),
        note="Section 3 &mdash; when evals signal a gap, here&rsquo;s how PMs turn signal into action.")

    add(operationalize_risks(),
        note="Source slide 15. Three live KPIs: Hallucination Rate, Human Override Rate, Model Drift &amp; Latency. These are your dashboard.")

    add(governance_framework(),
        note="Source slide 16. Four governance strategies: Hard vs Soft Gates, Zero-Tolerance Metrics, Grounding for Trust, Build a Failure Taxonomy.")

    add(three_levers(),
        note="Source slide 17. Three levers: Prompt &middot; Model &middot; Data. PM rule of thumb: try prompt first, model next, data last. Architecture is the slowest, most expensive lever.")

    add(pm_execution_plan(),
        note="Source slide 18. Four-step PM execution plan with key decisions: Build Eval Plan / Set Gatekeepers / Add Production Guardrails / Evolve Roadmap.")

    # Source slide 19 - Lab (originally Group, converted to solo)
    add(applied_work(
            title="Prepare &amp; Finalise Your Project Deliverables",
            goal="Pull every artefact from M1&ndash;M6 into one polished <code>README.md</code> at the root of your <code>juno-pm</code> fork. The repo URL is your LMS submission &mdash; the README is the pitch.",
            body_html=JUNO_FINAL_DELIVERABLES_LAB_BODY,
            repo_path="juno-pm/README.md",
            timer_min=20,
            tool_url="../Modules/Final%20Project%20Deliverables%20Builder.html",
            tool_desc="Aggregates the seven source-slide sections + your Build Insights reflection into one polished README. Exports to the repo root.",
        ),
        note="Solo lab (originally a group exercise). Output is the polished README of the learner&rsquo;s juno-pm fork. The repo URL becomes their LMS submission.")

    # Source slide 20 - Learner Journey
    add(learner_journey(),
        note="Source slide 20. The complete six-module journey &mdash; the mindset shift + the win for each module.")

    # Source slide 21 - 5-min break
    add(break_section(), note="Source slide 21. 5-minute break.")

    # Source slide 22 - Cameras On reminder
    add(cameras_on(), note="Source slide 22. Cameras-on reminder for live cohort sessions.")

    # ----- Final Showcase -----
    # Source slide 23 - Final Project Showcase title (adapted for solo)
    add(final_showcase_title(),
        note="Source slide 23. Final-project showcase title. Solo course adaptation: the repo IS the demo.")

    # Source slide 24 - LMS submission reminder
    add(lms_reminder(),
        note="Source slide 24. LMS submission reminder. The URL of the finalised juno-pm fork is the deliverable.")

    # Source slide 25 - Presentation Kick-Off (adapted: three valid paths)
    add(presentation_kickoff(),
        note="Source slide 25. Adapted for solo: three valid paths (live demo, async Loom, just submit URL). All count for certification.")

    # Source slide 26 - Key Takeaways
    add(takeaways(
            "Measure AI Quality with Evals and Guardrails",
            [
                ("Replace vibe checks with systematic evaluation harnesses.",
                 "PMs catch invisible failures and make objective, data-driven launch decisions across diverse user intents."),
                ("Define hard gates with zero-tolerance metrics + a failure taxonomy.",
                 "Establishing sensitivity thresholds protects the brand by balancing safety against necessary product utility."),
                ("Implement an evaluation stack with all three layers.",
                 "Automated checks, human evals, and real-time user feedback ensure technical accuracy, nuanced tone, and value delivery are all measured for production."),
                ("Optimise via three levers: Prompt, Model, Data.",
                 "Identify whether to refine instructions, swap models, or clean RAG datasets &mdash; targeted system improvement, in that order."),
            ],
        ),
        note="Source slide 26. Recap of the four big M6 moves.")

    # Source slide 27 - Resources & Templates
    add(m6_resources_templates(),
        note="Source slide 27. Resources: Eval Stack Designer, Human Evaluation Rubric, Final Project Deliverables Builder, repo template.")

    # Source slide 28 - Q&A
    add(qa_section(),
        note="Source slide 28. Async-only Q&A. Park unresolved questions in #ai-pm-cohort. Instructor responds in-thread within ~5 days. Wrap warmly &mdash; this is the final live session.")

    return sections_inst, sections_share

