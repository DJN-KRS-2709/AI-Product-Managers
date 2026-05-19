"""Module 4 - Design AI-Native User Experiences.

Mirrors m1_v2 / m2_v2 / m3_v2 structure:
- Reuses shared helpers from gen_module_decks
- Reuses class_expectations / cameras_on / section_divider from m1_v2
- Defines M4-specific visual helpers
- Exposes build_module_4() returning (sections_inst, sections_share)

Voice: solo only. The original "Breakout Group Exercise: Architect Juno's
User Flow" is converted to an Individual Exercise. The optional
post-class Lovable lab (Reimagine Juno as AI-Native Copilot) keeps its
optional / extra-credit framing. No thank-you slide.
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
# Syllabus visual + agenda
# ---------------------------------------------------------------------------

def syllabus_visual_m4() -> str:
    """6-card syllabus, M4 highlighted, M1-M3 marked done."""
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
         "current"),
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
    <div class="subtitle">Six modules. M1&ndash;M3 are committed. Today: the surface that wraps the engine.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1040px; margin:24px auto 0;">
      {''.join(cells)}
    </div>
  </div>
</section>
"""


def agenda_4_m4() -> str:
    """M4 agenda - four numbered sections + optional post-class lab."""
    items = [
        ("01", "Intent-Driven AI Design Systems",
         "Why AI-Native UX is a different game from layering AI on legacy interfaces.", "#3b82f6"),
        ("02", "Designing Invisible UI for AI-Native Outcomes",
         "Three patterns + three placement maneuvers. Match value to surface.", "#fbbf24"),
        ("03", "How to Architect an AI User Flow",
         "The Iceberg model. Map what the system thinks, not just what the user clicks.", "#79c0ff"),
        ("04", "The PM&rsquo;s Playbook for Closing AI Trust Gaps",
         "Black-box, hallucination, control. Three failures and how the UI closes them.", "#34d399"),
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
    <div class="subtitle">One in-class solo lab anchors the day. One optional post-class Lovable build.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; max-width:980px; margin:22px auto 0;">
      {cards}
    </div>
    <p style="font-size:11.5px; color:#bcb1ff; max-width:780px; margin:14px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">Bonus &middot; Post-class:</strong> Reimagine Juno as an AI-Native Copilot in Lovable. Optional &mdash; not required for completion.
    </p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 01 - Intent-Driven AI Design Systems
# ---------------------------------------------------------------------------

def clunky_aiux_qa() -> str:
    """Source slide 6 - Instructor-Led Q&A. Same three discussion questions
    from the source. Speaker notes (`add(...)` `note=`) carry the
    instructor cues. Async cohort learners can post their answer in
    `#ai-pm-cohort`."""
    return """<section data-title="Your Experience With Clunky AI-UX">
  <div class="inner">
    <div class="demo-tag tag-debrief">Instructor-Led Q&amp;A &middot; 5 min</div>
    <h2>Your Experience With &ldquo;Clunky&rdquo; AI-UX</h2>
    <div class="subtitle">To get you started thinking about how you might reimagine the AI-UX of your own products and experiences, share your perspective on the questions below.</div>

    <ol style="max-width:820px; margin:22px auto 0; padding:0 0 0 22px; text-align:left; color:#cdd5e3; font-size:14.5px; line-height:1.6;">
      <li style="margin-bottom:10px;">What&rsquo;s a product you&rsquo;ve tried where AI <em>technically</em> works, but the experience feels wrong, annoying, or pointless?</li>
      <li style="margin-bottom:10px;">On the flip side, where have you seen AI change <em>how</em> you interact with a product, not just <em>what</em> it can do?</li>
      <li>Did it remove steps? Did it change who is &lsquo;in control&rsquo;? Did it make the product feel more proactive?</li>
    </ol>

    <p style="font-size:13px; color:#8899bb; max-width:780px; margin:18px auto 0; text-align:center;">
      Feel free to unmute and share, or post your thoughts in the chat. Async learners: post in <code style="font-size:0.92em; color:#79c0ff;">#ai-pm-cohort</code>.
    </p>
  </div>
</section>
"""


def ai_ux_implementations() -> str:
    """Traditional AI-UX vs AI-Native UX - VS comparison with Bing/Perplexity."""
    return """<section data-title="AI-UX Implementations">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Frame</div>
    <h2>Two ways to ship AI in a product</h2>
    <div class="subtitle">Both are valid. One bolts AI <em>onto</em> a workflow. The other <em>is</em> the workflow.</div>

    <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:0; max-width:1080px; margin:18px auto 0; align-items:stretch;">

      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.10); border-radius:14px; overflow:hidden; text-align:left;">
        <div style="padding:14px 18px; background:rgba(255,255,255,0.04);">
          <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase;">Traditional AI-UX</div>
          <div style="font-family:'Poppins',sans-serif; font-size:17px; font-weight:800; color:#fff; margin-top:4px;">AI as a feature on a static UI</div>
        </div>
        <div style="padding:11px 18px; border-top:1px solid rgba(255,255,255,0.06);">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Approach</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;">AI features <em>retroactively layered</em> on a deterministic workflow.</p>
        </div>
        <div style="padding:11px 18px; border-top:1px solid rgba(255,255,255,0.06);">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Interaction</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;">User-driven &mdash; the user must manually trigger AI actions.</p>
        </div>
        <div style="padding:11px 18px; border-top:1px solid rgba(255,255,255,0.06);">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Outcome</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;">Incremental efficiency without disrupting familiar habits.</p>
        </div>
        <div style="padding:11px 18px; background:rgba(255,255,255,0.04); border-top:1px solid rgba(255,255,255,0.06);">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Example</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;"><strong style="color:#fff;">Google Search &middot; AI Overviews</strong> &mdash; an AI summary block sits above the same 10-blue-link results page.</p>
        </div>
      </div>

      <div style="display:flex; align-items:center; justify-content:center; padding:0 14px; min-width:54px;">
        <div style="font-family:'Poppins',sans-serif; font-size:32px; font-weight:900; color:#475569; letter-spacing:0.05em; transform:rotate(-2deg);">VS</div>
      </div>

      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.3); border-radius:14px; overflow:hidden; text-align:left;">
        <div style="padding:14px 18px; background:rgba(96,165,250,0.10);">
          <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase;">AI-Native UX</div>
          <div style="font-family:'Poppins',sans-serif; font-size:17px; font-weight:800; color:#fff; margin-top:4px;">The model <em>is</em> the workflow</div>
        </div>
        <div style="padding:11px 18px; border-top:1px solid rgba(96,165,250,0.18);">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Approach</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;">Built from the ground up &mdash; the model is the engine, not a feature.</p>
        </div>
        <div style="padding:11px 18px; border-top:1px solid rgba(96,165,250,0.18);">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Interaction</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;">Intent-driven &mdash; the interface evolves to surface only what&rsquo;s needed.</p>
        </div>
        <div style="padding:11px 18px; border-top:1px solid rgba(96,165,250,0.18);">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Outcome</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;">Seamless, personalized experiences. Minimal manual navigation.</p>
        </div>
        <div style="padding:11px 18px; background:rgba(96,165,250,0.10); border-top:1px solid rgba(96,165,250,0.18);">
          <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Example</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5;"><strong style="color:#fff;">Perplexity</strong> &mdash; AI generates the answer; the list of links is gone.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""


def why_ai_native_matters_4() -> str:
    """4 reasons why AI-Native UX matters."""
    items = [
        ("&#x1F4C9;", "Lowered Interaction Costs",
         "Move users from manual <em>searching</em> to <em>reviewing and deciding</em>.",
         "#3b82f6"),
        ("&#x1F9E0;", "Shifted Cognitive Load",
         "Replace repetitive instructional labor with synthesis &mdash; freeing high-level judgment.",
         "#79c0ff"),
        ("&#x1F501;", "Increased System Resilience",
         "Interface adapts to real intents instead of relying on rigid menus.",
         "#fbbf24"),
        ("&#x1F3AF;", "Contextual Relevance",
         "Surface only the most relevant information and actions exactly when needed.",
         "#34d399"),
    ]
    cards = "".join(
        f'<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:12px; padding:14px 16px; text-align:left; position:relative; overflow:hidden;">'
        f'<div style="position:absolute; top:0; left:0; right:0; height:3px; background:{col};"></div>'
        f'<div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">'
        f'<div style="font-size:18px;">{emoji}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:13px; font-weight:800; color:#fff;">{title}</div>'
        f'</div>'
        f'<p style="font-size:12px; color:#cdd5e3; line-height:1.5; margin:0;">{desc}</p>'
        f'</div>'
        for emoji, title, desc, col in items
    )
    return f"""<section data-title="Why AI-Native UX Matters">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>Why AI-Native UX matters</h2>
    <div class="subtitle">It&rsquo;s not about better buttons. It&rsquo;s about uncapping user potential by automating the manual execution that limits their impact.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; max-width:1080px; margin:22px auto 0;">
      {cards}
    </div>
    <p style="font-size:12.5px; color:#cdd5e3; max-width:780px; margin:18px auto 0; padding:10px 18px; background:rgba(217,142,34,0.06); border-left:3px solid #fbbf24; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">The shift:</strong> users move from <em>builder</em> to <em>strategic reviewer</em>. The product scales their judgment, not their typing.
    </p>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 02 - Designing Invisible UI for AI-Native Outcomes
# ---------------------------------------------------------------------------

def invisible_by_design_3() -> str:
    """3 patterns for invisible UI."""
    patterns = [
        ("&#x1F50C;", "Use environmental signals to trigger actions",
         "Wake up on file uploads, meeting endings, page loads. Stop waiting for a manual prompt.",
         "Glean", "Indexes activity in the background &mdash; analysis is done before you open the app.",
         "#3b82f6"),
        ("&#x1F4A1;", "Leverage intent prediction to surface micro-UIs",
         "Hide advanced controls until the system predicts the moment a user needs them.",
         "Adobe Firefly", "&ldquo;Generative Fill&rdquo; bar appears only after you select an area in Photoshop.",
         "#fbbf24"),
        ("&#x1F500;", "Automate data flow between workflows",
         "Push AI outputs directly into the next stage. Remove the friction of copy-paste.",
         "Salesforce", "AI extracts a lead from a transcript and auto-maps to CRM fields + drafts the follow-up.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:8px;">
  <div style="display:flex; align-items:center; gap:8px;">
    <div style="font-size:20px;">{emoji}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:13.5px; font-weight:800; color:#fff; line-height:1.3;">{title}</div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; line-height:1.5; margin:0;">{desc}</p>
  <div style="background:rgba(0,0,0,0.28); border-radius:8px; padding:8px 11px; margin-top:auto;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:{col}; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:3px;">&#x2728; {ex_label}</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.45;">{ex_desc}</p>
  </div>
</div>"""
        for emoji, title, desc, ex_label, ex_desc, col in patterns
    )
    return f"""<section data-title="Invisible by Design">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>Invisible by design &mdash; three patterns</h2>
    <div class="subtitle">Invisible isn&rsquo;t about the AI disappearing. It&rsquo;s about the <em>labor</em> disappearing.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1080px; margin:22px auto 0; align-items:stretch;">
      {cards}
    </div>
  </div>
</section>
"""


def ai_placement_3() -> str:
    """3 placement maneuvers: Inline, Floating, Full-Page."""
    placements = [
        ("01", "Inline &amp; Embedded",
         "AI capabilities placed directly in the text, code, or data the user is touching. Keeps them in flow.",
         "Google Docs", "&ldquo;Help me write&rdquo; button moves with the cursor.",
         "#3b82f6"),
        ("02", "Floating &amp; Contextual",
         "Dynamic toolbars or hover menus that follow user selection. Tools appear only when contextually relevant.",
         "Figma AI", "Floating pill appears at the bottom only when layers are selected.",
         "#fbbf24"),
        ("03", "Full-Page Canvas &amp; Hubs",
         "Dedicated views for high-complexity AI outputs. Roadmaps, decks, dashboards. Space to review V1 drafts.",
         "Gamma / Canva Magic", "Generated decks open into a full-screen canvas for validation.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:8px;">
  <div style="display:flex; align-items:baseline; gap:10px;">
    <div style="font-family:'Poppins',sans-serif; font-size:30px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:#fff; line-height:1.3;">{title}</div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; line-height:1.5; margin:0;">{desc}</p>
  <div style="background:rgba(0,0,0,0.28); border-radius:8px; padding:8px 11px; margin-top:auto;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:{col}; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:3px;">&#x2728; {ex_label}</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.45;">{ex_desc}</p>
  </div>
</div>"""
        for n, title, desc, ex_label, ex_desc, col in placements
    )
    return f"""<section data-title="AI Interaction Placement">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>Choosing the AI interaction placement</h2>
    <div class="subtitle">Once you know the AI&rsquo;s job, pick the real estate it deserves on the screen.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1080px; margin:22px auto 0; align-items:stretch;">
      {cards}
    </div>
  </div>
</section>
"""


def spot_the_friction_qa() -> str:
    """Source slide 12 - Instructor-Led Q&A. Source timer = 10 minutes.
    Speaker notes (passed via `note=` on the `add(...)` call) carry the
    answer paths and instructor cues."""
    return """<section data-title="Spot the Friction">
  <div class="inner">
    <div class="demo-tag tag-debrief">Instructor-Led Q&amp;A &middot; 10 min</div>
    <h2>Spot the Friction</h2>
    <div class="subtitle">To make these AI-native principles tangible, let&rsquo;s analyze how they apply to a real-world product scenario.</div>

    <div style="max-width:880px; margin:18px auto 0; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.10); border-radius:14px; padding:16px 22px; text-align:left;">
      <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:6px;">Scenario</div>
      <p style="font-size:14px; color:#fff; line-height:1.55; margin:0;">A recruiter opens a candidate&rsquo;s profile. A &ldquo;sidecar&rdquo; chat box pops up and says: <em>&ldquo;I have analyzed this profile. Ask me anything or tell me to write an outreach email.&rdquo;</em></p>
      <p style="font-size:13px; color:#cdd5e3; line-height:1.55; margin:8px 0 0;">Why is this <em>not</em> an AI-native &lsquo;invisible&rsquo; design, and what would you change to make it effortless?</p>
    </div>

    <p style="font-size:12.5px; color:#8899bb; max-width:780px; margin:14px auto 0; text-align:center;">
      Look at the scenario and identify why it fails to deliver an effortless experience. Be ready to share your reasoning.
    </p>
  </div>
</section>
"""


def value_to_ux_4() -> str:
    """Mapping AI value props to placement maneuvers."""
    rows = [
        ("Automation", "Full-Page Canvas",
         "Skip the manual work. Show a finished draft in a dedicated space before the user asks.",
         "#34d399"),
        ("Augmentation", "Inline &amp; Embedded",
         "Speed things up. Give a starting point right where the cursor is sitting.",
         "#3b82f6"),
        ("Insights", "Floating &amp; Contextual",
         "Explain messy data. Pop up an &ldquo;aha!&rdquo; moment only when the user selects something.",
         "#fbbf24"),
        ("Personalization", "Floating &amp; Contextual",
         "Keep the user focused. Change the interface to show only the tools the AI predicts they need.",
         "#bcb1ff"),
    ]
    cells = "".join(
        f"""<div style="display:grid; grid-template-columns:1.1fr 1.1fr 2fr; gap:14px; padding:11px 16px; align-items:center; border-bottom:1px solid rgba(255,255,255,0.06);">
  <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:{col};">{value}</div>
  <div style="font-family:'IBM Plex Mono',monospace; font-size:12px; color:#cdd5e3; padding:5px 10px; background:rgba(0,0,0,0.25); border:1px solid rgba(255,255,255,0.06); border-radius:6px;">{maneuver}</div>
  <p style="font-size:12px; color:#cdd5e3; margin:0; line-height:1.45;">{outcome}</p>
</div>"""
        for value, maneuver, outcome, col in rows
    )
    return f"""<section data-title="Mapping Value to UX Treatment">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>Mapping value to UX treatment</h2>
    <div class="subtitle">Match the AI value prop you picked in M2 to the right placement maneuver.</div>
    <div style="max-width:1040px; margin:22px auto 0; background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.10); border-radius:14px; overflow:hidden;">
      <div style="display:grid; grid-template-columns:1.1fr 1.1fr 2fr; gap:14px; padding:10px 16px; background:rgba(255,255,255,0.04); font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase;">
        <div>If your value is</div>
        <div>Use this UX maneuver</div>
        <div>To achieve this outcome</div>
      </div>
      {cells}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Section 03 - How to Architect an AI User Flow
# ---------------------------------------------------------------------------

def architecting_iceberg() -> str:
    """Source slide 15 - Architecting the AI 'Iceberg'.

    Two-column layout. Left: lead + Traditional/AI-native contrast.
    Right: vertically stacked panel with the source 'Top Tip' card on
    top, then the iceberg illustration below. Iceberg has a sharp peak
    above water and a much larger underwater body with a constellation
    network pattern, mirroring the source slide visual."""
    return """<section data-title="Architecting the AI Iceberg">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Mental Model</div>
    <h2>Architecting the AI &ldquo;Iceberg&rdquo;</h2>

    <div style="display:grid; grid-template-columns:1.2fr 0.95fr; gap:32px; max-width:1080px; margin:18px auto 0; align-items:stretch;">

      <!-- LEFT - source text content -->
      <div style="text-align:left; display:flex; flex-direction:column; justify-content:center;">
        <p style="font-size:15px; color:#fff; line-height:1.55; margin:0 0 18px; font-weight:600;">
          Don&rsquo;t just map what the user <em>does</em>; map what the system <em>thinks</em>. The most powerful AI experiences are often the simplest UIs supported by the most complex background logic.
        </p>

        <div style="display:flex; flex-direction:column; gap:10px;">
          <div style="display:flex; gap:12px; align-items:flex-start; background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.10); border-radius:10px; padding:11px 14px;">
            <div style="flex-shrink:0; width:38px; height:38px; border-radius:8px; background:rgba(96,165,250,0.18); border:1px solid rgba(96,165,250,0.4); display:flex; align-items:center; justify-content:center;">
              <span style="font-size:18px;">&#x1F5B1;&#xFE0F;</span>
            </div>
            <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5; padding-top:5px;"><strong style="color:#fff;">Traditional mapping</strong> focuses on user clicks, screen navigation, and manual inputs.</p>
          </div>

          <div style="display:flex; gap:12px; align-items:flex-start; background:rgba(124,140,255,0.06); border:1px solid rgba(124,140,255,0.30); border-radius:10px; padding:11px 14px;">
            <div style="flex-shrink:0; width:38px; height:38px; border-radius:8px; background:rgba(124,140,255,0.20); border:1px solid rgba(124,140,255,0.5); display:flex; align-items:center; justify-content:center;">
              <span style="font-size:18px;">&#x1F9E0;</span>
            </div>
            <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.5; padding-top:5px;"><strong style="color:#fff;">AI-native mapping</strong> focuses on the background orchestration happening between a user&rsquo;s intent and the final output.</p>
          </div>
        </div>
      </div>

      <!-- RIGHT - Top Tip + Iceberg, stacked vertically inside one panel -->
      <div style="background:linear-gradient(180deg, #07162C 0%, #050d1f 100%); border:1px solid rgba(255,255,255,0.10); border-radius:14px; padding:14px 14px 0; display:flex; flex-direction:column; gap:10px; overflow:hidden;">

        <!-- Top Tip card (sits at top of panel, never overlaps iceberg) -->
        <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(251,191,36,0.40); border-radius:11px; padding:10px 14px;">
          <div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">
            <div style="width:22px; height:22px; border-radius:50%; background:rgba(251,191,36,0.18); border:1px solid rgba(251,191,36,0.5); display:flex; align-items:center; justify-content:center;">
              <span style="font-size:12px;">&#x1F4A1;</span>
            </div>
            <span style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#fbbf24; letter-spacing:0.16em; text-transform:uppercase;">Top Tip</span>
          </div>
          <p style="font-size:11.5px; color:#fff; line-height:1.5; margin:0; font-weight:600;">
            You must decide what remains <em style="color:#79c0ff;">&ldquo;Invisible&rdquo;</em> to keep the experience effortless, and what needs to be <em style="color:#fbbf24;">&ldquo;Visible&rdquo;</em> to build user trust.
          </p>
        </div>

        <!-- Iceberg SVG -->
        <svg viewBox="0 0 360 380" preserveAspectRatio="xMidYMax meet" style="width:100%; height:auto; flex:1; min-height:0; display:block;" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="ib-sky" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#0a1f44" />
              <stop offset="100%" stop-color="#15325f" />
            </linearGradient>
            <linearGradient id="ib-water" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#0d2b5e" />
              <stop offset="55%" stop-color="#082046" />
              <stop offset="100%" stop-color="#03102a" />
            </linearGradient>
            <linearGradient id="ib-peak" x1="0.2" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#ffffff" />
              <stop offset="40%" stop-color="#cce0fa" />
              <stop offset="100%" stop-color="#7da4d8" />
            </linearGradient>
            <linearGradient id="ib-below" x1="0.3" y1="0" x2="0.7" y2="1">
              <stop offset="0%" stop-color="#3d6fb8" stop-opacity="0.95" />
              <stop offset="55%" stop-color="#1f4789" stop-opacity="0.85" />
              <stop offset="100%" stop-color="#0e2858" stop-opacity="0.80" />
            </linearGradient>
            <radialGradient id="ib-glow" cx="0.5" cy="0.85" r="0.6">
              <stop offset="0%" stop-color="#79c0ff" stop-opacity="0.22" />
              <stop offset="100%" stop-color="#79c0ff" stop-opacity="0" />
            </radialGradient>
          </defs>

          <!-- Sky -->
          <rect x="0" y="0" width="360" height="135" fill="url(#ib-sky)" />
          <!-- Water -->
          <rect x="0" y="135" width="360" height="245" fill="url(#ib-water)" />
          <!-- Soft underwater glow behind iceberg -->
          <rect x="0" y="135" width="360" height="245" fill="url(#ib-glow)" />

          <!-- Constellation network in the water (data/AI complexity) -->
          <g stroke="rgba(121,192,255,0.32)" stroke-width="0.6" fill="none">
            <line x1="48" y1="195" x2="92" y2="218" />
            <line x1="92" y1="218" x2="62" y2="262" />
            <line x1="62" y1="262" x2="118" y2="295" />
            <line x1="118" y1="295" x2="78" y2="338" />
            <line x1="92" y1="218" x2="146" y2="206" />
            <line x1="146" y1="206" x2="200" y2="232" />
            <line x1="200" y1="232" x2="262" y2="206" />
            <line x1="262" y1="206" x2="312" y2="238" />
            <line x1="312" y1="238" x2="280" y2="295" />
            <line x1="280" y1="295" x2="232" y2="328" />
            <line x1="232" y1="328" x2="170" y2="345" />
            <line x1="170" y1="345" x2="118" y2="295" />
            <line x1="200" y1="232" x2="170" y2="278" />
            <line x1="170" y1="278" x2="232" y2="284" />
            <line x1="232" y1="284" x2="280" y2="295" />
            <line x1="262" y1="206" x2="312" y2="178" />
            <line x1="48" y1="195" x2="22" y2="240" />
            <line x1="22" y1="240" x2="42" y2="295" />
            <line x1="42" y1="295" x2="78" y2="338" />
            <line x1="312" y1="178" x2="338" y2="220" />
            <line x1="338" y1="220" x2="320" y2="285" />
            <line x1="320" y1="285" x2="282" y2="338" />
          </g>
          <g fill="#79c0ff">
            <circle cx="48" cy="195" r="1.6" opacity="0.85" />
            <circle cx="92" cy="218" r="1.4" opacity="0.75" />
            <circle cx="62" cy="262" r="1.6" opacity="0.85" />
            <circle cx="118" cy="295" r="1.5" opacity="0.80" />
            <circle cx="78" cy="338" r="1.6" opacity="0.85" />
            <circle cx="146" cy="206" r="1.3" opacity="0.70" />
            <circle cx="200" cy="232" r="1.6" opacity="0.85" />
            <circle cx="262" cy="206" r="1.5" opacity="0.80" />
            <circle cx="312" cy="238" r="1.6" opacity="0.85" />
            <circle cx="280" cy="295" r="1.4" opacity="0.75" />
            <circle cx="232" cy="328" r="1.6" opacity="0.85" />
            <circle cx="170" cy="345" r="1.5" opacity="0.80" />
            <circle cx="170" cy="278" r="1.4" opacity="0.75" />
            <circle cx="232" cy="284" r="1.4" opacity="0.75" />
            <circle cx="22" cy="240" r="1.3" opacity="0.65" />
            <circle cx="42" cy="295" r="1.5" opacity="0.80" />
            <circle cx="312" cy="178" r="1.4" opacity="0.75" />
            <circle cx="338" cy="220" r="1.5" opacity="0.80" />
            <circle cx="320" cy="285" r="1.6" opacity="0.85" />
            <circle cx="282" cy="338" r="1.4" opacity="0.75" />
          </g>

          <!-- Iceberg peak (above water) - tall, sharp, asymmetric like source -->
          <polygon points="178,28 158,135 234,135 220,82 200,55 192,42" fill="url(#ib-peak)" />
          <!-- Right-side highlight facet -->
          <polygon points="192,42 200,55 220,82 210,135 234,135" fill="#ffffff" opacity="0.45" />
          <!-- Subtle wireframe lines on the peak -->
          <g stroke="rgba(255,255,255,0.55)" stroke-width="0.5" fill="none" opacity="0.55">
            <line x1="178" y1="28" x2="158" y2="135" />
            <line x1="178" y1="28" x2="234" y2="135" />
            <line x1="200" y1="55" x2="158" y2="135" />
            <line x1="200" y1="55" x2="234" y2="135" />
            <line x1="220" y1="82" x2="178" y2="135" />
          </g>

          <!-- Iceberg body (underwater) - much larger than the peak -->
          <polygon points="158,135 234,135 305,178 332,238 312,302 268,346 192,365 110,358 56,310 38,242 60,182" fill="url(#ib-below)" />
          <!-- Underwater facet highlights (subtle) -->
          <polygon points="234,135 305,178 268,200" fill="#ffffff" opacity="0.13" />
          <polygon points="158,135 60,182 110,210" fill="#ffffff" opacity="0.08" />
          <polygon points="305,178 332,238 290,225" fill="#ffffff" opacity="0.06" />
          <!-- Underwater shadow -->
          <polygon points="192,365 268,346 240,310" fill="#000000" opacity="0.22" />
          <polygon points="38,242 56,310 90,275" fill="#000000" opacity="0.15" />

          <!-- Wireframe overlay on iceberg body for depth -->
          <g stroke="rgba(255,255,255,0.12)" stroke-width="0.5" fill="none">
            <line x1="158" y1="135" x2="332" y2="238" />
            <line x1="234" y1="135" x2="38" y2="242" />
            <line x1="158" y1="135" x2="268" y2="346" />
            <line x1="234" y1="135" x2="110" y2="358" />
            <line x1="305" y1="178" x2="56" y2="310" />
            <line x1="60" y1="182" x2="312" y2="302" />
          </g>

          <!-- Water surface line -->
          <line x1="0" y1="135" x2="360" y2="135" stroke="#79c0ff" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.45" />
          <path d="M 0 132 Q 90 130 180 132 T 360 132" stroke="rgba(255,255,255,0.22)" stroke-width="0.6" fill="none" />
          <path d="M 0 139 Q 70 141 140 138 T 360 139" stroke="rgba(255,255,255,0.10)" stroke-width="0.6" fill="none" />

          <!-- Layer labels -->
          <text x="345" y="125" fill="#79c0ff" font-family="Poppins, sans-serif" font-size="9" font-weight="900" letter-spacing="2.5" text-anchor="end" opacity="0.75">SURFACE</text>
          <text x="345" y="370" fill="#bcb1ff" font-family="Poppins, sans-serif" font-size="9" font-weight="900" letter-spacing="2.5" text-anchor="end" opacity="0.65">UNDERWATER</text>
        </svg>
      </div>
    </div>

    <p style="font-size:12px; color:#cdd5e3; max-width:1040px; margin:14px auto 0; padding:9px 16px; background:rgba(217,142,34,0.06); border-left:3px solid #fbbf24; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">PM lever:</strong> show too much of the underwater logic &rarr; cluttered UX. Show too little &rarr; lose user trust. You&rsquo;re designing the balance between <em>invisible effortlessness</em> and <em>visible verification</em>.
    </p>
  </div>
</section>
"""


def four_pillars() -> str:
    """The 4 architecture pillars: Trigger, Processing, Presentation, Feedback Loop."""
    pillars = [
        ("01", "The Trigger",
         "Identify the earliest possible <em>intent signal</em>.",
         "&#x1F4E5; Meeting recording ends, PDF uploaded, page loads.",
         "An &lsquo;AI summary in progress&rsquo; notification appears instantly &mdash; before the user clicks anything.",
         "#3b82f6"),
        ("02", "The Processing State",
         "Use the wait to <em>build trust</em>, not show a spinner.",
         "&#x1F501; Routes the request, fetches data, reasons, drafts an output.",
         "Breadcrumbs: &ldquo;Scanning policy docs&hellip;&rdquo; &mdash; turns latency into transparency.",
         "#79c0ff"),
        ("03", "The Presentation",
         "Pick the maneuver that fits the <em>value</em>.",
         "&#x1F3AF; Inline draft, floating overlay, or full-page canvas.",
         "&ldquo;V1 outreach email&rdquo; renders directly in the message field.",
         "#fbbf24"),
        ("04", "The Feedback Loop",
         "Every edit, undo, or accept is a <em>training signal</em>.",
         "&#x1F501; Logs corrections back into the model state.",
         "&ldquo;Don&rsquo;t use this tone again&rdquo; updates the user&rsquo;s tone profile.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:7px;">
  <div style="display:flex; align-items:baseline; gap:10px;">
    <div style="font-family:'Poppins',sans-serif; font-size:26px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:#fff; line-height:1.3;">{title}</div>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; line-height:1.45; margin:0;">{logic_summary}</p>
  <div style="background:rgba(124,140,255,0.06); border:1px solid rgba(124,140,255,0.25); border-radius:7px; padding:6px 10px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9px; font-weight:900; color:#bcb1ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:2px;">Underwater</div>
    <p style="font-size:10.5px; color:#cdd5e3; margin:0; line-height:1.5;">{logic_detail}</p>
  </div>
  <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:7px; padding:6px 10px; margin-top:auto;">
    <div style="font-family:'Poppins',sans-serif; font-size:9px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:2px;">Surface</div>
    <p style="font-size:10.5px; color:#cdd5e3; margin:0; line-height:1.5;">{surface}</p>
  </div>
</div>"""
        for n, title, logic_summary, logic_detail, surface, col in pillars
    )
    return f"""<section data-title="Four Architecture Pillars">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>The four architecture pillars</h2>
    <div class="subtitle">Each pillar has an <em>underwater</em> half (logic the PM specs) and a <em>surface</em> half (what the user feels).</div>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px; max-width:1080px; margin:22px auto 0; align-items:stretch;">
      {cards}
    </div>
  </div>
</section>
"""


def user_flow_legend() -> str:
    """Source slide 17 - the Builder's Legend (5 shapes mapped to 4 pillars)
    plus the 4-step process. The legend renders each shape AS ITSELF using
    inline SVG so learners see the actual vocabulary they will use to draw
    the flow in the lab + the HR Agent example next."""

    # Each row: (inline SVG of the shape, name, description, pillar tag, pillar accent)
    rows = [
        # Signal - circle - THE TRIGGER
        ("""<svg viewBox="0 0 60 50" width="60" height="50"><circle cx="30" cy="25" r="18" fill="rgba(207,229,255,0.95)" stroke="#79c0ff" stroke-width="2"/></svg>""",
         "Signal", "Entry point", "The Trigger", "#79c0ff"),
        # Hidden Logic - light-blue rectangle (large) - THE PROCESSING STATE
        ("""<svg viewBox="0 0 60 50" width="60" height="50"><rect x="6" y="9" width="48" height="32" fill="#3b82f6" stroke="#79c0ff" stroke-width="2" rx="2"/></svg>""",
         "Hidden Logic", "Major step &middot; underwater", "The Processing State", "#bcb1ff"),
        # Interaction - dark-blue square (small) - THE PRESENTATION
        ("""<svg viewBox="0 0 60 50" width="60" height="50"><rect x="18" y="13" width="24" height="24" fill="#1e3a8a" stroke="#79c0ff" stroke-width="2" rx="2"/></svg>""",
         "Interaction", "Sub-step &middot; surface maneuver", "The Presentation", "#fbbf24"),
        # Data Flow - black diamond - THE FEEDBACK LOOP (top half)
        ("""<svg viewBox="0 0 60 50" width="60" height="50"><polygon points="30,7 51,25 30,43 9,25" fill="#0a1838" stroke="#94a3b8" stroke-width="1.5"/></svg>""",
         "Data Flow", "Routing decision", "The Feedback Loop", "#34d399"),
        # Generated Output - grey parallelogram - THE FEEDBACK LOOP (bottom half)
        ("""<svg viewBox="0 0 60 50" width="60" height="50"><polygon points="14,11 54,11 46,39 6,39" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/></svg>""",
         "Generated Output", "AI result", "The Feedback Loop", "#34d399"),
    ]

    legend_rows = "".join(
        f"""<div style="display:grid; grid-template-columns:60px 1fr auto; gap:12px; align-items:center; padding:7px 10px; background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:9px;">
  <div style="display:flex; align-items:center; justify-content:center;">{shape_svg}</div>
  <div style="text-align:left;">
    <div style="font-family:'Poppins',sans-serif; font-size:12px; font-weight:800; color:#fff; line-height:1.2;">{name}</div>
    <div style="font-size:10.5px; color:#8899bb; line-height:1.3; margin-top:1px;">{desc}</div>
  </div>
  <div style="font-family:'Poppins',sans-serif; font-size:8.5px; font-weight:900; color:{pillar_col}; letter-spacing:0.13em; text-transform:uppercase; padding:4px 9px; background:{pillar_col}1f; border:1px solid {pillar_col}66; border-radius:99px; white-space:nowrap;">{pillar}</div>
</div>"""
        for shape_svg, name, desc, pillar, pillar_col in rows
    )

    steps = [
        ("Step 1", "Identify the signal", "Capture the specific event or entry point that initiates the flow.", "#3b82f6"),
        ("Step 2", "Map the hidden logic", "Define the major steps the AI takes before the user sees a result.", "#bcb1ff"),
        ("Step 3", "Design the maneuver", "Match each sub-step of the interaction to the correct UI placement.", "#fbbf24"),
        ("Step 4", "Build the kill switch", "Map data flow + output so a recovery path always exists for the user.", "#34d399"),
    ]
    steps_html = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-left:3px solid {col}; border-radius:10px; padding:10px 14px; text-align:left;">
  <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:{col}; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">{n}</div>
  <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#fff; margin-bottom:4px;">{title}</div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{desc}</p>
</div>"""
        for n, title, desc, col in steps
    )

    return f"""<section data-title="How to Architect an AI User Flow">
  <div class="inner">
    <div class="demo-tag tag-build">Framework &middot; Builder&rsquo;s Legend</div>
    <h2>How to Architect an AI User Flow</h2>
    <div class="subtitle">A small set of shapes maps to the four pillars. Use these to draw the flow in the lab next &mdash; and to read the HR Agent example coming up.</div>

    <div style="display:grid; grid-template-columns:1.25fr 1fr; gap:22px; max-width:1080px; margin:18px auto 0; align-items:start;">

      <div style="background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:14px 18px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:10px;">&#x1F9F1; Builder&rsquo;s legend &middot; shape &rarr; pillar</div>
        <div style="display:flex; flex-direction:column; gap:6px;">
          {legend_rows}
        </div>
      </div>

      <div>
        <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px; padding-left:4px;">&#x270D;&#xFE0F; Four steps to map a flow</div>
        <div style="display:flex; flex-direction:column; gap:8px;">
          {steps_html}
        </div>
      </div>
    </div>
  </div>
</section>
"""


def hr_agent_example() -> str:
    """Source slide 18 - HR Agent example flow.

    Renders the actual user flow as a 3-layer SVG diagram with the shapes
    from the legend (circle / rectangle / diamond / parallelogram) connected
    by arrows. Surface = user experience. Handshake = router. Underwater =
    AI workflow. Round-trip arrows return results back to the surface."""

    return """<section data-title="Example: HR Agent">
  <div class="inner">
    <div class="demo-tag tag-build">Case Study</div>
    <h2>Example &mdash; HR Agent flow</h2>
    <div class="subtitle">The same shapes, connected with arrows. Follow the user from Surface, through the Handshake, into Underwater &mdash; and back up.</div>

    <div style="max-width:1100px; margin:14px auto 0;">
      <svg viewBox="0 0 1100 540" preserveAspectRatio="xMidYMid meet" style="width:100%; height:auto; display:block;">
        <defs>
          <marker id="arr-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#79c0ff"/>
          </marker>
          <marker id="arr-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#fbbf24"/>
          </marker>
          <marker id="arr-mint" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#34d399"/>
          </marker>
          <linearGradient id="surface-bg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="rgba(96,165,250,0.18)"/>
            <stop offset="100%" stop-color="rgba(96,165,250,0.06)"/>
          </linearGradient>
          <linearGradient id="handshake-bg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="rgba(124,140,255,0.12)"/>
            <stop offset="100%" stop-color="rgba(124,140,255,0.04)"/>
          </linearGradient>
          <linearGradient id="underwater-bg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="rgba(7,22,44,0.55)"/>
            <stop offset="100%" stop-color="rgba(7,22,44,0.85)"/>
          </linearGradient>
        </defs>

        <!-- Layer bands -->
        <rect x="0" y="0" width="1100" height="160" fill="url(#surface-bg)" rx="14"/>
        <rect x="0" y="160" width="1100" height="180" fill="url(#handshake-bg)"/>
        <rect x="0" y="340" width="1100" height="200" fill="url(#underwater-bg)" rx="14"/>

        <!-- Layer dividers (water lines) -->
        <line x1="0" y1="160" x2="1100" y2="160" stroke="rgba(255,255,255,0.18)" stroke-width="1" stroke-dasharray="5,4"/>
        <line x1="0" y1="340" x2="1100" y2="340" stroke="rgba(255,255,255,0.18)" stroke-width="1" stroke-dasharray="5,4"/>

        <!-- Layer labels (left edge) -->
        <text x="18" y="62" fill="#79c0ff" font-family="Poppins, sans-serif" font-size="10" font-weight="900" letter-spacing="2.5">THE USER EXPERIENCE</text>
        <text x="18" y="78" fill="#cdd5e3" font-family="Poppins, sans-serif" font-size="10.5" font-weight="700" font-style="italic">(Surface Layer)</text>

        <text x="18" y="232" fill="#bcb1ff" font-family="Poppins, sans-serif" font-size="10" font-weight="900" letter-spacing="2.5">THE HANDSHAKE</text>
        <text x="18" y="248" fill="#cdd5e3" font-family="Poppins, sans-serif" font-size="10.5" font-weight="700" font-style="italic">(Connection Layer)</text>

        <text x="18" y="412" fill="#fbbf24" font-family="Poppins, sans-serif" font-size="10" font-weight="900" letter-spacing="2.5">THE AI WORKFLOW</text>
        <text x="18" y="428" fill="#cdd5e3" font-family="Poppins, sans-serif" font-size="10.5" font-weight="700" font-style="italic">(Underwater Layer)</text>

        <!-- ============ SURFACE NODES ============ -->
        <!-- Signal circle (center entry) -->
        <circle cx="540" cy="80" r="42" fill="rgba(207,229,255,0.95)" stroke="#79c0ff" stroke-width="2"/>
        <text x="540" y="74" text-anchor="middle" fill="#0a1f44" font-family="Poppins, sans-serif" font-size="9" font-weight="900" letter-spacing="1">SIGNAL</text>
        <text x="540" y="88" text-anchor="middle" fill="#0a1f44" font-family="Poppins, sans-serif" font-size="8.5" font-weight="700">User enters</text>
        <text x="540" y="100" text-anchor="middle" fill="#0a1f44" font-family="Poppins, sans-serif" font-size="8.5" font-weight="700">HR Agent</text>

        <!-- Create support ticket (interaction) -->
        <rect x="200" y="56" width="130" height="48" fill="#1e3a8a" stroke="#79c0ff" stroke-width="1.5" rx="3"/>
        <text x="265" y="78" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="10" font-weight="700">Create a</text>
        <text x="265" y="92" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="10" font-weight="700">support ticket</text>

        <!-- Link to policy (interaction) -->
        <rect x="350" y="56" width="120" height="48" fill="#1e3a8a" stroke="#79c0ff" stroke-width="1.5" rx="3"/>
        <text x="410" y="84" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="10.5" font-weight="700">Link to policy</text>

        <!-- Link to new request on Workday (interaction) -->
        <rect x="900" y="56" width="180" height="48" fill="#1e3a8a" stroke="#79c0ff" stroke-width="1.5" rx="3"/>
        <text x="990" y="78" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="10" font-weight="700">Link to new request</text>
        <text x="990" y="92" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="10" font-weight="700">on Workday</text>

        <!-- ============ HANDSHAKE NODES ============ -->
        <!-- Router Logic (top-center, hidden logic = light blue rectangle) -->
        <rect x="430" y="178" width="220" height="62" fill="#3b82f6" stroke="#79c0ff" stroke-width="2" rx="4"/>
        <text x="540" y="198" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="10" font-weight="900" letter-spacing="0.5">Router Logic:</text>
        <text x="540" y="214" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="9" font-weight="600">Path A: Questions = RAG</text>
        <text x="540" y="228" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="9" font-weight="600">Path B: Task = Tools</text>

        <!-- A: User asks a question (interaction = dark blue square-ish) -->
        <rect x="290" y="280" width="180" height="44" fill="#1e3a8a" stroke="#79c0ff" stroke-width="1.5" rx="3"/>
        <text x="380" y="307" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="10" font-weight="700">A: User asks a question</text>

        <!-- B: User asks to enter vacation time -->
        <rect x="610" y="280" width="220" height="44" fill="#1e3a8a" stroke="#79c0ff" stroke-width="1.5" rx="3"/>
        <text x="720" y="307" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="10" font-weight="700">B: User asks to enter vacation time</text>

        <!-- ============ UNDERWATER NODES ============ -->
        <!-- "RAG" path label -->
        <text x="380" y="365" text-anchor="middle" fill="#79c0ff" font-family="Poppins, sans-serif" font-size="11" font-weight="900" letter-spacing="2">RAG</text>
        <!-- "API CALL" path label -->
        <text x="855" y="412" text-anchor="middle" fill="#fbbf24" font-family="Poppins, sans-serif" font-size="10" font-weight="900" letter-spacing="2">API CALL</text>

        <!-- HR policy KB (data flow = diamond) -->
        <polygon points="380,378 460,420 380,462 300,420" fill="#0a1838" stroke="#79c0ff" stroke-width="1.5"/>
        <text x="380" y="416" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="9" font-weight="700">HR policy</text>
        <text x="380" y="429" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="9" font-weight="700">knowledge base</text>

        <!-- HR Backend Workday API (data flow = diamond) -->
        <polygon points="720,378 810,420 720,462 630,420" fill="#0a1838" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="720" y="416" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="9" font-weight="700">HR Backend</text>
        <text x="720" y="429" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="9" font-weight="700">Workday API</text>

        <!-- AI-driven update of HR backend (hidden logic rectangle, parallel branch) -->
        <rect x="850" y="392" width="160" height="56" fill="#3b82f6" stroke="#79c0ff" stroke-width="1.5" rx="3"/>
        <text x="930" y="416" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="9.5" font-weight="700">AI-driven update of</text>
        <text x="930" y="430" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="9.5" font-weight="700">the HR backend</text>

        <!-- AI-generated answer (parallelogram = generated output) -->
        <polygon points="318,488 478,488 466,520 306,520" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1"/>
        <text x="392" y="508" text-anchor="middle" fill="#0a1838" font-family="Poppins, sans-serif" font-size="9.5" font-weight="700">AI-generated answer</text>

        <!-- AI-generated confirmation (parallelogram) -->
        <polygon points="600,488 820,488 808,520 588,520" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1"/>
        <text x="704" y="508" text-anchor="middle" fill="#0a1838" font-family="Poppins, sans-serif" font-size="9.5" font-weight="700">AI-generated confirmation (or failure)</text>

        <!-- ============ ARROWS ============ -->
        <!-- DOWN: Signal -> Router -->
        <path d="M 540 122 L 540 178" stroke="#79c0ff" stroke-width="2" fill="none" marker-end="url(#arr-blue)"/>

        <!-- DOWN: Router -> A -->
        <path d="M 480 240 L 380 280" stroke="#79c0ff" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>
        <!-- DOWN: Router -> B -->
        <path d="M 600 240 L 720 280" stroke="#79c0ff" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

        <!-- DOWN: A -> HR policy KB -->
        <path d="M 380 324 L 380 378" stroke="#79c0ff" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>
        <!-- DOWN: HR policy KB -> AI-generated answer -->
        <path d="M 380 462 L 388 488" stroke="#79c0ff" stroke-width="1.5" fill="none" marker-end="url(#arr-blue)"/>

        <!-- DOWN: B -> Workday API -->
        <path d="M 720 324 L 720 378" stroke="#fbbf24" stroke-width="1.5" fill="none" marker-end="url(#arr-amber)"/>
        <!-- DOWN: Workday API -> AI-driven update (right branch) -->
        <path d="M 810 420 L 850 420" stroke="#fbbf24" stroke-width="1.5" fill="none" marker-end="url(#arr-amber)"/>
        <!-- DOWN: Workday API -> AI-generated confirmation (left branch) -->
        <path d="M 720 462 L 710 488" stroke="#fbbf24" stroke-width="1.5" fill="none" marker-end="url(#arr-amber)"/>
        <!-- DOWN: AI-driven update -> AI-generated confirmation (curve back-left) -->
        <path d="M 850 448 C 820 470, 800 480, 770 488" stroke="#fbbf24" stroke-width="1.5" fill="none" marker-end="url(#arr-amber)"/>

        <!-- UP RETURN (mint, dashed). Both arrows sweep around the OUTSIDE of
             every tile. Same stroke-width and dash so neither dominates.
             Left: AI-gen answer -> Link to policy.
             Right: AI-gen confirmation -> Link to new request on Workday. -->
        <path d="M 306 520 C 0 520, 100 -200, 410 56" stroke="#34d399" stroke-width="1.5" fill="none" stroke-dasharray="6,4" marker-end="url(#arr-mint)"/>
        <path d="M 820 504 C 1300 520, 1000 -200, 990 56" stroke="#34d399" stroke-width="1.5" fill="none" stroke-dasharray="6,4" marker-end="url(#arr-mint)"/>

        <!-- Layer pillar tags (right edge of each layer) -->
        <text x="1080" y="44" text-anchor="end" fill="#79c0ff" font-family="Poppins, sans-serif" font-size="9" font-weight="900" letter-spacing="1.5" opacity="0.7">SURFACE = THE PRESENTATION</text>
        <text x="1080" y="180" text-anchor="end" fill="#bcb1ff" font-family="Poppins, sans-serif" font-size="9" font-weight="900" letter-spacing="1.5" opacity="0.7">HANDSHAKE = THE PROCESSING STATE</text>
        <text x="1080" y="358" text-anchor="end" fill="#fbbf24" font-family="Poppins, sans-serif" font-size="9" font-weight="900" letter-spacing="1.5" opacity="0.7">UNDERWATER = THE FEEDBACK LOOP</text>
      </svg>
    </div>

    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; max-width:1080px; margin:10px auto 0;">
      <div style="background:rgba(96,165,250,0.08); border:1px solid rgba(96,165,250,0.30); border-radius:8px; padding:7px 11px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:9px; color:#79c0ff; font-weight:900; letter-spacing:0.13em; text-transform:uppercase;">&darr; Down arrows</div>
        <div style="font-size:11px; color:#cdd5e3; line-height:1.45; margin-top:1px;">User signal sinks into hidden logic.</div>
      </div>
      <div style="background:rgba(251,191,36,0.08); border:1px solid rgba(251,191,36,0.30); border-radius:8px; padding:7px 11px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:9px; color:#fbbf24; font-weight:900; letter-spacing:0.13em; text-transform:uppercase;">&loz; Diamonds</div>
        <div style="font-size:11px; color:#cdd5e3; line-height:1.45; margin-top:1px;">Underwater data routing &mdash; KB or API.</div>
      </div>
      <div style="background:rgba(52,211,153,0.08); border:1px solid rgba(52,211,153,0.30); border-radius:8px; padding:7px 11px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:9px; color:#34d399; font-weight:900; letter-spacing:0.13em; text-transform:uppercase;">&uarr; Up arrows (dashed)</div>
        <div style="font-size:11px; color:#cdd5e3; line-height:1.45; margin-top:1px;">Generated output surfaces back to the user.</div>
      </div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Lab 1 (in-class, solo) - Architect Juno's Core AI User Flow
# ---------------------------------------------------------------------------

def _flow_step_card(num: str, title: str, body_html: str, accent: str) -> str:
    return f"""<div style="background:rgba(255,255,255,0.025); border:1px solid {accent}40; border-left:3px solid {accent}; border-radius:10px; padding:11px 14px; text-align:left;">
  <div style="display:flex; align-items:baseline; gap:8px; margin-bottom:5px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:{accent}; letter-spacing:0.14em; text-transform:uppercase;">{num}</div>
    <div style="font-family:'Poppins',sans-serif; font-size:12.5px; font-weight:800; color:#fff;">{title}</div>
  </div>
  {body_html}
</div>"""


JUNO_USER_FLOW_LAB_BODY = """
<div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:11px; padding:11px 14px; margin:0 auto 10px; max-width:1080px; text-align:left;">
  <div style="display:flex; flex-wrap:wrap; gap:14px; align-items:center; justify-content:space-between;">
    <div>
      <div style="font-family:'Poppins',sans-serif; font-size:11.5px; color:#79c0ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase;">&#x1F3AF; The Brief</div>
      <div style="font-family:'Poppins',sans-serif; font-size:13.5px; font-weight:800; color:#fff; margin-top:1px;">Architect Juno&rsquo;s strategic-alignment flow</div>
    </div>
    <div style="font-size:11.5px; color:#cdd5e3; max-width:640px; line-height:1.5;">
      Map exactly how Juno ingests a customer transcript, cross-references it against the RocketShip Strategy One-Pager <em>underwater</em>, and surfaces a defensible priority score on the dashboard.
    </div>
  </div>
</div>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; max-width:1080px; margin:0 auto;">
""" + _flow_step_card(
    "Step 1",
    "Identify the signal",
    '<p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.5;">e.g. <em>&ldquo;A new P0 transcript is uploaded to the Raw Input column.&rdquo;</em> Find the earliest moment data hits the system.</p>',
    "#3b82f6",
) + _flow_step_card(
    "Step 2",
    "Map the hidden logic",
    '<p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.5;">RAG retrieval of Strategy Doc &rarr; Comparison logic &rarr; Risk + alignment scoring. <strong style="color:#bcb1ff;">Steal from your M3 PRD.</strong></p>',
    "#bcb1ff",
) + _flow_step_card(
    "Step 3",
    "Design the maneuver",
    '<p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.5;">e.g. <em>&ldquo;Scanning Strategy&hellip;&rdquo;</em> breadcrumb in the Handshake Layer + inline V1 priority cards on the surface.</p>',
    "#fbbf24",
) + _flow_step_card(
    "Step 4",
    "Build the kill switch",
    '<p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.5;">A <em>Manual Override</em> on the priority score. Always a path back to a human-controlled state if logic fails.</p>',
    "#34d399",
) + """
</div>

<div style="display:grid; grid-template-columns:1.4fr 1fr; gap:10px; max-width:1080px; margin:10px auto 0;">
  <a href="../Modules/M4 - AI User Flow Architect.html" style="text-decoration:none;">
    <div style="background:linear-gradient(135deg, rgba(96,165,250,0.15), rgba(124,140,255,0.10)); border:1px solid rgba(96,165,250,0.5); border-radius:11px; padding:11px 14px; text-align:left;">
      <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">&#x270D;&#xFE0F; Tool &middot; Open the walkthrough</div>
      <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#fff;">M4 &mdash; AI User Flow Architect</div>
      <p style="font-size:11px; color:#cdd5e3; margin:4px 0 0; line-height:1.45;">Pre-loaded scenario + the four pillars laid out as forms. Exports to <code style="font-size:0.92em; color:#79c0ff;">04-ai-ux/user-flow.md</code>.</p>
    </div>
  </a>
  <div style="background:rgba(217,142,34,0.06); border:1px solid rgba(217,142,34,0.30); border-radius:11px; padding:10px 13px; text-align:left;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#fbbf24; font-weight:900; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">&#x1F4A1; Top tip</div>
    <p style="font-size:11px; color:#cdd5e3; margin:0; line-height:1.45;">Stuck on the underwater layer? Open <code style="font-size:0.92em; color:#fbbf24;">03-rag-prd/prd.md</code>. Your Knowledge Base, Top-K, and latency target are already there.</p>
  </div>
</div>
"""


# ---------------------------------------------------------------------------
# Section 04 - PM's Playbook for Closing AI Trust Gaps
# ---------------------------------------------------------------------------

def _trust_gap_card(num: str, name: str, problem: str, solutions: list, ex_label: str, ex_text: str, mockup_html: str, mockup_styles: str, accent: str) -> str:
    sol_html = "".join(
        f'<li style="font-size:11.5px; color:#cdd5e3; padding:3px 0 3px 0; line-height:1.5;"><strong style="color:#fff;">{title}:</strong> {detail}</li>'
        for title, detail in solutions
    )
    return f"""<section data-title="Trust Gap {num} &middot; {name}">
  <style>{mockup_styles}</style>
  <div class="inner">
    <div class="demo-tag tag-debrief">Trust Gap {num}</div>
    <h2>The {name} Gap</h2>
    <div class="subtitle" style="max-width:840px;">{problem}</div>

    <div style="display:grid; grid-template-columns:1.1fr 1fr; gap:14px; max-width:1080px; margin:18px auto 0; align-items:stretch;">

      <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.30); border-radius:14px; padding:14px 18px; text-align:left; display:flex; flex-direction:column; gap:6px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <div style="font-size:18px;">&#x1F4A1;</div>
          <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#34d399; letter-spacing:0.14em; text-transform:uppercase;">Solution &middot; Use explainable / controllable UI</div>
        </div>
        <ul style="margin:0; padding:0 0 0 18px;">
          {sol_html}
        </ul>
      </div>

      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.30); border-radius:14px; padding:14px 14px 14px; text-align:left; display:flex; flex-direction:column; gap:8px;">
        <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase;">&#x2728; Example &middot; {ex_label}</div>
        {mockup_html}
        <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{ex_text}</p>
      </div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Mockups: small CSS-animated product previews, conveying the same "GIF"
# energy as the source slides without bundling real screen recordings.
# ---------------------------------------------------------------------------

_MOCKUP_FRAME_BASE = """
.mk-frame{background:#0a1f44;border:1px solid rgba(255,255,255,0.10);border-radius:10px;overflow:hidden;font-family:'Lato','Inter',-apple-system,sans-serif;}
.mk-chrome{display:flex;align-items:center;gap:5px;background:rgba(255,255,255,0.04);border-bottom:1px solid rgba(255,255,255,0.08);padding:5px 8px;}
.mk-dot{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,0.18);}
.mk-addr{margin-left:6px;font-size:9px;color:#8899bb;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:0.04em;}
.mk-body{padding:9px 10px;font-size:10.5px;color:#cdd5e3;line-height:1.5;}
"""

# ---- Black Box mockup: Perplexity-style citations + animated source chip ---
_MOCKUP_BLACKBOX_STYLES = _MOCKUP_FRAME_BASE + """
.mk-bb sup{display:inline-block;background:rgba(96,165,250,0.18);color:#79c0ff;padding:0 5px;border-radius:4px;font-size:8.5px;font-weight:800;margin:0 1px;animation:bbPulse 2.4s ease-in-out infinite;}
.mk-bb sup:nth-child(2){animation-delay:0.6s;}
.mk-bb sup:nth-child(3){animation-delay:1.2s;}
@keyframes bbPulse{0%,80%,100%{background:rgba(96,165,250,0.18);color:#79c0ff;}40%{background:rgba(96,165,250,0.55);color:#fff;box-shadow:0 0 0 2px rgba(96,165,250,0.30);}}
.mk-bb-sources{display:flex;flex-wrap:wrap;gap:4px;margin-top:7px;padding-top:7px;border-top:1px solid rgba(255,255,255,0.08);}
.mk-bb-srcLabel{font-size:8.5px;color:#79c0ff;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;width:100%;margin-bottom:2px;}
.mk-bb-src{font-size:8.5px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:99px;padding:2px 7px;color:#cdd5e3;display:flex;align-items:center;gap:3px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;}
.mk-bb-src .num{color:#79c0ff;font-weight:800;}
.mk-bb-src.hl{animation:bbHL 4.8s ease-in-out infinite;}
.mk-bb-src.hl.d1{animation-delay:0s;} .mk-bb-src.hl.d2{animation-delay:1.6s;} .mk-bb-src.hl.d3{animation-delay:3.2s;}
@keyframes bbHL{0%,12%,90%,100%{background:rgba(255,255,255,0.04);border-color:rgba(255,255,255,0.08);}20%,30%{background:rgba(96,165,250,0.20);border-color:#79c0ff;color:#fff;}}
"""

_MOCKUP_BLACKBOX_HTML = """
<div class="mk-frame mk-bb">
  <div class="mk-chrome"><span class="mk-dot"></span><span class="mk-dot"></span><span class="mk-dot"></span><span class="mk-addr">perplexity.ai</span></div>
  <div class="mk-body">
    The Eiffel Tower is 330&nbsp;m tall<sup>1</sup> and was completed in 1889<sup>2</sup> after 2&nbsp;years of construction<sup>3</sup>.
    <div class="mk-bb-sources">
      <div class="mk-bb-srcLabel">&#x1F517; Sources</div>
      <span class="mk-bb-src hl d1"><span class="num">1</span> wikipedia.org</span>
      <span class="mk-bb-src hl d2"><span class="num">2</span> history.com</span>
      <span class="mk-bb-src hl d3"><span class="num">3</span> paris.fr</span>
    </div>
  </div>
</div>
"""


# ---- Hallucination mockup: Gemini-style draft chip + regenerate ----------
_MOCKUP_HALLUC_STYLES = _MOCKUP_FRAME_BASE + """
.mk-h-chip{display:inline-flex;align-items:center;gap:5px;background:rgba(251,191,36,0.16);color:#fbbf24;border:1px solid rgba(251,191,36,0.45);border-radius:99px;padding:2px 8px;font-size:8.5px;font-weight:800;letter-spacing:0.08em;text-transform:uppercase;animation:hChip 2.6s ease-in-out infinite;}
.mk-h-chip::before{content:"";width:6px;height:6px;border-radius:50%;background:#fbbf24;animation:hDot 1.4s ease-in-out infinite;}
@keyframes hChip{0%,100%{box-shadow:0 0 0 0 rgba(251,191,36,0);}50%{box-shadow:0 0 0 4px rgba(251,191,36,0.20);}}
@keyframes hDot{0%,100%{opacity:0.4;}50%{opacity:1;}}
.mk-h-text{margin-top:6px;color:#e8e8f0;border-bottom:1px dotted rgba(251,191,36,0.55);display:inline;padding-bottom:1px;}
.mk-h-alts{display:flex;flex-direction:column;gap:3px;margin-top:8px;}
.mk-h-alt{font-size:9.5px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:6px;padding:3px 8px;color:#cdd5e3;display:flex;align-items:center;gap:5px;}
.mk-h-alt.active{background:rgba(96,165,250,0.14);border-color:#79c0ff;color:#fff;}
.mk-h-alt .pick{color:#79c0ff;font-weight:800;font-size:9px;}
.mk-h-actions{display:flex;align-items:center;gap:6px;margin-top:8px;padding-top:6px;border-top:1px solid rgba(255,255,255,0.08);font-size:9.5px;color:#8899bb;}
.mk-h-actions .pill{display:inline-flex;align-items:center;gap:3px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:99px;padding:2px 8px;}
.mk-h-actions .regen{color:#79c0ff;border-color:rgba(96,165,250,0.40);background:rgba(96,165,250,0.10);animation:hRegen 3s ease-in-out infinite;}
@keyframes hRegen{0%,80%,100%{transform:rotate(0deg);}90%{transform:rotate(360deg);}}
"""

_MOCKUP_HALLUC_HTML = """
<div class="mk-frame mk-h">
  <div class="mk-chrome"><span class="mk-dot"></span><span class="mk-dot"></span><span class="mk-dot"></span><span class="mk-addr">docs.google.com &middot; gemini</span></div>
  <div class="mk-body">
    <span class="mk-h-chip">Draft &middot; Low confidence</span>
    <div style="margin-top:5px;">Q4 revenue was <span class="mk-h-text">approximately $4.2M</span> based on preliminary estimates.</div>
    <div class="mk-h-alts">
      <div class="mk-h-alt active"><span class="pick">&#9679;</span> &ldquo;approximately $4.2M&rdquo;</div>
      <div class="mk-h-alt"><span class="pick">&#9675;</span> &ldquo;around $4M&rdquo;</div>
      <div class="mk-h-alt"><span class="pick">&#9675;</span> &ldquo;in the $4&ndash;5M range&rdquo;</div>
    </div>
    <div class="mk-h-actions">
      <span class="pill">&#x1F44D; &#x1F44E;</span>
      <span class="pill regen">&#x21BB; Regenerate</span>
    </div>
  </div>
</div>
"""


# ---- Control mockup: Midjourney-style Vary Region selection ---------------
_MOCKUP_CONTROL_STYLES = _MOCKUP_FRAME_BASE + """
.mk-c-canvas{position:relative;height:122px;border-radius:6px;background:linear-gradient(135deg,#243b78 0%,#1e3a8a 30%,#5b3aa3 65%,#854d9c 100%);overflow:hidden;}
.mk-c-canvas::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 30% 70%,rgba(255,200,140,0.30) 0%,transparent 50%),radial-gradient(circle at 80% 30%,rgba(120,180,255,0.30) 0%,transparent 50%);}
.mk-c-sel{position:absolute;top:32px;left:54%;width:38%;height:48%;border:1.5px dashed #34d399;border-radius:3px;background:rgba(52,211,153,0.10);box-shadow:0 0 0 100vmax rgba(7,22,44,0.55);clip-path:inset(0);animation:cSel 3.2s ease-in-out infinite;}
.mk-c-sel::before,.mk-c-sel::after,.mk-c-sel > .h,.mk-c-sel > .h::after{content:"";position:absolute;width:7px;height:7px;background:#34d399;border:1.5px solid #07162C;border-radius:1px;}
.mk-c-sel::before{top:-4px;left:-4px;}
.mk-c-sel::after{top:-4px;right:-4px;}
.mk-c-sel .h{bottom:-4px;left:-4px;}
.mk-c-sel .h::after{position:absolute;bottom:0;right:-4px;left:auto;}
@keyframes cSel{0%,100%{transform:scale(1);}50%{transform:scale(1.04);}}
.mk-c-tooltip{position:absolute;bottom:8px;right:8px;background:rgba(7,22,44,0.85);border:1px solid #34d399;border-radius:6px;padding:4px 10px;font-size:9.5px;color:#34d399;font-weight:800;letter-spacing:0.06em;display:flex;align-items:center;gap:5px;animation:cTip 3.2s ease-in-out infinite;}
@keyframes cTip{0%,100%{transform:translateY(0);opacity:0.85;}50%{transform:translateY(-2px);opacity:1;}}
.mk-c-actions{display:flex;gap:5px;margin-top:7px;}
.mk-c-btn{flex:1;font-size:9.5px;font-weight:800;padding:5px 8px;border-radius:6px;text-align:center;background:rgba(52,211,153,0.18);color:#34d399;border:1px solid rgba(52,211,153,0.45);}
.mk-c-btn.alt{background:rgba(255,255,255,0.04);color:#cdd5e3;border-color:rgba(255,255,255,0.12);}
"""

_MOCKUP_CONTROL_HTML = """
<div class="mk-frame mk-c">
  <div class="mk-chrome"><span class="mk-dot"></span><span class="mk-dot"></span><span class="mk-dot"></span><span class="mk-addr">midjourney.com &middot; image edit</span></div>
  <div class="mk-body">
    <div class="mk-c-canvas">
      <div class="mk-c-sel"><span class="h"></span></div>
      <div class="mk-c-tooltip">&#x2728; Vary Region</div>
    </div>
    <div class="mk-c-actions">
      <div class="mk-c-btn">&#x270F;&#xFE0F; Vary Region</div>
      <div class="mk-c-btn alt">&#x21B6; Undo</div>
    </div>
  </div>
</div>
"""


def trust_gap_blackbox() -> str:
    return _trust_gap_card(
        "1",
        "Black Box",
        "Users reject AI-generated insights when they can&rsquo;t see the logic or the data sources used to reach the conclusion.",
        [
            ("Source scaffolding", "Link AI summaries back to the original docs with inline citations or hover-states that show the source material."),
            ("Chain-of-thought visibility", "Reveal reasoning steps for complex tasks &mdash; show files searched, rows extracted, decisions taken."),
        ],
        "Perplexity",
        "Dedicated <em>Sources</em> row + numbered citations throughout the answer &mdash; users verify any claim in a single click.",
        _MOCKUP_BLACKBOX_HTML,
        _MOCKUP_BLACKBOX_STYLES,
        "#fbbf24",
    )


def trust_gap_hallucination() -> str:
    return _trust_gap_card(
        "2",
        "Hallucination",
        "Users lose confidence in the entire product when the AI delivers factually incorrect or inconsistent answers without warning.",
        [
            ("Visual metadata", "Use light-grey text, dotted underlines, or &ldquo;Draft&rdquo; watermarks where the model&rsquo;s confidence score is below threshold."),
            ("Proactive caveats", "Surface low-confidence warnings or alternative interpretations when the model is uncertain."),
        ],
        "Gemini for Workspace",
        "Draft watermarks for low-confidence output, plus <em>rate / regenerate / pick another phrasing</em> &mdash; turning probabilistic mistakes into a conversation.",
        _MOCKUP_HALLUC_HTML,
        _MOCKUP_HALLUC_STYLES,
        "#fbbf24",
    )


def trust_gap_control() -> str:
    return _trust_gap_card(
        "3",
        "Control",
        "Invisible design backfires when users feel locked in to an AI&rsquo;s decision and can&rsquo;t easily override, edit, or undo a mistake.",
        [
            ("One-click reversion", "Provide instant <em>undo</em> or <em>restore original</em> for any AI-transformed content. Cost of a mistake = zero."),
            ("Direct-edit access", "Never present AI output read-only. Every V1 draft must be instantly editable without a new prompt."),
        ],
        "Midjourney &middot; Vary Region",
        "Select a specific part of the AI image and re-generate <em>just that section</em> &mdash; surgical control instead of all-or-nothing.",
        _MOCKUP_CONTROL_HTML,
        _MOCKUP_CONTROL_STYLES,
        "#fbbf24",
    )


def aiux_readiness_checklist() -> str:
    """3-level hierarchy of needs for AI-UX."""
    levels = [
        ("01", "Functional Baseline",
         "Does the AI trigger reliably at the correct moment?",
         "Define strict confidence thresholds. Only automate when the system is &ge; 90% certain of intent.",
         "Trigger Accuracy",
         "#3b82f6"),
        ("02", "Reliability &amp; Verification",
         "Can the user verify the output in under three seconds?",
         "Design source scaffolding &mdash; inline citations or logic summaries that bridge the trust gap without cluttering the UI.",
         "System Transparency",
         "#fbbf24"),
        ("03", "Magical Flow",
         "Does the interaction remove more labor than it creates?",
         "Measure correction rate. If users keep manually fixing the AI&rsquo;s work, revert from invisible UI to a validator UI.",
         "Invisible Integration",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:14px 16px; text-align:left; display:flex; flex-direction:column; gap:8px;">
  <div style="display:flex; align-items:baseline; gap:10px;">
    <div style="font-family:'Poppins',sans-serif; font-size:30px; font-weight:900; color:{col}; line-height:1;">{n}</div>
    <div>
      <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:{col}; letter-spacing:0.14em; text-transform:uppercase;">{tag}</div>
      <div style="font-family:'Poppins',sans-serif; font-size:14px; font-weight:800; color:#fff; line-height:1.3;">{title}</div>
    </div>
  </div>
  <div style="background:rgba(0,0,0,0.25); border-radius:7px; padding:7px 11px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:{col}; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:3px;">Ship criterion</div>
    <p style="font-size:11.5px; color:#fff; margin:0; line-height:1.5;">{question}</p>
  </div>
  <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;">{detail}</p>
</div>"""
        for n, title, question, detail, tag, col in levels
    )
    return f"""<section data-title="AI-UX Readiness Checklist">
  <div class="inner">
    <div class="demo-tag tag-build">Framework</div>
    <h2>The AI-UX Readiness Checklist</h2>
    <div class="subtitle">Don&rsquo;t build &ldquo;magic&rdquo; on a broken foundation. Pass each level before climbing to the next.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; max-width:1080px; margin:22px auto 0; align-items:stretch;">
      {cards}
    </div>
    <p style="font-size:12px; color:#cdd5e3; max-width:780px; margin:14px auto 0; padding:9px 16px; background:rgba(124,140,255,0.06); border-left:3px solid #bcb1ff; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">PM rule of thumb:</strong> if you can&rsquo;t pass Level 2 yet, ship a Level-2 UI. A &ldquo;reliable validator&rdquo; product beats a &ldquo;magical liar&rdquo; product every time.
    </p>
  </div>
</section>
"""


def intelligence_tax_2() -> str:
    """Latency tax + Privacy tax."""
    taxes = [
        ("&#x23F1;&#xFE0F;", "01", "The Latency Tax",
         "High-quality model inference takes time. The user thinks the app is broken.",
         "Use <strong>streaming responses</strong> or <strong>status breadcrumbs</strong> (&ldquo;Scanning backlog&hellip;&rdquo;). Turn idle time into active progress.",
         "#fbbf24"),
        ("&#x1F510;", "02", "The Privacy Tax",
         "Users hesitate to share proprietary or personal data with a model they don&rsquo;t own.",
         "Build <strong>permission-first architecture</strong> with clear privacy badges. Implement <strong>opt-in memory</strong> for surgical control.",
         "#34d399"),
    ]
    cards = "".join(
        f"""<div style="background:rgba(255,255,255,0.035); border:1px solid {col}40; border-radius:14px; padding:16px 20px; text-align:left;">
  <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
    <div style="font-size:28px;">{emoji}</div>
    <div>
      <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:{col}; letter-spacing:0.14em; text-transform:uppercase;">Tax {n}</div>
      <div style="font-family:'Poppins',sans-serif; font-size:15px; font-weight:800; color:#fff; line-height:1.3;">{title}</div>
    </div>
  </div>
  <p style="font-size:12.5px; color:#cdd5e3; line-height:1.5; margin:0 0 8px;">{problem}</p>
  <div style="background:rgba(0,0,0,0.25); border-left:3px solid {col}; border-radius:0 7px 7px 0; padding:8px 12px;">
    <div style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:{col}; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:3px;">Manage with</div>
    <p style="font-size:12px; color:#cdd5e3; margin:0; line-height:1.55;">{fix}</p>
  </div>
</div>"""
        for emoji, n, title, problem, fix, col in taxes
    )
    return f"""<section data-title="Managing the Intelligence Tax">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Reality Check</div>
    <h2>Managing the &ldquo;Intelligence Tax&rdquo;</h2>
    <div class="subtitle">These aren&rsquo;t bugs. They&rsquo;re inherent properties of LLMs. Your UI hides the technical limits.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; max-width:1000px; margin:22px auto 0; align-items:stretch;">
      {cards}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Optional Post-Class Lab + Resources
# ---------------------------------------------------------------------------

def optional_post_class_title() -> str:
    """Source slide 32 - title card for the optional post-class lab."""
    return """<section class="section-break" data-title="Optional Post-Class Hands-On Lab">
  <div class="section-break-inner">
    <div class="lab-title">Optional Post-Class &middot; Hands-On Lab</div>
    <div class="lab-name">Reimagine Juno as an AI-Native Copilot</div>
  </div>
</section>
"""


def optional_post_class_outcome() -> str:
    """Source slide 33 - outcome + walkthrough link."""
    return """<section data-title="Reimagine Juno as an AI-Native Copilot">
  <div class="inner">
    <div class="demo-tag tag-build">Optional &middot; Post-Class Practice</div>
    <h2>Reimagine Juno as an AI-Native Co-pilot</h2>
    <div class="subtitle">Optional, on your own time. Not required for course completion.</div>

    <div style="max-width:1040px; margin:22px auto 0;">
      <a href="../Modules/M4 - Juno AI-Native Lab.html" style="text-decoration:none;">
        <div style="background:linear-gradient(135deg, rgba(124,140,255,0.18), rgba(96,165,250,0.10)); border:1px solid rgba(124,140,255,0.5); border-radius:14px; padding:16px 22px; text-align:left;">
          <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#bcb1ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">&#x270D;&#xFE0F; Lab Exercise Outcome</div>
          <div style="font-family:'Poppins',sans-serif; font-size:15px; font-weight:800; color:#fff; margin-bottom:6px;">Follow along and complete this lab with the walkthrough &rarr;</div>
          <p style="font-size:12.5px; color:#cdd5e3; margin:0; line-height:1.55;"><code style="font-size:0.92em; color:#bcb1ff;">M4 &mdash; Juno AI-Native Lab.html</code> &middot; pick Path 1 (Strategic Trust Ladder) or Path 2 (Frictionless Architect). Three levels each (Functional &rarr; Reliable &rarr; Magical). Pre-loaded Lovable prompts + the Sarah transcript.</p>
        </div>
      </a>
    </div>
  </div>
</section>
"""


def m4_resources_templates() -> str:
    flow_url = "../Modules/M4 - AI User Flow Architect.html"
    native_url = "../Modules/M4 - Juno AI-Native Lab.html"
    trust_url = "../Modules/M4 - AI-UX Trust Gap Checker.html"
    cards = [
        ("&#x270D;&#xFE0F; In-Class Lab Tool", "Architect Juno&rsquo;s AI User Flow",
         "M4 &mdash; AI User Flow Architect", "The 4-pillar walkthrough. Auto-exports a markdown user flow.",
         flow_url, "#3b82f6"),
        ("&#x1F680; Optional Post-Class", "Reimagine Juno as AI-Native Copilot",
         "M4 &mdash; Juno AI-Native Lab", "3-level Lovable walkthrough. Path 1 (Trust Ladder) or Path 2 (Frictionless Architect).",
         native_url, "#bcb1ff"),
        ("&#x1F50D; Bonus Audit Tool", "Audit any AI feature for trust gaps",
         "M4 &mdash; AI-UX Trust Gap Checker", "Score Black-box, Hallucination, Control. Outputs to <code style=\"font-size:0.9em; color:#fbbf24;\">04-ai-ux/trust-gaps.md</code>.",
         trust_url, "#fbbf24"),
        ("&#x1F4DA; Project Repo Template", "One-click create your <code style=\"font-size:0.9em; color:#34d399;\">juno-pm</code> repo",
         "ai-product-management-template", "Use the template if you haven&rsquo;t already.",
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
    <div class="demo-tag tag-debrief">Resources</div>
    <h2>Resources &amp; templates</h2>
    <div class="subtitle">All M4 tools live in <code>/Modules/</code>. Deliverables commit to <code>04-ai-ux/</code>.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; max-width:1040px; margin:22px auto 0;">
      {cards_html}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build_module_4():
    """Build (instructor_sections, share_sections) for Module 4."""
    sections_inst, sections_share = [], []
    add = _add_builder(sections_inst, sections_share)

    # 1. Hero
    add(hero(
        title_lead="Design AI-Native",
        title_accent="User Experiences",
        subtitle="Module 4 &middot; AI Product Management Certification",
        waypoints=[
            ("Intent-Driven AI Design", "From layered features to clean-sheet AI-native flows."),
            ("Designing Invisible UI", "Three patterns, three placements. Match value to maneuver."),
            ("Architecting the AI Iceberg", "Map underwater logic + surface experience."),
            ("Closing AI Trust Gaps", "Black-box, hallucination, control. Three execution patterns."),
        ],
        out_line="You finish Module 4 with one required artefact: <code>04-ai-ux/user-flow.md</code> &mdash; Juno&rsquo;s AI-native user flow with surface, handshake, and underwater layers mapped.",
        module_n=4,
    ))

    # 2. Class Expectations
    add(class_expectations(),
        note="Source slide 2. Set ground rules: cameras-on for live cohort sessions, async etiquette for solo learners. Solo course &mdash; all interactions go through #ai-pm-cohort.")

    # 3. Syllabus
    add(syllabus_visual_m4(),
        note="Source slide 3. AI Product Management Syllabus, M4 highlighted.")

    # 4. Agenda
    add(agenda_4_m4(),
        note="Source slide 4. Four numbered sections + an optional post-class Lovable lab. One in-class solo lab anchors the day.")

    # ----- Section 01 -----
    add(section_divider("01", "Intent-Driven AI Design Systems"),
        note="Section 1 &mdash; why &lsquo;clean sheet&rsquo; AI products feel different from AI-layered legacy products.")

    add(clunky_aiux_qa(),
        note="Source slide 6. Instructor-Led Q&A &middot; 5 min. Read out the questions, give learners a few minutes to think, then take 2-3 examples live. Async cohort learners post their answer in #ai-pm-cohort.")

    add(ai_ux_implementations(),
        note="Bing = traditional. Perplexity = AI-native. Both ship; one scales differently. The model isn't a feature in AI-native &mdash; it's the engine.")

    add(why_ai_native_matters_4(),
        note="Four reasons AI-native matters: lowered interaction costs, shifted cognitive load, system resilience, contextual relevance. Users move from builder &rarr; strategic reviewer.")

    # ----- Section 02 -----
    add(section_divider("02", "Designing Invisible UI for AI-Native Outcomes"),
        note="Section 2 &mdash; three patterns + three placement maneuvers. Match value to surface.")

    add(invisible_by_design_3(),
        note="Three patterns: environmental signals (Glean), intent prediction (Adobe Firefly), automated data flow (Salesforce). Invisible = labour disappears, not the AI.")

    add(ai_placement_3(),
        note="Three placements: Inline (Google Docs), Floating (Figma AI), Full-Page Canvas (Gamma/Canva). Choose by complexity of the AI output.")

    add(spot_the_friction_qa(),
        note=(
            "Source slide 12. Instructor-Led Q&A &middot; 10 min. Read the scenario, give learners a few minutes to think, then take answers live. "
            "<br><br><strong>Possible answers (from source speaker notes):</strong>"
            "<br>&middot; <em>Chatbot trap</em> &mdash; sidecar UI that makes the recruiter look-then-chat-then-copy-paste."
            "<br>&middot; <em>Reactive</em> &mdash; waits for a manual prompt instead of using &lsquo;profile open&rsquo; as the signal."
            "<br>&middot; <em>Cognitive load</em> &mdash; forces the user to be a Creator (thinking of what to say) rather than a Validator (reacting to a draft)."
            "<br><br><strong>Possible AI-native pivot:</strong> the moment the page loads, the AI starts work in the background. V1 drafting creates a personalised message from the candidate&rsquo;s history and the open role. Put that draft inline directly in the messaging field of the platform."
        ))

    add(value_to_ux_4(),
        note="Decision logic: Automation &rarr; Full-Page Canvas. Augmentation &rarr; Inline. Insights and Personalization &rarr; Floating &amp; Contextual.")

    # ----- Section 03 -----
    add(section_divider("03", "How to Architect an AI User Flow"),
        note="Section 3 &mdash; the Iceberg model + four pillars. Map what the system thinks, not just what the user clicks.")

    add(architecting_iceberg(),
        note="Mental model: simple UI on top, complex logic below. The PM&rsquo;s strategic lever is deciding the balance between effortlessness (invisible) and verification (visible).")

    add(four_pillars(),
        note="Trigger / Processing / Presentation / Feedback Loop. Each pillar has an underwater half (PM specs the logic) and a surface half (what the user feels).")

    add(user_flow_legend(),
        note="Builder&rsquo;s legend (Signal &middot; Logic &middot; Maneuver &middot; Data Flow &middot; Output) + the 4-step process. This is what learners will use in the lab.")

    add(hr_agent_example(),
        note="HR Agent walkthrough: 3 layers (Surface / Handshake / Underwater). RAG path for questions, API path for tasks. Always a human fall-back if logic fails.")

    # 5-min break
    add(break_section(), note="5-minute break.")

    # Cameras on reminder
    add(cameras_on(), note="Cameras-on reminder for live cohort.")

    # Lab 1 (in-class, solo)
    add(applied_work(
            title="Architect Juno&rsquo;s Core AI User Flow",
            goal="Design the logic that lets Juno move beyond summarisation into strategic judgment &mdash; mapping how it ingests transcripts, cross-references the RocketShip Strategy One-Pager underwater, and surfaces a defensible priority score.",
            body_html=JUNO_USER_FLOW_LAB_BODY,
            repo_path="juno-pm/04-ai-ux/user-flow.md",
            timer_min=30,
            tool_url="../Modules/M4%20-%20AI%20User%20Flow%20Architect.html",
            tool_desc="The 4-pillar walkthrough as forms (Signal, Logic, Maneuver, Feedback Loop). Pre-loaded with the Juno strategic-alignment scenario. Exports straight to <code>04-ai-ux/user-flow.md</code>.",
        ),
        note="Solo lab. Originally a group exercise &mdash; converted to individual work. Learners use the M4 - AI User Flow Architect tool. Output committed to 04-ai-ux/user-flow.md.")

    # ----- Section 04 -----
    add(section_divider("04", "The PM&rsquo;s Playbook for Closing AI Trust Gaps"),
        note="Section 4 &mdash; three failure modes (Black-box, Hallucination, Control) and the execution patterns that close each.")

    add(trust_gap_blackbox(),
        note="Source scaffolding + chain-of-thought visibility. The PM goal: reduce the cost of verification under 3 seconds. Perplexity is the gold-standard example.")

    add(trust_gap_hallucination(),
        note="Visual metadata + proactive caveats. Manage expectations, don&rsquo;t pretend the model is certain. Gemini Workspace lets users rate, regenerate, and refine in-context.")

    add(trust_gap_control(),
        note="One-click revert + direct edit. Never read-only. Midjourney&rsquo;s Vary Region = surgical control instead of all-or-nothing regeneration.")

    add(aiux_readiness_checklist(),
        note="3-level hierarchy: Functional &rarr; Reliable &rarr; Magical. Don&rsquo;t skip floors. If you can&rsquo;t pass Level 2, ship a Level-2 UI &mdash; reliable validator &gt; magical liar.")

    add(intelligence_tax_2(),
        note="Source slide 27. Two inherent LLM costs the UI must mask: Latency (streaming + status breadcrumbs turn waiting into transparency) and Privacy (permission-first + opt-in memory).")

    # Source slide 28 - Key Takeaways
    add(takeaways(
            "Design AI-Native User Experiences",
            [
                ("AI-Native beats AI-Layered.",
                 "Move from layering AI on legacy systems to designing flows where the model is the engine. Surface tools only when the system predicts intent."),
                ("Invisible UI uses environmental signals.",
                 "Background tasks triggered by uploads, meetings, page loads. The user becomes a manager of outcomes, not an active operator."),
                ("Architect the AI Iceberg.",
                 "Map underwater logic + visible maneuvers. Confidence thresholds and kill switches let users recover without friction."),
                ("Close trust gaps with explainable UI.",
                 "Source scaffolding, chain-of-thought visibility, one-click undo. Verifiable in &lt; 3 seconds or it doesn&rsquo;t ship."),
            ],
        ),
        note="Source slide 28. Recap of the four big moves of M4.")

    # Source slide 29 - Next Session + Extra Practice (combined slide in source)
    add(extra_practice(
            [
                ("Audit for invisible-UI opportunities", "In your current product",
                 "Pick a high-friction workflow that requires multiple menus or copy-paste. Re-map it as an Iceberg. Identify which steps could move underwater using environmental signals (file upload, meeting end, page load)."),
                ("Close a real-world trust gap", "On an existing AI feature",
                 "Select an AI feature with low adoption or hallucination problems. Use the AI-UX Readiness Checklist to spec a high-fidelity Explainable UI requirement &mdash; verifiable in &lt; 3 seconds."),
            ],
            "<strong>Next session: Module 5</strong> &mdash; <em>Deploy Agentic Systems and Workflows</em>. Configure reasoning paths and tool triggers to execute complex tasks with minimal human intervention.",
        ),
        note="Source slide 29. Next-session preview + Extra Practice combined per the source.")

    # Source slide 30 - Bonus Resources & Templates
    add(m4_resources_templates(),
        note="Source slide 30. Bonus resources: AI User Flow Template + Module 4 Exercise Guide.")

    # Source slide 31 - Q&A
    add(qa_section(),
        note="Source slide 31. Async-only Q&A. Park unresolved questions in #ai-pm-cohort. Instructor responds in-thread within ~5 days.")

    # Source slides 32 + 33 - Optional Post-Class Hands-On Lab (after Q&A in the source)
    add(optional_post_class_title(),
        note="Source slide 32. Title card for the optional post-class lab. Not required for course completion.")
    add(optional_post_class_outcome(),
        note="Source slide 33. Outcome + link to the walkthrough tool. Two paths in the tool: Trust Ladder or Frictionless Architect.")

    # Source slide 34 (Thank you) - intentionally skipped per user instruction.

    return sections_inst, sections_share
