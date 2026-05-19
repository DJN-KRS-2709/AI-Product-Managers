"""Module 5 - Deploy Agentic Systems and Workflows.

Mirrors m1_v2 / m2_v2 / m3_v2 / m4_v2 structure:
- Reuses shared helpers from gen_module_decks
- Reuses class_expectations / cameras_on / section_divider from m1_v2
- Defines M5-specific visual helpers
- Exposes build_module_5() returning (sections_inst, sections_share)

Voice: solo only. The original "Breakout Group Exercise: Write Your AWSpec
for Juno" is converted to an Individual Exercise. The optional post-class
Langflow lab keeps its optional / extra-credit framing. No thank-you slide.

Source fidelity rule (RULE 0): every slide here maps 1:1 to the source
PowerPoint M5_Deploy Agentic Systems and Workflows.pptx (31 source slides).
No invented slides or framings.
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
# Source slide 3 - Syllabus
# ---------------------------------------------------------------------------

def syllabus_visual_m5() -> str:
    """6-card syllabus, M5 highlighted, M1-M4 marked done."""
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
         "current"),
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
    <div class="subtitle">Five modules done. Today: hand the wheel to the agent &mdash; with a written contract.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1040px; margin:24px auto 0;">
      {''.join(cells)}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Source slide 4 - Presentation Reminder
# ---------------------------------------------------------------------------

def presentation_reminder() -> str:
    return """<section class="centered" data-title="Presentation Reminder">
  <div class="inner">
    <div class="demo-tag tag-recall">Heads-up</div>
    <h2 style="margin-top:6px;">Final-project showcase &middot; volunteer slot</h2>
    <p style="font-size:15.5px; color:#cdd5e3; max-width:780px; margin:18px auto 0; line-height:1.65;">
      We&rsquo;re almost at the end. Now is your opportunity to volunteer and present your final project next class.
    </p>
    <p style="font-size:14.5px; color:#cdd5e3; max-width:780px; margin:14px auto 0; line-height:1.65;">
      We highly recommend this approach so you get live, actionable feedback. Your instructor will ask for 2&ndash;3 volunteers in Slack &mdash; first come, first served.
    </p>
    <p style="font-size:12.5px; color:#79c0ff; max-width:760px; margin:22px auto 0; padding:9px 16px; background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:8px;">
      Async cohort: drop a comment in <code>#ai-pm-cohort</code> with your project repo URL by Friday for written instructor feedback.
    </p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Source slide 5 - Agenda
# ---------------------------------------------------------------------------

def agenda_5() -> str:
    """3 numbered sections + optional post-class lab."""
    items = [
        ("01", "The Shift to Agentic Orchestration",
         "From answers to judgement. Agent anatomy, the autonomy spectrum, and how companies actually use agents.", "#3b82f6"),
        ("02", "Agentic Design Patterns",
         "ReAct, Planner-Executor, and the four memory types. Pick the wiring before you write the prompt.", "#fbbf24"),
        ("03", "Managing the Agentic Handoff",
         "The AWSpec, the Agent Control Panel, and the Decision Triangle. PM job: define the rules of engagement.", "#34d399"),
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
    <div class="subtitle">One in-class solo lab anchors the day &mdash; write the AWSpec for Juno. One optional post-class Langflow build.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
    <p style="font-size:11.5px; color:#bcb1ff; max-width:780px; margin:14px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">Bonus &middot; Post-class:</strong> Build Juno&rsquo;s Agentic Workflow in Langflow. Optional &mdash; not required for completion.
    </p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 01 - The Shift to Agentic Orchestration
# ---------------------------------------------------------------------------

def evolution_of_value() -> str:
    """Source slide 7 - Chatbot vs Workflows vs Agents.

    3-column comparison: Value Prop + Operating Model per generation.
    """
    cols = [
        ("01", "#3b82f6", "Chatbot",
         "Provide answers based on a knowledge base.",
         "Reactive: System responds only when prompted; user owns the workflow."),
        ("02", "#bcb1ff", "Workflows",
         "Provide execution of predefined steps across systems.",
         "Human-supervised: System follows a rigid track; human monitors the process."),
        ("03", "#34d399", "Agents",
         "Provide judgement for path choice based on real-time context.",
         "Autonomous: System chooses the next step; human sets the goal and the guardrails."),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; overflow:hidden; text-align:left; display:flex; flex-direction:column;">
  <div style="padding:16px 20px; background:linear-gradient(135deg, {col}22 0%, transparent 70%); border-bottom:1px solid {col}30;">
    <div style="display:flex; align-items:baseline; gap:10px;">
      <div style="font-family:'Poppins',sans-serif; font-size:30px; font-weight:900; color:{col}; line-height:1;">{n}</div>
      <div style="font-family:'Poppins',sans-serif; font-size:18px; font-weight:800; color:#fff;">{name}</div>
    </div>
  </div>
  <div style="padding:13px 20px; border-bottom:1px solid rgba(255,255,255,0.06);">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:{col}; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:4px;">Value prop</div>
    <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">{value}</p>
  </div>
  <div style="padding:13px 20px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:{col}; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:4px;">Operating model</div>
    <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">{model}</p>
  </div>
</div>"""
        for n, col, name, value, model in cols
    )
    return f"""<section data-title="The Evolution of Value">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Frame</div>
    <h2>From answers to judgement</h2>
    <div class="subtitle">This changes the dynamic between your user and your product &mdash; you now design for goals and guardrails, not turns and replies.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
    <p style="font-size:12px; color:#bcb1ff; max-width:880px; margin:14px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">PM lens:</strong> when the system gains judgement, your spec stops describing outputs and starts describing <em>rules of action</em>.
    </p>
  </div>
</section>
"""


def what_is_an_agent() -> str:
    """Source slide 8 - Definition + 3 traits."""
    intro = ("An agent is an intelligent system that interprets intent, makes decisions, "
             "and takes actions autonomously to achieve a goal. Unlike standard models, "
             "agents act on their environment, not just on prompts.")
    traits = [
        ("1", "&#x1F680;", "Proactive",
         "Acts on environmental triggers without direct user prompts or input.", "#3b82f6"),
        ("2", "&#x1F3AF;", "Task-Oriented",
         "Executes multi-step workflows to deliver finished outcomes.", "#fbbf24"),
        ("3", "&#x1F517;", "Integrated",
         "Connects with tool stacks to perform actions in the real world.", "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:18px 22px; text-align:left; display:flex; flex-direction:column; gap:10px;">
  <div style="display:flex; align-items:center; gap:12px;">
    <div style="font-family:'Poppins',sans-serif; font-size:34px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div style="font-size:28px;">{icon}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:17px; font-weight:800; color:#fff;">{title}</div>
  </div>
  <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>
</div>"""
        for n, icon, title, desc, col in traits
    )
    return f"""<section data-title="What Is an Agent">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Definition</div>
    <h2>What is an agent?</h2>
    <p style="font-size:14.5px; color:#cdd5e3; max-width:880px; margin:12px auto 0; line-height:1.6;">{intro}</p>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; max-width:1080px; margin:24px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


def agent_anatomy() -> str:
    """Source slide 9 - Brain (LLM) / Reasoning Engine / Strategy / Action layers,
    with the 'Plan a trip -> Search/Compare/Book + Past results' example.

    Big SVG that mirrors the source diagram.
    """
    return """<section data-title="Agent Anatomy">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Mental model</div>
    <h2>The anatomy of an agent</h2>
    <div class="subtitle">Three layers + a brain. Memory carries context, the brain decides, tools act.</div>

    <div style="max-width:1100px; margin:18px auto 0;">
      <svg viewBox="0 0 1100 460" preserveAspectRatio="xMidYMid meet" style="width:100%; height:auto; display:block;">
        <defs>
          <marker id="anaA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#79c0ff"/></marker>
          <marker id="anaG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#34d399"/></marker>
          <linearGradient id="brainBg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1e3a8a"/><stop offset="100%" stop-color="#0c2244"/></linearGradient>
          <linearGradient id="strategyBg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(124,140,255,0.18)"/><stop offset="100%" stop-color="rgba(124,140,255,0.05)"/></linearGradient>
          <linearGradient id="actionBg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(251,191,36,0.16)"/><stop offset="100%" stop-color="rgba(251,191,36,0.04)"/></linearGradient>
          <linearGradient id="contextBg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(52,211,153,0.16)"/><stop offset="100%" stop-color="rgba(52,211,153,0.04)"/></linearGradient>
        </defs>

        <rect x="40" y="20" width="1020" height="80" rx="14" fill="url(#strategyBg)" stroke="#bcb1ff" stroke-width="1" stroke-dasharray="4,4" opacity="0.9"/>
        <text x="60" y="42" fill="#bcb1ff" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">STRATEGY LAYER &middot; HOW</text>
        <text x="60" y="64" fill="#fff" font-family="Poppins,sans-serif" font-size="13" font-weight="800">Planning</text>
        <text x="60" y="84" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11.5">Decomposes the user&#39;s goal into ordered steps. Re-plans on failure.</text>

        <rect x="40" y="120" width="1020" height="190" rx="14" fill="rgba(7,22,44,0.55)" stroke="#79c0ff" stroke-width="1" opacity="0.9"/>
        <text x="60" y="142" fill="#79c0ff" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">REASONING ENGINE &middot; WHY</text>

        <rect x="430" y="158" width="240" height="130" rx="60" fill="url(#brainBg)" stroke="#79c0ff" stroke-width="2"/>
        <text x="550" y="195" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="18" font-weight="900">The Brain</text>
        <text x="550" y="220" text-anchor="middle" fill="#79c0ff" font-family="Poppins,sans-serif" font-size="12" font-weight="700" letter-spacing="2">LLM</text>
        <text x="550" y="248" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">Interprets intent. Picks the next step.</text>
        <text x="550" y="266" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">Asks tools. Reads results.</text>

        <rect x="80" y="170" width="270" height="110" rx="10" fill="rgba(255,255,255,0.04)" stroke="#bcb1ff" stroke-width="1.5"/>
        <text x="215" y="195" text-anchor="middle" fill="#bcb1ff" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">MEMORY</text>
        <text x="215" y="216" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="14" font-weight="800">Past results</text>
        <text x="215" y="240" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">What the agent has learned</text>
        <text x="215" y="256" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">across this run + prior runs.</text>

        <rect x="750" y="170" width="270" height="110" rx="10" fill="rgba(255,255,255,0.04)" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="885" y="195" text-anchor="middle" fill="#fbbf24" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">ARMS</text>
        <text x="885" y="216" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="14" font-weight="800">Tools</text>
        <text x="885" y="240" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">APIs, databases, automations</text>
        <text x="885" y="256" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">the brain can call into.</text>

        <path d="M 350 225 L 430 225" stroke="#79c0ff" stroke-width="1.8" fill="none" marker-end="url(#anaA)"/>
        <path d="M 670 225 L 750 225" stroke="#79c0ff" stroke-width="1.8" fill="none" marker-end="url(#anaA)"/>

        <rect x="40" y="330" width="1020" height="60" rx="14" fill="url(#actionBg)" stroke="#fbbf24" stroke-width="1" stroke-dasharray="4,4" opacity="0.9"/>
        <text x="60" y="354" fill="#fbbf24" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">ACTION LAYER &middot; WHAT</text>
        <text x="60" y="376" fill="#fff" font-family="Lato,sans-serif" font-size="11.5">The brain triggers tools. Tools change state in the world: searches, files, payments, posts, drafts.</text>

        <rect x="40" y="402" width="1020" height="48" rx="14" fill="url(#contextBg)" stroke="#34d399" stroke-width="1" stroke-dasharray="4,4" opacity="0.9"/>
        <text x="60" y="424" fill="#34d399" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">CONTEXT LAYER &middot; WHEN</text>
        <text x="60" y="442" fill="#fff" font-family="Lato,sans-serif" font-size="11.5">Goal &middot; Memory &middot; Environment. The conditions the agent runs inside.</text>

        <rect x="40" y="100" width="180" height="20" rx="0" fill="none"/>

        <g>
          <rect x="380" y="95" width="340" height="22" rx="11" fill="rgba(52,211,153,0.16)" stroke="#34d399" stroke-width="1"/>
          <text x="550" y="111" text-anchor="middle" fill="#34d399" font-family="Poppins,sans-serif" font-size="11" font-weight="900" letter-spacing="2">USER GOAL: &ldquo;PLAN A TRIP&rdquo;</text>
          <path d="M 550 117 L 550 154" stroke="#34d399" stroke-width="1.6" fill="none" marker-end="url(#anaG)"/>
        </g>

        <g font-family="Poppins,sans-serif" font-size="11" font-weight="800">
          <rect x="780" y="305" width="68" height="22" rx="11" fill="rgba(251,191,36,0.18)" stroke="#fbbf24" stroke-width="1"/>
          <text x="814" y="320" text-anchor="middle" fill="#fbbf24">SEARCH</text>
          <rect x="858" y="305" width="68" height="22" rx="11" fill="rgba(251,191,36,0.18)" stroke="#fbbf24" stroke-width="1"/>
          <text x="892" y="320" text-anchor="middle" fill="#fbbf24">COMPARE</text>
          <rect x="936" y="305" width="68" height="22" rx="11" fill="rgba(251,191,36,0.18)" stroke="#fbbf24" stroke-width="1"/>
          <text x="970" y="320" text-anchor="middle" fill="#fbbf24">BOOK</text>
        </g>
      </svg>
    </div>

    <p style="font-size:12px; color:#bcb1ff; max-width:880px; margin:14px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">PM read:</strong> the Strategy + Action layers are <em>your spec</em>. The brain ships with the model. The PM is responsible for everything around it.
    </p>
  </div>
</section>
"""


def agent_spectrum() -> str:
    """Source slide 10 - The Agent Spectrum, 4 levels (0-3) on a horizontal axis,
    with PM Accountability rising as autonomy rises.
    """
    levels = [
        ("0", "Reactive", "(No Autonomy)",
         "PM owns the prompt quality and response accuracy.",
         "#3b82f6"),
        ("1", "Function-Calling", "(Assisted Autonomy)",
         "PM owns tool selection logic and fallback behaviors.",
         "#fbbf24"),
        ("2", "Semi-Autonomous", "(Human-in-the-Loop)",
         "PM owns checkpoint design and approval thresholds.",
         "#bcb1ff"),
        ("3", "Fully Autonomous", "(Goal-Driven)",
         "PM owns the full guardrail spec, eval suite, and kill switch.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-top:3px solid {col}; border-radius:12px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:6px;">
  <div style="display:flex; align-items:baseline; gap:8px;">
    <div style="font-family:'Poppins',sans-serif; font-size:32px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div>
      <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:#fff; line-height:1.2;">{title}</div>
      <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:{col}; font-weight:700; letter-spacing:0.08em; text-transform:uppercase;">{sub}</div>
    </div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{accountability}</p>
</div>"""
        for n, title, sub, accountability, col in levels
    )
    return f"""<section data-title="The Agent Spectrum">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>The Agent Spectrum</h2>
    <div class="subtitle">More autonomy means assuming a higher level of operational accountability.</div>

    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; max-width:1100px; margin:22px auto 0;">
      {cards}
    </div>

    <div style="max-width:1100px; margin:14px auto 0;">
      <svg viewBox="0 0 1100 70" preserveAspectRatio="xMidYMid meet" style="width:100%; height:auto;">
        <defs>
          <linearGradient id="acctGrad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#3b82f6"/>
            <stop offset="33%" stop-color="#fbbf24"/>
            <stop offset="66%" stop-color="#bcb1ff"/>
            <stop offset="100%" stop-color="#34d399"/>
          </linearGradient>
        </defs>
        <text x="20" y="22" fill="#8899bb" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2.4">PM ACCOUNTABILITY</text>
        <rect x="20" y="32" width="1060" height="14" rx="7" fill="url(#acctGrad)" opacity="0.85"/>
        <text x="36" y="62" fill="#cdd5e3" font-family="Poppins,sans-serif" font-size="11" font-weight="700">low</text>
        <text x="1054" y="62" fill="#cdd5e3" font-family="Poppins,sans-serif" font-size="11" font-weight="700" text-anchor="end">very high</text>
      </svg>
    </div>

    <p style="font-size:12px; color:#bcb1ff; max-width:880px; margin:14px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">PM rule of thumb:</strong> ship the <em>lowest</em> level that delivers the job. Higher levels need explicit handoff rules and a real eval surface.
    </p>
  </div>
</section>
"""


def real_world_agents() -> str:
    """Source slide 11 - 5 industry examples. Refresh with current, hyped names.

    Source examples kept faithful, surfaced with current branding.
    """
    items = [
        ("&#x1F9EA;", "Drug Discovery",
         "Johnson &amp; Johnson",
         "Lab agents optimise chemical synthesis &mdash; determining reaction conditions, leveraging digital twins and ML for precision.",
         "#3b82f6"),
        ("&#x1F4DE;", "Support &amp; Resolution",
         "Uber &middot; Klarna",
         "Agents autonomously diagnose ride / order issues, gather evidence, trigger refunds, and execute resolution loops.",
         "#fbbf24"),
        ("&#x1F4B3;", "Financial Operations",
         "Stripe",
         "Agents investigate failed payments and regulatory compliance &mdash; retrieving policy context and analysing transaction telemetry.",
         "#bcb1ff"),
        ("&#x1F6CD;&#xFE0F;", "Merchant Operations",
         "Shopify Sidekick",
         "Agents manage store setups and inventory by reasoning over merchant context and calling internal APIs.",
         "#34d399"),
        ("&#x1F4BB;", "Developer Workflows",
         "Cursor &middot; Devin",
         "IDE agents plan refactors and apply edits across files, with full pull-request workflows.",
         "#79c0ff"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:12px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:6px;">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:2px;">
    <div style="font-size:24px;">{ic}</div>
    <div>
      <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:{col}; font-weight:900; letter-spacing:0.13em; text-transform:uppercase;">{tag}</div>
      <div style="font-family:'Poppins',sans-serif; font-size:13.5px; font-weight:800; color:#fff; line-height:1.25;">{co}</div>
    </div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{desc}</p>
</div>"""
        for ic, tag, co, desc, col in items
    )
    return f"""<section data-title="Real-World Examples">
  <div class="inner">
    <div class="demo-tag tag-case">Case Studies</div>
    <h2>How companies are using agents</h2>
    <div class="subtitle">Five domains. Same shape: bounded scope, explicit tools, human checkpoints at risky steps.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1100px; margin:22px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 02 - Agentic Design Patterns
# ---------------------------------------------------------------------------

def why_patterns_matter() -> str:
    """Source slide 13 - Designing for Outcomes."""
    points = [
        ("1", "Patterns provide a common vocabulary",
         "Define expected AI output behaviors in your AI PRD &mdash; so engineering and PM agree on <em>how the agent thinks</em>, not just what it returns.",
         "#3b82f6"),
        ("2", "Patterns enforce a reasoning structure",
         "They prevent orchestration-gap failures like reasoning drift and infinite loops. The wiring choice is the spec.",
         "#fbbf24"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-left:4px solid {col}; border-radius:12px; padding:18px 22px; text-align:left;">
  <div style="display:flex; align-items:baseline; gap:14px; margin-bottom:8px;">
    <div style="font-family:'Poppins',sans-serif; font-size:42px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:15.5px; font-weight:800; color:#fff; line-height:1.3;">{title}</div>
  </div>
  <p style="font-size:13px; color:#cdd5e3; margin:0; line-height:1.6;">{body}</p>
</div>"""
        for n, title, body, col in points
    )
    return f"""<section data-title="Why Patterns Matter">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Frame</div>
    <div style="font-family:'Poppins',sans-serif; font-size:10.5px; color:#fbbf24; font-weight:900; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:6px;">Why patterns matter</div>
    <h2>Designing for outcomes</h2>
    <p style="font-size:14.5px; color:#cdd5e3; max-width:880px; margin:12px auto 0; line-height:1.6;">
      You don&rsquo;t solve complex agentic problems with a better prompt. You solve them by choosing how the agent is wired to think.
    </p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; max-width:1080px; margin:24px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


def react_pattern() -> str:
    """Source slide 14 - ReAct: Reason - Action - Observe loop, with inner monologue."""
    return """<section data-title="ReAct Pattern">
  <div class="inner">
    <div class="demo-tag tag-framework">Agentic Pattern &middot; 1 of 2</div>
    <h2>ReAct &mdash; the agent that thinks before it acts</h2>
    <div class="subtitle">A continuous <em>Reason &rarr; Act &rarr; Observe</em> loop verifies logic against real-world data before delivering the final answer.</div>

    <div style="display:grid; grid-template-columns:1.05fr 0.95fr; gap:16px; max-width:1100px; margin:22px auto 0; align-items:stretch;">

      <div style="background:rgba(7,22,44,0.55); border:1px solid var(--card-border, rgba(255,255,255,0.08)); border-radius:14px; padding:14px 12px;">
        <svg viewBox="0 0 520 360" preserveAspectRatio="xMidYMid meet" style="width:100%; height:auto; display:block;">
          <defs>
            <marker id="reactA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#79c0ff"/></marker>
            <marker id="reactG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#34d399"/></marker>
          </defs>

          <text x="260" y="28" text-anchor="middle" fill="#bcb1ff" font-family="Poppins,sans-serif" font-size="11" font-weight="900" letter-spacing="2.4">THE INNER MONOLOGUE</text>

          <ellipse cx="135" cy="105" rx="86" ry="46" fill="rgba(59,130,246,0.18)" stroke="#79c0ff" stroke-width="1.6"/>
          <text x="135" y="98" text-anchor="middle" fill="#79c0ff" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">THINK</text>
          <text x="135" y="118" text-anchor="middle" fill="#fff" font-family="Lato,sans-serif" font-size="11" font-weight="700">"I need to find the source"</text>

          <ellipse cx="385" cy="105" rx="86" ry="46" fill="rgba(251,191,36,0.18)" stroke="#fbbf24" stroke-width="1.6"/>
          <text x="385" y="98" text-anchor="middle" fill="#fbbf24" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">ACT</text>
          <text x="385" y="118" text-anchor="middle" fill="#fff" font-family="Lato,sans-serif" font-size="11" font-weight="700">"Calls Search Tool"</text>

          <ellipse cx="260" cy="220" rx="120" ry="46" fill="rgba(124,140,255,0.16)" stroke="#bcb1ff" stroke-width="1.6"/>
          <text x="260" y="213" text-anchor="middle" fill="#bcb1ff" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">OBSERVE</text>
          <text x="260" y="233" text-anchor="middle" fill="#fff" font-family="Lato,sans-serif" font-size="11" font-weight="700">"Reads API result: data found"</text>

          <path d="M 215 113 Q 260 98 305 113" stroke="#79c0ff" stroke-width="1.8" fill="none" marker-end="url(#reactA)"/>
          <path d="M 372 152 Q 320 200 312 192" stroke="#79c0ff" stroke-width="1.8" fill="none" marker-end="url(#reactA)"/>
          <path d="M 200 192 Q 145 175 145 152" stroke="#79c0ff" stroke-width="1.8" fill="none" marker-end="url(#reactA)"/>

          <path d="M 260 268 L 260 295" stroke="#bcb1ff" stroke-width="1.5" fill="none" stroke-dasharray="4,4"/>
          <rect x="155" y="295" width="210" height="36" rx="18" fill="rgba(124,140,255,0.18)" stroke="#bcb1ff" stroke-width="1"/>
          <text x="260" y="318" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="11" font-weight="800">"Does this answer the question?"</text>
          <text x="380" y="318" fill="#34d399" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">YES &rarr;</text>

          <rect x="425" y="295" width="80" height="36" rx="6" fill="rgba(52,211,153,0.18)" stroke="#34d399" stroke-width="1"/>
          <text x="465" y="319" text-anchor="middle" fill="#34d399" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">FINAL</text>
        </svg>
      </div>

      <div style="display:flex; flex-direction:column; gap:10px; text-align:left;">
        <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.30); border-radius:12px; padding:14px 18px;">
          <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:6px;">&#x2699;&#xFE0F; Mechanism</div>
          <p style="font-size:13px; color:#cdd5e3; margin:0; line-height:1.6;">A <em>Reason &rarr; Act &rarr; Observe</em> loop verifies the agent&rsquo;s logic against real-world data before delivering the final response.</p>
        </div>
        <div style="background:rgba(251,191,36,0.05); border:1px solid rgba(251,191,36,0.30); border-radius:12px; padding:14px 18px;">
          <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#fbbf24; font-weight:900; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:6px;">&#x1F4A1; Value</div>
          <p style="font-size:13px; color:#cdd5e3; margin:0; line-height:1.6;">Solves high-variability problems by &ldquo;thinking out loud&rdquo; &mdash; producing a visible reasoning trace for easier debugging.</p>
        </div>
        <div style="background:rgba(248,113,113,0.05); border:1px solid rgba(248,113,113,0.30); border-radius:12px; padding:14px 18px;">
          <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#f87171; font-weight:900; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:6px;">&#x26A0;&#xFE0F; Cost</div>
          <p style="font-size:13px; color:#cdd5e3; margin:0; line-height:1.6;">Every loop adds latency and tokens. Bound the loop with a <code>max_steps</code> ceiling.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""


def planner_executor_pattern() -> str:
    """Source slide 15 - Planner-Executor with handoff."""
    return """<section data-title="Planner-Executor Pattern">
  <div class="inner">
    <div class="demo-tag tag-framework">Agentic Pattern &middot; 2 of 2</div>
    <h2>Planner-Executor &mdash; the agent that maps its own roadmap</h2>
    <div class="subtitle">A planner agent decomposes the goal. One or many executor agents run the steps. The planner re-plans on failure.</div>

    <div style="background:rgba(7,22,44,0.55); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px 16px; max-width:1100px; margin:22px auto 0;">
      <svg viewBox="0 0 1080 320" preserveAspectRatio="xMidYMid meet" style="width:100%; height:auto; display:block;">
        <defs>
          <marker id="peA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#79c0ff"/></marker>
          <marker id="peY" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#fbbf24"/></marker>
        </defs>

        <rect x="40" y="58" width="200" height="60" rx="10" fill="rgba(52,211,153,0.16)" stroke="#34d399" stroke-width="1.5"/>
        <text x="140" y="80" text-anchor="middle" fill="#34d399" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">USER INPUT</text>
        <text x="140" y="102" text-anchor="middle" fill="#fff" font-family="Lato,sans-serif" font-size="14" font-weight="700">"Plan a trip"</text>

        <path d="M 240 88 L 305 88" stroke="#79c0ff" stroke-width="1.8" fill="none" marker-end="url(#peA)"/>

        <rect x="305" y="40" width="220" height="100" rx="50" fill="rgba(59,130,246,0.18)" stroke="#79c0ff" stroke-width="2"/>
        <text x="415" y="78" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="16" font-weight="900">Planner Agent</text>
        <text x="415" y="98" text-anchor="middle" fill="#79c0ff" font-family="Poppins,sans-serif" font-size="11" font-weight="700">(The Brain)</text>
        <text x="415" y="120" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">Decomposes goal &rarr; ordered steps.</text>

        <text x="595" y="70" text-anchor="middle" fill="#fbbf24" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">HANDOFF</text>
        <path d="M 525 90 L 670 90" stroke="#fbbf24" stroke-width="1.8" fill="none" marker-end="url(#peY)" stroke-dasharray="6,4"/>

        <rect x="670" y="40" width="220" height="100" rx="50" fill="rgba(251,191,36,0.18)" stroke="#fbbf24" stroke-width="2"/>
        <text x="780" y="78" text-anchor="middle" fill="#fff" font-family="Poppins,sans-serif" font-size="16" font-weight="900">Executor Agent</text>
        <text x="780" y="98" text-anchor="middle" fill="#fbbf24" font-family="Poppins,sans-serif" font-size="11" font-weight="700">(The Doer)</text>
        <text x="780" y="120" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">Runs each step. Reports back.</text>

        <text x="500" y="190" text-anchor="middle" fill="#bcb1ff" font-family="Poppins,sans-serif" font-size="10" font-weight="900" letter-spacing="2">TASK LIST</text>

        <g font-family="Poppins,sans-serif" font-size="13" font-weight="800">
          <rect x="80" y="210" width="180" height="48" rx="8" fill="rgba(255,255,255,0.04)" stroke="#bcb1ff" stroke-width="1.2"/>
          <text x="170" y="240" text-anchor="middle" fill="#fff">1. Book Flight</text>

          <rect x="290" y="210" width="180" height="48" rx="8" fill="rgba(255,255,255,0.04)" stroke="#bcb1ff" stroke-width="1.2"/>
          <text x="380" y="240" text-anchor="middle" fill="#fff">2. Book Hotel</text>

          <rect x="500" y="210" width="180" height="48" rx="8" fill="rgba(255,255,255,0.04)" stroke="#bcb1ff" stroke-width="1.2"/>
          <text x="590" y="240" text-anchor="middle" fill="#fff">3. Book Transit</text>

          <rect x="710" y="210" width="270" height="48" rx="8" fill="rgba(52,211,153,0.10)" stroke="#34d399" stroke-width="1.2"/>
          <text x="845" y="240" text-anchor="middle" fill="#34d399">&check; Completes Task 1</text>
        </g>

        <path d="M 415 158 L 415 200" stroke="#79c0ff" stroke-width="1.5" fill="none" stroke-dasharray="3,3"/>
        <path d="M 780 158 L 780 200" stroke="#fbbf24" stroke-width="1.5" fill="none" stroke-dasharray="3,3"/>
      </svg>

      <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-top:14px;">
        <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.30); border-radius:10px; padding:10px 14px; text-align:left;">
          <div style="font-family:'Poppins',sans-serif; font-size:9px; color:#79c0ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">&#x2699;&#xFE0F; Mechanism</div>
          <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">Planner decomposes &amp; sequences. Executor(s) run, report, escalate.</p>
        </div>
        <div style="background:rgba(251,191,36,0.05); border:1px solid rgba(251,191,36,0.30); border-radius:10px; padding:10px 14px; text-align:left;">
          <div style="font-family:'Poppins',sans-serif; font-size:9px; color:#fbbf24; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">&#x1F4A1; Value</div>
          <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">Best for multi-step tasks with parallelism &mdash; the planner can fork executors.</p>
        </div>
        <div style="background:rgba(248,113,113,0.05); border:1px solid rgba(248,113,113,0.30); border-radius:10px; padding:10px 14px; text-align:left;">
          <div style="font-family:'Poppins',sans-serif; font-size:9px; color:#f87171; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">&#x26A0;&#xFE0F; Cost</div>
          <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">Two surfaces to debug. Spec the handoff contract crisply.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""


def types_of_memory() -> str:
    """Source slide 16 - 4 memory types."""
    types_ = [
        ("1", "Episodic",
         "Track the sequence of actions taken within a specific multi-step task.",
         "Within one run", "#3b82f6"),
        ("2", "Semantic",
         "Store persistent behaviours, user preferences, and core system instructions.",
         "Across sessions", "#fbbf24"),
        ("3", "Working / Contextual",
         "Manage the immediate data and variables currently being processed.",
         "Live, in-flight", "#bcb1ff"),
        ("4", "External Tools",
         "Access real-world systems and live databases via persistent APIs.",
         "Source of truth", "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:12px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:8px;">
  <div style="display:flex; align-items:baseline; gap:10px;">
    <div style="font-family:'Poppins',sans-serif; font-size:32px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div>
      <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:#fff; line-height:1.2;">{name}</div>
      <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:{col}; font-weight:700; letter-spacing:0.1em; text-transform:uppercase;">{lifetime}</div>
    </div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{desc}</p>
</div>"""
        for n, name, desc, lifetime, col in types_
    )
    return f"""<section data-title="Types of Agentic Memory">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>Types of agentic memory</h2>
    <p style="font-size:14.5px; color:#cdd5e3; max-width:880px; margin:12px auto 0; line-height:1.6;">
      Just like humans have different ways of remembering, agents leverage distinct memory types for different purposes.
    </p>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; max-width:1100px; margin:24px auto 0;">
      {cards}
    </div>
    <p style="font-size:12px; color:#bcb1ff; max-width:880px; margin:14px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">PM rule:</strong> spec each memory type explicitly &mdash; including the &ldquo;no&rsquo;s.&rdquo; &ldquo;Juno does not maintain long-term memory of customer-specific contracts&rdquo; is a spec line worth writing.
    </p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 03 - Managing the Agentic Handoff
# ---------------------------------------------------------------------------

def awspec_blueprint() -> str:
    """Source slide 20 - The Agent Workflow Spec (one-page blueprint)."""
    parts = [
        ("1", "Actors",
         "Define which agents, tools, and humans are involved in the loop. Be explicit about who is the pilot driving the goal and exactly when control passes back.",
         "Who is in the loop?", "#3b82f6"),
        ("2", "Pattern Plan",
         "Identify which core agentic pattern(s) will be used. Map the key sequential steps the agent must take to transform the initial goal into outcomes.",
         "Which wiring + steps?", "#fbbf24"),
        ("3", "Memory",
         "Specify what information must persist across the session and define the scope. Determine what needs to be in working memory versus what can be retrieved.",
         "What persists, where?", "#bcb1ff"),
        ("4", "Tools",
         "List the specific APIs and internal databases the agent is authorized to call. Define the required schemas and read / write boundaries.",
         "Which APIs, what scope?", "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:16px 20px; text-align:left; display:flex; flex-direction:column; gap:10px;">
  <div style="display:flex; align-items:baseline; gap:10px;">
    <div style="font-family:'Poppins',sans-serif; font-size:32px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div>
      <div style="font-family:'Poppins',sans-serif; font-size:15.5px; font-weight:800; color:#fff;">{title}</div>
      <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:{col}; font-weight:800; letter-spacing:0.13em; text-transform:uppercase;">{q}</div>
    </div>
  </div>
  <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>
</div>"""
        for n, title, desc, q, col in parts
    )
    return f"""<section data-title="The AWSpec">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <div style="font-family:'Poppins',sans-serif; font-size:10.5px; color:#34d399; font-weight:900; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:6px;">One-page blueprint</div>
    <h2>The Agent Workflow Spec (AWSpec)</h2>
    <p style="font-size:14.5px; color:#cdd5e3; max-width:920px; margin:12px auto 0; line-height:1.6;">
      Your <em>technical bridge</em> for translating a high-level agentic feature into a structured, governable design that engineering can actually build &mdash; and that you can measure.
    </p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


JUNO_AWSPEC_LAB_BODY = """
<div style="max-width:980px; margin:14px auto 0; text-align:left;">

<p style="font-size:13.5px; color:#cdd5e3; line-height:1.6; margin:0 0 12px;">
  Review your Juno prototype and find the <strong>transition points</strong> between synthesising data, prioritising risks, and drafting the spec. Now turn those transitions into autonomous logic.
</p>

<div style="background:rgba(124,140,255,0.05); border:1px solid rgba(124,140,255,0.25); border-radius:12px; padding:14px 18px; margin:12px 0; font-size:12.5px; color:#cdd5e3;">
  <strong style="color:#bcb1ff;">Was a group breakout &middot; converted to solo.</strong> You write your own AWSpec. Self-review checklist + AI-review prompt are inside the tool.
</div>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:14px 0;">
  <div style="background:rgba(7,22,44,0.55); border:1px solid rgba(96,165,250,0.30); border-radius:10px; padding:12px 14px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Step 1 &middot; Open</div>
    <p style="margin:0; font-size:12.5px; color:#cdd5e3; line-height:1.5;">Open <code style="color:#79c0ff;">M5 - Agent Workflow Spec Builder.html</code>. The 4 pillars are pre-loaded with a Juno scenario &mdash; tweak them.</p>
  </div>
  <div style="background:rgba(7,22,44,0.55); border:1px solid rgba(251,191,36,0.30); border-radius:10px; padding:12px 14px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#fbbf24; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Step 2 &middot; Spec the wiring</div>
    <p style="margin:0; font-size:12.5px; color:#cdd5e3; line-height:1.5;">Define <strong>Actors &middot; Pattern Plan &middot; Memory &middot; Tools</strong>. Use ReAct unless you have a real reason for Planner-Executor.</p>
  </div>
  <div style="background:rgba(7,22,44,0.55); border:1px solid rgba(124,140,255,0.30); border-radius:10px; padding:12px 14px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#bcb1ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Step 3 &middot; Visualise + ground</div>
    <p style="margin:0; font-size:12.5px; color:#cdd5e3; line-height:1.5;">The diagram on the right rebuilds live as you type. Cross-check with your <code style="color:#bcb1ff;">03-rag-prd/ai-prd.md</code> &mdash; tools and data flows must line up.</p>
  </div>
  <div style="background:rgba(7,22,44,0.55); border:1px solid rgba(52,211,153,0.30); border-radius:10px; padding:12px 14px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#34d399; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Step 4 &middot; Commit</div>
    <p style="margin:0; font-size:12.5px; color:#cdd5e3; line-height:1.5;">Copy as markdown &rarr; <code style="color:#34d399;">05-agentic-workflows/awspec.md</code>. Push. Drop the link in <code>#ai-pm-cohort</code>.</p>
  </div>
</div>

</div>
"""


def orchestration_gap() -> str:
    """Source slide 22 - The Orchestration Gap, 4 failure modes with mocks.

    The 4 failures: Silent Failures, Reasoning Drift, Infinite Loops, Latency Tax.
    """
    failures = [
        ("&#x1F4A4;", "Silent Failures",
         "When a tool returns &ldquo;No data,&rdquo; the agent may falsely assume the task is complete instead of verifying the query logic.",
         "tool: search('Q1 churn cohort')\n&rarr; result: []\n&rarr; agent: \"Task complete.\" &check;",
         "#3b82f6"),
        ("&#x1F300;", "Reasoning Drift",
         "After multiple loops, the agent can lose its &ldquo;North Star&rdquo; and begin autonomously solving for the wrong sub-task.",
         "step 1: synthesise risks\nstep 2: prioritise risks\nstep 6: ...explain methodology",
         "#fbbf24"),
        ("&#x267B;&#xFE0F;", "Infinite Loops",
         "The agent gets stuck in a thought-action cycle, repeatedly trying a failing tool without recognising a logical dead end.",
         "Think &rarr; Act &rarr; Observe (fail)\nThink &rarr; Act &rarr; Observe (fail)\nThink &rarr; Act &rarr; Observe (fail)&hellip;",
         "#bcb1ff"),
        ("&#x23F1;&#xFE0F;", "The Latency Tax",
         "Each autonomous reasoning step adds cumulative seconds; a 5-step loop can force a user to wait 40+ seconds for a result.",
         "step 1 (8s)  step 2 (7s)\nstep 3 (12s) step 4 (6s)\nstep 5 (9s) &rarr; total: 42s",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-left:4px solid {col}; border-radius:12px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:8px;">
  <div style="display:flex; align-items:center; gap:10px;">
    <div style="font-size:24px;">{ic}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:14.5px; font-weight:800; color:#fff;">{name}</div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{desc}</p>
  <pre style="margin:0; padding:8px 10px; background:rgba(0,0,0,0.30); border-radius:6px; font-family:'IBM Plex Mono',monospace; font-size:10px; color:{col}; white-space:pre-wrap; line-height:1.5;">{snippet}</pre>
</div>"""
        for ic, name, desc, snippet, col in failures
    )
    return f"""<section data-title="The Orchestration Gap">
  <div class="inner">
    <div class="demo-tag tag-provocation">Common failure modes</div>
    <h2>The Orchestration Gap</h2>
    <div class="subtitle">When patterns fail, they fail in predictable shapes. Spec defences for each.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


def control_panel() -> str:
    """Source slide 23 - From Logic to Control: A PM's Agent Control Panel."""
    levers = [
        ("1", "Define Stop Conditions",
         "Set the number of <code>max_steps</code> to prevent infinite loops and cost overruns.",
         "#3b82f6"),
        ("2", "Structure Tool Outputs",
         "Partner with engineering to ensure APIs return clear observations and avoid hallucinations.",
         "#fbbf24"),
        ("3", "Set Confidence Thresholds",
         "Define when an agent&rsquo;s thoughts trigger human-in-the-loop reviews.",
         "#bcb1ff"),
        ("4", "Manage the North Star",
         "Provide the system instructions an agent re-reads in every loop to prevent reasoning drift.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-top:3px solid {col}; border-radius:12px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:6px;">
  <div style="display:flex; align-items:baseline; gap:10px;">
    <div style="font-family:'Poppins',sans-serif; font-size:30px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:13.5px; font-weight:800; color:#fff; line-height:1.2;">{title}</div>
  </div>
  <p style="font-size:12px; color:#cdd5e3; margin:0; line-height:1.55;">{desc}</p>
</div>"""
        for n, title, desc, col in levers
    )
    return f"""<section data-title="A PM&rsquo;s Agent Control Panel">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <div style="font-family:'Poppins',sans-serif; font-size:10.5px; color:#79c0ff; font-weight:900; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:6px;">From logic to control</div>
    <h2>A PM&rsquo;s Agent Control Panel</h2>
    <div class="subtitle">Four levers you specify. Engineering implements. You measure.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; max-width:1100px; margin:22px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


def rules_of_engagement() -> str:
    """Source slide 24 - Defining the Rules of Engagement, 4 categories."""
    rules = [
        ("&#x1F510;", "Agency Permission",
         "You define the autonomy threshold.",
         "An agent can <strong>draft</strong> a $5k quote but cannot hit <em>&ldquo;Send.&rdquo;</em>",
         "#3b82f6"),
        ("&#x1F511;", "Access Control",
         "You identify the read/write boundaries for every tool and database.",
         "The agent can <strong>read</strong> the HR handbook but cannot <strong>edit</strong> payroll.",
         "#fbbf24"),
        ("&#x21A9;&#xFE0F;", "Fallback Protocols",
         "You specify the fallback experience when loops break or gates are triggered.",
         "After <strong>3 failed attempts</strong> to resolve, the agent must escalate to a human.",
         "#bcb1ff"),
        ("&#x1F6A8;", "Checkpoints",
         "You set the red-zone triggers for human intervention based on risk, value, or ambiguity.",
         "Any <strong>legal-policy change</strong> by an agent requires a human approval step.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:12px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:8px;">
  <div style="display:flex; align-items:center; gap:10px;">
    <div style="font-size:22px;">{ic}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:13.5px; font-weight:800; color:#fff;">{name}</div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{desc}</p>
  <div style="background:rgba(0,0,0,0.25); border-left:3px solid {col}; padding:7px 10px; border-radius:0 6px 6px 0;">
    <div style="font-family:'Poppins',sans-serif; font-size:9px; color:{col}; font-weight:900; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:2px;">e.g.</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.5;">{example}</p>
  </div>
</div>"""
        for ic, name, desc, example, col in rules
    )
    return f"""<section data-title="Rules of Engagement">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>Defining the rules of engagement</h2>
    <div class="subtitle">Four contracts the PM owns &mdash; one per axis of risk.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
  </div>
</section>
"""


def decision_triangle() -> str:
    """Source slide 25 - The PM Decision Triangle: Latency / Cost / Accuracy."""
    return """<section data-title="The PM Decision Triangle">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <div style="font-family:'Poppins',sans-serif; font-size:10.5px; color:#fbbf24; font-weight:900; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:6px;">Balancing trade-offs</div>
    <h2>The PM Decision Triangle</h2>
    <div class="subtitle">Three axes. Pick two to optimise &mdash; the third pays the bill.</div>

    <div style="max-width:1000px; margin:22px auto 0; background:rgba(7,22,44,0.55); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:14px;">
      <svg viewBox="0 0 1000 420" preserveAspectRatio="xMidYMid meet" style="width:100%; height:auto; display:block;">
        <defs>
          <linearGradient id="triFill" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(96,165,250,0.18)"/><stop offset="100%" stop-color="rgba(124,140,255,0.05)"/></linearGradient>
        </defs>

        <polygon points="500,40 80,360 920,360" fill="url(#triFill)" stroke="#79c0ff" stroke-width="1.5"/>

        <circle cx="500" cy="40" r="9" fill="#3b82f6" stroke="#fff" stroke-width="2"/>
        <text x="500" y="22" text-anchor="middle" fill="#3b82f6" font-family="Poppins,sans-serif" font-size="13" font-weight="900" letter-spacing="2">LATENCY</text>
        <text x="500" y="-2" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11" dy="0">(Speed / UX)</text>

        <circle cx="80" cy="360" r="9" fill="#fbbf24" stroke="#fff" stroke-width="2"/>
        <text x="80" y="385" text-anchor="middle" fill="#fbbf24" font-family="Poppins,sans-serif" font-size="13" font-weight="900" letter-spacing="2">COST</text>
        <text x="80" y="404" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">(Efficiency / ROI)</text>

        <circle cx="920" cy="360" r="9" fill="#34d399" stroke="#fff" stroke-width="2"/>
        <text x="920" y="385" text-anchor="middle" fill="#34d399" font-family="Poppins,sans-serif" font-size="13" font-weight="900" letter-spacing="2">ACCURACY</text>
        <text x="920" y="404" text-anchor="middle" fill="#cdd5e3" font-family="Lato,sans-serif" font-size="11">(Quality / Reasoning)</text>

        <g font-family="Lato,sans-serif" font-size="11.5">
          <rect x="240" y="120" width="170" height="64" rx="10" fill="rgba(59,130,246,0.10)" stroke="#79c0ff" stroke-width="1"/>
          <text x="325" y="142" text-anchor="middle" fill="#79c0ff" font-family="Poppins,sans-serif" font-size="9.5" font-weight="900" letter-spacing="2">LATENCY LEVERS</text>
          <text x="325" y="162" text-anchor="middle" fill="#fff">Single-pass routing</text>
          <text x="325" y="178" text-anchor="middle" fill="#fff">Smaller models on path</text>

          <rect x="170" y="244" width="190" height="80" rx="10" fill="rgba(251,191,36,0.10)" stroke="#fbbf24" stroke-width="1"/>
          <text x="265" y="266" text-anchor="middle" fill="#fbbf24" font-family="Poppins,sans-serif" font-size="9.5" font-weight="900" letter-spacing="2">COST LEVERS</text>
          <text x="265" y="286" text-anchor="middle" fill="#fff">Open-source models</text>
          <text x="265" y="302" text-anchor="middle" fill="#fff">Prompt caching</text>
          <text x="265" y="318" text-anchor="middle" fill="#fff">Slimmer context</text>

          <rect x="640" y="244" width="190" height="80" rx="10" fill="rgba(52,211,153,0.10)" stroke="#34d399" stroke-width="1"/>
          <text x="735" y="266" text-anchor="middle" fill="#34d399" font-family="Poppins,sans-serif" font-size="9.5" font-weight="900" letter-spacing="2">ACCURACY LEVERS</text>
          <text x="735" y="286" text-anchor="middle" fill="#fff">Reflection loops</text>
          <text x="735" y="302" text-anchor="middle" fill="#fff">Multi-step planning</text>
          <text x="735" y="318" text-anchor="middle" fill="#fff">Verifier agents</text>
        </g>
      </svg>
    </div>

    <p style="font-size:12px; color:#bcb1ff; max-width:880px; margin:14px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">PM rule:</strong> name the corner you&rsquo;re sacrificing in the AWSpec. &ldquo;We are buying accuracy at the cost of latency&rdquo; is a defensible decision. Silence isn&rsquo;t.
    </p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Source slide 28 - Bonus Resources & Templates
# ---------------------------------------------------------------------------

def m5_resources_templates() -> str:
    awspec_url = "../Modules/M5 - Agent Workflow Spec Builder.html"
    panel_url = "../Modules/M5 - Agent Control Panel.html"
    langflow_url = "../Modules/M5 - Juno Langflow Walkthrough.html"
    cards = [
        ("&#x270D;&#xFE0F; In-Class Lab Tool", "Write Juno&rsquo;s AWSpec",
         "M5 &mdash; Agent Workflow Spec Builder",
         "4-pillar walkthrough (Actors, Pattern Plan, Memory, Tools). Live diagram + visualize prompt. Exports straight to <code style=\"font-size:0.9em; color:#3b82f6;\">05-agentic-workflows/awspec.md</code>.",
         awspec_url, "#3b82f6"),
        ("&#x1F39B;&#xFE0F; Companion Tool", "Spec Juno&rsquo;s Agent Control Panel",
         "M5 &mdash; Agent Control Panel",
         "Four levers + the four rules of engagement. Outputs <code style=\"font-size:0.9em; color:#fbbf24;\">05-agentic-workflows/agent-control-panel.md</code>.",
         panel_url, "#fbbf24"),
        ("&#x1F680; Optional Post-Class", "Build Juno&rsquo;s Workflow in Langflow",
         "M5 &mdash; Juno Langflow Walkthrough",
         "Step-by-step rebuild of <code style=\"font-size:0.9em; color:#bcb1ff;\">Juno Agent.json</code>. Visual node-graph guide.",
         langflow_url, "#bcb1ff"),
        ("&#x1F4DA; Project Repo Template", "One-click create your <code style=\"font-size:0.9em; color:#34d399;\">juno-pm</code> repo",
         "ai-product-management-template",
         "Use the template if you haven&rsquo;t already.",
         TEMPLATE_USE_URL, "#34d399"),
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
    <div class="demo-tag tag-debrief">Bonus &middot; Resources</div>
    <h2>Resources &amp; templates</h2>
    <div class="subtitle">All M5 tools live in <code>/Modules/</code>. Deliverables commit to <code>05-agentic-workflows/</code>.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; max-width:1040px; margin:22px auto 0;">
      {cards_html}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Source slides 30 + 31 - Optional Post-Class Hands-On Lab
# ---------------------------------------------------------------------------

def optional_post_class_title_5() -> str:
    return """<section class="centered" data-title="Optional Post-Class Lab">
  <div class="inner">
    <div class="demo-tag tag-debrief">Optional &middot; Post-class</div>
    <h2 style="font-size:46px; margin-top:8px;">Hands-On Lab</h2>
    <p style="font-family:'Poppins',sans-serif; font-size:24px; font-weight:800; color:#fbbf24; margin-top:14px;">Build Juno&rsquo;s Agentic Workflow in Langflow</p>
    <p style="font-size:14px; color:#cdd5e3; max-width:700px; margin:18px auto 0; line-height:1.65;">
      Optional. Not required for course completion. Hand the AWSpec to a real agent runtime and watch the wiring come alive.
    </p>
  </div>
</section>
"""


def optional_post_class_outcome_5() -> str:
    langflow_url = "../Modules/M5 - Juno Langflow Walkthrough.html"
    return f"""<section data-title="Optional Post-Class Outcome">
  <div class="inner">
    <div class="demo-tag tag-debrief">Optional &middot; Post-class</div>
    <h2>Run your AWSpec in a real graph</h2>
    <div class="subtitle">Open the walkthrough. Import the starter Langflow JSON. Plug in an OpenAI key. Trigger Juno on a sample P0 thread.</div>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; max-width:1000px; margin:22px auto 0; text-align:left;">
      <div style="background:rgba(124,140,255,0.05); border:1px solid rgba(124,140,255,0.30); border-radius:12px; padding:14px 18px;">
        <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#bcb1ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">Path 1 &middot; Rebuild from Scratch</div>
        <p style="font-size:13px; color:#cdd5e3; margin:0; line-height:1.6;">Architect Juno node-by-node in Langflow. Best for understanding how each AWSpec section maps to a real agent graph.</p>
      </div>
      <div style="background:rgba(251,191,36,0.05); border:1px solid rgba(251,191,36,0.30); border-radius:12px; padding:14px 18px;">
        <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#fbbf24; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">Path 2 &middot; Import the Starter</div>
        <p style="font-size:13px; color:#cdd5e3; margin:0; line-height:1.6;">Drop <code style="color:#fbbf24;">Juno Agent.json</code> into Langflow, swap the placeholder retriever with your M3 KB, and run the loop end-to-end.</p>
      </div>
    </div>

    <div style="text-align:center; margin-top:22px;">
      <a class="tool-btn" href="{langflow_url}" target="_blank" rel="noopener">Open the walkthrough &uarr;</a>
      <div style="font-size:12px; color:#8899bb; margin-top:6px;">Captures all six steps and exports screenshots into <code>05-agentic-workflows/langflow-screenshots/</code>.</div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build_module_5():
    """Build (instructor_sections, share_sections) for Module 5."""
    sections_inst, sections_share = [], []
    add = _add_builder(sections_inst, sections_share)

    # Source slide 1 - Hero
    add(hero(
        title_lead="Deploy Agentic Systems",
        title_accent="and Workflows",
        subtitle="Module 5 &middot; AI Product Management Certification",
        waypoints=[
            ("The Shift to Agentic Orchestration", "From answers to judgement. Anatomy + the autonomy spectrum."),
            ("Agentic Design Patterns", "ReAct, Planner-Executor, and the four memory types."),
            ("Managing the Agentic Handoff", "AWSpec, Control Panel, and the PM Decision Triangle."),
        ],
        out_line="You finish Module 5 with one required artefact: <code>05-agentic-workflows/awspec.md</code> &mdash; Juno&rsquo;s Agent Workflow Spec covering Actors, Pattern Plan, Memory, and Tools.",
        module_n=5,
    ))

    # Source slide 2 - Class Expectations
    add(class_expectations(),
        note="Source slide 2. Set ground rules: cameras-on for live cohort sessions, async etiquette for solo learners. Solo course &mdash; all interactions go through #ai-pm-cohort.")

    # Source slide 3 - Syllabus
    add(syllabus_visual_m5(),
        note="Source slide 3. AI Product Management Syllabus, M5 highlighted.")

    # Source slide 4 - Presentation Reminder
    add(presentation_reminder(),
        note="Source slide 4. Volunteer reminder for the next-class final-project showcase. Async cohort: post repo URL in #ai-pm-cohort by Friday for written feedback.")

    # Source slide 5 - Agenda
    add(agenda_5(),
        note="Source slide 5. Three numbered sections + an optional post-class Langflow lab. One in-class solo lab anchors the day.")

    # ----- Section 01 -----
    add(section_divider("01", "The Shift to Agentic Orchestration"),
        note="Section 1 &mdash; from answers to judgement. The dynamic between user and product changes when the system gains judgement.")

    add(evolution_of_value(),
        note="Source slide 7. Chatbot &rarr; Workflows &rarr; Agents. The PM job shifts from spec'ing outputs to spec'ing rules of action.")

    add(what_is_an_agent(),
        note="Source slide 8. Definition + the three traits (Proactive / Task-Oriented / Integrated). If a system has all three, it's an agent &mdash; otherwise it's a tool or assistant.")

    add(agent_anatomy(),
        note="Source slide 9. The Brain (LLM) + Reasoning Engine + Strategy Layer + Action Layer. PM owns Strategy and Action; the Brain ships with the model.")

    add(agent_spectrum(),
        note="Source slide 10. Four levels (Reactive &rarr; Function-Calling &rarr; Semi-Autonomous &rarr; Fully Autonomous). PM accountability rises with autonomy.")

    add(real_world_agents(),
        note="Source slide 11. Real-world examples refreshed with the most current names (J&amp;J, Uber/Klarna, Stripe, Shopify Sidekick, Cursor/Devin). Same structural pattern: bounded scope, explicit tools, human checkpoints.")

    # ----- Section 02 -----
    add(section_divider("02", "Agentic Design Patterns"),
        note="Section 2 &mdash; pick the wiring before you write the prompt. Pattern is spec.")

    add(why_patterns_matter(),
        note="Source slide 13. Patterns provide a common vocabulary + enforce a reasoning structure. They prevent orchestration-gap failures (drift, infinite loops).")

    add(react_pattern(),
        note="Source slide 14. ReAct pattern &mdash; Reason &rarr; Act &rarr; Observe loop. Best for bounded sequential tasks with feedback loops. Default pattern for most PM use cases.")

    add(planner_executor_pattern(),
        note="Source slide 15. Planner-Executor &mdash; one planner agent decomposes; one or many executor agents run. Best for multi-step tasks with parallelism.")

    add(types_of_memory(),
        note="Source slide 16. Four memory types: Episodic, Semantic, Working/Contextual, External Tools. PM rule: spec each one explicitly &mdash; including the no's.")

    # 5-min break (source slide 17)
    add(break_section(), note="Source slide 17. 5-minute break.")

    # Cameras on reminder (source slide 18)
    add(cameras_on(), note="Source slide 18. Cameras-on reminder for live cohort.")

    # ----- Section 03 -----
    add(section_divider("03", "Managing the Agentic Handoff"),
        note="Section 3 &mdash; the PM job: define the rules of engagement. AWSpec, Control Panel, Decision Triangle.")

    add(awspec_blueprint(),
        note="Source slide 20. The AWSpec is the technical bridge. Four sections: Actors, Pattern Plan, Memory, Tools. This is the M5 deliverable.")

    # Source slide 21 - Lab (originally a group breakout, converted to solo)
    add(applied_work(
            title="Write Juno&rsquo;s AWSpec",
            goal="Write the autonomous system logic that lets Juno move beyond static screens into a functional agent &mdash; mapping who is in the loop, the reasoning pattern, what persists, and the tools it can call.",
            body_html=JUNO_AWSPEC_LAB_BODY,
            repo_path="juno-pm/05-agentic-workflows/awspec.md",
            timer_min=30,
            tool_url="../Modules/M5%20-%20Agent%20Workflow%20Spec%20Builder.html",
            tool_desc="The 4-pillar walkthrough as forms (Actors, Pattern Plan, Memory, Tools). Pre-loaded with the Juno scenario. Live diagram + visualize prompt. Exports straight to <code>05-agentic-workflows/awspec.md</code>.",
        ),
        note="Solo lab. Originally a group exercise &mdash; converted to individual work. Learners use the M5 - Agent Workflow Spec Builder tool. Output committed to 05-agentic-workflows/awspec.md.")

    add(orchestration_gap(),
        note="Source slide 22. Four common failure modes &mdash; Silent Failures, Reasoning Drift, Infinite Loops, Latency Tax. Each fails in a predictable shape; spec defences for each.")

    add(control_panel(),
        note="Source slide 23. PM's Agent Control Panel: Stop Conditions, Tool Outputs, Confidence Thresholds, North Star instructions. Four levers PM specifies; engineering implements.")

    add(rules_of_engagement(),
        note="Source slide 24. Four rules of engagement: Agency Permission, Access Control, Fallback Protocols, Checkpoints. The PM contract for risk per axis.")

    add(decision_triangle(),
        note="Source slide 25. The PM Decision Triangle: Latency, Cost, Accuracy. Pick two to optimise &mdash; the third pays the bill. Name the corner you're sacrificing in the AWSpec.")

    # Source slide 26 - Key Takeaways
    add(takeaways(
            "Deploy Agentic Systems and Workflows",
            [
                ("From manual prompting to governing agents.",
                 "PMs shift from prompt craft to defining the rules under which an agent exercises judgement on real-time context."),
                ("Agent anatomy = strategy + action layers.",
                 "The reasoning engine and strategy layer deconstruct goals into multi-step plans. PMs oversee the underwater wiring."),
                ("Patterns replace if-then rules.",
                 "ReAct, Planner-Executor, and friends provide scalable, resilient reasoning. Pick the lowest-cost pattern that delivers."),
                ("PMs define the rules of engagement.",
                 "Stop conditions, access boundaries, and human-in-the-loop checkpoints. The AWSpec is the contract."),
            ],
        ),
        note="Source slide 26. Recap of the four big moves of M5.")

    # Source slide 27 - Extra Practice + Next Session
    add(extra_practice(
            [
                ("Try Building the Juno Agent in Langflow", "Optional &middot; post-class",
                 "Return to the exercise guide and build Juno&rsquo;s workflow yourself in Langflow. Import the starter JSON, plug in an OpenAI key, and run it on a sample P0 thread."),
                ("Architect a Reasoning Pattern to Solve Drift", "On a current AI system",
                 "Select a workflow where AI suffers from reasoning drift or silent failures. Design a new technical requirement using ReAct or Planner-Executor + a North Star + stop conditions."),
            ],
            "<strong>Next session: Module 6</strong> &mdash; <em>Measure AI Quality with Evals and Guardrails</em>. Build robust eval sets and safety guardrails to mitigate risks and ensure production-grade performance.",
        ),
        note="Source slide 27. Extra Practice + next-session preview combined per the source.")

    # Source slide 28 - Bonus Resources & Templates
    add(m5_resources_templates(),
        note="Source slide 28. Bonus resources: AWSpec Builder, Agent Control Panel, optional Langflow walkthrough, repo template.")

    # Source slide 29 - Q&A
    add(qa_section(),
        note="Source slide 29. Async-only Q&A. Park unresolved questions in #ai-pm-cohort. Instructor responds in-thread within ~5 days.")

    # Source slide 30 - Optional Post-Class title
    add(optional_post_class_title_5(),
        note="Source slide 30. Title card for the optional post-class Langflow lab. Not required for course completion.")

    # Source slide 31 - Optional Post-Class outcome
    add(optional_post_class_outcome_5(),
        note="Source slide 31. Outcome + link to the Langflow walkthrough. Two paths: rebuild from scratch or import Juno Agent.json.")

    return sections_inst, sections_share
