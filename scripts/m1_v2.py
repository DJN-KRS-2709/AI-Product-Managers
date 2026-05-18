"""Module 1 deck rebuilt to follow the original PowerPoint flow.

Source of truth: scripts/_out/m1_drive_ai_first_execution_with_prompting.md
(the extraction of the original PPTX). 36 slides, 4 numbered sections.

Voice: solo only. The original "Breakout Group Exercise" for Configure
Juno's System Prompt is converted to an Individual Exercise (this is the
project's solo-only rule — see /skills/course-to-github-pages/voice.md).

This module is wired into gen_module_decks.py via build_module_1 alias.
"""
from __future__ import annotations

# Reuse existing shared helpers from gen_module_decks.
from gen_module_decks import (
    LOGO_REL,
    hero, break_section, qa_section,
    takeaways, extra_practice, _add_builder, applied_work,
)

# ─────────────────────────────────────────────────────────────────────────────
# M1-specific visual section helpers (inline, to keep gen_module_decks small)
# ─────────────────────────────────────────────────────────────────────────────

def section_divider(num: str, title: str) -> str:
    """Full-bleed numbered section transition (e.g. '01 · The AI-First Product Mindset')."""
    return f"""<section class="section-break" data-title="Section {num} &middot; {title}">
  <div class="section-break-inner">
    <div class="lab-title">Section {num}</div>
    <div class="lab-name">{title}</div>
  </div>
</section>
"""


def class_expectations() -> str:
    cards = [
        ("📹", "Cameras On (live cohort)", "Be present and visible if you join the optional live session — keeps interaction valuable."),
        ("⏰", "Arrive On Time", "Respect everyone's time. Sessions start and end on schedule."),
        ("🤝", "Engage Async to Network", "Post in <code>#ai-pm-cohort</code>. Build your professional learning network on Slack."),
        ("🛠️", "Tool Readiness", "Lovable + ChatGPT/Claude accounts active before module 1. We will not stop or restart for setup."),
        ("🎓", "Use Slack", "All cohort communication runs through <code>#ai-pm-cohort</code>. Keeps questions and answers organised."),
        ("🚦", "Class Momentum", "Individual or deep-dive questions are handled async, in-thread, within ~5 days."),
    ]
    cells = "\n".join(
        f'      <div class="expect-card"><div class="expect-icon" style="font-size:36px;">{ic}</div>'
        f'<div class="expect-title">{t}</div><div class="expect-desc">{d}</div></div>'
        for ic, t, d in cards
    )
    return f"""<section class="centered" data-title="Class Expectations">
  <div class="inner">
    <div class="section-label">Ground Rules</div>
    <h2>Class Expectations</h2>
    <div class="expect-grid">
{cells}
    </div>
  </div>
</section>
"""


def introductions() -> str:
    return """<section data-title="Introductions">
  <div class="inner">
    <div class="demo-tag tag-activity">Introductions</div>
    <h2>Get to know your instructor &mdash; and your peers</h2>
    <div class="subtitle">Async, individual. Not a live round-robin.</div>
    <div style="display:flex; gap:20px; margin:24px 0;">
      <div style="flex:1; background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.2); border-radius:14px; padding:24px; text-align:left;">
        <div style="font-size:32px; margin-bottom:8px;">👋</div>
        <div style="font-size:14px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:10px;">Meet Your Instructor</div>
        <ul style="margin:0; padding:0;">
          <li><strong>Background</strong> &mdash; name, location, current role.</li>
          <li><strong>Career path</strong> &mdash; how they got into AI product management.</li>
          <li><strong>Milestones</strong> &mdash; one or two career anchors worth sharing.</li>
        </ul>
      </div>
      <div style="flex:1; background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.2); border-radius:14px; padding:24px; text-align:left;">
        <div style="font-size:32px; margin-bottom:8px;">🧑‍💻</div>
        <div style="font-size:14px; font-weight:800; color:#34d399; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:10px;">Introduce Yourself &mdash; Async</div>
        <ul style="margin:0; padding:0;">
          <li><strong>Who you are</strong> &mdash; name, location, current role.</li>
          <li><strong>Course goal</strong> &mdash; one sentence on what you want from M1&ndash;M6.</li>
          <li><strong>Fun fact</strong> &mdash; a hobby or interest outside work.</li>
        </ul>
        <p style="font-size:13px; color:#8899bb; margin-top:14px;">Post in <code>#ai-pm-cohort</code> with your LinkedIn URL. No live introductions required.</p>
      </div>
    </div>
  </div>
</section>
"""


FINAL_PROJECT_VIDEO_URL = "https://drive.google.com/file/d/11aEB_czorQA6zd7w90Ov-ivWUrOUWu8D/view"
FINAL_PROJECT_VIDEO_EMBED = "https://drive.google.com/file/d/11aEB_czorQA6zd7w90Ov-ivWUrOUWu8D/preview"


def final_project_video() -> str:
    return f"""<section data-title="Final Project Explanation">
  <div class="inner">
    <div class="demo-tag tag-build">Final Project</div>
    <h2>Final Project &mdash; the 4.5 minute briefing</h2>
    <div class="subtitle">Watch the brief, then we&rsquo;ll walk the deliverables.</div>
    <div style="position:relative; width:100%; max-width:880px; margin:24px auto 16px; aspect-ratio:16/9; background:#000; border:1px solid rgba(124,140,255,0.25); border-radius:14px; overflow:hidden; box-shadow:0 18px 48px rgba(0,0,0,0.45);">
      <iframe
        src="{FINAL_PROJECT_VIDEO_EMBED}"
        title="AI Product Management Final Project Overview"
        style="position:absolute; inset:0; width:100%; height:100%; border:0;"
        allow="autoplay; encrypted-media; fullscreen"
        allowfullscreen
        loading="lazy"></iframe>
    </div>
    <p style="font-size:13px; color:#8899bb; max-width:880px; margin:0 auto;">
      Can&rsquo;t see the player? <a href="{FINAL_PROJECT_VIDEO_URL}" target="_blank" rel="noopener" style="color:#60a5fa;">Open the video on Google Drive</a> &mdash; or read the <a href="../Final%20Project%20Brief.html" style="color:#60a5fa;">Final Project Brief</a> and the <a href="../juno-project-template/README.md" style="color:#60a5fa;">project template</a> for the same content in text.
    </p>
  </div>
</section>
"""


def final_project_deliverables() -> str:
    items = [
        ("1", "System Message", "Juno's persona + scope + refusal rules. M1."),
        ("2", "AI Strategy One-Pager &amp; link", "Seven-block strategy doc. M2."),
        ("3", "RAG Architecture &amp; Data Strategy", "Retrieval picks + corpus map. M3."),
        ("4", "UX Design Screenshots from Lovable", "AI Iceberg + trust gaps. M4."),
        ("5", "Agentic Workflow Spec &amp; link", "9-section AWSpec + control panel. M5."),
        ("6", "Evaluation Plan", "3-layer eval stack + human rubric. M6."),
        ("7", "Build Insights", "1 friction · 1 learning · 1 aha &mdash; in the README. M6."),
    ]
    cells = "\n".join(
        f'    <div style="display:flex; gap:18px; align-items:center; padding:16px 20px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; transition:all 0.3s;">'
        f'<div style="width:44px; height:44px; border-radius:10px; flex-shrink:0; display:flex; align-items:center; justify-content:center; font-family:\'Poppins\',sans-serif; font-weight:900; font-size:18px; color:#fff; background:#1241B0;">{n}</div>'
        f'<div style="flex:1; text-align:left;"><div style="font-size:16px; font-weight:700; color:#fff; margin-bottom:2px;">{t}</div>'
        f'<div style="font-size:13px; color:#8899bb;">{d}</div></div></div>'
        for n, t, d in items
    )
    return f"""<section data-title="Final Project Deliverables">
  <div class="inner">
    <div class="demo-tag tag-build">Final Project &mdash; Include</div>
    <h2>The seven deliverables</h2>
    <div class="subtitle">All seven live in your <code>juno-pm/</code> fork. The repo URL is the submission.</div>
    <div style="display:flex; flex-direction:column; gap:10px; margin:24px 0; max-width:780px;">
{cells}
    </div>
    <p style="font-size:13px; color:#8899bb; text-align:center;">Full brief: <a href="../Final%20Project%20Brief.html" style="color:#60a5fa;">Final Project Brief.html</a></p>
  </div>
</section>
"""


def syllabus_visual() -> str:
    items = [
        ("01", "Drive AI-First Execution with Prompting", "Adopt the new AI PM execution language to accelerate delivery and command outputs. Master the systematic use of context, parameters, and prompt engineering to guide AI behavior with precision.", "#3b82f6"),
        ("02", "Validate AI Opportunities and Technical Feasibility", "Become an AI strategist capable of selecting and shaping AI bets that ship and move business metrics. Learn to evaluate feasibility and viability to prioritize features that deliver tangible value.", "#58a6ff"),
        ("03", "Improve AI Product Requirements with RAG Architecture", "Bridge the gap between product specs and RAG systems. Understand how embeddings, vector stores, and retrieval impact product performance to define the technical requirements of a modern AI PRD.", "#d29922"),
        ("04", "Design AI-Native User Experiences", "Design seamless user flows and AI features to unlock new ways for users to interact with your product. Use prototyping to validate experiences and transition from static interfaces to dynamic, intelligent systems.", "#bc8cff"),
        ("05", "Deploy Agentic Systems and Workflows", "Transition from single prompts to autonomous agents and multi-step workflows. Configure reasoning paths and tool triggers to execute complex tasks and drive operational efficiency.", "#f85149"),
        ("06", "Measure AI Quality with Evals and Guardrails", "Replace \"vibe checks\" with systematic evaluation harnesses to ensure production-grade performance. Build robust eval sets and safety guardrails to mitigate risk and embed trust into the user experience.", "#34d399"),
    ]
    cells = "\n".join(
        f'    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-top:3px solid {col}; border-radius:12px; padding:22px; text-align:left;">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-weight:800; font-size:11px; letter-spacing:0.16em; color:{col}; margin-bottom:8px;">MODULE {n}</div>'
        f'<div style="font-size:16px; font-weight:700; color:#fff; line-height:1.3; margin-bottom:8px;">{t}</div>'
        f'<div style="font-size:13px; color:#8899bb; line-height:1.5;">{d}</div></div>'
        for n, t, d, col in items
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


def agenda_4() -> str:
    items = [
        ("01", "The AI-First Product Mindset"),
        ("02", "The Anatomy of a High-Quality Prompt"),
        ("03", "Hands-On Lab: Prompt-to-Prototype Your Copilot with Lovable"),
        ("04", "Prompting as Product Configuration"),
    ]
    cells = "\n".join(
        f'    <div style="display:flex; gap:24px; align-items:center; padding:24px 28px; background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.18); border-radius:14px;">'
        f'<div style="font-family:\'Poppins\',sans-serif; font-weight:900; font-size:42px; color:#60a5fa; min-width:80px; line-height:1;">{n}</div>'
        f'<div style="font-size:20px; font-weight:700; color:#fff; line-height:1.3; text-align:left;">{t}</div></div>'
        for n, t in items
    )
    return f"""<section data-title="Agenda">
  <div class="inner">
    <div class="demo-tag tag-framework">Today</div>
    <h2>Agenda</h2>
    <div style="display:flex; flex-direction:column; gap:14px; margin:24px 0; max-width:760px;">
{cells}
    </div>
  </div>
</section>
"""


def ai_first_reflection() -> str:
    return """<section data-title="AI-First Product Thinking">
  <div class="inner">
    <div class="demo-tag tag-debrief">Solo Reflection &middot; 5 min</div>
    <h2>AI-First Product Thinking</h2>
    <div class="subtitle">Before we dive in, sit with two questions. Post your answers in <code>#ai-pm-cohort</code>.</div>
    <div style="display:flex; flex-direction:column; gap:14px; margin:24px 0; max-width:780px;">
      <div style="background:rgba(96,165,250,0.06); border-left:3px solid #60a5fa; border-radius:0 12px 12px 0; padding:20px 24px; text-align:left;">
        <div style="font-size:13px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:8px;">Question 1</div>
        <p style="font-size:16px; color:#e0e0f0; line-height:1.55;">In an AI-first product, what user signals (like intent or behavior) do you think matter more than a list of rigid feature requirements?</p>
      </div>
      <div style="background:rgba(96,165,250,0.06); border-left:3px solid #60a5fa; border-radius:0 12px 12px 0; padding:20px 24px; text-align:left;">
        <div style="font-size:13px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:8px;">Question 2</div>
        <p style="font-size:16px; color:#e0e0f0; line-height:1.55;">If you could stop writing every single &ldquo;if/then&rdquo; rule for your engineers, what would you stop doing as a PM to focus on higher-level strategy?</p>
      </div>
    </div>
    <p style="font-size:14px; color:#8899bb; margin-top:14px;"><strong>Takeaway:</strong> the shift to AI-first means moving from <em>writing rules</em> to <em>shaping intent</em>. You stop being a feature architect and start being a system governor.</p>
  </div>
</section>
"""


def every_pm_is_ai_pm() -> str:
    return """<section data-title="Every PM is now an AI PM">
  <div class="inner">
    <div class="demo-tag tag-lecture">Frame</div>
    <h2>Every Product Manager is now<br>an AI Product Manager</h2>
    <div class="subtitle" style="font-size:24px; max-width:720px; line-height:1.4;">Whether managing infrastructure, UI, or core features, you are now managing <em>outcomes</em>.</div>
    <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.2); border-radius:14px; padding:24px; margin:24px auto; max-width:760px; text-align:left;">
      <p style="font-size:15px; color:#cdd5e3; line-height:1.7;">In 2023, &ldquo;AI PM&rdquo; meant you built a chatbot or a wrapper. Today the bar is higher. Software has moved from <em>deterministic</em> to <em>probabilistic</em>. Even if you don&rsquo;t think you build AI, your competitors do, and your users now expect personalisation, speed, and intuition. You are managing systems that can surprise you. That changes how you spec, test, and ship. That changes everything.</p>
    </div>
  </div>
</section>
"""



def deterministic_vs_probabilistic() -> str:
    return """<section data-title="From Rules to Probabilities">
  <div class="inner">
    <div class="demo-tag tag-lecture">Mental Model</div>
    <h2>From Rules to Probabilities</h2>
    <div class="subtitle">Deterministic vs. Non-Deterministic Systems &mdash; the single biggest mental model shift.</div>

    <div style="display:grid; grid-template-columns: 1fr 80px 1fr; gap:24px; margin:32px 0; align-items:stretch; max-width:1080px; margin-left:auto; margin-right:auto;">

      <!-- LEFT — Deterministic -->
      <div style="background:linear-gradient(160deg, rgba(100,116,139,0.10), rgba(100,116,139,0.03)); border:1px solid rgba(100,116,139,0.25); border-radius:18px; padding:28px; text-align:left; display:flex; flex-direction:column;">
        <div style="font-size:11px; font-weight:800; color:#94a3b8; text-transform:uppercase; letter-spacing:0.14em; margin-bottom:12px;">Deterministic Systems</div>
        <p style="font-size:14px; color:#cdd5e3; line-height:1.6; margin-bottom:18px;">Most software you&rsquo;ve managed. The code follows rigid pre-written instructions where the same input always produces the exact same output.</p>

        <svg viewBox="0 0 380 110" style="width:100%; height:auto; margin:4px 0 16px; display:block;" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="det-input" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#1f2a44"/>
              <stop offset="100%" stop-color="#0f172a"/>
            </linearGradient>
            <linearGradient id="det-code" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#1e3a8a"/>
              <stop offset="100%" stop-color="#1e40af"/>
            </linearGradient>
            <linearGradient id="det-out" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="rgba(110,231,183,0.18)"/>
              <stop offset="100%" stop-color="rgba(110,231,183,0.06)"/>
            </linearGradient>
            <marker id="arr-det" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#94a3b8"/>
            </marker>
          </defs>
          <rect x="6" y="40" width="92" height="34" rx="17" fill="url(#det-input)" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
          <text x="52" y="62" text-anchor="middle" fill="#cdd5e3" font-family="Poppins, sans-serif" font-size="12" font-weight="700">User Input</text>
          <line x1="102" y1="57" x2="138" y2="57" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arr-det)"/>
          <rect x="142" y="40" width="84" height="34" rx="17" fill="url(#det-code)" stroke="rgba(96,165,250,0.45)" stroke-width="1"/>
          <text x="184" y="62" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="12" font-weight="700">Code</text>
          <line x1="230" y1="57" x2="266" y2="57" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arr-det)"/>
          <rect x="270" y="34" width="106" height="46" rx="14" fill="url(#det-out)" stroke="rgba(110,231,183,0.45)" stroke-width="1"/>
          <text x="323" y="52" text-anchor="middle" fill="#6ee7b7" font-family="Poppins, sans-serif" font-size="10" font-weight="800">100% PREDICTABLE</text>
          <text x="323" y="68" text-anchor="middle" fill="#a7f3d0" font-family="Lato, sans-serif" font-size="9" font-weight="600">output or experience</text>
        </svg>

        <p style="font-size:12px; color:#8899bb; margin-top:auto; padding-top:14px; border-top:1px solid rgba(255,255,255,0.06);"><strong style="color:#cdd5e3;">E.g.</strong> keyword search, login auth, Excel formulas.</p>
      </div>

      <!-- CENTER — VS divider -->
      <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px;">
        <div style="width:2px; flex:1; background:linear-gradient(to bottom, transparent, rgba(96,165,250,0.35), transparent); border-radius:2px;"></div>
        <div style="position:relative; width:64px; height:64px; display:flex; align-items:center; justify-content:center;">
          <div style="position:absolute; inset:-8px; border-radius:50%; background:radial-gradient(circle at center, rgba(96,165,250,0.35), transparent 70%); filter:blur(4px);"></div>
          <div style="position:relative; width:64px; height:64px; border-radius:50%; background:radial-gradient(circle at 35% 30%, #60a5fa 0%, #1e3a8a 70%); border:2px solid rgba(255,255,255,0.35); display:flex; align-items:center; justify-content:center; font-family:'Poppins',sans-serif; font-weight:900; font-size:18px; color:#fff; letter-spacing:0.04em; box-shadow:0 0 28px rgba(96,165,250,0.4), inset 0 1px 4px rgba(255,255,255,0.25);">VS</div>
        </div>
        <div style="width:2px; flex:1; background:linear-gradient(to bottom, transparent, rgba(96,165,250,0.35), transparent); border-radius:2px;"></div>
      </div>

      <!-- RIGHT — Probabilistic -->
      <div style="background:linear-gradient(160deg, rgba(96,165,250,0.12), rgba(96,165,250,0.04)); border:1px solid rgba(96,165,250,0.32); border-radius:18px; padding:28px; text-align:left; display:flex; flex-direction:column; box-shadow:0 0 32px rgba(96,165,250,0.06);">
        <div style="font-size:11px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.14em; margin-bottom:12px;">Probabilistic Systems</div>
        <p style="font-size:14px; color:#cdd5e3; line-height:1.6; margin-bottom:18px;">AI-powered products. The model predicts the most likely next step, where the same input can produce different valid outputs each time.</p>

        <svg viewBox="0 0 380 130" style="width:100%; height:auto; margin:4px 0 16px; display:block;" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="prob-input" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#1f2a44"/>
              <stop offset="100%" stop-color="#0f172a"/>
            </linearGradient>
            <linearGradient id="prob-code" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#3b82f6"/>
              <stop offset="100%" stop-color="#1d4ed8"/>
            </linearGradient>
            <linearGradient id="prob-out" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="rgba(121,192,255,0.22)"/>
              <stop offset="100%" stop-color="rgba(121,192,255,0.06)"/>
            </linearGradient>
            <marker id="arr-prob" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#79c0ff"/>
            </marker>
          </defs>
          <rect x="6" y="48" width="92" height="34" rx="17" fill="url(#prob-input)" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
          <text x="52" y="70" text-anchor="middle" fill="#cdd5e3" font-family="Poppins, sans-serif" font-size="12" font-weight="700">User Input</text>
          <line x1="102" y1="65" x2="138" y2="65" stroke="#79c0ff" stroke-width="1.5" marker-end="url(#arr-prob)"/>
          <rect x="142" y="48" width="84" height="34" rx="17" fill="url(#prob-code)" stroke="rgba(96,165,250,0.6)" stroke-width="1"/>
          <text x="184" y="70" text-anchor="middle" fill="#fff" font-family="Poppins, sans-serif" font-size="12" font-weight="700">Model</text>
          <!-- fan-out arrows -->
          <path d="M 230 60 Q 250 36 264 22" stroke="#79c0ff" stroke-width="1.5" fill="none" marker-end="url(#arr-prob)"/>
          <path d="M 230 65 L 264 65" stroke="#79c0ff" stroke-width="1.5" fill="none" marker-end="url(#arr-prob)"/>
          <path d="M 230 70 Q 250 94 264 108" stroke="#79c0ff" stroke-width="1.5" fill="none" marker-end="url(#arr-prob)"/>
          <!-- three different outputs -->
          <rect x="268" y="6" width="106" height="32" rx="14" fill="url(#prob-out)" stroke="rgba(121,192,255,0.45)" stroke-width="1"/>
          <text x="321" y="26" text-anchor="middle" fill="#79c0ff" font-family="Poppins, sans-serif" font-size="10" font-weight="800">Output A</text>
          <rect x="268" y="49" width="106" height="32" rx="14" fill="url(#prob-out)" stroke="rgba(121,192,255,0.55)" stroke-width="1.5"/>
          <text x="321" y="69" text-anchor="middle" fill="#79c0ff" font-family="Poppins, sans-serif" font-size="10" font-weight="800">Output B</text>
          <rect x="268" y="92" width="106" height="32" rx="14" fill="url(#prob-out)" stroke="rgba(121,192,255,0.45)" stroke-width="1"/>
          <text x="321" y="112" text-anchor="middle" fill="#79c0ff" font-family="Poppins, sans-serif" font-size="10" font-weight="800">Output C</text>
        </svg>

        <p style="font-size:12px; color:#8899bb; margin-top:auto; padding-top:14px; border-top:1px solid rgba(255,255,255,0.06);"><strong style="color:#cdd5e3;">E.g.</strong> semantic (RAG) search, LLM summarisation, image generation.</p>
      </div>

    </div>

    <div style="background:linear-gradient(135deg, rgba(96,165,250,0.10), rgba(124,140,255,0.06)); border:1px solid rgba(96,165,250,0.25); border-left:4px solid #60a5fa; border-radius:12px; padding:18px 26px; max-width:920px; margin:0 auto;">
      <p style="font-size:14px; color:#cdd5e3; line-height:1.6; text-align:center; margin:0;">You can no longer write &ldquo;the output will be X.&rdquo; You define the <strong style="color:#60a5fa;">qualities and guardrails</strong> of an acceptable output.</p>
    </div>
  </div>
</section>
"""


def dual_role() -> str:
    return """<section data-title="The PM's Dual Role">
  <div class="inner">
    <div class="demo-tag tag-lecture">Operating Mode</div>
    <h2>Navigating Uncertainty:<br>The PM&rsquo;s Dual Role</h2>
    <div class="subtitle">Same job. Two operating contexts. Different skills.</div>

    <div style="display:grid; grid-template-columns: 1fr 200px 1fr; gap:0; margin:32px 0; align-items:center; max-width:1140px; margin-left:auto; margin-right:auto;">

      <!-- LEFT card -->
      <div style="background:linear-gradient(160deg, rgba(96,165,250,0.14), rgba(96,165,250,0.04)); border:1px solid rgba(96,165,250,0.32); border-radius:18px; padding:32px; text-align:left; box-shadow:0 0 32px rgba(96,165,250,0.08);">
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:16px;">
          <div style="font-size:40px; line-height:1;">🏗️</div>
          <div style="font-size:13px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.12em;">When Building AI Products</div>
        </div>
        <p style="font-size:15px; color:#cdd5e3; line-height:1.65; margin:0 0 14px;">When scoping requirements for stakeholders and engineering, you can&rsquo;t define a single exact output &mdash; the system is designed to change.</p>
        <div style="height:1px; background:linear-gradient(to right, rgba(96,165,250,0.4), transparent); margin:14px 0;"></div>
        <p style="font-size:14px; color:#8899bb; line-height:1.6; margin:0;">Your PRD must evolve to specify <strong style="color:#cdd5e3;">qualities and guardrails</strong> of an acceptable response &mdash; ensuring the team builds a safe, reliable AI experience. You&rsquo;re a city planner, not a building architect.</p>
      </div>

      <!-- CENTRE — orb cluster + outward arrows -->
      <div style="position:relative; height:340px; display:flex; align-items:center; justify-content:center;">
        <svg viewBox="0 0 200 340" style="width:200px; height:340px; display:block;" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="orb-deep" cx="40%" cy="35%">
              <stop offset="0%" stop-color="#bcd9ff" stop-opacity="0.95"/>
              <stop offset="35%" stop-color="#3b82f6" stop-opacity="0.85"/>
              <stop offset="70%" stop-color="#1e3a8a" stop-opacity="0.75"/>
              <stop offset="100%" stop-color="#0a1934" stop-opacity="0.4"/>
            </radialGradient>
            <radialGradient id="orb-mid" cx="40%" cy="35%">
              <stop offset="0%" stop-color="#79c0ff" stop-opacity="0.55"/>
              <stop offset="60%" stop-color="#1e40af" stop-opacity="0.4"/>
              <stop offset="100%" stop-color="#0a1934" stop-opacity="0"/>
            </radialGradient>
            <radialGradient id="orb-halo" cx="50%" cy="50%">
              <stop offset="0%" stop-color="rgba(96,165,250,0.3)"/>
              <stop offset="100%" stop-color="rgba(96,165,250,0)"/>
            </radialGradient>
            <marker id="arr-l" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#cdd5e3"/>
            </marker>
            <marker id="arr-r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#cdd5e3"/>
            </marker>
          </defs>
          <!-- Outer halo (subtle glow) -->
          <ellipse cx="100" cy="170" rx="100" ry="160" fill="url(#orb-halo)"/>
          <!-- Three nested ellipses creating depth -->
          <ellipse cx="100" cy="170" rx="78" ry="148" fill="url(#orb-mid)" opacity="0.5"/>
          <ellipse cx="100" cy="170" rx="56" ry="124" fill="url(#orb-deep)" opacity="0.75"/>
          <ellipse cx="100" cy="170" rx="34" ry="100" fill="url(#orb-mid)" opacity="0.85"/>
          <ellipse cx="100" cy="170" rx="16" ry="76" fill="url(#orb-deep)" opacity="1"/>
          <!-- Outward arrows: AI is centre, role bifurcates -->
          <line x1="84" y1="170" x2="20" y2="170" stroke="#cdd5e3" stroke-width="1.5" marker-end="url(#arr-l)"/>
          <line x1="116" y1="170" x2="180" y2="170" stroke="#cdd5e3" stroke-width="1.5" marker-end="url(#arr-r)"/>
        </svg>
        <div style="position:absolute; bottom:18px; left:50%; transform:translateX(-50%); font-family:'Poppins',sans-serif; font-size:10px; font-weight:800; color:#8899bb; letter-spacing:0.18em; text-transform:uppercase; white-space:nowrap;">AI uncertainty</div>
      </div>

      <!-- RIGHT card -->
      <div style="background:linear-gradient(160deg, rgba(52,211,153,0.14), rgba(52,211,153,0.04)); border:1px solid rgba(52,211,153,0.32); border-radius:18px; padding:32px; text-align:left; box-shadow:0 0 32px rgba(52,211,153,0.08);">
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:16px;">
          <div style="font-size:40px; line-height:1;">⚡</div>
          <div style="font-size:13px; font-weight:800; color:#34d399; text-transform:uppercase; letter-spacing:0.12em;">When Using AI in Workflows</div>
        </div>
        <p style="font-size:15px; color:#cdd5e3; line-height:1.65; margin:0 0 14px;">The AI&rsquo;s variability can be a source of creativity &mdash; but it means you are responsible for critically evaluating each unique output.</p>
        <div style="height:1px; background:linear-gradient(to left, rgba(52,211,153,0.4), transparent); margin:14px 0;"></div>
        <p style="font-size:14px; color:#8899bb; line-height:1.6; margin:0;">You guide the AI toward the desired result through <strong style="color:#cdd5e3;">prompt iteration</strong> and your strategic judgment. The interaction is a conversation, not a command.</p>
      </div>

    </div>

    <p style="font-size:13px; color:#8899bb; text-align:center; margin-top:8px;">Your job is to <strong style="color:#cdd5e3;">guide AI</strong> toward the desired result by iterating on your prompts and applying your strategic judgment.</p>
  </div>
</section>
"""


def role_evolved_quadrants() -> str:
    items = [
        ("1", "Assess the AI-Ability of the Problem", "Validate if the problem truly needs a probabilistic solution. Avoid using AI where a deterministic rule delivers better predictability and value.", "#3b82f6"),
        ("2", "Own the &ldquo;Vibe&rdquo; & Trade-offs", "Configure the specific balance of cost, latency, and quality. Define the model's behaviour through parameters &mdash; not abstract concepts.", "#79c0ff"),
        ("3", "Define the Failure State", "Design explicitly for variability. Create guardrails, feedback loops, and fallback UIs to maintain trust when the AI inevitably fails.", "#d29922"),
        ("4", "Prototype as Spec", "Replace static requirements with functioning prompts. Demonstrate intent and prove technical feasibility through hands-on configuration.", "#34d399"),
    ]
    cells = "\n".join(
        f'    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:26px; text-align:left; transition:all 0.3s; position:relative; overflow:hidden;">'
        f'<div style="position:absolute; top:0; left:0; right:0; height:3px; background:{col};"></div>'
        f'<div style="display:flex; align-items:center; gap:16px; margin-bottom:12px;">'
        f'<div style="width:44px; height:44px; border-radius:10px; background:{col}; color:#fff; display:flex; align-items:center; justify-content:center; font-family:\'Poppins\',sans-serif; font-weight:900; font-size:20px; flex-shrink:0;">{n}</div>'
        f'<div style="font-size:17px; font-weight:700; color:#fff; line-height:1.25;">{t}</div></div>'
        f'<p style="font-size:14px; color:#8899bb; line-height:1.6;">{d}</p></div>'
        for n, t, d, col in items
    )
    return f"""<section data-title="How the AI-Era PM Role Has Evolved">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>How the AI-Era PM Role Has Evolved</h2>
    <div class="subtitle">PMs must move from defining deterministic specs to owning the outcomes of probabilistic systems.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:24px 0;">
{cells}
    </div>
  </div>
</section>
"""


def pm_toolkit() -> str:
    items = [
        ("🔍", "Research &amp; Discovery", "Synthesise customer feedback, competitor activity, market signals."),
        ("📋", "PRDs &amp; Documentation", "First drafts of PRDs, user stories, acceptance criteria &mdash; you refine."),
        ("🗺️", "Roadmapping &amp; Prioritisation", "Cluster customer feedback, feature requests, support tickets into themes."),
        ("✏️", "Prototyping &amp; Design", "Turn rough ideas into wireframes or interactive mockups in minutes."),
        ("🧪", "Experimentation &amp; Insights", "Generate test hypotheses, analyse results, surface user behaviour patterns."),
        ("📣", "Messaging &amp; Go-to-Market", "Draft messaging pillars, campaign copy, FAQs, sales enablement."),
        ("🎤", "Presentations &amp; Enablement", "Generate decks, battlecards, training material &mdash; you keep the narrative."),
    ]
    cells = "\n".join(
        f'    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:20px; text-align:center;">'
        f'<div style="font-size:40px; margin-bottom:10px;">{ic}</div>'
        f'<div style="font-size:14px; font-weight:700; color:#fff; margin-bottom:6px; line-height:1.25;">{t}</div>'
        f'<div style="font-size:12.5px; color:#8899bb; line-height:1.5;">{d}</div></div>'
        for ic, t, d in items
    )
    return f"""<section data-title="A PM's AI Toolkit">
  <div class="inner">
    <div class="demo-tag tag-lecture">Directory</div>
    <h2>A PM&rsquo;s AI Toolkit</h2>
    <div class="subtitle">Seven categories of AI capabilities you plug into PM work. AI is your co-pilot &mdash; you keep the judgment.</div>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:14px; margin:24px 0;">
{cells}
    </div>
  </div>
</section>
"""


def prompt_anatomy_4d() -> str:
    items = [
        ("🎭", "ROLE", "Defines the model's expertise.", "&ldquo;Act as a senior B2B product researcher&rdquo;", "#3b82f6"),
        ("🎯", "TASK", "Defines the specific goal.", "&ldquo;Synthesise insights from raw feedback&rdquo;", "#79c0ff"),
        ("🚧", "CONSTRAINTS", "Defines the guardrails.", "&ldquo;Do not speculate. Use only the provided transcript.&rdquo;", "#d29922"),
        ("📐", "FORMAT", "Defines the output structure.", "&ldquo;Return a markdown table with headers.&rdquo;", "#34d399"),
    ]
    cells = "\n".join(
        f'    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:24px; text-align:left; position:relative; overflow:hidden;">'
        f'<div style="position:absolute; top:0; left:0; right:0; height:3px; background:{col};"></div>'
        f'<div style="display:flex; align-items:center; gap:14px; margin-bottom:10px;">'
        f'<div style="font-size:36px;">{ic}</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:18px; font-weight:900; color:{col}; letter-spacing:0.04em;">{t}</div></div>'
        f'<p style="font-size:14px; color:#cdd5e3; line-height:1.55; margin-bottom:10px;">{d}</p>'
        f'<div style="background:rgba(0,0,0,0.25); border-radius:8px; padding:12px; font-family:\'IBM Plex Mono\', monospace; font-size:12px; color:#cdd5e3; line-height:1.5;">{ex}</div></div>'
        for ic, t, d, ex, col in items
    )
    return f"""<section data-title="The Anatomy of a High-Quality Prompt">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>The Anatomy of a High-Quality Prompt</h2>
    <div class="subtitle">Ambiguity creates inconsistency. Every prompt must explicitly define these four dimensions.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:24px 0;">
{cells}
    </div>
    <p style="font-size:13px; color:#8899bb; text-align:center; margin-top:8px;">🦾 <em>Model configuration</em> &mdash; structure reduces randomness.</p>
  </div>
</section>
"""



def cameras_on() -> str:
    return """<section class="centered" data-title="Cameras On">
  <div class="inner">
    <div style="font-size:80px; margin-bottom:16px;">📹</div>
    <div class="section-label" style="color:#f87171;">Reminder</div>
    <h2>Cameras On (live cohort)</h2>
    <div class="subtitle" style="max-width:560px;">It&rsquo;s always better to see your face. Be present and visible to stay engaged and keep interactions valuable. Async-only? You&rsquo;re excused.</div>
  </div>
</section>
"""


def prompt_layers_stack() -> str:
    return """<section data-title="Prompt Layers for Product Configuration">
  <div class="inner">
    <div class="demo-tag tag-framework">Framework</div>
    <h2>Prompt Layers for Product Configuration</h2>
    <div class="subtitle">Three layers. Configure all three or you&rsquo;re just wrapping a chat box.</div>
    <div style="display:flex; flex-direction:column; gap:14px; margin:28px auto; max-width:880px;">
      <div style="background:linear-gradient(135deg, rgba(124,140,255,0.12), rgba(124,140,255,0.04)); border:1px solid rgba(124,140,255,0.3); border-radius:14px; padding:22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:10px;">
          <div style="font-size:32px;">🛠️</div>
          <div>
            <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:800; color:#bcb1ff; letter-spacing:0.12em;">TOP LAYER</div>
            <div style="font-size:18px; font-weight:700; color:#fff;">Tools and Functions</div>
          </div>
        </div>
        <p style="font-size:14px; color:#cdd5e3; line-height:1.6;">Shapes what the model can <em>do</em>, beyond text generation.</p>
        <div style="margin-top:10px; font-family:'IBM Plex Mono', monospace; font-size:12px; color:#bcb1ff; background:rgba(0,0,0,0.25); border-radius:8px; padding:10px 14px;"><strong>Example:</strong> [Calculator Tool], [CRM Search Tool], [API call]</div>
      </div>
      <div style="background:linear-gradient(135deg, rgba(96,165,250,0.12), rgba(96,165,250,0.04)); border:1px solid rgba(96,165,250,0.3); border-radius:14px; padding:22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:10px;">
          <div style="font-size:32px;">💬</div>
          <div>
            <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:800; color:#79c0ff; letter-spacing:0.12em;">MIDDLE LAYER</div>
            <div style="font-size:18px; font-weight:700; color:#fff;">User Prompts</div>
          </div>
        </div>
        <p style="font-size:14px; color:#cdd5e3; line-height:1.6;">Expresses intent based on dynamic, variable user input. The trigger for each system run.</p>
        <div style="margin-top:10px; font-family:'IBM Plex Mono', monospace; font-size:12px; color:#79c0ff; background:rgba(0,0,0,0.25); border-radius:8px; padding:10px 14px;"><strong>Example:</strong> &ldquo;Analyse this churn report for insights.&rdquo;</div>
      </div>
      <div style="background:linear-gradient(135deg, rgba(52,211,153,0.12), rgba(52,211,153,0.04)); border:1px solid rgba(52,211,153,0.3); border-radius:14px; padding:22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:10px;">
          <div style="font-size:32px;">⚙️</div>
          <div>
            <div style="font-family:'Poppins',sans-serif; font-size:11px; font-weight:800; color:#34d399; letter-spacing:0.12em;">FOUNDATIONAL LAYER</div>
            <div style="font-size:18px; font-weight:700; color:#fff;">System Messages</div>
          </div>
        </div>
        <p style="font-size:14px; color:#cdd5e3; line-height:1.6;">Defines global rules &mdash; persona, boundaries, safety protocols. The model&rsquo;s &ldquo;constitution.&rdquo;</p>
        <div style="margin-top:10px; font-family:'IBM Plex Mono', monospace; font-size:12px; color:#34d399; background:rgba(0,0,0,0.25); border-radius:8px; padding:10px 14px;"><strong>Example:</strong> &ldquo;You are a Senior Data Analyst. Output only JSON.&rdquo;</div>
      </div>
    </div>
  </div>
</section>
"""


def strategy_matrix_3() -> str:
    items = [
        ("⚡", "Zero-Shot", "Rapid Ideation", "Giving the AI a task with no examples, relying solely on your instructions.", "Generate hypotheses, interview scripts, broad market summaries when you need volume over precision.", "&ldquo;List 10 potential user problems for a new pet sitting app.&rdquo;", "#3b82f6"),
        ("📑", "Few-Shot", "Output Consistency", "Providing 2&ndash;3 examples to guide strict structure or style.", "Acceptance criteria, JSON schemas, status updates that must match team templates exactly.", "&ldquo;Here are 3 examples of our user stories. Write a new story for the &lsquo;Export PDF&rsquo; feature following this exact format.&rdquo;", "#79c0ff"),
        ("🧠", "Chain-of-Thought", "Complex Logic", "Prompting the AI to explain its reasoning step-by-step before answering.", "Sizing markets, analysing feedback, prioritisation. Forces the AI to &ldquo;show its work.&rdquo;", "&ldquo;Think step-by-step. First, estimate the total addressable market (TAM). Then apply our segment filters to calculate the SAM.&rdquo;", "#34d399"),
    ]
    cells = "\n".join(
        f'    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:22px; text-align:left; position:relative; overflow:hidden;">'
        f'<div style="position:absolute; top:0; left:0; right:0; height:3px; background:{col};"></div>'
        f'<div style="display:flex; align-items:center; gap:12px; margin-bottom:10px;">'
        f'<div style="font-size:32px;">{ic}</div>'
        f'<div><div style="font-size:11px; font-weight:800; color:{col}; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:2px;">{tag}</div>'
        f'<div style="font-size:18px; font-weight:700; color:#fff;">{t}</div></div></div>'
        f'<p style="font-size:13px; color:#cdd5e3; line-height:1.5; margin-bottom:10px;"><strong>Definition.</strong> {d}</p>'
        f'<p style="font-size:13px; color:#cdd5e3; line-height:1.5; margin-bottom:12px;"><strong>Use case.</strong> {u}</p>'
        f'<div style="background:rgba(0,0,0,0.25); border-radius:8px; padding:10px 12px; font-family:\'IBM Plex Mono\', monospace; font-size:11.5px; color:#cdd5e3; line-height:1.5;"><strong>Example.</strong> {ex}</div></div>'
        for ic, t, tag, d, u, ex, col in items
    )
    return f"""<section data-title="The Prompting Strategy Matrix">
  <div class="inner">
    <div class="demo-tag tag-framework">Core Techniques</div>
    <h2>The Prompting Strategy Matrix</h2>
    <div class="subtitle">As a PM, you&rsquo;re choosing a configuration based on the problem. Three strategies. One trade-off triangle.</div>
    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:14px; margin:24px 0;">
{cells}
    </div>
  </div>
</section>
"""


def fewshot_compare() -> str:
    return """<section data-title="Few-Shot Prompting in Practice">
  <div class="inner">
    <div class="demo-tag tag-lecture">Few-Shot</div>
    <h2>Few-Shot Prompting</h2>
    <div class="subtitle">Instructions tell the model <em>what to do</em>. Examples show it <em>how</em>.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin:24px 0;">
      <div style="background:rgba(248,113,113,0.06); border:1px solid rgba(248,113,113,0.25); border-radius:14px; padding:22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
          <div style="font-size:24px;">⚠️</div>
          <div style="font-size:14px; font-weight:800; color:#f87171; text-transform:uppercase; letter-spacing:0.08em;">Instruction Only</div>
        </div>
        <div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; margin-bottom:6px;">The Prompt</div>
        <div style="background:rgba(0,0,0,0.3); border-radius:8px; padding:12px; font-family:'IBM Plex Mono', monospace; font-size:12px; color:#cdd5e3; line-height:1.5; margin-bottom:12px;">&ldquo;Classify this user feedback as a Feature Request, Bug, or Praise: &lsquo;The reports load slowly&rsquo;&rdquo;</div>
        <div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; margin-bottom:6px;">The Result</div>
        <p style="font-size:13px; color:#cdd5e3; line-height:1.55; margin-bottom:12px;">&ldquo;The reports load slowly&rdquo; is a <strong>Bug</strong>.</p>
        <div style="font-size:12px; font-weight:800; color:#f87171; text-transform:uppercase; margin-bottom:6px;">The Failure</div>
        <p style="font-size:12.5px; color:#8899bb; line-height:1.55;">Without examples, the model guesses your criteria. It might call &ldquo;Login is slow&rdquo; a Bug, while you consider it a Feature Request for performance.</p>
      </div>
      <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:14px; padding:22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
          <div style="font-size:24px;">✅</div>
          <div style="font-size:14px; font-weight:800; color:#34d399; text-transform:uppercase; letter-spacing:0.08em;">Instruction + Data</div>
        </div>
        <div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; margin-bottom:6px;">The Prompt</div>
        <div style="background:rgba(0,0,0,0.3); border-radius:8px; padding:12px; font-family:'IBM Plex Mono', monospace; font-size:12px; color:#cdd5e3; line-height:1.6; margin-bottom:12px;">&ldquo;Classify this user feedback as a Feature Request, Bug, or Praise. Use these examples:<br>1. &lsquo;Login is slow&rsquo; → Feature Request<br>2. &lsquo;Login returns 404&rsquo; → Bug<br>3. &lsquo;Love the login!&rsquo; → Praise<br>Input: &lsquo;The reports load slowly.&rsquo;&rdquo;</div>
        <div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; margin-bottom:6px;">The Result</div>
        <p style="font-size:13px; color:#cdd5e3; line-height:1.55;">The model matches &ldquo;reports load slowly&rdquo; to &ldquo;Login is slow&rdquo; and correctly tags it: <strong style="color:#34d399;">Feature Request</strong>.</p>
      </div>
    </div>
    <p style="font-size:13px; color:#8899bb; text-align:center;">Zero-Shot is for <em>creativity</em>. Few-Shot is for <em>compliance</em>.</p>
  </div>
</section>
"""


def cot_compare() -> str:
    return """<section data-title="Chain-of-Thought Prompting in Practice">
  <div class="inner">
    <div class="demo-tag tag-lecture">Chain-of-Thought</div>
    <h2>Chain-of-Thought (CoT) Prompting</h2>
    <div class="subtitle">Pattern matching isn&rsquo;t enough for logic. You need reasoning.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin:24px 0;">
      <div style="background:rgba(248,113,113,0.06); border:1px solid rgba(248,113,113,0.25); border-radius:14px; padding:22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
          <div style="font-size:24px;">⚠️</div>
          <div style="font-size:14px; font-weight:800; color:#f87171; text-transform:uppercase; letter-spacing:0.08em;">Prediction Only</div>
        </div>
        <div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; margin-bottom:6px;">The Prompt</div>
        <div style="background:rgba(0,0,0,0.3); border-radius:8px; padding:12px; font-family:'IBM Plex Mono', monospace; font-size:12px; color:#cdd5e3; line-height:1.6; margin-bottom:12px;">&ldquo;Is &lsquo;Add AI Avatars&rsquo; a high priority feature? (Context: our Q3 goal is reducing churn.)&rdquo;</div>
        <div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; margin-bottom:6px;">The Result</div>
        <p style="font-size:13px; color:#cdd5e3; line-height:1.55; margin-bottom:12px;">&ldquo;Priority: <strong>High</strong>. AI features are trending and usually drive user engagement.&rdquo;</p>
        <div style="font-size:12px; font-weight:800; color:#f87171; text-transform:uppercase; margin-bottom:6px;">The Failure</div>
        <p style="font-size:12.5px; color:#8899bb; line-height:1.55;">The model relies on surface-level patterns. It sees &ldquo;AI&rdquo; (a popular topic) and predicts &ldquo;High Priority&rdquo;, ignoring your specific churn goal.</p>
      </div>
      <div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:14px; padding:22px; text-align:left;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
          <div style="font-size:24px;">✅</div>
          <div style="font-size:14px; font-weight:800; color:#34d399; text-transform:uppercase; letter-spacing:0.08em;">Prediction + Reasoning</div>
        </div>
        <div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; margin-bottom:6px;">The Prompt</div>
        <div style="background:rgba(0,0,0,0.3); border-radius:8px; padding:12px; font-family:'IBM Plex Mono', monospace; font-size:12px; color:#cdd5e3; line-height:1.6; margin-bottom:12px;">&ldquo;Is &lsquo;Add AI Avatars&rsquo; a high priority feature? Think step-by-step:<br>1. Define the primary driver of our churn.<br>2. Evaluate if &lsquo;AI Avatars&rsquo; directly solves that driver.<br>3. Assign priority based only on that evaluation.&rdquo;</div>
        <div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; margin-bottom:6px;">The Result</div>
        <p style="font-size:13px; color:#cdd5e3; line-height:1.55;">&ldquo;Step 1: Churn is primarily driven by high costs. Step 2: AI Avatars add value but do not reduce cost. <strong style="color:#34d399;">Conclusion: Priority Low.</strong>&rdquo;</p>
      </div>
    </div>
    <p style="font-size:13px; color:#8899bb; text-align:center;">Few-Shot for <em>format</em>. Chain-of-Thought for <em>analysis, math, logic, priority</em>.</p>
  </div>
</section>
"""


def hyperparameters_3() -> str:
    items = [
        ("🌡️", "Temperature", "The Risk Slider", "Adjusts response randomness to control creativity or precision.", "Low (0.2) → product logic, code, data. High (0.7+) → ideation, chat.", "Spotify uses low temp for support summaries (facts). Netflix high for title brainstorms (wild ideas).", "#f87171"),
        ("🎯", "Top P", "The Quality Bar", "Limits the model to only the top % of likely words to control vocabulary quality.", "Cuts off &ldquo;weird&rdquo; or long-tail hallucinations without making outputs boring.", "Salesforce uses lower values for legal content. Netflix expands it for diverse storytelling.", "#79c0ff"),
        ("💰", "Max Tokens", "The Budget Knob", "Sets a hard limit on token output to control latency and cost.", "Always set a limit. Prevents rambling, infinite loops, wasted API budget.", "Spotify forces concise summaries. Salesforce compresses CRM notes. Figma stops repetitive UI copy.", "#34d399"),
    ]
    cells = "\n".join(
        f'    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:24px; text-align:left; position:relative; overflow:hidden;">'
        f'<div style="position:absolute; top:0; left:0; right:0; height:3px; background:{col};"></div>'
        f'<div style="display:flex; align-items:center; gap:12px; margin-bottom:10px;">'
        f'<div style="font-size:36px;">{ic}</div>'
        f'<div><div style="font-size:11px; font-weight:800; color:{col}; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:2px;">{tag}</div>'
        f'<div style="font-size:18px; font-weight:700; color:#fff;">{t}</div></div></div>'
        f'<p style="font-size:13.5px; color:#cdd5e3; line-height:1.55; margin-bottom:10px;">{d}</p>'
        f'<p style="font-size:13px; color:#8899bb; line-height:1.55; margin-bottom:10px;"><strong style="color:#cdd5e3;">When.</strong> {u}</p>'
        f'<div style="font-size:12px; color:#8899bb; line-height:1.5; padding-top:10px; border-top:1px solid rgba(255,255,255,0.06);"><strong style="color:#cdd5e3;">In the wild.</strong> {ex}</div></div>'
        for ic, t, tag, d, u, ex, col in items
    )
    return f"""<section data-title="From Strategy to Spec — Model Configuration">
  <div class="inner">
    <div class="demo-tag tag-framework">Hyperparameters</div>
    <h2>From Strategy to Spec: Model Configuration</h2>
    <div class="subtitle">Your prompt is the software. These settings are the operating environment.</div>
    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:14px; margin:24px 0;">
{cells}
    </div>
    <p style="font-size:13px; color:#8899bb; text-align:center; margin-top:8px;"><strong>Pro tip.</strong> Don&rsquo;t guess. Run a parameter sweep &mdash; test multiple settings, pick the one that aligns with your product goals.</p>
  </div>
</section>
"""


def fine_tuning_card() -> str:
    return """<section data-title="The Role of Fine-Tuning">
  <div class="inner">
    <div class="demo-tag tag-lecture">Fine-Tuning</div>
    <h2>The Role of Fine-Tuning</h2>
    <div class="subtitle">Behaviour, not knowledge.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin:24px 0;">
      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:14px; padding:24px; text-align:left;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
          <div style="font-size:32px;">🧬</div>
          <div style="font-size:15px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.08em;">Behaviour, not knowledge</div>
        </div>
        <p style="font-size:14px; color:#cdd5e3; line-height:1.6; margin-bottom:10px;">Fine-tuning bakes instructions directly into the model&rsquo;s weights. Unlike Few-Shot, this eliminates the need to send long, expensive examples with every API call &mdash; reducing latency and cost.</p>
        <div style="background:rgba(0,0,0,0.25); border-radius:8px; padding:12px 14px; font-size:12.5px; color:#cdd5e3; line-height:1.55; margin-top:10px;"><strong>GitHub Copilot.</strong> Not just &ldquo;prompted&rdquo; to write code. Fine-tuned on billions of lines to instinctively understand syntax, style, and logic patterns &mdash; without specific instructions.</div>
      </div>
      <div style="background:rgba(248,113,113,0.06); border:1px solid rgba(248,113,113,0.25); border-radius:14px; padding:24px; text-align:left;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
          <div style="font-size:32px;">⚠️</div>
          <div style="font-size:15px; font-weight:800; color:#f87171; text-transform:uppercase; letter-spacing:0.08em;">The Knowledge Misconception</div>
        </div>
        <p style="font-size:14px; color:#cdd5e3; line-height:1.6; margin-bottom:10px;">Don&rsquo;t use fine-tuning to teach the model your proprietary data or policies. Models are probabilistic engines, not databases &mdash; they cannot &ldquo;look up&rdquo; facts and will hallucinate when uncertain.</p>
        <div style="background:rgba(0,0,0,0.25); border-radius:8px; padding:12px 14px; font-size:12.5px; color:#cdd5e3; line-height:1.55; margin-top:10px;"><strong>To stop hallucinations on data.</strong> You need <strong style="color:#f87171;">Retrieval Augmented Generation (RAG)</strong>. Coming up in Module 3.</div>
      </div>
    </div>
    <p style="font-size:13px; color:#8899bb; text-align:center; margin-top:6px;"><strong>Pro tip.</strong> Use fine-tuning to bake in <em>skills</em>, not <em>facts</em>.</p>
  </div>
</section>
"""


def optimization_decision_3step() -> str:
    items = [
        ("1", "&ldquo;The model gives inconsistent answers&rdquo;", "Few-Shot Prompting", "If the model oscillates between good and bad outputs, it usually just needs clearer guardrails or examples. Fastest, cheapest fix.", "#3b82f6"),
        ("2", "&ldquo;The model doesn&rsquo;t know our specific data&rdquo;", "RAG", "If the user asks about &ldquo;User X&rsquo;s refund status&rdquo;, the model can&rsquo;t guess. It needs to <em>read your database</em>. No training will fix this.", "#d29922"),
        ("3", "&ldquo;The model sounds like a robot, not our brand&rdquo;", "Fine-Tuning", "If content is correct but the vibe is wrong (too formal, wrong code syntax), retrain the model&rsquo;s weights to mimic your voice or format.", "#34d399"),
    ]
    cells = "\n".join(
        f'    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:22px; text-align:left; position:relative; overflow:hidden;">'
        f'<div style="position:absolute; top:0; left:0; bottom:0; width:4px; background:{col};"></div>'
        f'<div style="display:flex; align-items:center; gap:14px; margin-bottom:12px;">'
        f'<div style="width:36px; height:36px; border-radius:50%; background:{col}; color:#fff; display:flex; align-items:center; justify-content:center; font-family:\'Poppins\',sans-serif; font-weight:900; font-size:16px; flex-shrink:0;">{n}</div>'
        f'<div style="flex:1;"><div style="font-size:12px; font-weight:800; color:#8899bb; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:2px;">Symptom</div>'
        f'<div style="font-size:15px; color:#fff; line-height:1.4; font-style:italic;">{sym}</div></div></div>'
        f'<div style="background:rgba(0,0,0,0.25); border-radius:8px; padding:14px 16px; margin-bottom:10px;">'
        f'<div style="font-size:11px; font-weight:800; color:{col}; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:6px;">Tool</div>'
        f'<div style="font-family:\'Poppins\',sans-serif; font-size:18px; font-weight:800; color:#fff;">{tool}</div></div>'
        f'<p style="font-size:13px; color:#8899bb; line-height:1.55;">{d}</p></div>'
        for n, sym, tool, d, col in items
    )
    return f"""<section data-title="The Optimisation Decision Framework">
  <div class="inner">
    <div class="demo-tag tag-framework">Decision Framework</div>
    <h2>🔎 The Optimisation Decision Framework</h2>
    <div class="subtitle">Diagnose the problem to pick the right tool. PMs must triage &mdash; not say yes to &ldquo;fine-tune it&rdquo;.</div>
    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:14px; margin:24px 0;">
{cells}
    </div>
    <p style="font-size:13px; color:#8899bb; text-align:center; margin-top:6px;"><strong>Coming up.</strong> A deep technical dive on RAG in Module 3.</p>
  </div>
</section>
"""


def prds_to_prompts() -> str:
    return """<section data-title="From PRDs to Prompts">
  <div class="inner">
    <div class="demo-tag tag-framework">Workflow Shift</div>
    <h2>From PRDs to Prompts</h2>
    <div class="subtitle">Your prompt is the prototype. The interpretation gap between Product and Engineering closes.</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin:24px 0;">
      <div style="background:rgba(100,116,139,0.08); border:1px solid rgba(100,116,139,0.2); border-radius:14px; padding:24px; text-align:left;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:14px;">
          <div style="font-size:32px;">📄</div>
          <div style="font-size:14px; font-weight:800; color:#94a3b8; text-transform:uppercase; letter-spacing:0.1em;">Old Way &middot; Paper Spec</div>
        </div>
        <ul style="margin:0; padding:0 0 0 4px; list-style:none;">
          <li style="font-size:14px; color:#cdd5e3; line-height:1.55; padding:8px 0; border-bottom:1px dashed rgba(255,255,255,0.08);">A static text document describing desired behaviour, like &ldquo;the chatbot should be helpful and polite.&rdquo;</li>
          <li style="font-size:14px; color:#cdd5e3; line-height:1.55; padding:8px 0; border-bottom:1px dashed rgba(255,255,255,0.08);">PMs handed their requirements doc to Engineering to interpret it.</li>
          <li style="font-size:14px; color:#cdd5e3; line-height:1.55; padding:8px 0;">You wait 2 weeks and find &ldquo;polite&rdquo; means different things to you, Eng, and the model.</li>
        </ul>
      </div>
      <div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:14px; padding:24px; text-align:left;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:14px;">
          <div style="font-size:32px;">📦</div>
          <div style="font-size:14px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.1em;">New Way &middot; Prompt Spec</div>
        </div>
        <ul style="margin:0; padding:0 0 0 4px; list-style:none;">
          <li style="font-size:14px; color:#cdd5e3; line-height:1.55; padding:8px 0; border-bottom:1px dashed rgba(255,255,255,0.08);">A working system prompt using the four prompt anatomy configurations and prompting techniques.</li>
          <li style="font-size:14px; color:#cdd5e3; line-height:1.55; padding:8px 0; border-bottom:1px dashed rgba(255,255,255,0.08);">PMs build the logic in a playground and test edge cases immediately.</li>
          <li style="font-size:14px; color:#cdd5e3; line-height:1.55; padding:8px 0;">You hand the working prompt to Eng and prove the logic works &mdash; no guessing required.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""


def resources_templates() -> str:
    return """<section data-title="Resources &amp; Templates">
  <div class="inner">
    <div class="demo-tag tag-build">Resources</div>
    <h2>Resources &amp; Templates</h2>
    <div class="subtitle">Bonus &mdash; everything you need is in the repo.</div>
    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:16px; margin:24px 0; max-width:920px; margin-left:auto; margin-right:auto;">
      <a href="../juno-project-template/01-prompting/lab-walkthrough.md" style="text-decoration:none;"><div style="background:rgba(96,165,250,0.06); border:1px solid rgba(96,165,250,0.25); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">Hands-On Lab Walkthrough</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">Module 1 Lab Guide</div>
        <div style="font-size:13px; color:#8899bb;">→ View resource</div>
      </div></a>
      <a href="../Final%20Project%20Brief.html" style="text-decoration:none;"><div style="background:rgba(124,140,255,0.06); border:1px solid rgba(124,140,255,0.25); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#bcb1ff; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">AI PM Certification</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">Final Project Brief &amp; Deliverables</div>
        <div style="font-size:13px; color:#8899bb;">→ View resource</div>
      </div></a>
      <a href="../juno-project-template/" style="text-decoration:none;"><div style="background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.25); border-radius:14px; padding:22px; text-align:left; transition:all 0.3s; height:100%;">
        <div style="font-size:11px; font-weight:800; color:#34d399; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">AI PM Certification</div>
        <div style="font-size:17px; font-weight:700; color:#fff; margin-bottom:8px; line-height:1.3;">Final Project Deliverables Template</div>
        <div style="font-size:13px; color:#8899bb;">→ View resource</div>
      </div></a>
    </div>
  </div>
</section>
"""


def thank_you() -> str:
    return """<section class="centered" data-title="Thank you">
  <div class="inner">
    <div style="font-size:80px; margin-bottom:20px;">💥</div>
    <h2 style="font-size:64px; margin-bottom:12px;">Thank you</h2>
    <div class="subtitle" style="font-size:20px; max-width:520px;">Commit your Module 1 artefacts. See you in Module 2: Validate AI Opportunities and Technical Feasibility.</div>
  </div>
</section>
"""



# ─────────────────────────────────────────────────────────────────────────────
# Lab content used inside applied_work() bodies
# ─────────────────────────────────────────────────────────────────────────────

LOVABLE_LAB_BODY = """
<p>You will use Lovable to build a functional, high-fidelity dashboard for your AI Copilot, <strong>Juno</strong>. The goal: prompt Lovable to generate the interface for Juno with a three-column layout (Raw Input · Analysis · Output) and apply a professional design system to it.</p>
<ol style="text-align:left; max-width:760px; margin:18px auto;">
  <li>Open <a href="https://lovable.dev" target="_blank" rel="noopener" style="color:#60a5fa;">Lovable</a>.</li>
  <li>Create your own prompt using the <strong>Anatomy framework</strong> (Role · Task · Constraints · Format), <em>or</em> paste the pre-built prompt from the <a href="../juno-project-template/01-prompting/lab-walkthrough.md" style="color:#60a5fa;">walkthrough</a> to create the core three-column layout.</li>
  <li>Iterate on the style with a second prompt &mdash; either <strong>upload a screenshot</strong> of your company&rsquo;s product / Figma design system to clone it, or use a <strong>&ldquo;Vibe&rdquo; prompt</strong> like <em>&ldquo;Make it look like Linear&rdquo;</em>.</li>
  <li>Once finalised, paste the user-interview artifact snippet from the lab guide into your new <strong>Raw Input</strong> box and observe the output.</li>
</ol>
<p style="font-size:13px; color:#8899bb; max-width:720px; margin:18px auto 0;">If you wish to use a different tool, try <a href="https://stitch.withgoogle.com/" style="color:#60a5fa;">Google Stitch</a>, <a href="https://bolt.new" style="color:#60a5fa;">Bolt</a>, or upgrade to a Pro Lovable plan for more credits.</p>
"""


JUNO_SYSTEM_PROMPT_BODY = """
<p>You will move from being a <em>user</em> of an AI to being an <em>architect</em>. You&rsquo;ll configure a System Prompt that turns unstructured chaos into a professional <strong>Opportunity Brief</strong>. This system prompt is part of your final project deliverables.</p>
<ol style="text-align:left; max-width:760px; margin:18px auto;">
  <li>Skim the 5 artefacts in the lab guide. Identify <em>signal vs noise</em> on your own.</li>
  <li>Open ChatGPT (or Claude). Using the template in the lab guide, define <strong>Role</strong> and <strong>Task</strong> &mdash; establishing Juno as an AI Associate PM whose job is to synthesise raw discovery notes into a structured Opportunity Brief.</li>
  <li>Establish <strong>Constraints</strong> and <strong>Format</strong> by instructing Juno to never invent quotes, always cite source IDs, and follow a specific output schema (Problem · Persona · Evidence Table).</li>
  <li>Provide <strong>one &ldquo;golden&rdquo; example</strong> (Few-Shot) within your prompt to show Juno how to filter raw chaos into a high-fidelity strategic insight.</li>
  <li>Add a <strong>Chain-of-Thought</strong> instruction forcing Juno to surface risks and assumptions step-by-step before generating the final brief.</li>
</ol>
<p style="font-size:13px; color:#8899bb; max-width:720px; margin:18px auto 0;"><strong>Self-review checklist</strong> &mdash; use the 5-point checklist in the <a href="../juno-project-template/01-prompting/system-prompt-self-review.md" style="color:#60a5fa;">lab guide</a> before you commit. Then paste the artefact + verbatim review prompt into ChatGPT for an AI review.</p>
"""



# ─────────────────────────────────────────────────────────────────────────────
# build_module_1 — wires the original PowerPoint flow (36 slides)
# ─────────────────────────────────────────────────────────────────────────────

def build_module_1():
    sections_inst, sections_share = [], []
    add = _add_builder(sections_inst, sections_share)

    # Slide 1 — Title
    add(
        hero(
            title_lead="Drive AI-First Execution",
            title_accent="with Prompting",
            subtitle="Module 1 &middot; AI Product Management Certification",
            waypoints=[
                ("The AI-First Product Mindset", "Mental model shift: deterministic to probabilistic systems."),
                ("The Anatomy of a High-Quality Prompt", "Role &middot; Task &middot; Constraints &middot; Format."),
                ("Lab: Prompt-to-Prototype with Lovable", "Build the V1 face of Juno in 25 min."),
                ("Prompting as Product Configuration", "System prompts, parameters, fine-tuning, RAG triage."),
            ],
            out_line="You finish Module 1 with Juno&rsquo;s system prompt + a working Lovable prototype committed to your fork.",
            module_n=1,
        ),
        note="Module 1: Drive AI-First Execution with Prompting. Welcome the cohort and set the scene — by the end of this module, every learner walks away with a configured System Prompt for Juno and a clickable Lovable prototype, both committed to their juno-pm fork.",
    )

    # Slide 2 — Class Expectations
    add(class_expectations(), note="Set ground rules: cameras-on for live cohort sessions, async etiquette for solo learners. Reinforce: this is a 100% solo course. No groups. No partner work. All cohort communication is async via Slack.")

    # Slide 3 — Introductions
    add(introductions(), note="Introduce yourself live. Tell learners to post their async intro in #ai-pm-cohort with their LinkedIn. Keep this short — under 5 minutes.")

    # Slide 4 — Final Project Explanation (video placeholder)
    add(final_project_video(), note="Live cohort: play the 4.5-minute Final Project briefing video. Async learners: point them at the Final Project Brief HTML and the juno-project-template README.")

    # Slide 5 — Final Project Deliverables
    add(final_project_deliverables(), note="Walk through the 7 deliverables. Emphasise: every deliverable lives in their juno-pm/ fork. The repo URL IS the submission. No 'permanent groups' — the original course had this; we removed it. Solo only.")

    # Slide 6 — AI Product Management Syllabus
    add(syllabus_visual(), note="Frame the arc across the 6 modules. Each module produces a deliverable that compounds into the final Juno copilot.")

    # Slide 7 — Agenda (Module 1)
    add(agenda_4(), note="The four numbered sections of Module 1. We'll move section by section.")

    # Slide 8 — Section 01 divider
    add(section_divider("01", "The AI-First Product Mindset"), note="Section transition — set up the mindset arc.")

    # Slide 9 — AI-First Product Thinking (solo reflection, was instructor-led Q&A)
    add(ai_first_reflection(), note="Solo reflection. Original was instructor-led Q&A — we converted to a 5-minute solo reflection with answers posted in #ai-pm-cohort. Same outcome: surface the mindset shift from rule-writing to intent-shaping.")

    # Slide 10 — Every PM is now an AI PM
    add(every_pm_is_ai_pm(), note="The big frame. AI is no longer a vertical specialty — it's baseline competency for every PM. Like mobile in 2015. Every PM needs AI fluency now.")

    # Slide 11 — From Rules to Probabilities
    add(deterministic_vs_probabilistic(), note="The single biggest mental model shift for a PM in this era: deterministic to probabilistic. Drive home: same input can produce different valid outputs. Acceptance criteria can't say 'output will be X' anymore — they specify qualities and guardrails.")

    # Slide 12 — PM's Dual Role
    add(dual_role(), note="PM operates in two modes. Building AI Products: city planner (zoning laws, not buildings). Using AI in Workflows: conversation, not command — judgment lives in iteration.")

    # Slide 13 — How the AI-Era PM Role Has Evolved
    add(role_evolved_quadrants(), note="Four shifts: Assess AI-Ability (don't force AI where deterministic rule wins), Own the Vibe (configure cost/latency/quality), Define the Failure State (design for AI failure), Prototype as Spec (the prompt IS the requirement).")

    # Slide 14 — A PM's AI Toolkit
    add(pm_toolkit(), note="Quick gloss. Seven categories of AI capability that augment PM workflow: Research/PRDs/Roadmapping/Prototyping/Experimentation/GTM/Presentations. Tell learners they can explore on their own.")

    # Slide 15 — Section 02 divider
    add(section_divider("02", "The Anatomy of a High-Quality Prompt"), note="Section transition.")

    # Slide 16 — Anatomy of a High-Quality Prompt
    add(prompt_anatomy_4d(), note="The four dimensions: Role, Task, Constraints, Format. Structure reduces randomness. Miss one of these and you're introducing inconsistency into your product. This is the framework learners will use in the Lovable lab next.")

    # Slide 17 — Section 03 divider
    add(section_divider("03", "Hands-On Lab: Prompt-to-Prototype with Lovable"), note="Section transition — flip into hands-on mode.")

    # Slide 18 — Lovable Lab
    add(
        applied_work(
            title="Prompt-to-Prototype Your Copilot with Lovable",
            goal="Build the V1 'face' of Juno — a clickable three-column dashboard with a real design system applied.",
            body_html=LOVABLE_LAB_BODY,
            repo_path="juno-pm/01-prompting/lovable-prototype.md",
            timer_min=25,
            tool_url="../Modules/M1%20-%20Prompt%20Anatomy%20Builder.html",
            tool_desc="Use the Prompt Anatomy Builder to draft Role · Task · Constraints · Format before pasting into Lovable.",
        ),
        note="25-minute solo build. The activity is 100% individual — original course called this an 'Individual Exercise', so we kept that. After the lab, learners post their experience in #ai-pm-cohort.",
    )

    # Slide 19 — Quick Debrief
    add(
        applied_work(
            title="Quick Debrief — Your Copilot Prototype",
            goal="In one sentence: when you pasted the artifact and pressed 'Process', where did the prototype fall short?",
            body_html="""<p>Post your one-sentence answer in <code>#ai-pm-cohort</code>. Look for the <strong>Beautiful Liar</strong> pattern: the cards looked right but the text was generic, or the AI ignored the actual evidence in your transcript.</p>
            <p style="font-size:13px; color:#8899bb; margin-top:14px;">This is the bridge to Section 04. We gave the AI a design system but not a <em>product brain</em>. To fix that, you stop &ldquo;asking nicely&rdquo; and start <em>system configuration</em>.</p>""",
            repo_path="juno-pm/01-prompting/lovable-debrief.md",
            timer_min=2,
            tool_url=None,
            tool_desc=None,
        ),
        note="2-minute Slack debrief. Read 3-4 representative posts aloud (live) or pin them (async). Pivot statement: 'We gave the AI a design system but no Product Brain. System Prompts come next.'",
    )

    # Slide 20 — Break
    add(break_section(), note="5-minute break. They earned it.")

    # Slide 21 — Cameras On reminder
    add(cameras_on(), note="Quick reminder for live cohort sessions only. Async learners can skip.")

    # Slide 22 — Section 04 divider
    add(section_divider("04", "Prompting as Product Configuration"), note="Section transition — the deepest section of the module.")

    # Slide 23 — Prompt Layers
    add(prompt_layers_stack(), note="In Lab 1, you worked exclusively in the Middle Layer (User Prompts) inside Lovable's already-engineered system. To build YOUR product, you have to configure all three layers. System Messages are your real PRD — that's where you lock in the rules.")

    # Slide 24 — The Prompting Strategy Matrix
    add(strategy_matrix_3(), note="Three strategies: Zero-Shot (baseline), Few-Shot (the standardiser), Chain-of-Thought (the analyst). PMs choose based on the problem. Note we're going deeper on Few-Shot and CoT in the next two slides.")

    # Slide 25 — Few-Shot in Practice
    add(fewshot_compare(), note="Walk through the comparison. Zero-Shot for creativity. Few-Shot for compliance. The 'Slow login → Feature Request' example matters because it shows how examples encode YOUR taxonomy, not the model's guess.")

    # Slide 26 — CoT in Practice
    add(cot_compare(), note="Walk through the AI Avatars example. The model wants to call AI features 'High Priority' because it pattern-matches on 'AI = good'. CoT forces it to LINK the feature to the actual goal (churn) before deciding.")

    # Slide 27 — Configure Juno's System Prompt — Individual Exercise (was breakout group)
    add(
        applied_work(
            title="Configure Juno&rsquo;s System Prompt",
            goal="Write a system message that turns messy cross-functional artefacts into a clean evidence-based opportunity brief — Juno&rsquo;s job description.",
            body_html=JUNO_SYSTEM_PROMPT_BODY,
            repo_path="juno-pm/01-prompting/system-prompt.md",
            timer_min=30,
            tool_url="../Modules/M1%20-%20Prompt%20Anatomy%20Builder.html",
            tool_desc="Use the Prompt Anatomy Builder for Role/Task/Constraints/Format scaffolding.",
        ),
        note="30-minute solo build. The original PowerPoint called this a 'Breakout Group Exercise' with permanent project teams — we converted it to a 100% individual exercise per the solo-only course design. Same scenario (Juno-as-Associate-PM, 5 messy artefacts, opportunity brief), different format. Output is part of their final project deliverables.",
    )

    # Slide 28 — Hyperparameters
    add(hyperparameters_3(), note="Three knobs: Temperature (creativity slider), Top P (vocabulary filter), Max Tokens (cost ceiling). Real-world examples ground the trade-offs. Pro tip: always run a parameter sweep — don't guess.")

    # Slide 29 — Fine-Tuning
    add(fine_tuning_card(), note="Fine-tuning bakes BEHAVIOUR into weights — not knowledge. Use it for skills (style, format, code patterns), not for facts (prices, policies, specific data). For facts, you need RAG (Module 3).")

    # Slide 30 — Optimization Decision Framework
    add(optimization_decision_3step(), note="The triage framework. When stakeholders shout 'fine-tune the model!' your job is to diagnose. Inconsistency? Few-Shot. Missing data? RAG. Wrong vibe? Fine-Tuning. Saves your company $50k of unnecessary fine-tuning runs.")

    # Slide 31 — From PRDs to Prompts
    add(prds_to_prompts(), note="Old way: paper spec, hand off to Eng, wait, find out it doesn't work. New way: prompt spec, prove it in the playground, hand off a validated configuration. Closes the interpretation gap. Your prompt is the prototype is the requirement.")

    # Slide 32 — Key Takeaways
    add(
        takeaways(
            module_short="M1 · Drive AI-First Execution with Prompting",
            items=[
                ("Adapt the lifecycle for probabilistic systems", "PMs must steer continuously, not write rigid code. AI-native tools let you move from paper requirements to functional prototypes that validate intent in real time."),
                ("System prompts are invisible code", "Mastering the anatomy &mdash; Role, Task, Constraints, Format &mdash; lets you build reliable system logic instead of basic chat."),
                ("Optimise with the right tool", "Choosing between Prompting, Fine-Tuning, or RAG is a strategic decision. Diagnose: instructions vs style vs facts. Pick the most cost-effective architectural lever."),
            ],
        ),
        note="The three takeaways from the original deck. Recap before learners head into extra practice and Module 2.",
    )

    # Slide 33 — Extra Practice + Next Session preview
    add(
        extra_practice(
            items=[
                ("Exercise 1", "Expand Your Lovable Prototype", "Go back to your Lovable project and prompt the AI to generate a strategic dashboard view for Juno. Use a &lsquo;Vibe&rsquo; prompt to style it like a professional analytics tool of your choice."),
                ("Exercise 2", "Audit a Manual Task for AI-Ability", "Identify a frequent rule-based task in your current job and draft a System Message to automate it. Use the Anatomy framework. Does the output need Few-Shot examples, or is Zero-Shot enough?"),
            ],
            next_module_blurb=(
                "<strong>Module 2 &middot; Validate AI Opportunities and Technical Feasibility.</strong> "
                "Become an AI strategist capable of selecting and shaping AI bets that ship and move business metrics. "
                "Move from broad ideas to a formal AI Strategy One-Pager that defines the technical approach, data provenance, and target autonomy levels."
            ),
        ),
        note="Optional homework — the 'Dig Deeper' section. Then preview Module 2.",
    )

    # Slide 34 — Resources & Templates
    add(resources_templates(), note="Three resource cards: Module 1 Lab Guide, Final Project Brief, Final Project Deliverables Template. Tell learners these are also linked from the README.")

    # Slide 35 — Q&A
    add(qa_section(), note="Q&A. Live cohort: open the floor. Async: this is a thread in #ai-pm-cohort.")

    # Slide 36 — Thank you
    add(thank_you(), note="Wrap. Remind learners to commit their Module 1 artefacts to their fork before Module 2.")

    return sections_inst, sections_share

