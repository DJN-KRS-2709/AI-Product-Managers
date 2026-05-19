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
    Two-column layout mirrors the source: lead + Traditional/AI-native
    contrast on the left, literal iceberg illustration with the source
    'Top Tip' floating callout on the right."""
    return """<section data-title="Architecting the AI Iceberg">
  <div class="inner">
    <div class="demo-tag tag-build">Lecture &middot; Mental Model</div>
    <h2>Architecting the AI &ldquo;Iceberg&rdquo;</h2>

    <div style="display:grid; grid-template-columns:1.2fr 0.95fr; gap:36px; max-width:1080px; margin:18px auto 0; align-items:stretch;">

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

      <!-- RIGHT - iceberg illustration with floating Top Tip -->
      <div style="position:relative; min-height:380px;">

        <!-- Top Tip floating callout - overlaps the iceberg sky -->
        <div style="position:absolute; top:8px; left:50%; transform:translateX(-50%); width:88%; background:rgba(7,22,44,0.92); border:1px solid rgba(251,191,36,0.45); border-radius:12px; padding:11px 14px; backdrop-filter:blur(6px); z-index:2; box-shadow:0 8px 24px rgba(0,0,0,0.4);">
          <div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">
            <div style="width:24px; height:24px; border-radius:50%; background:rgba(251,191,36,0.18); border:1px solid rgba(251,191,36,0.5); display:flex; align-items:center; justify-content:center;">
              <span style="font-size:13px;">&#x1F4A1;</span>
            </div>
            <span style="font-family:'Poppins',sans-serif; font-size:9.5px; font-weight:900; color:#fbbf24; letter-spacing:0.16em; text-transform:uppercase;">Top Tip</span>
          </div>
          <p style="font-size:11.5px; color:#fff; line-height:1.5; margin:0; font-weight:600;">
            You must decide what remains <em style="color:#79c0ff;">&ldquo;Invisible&rdquo;</em> to keep the experience effortless, and what needs to be <em style="color:#fbbf24;">&ldquo;Visible&rdquo;</em> to build user trust.
          </p>
        </div>

        <!-- Iceberg SVG -->
        <svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid meet" style="width:100%; height:100%; min-height:380px; border-radius:14px; display:block;" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="sky-grad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#0a1f44" />
              <stop offset="100%" stop-color="#15315a" />
            </linearGradient>
            <linearGradient id="water-grad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#0a1838" />
              <stop offset="100%" stop-color="#04091e" />
            </linearGradient>
            <linearGradient id="ice-above-grad" x1="0.3" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#f0f7ff" />
              <stop offset="55%" stop-color="#bcd5f5" />
              <stop offset="100%" stop-color="#7da4d8" />
            </linearGradient>
            <linearGradient id="ice-below-grad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#5b8ac8" stop-opacity="0.85" />
              <stop offset="100%" stop-color="#1f3870" stop-opacity="0.65" />
            </linearGradient>
            <radialGradient id="glow" cx="0.7" cy="0.2" r="0.6">
              <stop offset="0%" stop-color="#ffffff" stop-opacity="0.18" />
              <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
            </radialGradient>
          </defs>

          <!-- Sky band -->
          <rect x="0" y="0" width="400" height="170" fill="url(#sky-grad)" />
          <!-- Subtle radial glow on sky -->
          <rect x="0" y="0" width="400" height="170" fill="url(#glow)" />
          <!-- Water band -->
          <rect x="0" y="170" width="400" height="230" fill="url(#water-grad)" />

          <!-- Iceberg peak (above water) -->
          <polygon points="190,55 160,170 244,170 222,95 205,72" fill="url(#ice-above-grad)" />
          <!-- Highlight facet on the peak -->
          <polygon points="205,72 222,95 195,128 187,90" fill="#ffffff" opacity="0.35" />
          <!-- Shadow facet -->
          <polygon points="187,90 195,128 175,170 160,170" fill="#0a1f44" opacity="0.18" />

          <!-- Iceberg body (underwater) - much larger than the peak -->
          <polygon points="160,170 244,170 322,232 340,290 310,340 240,360 130,355 70,300 60,238" fill="url(#ice-below-grad)" />
          <!-- Underwater facet highlights -->
          <polygon points="244,170 322,232 270,210" fill="#ffffff" opacity="0.10" />
          <polygon points="160,170 70,300 110,220" fill="#ffffff" opacity="0.06" />
          <!-- Underwater shadow facets -->
          <polygon points="240,360 310,340 280,300" fill="#000" opacity="0.20" />
          <polygon points="60,238 70,300 95,260" fill="#000" opacity="0.15" />

          <!-- Water surface line + shimmer -->
          <line x1="0" y1="170" x2="400" y2="170" stroke="#79c0ff" stroke-width="0.8" stroke-dasharray="4,4" opacity="0.45" />
          <path d="M 0 167 Q 100 165 200 167 T 400 167" stroke="rgba(255,255,255,0.18)" stroke-width="0.6" fill="none" />
          <path d="M 0 174 Q 80 176 160 173 T 400 174" stroke="rgba(255,255,255,0.10)" stroke-width="0.6" fill="none" />

          <!-- "Surface" label - subtle, above water on the right -->
          <text x="385" y="160" fill="#79c0ff" font-family="Poppins, sans-serif" font-size="9" font-weight="900" letter-spacing="2" text-anchor="end" opacity="0.7">SURFACE</text>
          <!-- "Underwater" label - subtle, below the iceberg waist on the right -->
          <text x="385" y="380" fill="#bcb1ff" font-family="Poppins, sans-serif" font-size="9" font-weight="900" letter-spacing="2" text-anchor="end" opacity="0.55">UNDERWATER</text>
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
    """The legend + 4-step process for building an AI User Flow."""
    legend = [
        ("&#x25EF;", "Signal", "Entry point", "#3b82f6"),
        ("&#x2B22;", "Hidden Logic", "Major step (underwater)", "#bcb1ff"),
        ("&#x25A0;", "Interaction", "Sub-step (surface maneuver)", "#fbbf24"),
        ("&#x25C6;", "Data Flow", "Routing decision", "#34d399"),
        ("&#x25B0;", "Generated Output", "AI result", "#f87171"),
    ]
    legend_html = "".join(
        f'<div style="display:flex; align-items:center; gap:10px; padding:6px 10px; background:rgba(255,255,255,0.025); border:1px solid {col}40; border-radius:8px;">'
        f'<div style="font-size:24px; color:{col}; line-height:1; width:30px; text-align:center;">{glyph}</div>'
        f'<div style="text-align:left;">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:11.5px; font-weight:800; color:#fff;">{name}</div>'
        f'<div style="font-size:10.5px; color:#8899bb;">{desc}</div>'
        f'</div></div>'
        for glyph, name, desc, col in legend
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

    return f"""<section data-title="Building the AI User Flow">
  <div class="inner">
    <div class="demo-tag tag-build">Framework &middot; Builder&rsquo;s Legend</div>
    <h2>How to build the AI user flow</h2>
    <div class="subtitle">A small set of shapes + four steps. Used in the lab next.</div>

    <div style="display:grid; grid-template-columns:1.1fr 1.5fr; gap:18px; max-width:1080px; margin:18px auto 0; align-items:start;">
      <div style="background:rgba(255,255,255,0.025); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:14px 18px; text-align:left;">
        <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#a0aec0; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px;">&#x1F9F1; Builder&rsquo;s legend</div>
        <div style="display:flex; flex-direction:column; gap:6px;">
          {legend_html}
        </div>
      </div>

      <div>
        <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px; padding-left:4px;">&#x270D;&#xFE0F; Four steps to map a flow</div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
          {steps_html}
        </div>
      </div>
    </div>
  </div>
</section>
"""


def hr_agent_example() -> str:
    """3-layer Iceberg case study: HR Agent."""
    return """<section data-title="Example: HR Agent">
  <div class="inner">
    <div class="demo-tag tag-build">Case Study</div>
    <h2>Example &mdash; HR Agent in three layers</h2>
    <div class="subtitle">The same iceberg, spelled out for a real product. Read the rows top-down.</div>

    <div style="max-width:1080px; margin:18px auto 0; border:1px solid rgba(255,255,255,0.10); border-radius:14px; overflow:hidden;">

      <!-- Surface Layer -->
      <div style="background:rgba(96,165,250,0.10); padding:13px 18px; border-bottom:1px solid rgba(255,255,255,0.10);">
        <div style="display:grid; grid-template-columns:140px 1fr; gap:18px; align-items:start;">
          <div>
            <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Surface</div>
            <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#fff;">User experience</div>
            <p style="font-size:11px; color:#8899bb; margin:4px 0 0; line-height:1.5;">What the employee touches.</p>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px;">
            <div style="background:rgba(0,0,0,0.25); border:1px solid rgba(96,165,250,0.4); border-radius:6px; padding:8px 10px;"><div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.1em;">SIGNAL</div><div style="font-size:11px; color:#fff; margin-top:2px;">User enters HR Agent</div></div>
            <div style="background:rgba(0,0,0,0.25); border:1px solid rgba(96,165,250,0.4); border-radius:6px; padding:8px 10px;"><div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.1em;">A &middot; Question</div><div style="font-size:11px; color:#fff; margin-top:2px;">AI answer + link to policy</div></div>
            <div style="background:rgba(0,0,0,0.25); border:1px solid rgba(96,165,250,0.4); border-radius:6px; padding:8px 10px;"><div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.1em;">B &middot; Action</div><div style="font-size:11px; color:#fff; margin-top:2px;">Confirmation + ticket fallback</div></div>
          </div>
        </div>
      </div>

      <!-- Handshake Layer -->
      <div style="background:rgba(124,140,255,0.10); padding:13px 18px; border-bottom:1px solid rgba(255,255,255,0.10);">
        <div style="display:grid; grid-template-columns:140px 1fr; gap:18px; align-items:start;">
          <div>
            <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#bcb1ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">Handshake</div>
            <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#fff;">Connection layer</div>
            <p style="font-size:11px; color:#8899bb; margin:4px 0 0; line-height:1.5;">PM magic happens here.</p>
          </div>
          <div style="background:rgba(0,0,0,0.25); border:1px dashed rgba(124,140,255,0.4); border-radius:6px; padding:10px 14px;">
            <div style="font-family:'Poppins',sans-serif; font-size:10px; font-weight:900; color:#bcb1ff; letter-spacing:0.13em; text-transform:uppercase; margin-bottom:5px;">&#x1F500; Router Logic + Progress Breadcrumbs</div>
            <p style="font-size:11.5px; color:#cdd5e3; margin:0 0 4px; line-height:1.5;"><strong style="color:#fff;">Path A &rarr; Question:</strong> route to <em>RAG over HR knowledge base</em>.</p>
            <p style="font-size:11.5px; color:#cdd5e3; margin:0; line-height:1.5;"><strong style="color:#fff;">Path B &rarr; Task:</strong> route to <em>Workday API tool call</em>. Show &ldquo;Submitting to Workday&hellip;&rdquo; status.</p>
          </div>
        </div>
      </div>

      <!-- Underwater Workflow Layer -->
      <div style="background:rgba(7,22,44,0.5); padding:13px 18px;">
        <div style="display:grid; grid-template-columns:140px 1fr; gap:18px; align-items:start;">
          <div>
            <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:3px;">&#x1F9CA; Underwater</div>
            <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:800; color:#fff;">AI workflow layer</div>
            <p style="font-size:11px; color:#8899bb; margin:4px 0 0; line-height:1.5;">The heavy lifting.</p>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <div style="background:rgba(96,165,250,0.10); border:1px solid rgba(96,165,250,0.30); border-radius:6px; padding:8px 10px;"><div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#79c0ff; font-weight:900; letter-spacing:0.1em;">RAG PATH</div><div style="font-size:11px; color:#cdd5e3; margin-top:2px;">Vector search over HR policy KB &rarr; grounded answer + citation</div></div>
            <div style="background:rgba(217,142,34,0.10); border:1px solid rgba(217,142,34,0.30); border-radius:6px; padding:8px 10px;"><div style="font-family:'Poppins',sans-serif; font-size:9.5px; color:#fbbf24; font-weight:900; letter-spacing:0.1em;">TASK PATH</div><div style="font-size:11px; color:#cdd5e3; margin-top:2px;">Workday API call to enter vacation &rarr; AI-driven update + confirmation</div></div>
          </div>
        </div>
      </div>
    </div>

    <p style="font-size:12px; color:#cdd5e3; max-width:880px; margin:14px auto 0; padding:9px 16px; background:rgba(248,113,113,0.06); border-left:3px solid #f87171; border-radius:0 8px 8px 0; text-align:left;">
      <strong style="color:#fff;">Fail-safe rule:</strong> if the underwater workflow fails (no policy match, API error), the surface must always offer a clean human path &mdash; the &ldquo;Create support ticket&rdquo; option here.
    </p>
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

def _trust_gap_card(num: str, name: str, problem: str, solutions: list, ex_label: str, ex_text: str, accent: str) -> str:
    sol_html = "".join(
        f'<li style="font-size:11.5px; color:#cdd5e3; padding:3px 0 3px 0; line-height:1.5;"><strong style="color:#fff;">{title}:</strong> {detail}</li>'
        for title, detail in solutions
    )
    return f"""<section data-title="Trust Gap {num} &middot; {name}">
  <div class="inner">
    <div class="demo-tag tag-debrief">Trust Gap {num}</div>
    <h2>The {name} Gap</h2>
    <div class="subtitle" style="max-width:840px;">{problem}</div>

    <div style="display:grid; grid-template-columns:1.3fr 1fr; gap:14px; max-width:1080px; margin:18px auto 0; align-items:stretch;">

      <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.30); border-radius:14px; padding:14px 18px; text-align:left;">
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
          <div style="font-size:18px;">&#x1F4A1;</div>
          <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:900; color:#34d399; letter-spacing:0.14em; text-transform:uppercase;">Solution &middot; Use explainable / controllable UI</div>
        </div>
        <ul style="margin:0; padding:0 0 0 18px;">
          {sol_html}
        </ul>
      </div>

      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.30); border-radius:14px; padding:14px 18px; text-align:left; display:flex; flex-direction:column; gap:6px;">
        <div style="font-family:'Poppins',sans-serif; font-size:10.5px; font-weight:900; color:#79c0ff; letter-spacing:0.14em; text-transform:uppercase;">&#x2728; Example &middot; {ex_label}</div>
        <p style="font-size:12px; color:#cdd5e3; margin:0; line-height:1.55;">{ex_text}</p>
      </div>
    </div>
  </div>
</section>
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
        "Provides a dedicated sources row and numbered citations throughout the response, allowing users to verify outputs in a single click.",
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
        "Gemini for Google Workspace",
        "Lets users rate suggestions, regenerate alternatives, or refine the prompt in-context &mdash; turning probabilistic mistakes into a conversation.",
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
        "Lets users select a specific part of an AI image and re-generate just that section &mdash; surgical control instead of all-or-nothing.",
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
