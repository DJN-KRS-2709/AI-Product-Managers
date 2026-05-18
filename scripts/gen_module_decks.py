"""Generate all 6 module slide decks (instructor + shareable) for the AI Product Management Certification.

Mirrors the AI Product Strategy reference deck pattern: dark navy + Product School branding,
Poppins/Lato/IBM Plex Mono, fade-up sections, nav dots, progress bar, section sorter.

Run from the repo root:
    python3 scripts/gen_module_decks.py
"""
from __future__ import annotations
from pathlib import Path
import textwrap

REPO_ROOT = Path(__file__).resolve().parent.parent
MODULES_DIR = REPO_ROOT / "Modules"
LOGO_REL = "../Design/Minimalist shield with glowing _P_.png"

# ─────────────────────────────────────────────────────────────────────────────
# SHARED CSS — mirrors the AI Product Strategy reference deck
# ─────────────────────────────────────────────────────────────────────────────

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap');

*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-snap-type: y mandatory; scroll-behavior: smooth; }
body {
  font-family: 'Lato', -apple-system, sans-serif;
  background: #07162C;
  color: #e8e8f0;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

section {
  min-height: 100vh;
  scroll-snap-align: start;
  padding: 80px 60px 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
  background: radial-gradient(ellipse at 30% 40%, rgba(59,130,246,0.25) 0%, #07162C 60%);
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
section.visible { opacity: 1; transform: translateY(0); }
section.skipped { display: none; }

.nav-dots {
  position: fixed; right: 24px; top: 50%; transform: translateY(-50%);
  display: flex; flex-direction: column; gap: 6px; z-index: 100;
}
.nav-dot {
  width: 8px; height: 8px; border-radius: 50%;
  background: #333; border: none; cursor: pointer;
  transition: all 0.3s; position: relative;
}
.nav-dot.active { background: #3b82f6; box-shadow: 0 0 8px rgba(59,130,246,0.5); transform: scale(1.4); }
.nav-dot:hover { background: rgba(59,130,246,0.7); }
.nav-dot .tooltip {
  position: absolute; right: 20px; top: 50%; transform: translateY(-50%);
  background: #0c2244; color: #b0b4c8; padding: 4px 10px; border-radius: 6px;
  font-size: 11px; white-space: nowrap; opacity: 0; pointer-events: none;
  transition: opacity 0.2s; border: 1px solid rgba(59,130,246,0.2);
}
.nav-dot:hover .tooltip { opacity: 1; }

.progress-bar {
  position: fixed; top: 0; left: 0; height: 3px; z-index: 100;
  background: linear-gradient(90deg, #1241B0, #3b82f6);
  transition: width 0.3s ease;
}

h1, h2 { font-family: 'Poppins', sans-serif; }
h1 { font-size: 56px; font-weight: 900; color: #fff; line-height: 1.1; }
h2 { font-size: 40px; font-weight: 800; color: #fff; margin-bottom: 12px; }
h3 { font-size: 22px; font-weight: 700; color: #e0e0f0; }
p, li { font-size: 17px; line-height: 1.7; color: #b0b4c8; }
.subtitle { font-size: 20px; color: #8899bb; margin-top: 8px; margin-bottom: 32px; }
.section-label {
  font-size: 12px; text-transform: uppercase; letter-spacing: 3px;
  color: rgba(255,255,255,0.7); margin-bottom: 12px; font-weight: 700;
}
strong { color: #fff; font-weight: 700; }
em { color: #60a5fa; font-style: normal; font-weight: 600; }
code {
  background: rgba(18,65,176,0.15); padding: 2px 8px; border-radius: 4px;
  font-size: 14px; color: #60a5fa; font-family: 'IBM Plex Mono', 'SF Mono', monospace;
}
ul { list-style: none; padding: 0; }
ul li { padding: 6px 0; padding-left: 24px; position: relative; }
ul li::before {
  content: ''; position: absolute; left: 0; top: 14px;
  width: 8px; height: 8px; border-radius: 2px; background: #1241B0;
}

.inner { max-width: 880px; width: 100%; text-align: left; }
section.centered { text-align: center; }
section.centered .inner { text-align: center; }
section.centered ul li { padding-left: 0; }
section.centered ul li::before { display: none; }

/* HERO */
.hero { align-items: center; text-align: center; }
.hero h1 { font-size: 64px; margin-bottom: 4px; }
.hero h1 span { color: #60a5fa; }
.hero .subtitle { font-size: 22px; max-width: 600px; margin: 12px auto 28px; color: #60a5fa; }
.hero .scroll-hint { font-size: 13px; color: #444; margin-top: 32px; animation: pulse 2s ease infinite; }
.hero .scroll-hint span { display: block; margin-top: 8px; font-size: 20px; }
.hero-logo { position: absolute; top: 32px; left: 50%; transform: translateX(-50%); }
.hero-logo img { height: 48px; width: auto; opacity: 0.95; }
@keyframes pulse { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }

/* TAGS */
.demo-tag {
  display: inline-block; font-size: 11px; font-weight: 800;
  letter-spacing: 0.12em; text-transform: uppercase;
  padding: 6px 16px; border-radius: 6px; margin-bottom: 18px;
}
.tag-provocation { background: rgba(248,81,73,0.12); color: #ff7b72; }
.tag-lecture { background: rgba(88,166,255,0.12); color: #79c0ff; }
.tag-case { background: rgba(210,153,34,0.12); color: #e3b341; }
.tag-exercise { background: rgba(52,211,153,0.12); color: #6ee7b7; }
.tag-activity { background: rgba(188,140,255,0.12); color: #d2a8ff; }
.tag-build { background: rgba(255,123,182,0.12); color: #ff7b72; }
.tag-break { background: rgba(100,116,139,0.12); color: #94a3b8; }
.tag-debrief { background: rgba(188,140,255,0.12); color: #d2a8ff; }
.tag-complete { background: rgba(52,211,153,0.12); color: #6ee7b7; }
.tag-recall { background: rgba(59,130,246,0.12); color: #79c0ff; }
.tag-framework { background: rgba(210,153,34,0.12); color: #e3b341; }

.lab-timer {
  position: absolute; top: 24px; right: 32px;
  display: flex; align-items: center; gap: 8px;
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12);
  border-radius: 12px; padding: 10px 18px;
  font-family: 'IBM Plex Mono', monospace; font-size: 15px; font-weight: 600;
  color: #60a5fa; z-index: 10;
}

/* WAYPOINTS */
.waypoints { display: flex; flex-direction: column; gap: 14px; margin: 24px 0; max-width: 720px; }
.waypoint {
  display: flex; align-items: flex-start; gap: 18px;
  background: rgba(59,130,246,0.06); border: 1px solid rgba(59,130,246,0.15);
  border-radius: 12px; padding: 20px 24px;
  transition: all 0.3s ease;
  text-align: left;
}
.waypoint:hover { transform: translateX(4px); border-color: rgba(59,130,246,0.3); }
.waypoint-num {
  width: 36px; height: 36px; border-radius: 8px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-size: 16px; font-weight: 800; color: #fff; background: #1241B0;
}
.waypoint-text { flex: 1; }
.waypoint-text .wt-title { font-size: 17px; font-weight: 700; color: #fff; margin-bottom: 4px; }
.waypoint-text .wt-desc { font-size: 14px; color: #8899bb; line-height: 1.5; }

/* CARDS */
.cards-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px; margin: 24px 0;
}
.card-item {
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; padding: 22px; text-align: center;
  transition: all 0.3s ease; position: relative; overflow: hidden;
}
.card-item::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: var(--card-accent, #3b82f6);
  transform: scaleX(0); transform-origin: left;
  transition: transform 0.3s ease;
}
.card-item:hover { border-color: var(--card-accent, #3b82f6); transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.4); }
.card-item:hover::before { transform: scaleX(1); }
.card-item .card-icon { font-size: 24px; margin-bottom: 8px; }
.card-item .card-title { font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 4px; }
.card-item .card-desc { font-size: 12.5px; color: #8899bb; line-height: 1.45; }

/* EXPECT GRID (How This Module Runs) */
.expect-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 20px 0;
}
.expect-card {
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px; padding: 18px; text-align: center;
  transition: all 0.3s ease;
}
.expect-card:hover { border-color: rgba(59,130,246,0.3); transform: translateY(-2px); }
.expect-icon { font-size: 26px; margin-bottom: 8px; }
.expect-title { font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 4px; }
.expect-desc { font-size: 12.5px; color: #8899bb; line-height: 1.45; }

/* TRUE/FALSE */
.tf-grid { display: flex; flex-direction: column; gap: 12px; margin: 20px 0; }
.tf-item {
  display: flex; align-items: flex-start; gap: 16px;
  padding: 20px 24px; border-radius: 12px;
  transition: all 0.3s ease; cursor: pointer;
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  text-align: left;
}
.tf-item:hover { transform: translateX(4px); border-color: rgba(255,255,255,0.15); }
.tf-item.revealed.tf-false { background: rgba(248,113,113,0.06); border: 1px solid rgba(248,113,113,0.15); }
.tf-item.revealed.tf-true { background: rgba(52,211,153,0.06); border: 1px solid rgba(52,211,153,0.15); }
.tf-item.revealed.tf-partial { background: rgba(210,153,34,0.06); border: 1px solid rgba(210,153,34,0.15); }
.tf-verdict { font-size: 13px; font-weight: 900; min-width: 64px; padding-top: 2px; letter-spacing: 0.05em; }
.tf-item:not(.revealed) .tf-verdict { visibility: hidden; }
.tf-item:not(.revealed) .tf-verdict::after { content: '?'; visibility: visible; color: #555; font-size: 16px; }
.tf-false .tf-verdict { color: #fca5a5; }
.tf-true .tf-verdict { color: #6ee7b7; }
.tf-partial .tf-verdict { color: #fde68a; }
.tf-body .tf-claim { font-size: 16px; font-weight: 700; color: #e0e0f0; margin-bottom: 4px; }
.tf-body .tf-why { font-size: 13px; color: #8899bb; line-height: 1.5; }
.tf-item:not(.revealed) .tf-why { display: none; }

/* ARC FLOW */
.arc-flow {
  display: flex; gap: 8px; align-items: center; margin: 28px 0;
  flex-wrap: wrap; justify-content: center;
}
.arc-node {
  padding: 12px 16px; border-radius: 10px; text-align: center;
  font-size: 13px; font-weight: 700; color: #fff; min-width: 110px;
  transition: all 0.3s ease;
  background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.2);
}
.arc-node:hover { transform: scale(1.05); }
.arc-node.active-node { box-shadow: 0 0 20px rgba(59,130,246,0.3); background: rgba(59,130,246,0.2); border: 2px solid #3b82f6; }
.arc-arrow { color: #333; font-size: 18px; }
.arc-node .ad-num { font-size: 10px; opacity: 0.5; margin-bottom: 2px; }

/* TABLE */
.ref-table { width: 100%; border-collapse: collapse; margin: 16px 0; }
.ref-table th {
  text-align: left; padding: 12px; font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em; color: #8899bb;
  border-bottom: 1px solid rgba(59,130,246,0.15);
}
.ref-table td {
  padding: 14px 12px; border-bottom: 1px solid rgba(255,255,255,0.06);
  font-size: 14px; color: #b0b4c8; line-height: 1.4;
}
.ref-table td:first-child { font-weight: 700; color: #e0e0f0; white-space: nowrap; }
.ref-table tr:hover td { background: rgba(59,130,246,0.04); }

/* EVIDENCE CARDS */
.evidence-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 20px 0; }
.evidence-card {
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px;
  padding: 22px; transition: all 0.3s ease; text-align: left;
}
.evidence-card:hover { transform: translateY(-2px); border-color: rgba(59,130,246,0.3); }
.evidence-card .ec-label {
  font-size: 11px; font-weight: 800; text-transform: uppercase;
  letter-spacing: 0.08em; color: #60a5fa; margin-bottom: 8px;
}
.evidence-card .ec-company { font-size: 16px; font-weight: 700; color: #fff; margin-bottom: 4px; }
.evidence-card .ec-text { font-size: 13px; color: #8899bb; line-height: 1.5; }

/* CASE STUDY */
.case-acts { display: flex; gap: 16px; margin: 24px 0; }
.case-act { flex: 1; border-radius: 14px; padding: 24px; transition: all 0.3s ease; text-align: left; }
.case-act:hover { transform: translateY(-3px); }
.case-act .ca-label { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; }
.case-act .ca-text { font-size: 14px; color: #a0a8b4; line-height: 1.5; }
.act-bet { background: rgba(88,166,255,0.06); border: 1px solid rgba(88,166,255,0.15); }
.act-bet .ca-label { color: #58a6ff; }
.act-crack { background: rgba(210,153,34,0.06); border: 1px solid rgba(210,153,34,0.15); }
.act-crack .ca-label { color: #d29922; }
.act-correct { background: rgba(52,211,153,0.06); border: 1px solid rgba(52,211,153,0.15); }
.act-correct .ca-label { color: #34d399; }

/* DIAG AXES */
.diag-axes { display: flex; gap: 20px; margin: 24px 0; }
.diag-axis {
  flex: 1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; padding: 28px; text-align: center;
  transition: all 0.3s ease;
}
.diag-axis:hover { transform: translateY(-3px); border-color: rgba(59,130,246,0.3); }
.diag-axis .da-num { font-size: 28px; font-weight: 900; margin-bottom: 6px; color: #60a5fa; }
.diag-axis .da-name { font-size: 16px; font-weight: 700; color: #fff; margin-bottom: 6px; }
.diag-axis .da-q { font-size: 13px; color: #8899bb; line-height: 1.4; }

/* SECTION BREAK */
section.section-break { padding: 0; }
section.section-break .section-break-inner {
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 50% 20%, rgba(59,130,246,0.25) 0%, rgba(59,130,246,0.08) 35%, #07162C 75%);
  display: flex; flex-direction: column; justify-content: flex-end;
  padding: 80px;
  text-align: left;
}
.section-break-inner .lab-title {
  font-size: 13px; font-weight: 800; text-transform: uppercase;
  letter-spacing: 0.16em; color: rgba(255,255,255,0.5); margin-bottom: 16px;
}
.section-break-inner .lab-name { font-size: 52px; font-weight: 900; color: #fff; line-height: 1.1; max-width: 700px; font-family: 'Poppins', sans-serif; }
.section-break-inner .lab-desc { font-size: 18px; color: rgba(255,255,255,0.5); line-height: 1.6; margin-top: 16px; max-width: 600px; }

/* CAMERAS ON — matches the AI Product Strategy reference deck */
section.cameras-section { padding: 0; }
section.cameras-section .cameras-inner {
  position: absolute; inset: 0;
  background: linear-gradient(135deg, #07162C 0%, #0c2244 50%, #1241B0 100%);
  display: flex; align-items: center; justify-content: center;
}
.cameras-layout { display: flex; align-items: center; gap: 60px; max-width: 900px; width: 100%; }
.cameras-left { flex: 1; position: relative; }
.cameras-logo { width: 48px; height: 48px; margin-bottom: 40px; opacity: 0.9; }
.cameras-card {
  border: 1.5px solid rgba(255,255,255,0.15); border-radius: 20px;
  padding: 48px 64px; max-width: 520px; text-align: left;
}
.cameras-card h2 { font-size: 32px; margin-bottom: 8px; }
.cameras-card .cameras-arrow { font-size: 18px; font-weight: 700; color: #60a5fa; margin-bottom: 4px; }
.cameras-card p { font-size: 16px; color: rgba(255,255,255,0.65); line-height: 1.6; }
.cameras-photo-strip {
  flex-shrink: 0; width: 220px; height: 480px; border-radius: 16px;
  overflow: hidden; border: 1.5px solid rgba(255,255,255,0.12);
}
.cameras-photo-strip img { width: 100%; height: 100%; object-fit: cover; }

/* COMPLETION / TAKEAWAYS */
.takeaway-list { display: flex; flex-direction: column; gap: 14px; margin: 24px 0; max-width: 880px; }
.takeaway-item { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 18px 22px; transition: all 0.3s; text-align: left; }
.takeaway-item:hover { border-color: rgba(59,130,246,0.3); transform: translateX(4px); }
.takeaway-item p { font-size: 15px; color: #b0b4c8; line-height: 1.6; }

.artifact-preview {
  background: rgba(59,130,246,0.06); border: 1px solid rgba(59,130,246,0.2);
  border-radius: 14px; padding: 24px; margin: 20px auto; max-width: 700px;
  text-align: left;
}
.artifact-preview .ap-title {
  font-size: 14px; font-weight: 800; color: #60a5fa; text-transform: uppercase;
  letter-spacing: 0.1em; margin-bottom: 14px;
}

.bottom-cta {
  position: absolute; bottom: 0; left: 0; right: 0;
  background: rgba(52,211,153,0.08); border-top: 1px solid rgba(52,211,153,0.25);
  padding: 14px 32px; text-align: center;
  font-size: 14px; font-weight: 600; color: #6ee7b7;
}
.bottom-cta a { color: #6ee7b7; text-decoration: underline; }

/* INSTRUCTOR NOTES */
.notes {
  background: rgba(59,130,246,0.06); border-left: 3px solid #1241B0;
  border-radius: 0 8px 8px 0; padding: 14px 18px; margin: 24px 0 0;
  text-align: left; max-width: 880px;
}
.notes h4 { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.14em; color: #60a5fa; margin: 0 0 6px; }
.notes p { font-size: 14px; color: #cdd5e3; line-height: 1.55; }

/* SHAREABLE TAKEAWAY (replaces .notes in shareable decks) */
.takeaway {
  background: rgba(34,211,238,0.05); border-left: 3px solid #22d3ee;
  border-radius: 0 8px 8px 0; padding: 14px 18px; margin: 24px 0 0;
  text-align: left; max-width: 880px;
}
.takeaway h4 { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.14em; color: #22d3ee; margin: 0 0 6px; }
.takeaway p { font-size: 14px; color: #cdd5e3; line-height: 1.55; }

/* Repo CTA inline */
.repo-cta { font-size: 14px; color: #6ee7b7; margin-top: 14px; text-align: center; }
.repo-cta strong { color: #6ee7b7; }
.repo-cta code { color: #6ee7b7; }

/* Tool button */
.tool-btn {
  display: inline-block; background: #1241B0; color: #fff; text-decoration: none;
  font-size: 14px; font-weight: 800; padding: 10px 22px; border-radius: 999px;
  box-shadow: 0 8px 24px rgba(18,65,176,0.35); margin-top: 14px;
  transition: transform .2s, box-shadow .2s;
}
.tool-btn:hover { transform: translateY(-2px); box-shadow: 0 12px 32px rgba(18,65,176,0.5); }

/* Help hint, skip badge, sorter */
.help-hint {
  position: fixed; bottom: 14px; right: 18px;
  font-size: 11px; color: rgba(255,255,255,0.3);
  font-family: 'IBM Plex Mono', monospace; z-index: 90;
}
.skip-badge {
  position: fixed; bottom: 14px; left: 18px;
  background: rgba(248,113,113,0.2); color: #fca5a5;
  border: 1px solid rgba(248,113,113,0.3);
  padding: 4px 10px; border-radius: 999px;
  font-size: 11px; font-weight: 700; letter-spacing: 0.1em;
  cursor: pointer; opacity: 0; pointer-events: none;
  transition: opacity 0.2s; z-index: 90;
}
.skip-badge.visible { opacity: 1; pointer-events: auto; }
.slide-sorter {
  position: fixed; inset: 0; background: rgba(7,22,44,0.95);
  z-index: 200; padding: 60px; overflow-y: auto;
  display: none; flex-direction: column;
}
.slide-sorter.visible { display: flex; }
.sorter-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 32px; }
.sorter-title { font-size: 28px; font-weight: 800; color: #fff; font-family: 'Poppins', sans-serif; }
.sorter-subtitle { font-size: 14px; color: #8899bb; margin-top: 4px; }
.sorter-close { background: transparent; border: 1px solid rgba(255,255,255,0.2); color: #fff; font-size: 18px; padding: 8px 14px; border-radius: 8px; cursor: pointer; }
.sorter-close:hover { background: rgba(255,255,255,0.05); }
.sorter-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }
.sorter-item {
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px;
  padding: 14px 16px; cursor: pointer; transition: all 0.2s ease;
}
.sorter-item:hover { border-color: #3b82f6; transform: translateY(-2px); }
.sorter-item.sorter-active { border-color: #3b82f6; background: rgba(59,130,246,0.1); }
.sorter-item.sorter-skipped { opacity: 0.4; }
.sorter-num { font-size: 11px; font-weight: 800; color: #60a5fa; text-transform: uppercase; letter-spacing: 0.1em; }
.sorter-label { font-size: 14px; color: #fff; margin: 4px 0 8px; font-weight: 600; }
.sorter-skip-btn { font-size: 11px; padding: 4px 10px; border-radius: 6px; cursor: pointer; border: 0; }
.sorter-skip-btn.skip-on { background: rgba(248,113,113,0.2); color: #fca5a5; }
.sorter-skip-btn.skip-off { background: rgba(52,211,153,0.15); color: #6ee7b7; }

@media (max-width: 768px) {
  section { padding: 40px 24px; }
  h1 { font-size: 36px; }
  h2 { font-size: 28px; }
  .hero h1 { font-size: 40px; }
  .case-acts, .diag-axes { flex-direction: column; }
  .cards-grid, .evidence-cards, .expect-grid { grid-template-columns: 1fr; }
  .nav-dots { display: none; }
}
"""

# ─────────────────────────────────────────────────────────────────────────────
# SHARED JS — nav dots, progress bar, fade-up, sorter, skip
# ─────────────────────────────────────────────────────────────────────────────

JS = r"""
const sections = Array.from(document.querySelectorAll('section'));
const navDotsContainer = document.getElementById('navDots');
let currentIdx = 0;
let sorterVisible = false;

const STORAGE_KEY = 'skip-sections-' + document.title.replace(/[^a-zA-Z0-9]/g, '-').substring(0, 60);
const skippedSections = new Set(JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'));

function saveSkips() { localStorage.setItem(STORAGE_KEY, JSON.stringify([...skippedSections])); }

function applySkips() {
  sections.forEach((sec, i) => sec.classList.toggle('skipped', skippedSections.has(i)));
  rebuildDots();
}

function rebuildDots() {
  navDotsContainer.innerHTML = '';
  sections.forEach((sec, i) => {
    if (skippedSections.has(i)) return;
    const dot = document.createElement('button');
    dot.className = 'nav-dot';
    const title = sec.dataset.title || 'Section';
    dot.innerHTML = `<span class="tooltip">${title}</span>`;
    dot.dataset.idx = i;
    dot.onclick = () => sections[i].scrollIntoView({ behavior: 'smooth' });
    navDotsContainer.appendChild(dot);
  });
}

function getActiveSections() { return sections.map((s, i) => i).filter(i => !skippedSections.has(i)); }

function updateProgress(idx) {
  currentIdx = idx;
  const active = getActiveSections();
  const posInActive = active.indexOf(idx);
  const progress = posInActive >= 0 ? (posInActive + 1) / active.length * 100 : 0;
  document.getElementById('progressBar').style.width = progress + '%';
  const dots = navDotsContainer.querySelectorAll('.nav-dot');
  dots.forEach(d => d.classList.toggle('active', parseInt(d.dataset.idx) === idx));
  document.getElementById('skip-badge').classList.toggle('visible', skippedSections.has(idx));
}

function toggleSkip(idx) {
  if (skippedSections.has(idx)) skippedSections.delete(idx);
  else skippedSections.add(idx);
  saveSkips();
  applySkips();
  updateProgress(currentIdx);
  if (sorterVisible) renderSorter();
}

function nextActive(from, dir) {
  let i = from + dir;
  while (i >= 0 && i < sections.length) {
    if (!skippedSections.has(i)) return i;
    i += dir;
  }
  return -1;
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      const idx = sections.indexOf(entry.target);
      updateProgress(idx);
    }
  });
}, { threshold: 0.35 });
sections.forEach(sec => observer.observe(sec));

function renderSorter() {
  const grid = document.getElementById('sorter-grid');
  grid.innerHTML = '';
  sections.forEach((sec, i) => {
    const isSkipped = skippedSections.has(i);
    const isCurrent = i === currentIdx;
    const div = document.createElement('div');
    div.className = 'sorter-item' + (isSkipped ? ' sorter-skipped' : '') + (isCurrent ? ' sorter-active' : '');
    const title = sec.dataset.title || 'Section';
    div.innerHTML = `
      <div class="sorter-num">Section ${i + 1}</div>
      <div class="sorter-label">${title}</div>
      <button class="sorter-skip-btn ${isSkipped ? 'skip-on' : 'skip-off'}"
              onclick="event.stopPropagation(); toggleSkip(${i})">
        ${isSkipped ? '↩ Unskip' : '⊘ Skip'}
      </button>`;
    div.addEventListener('click', () => { sections[i].scrollIntoView({ behavior: 'smooth' }); closeSorter(); });
    grid.appendChild(div);
  });
}
function openSorter() { sorterVisible = true; renderSorter(); document.getElementById('slide-sorter').classList.add('visible'); }
function closeSorter() { sorterVisible = false; document.getElementById('slide-sorter').classList.remove('visible'); }

document.getElementById('skip-badge').addEventListener('click', () => toggleSkip(currentIdx));

document.addEventListener('keydown', (e) => {
  if (sorterVisible) {
    if (e.key === 'Escape' || e.key === 'm' || e.key === 'M') { e.preventDefault(); closeSorter(); }
    return;
  }
  if (e.key === 'ArrowDown' || e.key === 'ArrowRight' || e.key === ' ') {
    e.preventDefault();
    const n = nextActive(currentIdx, 1);
    if (n >= 0) sections[n].scrollIntoView({ behavior: 'smooth' });
  }
  else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
    e.preventDefault();
    const n = nextActive(currentIdx, -1);
    if (n >= 0) sections[n].scrollIntoView({ behavior: 'smooth' });
  }
  else if (e.key === 'k' || e.key === 'K') { toggleSkip(currentIdx); }
  else if (e.key === 'm' || e.key === 'M') { openSorter(); }
});

applySkips();
sections[0].classList.add('visible');
document.querySelectorAll('.tf-item').forEach(item => {
  item.addEventListener('click', () => item.classList.toggle('revealed'));
});
"""

# ─────────────────────────────────────────────────────────────────────────────
# DOMAIN MAP — short labels used in arc-flow + section break crumbs
# ─────────────────────────────────────────────────────────────────────────────

MODULES_META = [
    # (n, slug, short_label, full_title, subtitle, folder)
    (1, "prompting",  "Prompting", "Drive AI-First Execution with Prompting",
     "Stop chatting with AI. Start configuring it.", "01-prompting"),
    (2, "strategy",   "Strategy",  "Strategically Plan AI-Driven Solutions",
     "From AI tactics to product strategy your CFO can sign off on.", "02-strategy"),
    (3, "rag-prd",    "RAG / PRD", "Build the AI PRD: RAG, Specs, Decisions",
     "Write specs an LLM can actually execute.", "03-rag-prd"),
    (4, "ai-ux",      "AI-UX",     "Design AI-Native User Experiences",
     "Make uncertainty feel safe — without hiding it.", "04-ai-ux"),
    (5, "agentic",    "Agentic",   "Orchestrate AI with Agentic Workflows",
     "Hand work to agents — without losing the room.", "05-agentic-workflows"),
    (6, "evals",      "Evals",     "Measure AI Quality with Evals & Guardrails",
     "Prove it works. Catch it when it doesn't.", "06-evals"),
]


# ─────────────────────────────────────────────────────────────────────────────
# Section builders — return raw HTML strings
# ─────────────────────────────────────────────────────────────────────────────

def hero(title_lead: str, title_accent: str, subtitle: str, waypoints: list[tuple[str, str]],
         out_line: str, module_n: int) -> str:
    waypoints_html = "\n".join(
        f'  <div class="waypoint"><div class="waypoint-num">{i+1}</div>'
        f'<div class="waypoint-text"><div class="wt-title">{wt}</div>'
        f'<div class="wt-desc">{wd}</div></div></div>'
        for i, (wt, wd) in enumerate(waypoints)
    )
    return f"""<section class="hero" data-title="{title_lead} {title_accent}">
  <div class="hero-logo"><img src="{LOGO_REL}" alt="Product School logo"/></div>
  <div class="section-label">Module {module_n} &mdash; AI Product Management Certification</div>
  <h1>{title_lead} <span>{title_accent}</span></h1>
  <p class="subtitle">{subtitle}</p>
  <div class="waypoints" style="max-width:640px;">
{waypoints_html}
  </div>
  <p style="font-size:15px; color:#8899bb; margin-top:8px;">{out_line}</p>
  <div class="scroll-hint">Scroll to explore<span>&#8595;</span></div>
</section>
"""


def how_it_runs() -> str:
    cards = [
        ("⏱", "~2 hours, async-friendly", "Self-paced. Each module builds one repo artifact."),
        ("👤", "100% individual", "No groups. No partner work. You own every deliverable."),
        ("🛠", "Open the tool", "Each exercise points at a single-file HTML tool you fill in."),
        ("✅", "Self-review", "Each tool ships with a 4–6 item checklist. Do it before you commit."),
        ("🤖", "AI-review", "Paste your artifact + the verbatim prompt into ChatGPT or Claude."),
        ("📂", "Async share", "Commit to your <code>juno-pm/</code> fork. Optional Loom in <code>#ai-pm-cohort</code>."),
    ]
    cells = "\n".join(
        f'      <div class="expect-card"><div class="expect-icon">{ic}</div>'
        f'<div class="expect-title">{t}</div><div class="expect-desc">{d}</div></div>'
        for ic, t, d in cards
    )
    return f"""<section class="centered" data-title="How This Module Runs">
  <div class="inner">
    <div class="section-label">Ground Rules</div>
    <h2>How This Module Runs</h2>
    <div class="expect-grid">
{cells}
    </div>
  </div>
</section>
"""


def course_arc(active_n: int) -> str:
    nodes = []
    for n, _, label, _, _, _ in MODULES_META:
        cls = "arc-node active-node" if n == active_n else "arc-node"
        nodes.append(f'<div class="{cls}"><div class="ad-num">M{n}</div>{label}</div>')
    sep = '<div class="arc-arrow">→</div>'
    flow = sep.join(nodes)
    return f"""<section class="centered" data-title="Course Arc">
  <div class="inner">
    <div class="section-label">The Course Arc</div>
    <h2>Six Modules. One Living Copilot.</h2>
    <div class="arc-flow">{flow}</div>
    <div class="artifact-preview" style="max-width:680px; margin:20px auto;">
      <div class="ap-title">Your Throughline — Juno PM, in a Repo You Build Across 6 Modules</div>
      <p style="font-size:15px; color:#8899bb; line-height:1.5;">Not a deck. Not a Notion page. A <strong>GitHub repo</strong> — version-controlled, shareable, alive. One folder per module, one artifact each. <strong>Today &rarr; folder <code>{MODULES_META[active_n-1][5]}/</code>.</strong></p>
    </div>
  </div>
</section>
"""


def provocation(headline: str, subtitle: str, claims: list[tuple[str, str, str]]) -> str:
    """claims = [(verdict_class, claim, why)]; verdict_class in {tf-true, tf-false, tf-partial}"""
    items = []
    for vclass, claim, why in claims:
        verdict = vclass.replace('tf-', '').upper()
        items.append(
            f'      <div class="tf-item {vclass}">'
            f'<div class="tf-verdict">{verdict}</div>'
            f'<div class="tf-body"><div class="tf-claim">{claim}</div>'
            f'<div class="tf-why">{why}</div></div></div>'
        )
    body = "\n".join(items)
    return f"""<section data-title="Provocation">
  <div class="inner">
    <div class="demo-tag tag-provocation">Provocation</div>
    <h2>{headline}</h2>
    <div class="subtitle">{subtitle}</div>
    <div class="tf-grid">
{body}
    </div>
  </div>
</section>
"""


def lecture_table(title: str, subtitle: str, headers: list[str], rows: list[list[str]],
                  caption: str = "", tag_label: str = "Lecture") -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "\n".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows
    )
    cap = f'<p style="font-size:13px; color:#8899bb; margin-top:14px; text-align:center;">{caption}</p>' if caption else ""
    return f"""<section data-title="{title}">
  <div class="inner">
    <div class="demo-tag tag-lecture">{tag_label}</div>
    <h2>{title}</h2>
    <div class="subtitle">{subtitle}</div>
    <table class="ref-table">
      <thead><tr>{th}</tr></thead>
      <tbody>
{tr}
      </tbody>
    </table>
    {cap}
  </div>
</section>
"""


def lecture_cards(title: str, subtitle: str, cards: list[tuple[str, str, str]],
                  footer: str = "", tag_label: str = "Lecture") -> str:
    """cards = [(icon, title, desc)] — flexible. Pass empty icon to skip."""
    cell_html = "\n".join(
        f'      <div class="card-item">'
        + (f'<div class="card-icon">{ic}</div>' if ic else "")
        + f'<div class="card-title">{t}</div>'
          f'<div class="card-desc">{d}</div></div>'
        for ic, t, d in cards
    )
    foot = f'<p style="font-size:13px; color:#8899bb; margin-top:14px; text-align:center;">{footer}</p>' if footer else ""
    return f"""<section data-title="{title}">
  <div class="inner">
    <div class="demo-tag tag-lecture">{tag_label}</div>
    <h2>{title}</h2>
    <div class="subtitle">{subtitle}</div>
    <div class="cards-grid">
{cell_html}
    </div>
    {foot}
  </div>
</section>
"""


def two_column(title: str, subtitle: str, left: tuple[str, str, str],
               right: tuple[str, str, str], footer: str = "",
               tag_label: str = "Lecture") -> str:
    """left/right = (label, body, body2)"""
    return f"""<section data-title="{title}">
  <div class="inner">
    <div class="demo-tag tag-lecture">{tag_label}</div>
    <h2>{title}</h2>
    <div class="subtitle">{subtitle}</div>
    <div style="display:flex; gap:20px; margin:24px 0;">
      <div style="flex:1; background:rgba(100,116,139,0.06); border:1px solid rgba(100,116,139,0.15); border-radius:12px; padding:22px; text-align:left;">
        <div style="font-size:13px; font-weight:800; color:#94a3b8; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:10px;">{left[0]}</div>
        <div style="font-size:14px; color:#cdd5e3; line-height:1.55;">{left[1]}</div>
        <div style="font-size:13px; color:#8899bb; line-height:1.5; margin-top:8px;">{left[2]}</div>
      </div>
      <div style="flex:1; background:rgba(59,130,246,0.08); border:1px solid rgba(59,130,246,0.25); border-radius:12px; padding:22px; text-align:left;">
        <div style="font-size:13px; font-weight:800; color:#60a5fa; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:10px;">{right[0]}</div>
        <div style="font-size:14px; color:#cdd5e3; line-height:1.55;">{right[1]}</div>
        <div style="font-size:13px; color:#8899bb; line-height:1.5; margin-top:8px;">{right[2]}</div>
      </div>
    </div>
    {f'<p style="font-size:13px; color:#8899bb; margin-top:8px; text-align:center;">{footer}</p>' if footer else ''}
  </div>
</section>
"""


def section_break(label: str, name: str, desc: str) -> str:
    return f"""<section class="section-break" data-title="{name}">
  <div class="section-break-inner">
    <div class="lab-title">{label}</div>
    <div class="lab-name">{name}</div>
    <div class="lab-desc">{desc}</div>
  </div>
</section>
"""


def applied_work(title: str, goal: str, body_html: str, repo_path: str,
                 timer_min: int, tool_url: str = "", tool_desc: str = "") -> str:
    timer = f'<div class="lab-timer">⏰ {timer_min} min</div>' if timer_min else ""
    cta = ""
    if tool_url:
        cta = f"""    <div style="text-align:center; margin-top:18px;">
      <a class="tool-btn" href="{tool_url}" target="_blank" rel="noopener">Open the tool ↗</a>
      <div style="font-size:12px; color:#8899bb; margin-top:6px;">{tool_desc}</div>
    </div>
"""
    return f"""<section data-title="{title}">
  {timer}
  <div class="inner">
    <div class="demo-tag tag-exercise">Applied Work</div>
    <h2>{title}</h2>
    <div class="subtitle">{goal}</div>
    {body_html}
{cta}
    <p class="repo-cta"><span style="color:#34d399;">📂</span> <strong>Go to your repo &rarr;</strong> <code>{repo_path}</code></p>
  </div>
</section>
"""


def case_study(title: str, headline: str, bet: str, crack: str, correct: str,
               footer: str = "") -> str:
    return f"""<section data-title="{title}">
  <div class="inner">
    <div class="demo-tag tag-case">Case Study</div>
    <h2>{headline}</h2>
    <div class="case-acts">
      <div class="case-act act-bet">
        <div class="ca-label">The Bet</div>
        <div class="ca-text">{bet}</div>
      </div>
      <div class="case-act act-crack">
        <div class="ca-label">The Crack</div>
        <div class="ca-text">{crack}</div>
      </div>
      <div class="case-act act-correct">
        <div class="ca-label">The Correction</div>
        <div class="ca-text">{correct}</div>
      </div>
    </div>
    {f'<p style="font-size:13px; color:#8899bb; text-align:center; margin-top:12px;">{footer}</p>' if footer else ''}
  </div>
</section>
"""


def takeaways(module_short: str, items: list[tuple[str, str]]) -> str:
    body = "\n".join(
        f'      <div class="takeaway-item"><p><strong>{t}</strong> {b}</p></div>'
        for t, b in items
    )
    return f"""<section data-title="Takeaways">
  <div class="inner">
    <div class="section-label">Key Takeaways</div>
    <h2>{module_short}</h2>
    <div class="takeaway-list">
{body}
    </div>
  </div>
</section>
"""


def extra_practice(items: list[tuple[str, str, str]], next_module_blurb: str) -> str:
    cards = "\n".join(
        f'      <div class="evidence-card"><div class="ec-label">{l}</div>'
        f'<div class="ec-company">{c}</div><div class="ec-text">{t}</div></div>'
        for l, c, t in items
    )
    return f"""<section data-title="Extra Practice">
  <div class="inner">
    <div class="section-label">Extra Practice</div>
    <h2>Optional: Go Deeper</h2>
    <div class="evidence-cards" style="margin:24px 0;">
{cards}
    </div>
    <div class="artifact-preview">
      <div class="ap-title">Next: {next_module_blurb}</div>
    </div>
  </div>
</section>
"""


def bridge(active_n: int, headline_a: str, headline_b: str, bring: str) -> str:
    nodes = []
    for n, _, label, _, _, _ in MODULES_META:
        if n < active_n:
            nodes.append(f'<div class="arc-node" style="background:rgba(52,211,153,0.15); border:1px solid rgba(52,211,153,0.3);"><div class="ad-num">M{n}</div>{label}</div>')
        elif n == active_n:
            nodes.append(f'<div class="arc-node active-node"><div class="ad-num">M{n}</div>{label}</div>')
        else:
            nodes.append(f'<div class="arc-node" style="opacity:0.5;"><div class="ad-num">M{n}</div>{label}</div>')
    flow = '<div class="arc-arrow">→</div>'.join(nodes)
    return f"""<section class="centered" data-title="Bridge to next">
  <div class="inner">
    <div class="section-label">Bridge to Module {active_n}</div>
    <h2>{headline_a}<br>{headline_b}</h2>
    <p style="font-size:14px; color:#8899bb; margin:12px 0 24px;"><strong>Bring:</strong> {bring}</p>
    <div class="arc-flow">{flow}</div>
  </div>
</section>
"""


def synthesis(active_n: int, deliverables: list[tuple[str, str]]) -> str:
    folders = []
    for n, _, _, _, _, folder in MODULES_META:
        if n < active_n:
            folders.append(
                f'<div style="background:rgba(52,211,153,0.05); border:1px solid rgba(52,211,153,0.12); border-radius:10px; padding:16px 20px; min-width:140px; text-align:left; opacity:0.55;">'
                f'<div style="font-size:13px; font-weight:800; color:#34d399;">{folder}/ ✓</div></div>'
            )
        elif n == active_n:
            inner = "".join(
                f'<div style="font-size:12px; color:#d8def0;">{name}</div>'
                f'<div style="font-size:12px; color:#7a7a9a; margin-top:2px;">{sub}</div>'
                for name, sub in deliverables
            )
            folders.append(
                f'<div style="background:rgba(52,211,153,0.08); border:1px solid rgba(52,211,153,0.2); border-radius:10px; padding:18px 22px; min-width:220px; text-align:left;">'
                f'<div style="font-size:13px; font-weight:800; color:#34d399; margin-bottom:6px;">{folder}/ ✓</div>'
                f'{inner}</div>'
            )
        else:
            folders.append(
                f'<div style="background:rgba(59,130,246,0.06); border:1px solid rgba(59,130,246,0.15); border-radius:10px; padding:16px 20px; min-width:140px; text-align:left;">'
                f'<div style="font-size:13px; font-weight:800; color:#60a5fa;">{folder}/</div>'
                f'<div style="font-size:11px; color:#7a7a9a; margin-top:4px;">M{n}</div></div>'
            )
    deliv_cells = "".join(
        f'<div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">'
        f'<div style="font-size:12px; font-weight:800; color:#6ee7b7; margin-bottom:6px;">{name}</div>'
        f'<div style="font-size:12px; color:#8899bb; line-height:1.45;">{sub}</div></div>'
        for name, sub in deliverables
    )
    return f"""<section class="centered" data-title="Synthesis">
  <div class="inner">
    <div class="section-label">Synthesis</div>
    <h2>Your Repo After Today</h2>
    <p class="subtitle">{active_n} of 6 components committed.</p>
    <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin:24px 0;">
      {''.join(folders)}
    </div>
    <div style="display:grid; grid-template-columns:repeat({len(deliverables)},1fr); gap:12px; max-width:820px; margin:0 auto;">
      {deliv_cells}
    </div>
  </div>
</section>
"""


def break_section() -> str:
    return """<section class="centered" data-title="Break">
  <div class="inner">
    <div class="demo-tag tag-break">Take a Beat</div>
    <h1 style="font-size:64px; color:#333; margin-top:40px;">☕</h1>
    <div class="subtitle" style="margin:16px auto;">Pause. Stretch. Refill. Back in five.</div>
  </div>
</section>
"""


def qa_section() -> str:
    return """<section class="centered" data-title="Q&A">
  <div class="inner">
    <h1 style="font-size:64px; color:#60a5fa; margin-bottom:24px;">Q&amp;A</h1>
    <p style="font-size:20px; color:#8899bb;">Park anything we can't unblock here in <code>#ai-pm-cohort</code>.</p>
    <p style="font-size:14px; color:#555; margin-top:20px;">Instructor responds in-thread within ~5 days.</p>
  </div>
</section>
"""


def notes_block(text: str) -> str:
    return f'<div class="notes"><h4>Speaker Notes</h4><p>{text}</p></div>'


def takeaway_block(text: str) -> str:
    return f'<div class="takeaway"><h4>Takeaway</h4><p>{text}</p></div>'


# ─────────────────────────────────────────────────────────────────────────────
# Page wrapper — head + style + body opening + JS + closing
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# Per-module content — section trees keyed by module number
# Each builder returns (instructor_sections, shareable_sections) so notes can
# be swapped for takeaways.
# ─────────────────────────────────────────────────────────────────────────────

def build_module_1():
    sections_inst, sections_share = [], []

    def add(html: str, note: str = "", takeaway: str = ""):
        # Instructor decks get speaker notes inside the section. Shareable decks
        # do not get a per-slide takeaway box — the dedicated Key Takeaways
        # section at the end is the consolidated takeaway.
        s_inst = html.replace("</section>", (notes_block(note) if note else "") + "\n</section>") if note else html
        sections_inst.append(s_inst)
        sections_share.append(html)

    # 1. Hero
    add(hero(
        title_lead="Drive AI-First Execution with",
        title_accent="Prompting",
        subtitle="Stop chatting with AI. Start configuring it.",
        waypoints=[
            ("Anatomise", "Five elements every production prompt declares."),
            ("Configure", "System prompts, hyperparameters, refusal rules — your levers."),
            ("Prototype", "Spin Juno PM up in Lovable in under 25 minutes."),
        ],
        out_line="Out: folder 01-prompting/ · system-prompt.md · lovable-prototype.md · toolkit.md.",
        module_n=1,
    ),
    note="Open hard. The course thesis lives or dies on the first five minutes. Read the M1 provocation aloud, then jump to the AI-First Mindset slide. Do not soften.",
    takeaway="Today is execution-focused, not foundational. By the end you will have prototyped Juno PM in Lovable, configured its system prompt, and committed both artifacts.")

    # 2. How This Module Runs
    add(how_it_runs(),
        note="Set expectations clearly. This is execution-focused, not foundational. Cert is based on the individual repo submission within 7 days of cohort end. Encourage everyone to fork the juno-project-template now.",
        takeaway="100% individual format. Fork juno-project-template now. Every exercise = self-review + AI-review + commit. Submit your fork URL within 7 days post-cohort.")

    # 3. Course Arc
    add(course_arc(active_n=1),
        note="Show the curriculum map briefly. Each module produces one committable artifact in a numbered folder. M6 finalises the README.",
        takeaway="Each module produces one committable artifact in a numbered folder. M6 finalises the README.")

    # 4. The Scenario
    scenario_body = """<div class="case-acts">
      <div class="case-act act-bet">
        <div class="ca-label">The Setup</div>
        <div class="ca-text"><strong>RocketShip</strong> · B2B SaaS for Enterprise Data Teams · You are the AI PM.</div>
      </div>
      <div class="case-act act-crack">
        <div class="ca-label">The Crack</div>
        <div class="ca-text">Wall of P0 escalations · thousands of stalled tickets · sales deals frozen · zero new headcount.</div>
      </div>
      <div class="case-act act-correct">
        <div class="ca-label">Your Move</div>
        <div class="ca-text">You can't scale yourself. You scale your <strong>judgment</strong>. You build <strong>Juno PM</strong>.</div>
      </div>
    </div>
    <p style="font-size:14px; color:#8899bb; text-align:center; margin-top:14px;">An AI Associate PM that lives <em>inside</em> Slack, Notion, and Jira — not as a standalone chat tab.</p>"""
    add(f"""<section data-title="Scenario">
  <div class="inner">
    <div class="demo-tag tag-recall">The Scenario</div>
    <h2>RocketShip is in Signal Collapse</h2>
    <div class="subtitle">A real situation, dropped on you Monday.</div>
    {scenario_body}
  </div>
</section>
""",
        note="This is the moment the course earns trust. Every learner has felt some version of this. Pause and let it land.",
        takeaway="The Juno PM scenario is the single thread across all six modules. Bring a real bet from your day job to make it click.")

    # 5. Provocation
    add(provocation(
        headline="Prompting is product configuration —<br>not chatting.",
        subtitle="Thumb-vote each line — then we unpack with real teams.",
        claims=[
            ("tf-false", "\"Prompts are throwaway — eng will rewrite them.\"",
             "Production AI products ship with versioned, evaled prompts. <em>OpenAI</em>, <em>Notion AI</em>, <em>Linear</em> — system prompts are the product surface."),
            ("tf-false", "\"If the model is good enough, the prompt doesn't matter.\"",
             "Same model, different prompt = different product. <em>GitHub Copilot</em> vs <em>Cursor</em> use the same base — the prompt is the moat."),
            ("tf-true", "\"Most PMs ship prompts that drift on day 2.\"",
             "Without anatomy + refusal rules + evals, prompts collapse the moment a user types something off-pattern."),
        ],
    ),
    note="Read each claim, get a thumb vote, click to reveal. Don't move on until everyone is bought into the configuration framing.",
    takeaway="The prompt IS the product surface. If you treat it as throwaway, your AI feature collapses on day 2.")

    # 6. Why every PM is now an AI PM (table)
    add(lecture_table(
        title="Every PM is now an AI PM",
        subtitle="The role is bending around one technical fact.",
        headers=["Traditional PM assumption", "What AI broke"],
        rows=[
            ["Outputs are deterministic", "Outputs are <em>probabilistic</em> — drift, hallucination, variance."],
            ["Spec is a doc", "Spec is a doc + prompt + data corpus + eval set."],
            ["UI is command-driven", "UI is intent-driven — and often invisible."],
            ["Workflows are sequential", "Workflows are <em>agentic</em> — branched, conditional, handed off."],
            ["Ship + monitor with analytics", "Ship + eval harness + human rubric + guardrails."],
        ],
        caption="This table is the spine of the certification. Each module reinforces one row.",
    ),
    note="Pin this table. Every later module reinforces one row. Spend a minute per row, no more.",
    takeaway="Five rows, five shifts. Each row maps to a later module — prompt (M1), strategy (M2), spec/RAG (M3), UX (M4), agents (M5), evals (M6).")

    # 7. Deterministic vs non-det
    add(two_column(
        title="Why this is hard",
        subtitle="Same input. Two different outputs. Welcome to product variance.",
        left=("Deterministic",
              "Same input → same output.",
              "SQL, regex, every API you've shipped before. Specs assume the system behaves."),
        right=("Non-Deterministic",
               "Same input → variable output.",
               "Every modern LLM, every agent. Specs must <em>shape</em> behaviour and <em>measure</em> it."),
        footer="Your job: <strong>narrow the variance</strong>. Configuration · guardrails · evals.",
    ),
    note="Quick anecdote — same prompt, two different ChatGPT responses live. Sells the variance point in 30 seconds.",
    takeaway="Determinism is gone. The PM job becomes: narrow variance through prompt, RAG, guardrails, and evals.")

    # 8. PM Toolkit (table)
    add(lecture_table(
        title="The PM's AI Toolkit",
        subtitle="Five categories every AI PM keeps bookmarked.",
        headers=["Category", "Pick one", "Use for"],
        rows=[
            ["Prompt-to-prototype", "Lovable · v0 · Cursor", "Working UI in minutes."],
            ["LLM playground", "OpenAI · Anthropic Console", "Tune prompts + hyperparameters."],
            ["No-code agent builder", "Langflow · n8n", "Wire agents and tool calls."],
            ["Eval / observability", "LangSmith · Phoenix · Braintrust", "Score, trace, regress."],
            ["Repo + version control", "GitHub", "Your <code>juno-pm/</code> lives here."],
        ],
        caption="Pin one tool per category. Commit to <code>01-prompting/toolkit.md</code>.",
        tag_label="Framework",
    ),
    note="Don't let this become a brand debate. The point is the categories. Make sure everyone has GitHub before they leave M1.",
    takeaway="The categories matter, not the brand. Pick one tool per row, commit to toolkit.md.")

    # 9. Section break — Lab 1
    add(section_break(
        label="Hands-On Lab · 10 min",
        name="Pick Your Toolkit",
        desc="Choose one tool per category. Commit toolkit.md. This is your launch pad for everything that follows.",
    ),
    note="Hands-on energy starts here. Walk the room. Most people overthink — push them to commit fast.",
    takeaway="10 minutes. Pick a tool per category, no debate. You can always swap later.")

    # 10. Applied Work — Toolkit Picker
    toolkit_body = """<table class="ref-table">
      <thead><tr><th>Category</th><th>Your pick</th><th>Why</th></tr></thead>
      <tbody>
        <tr><td>Prompt-to-prototype</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td></tr>
        <tr><td>LLM playground</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td></tr>
        <tr><td>No-code agent builder</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td></tr>
        <tr><td>Eval / observability</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td></tr>
        <tr><td>Repo + version control</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">GitHub</td><td style="color:#555; font-family:'IBM Plex Mono',monospace;">_____</td></tr>
      </tbody>
    </table>"""
    add(applied_work(
        title="Pick Your AI PM Stack",
        goal="One tool per category. One reason each. Commit and move on.",
        body_html=toolkit_body,
        repo_path="01-prompting/toolkit.md",
        timer_min=10,
        tool_url="M1 - PM Toolkit Picker.html",
        tool_desc="Auto-saves your picks · live markdown preview · copy-as-markdown.",
    ),
    note="Time-box hard. Push them to commit — perfectionism kills momentum on M1.",
    takeaway="Commit your picks even if imperfect. The act of choosing tools surfaces gaps you didn't know you had.")

    # 11. Anatomy of a high-quality prompt
    add(lecture_cards(
        title="Anatomy of a High-Quality Prompt",
        subtitle="Five elements every production prompt declares.",
        cards=[
            ("①", "Context", "Who the AI is, what system it lives in, what it knows."),
            ("②", "Task", "The explicit instruction (verb-first)."),
            ("③", "Constraints", "Must-not-do, format, scope. At least three."),
            ("④", "Output Format", "Schema, length, structure."),
            ("⑤", "Examples", "1–3 ideal pairs, when format matters."),
        ],
        footer="If any element is missing, your output drifts on day 2.",
        tag_label="Framework",
    ),
    note="Run the demo: vague prompt vs all-five prompt in ChatGPT. The diff sells itself.",
    takeaway="Five elements. Drop one and the prompt drifts. The Prompt Anatomy Builder forces you to fill all five.")

    # 12. Section break — Build the prompt
    add(section_break(
        label="Hands-On Lab · 15 min",
        name="Build a Prompt with Anatomy",
        desc="Open the Prompt Anatomy Builder. Watch the assembled prompt update live as you fill in each element.",
    ),
    note="Energy spike. Walk and look at screens. Most learners skip constraints — push them to write at least three.",
    takeaway="The tool forces all five elements. Use the live preview to feel how each element shapes the output.")

    # 13. Applied Work — Prompt Anatomy
    add(applied_work(
        title="Prompt Anatomy Builder",
        goal="Build a Juno-PM-style prompt, anatomy-first.",
        body_html="""<ul style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Pick a Juno scenario (synthesise escalations · draft a P0 spec · prioritise risks).</li>
      <li>Fill in Context · Task · Constraints (≥3) · Output Format · Examples.</li>
      <li>Watch the assembled prompt update live.</li>
      <li>Click <strong>Copy as markdown</strong> &rarr; commit to <code>01-prompting/anatomy-prompt.md</code>.</li>
      <li>Self-review with the on-tool checklist before you commit.</li>
    </ul>""",
        repo_path="01-prompting/anatomy-prompt.md",
        timer_min=15,
        tool_url="M1 - Prompt Anatomy Builder.html",
        tool_desc="Assembles the prompt as you type · checklist + AI-review prompt baked in.",
    ),
    note="5–10 min of build, then have everyone paste their constraints aloud. Most common miss: vague refusals (\"don't be wrong\") instead of testable rules.",
    takeaway="Your refusal rules need to be testable. \"Don't make up data\" is testable. \"Be helpful\" isn't.")

    # 14. Break
    add(break_section(),
        note="Hard 5-minute break. Reset.",
        takeaway="")

    # 15. Prompting techniques
    add(lecture_table(
        title="Prompting as Configuration",
        subtitle="Once you treat the prompt as configuration, every framework becomes obvious.",
        headers=["Technique", "Use when", "Example for Juno"],
        rows=[
            ["Zero-shot", "The model already knows the domain. Behaviour needs tuning, not knowledge.", "\"Summarise these 12 escalations in 3 bullets.\""],
            ["Few-shot", "You need a specific format or style — show 1–3 examples.", "Two ideal P0 spec templates as reference."],
            ["Chain-of-thought", "Multi-step reasoning required.", "Risk prioritisation: \"Think step-by-step before ranking.\""],
            ["System prompt + role", "Persona, persistent guardrails, organisation context.", "\"You are Juno, an Associate PM. You never execute, only flag.\""],
        ],
        caption="The technique you pick is a product decision, not a prompt-engineering trick.",
        tag_label="Framework",
    ),
    note="Tie each row to a Juno scenario. Few-shot for spec generation. Chain-of-thought for prioritisation. System prompt for persistent role.",
    takeaway="Picking the technique is product work. Few-shot for style, chain-of-thought for reasoning, system prompt for persona.")

    # 16. Hyperparameters
    add(two_column(
        title="The Two Dials PMs Should Know",
        subtitle="Top-p, frequency penalty, presence penalty — nice to know, not must-know.",
        left=("Temperature",
              "0 = deterministic-ish · 1+ = creative.",
              "Spec it for the job. Risk-watchdog Juno = low. Brainstorming Juno = high. PMs decide this — not engineers."),
        right=("Max Tokens / Length",
               "Cap it.",
               "Long outputs hide failures. Short outputs force prioritisation. Most consumer LLMs default too long."),
        footer="The point is awareness, not mastery. Know temperature exists. Know it's a product decision.",
    ),
    note="Awareness, not mastery. PMs should know temperature exists and that it's a product decision.",
    takeaway="Two dials, two product decisions. Don't let an engineer set them silently.")

    # 17. Section break — Configure Juno
    add(section_break(
        label="Hands-On Lab · 30 min · Final-Project Deliverable",
        name="Lab · Configure Juno's System Prompt",
        desc="The biggest piece of M1. This system prompt is one of your six final-project deliverables. Self-review and AI-review before you commit.",
    ),
    note="This is the M1 deliverable. Do NOT cut it short. Walk the room — most people forget refusal rules.",
    takeaway="This is a final-project deliverable. Treat it like a spec — every line ships.")

    # 18. System prompt configurator
    add(applied_work(
        title="Configure Juno's System Prompt",
        goal="Persona · scope · guardrails · output format · refusal rules — every field locked.",
        body_html="""<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M1 - System Prompt Configurator.html</code>.</li>
      <li>Fill all five sections. Refusal rules need at least three testable clauses.</li>
      <li>Click <strong>Copy as markdown</strong> &rarr; save to <code>01-prompting/system-prompt.md</code>.</li>
      <li><strong>Self-review</strong> against the on-tool checklist.</li>
      <li><strong>AI-review</strong>: paste your prompt + the verbatim AI-review prompt into ChatGPT or Claude.</li>
      <li><strong>Async share</strong>: commit · push · post the file link in <code>#ai-pm-cohort</code> with a 1-paragraph reflection.</li>
    </ol>""",
        repo_path="01-prompting/system-prompt.md",
        timer_min=30,
        tool_url="M1 - System Prompt Configurator.html",
        tool_desc="Five-element system-prompt builder · self-review · AI-review prompt.",
    ),
    note="The biggest miss: people forget refusal rules. \"Don't make up data,\" \"Always cite the ticket ID.\" Push them.",
    takeaway="Refusal rules are the difference between a demo and a product. Three is the minimum.")

    # 19. Optimization decision framework
    add(lecture_table(
        title="The Optimisation Decision Framework",
        subtitle="Three levers. Cheapest first. If prompt fixes it, don't build infra.",
        headers=["Lever", "Try when", "Cost / time"],
        rows=[
            ["<strong>Prompt</strong>", "Model already knows the domain. Behaviour needs tuning, not knowledge.", "Minutes. Almost free."],
            ["<strong>RAG</strong>", "Need to ground the model in <em>your</em> data. (M3 lives here.)", "Days. Real infra cost."],
            ["<strong>Fine-tune</strong>", "Style/format/behaviour matters more than retrieval. Last resort.", "Weeks. Real infra + training cost."],
        ],
        caption="<em>If you can fix it with the prompt, do not build infra.</em>",
        tag_label="Framework",
    ),
    note="This sets up M3 (RAG) and previews fine-tuning. Most learners will never own a fine-tune — they need the decision criteria.",
    takeaway="Prompt → RAG → fine-tune. Cheapest first. Most teams over-engineer step 2 before exhausting step 1.")

    # 20. Section break — Lovable Prototype
    add(section_break(
        label="Hands-On Lab · 25 min",
        name="Prototype Juno PM in Lovable",
        desc="A functional URL by the end. Not a polished product. Speed is the lesson.",
    ),
    note="High-energy moment. Time-box hard. v0 or Cursor as fallback if Lovable misbehaves.",
    takeaway="A URL is the deliverable. Polish is not.")

    # 21. Lovable Lab
    add(applied_work(
        title="Prompt-to-Prototype Your Copilot",
        goal="A working URL for Juno PM by the end of this section.",
        body_html="""<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open Lovable. Sign in.</li>
      <li>Paste the seed prompt (next section).</li>
      <li>Iterate <em>once</em>: change the UI shape, the colors, or the homepage copy.</li>
      <li>Copy the shareable URL.</li>
      <li>Commit the URL to <code>01-prompting/lovable-prototype.md</code> in your <code>juno-pm/</code> fork.</li>
    </ol>
    <p style="font-size:13px; color:#8899bb; text-align:center; margin-top:10px;">Goal: a functional URL. Not a polished product.</p>""",
        repo_path="01-prompting/lovable-prototype.md",
        timer_min=25,
        tool_url="",
        tool_desc="",
    ),
    note="Walk the room. Anyone whose Lovable misbehaves: switch to v0 or Cursor. The tangible URL is what matters.",
    takeaway="The URL is the artifact. Polish later. Feel the speed of prompt-to-prototype.")

    # 22. Seed prompt
    add(f"""<section data-title="Seed Prompt">
  <div class="inner">
    <div class="demo-tag tag-framework">Seed Prompt</div>
    <h2>The Juno PM Seed Prompt</h2>
    <pre style="background:rgba(18,65,176,0.1); border:1px solid rgba(59,130,246,0.2); border-radius:12px; padding:18px; overflow:auto; font-size:13.5px; line-height:1.6; color:#cdd5e3; font-family:'IBM Plex Mono', monospace; text-align:left; margin-top:12px;">Build a web app called "Juno PM". It is the homepage for an AI Associate PM that lives inside Slack, Notion, and Jira. The homepage has:
- A hero strip with the tagline "Scale your judgment, not yourself"
- A three-column section explaining the pillars: Synthesize Insights, Draft Specs, Prioritize Risks
- A chat-style input at the bottom with placeholder text "Paste a wall of escalations..."
- A side panel showing the last 3 risks Juno flagged

Use a calm professional palette — deep navy, off-white, one accent color. No emojis.</pre>
    <p style="font-size:13px; color:#8899bb; text-align:center; margin-top:14px;">Iterate once. Then stop. The point is feeling the speed.</p>
  </div>
</section>
""",
    note="Encourage them to keep iterating after class. The point in the room is feeling the speed.",
    takeaway="One iteration in class. Endless iterations after. The seed prompt unlocks ~80% of the surface in two minutes.")

    # 23. PM Artifact is changing
    add(lecture_cards(
        title="The PM Artifact Is Changing",
        subtitle="In an AI-native team, the PRD is no longer the source of truth.",
        cards=[
            ("📄", "PRD", "What & why."),
            ("🤖", "System Prompt", "How the AI behaves. (M1.)"),
            ("📚", "Data Corpus + Retrieval", "What it knows. (M3.)"),
            ("✅", "Eval Set", "How we know it's working. (M6.)"),
        ],
        footer="By M6 you commit all four to <code>juno-pm/</code>.",
        tag_label="Lecture",
    ),
    note="Preview the arc. Each artifact gets built in its own module. The repo is the throughline.",
    takeaway="Four artifacts make up an AI product. M1 ships the system prompt. M3 ships the data. M6 ships the evals.")

    # 24. Synthesis
    add(synthesis(
        active_n=1,
        deliverables=[
            ("system-prompt.md", "Juno's persona · scope · refusal rules"),
            ("anatomy-prompt.md", "Five-element prompt for one Juno task"),
            ("lovable-prototype.md", "URL of your prototype"),
            ("toolkit.md", "Your 5-category PM AI stack"),
        ],
    ),
    note="Show the repo. Make sure everyone has committed at least one artifact before they leave.",
    takeaway="Component 1 of 6 committed. Five to go.")

    # 25. Bridge to M2
    add(bridge(
        active_n=2,
        headline_a="Tactics into",
        headline_b="strategy.",
        bring="Your repo with 01-prompting/ committed · one real AI bet from your day job · thick skin.",
    ),
    note="The \"real bet from your day job\" line is critical — M2 lands harder when learners have skin in the game.",
    takeaway="M2 turns prompts into a strategy your CFO can sign off on.")

    # 26. Takeaways
    add(takeaways(
        module_short="Drive AI-First Execution with Prompting",
        items=[
            ("Prompting is configuration, not chat.", "The prompt is a product surface — versioned, evaled, reviewed."),
            ("Five elements or it drifts.", "Context · task · constraints · output · examples. Drop one, the output collapses."),
            ("Cheapest lever first.", "Prompt → RAG → fine-tune. Don't build infra to fix something the prompt would solve."),
            ("Prototype to feel the speed.", "Lovable + a seed prompt = a working surface in 25 minutes."),
            ("The repo is the throughline.", "By M6 you commit four artifacts: PRD · system prompt · data + retrieval · eval set."),
        ],
    ),
    note="Hold the line on time. Read each takeaway aloud.",
    takeaway="Five takeaways. The repo is the deliverable.")

    # 27. Extra Practice
    add(extra_practice(
        items=[
            ("Practice 1", "Refactor a Real Prompt You Use Every Week",
             "Pick a prompt you re-paste constantly. Re-write it through the 5-element anatomy. Commit to <code>01-prompting/anatomy-prompt.md</code> with a before/after."),
            ("Practice 2", "Ship a Second Lovable Surface",
             "Build a second view of Juno (the side panel · the risk-detail page). Commit the URL alongside your first."),
        ],
        next_module_blurb="Module 2 — Strategically Plan AI-Driven Solutions. Bring one bet from your day job.",
    ),
    note="Optional but encouraged. Async showcase via Loom + repo URL in #ai-pm-cohort.",
    takeaway="Optional. Async share via Loom + repo URL.")

    # 28. Q&A
    add(qa_section(),
        note="Hard 5-min cap. Anything that doesn't fit goes to Slack.",
        takeaway="")

    return sections_inst, sections_share


def _add_builder(sections_inst, sections_share):
    def add(html: str, note: str = "", takeaway: str = ""):
        # Instructor decks: per-slide speaker notes (kept).
        # Shareable decks: no per-slide takeaway box — the dedicated
        # Key Takeaways section at the end is the consolidated takeaway.
        s_inst = html.replace("</section>", (notes_block(note) if note else "") + "\n</section>") if note else html
        sections_inst.append(s_inst)
        sections_share.append(html)
    return add


def recall_section(prev_module_short: str, items: list[tuple[str, str]], bridge_line: str) -> str:
    body = "\n".join(
        f'      <div class="waypoint"><div class="waypoint-num" style="background:#059669;">✓</div>'
        f'<div class="waypoint-text"><div class="wt-title">{t}</div>'
        f'<div class="wt-desc">{d}</div></div></div>'
        for t, d in items
    )
    return f"""<section data-title="Recall">
  <div class="inner">
    <div class="demo-tag tag-recall">Recall from {prev_module_short}</div>
    <h2>What You Brought Today</h2>
    <div class="waypoints">
{body}
    </div>
    <div style="background:rgba(248,113,113,0.06); border:1px solid rgba(248,113,113,0.15); border-radius:10px; padding:16px; margin-top:16px; text-align:center;">
      <p style="font-size:15px; font-weight:700; color:#fca5a5;">{bridge_line}</p>
    </div>
  </div>
</section>
"""


def build_module_2():
    si, sh = [], []
    add = _add_builder(si, sh)

    add(hero("Strategically Plan", "AI-Driven Solutions",
             "Most AI features are fake-good. Pressure-test the bet before you waste a quarter.",
             [("Filter", "Four value frames separate fake-good from boring-killer."),
              ("Score", "AI Solution Decision Matrix: 5 axes, 1–5, board-ready."),
              ("Pitch", "AI Strategy One-Pager — seven blocks on one page.")],
             "Out: folder 02-strategy/ · decision-matrix.md · strategy-one-pager.md.", 2),
        note="Open with the provocation. Pull up the M1 reflection in #ai-pm-cohort — call out 2-3 strong ones to set the tone.",
        takeaway="By the end you have a scored bet and a one-pager that survives a board challenge.")

    add(how_it_runs(), note="Same expectations as M1.", takeaway="Solo · self-review · AI-review · async share.")
    add(course_arc(2), note="Show progression from M1.", takeaway="M2 turns prompts into a defensible bet.")

    add(recall_section("Module 1",
                       [("01-prompting/system-prompt.md", "Juno's persona, scope, refusal rules"),
                        ("01-prompting/anatomy-prompt.md", "Five-element prompt for one Juno task"),
                        ("01-prompting/lovable-prototype.md", "URL of your Juno prototype"),
                        ("01-prompting/toolkit.md", "Your AI PM stack — 5 categories")],
                       "M1 was tactics. M2 is strategy. Same Juno. Bigger frame."),
        note="Make sure everyone has M1 committed. If not, give them 2 min to commit before continuing.",
        takeaway="Tactics committed. Strategy starts now.")

    add(provocation(
        "AI is a bet, not a feature.",
        "Vote, then we unpack with real cases.",
        [("tf-true", "\"Most AI features die before product-market fit because they were fake-good.\"",
          "Demos brilliantly · no clear value frame · loses to a platform feature in 6 months. The four-frame filter catches them early."),
         ("tf-false", "\"If we ship it and users use it, the bet was right.\"",
          "Usage ≠ value. <em>Notion AI</em> tracked usage, then audited which of those uses survived a 3× cost stress test."),
         ("tf-partial", "\"PMs decide autonomy levels.\"",
          "PMs <em>should</em>. Most teams default autonomy to whatever engineering ships. That's a strategic gap.")]),
        note="Hold thumb votes. Most learners will mis-vote the third — push them.",
        takeaway="Autonomy is a strategic decision. Don't default it.")

    add(two_column("Fake-Good vs Boring Killer",
                   "Two simple filters keep a quarter from disappearing.",
                   ("Fake-Good",
                    "Demos brilliantly.",
                    "No clear value frame · loses to a platform feature in 6 months · \"Generate this summary.\""),
                   ("Boring Killer",
                    "Looks dull on a slide.",
                    "Ladders to a real value frame · survives a 3× cost stress test · \"Cut on-call escalations 40%.\""),
                   footer="Two-question filter: (a) does it ladder to a value frame? (b) survives a 3× cost stress? If either no — it's fake-good."),
        note="The 3× cost stress test is the headline. Use it for every bet learners pitch.",
        takeaway="Two questions kill 80% of bad AI bets in 60 seconds.")

    add(lecture_cards("The Four AI Value Propositions",
                      "If your bet doesn't ladder to one of these — it's fake-good.",
                      [("💸", "Cost", "Replace human labour. Lower OPEX per unit of work."),
                       ("📈", "Revenue", "New product surfaces, new willingness to pay."),
                       ("🛡", "Risk", "Catch what humans miss — compliance, fraud, escalation."),
                       ("✨", "Delight", "Anticipate intent, reduce friction, surprise positively.")],
                      "For Juno: <strong>Risk</strong> is primary. Cost is secondary. Revenue and Delight come later.",
                      tag_label="Framework"),
        note="Force learners to label Juno's bet. Most land on Cost+Risk; push for the primary.",
        takeaway="Pick the primary frame. That's the frame the CFO will probe.")

    add(lecture_table("The Three-Layer Model",
                      "PMs own all three. Most fail at the Mechanic layer.",
                      ["Layer", "Question", "For Juno PM"],
                      [["<strong>Strategy</strong>", "Which bet? Why now? What value frame?",
                        "Risk mitigation — RocketShip is in Signal Collapse"],
                       ["<strong>Mechanic</strong>", "What does the product actually do?",
                        "Synthesise + draft + prioritise, inside Slack/Notion/Jira"],
                       ["<strong>Implementation</strong>", "Prompt / RAG / fine-tune / agent?",
                        "System prompt + RAG over RocketShip corpus + bounded agent"]],
                      caption="Use the Three-Layer Mapper tool to expose where strategy ↔ implementation drifts.",
                      tag_label="Framework"),
        note="Use the Three-Layer Mapper live. Show how easy it is to skip Mechanic.",
        takeaway="The Mechanic layer is where most bets get hand-waved.")

    add(section_break("Hands-On Lab · 25 min", "Map Juno's Strategic Bet",
                      "Score Juno's three pillars on Job × Risk × Autonomy. Plot each on Suggest / Draft / Execute / Operate."),
        note="High focus. Walk the room. Push back on uniform autonomy across pillars.",
        takeaway="Three pillars · three different autonomy levels — almost always.")

    add(applied_work("Three-Layer Model Mapper",
                     "Score Job × Risk × Autonomy for each Juno pillar.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M2 - Three-Layer Model Mapper.html</code>.</li>
      <li>For Synthesise · Draft · Prioritise — score Job × Risk × Autonomy.</li>
      <li>Plot each on Suggest / Draft / Execute / Operate.</li>
      <li>Copy as markdown &rarr; <code>02-strategy/decision-matrix.md</code> (Three-Layer + autonomy section).</li>
      <li>Self-review. Then run the AI-review prompt in ChatGPT/Claude.</li>
    </ol>""",
                     "02-strategy/decision-matrix.md", 25,
                     "M2 - Three-Layer Model Mapper.html",
                     "Maps Job × Risk → Autonomy · live preview · AI-review prompt baked in."),
        note="Variance is realistic. Push back on uniform autonomy.",
        takeaway="Variance across pillars is healthy.")

    add(lecture_cards("Suggest → Draft → Execute → Operate",
                      "As autonomy rises, error cost skyrockets. High-risk jobs cap at Draft.",
                      [("①", "Suggest", "\"Here's an idea.\" Human decides. Lowest risk, lowest leverage."),
                       ("②", "Draft", "\"Here's a v0.1.\" Human edits + approves. Most AI PM work lives here."),
                       ("③", "Execute", "AI acts; human reviews after. Requires explicit guardrails."),
                       ("④", "Operate", "AI runs long horizons. Requires explicit handoff rules (M5).")],
                      "For Juno: Synthesise = Execute · Draft = Draft · Prioritise = Suggest, then Draft once trust is earned.",
                      tag_label="Framework"),
        note="Tie each level to a Juno pillar.",
        takeaway="Pick the lowest level that delivers the job.")

    add(break_section(), note="5-min break.", takeaway="")

    add(lecture_table("AI Solution Decision Matrix",
                      "Pressure-test every proposed AI bet on five axes, scored 1–5.",
                      ["Axis", "Question", "1 (red flag)", "5 (boring killer)"],
                      [["Value clarity", "Does it ladder to a value frame?", "Vague", "Quantified $$$ or $$ saved"],
                       ["Technical feasibility", "Can current models do this well enough?",
                        "Novel research", "Standard pattern, off-the-shelf"],
                       ["Data availability", "Do you have / can you get the corpus?",
                        "No corpus", "Clean labelled corpus exists"],
                       ["Risk tolerance", "Can you tolerate wrong outputs?",
                        "Regulatory / reputational", "Internal, reversible"],
                       ["Strategic fit", "Does it earn company oxygen?",
                        "Pet project", "Directly serves a top-3 priority"]],
                      caption="<strong>Score &lt; 3 average = don't ship. Score 4+ on all five = boring killer.</strong>",
                      tag_label="Framework"),
        note="This is the artefact that outlives the course. Re-usable for every future bet.",
        takeaway="The matrix is reusable forever. Score every future bet.")

    add(applied_work("Score Your Juno Bet (and a real one)",
                     "Use the matrix on Juno + the bet you brought from M1 homework.",
                     """<p style="text-align:left; max-width:720px; margin:0 auto;">
      Open <code>M2 - AI Solution Decision Matrix.html</code>. Use the sliders. Watch the verdict update. Copy as markdown &rarr; <code>02-strategy/decision-matrix.md</code>.
    </p>
    <p style="text-align:left; max-width:720px; margin:14px auto 0; color:#fca5a5; font-weight:600;">If the bet scores &lt; 3 average — what would have to be true to raise it? That's the gap to close before you pitch.</p>""",
                     "02-strategy/decision-matrix.md", 15,
                     "M2 - AI Solution Decision Matrix.html",
                     "Five-axis sliders · live verdict · copy-as-markdown."),
        note="If a bet scores low, ask what would have to be true to raise it. That's the gap.",
        takeaway="A low score isn't a kill — it's a list of gaps to close.")

    add(case_study("Klarna",
                   "Klarna's AI Assistant",
                   "<strong>Klarna</strong> · Replace 700 customer-service reps with a single LLM-powered agent.",
                   "Headlines say 700 jobs replaced. Real story = handoff rate. Some queries still escalate to humans — and which ones matters more than the percentage.",
                   "Bet survives: agent for low-risk · human for novel/high-stakes · explicit boundary contract.",
                   "Lesson: the boundary between AI and human is the product."),
        note="The handoff rate is the headline. Don't let the 700-jobs story dominate.",
        takeaway="The handoff rule, not the automation rate, is what makes the product safe to ship.")

    add(lecture_cards("Responsible AI as Strategic Lever",
                      "Each guardrail is a sales asset for enterprise buyers — not just a cost.",
                      [("⚖️", "Compliance", "Regulatory (GDPR · EU AI Act · sector-specific)."),
                       ("🛑", "Safety", "Content · prompt injection · misuse."),
                       ("🔁", "Reliability", "Uptime · fallback paths · graceful degradation."),
                       ("📣", "Reputation", "Public failure scenarios + response playbook.")],
                      "Tee up M5 (governance). Today: factor risk into the bet, not the policy.",
                      tag_label="Lecture"),
        note="M5 will operationalise these. Today's job is making them part of the bet.",
        takeaway="Risk is a strategic lever. Spec it now; operationalise it in M5.")

    add(section_break("Hands-On Lab · 30 min · Final-Project Deliverable",
                      "Build Juno's AI Strategy One-Pager",
                      "Seven blocks. One page. The deliverable that survives a board challenge."),
        note="Highest-stakes M2 deliverable. Walk the room.",
        takeaway="One page. Seven blocks. CFO-ready.")

    add(applied_work("AI Strategy One-Pager Builder",
                     "Bet · User · Mechanic · Autonomy · Approach · Risk · Metric.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M2 - AI Strategy One-Pager Builder.html</code>.</li>
      <li>Fill the 7 blocks for Juno PM. The bet is one sentence — name the value frame.</li>
      <li>Copy as markdown &rarr; <code>02-strategy/strategy-one-pager.md</code>.</li>
      <li>Self-review with the on-tool checklist.</li>
      <li>AI-review: paste into ChatGPT/Claude with the verbatim review prompt.</li>
      <li>Async share: commit · push · post the file link in <code>#ai-pm-cohort</code>.</li>
    </ol>""",
                     "02-strategy/strategy-one-pager.md", 30,
                     "M2 - AI Strategy One-Pager Builder.html",
                     "Seven-block one-pager · self-review · AI-review prompt."),
        note="The success metric is where most learners get vague. Push for measurable in 30 days.",
        takeaway="Vague metric = no metric. Measurable in 30 days or rewrite.")

    add(synthesis(2, [
        ("decision-matrix.md", "Three-Layer + 5-axis pressure test"),
        ("strategy-one-pager.md", "Seven-block bet · CFO-ready"),
    ]),
        note="Two artifacts now committed for the final project.",
        takeaway="Two strategy artifacts shipped. Five components to go.")

    add(bridge(3, "Bet justified.", "Spec it.",
               "Your repo with 02-strategy/ committed · the corpus you'd need for Juno (Slack? Notion? Jira? Tickets?)."),
        note="Tee up the corpus question.",
        takeaway="M3 turns the bet into a spec an LLM can execute.")

    add(takeaways("Strategically Plan AI-Driven Solutions",
                  [("Most AI features are fake-good.",
                    "Filter with the four value frames. If it doesn't ladder, kill it."),
                   ("Three layers, all yours.",
                    "Strategy · Mechanic · Implementation. Most teams skip Mechanic."),
                   ("Autonomy is a strategic decision.",
                    "Job × Risk → Suggest / Draft / Execute / Operate. Don't default it."),
                   ("The matrix is reusable.",
                    "Score every future AI bet on the same 5 axes. < 3 = don't ship."),
                   ("The one-pager is the pitch.",
                    "Seven blocks · one page · survives a board challenge.")]),
        note="Wrap on time. Tee up M3 (corpus).",
        takeaway="Five takeaways. The matrix and the one-pager are reusable beyond Juno.")

    add(extra_practice([
        ("Practice 1", "Score a Real Bet on Your Roadmap",
         "Pick the AI bet your team is currently selling internally. Score it on all 5 axes. Commit alongside the Juno score."),
        ("Practice 2", "Stress-Test Your One-Pager",
         "Have ChatGPT play three personas (CFO · CISO · skeptical Eng VP). Note where the one-pager cracks. Commit a v2."),
    ], "Module 3 — Build the AI PRD: RAG, Specs, Decisions. Bring the corpus you'd need for Juno."),
        note="Async showcase optional. Loom + repo URL.",
        takeaway="Practice on a real bet. The matrix becomes muscle memory.")

    add(qa_section(), note="5-min cap.", takeaway="")

    return si, sh


# === M3 ===
def build_module_3():
    si, sh = [], []
    add = _add_builder(si, sh)

    add(hero("Build the AI PRD:", "RAG, Specs, Decisions",
             "Your PRD is missing the data corpus. That's not the engineer's problem — it's yours.",
             [("Context", "PMs own context engineering, not just prompts."),
              ("Architect", "Five questions pick your RAG architecture."),
              ("Spec", "AI PRD = traditional PRD + 3 new sections.")],
             "Out: folder 03-rag-prd/ · ai-prd.md · before-after-rag.md.", 3),
        note="This module breaks the \"spec is a doc\" assumption. Spec is now doc + prompt + corpus + eval.",
        takeaway="Today you commit a real AI PRD with explicit RAG architecture choices.")

    add(how_it_runs(), note="", takeaway="Solo · self-review · AI-review · async share.")
    add(course_arc(3), note="", takeaway="M3 spec's the data and the architecture.")

    add(recall_section("Module 2",
                       [("02-strategy/decision-matrix.md", "Three-Layer + 5-axis pressure test"),
                        ("02-strategy/strategy-one-pager.md", "Bet justified · seven blocks · CFO-ready"),
                        ("Real bet (homework)", "Brought from your day job — pressure-tested live")],
                       "Strategy committed. Now the spec — including the data."),
        note="Confirm M2 commits. Anyone missing — 2 min to commit.",
        takeaway="Bet justified. Spec time.")

    add(provocation(
        "Engineers own retrieval mechanics.<br>You own what should be retrieved.",
        "Vote, then we walk it.",
        [("tf-true", "\"Most AI PRDs are missing the corpus section entirely.\"",
          "Audit any PRD on your team. The corpus paragraph is usually \"internal docs.\" That's not a spec — that's a hand-wave."),
         ("tf-false", "\"Bigger context windows kill RAG.\"",
          "1M-token windows change the trade-off — they don't kill it. Latency · cost · needle-in-haystack recall all degrade with size."),
         ("tf-true", "\"Without an eval plan, the PRD is fiction.\"",
          "You've shipped a probabilistic system with no idea how to know it's working. M6 turns the eval stub into reality.")]),
        note="The third claim is the M6 setup. Don't go deep yet.",
        takeaway="No corpus + no eval = no spec.")

    add(lecture_table("Prompt → Context engineering",
                      "PMs own context. Engineers own retrieval mechanics.",
                      ["Prompt engineering", "Context engineering"],
                      [["Words to the model", "Data assembled <em>around</em> the prompt"],
                       ["Engineer / PM, shared", "<strong>PM-owned</strong>"],
                       ["Tunes behaviour", "Grounds output in <em>your</em> reality"]],
                      caption="If the PM doesn't own context strategy — no one does.",
                      tag_label="Framework"),
        note="The re-allocation is the headline.",
        takeaway="Engineers retrieve. PMs decide what to retrieve and why.")

    add(lecture_cards("RAG in Four Steps",
                      "Retrieval-Augmented Generation. Reduces hallucination. Adds cost + latency.",
                      [("①", "Index", "Chunk the corpus · embed each chunk · store in a vector DB."),
                       ("②", "Retrieve", "At runtime, fetch relevant chunks for the query."),
                       ("③", "Augment", "Inject retrieved chunks into the prompt as context."),
                       ("④", "Generate", "Model responds, grounded in your data.")],
                      "PM trade-off: <em>what</em> to retrieve and <em>when</em>.",
                      tag_label="Lecture"),
        note="Whiteboard a before/after RAG answer. Sells RAG in 60 seconds.",
        takeaway="Four steps, one PM lever: what gets retrieved.")

    add(lecture_table("Three RAG Trade-offs",
                      "The right context at the right time beats more context every time.",
                      ["Trade-off", "Lever", "Watch"],
                      [["<strong>Cost</strong>", "Embedding model size · storage · retrieval calls/query", "$/query at production scale"],
                       ["<strong>Speed</strong>", "k (top-k) · reranker · hybrid retrieval · parallelism", "p95 latency budget"],
                       ["<strong>Accuracy</strong>", "Chunk size · k · reranker quality · query rewriting", "Eval score on golden set (M6)"]],
                      caption="Most learners optimise for accuracy and forget cost. Don't.",
                      tag_label="Framework"),
        note="Pick one Juno scenario, walk it across all three.",
        takeaway="Three trade-offs. Optimise the trade-off, not just one axis.")

    add(section_break("Hands-On Lab · 25 min", "Improve Juno with RAG",
                      "Ground Juno in the RocketShip corpus. Compare before/after. Save the diff."),
        note="Diagnostic lab. Encourage learners to write down the before/after diff.",
        takeaway="Before/after is a snippet you'll reuse forever.")

    add(applied_work("Ground Juno in Real Data",
                     "See \"no longer guessing — now citing.\"",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open your Juno Lovable prototype (from M1).</li>
      <li>Paste the <strong>RocketShip Strategy One-Pager</strong> corpus into Lovable's context (or use the lab's seed corpus).</li>
      <li>Ask Juno: <em>"What are the top 3 risks for our Q3 enterprise tier launch, with citations?"</em></li>
      <li>Compare the answer <em>before</em> grounding vs <em>after</em>.</li>
      <li>Save both answers to <code>03-rag-prd/before-after-rag.md</code>.</li>
    </ol>""",
                     "03-rag-prd/before-after-rag.md", 25),
        note="The diff is the lesson. Ask 2-3 learners to read theirs aloud.",
        takeaway="Citations are the trust signal. Before/after = your sales demo.")

    add(lecture_cards("Five Questions Pick Your Architecture",
                      "Most teams pick chunk-size and rerank by gut. Don't.",
                      [("⏱", "Data freshness", "How stale can context be? Seconds · hours · days."),
                       ("📦", "Corpus size", "Fits in context window vs must be retrieved?"),
                       ("⚡", "Latency budget", "How fast must this return? p95 in seconds."),
                       ("🔁", "Update cadence", "Read-heavy or write-heavy?"),
                       ("🔒", "Privacy / tenancy", "Multi-tenant or per-user corpus?")],
                      "For Juno: stale ≤ 1h OK · corpus too big · p95 ≤ 4s · write-heavy · per-team tenancy.",
                      tag_label="Framework"),
        note="Use the RAG Decider tool live for 2 minutes.",
        takeaway="Five answers, one architecture. The tool maps them.")

    add(applied_work("RAG Architecture Decider",
                     "Answer five questions for Juno. The tool emits an opinionated architecture.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M3 - RAG Architecture Decider.html</code>.</li>
      <li>Answer the 5 questions for Juno.</li>
      <li>Tool outputs chunk size · retrieval strategy · reranker · refresh cadence.</li>
      <li>Copy the recommendation as markdown — you'll paste it into the AI PRD next.</li>
    </ol>""",
                     "03-rag-prd/ai-prd.md (paste into Data corpus + retrieval section)", 10,
                     "M3 - RAG Architecture Decider.html",
                     "Five-question wizard · opinionated output · copy-as-markdown."),
        note="The recommendation is opinionated — encourage disagreement when learners have context.",
        takeaway="Disagree with the tool when you have context it doesn't.")

    add(break_section(), note="5-min break.", takeaway="")

    add(lecture_cards("Three New Sections in an AI PRD",
                      "Skip these and you ship a probabilistic system with no idea how it fails.",
                      [("📚", "Data corpus + retrieval", "What data, indexed how, retrieved how."),
                       ("✅", "Eval plan", "Golden set · success bar · regression cadence (M6)."),
                       ("🛑", "Failure modes + guardrails", "What can go wrong + what blocks it.")],
                      "Engineers can build any of it. Only the PM can decide what's in scope.",
                      tag_label="Framework"),
        note="These three sections live or die on PM craft.",
        takeaway="Three sections. All yours.")

    add(lecture_cards("PM Checklist for Corpus Readiness",
                      "The slide that wakes the legal team up.",
                      [("📂", "Source identification", "Which docs · channels · tickets · transcripts?"),
                       ("📏", "Quality bar", "Min freshness · accuracy · completeness?"),
                       ("🔐", "PII handling", "Redact · exclude · pseudonymise?"),
                       ("👥", "Permissions", "Does the corpus respect user-level access?"),
                       ("🔁", "Update cadence", "How often does the index refresh?")],
                      "Get learners thinking about <em>who</em> should be able to query <em>which slice</em>.",
                      tag_label="Framework"),
        note="Push them on permissions. \"Anyone in the company\" is not an answer.",
        takeaway="Permissions are a product decision. Spec them.")

    add(section_break("Hands-On Lab · 30 min · Final-Project Deliverable",
                      "Specify Juno's RAG Architecture in Your AI PRD",
                      "Carry over from M2. Add corpus + retrieval + failure modes. Eval is a stub for M6."),
        note="The M3 deliverable. Don't cut short.",
        takeaway="Final-project deliverable.")

    add(applied_work("AI PRD Builder",
                     "Interactive port of the original AI PRD Template, with the three new AI sections baked in.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M3 - AI PRD Builder.html</code>.</li>
      <li>Carry over <strong>bet · mechanic · autonomy</strong> from your M2 one-pager.</li>
      <li>Fill <strong>Data corpus + retrieval strategy</strong> (paste from the RAG Decider).</li>
      <li>Fill <strong>Failure modes + guardrails</strong> — at least 3 modes, each paired with a guardrail.</li>
      <li>Leave <strong>Eval plan</strong> as a stub — M6 fills it.</li>
      <li>Copy as markdown &rarr; <code>03-rag-prd/ai-prd.md</code>.</li>
      <li>Self-review · AI-review · commit · share in <code>#ai-pm-cohort</code>.</li>
    </ol>""",
                     "03-rag-prd/ai-prd.md", 30,
                     "M3 - AI PRD Builder.html",
                     "Full PRD builder · 3 new AI sections · self-review · AI-review."),
        note="Push back on anyone who skips failure modes. \"Hallucination\" alone is not a list.",
        takeaway="Three concrete failure modes — each with a guardrail. Otherwise the spec is fiction.")

    add(synthesis(3, [("ai-prd.md", "Bet · mechanic · autonomy + 3 new AI sections"),
                       ("before-after-rag.md", "Diagnostic diff · sales demo")]),
        note="Three components committed.",
        takeaway="Half the repo is built. UX next.")

    add(bridge(4, "The spec is solid.", "Now the surface.",
               "Your repo with 03-rag-prd/ committed · screenshot of the worst AI UX you used this week."),
        note="Make sure they bring a screenshot.",
        takeaway="M4 wraps the spec in an interface users will trust.")

    add(takeaways("Build the AI PRD: RAG, Specs, Decisions",
                  [("Prompt → context engineering.",
                    "PMs own what gets retrieved. Engineers own how."),
                   ("AI PRD = traditional PRD + 3 new sections.",
                    "Data corpus · eval plan · failure modes + guardrails."),
                   ("Right context > more context.",
                    "Bigger windows are not free. Latency, cost, recall all degrade."),
                   ("Three trade-offs.", "Cost · speed · accuracy. Optimise the trade-off, not the axis."),
                   ("You shipped a real AI PRD.",
                    "With explicit architecture choices and named failure modes.")]),
        note="Wrap on time.",
        takeaway="Five takeaways. The PRD is reusable.")

    add(extra_practice([("Practice 1", "Audit a Real PRD",
                         "Open a recent PRD from your team. Score it 1–5 on the three new AI sections. Commit a refactor proposal."),
                        ("Practice 2", "Run the RAG Decider on a Real Bet",
                         "Take the bet from M2 homework. Run it through the Decider. Commit alongside Juno's architecture.")],
                       "Module 4 — Design AI-Native UX. Bring the worst AI UX you used this week."),
        note="Optional. Loom + repo URL.",
        takeaway="Audit a real PRD. The diff is the learning.")

    add(qa_section(), note="5-min cap.", takeaway="")

    return si, sh


def render_page(title: str, body_sections: list[str]) -> str:
    body = "\n\n".join(body_sections)
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


# === M4 ===
def build_module_4():
    si, sh = [], []
    add = _add_builder(si, sh)

    add(hero("Design", "AI-Native UX",
             "Chat-in-a-tab is the wrong default. AI-native UX is invisible by design.",
             [("Surface", "Anticipation > response. Visible only when value justifies attention."),
              ("Iceberg", "Seven nodes per AI user flow — tip + underwater."),
              ("Trust", "Three trust gaps. All three closed before shipping.")],
             "Out: folder 04-ai-ux/ · user-flow.md · trust-gaps.md.", 4),
        note="This module breaks the \"UI is command-driven\" assumption.",
        takeaway="By the end you have an AI user flow + closed trust gaps for Juno.")

    add(how_it_runs(), note="", takeaway="")
    add(course_arc(4), note="", takeaway="")

    add(recall_section("Module 3",
                       [("03-rag-prd/ai-prd.md", "Bet · mechanic · 3 new AI sections"),
                        ("03-rag-prd/before-after-rag.md", "Diagnostic diff — your sales demo"),
                        ("Worst AI UX screenshot", "Brought from your week — the lesson is in the details")],
                       "Spec is solid. Now the surface."),
        note="Solicit the worst-UX screenshots. Pin one.",
        takeaway="A great spec with bad UX still loses.")

    add(provocation(
        "The 95%-accuracy product loses<br>to the 90% one with better UX.",
        "Vote, then unpack.",
        [("tf-true", "\"Most AI features ship as a chat tab — and that's the failure.\"",
          "Chat-in-a-tab is the wrong default. Users have to remember to open it. AI-native UX surfaces value where decisions happen."),
         ("tf-true", "\"Trust is a UX choice, not a model choice.\"",
          "Same model, two interfaces. <em>Cursor</em> shows reasoning · <em>plain ChatGPT</em> doesn't. Same outputs, different trust."),
         ("tf-false", "\"More information = more trust.\"",
          "Confidence cues + escape hatches > raw data dumps. <em>Air Canada</em>'s chatbot was confidently wrong — and the courts held the company liable.")]),
        note="The Air Canada line lands. Use it.",
        takeaway="UX is where trust is built or destroyed.")

    add(two_column("Invisible by Design",
                   "The default for AI-native UX. Anticipate intent. Surface only when it earns attention.",
                   ("Wrong",
                    "Juno is a chat tab.",
                    "PM must remember it exists, open it, type a query, wait for an answer."),
                   ("Right",
                    "Juno surfaces.",
                    "Prioritised risk panel in <code>#escalations</code> the moment a P0 thread crosses 5 messages. PM gets the answer before asking."),
                   footer="Anticipation &gt; response. Visible only when value justifies attention."),
        note="The right column is the principle.",
        takeaway="Anticipation, not response. Visible only when value justifies attention.")

    add(lecture_table("Map Value to UX Treatment",
                      "Don't pick UX patterns by aesthetic. Map them to the value frame.",
                      ["Value frame", "UX treatment", "Juno example"],
                      [["Cost reduction", "Background automation with audit trail", "Auto-tag P0/P1 on incoming Slack threads"],
                       ["Revenue generation", "Inline assist at the moment of decision", "\"Draft spec from this thread\" button in Slack"],
                       ["Risk mitigation", "Proactive flag + reason + one-click action", "Daily top-3 risks panel in <code>#pm-daily</code>"],
                       ["User delight", "Anticipatory suggestion, dismissible", "\"Looks like this thread is going P0 — want a summary?\""]],
                      caption="For Juno: Risk Mitigation is primary (per M2). That dictates the dominant UX treatment.",
                      tag_label="Framework"),
        note="Tie back to M2's value frame.",
        takeaway="Value frame → UX treatment. Not the other way around.")

    add(two_column("The AI Iceberg",
                   "Most PMs design the tip and hand-wave the underwater. Spec both.",
                   ("Tip (what users see)",
                    "Trigger · Surface · Confirm/Correct.",
                    "The visible 30%. Where trust is built or destroyed."),
                   ("Underwater (what runs)",
                    "Capture · Retrieve · Reason · Act · Log · Guardrail · Fallback.",
                    "The invisible 70%. PM specs what happens at each step — not just \"engineer's problem.\""),
                   footer="The visible tip is where PM craft lives today. The underwater is where it'll live tomorrow.",
                   tag_label="Framework"),
        note="Don't skip underwater spec. PM owns it.",
        takeaway="Spec the iceberg. All seven nodes.")

    add(lecture_cards("Seven Nodes Per Flow",
                      "The shape of an AI user flow.",
                      [("①", "Trigger", "What initiates the flow."),
                       ("②", "Capture", "What context the system gathers."),
                       ("③", "Retrieve", "What data is pulled in."),
                       ("④", "Reason", "What the model decides."),
                       ("⑤", "Act", "What happens in the world (send / write / call)."),
                       ("⑥", "Surface", "What the user sees."),
                       ("⑦", "Confirm / Correct", "How the user steers, accepts, overrides.")],
                      "This list is the deliverable shape for the next exercise.",
                      tag_label="Framework"),
        note="Use the HR Agent walkthrough as the demo.",
        takeaway="Seven nodes. The deliverable shape for M4.")

    add(section_break("Hands-On Lab · 30 min · Final-Project Deliverable",
                      "Architect Juno's AI User Flow",
                      "Pick one pillar. Spec all 7 nodes. Mark tip vs underwater per node."),
        note="The big deliverable for M4.",
        takeaway="Architect the flow.")

    add(applied_work("AI User Flow Architect",
                     "Spec all seven nodes for one Juno pillar.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Pick <strong>one</strong> Juno pillar (recommendation: <em>Prioritise Risks</em>).</li>
      <li>Open <code>M4 - AI User Flow Architect.html</code>.</li>
      <li>Spec all 7 nodes. Be specific (e.g., trigger = <em>"new P0 tagged in #escalations"</em>).</li>
      <li>Mark tip vs underwater per node.</li>
      <li>Copy as markdown &rarr; <code>04-ai-ux/user-flow.md</code>.</li>
      <li>Self-review · AI-review · commit · share.</li>
    </ol>""",
                     "04-ai-ux/user-flow.md", 30,
                     "M4 - AI User Flow Architect.html",
                     "Seven-node flow builder · live preview · self + AI review."),
        note="One-line specs per underwater node are fine. The tip is where PM craft lives.",
        takeaway="One pillar, fully specced. The other two follow the same shape.")

    add(break_section(), note="5-min break.", takeaway="")

    add(lecture_table("Three Trust Gaps",
                      "All three must be closed for a probabilistic system to feel safe.",
                      ["Gap", "Question", "Mitigation"],
                      [["Black-box", "Can the user see <em>why</em>?", "Reasoning · citations · \"show your work\""],
                       ["Hallucination", "Could this confidently be wrong?", "Confidence cues · source links · escape hatches"],
                       ["Control", "Can the user steer or stop?", "Undo · edit · regenerate · \"don't suggest this again\""]],
                      caption="The Trust Gap Checker tool walks each one.",
                      tag_label="Framework"),
        note="The second deliverable for M4.",
        takeaway="Three gaps. All three closed. No exceptions.")

    add(applied_work("AI-UX Trust Gap Checker",
                     "Score Juno on each gap. Write each mitigation in product terms.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M4 - AI-UX Trust Gap Checker.html</code>.</li>
      <li>Score Juno on each of the three gaps (1–5).</li>
      <li>For each gap, write your mitigation in product terms.</li>
      <li>Add the intelligence-tax row (extra latency · cognitive load).</li>
      <li>Copy as markdown &rarr; <code>04-ai-ux/trust-gaps.md</code>.</li>
    </ol>""",
                     "04-ai-ux/trust-gaps.md", 12,
                     "M4 - AI-UX Trust Gap Checker.html",
                     "Three-gap scorer · mitigation prompts · markdown export."),
        note="Quick exercise. ~12 min.",
        takeaway="Mitigations in product terms — not engineering terms.")

    add(lecture_cards("Manage the Intelligence Tax",
                      "Extra latency and cognitive load are product surfaces.",
                      [("⚡", "Spec p95 latency", "Maximum acceptable. Under 4s for synchronous, under 30s for async."),
                       ("📡", "Stream output", "Perceived latency drops dramatically. Almost-free win."),
                       ("👁", "Show reasoning", "Transparency vs distraction. Pick per surface."),
                       ("🛑", "Kill if tax > value", "If the intelligence tax exceeds the value frame, kill the feature.")],
                      "Streaming is the cheapest perceived-latency improvement most learners overlook.",
                      tag_label="Lecture"),
        note="Streaming is free perceived-latency win. Push them.",
        takeaway="Streaming is free. Use it.")

    add(synthesis(4, [("user-flow.md", "Seven nodes · tip + underwater · for one Juno pillar"),
                       ("trust-gaps.md", "Three gaps scored · mitigations in product terms")]),
        note="Four components committed.",
        takeaway="Four down. Two to go.")

    add(bridge(5, "The flow has an Act node.", "M5 makes it agentic.",
               "Your repo with 04-ai-ux/ committed · re-read your user-flow's Act node — it's M5's input."),
        note="Tee up M5: the Act node becomes the AWSpec.",
        takeaway="The Act node is what M5 turns into an Agent Workflow Spec.")

    add(takeaways("Design AI-Native User Experiences",
                  [("Chat-in-a-tab is the wrong default.",
                    "Anticipate intent. Surface only when value justifies attention."),
                   ("Map value → UX treatment.",
                    "Don't pick UX patterns by aesthetic."),
                   ("Spec the iceberg.",
                    "Seven nodes. Tip + underwater. PM owns both."),
                   ("Close all three trust gaps.",
                    "Black-box · hallucination · control. No exceptions."),
                   ("The intelligence tax is a product surface.",
                    "Spec p95. Stream. If tax &gt; value — kill it.")]),
        note="Wrap on time.",
        takeaway="UX is where trust is built. Five takeaways carry it.")

    add(extra_practice([("Practice 1", "Reimagine Juno Out of a Chat Tab",
                         "Move Juno entirely out of a standalone chat. Embed proactive surfaces in Slack/Jira/Notion. Update your Lovable URL or commit screenshots."),
                        ("Practice 2", "Audit a Real AI UX",
                         "Open the worst AI UX you screenshot'd. Score it on the three trust gaps. Write the rewrite. Commit alongside Juno's gaps.")],
                       "Module 5 — Orchestrate AI with Agentic Workflows. Bring your M4 user flow."),
        note="Optional. Loom + repo URL.",
        takeaway="Reimagine without the chat tab. The unlock is real.")

    add(qa_section(), note="5-min cap.", takeaway="")

    return si, sh


# === M5 ===
def build_module_5():
    si, sh = [], []
    add = _add_builder(si, sh)

    add(hero("Orchestrate AI with", "Agentic Workflows",
             "An agent without explicit handoff rules is a liability. Spec the rules of engagement.",
             [("Pick", "Lowest agent level that delivers the job."),
              ("Pattern", "ReAct or Planner-Executor — and why."),
              ("Spec", "AWSpec — 9 sections. All required.")],
             "Out: folder 05-agentic-workflows/ · awspec.md · agent-control-panel.md.", 5),
        note="This module breaks the \"workflows are sequential\" assumption.",
        takeaway="By the end you have an Agent Workflow Spec for Juno.")

    add(how_it_runs(), note="", takeaway="")
    add(course_arc(5), note="", takeaway="")

    add(recall_section("Module 4",
                       [("04-ai-ux/user-flow.md", "Seven-node flow for one Juno pillar"),
                        ("04-ai-ux/trust-gaps.md", "Three gaps scored · mitigations specced")],
                       "Your Act node is what M5 turns into an Agent Workflow Spec."),
        note="Recall the Act node. M5 builds on it.",
        takeaway="The Act node was the foreshadowing. M5 cashes it.")

    add(provocation(
        "An agent without handoff rules<br>is a liability, not a feature.",
        "Vote, then unpack.",
        [("tf-true", "\"Most \\\"agents\\\" you'll see in vendor pitches are actually mid-agents.\"",
          "Don't pay autonomous-agent prices for assistant-level capability. Use the four-trait test."),
         ("tf-true", "\"Memory is where most agents go wrong in production.\"",
          "Long-term memory pulls behaviour off-spec over weeks. Spec what's stored, where, and for how long."),
         ("tf-false", "\"Agents are too risky to ship.\"",
          "<em>Klarna</em> ships an agent. <em>Salesforce Agentforce</em> ships agents. The difference is explicit handoff rules — not the absence of agents.")]),
        note="Push the four-trait test.",
        takeaway="Agents ship safely with explicit handoff rules.")

    add(lecture_cards("Four Traits of Agency",
                      "If a system has all four, it's an agent. One or two = tool or assistant.",
                      [("🎯", "Goals", "Pursues a goal, not just responds."),
                       ("🔧", "Tool use", "Calls functions on the world."),
                       ("🧠", "Memory", "State persists across turns or sessions."),
                       ("🔁", "Iteration", "Observes results, re-plans.")],
                      "Use this to pressure-test \"agentic\" claims from vendors.",
                      tag_label="Framework"),
        note="The four-trait test beats the agent spectrum for spec work.",
        takeaway="Four traits or it's not an agent.")

    add(lecture_table("The Agent Spectrum",
                      "Pick the lowest level that delivers the job. Higher levels need explicit handoff rules.",
                      ["Level", "Behaviour", "Juno example"],
                      [["Tool", "Does one thing on request", "\"Summarise this thread\""],
                       ["Assistant", "Drafts, recommends", "Juno suggests 3 risks; PM picks"],
                       ["Agent", "Plans + calls tools + iterates", "Juno triages P0s, opens Jira stubs, posts to <code>#pm-daily</code>"],
                       ["Autonomous Agent", "Operates long horizons unsupervised", "<em>Not</em> appropriate for Juno's risk profile"]],
                      caption="\"Autonomous\" is rarely the right level. Don't get sold up.",
                      tag_label="Framework"),
        note="Most vendors mis-label assistants as agents.",
        takeaway="Lowest level that delivers. Don't pay autonomous prices for assistant work.")

    add(case_study("Klarna",
                   "Klarna's AI Assistant — Bounded, Tooled, Logged",
                   "<strong>Klarna</strong> · Replace 700 customer-service reps with an LLM-powered agent — for FAQs, refunds, simple disputes.",
                   "Headlines: 700 jobs replaced. Real story: handoff rate. Some queries always escalate to humans — and which kind matters more than the percentage.",
                   "Bet survives because: bounded scope · explicit tools · human checkpoint at high-risk steps · evals run continuously.",
                   "Lesson: the boundary contract is the product."),
        note="The handoff rate is the data point.",
        takeaway="The handoff contract is the product. Spec it.")

    add(lecture_cards("Hidden Costs of Autonomy",
                      "Make these costs visible and bounded in the spec.",
                      [("⛓", "Cascading errors", "One wrong tool call → next step builds on it."),
                       ("💸", "Cost blowup", "Autonomous loops without stop conditions burn tokens."),
                       ("🔍", "Audit opacity", "\"The agent decided\" is not an audit log."),
                       ("📉", "Drift", "Long-term memory pulls behaviour off-spec over weeks.")],
                      "If any of these are unbounded — you've shipped a liability.",
                      tag_label="Lecture"),
        note="This is what makes the AWSpec valuable.",
        takeaway="Four hidden costs. The AWSpec is how you bound them.")

    add(two_column("ReAct vs Planner-Executor",
                   "For most PM purposes, ReAct is the workhorse.",
                   ("ReAct",
                    "Reason → Act → Observe → loop.",
                    "Single-agent reasoning. Best for bounded, sequential tasks with feedback. Juno triaging one P0 thread."),
                   ("Planner-Executor",
                    "Planner decomposes; executors run; planner re-plans on failure.",
                    "Multi-step tasks with parallelism. Juno running the daily risk pipeline across all <code>#escalations</code>."),
                   footer="Default to ReAct unless you have a reason for Planner-Executor."),
        note="Don't over-architect. ReAct is enough for 80% of cases.",
        takeaway="ReAct for one task. Planner-Executor for parallel tasks.")

    add(lecture_table("Four Memory Flavours",
                      "Memory choices shape privacy, cost, and behaviour.",
                      ["Type", "Lifetime", "Use for"],
                      [["Short-term", "Within one task", "Tool results · intermediate reasoning"],
                       ["Long-term", "Across sessions", "User preferences · learned facts"],
                       ["Episodic", "Specific past events", "\"Last week the user said X\""],
                       ["Semantic", "General knowledge", "Org context · domain facts"]],
                      caption="Spec each one explicitly — including the no's.",
                      tag_label="Framework"),
        note="Memory is where most agents go wrong.",
        takeaway="Spec what's remembered. And what isn't.")

    add(section_break("Hands-On Lab · 30 min · Final-Project Deliverable",
                      "Write Juno's Agent Workflow Spec",
                      "Nine sections. The biggest M5 deliverable. Take your M4 Act node and make it agentic."),
        note="The M5 deliverable.",
        takeaway="Final-project deliverable.")

    add(applied_work("Agent Workflow Spec Builder",
                     "Goal · Trigger · Inputs · Tools · Memory · Pattern · Stop · Handoff · Eval hooks.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M5 - Agent Workflow Spec Builder.html</code>.</li>
      <li>Take your M4 Act node — turn it into an AWSpec.</li>
      <li>Default to ReAct unless you have a specific reason.</li>
      <li>Be precise on stop conditions and handoff rules. \"If confidence &lt; 70%\" — not \"if uncertain.\"</li>
      <li>Copy as markdown &rarr; <code>05-agentic-workflows/awspec.md</code>.</li>
      <li>Self-review · AI-review · commit · share.</li>
    </ol>""",
                     "05-agentic-workflows/awspec.md", 30,
                     "M5 - Agent Workflow Spec Builder.html",
                     "Nine-section AWSpec builder · self + AI review · markdown export."),
        note="Push for precise thresholds. \"Uncertain\" is not testable.",
        takeaway="Precise thresholds. Otherwise the spec is fiction.")

    add(break_section(), note="5-min break.", takeaway="")

    add(lecture_cards("Agent Control Panel — Five Levers",
                      "If any lever is missing — you've shipped a liability.",
                      [("⏰", "Triggers", "When does the agent activate?"),
                       ("🔧", "Tools", "What can it call? Read · write · external API?"),
                       ("🧠", "Memory scope", "What does it remember, for how long, for whom?"),
                       ("🛑", "Stop conditions", "When does it hand back / shut down?"),
                       ("📊", "Observability", "Logs · traces · eval surface (M6).")],
                      "The Agent Control Panel tool covers each lever.",
                      tag_label="Framework"),
        note="Five levers. Standalone artifact alongside the AWSpec.",
        takeaway="Five levers. Spec the minimum-viable rule per lever.")

    add(applied_work("Agent Control Panel",
                     "Spec each lever for Juno. The minimum-viable rule per lever.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M5 - Agent Control Panel.html</code>.</li>
      <li>For each of the 5 levers, declare the minimum viable rule.</li>
      <li>Copy as markdown &rarr; <code>05-agentic-workflows/agent-control-panel.md</code>.</li>
    </ol>""",
                     "05-agentic-workflows/agent-control-panel.md", 12,
                     "M5 - Agent Control Panel.html",
                     "Five-lever spec · supporting artifact alongside the AWSpec."),
        note="5-min hands-on.",
        takeaway="The Control Panel is your one-page operator's manual.")

    add(lecture_cards("PM Decision Triangle",
                      "At every step in the flow: AI alone / AI + human / human alone.",
                      [("🤖", "AI alone", "Full execute. Low risk. Trust earned via evals."),
                       ("🤝", "AI + human", "Draft + approve. Default for high-risk steps."),
                       ("👤", "Human alone", "Agent declines, escalates. For contracts, regulators, novel cases.")],
                      "The triangle is the boundary contract between PM and agent.",
                      tag_label="Framework"),
        note="Every AWSpec step gets one of these tags.",
        takeaway="Tag every step with one of three. That's the contract.")

    add(synthesis(5, [("awspec.md", "Nine-section spec — your agent's rules of engagement"),
                       ("agent-control-panel.md", "Five levers · minimum-viable rule per lever")]),
        note="Five components committed.",
        takeaway="Five down. One to go.")

    add(bridge(6, "You have an agent.", "Now prove it's shippable.",
               "Your repo with 05-agentic-workflows/ committed · your AWSpec's Eval hooks section."),
        note="Tee up M6: evals.",
        takeaway="M6 turns Eval hooks into a real eval stack.")

    add(takeaways("Orchestrate AI with Agentic Workflows",
                  [("Pick the lowest level that delivers the job.",
                    "Don't pay autonomous prices for assistant work."),
                   ("Spec the four traits explicitly.",
                    "Goals · tools · memory · iteration. Including the no's."),
                   ("ReAct is the default. Planner-Executor for parallel.",
                    "Default to the simpler pattern."),
                   ("AWSpec has 9 sections. All required.",
                    "Stop conditions and handoff rules earn the most pushback. Hold the line."),
                   ("PM Decision Triangle = boundary contract.",
                    "Every step tagged AI / AI+human / human.")]),
        note="Wrap on time.",
        takeaway="Five takeaways. The contract is the product.")

    add(extra_practice([("Practice 1", "Build Juno's Agent in Langflow",
                         "Open <code>juno-project-template/05-agentic-workflows/Juno Agent.json</code>. Import into Langflow. Add an OpenAI key. Run with a test P0. Capture screenshots."),
                        ("Practice 2", "Apply the Triangle to a Real Workflow",
                         "Pick one workflow on your team. Tag every step AI / AI+human / human. Find the gaps. Commit alongside Juno's.")],
                       "Module 6 — Measure AI Quality with Evals & Guardrails. Bring your AWSpec."),
        note="Langflow exercise is optional, requires API credits.",
        takeaway="Build the agent. Apply the triangle to a real workflow.")

    add(qa_section(), note="5-min cap.", takeaway="")

    return si, sh


# === M6 ===
def build_module_6():
    si, sh = [], []
    add = _add_builder(si, sh)

    add(hero("Measure AI Quality with", "Evals & Guardrails",
             "95% accuracy is a 5% production disaster waiting to happen.",
             [("Stack", "Three eval layers — always all three."),
              ("Rubric", "Human eval rubric · anchors · disagreement protocol."),
              ("Ship", "PM Execution Plan — your README is the pitch.")],
             "Out: folder 06-evals/ · eval-stack.md · human-rubric.md · finalised README.md.", 6),
        note="This module breaks the \"ship-and-monitor-with-analytics\" assumption.",
        takeaway="By the end you have evals + the finalised README of your fork.")

    add(how_it_runs(), note="", takeaway="")
    add(course_arc(6), note="", takeaway="")

    add(recall_section("Module 5",
                       [("05-agentic-workflows/awspec.md", "Nine-section spec · the rules of engagement"),
                        ("05-agentic-workflows/agent-control-panel.md", "Five levers · minimum-viable rules"),
                        ("Eval hooks (in AWSpec)", "What gets logged — M6's input")],
                       "Five components built. M6 makes the whole stack shippable."),
        note="Confirm M5 commits.",
        takeaway="Five components. M6 ships them.")

    add(provocation(
        "Vibe checks fail in production.<br>The 95% pass rate is a 5% liability surface.",
        "Vote, then unpack.",
        [("tf-true", "\"Most teams ship one eval layer. Two if mature.\"",
          "Three is what shippable AI products do. <em>Google Assistant</em> samples ~50 utterances/week per intent across 4 dimensions."),
         ("tf-true", "\"PMs own the eval bar — not QA.\"",
          "If you delegate evals to QA, you've outsourced the product surface. Engineers run them. PMs own the bar."),
         ("tf-false", "\"95% accuracy means it's safe to ship.\"",
          "Do the math: 1,000 calls/day × 5% = 50 wrong outputs/day. Some silently. One high-stakes wrong outweighs the other 950.")]),
        note="The math sells the third claim.",
        takeaway="The eval stack is what makes the 5% liability bounded.")

    add(lecture_table("AI Evals Stack",
                      "You need all three. They answer different questions.",
                      ["Layer", "Volume", "Fidelity", "What it tells you"],
                      [["User feedback", "Highest", "Lowest", "What users do (thumbs · regen · abandon)"],
                       ["Human evaluation", "Mid", "High", "What graders think (rubric scores)"],
                       ["Automated evals", "Highest", "Mid", "What an LLM-judge or regression suite measures"]],
                      caption="<em>Real-world:</em> Google Assistant samples ~50 utterances/week per intent across 4 dimensions.",
                      tag_label="Framework"),
        note="Most teams ship one. Push for all three.",
        takeaway="Three layers. Always all three. They answer different questions.")

    add(lecture_cards("Build a Human Eval Rubric",
                      "A contract between the PM and the graders.",
                      [("①", "Dimensions", "Accuracy · tone · completeness · safety · citation correctness."),
                       ("②", "Scale", "1–5 or pass/fail — with anchor descriptions per scale point."),
                       ("③", "Examples", "One example per scale point. Non-negotiable."),
                       ("④", "Disagreement", "Protocol for when graders disagree."),
                       ("⑤", "Cadence", "How often, how many. Weekly · ~50/intent · etc.")],
                      "Anchors per scale point are the difference between a rubric and a vibe check.",
                      tag_label="Framework"),
        note="Common miss: the disagreement protocol. Push them.",
        takeaway="Anchors + disagreement protocol or it's a vibe check.")

    add(applied_work("Human Evaluation Rubric",
                     "Spec 3–5 dimensions · anchors per scale point · disagreement protocol · sampling cadence.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M6 - Human Evaluation Rubric.html</code>.</li>
      <li>Spec 3–5 dimensions for Juno's risk lists.</li>
      <li>Write anchor descriptions for each scale point.</li>
      <li>Pick a sampling cadence + disagreement protocol.</li>
      <li>Copy as markdown &rarr; <code>06-evals/human-rubric.md</code>.</li>
    </ol>""",
                     "06-evals/human-rubric.md", 12,
                     "M6 - Human Evaluation Rubric.html",
                     "Build the rubric · anchors required · disagreement protocol · markdown export."),
        note="Don't let them skip anchors.",
        takeaway="Anchors per scale. Otherwise graders drift.")

    add(section_break("Hands-On Lab · 25 min · Final-Project Deliverable",
                      "Plan Juno's Eval Stack",
                      "Three layers. For each: signals · cadence · pass bar · who acts on it."),
        note="Big M6 deliverable.",
        takeaway="Final-project deliverable.")

    add(applied_work("Eval Stack Designer",
                     "Plan all three layers — user feedback · human · automated.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>M6 - Eval Stack Designer.html</code>.</li>
      <li>Plan all three layers: user feedback · human eval · automated.</li>
      <li>For each: signals · cadence · pass bar · who acts on it.</li>
      <li>Copy as markdown &rarr; <code>06-evals/eval-stack.md</code>.</li>
      <li>Self-review · AI-review · commit · share.</li>
    </ol>""",
                     "06-evals/eval-stack.md", 25,
                     "M6 - Eval Stack Designer.html",
                     "Plan three eval layers · self + AI review · markdown export."),
        note="Push back on \"automated layer is too complex.\" Even a 10-prompt regression suite counts.",
        takeaway="Automated layer is required. Even a 10-prompt regression counts.")

    add(break_section(), note="5-min break.", takeaway="")

    add(lecture_table("Three Optimisation Levers",
                      "When eval scores miss the bar — model · data · architecture. In that order.",
                      ["Lever", "Try first", "Cost"],
                      [["<strong>Model</strong>", "Swap · upgrade · fine-tune", "Low (swap) → high (fine-tune)"],
                       ["<strong>Data</strong>", "Improve corpus · clean inputs · expand context", "Mid — your time + ops"],
                       ["<strong>Architecture</strong>", "Add RAG · decompose agents · add guardrails", "High — engineering time"]],
                      caption="Most teams reach for architecture first. It's the slowest and most expensive.",
                      tag_label="Framework"),
        note="Push back on architecture-first. Use this rule of thumb.",
        takeaway="Try model and data before architecture.")

    add(lecture_cards("Operationalise Risk — Four Buckets",
                      "Each bucket gets a row in your PM Execution Plan.",
                      [("⚖️", "Compliance", "Regulatory (GDPR · EU AI Act)."),
                       ("🛑", "Safety", "Content · prompt injection · misuse."),
                       ("🔁", "Reliability", "Uptime · fallback paths · graceful degradation."),
                       ("📣", "Reputation", "Public failure scenarios + response playbook.")],
                      "Same framework as M2. Difference: now you operationalise it with metrics + owners.",
                      tag_label="Framework"),
        note="Same buckets as M2 — operationalised.",
        takeaway="M2 buckets — now with metrics and owners.")

    add(section_break("Hands-On Lab · 20 min · The Final Artifact",
                      "Finalise Your Project README",
                      "Pull every artifact together. Your README is the pitch."),
        note="The capstone artifact.",
        takeaway="Your README is the pitch. The repo is the certificate.")

    add(applied_work("Final Project Deliverables Builder",
                     "One structured page · every M1–M6 artifact · Build Insights reflection.",
                     """<ol style="text-align:left; max-width:720px; margin:0 auto;">
      <li>Open <code>Final Project Deliverables Builder.html</code>.</li>
      <li>The tool pulls together: system prompt · strategy one-pager · AI PRD · user flow + trust gaps · AWSpec · eval stack.</li>
      <li>Add your <strong>Build Insights</strong> reflection: 1 friction · 1 learning · 1 aha.</li>
      <li>Copy as markdown &rarr; top-level <code>README.md</code> of your <code>juno-pm/</code> fork.</li>
      <li>Commit. Push. Done.</li>
    </ol>""",
                     "README.md (top-level of your juno-pm/ fork)", 20,
                     "Final Project Deliverables Builder.html",
                     "Pulls every M1–M6 artifact into one README · Build Insights · optional Loom."),
        note="Make sure they understand: README = the pitch. Not a deck. A repo's front page.",
        takeaway="The README is the pitch. The repo is the certificate.")

    add(lecture_cards("Certification — What You Submit",
                      "Submit: the URL of your finalised <code>juno-pm/</code> fork. Window: 7 days post-cohort.",
                      [("📋", "Application of Concepts", "How well M1–M6 frameworks land in your artifacts."),
                       ("🧠", "Credibility & Reasoning", "Whether your decisions hold up to scrutiny."),
                       ("✏️", "Clarity", "Whether a stranger could read your README and \"get\" Juno."),
                       ("🎯", "Strategic Thinking", "Whether the bet, the bar, and the trade-offs are coherent.")],
                      "Scale: 1 — Poor (0–49) · 2 — Sufficient (50–79) · 3 — Excellent (80–100). No live demo required.",
                      tag_label="Framework"),
        note="Re-read the rubric aloud. No one fails for not presenting live.",
        takeaway="Repo URL = submission. Within 7 days. Four rubric dimensions.")

    add(synthesis(6, [("eval-stack.md", "Three layers · cadence · pass bar · owner per layer"),
                       ("human-rubric.md", "Dimensions · anchors · disagreement protocol"),
                       ("README.md (root)", "PM Execution Plan · finalised pitch")]),
        note="Six components committed. Course complete.",
        takeaway="Six down. The repo is the certificate.")

    add(takeaways("Measure AI Quality with Evals & Guardrails",
                  [("Vibe checks fail in production.",
                    "A handful of successful prompts is not a quality bar."),
                   ("AI Evals Stack: three layers, always all three.",
                    "User feedback · human eval · automated. They answer different questions."),
                   ("Human eval needs anchors.",
                    "Without anchor descriptions per scale point, graders drift. Disagreement protocol non-negotiable."),
                   ("Optimise model → data → architecture.",
                    "Most teams architecture-first. It's the slowest, most expensive lever."),
                   ("Eval is product surface. PMs own the bar.",
                    "Engineers can run evals. Only PMs can decide what's good enough to ship."),
                   ("Your README is the pitch.",
                    "Not a deck. Not a doc. The front page of a repo you're proud to submit.")]),
        note="Final takeaway is the most important: they built a real artifact.",
        takeaway="Six takeaways. The repo is the artifact you keep forever.")

    add(extra_practice([("Practice 1", "Optional Async Showcase",
                         "Record a 3-min Loom of your <code>juno-pm/</code> walkthrough — bet · system prompt · user flow · AWSpec · eval stack. Post in <code>#ai-pm-cohort</code> with the repo URL. Instructor responds in-thread within ~5 days."),
                        ("Practice 2", "Re-Run M6 Reviews on Your Next Bet",
                         "The eval-stack template + human-rubric template are reusable forever. Re-run them on the next AI bet on your roadmap.")],
                       "After the cohort: submit your repo within 7 days for certification."),
        note="Re-stress: certification = repo URL within 7 days.",
        takeaway="Course toolkit is reusable forever. Re-run on every future bet.")

    add(qa_section(), note="Wrap warmly.", takeaway="")

    return si, sh


# ─────────────────────────────────────────────────────────────────────────────
# MAIN — write all 12 module files
# ─────────────────────────────────────────────────────────────────────────────

def write_module(n: int, title: str, sections_inst: list[str], sections_share: list[str]):
    inst_path = MODULES_DIR / f"Module {n} - Slides.html"
    share_path = MODULES_DIR / f"Module {n} - Slides (Shareable).html"
    inst_path.write_text(render_page(f"Module {n}: {title} (Instructor)", sections_inst), encoding="utf-8")
    share_path.write_text(render_page(f"Module {n}: {title}", sections_share), encoding="utf-8")
    print(f"  ✓ wrote {inst_path.name} ({inst_path.stat().st_size//1024} KB)")
    print(f"  ✓ wrote {share_path.name} ({share_path.stat().st_size//1024} KB)")


def main():
    print(f"Writing module decks to {MODULES_DIR}")
    # Module 1 follows the original PowerPoint flow — implementation lives
    # in m1_v2.py to keep this file from ballooning.
    from m1_v2 import build_module_1 as build_module_1_v2

    builders = {
        1: build_module_1_v2,
        2: build_module_2,
        3: build_module_3,
        4: build_module_4,
        5: build_module_5,
        6: build_module_6,
    }
    for n, _, _, full_title, _, _ in MODULES_META:
        sections_inst, sections_share = builders[n]()
        write_module(n, full_title, sections_inst, sections_share)
    print("Done.")


if __name__ == "__main__":
    main()
