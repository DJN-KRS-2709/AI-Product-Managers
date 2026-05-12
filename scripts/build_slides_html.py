"""Convenience helper. Given a markdown file with one section per slide (as produced by
extract_pptx.py), emit a self-contained scroll-snap HTML deck matching the AI Product
Strategy visual pattern.

This is a fallback skeleton — the human-authored Slides.html files are written by hand
to apply the individual-only voice sweep and pedagogical reshaping. Run this only if you
want a quick visual diff against the raw extraction.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

TEMPLATE = """<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />
<title>{title}</title>
<style>
  :root {{ --bg:#0b0d12; --fg:#f6f7fb; --muted:#9aa3b2; --accent:#7c8cff; }}
  * {{ box-sizing:border-box }} html,body {{ margin:0; padding:0; background:var(--bg); color:var(--fg); font-family:-apple-system,Segoe UI,Inter,sans-serif }}
  main {{ scroll-snap-type:y mandatory; height:100vh; overflow-y:auto }}
  section {{ scroll-snap-align:start; min-height:100vh; padding:8vh 8vw; display:flex; flex-direction:column; justify-content:center; border-bottom:1px solid #1b1f29 }}
  h1 {{ font-size:clamp(28px,4vw,56px); line-height:1.1; margin:0 0 .4em }}
  h2 {{ font-size:clamp(22px,2.6vw,36px); margin:0 0 .8em; color:var(--accent) }}
  p,li {{ font-size:clamp(16px,1.4vw,20px); line-height:1.55; color:var(--fg) }}
  ul {{ margin:0; padding-left:1.2em }}
  .muted {{ color:var(--muted) }}
  .progress {{ position:fixed; top:0; left:0; height:3px; background:var(--accent); width:0%; transition:width .15s }}
  .dots {{ position:fixed; right:20px; top:50%; transform:translateY(-50%); display:flex; flex-direction:column; gap:8px }}
  .dot {{ width:8px; height:8px; border-radius:50%; background:#2a2f3a; cursor:pointer }} .dot.on {{ background:var(--accent) }}
</style>
</head>
<body>
<div class=\"progress\" id=\"p\"></div>
<div class=\"dots\" id=\"d\"></div>
<main id=\"m\">
{slides}
</main>
<script>
  const m=document.getElementById('m'),p=document.getElementById('p'),d=document.getElementById('d');
  const sections=[...document.querySelectorAll('section')];
  sections.forEach((_,i)=>{{const x=document.createElement('div');x.className='dot';x.onclick=()=>sections[i].scrollIntoView({{behavior:'smooth'}});d.appendChild(x)}});
  const dots=[...d.children];
  const update=()=>{{const t=m.scrollTop,h=m.scrollHeight-m.clientHeight;p.style.width=(t/h*100)+'%';const i=Math.round(t/m.clientHeight);dots.forEach((x,j)=>x.classList.toggle('on',i===j))}};
  m.addEventListener('scroll',update);update();
  document.addEventListener('keydown',e=>{{if(e.key==='ArrowDown'||e.key==='PageDown'||e.key===' ')sections[Math.min(sections.length-1,Math.round(m.scrollTop/m.clientHeight)+1)].scrollIntoView({{behavior:'smooth'}});if(e.key==='ArrowUp'||e.key==='PageUp')sections[Math.max(0,Math.round(m.scrollTop/m.clientHeight)-1)].scrollIntoView({{behavior:'smooth'}})}});
</script>
</body>
</html>
"""


def md_to_slides_html(md: str) -> str:
    chunks = re.split(r"\n##\s+Slide\s+\d+\s*\n", "\n" + md)[1:]
    out = []
    for chunk in chunks:
        body_match = re.search(r"###\s+Body\s*\n(.+?)(?=\n###|\Z)", chunk, re.S)
        body = (body_match.group(1) if body_match else "").strip()
        lines = [l for l in body.splitlines() if l.strip()]
        if not lines:
            continue
        title, *rest = lines
        items = "".join(f"<li>{l}</li>" for l in rest)
        out.append(f"<section><h1>{title}</h1><ul>{items}</ul></section>")
    return "\n".join(out)


def main() -> None:
    if len(sys.argv) < 3:
        print("usage: build_slides_html.py <input.md> <output.html> [title]", file=sys.stderr)
        sys.exit(1)
    md = Path(sys.argv[1]).read_text()
    out = Path(sys.argv[2])
    title = sys.argv[3] if len(sys.argv) > 3 else out.stem
    out.write_text(TEMPLATE.format(title=title, slides=md_to_slides_html(md)))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
