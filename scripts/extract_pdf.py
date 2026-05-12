"""Extract text from every PDF in 'Old artefacts AI Product Manager ' (instructor notes,
lab guides, templates) into scripts/_out/<file>.txt for use as raw source.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from pdfminer.high_level import extract_text
except ImportError:
    print("Install requirements first: pip install -r scripts/requirements.txt", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "Old artefacts AI Product Manager "
OUT = ROOT / "scripts" / "_out"
OUT.mkdir(parents=True, exist_ok=True)


def slugify(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower()
    return s[:80]


def main() -> None:
    pdfs = sorted(SOURCE.rglob("*.pdf"))
    if not pdfs:
        print("No PDFs found.", file=sys.stderr)
        sys.exit(1)
    for pdf in pdfs:
        try:
            text = extract_text(str(pdf))
        except Exception as exc:
            print(f"failed {pdf.name}: {exc}", file=sys.stderr)
            continue
        out = OUT / f"{slugify(pdf.stem)}.txt"
        out.write_text(text)
        print(f"wrote {out.relative_to(ROOT)}  ({pdf.relative_to(ROOT)})")


if __name__ == "__main__":
    main()
