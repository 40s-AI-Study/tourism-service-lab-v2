#!/usr/bin/env python3
"""Build PROPOSAL.pdf from PROPOSAL.md via headless Chrome."""
import markdown
import subprocess
import os
import re
from pathlib import Path

ROOT = Path(__file__).parent
MD = ROOT / "PROPOSAL.md"
HTML = ROOT / "PROPOSAL.html"
PDF = ROOT / "PROPOSAL.pdf"

# Read & strip frontmatter
text = MD.read_text(encoding="utf-8")
text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

# Render markdown → HTML (with tables, fenced code)
html_body = markdown.markdown(
    text,
    extensions=["tables", "fenced_code", "attr_list"],
)

# Resolve image paths to absolute file:// URIs (Chrome needs them)
def fix_img(match):
    src = match.group(1)
    if src.startswith("http"):
        return match.group(0)
    abs_path = (ROOT / src).resolve()
    return f'src="file://{abs_path}"'

html_body = re.sub(r'src="([^"]+)"', fix_img, html_body)

CSS = """
@page { size: A4; margin: 10mm 10mm; }
* { box-sizing: border-box; }
html, body {
  font-family: 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
  font-size: 12pt;
  line-height: 1.28;
  color: #111;
  margin: 0;
  padding: 0;
}
h1 { font-size: 16pt; text-align: center; border-bottom: 2px solid #1a56db; padding: 2pt 0; margin: 0 0 4pt; color: #0f172a; }
h2 { font-size: 13pt; color: #fff; background: #1a56db; padding: 3pt 6pt; margin: 6pt 0 3pt; page-break-after: avoid; }
h3 { font-size: 12pt; color: #1a56db; margin: 5pt 0 2pt; padding-bottom: 1pt; border-bottom: 1px solid #cbd5e1; page-break-after: avoid; }
p { margin: 2pt 0; font-size: 12pt; text-align: justify; }
li { font-size: 12pt; margin: 1pt 0; }
strong { color: #1a56db; }
blockquote {
  border-left: 3px solid #94a3b8;
  background: #f8fafc;
  margin: 2pt 0;
  padding: 2pt 6pt;
  font-size: 12pt;
  color: #334155;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 2pt 0;
  font-size: 12pt;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #94a3b8;
  padding: 2pt 4pt;
  vertical-align: top;
  text-align: left;
  line-height: 1.22;
}
th { background: #1a56db; color: #fff; font-weight: 700; }
tr:nth-child(even) td { background: #f8fafc; }
img { max-width: 60%; height: auto; display: block; margin: 2pt auto; page-break-inside: avoid; }
img[src*="hero-mockup"] { max-width: 30%; }
img[src*="architecture"] { max-width: 80%; }
img[src*="user-journey"] { max-width: 80%; }
code { background: #f1f5f9; padding: 0 2pt; border-radius: 2px; font-size: 12pt; }
pre {
  background: #0f172a;
  color: #e2e8f0;
  padding: 4pt 6pt;
  border-radius: 3px;
  font-size: 12pt;
  line-height: 1.18;
  page-break-inside: avoid;
  overflow-x: hidden;
  white-space: pre-wrap;
  margin: 2pt 0;
}
pre code { background: transparent; color: inherit; padding: 0; font-size: 12pt; }
hr { border: none; border-top: 1px solid #cbd5e1; margin: 3pt 0; }
ul, ol { margin: 2pt 0 2pt 16pt; }
"""

full_html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>2026 관광데이터 활용 공모전 제안서 — TripCraft Korea</title>
<style>{CSS}</style>
</head>
<body>
{html_body}
</body>
</html>
"""

HTML.write_text(full_html, encoding="utf-8")
print(f"[OK] HTML built: {HTML} ({HTML.stat().st_size:,} bytes)")

# Chrome headless → PDF
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF}",
    f"file://{HTML.resolve()}",
]
result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
if PDF.exists():
    print(f"[OK] PDF built:  {PDF} ({PDF.stat().st_size:,} bytes)")
else:
    print("[ERR] PDF not produced")
    print(result.stderr)
