#!/usr/bin/env python3
"""Build PROPOSAL_FINAL.pdf from PROPOSAL_FINAL.md via headless Chrome.
   Redesigned: formal Korean government-style 제안서 aesthetic.
"""
import markdown
import subprocess
import re
from pathlib import Path

ROOT = Path(__file__).parent
MD   = ROOT / "PROPOSAL_FINAL.md"
HTML = ROOT / "PROPOSAL_FINAL.html"
PDF  = ROOT / "PROPOSAL_FINAL.pdf"

# ── 1. Read & strip YAML frontmatter ────────────────────────────────────────
text = MD.read_text(encoding="utf-8")
text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

# ── 2. Remove the existing H1 (we replace it with a styled cover block) ─────
text = re.sub(r"^#\s+.*\n(\*\*TripCraft Korea\*\*.*\n)?", "", text, count=1)

# ── 3. Render markdown → HTML ────────────────────────────────────────────────
html_body = markdown.markdown(
    text,
    extensions=["tables", "fenced_code", "attr_list"],
)

# ── 4. Resolve image paths to absolute file:// URIs ─────────────────────────
def fix_img(match):
    src = match.group(1)
    if src.startswith("http"):
        return match.group(0)
    abs_path = (ROOT / src).resolve()
    return f'src="file://{abs_path}"'

html_body = re.sub(r'src="([^"]+)"', fix_img, html_body)

# ── 5. Inject formal cover block BEFORE body content ────────────────────────
COVER = """
<header class="cover">
  <div class="cover-label">2026 관광데이터 활용 공모전 · ① 웹·앱 개발 부문 제안서</div>
  <div class="cover-title">TripCraft Korea</div>
  <div class="cover-subtitle">카테고리 테마 기반 개인화 여행 플래너</div>
  <div class="cover-slogan">데이터 가치를 넘어, 서비스로 실현하다 — 관광데이터 스케일 UP</div>
  <div class="cover-meta">
    <span>작성일&nbsp;2026-05-06</span>
    <span class="sep">·</span>
    <span>한국관광공사 × 카카오 공동주최</span>
    <span class="sep">·</span>
    <span>부문 ① 웹·앱 개발</span>
  </div>
</header>
"""

html_body = COVER + html_body

# ── 6. Post-process: wrap ## headings with section-band markup ───────────────
# markdown renders ## as <h2>; we need the circle number + band layout
def upgrade_h2(match):
    inner = match.group(1)
    # extract leading number like "1)" or "2)"
    num_m = re.match(r"^(\d+)\)", inner.strip())
    num   = num_m.group(1) if num_m else "●"
    title = inner.strip()
    return (
        f'<h2><span class="sec-num">{num}</span>'
        f'<span class="sec-title">{title}</span></h2>'
    )

html_body = re.sub(r"<h2>(.*?)</h2>", upgrade_h2, html_body)

# Wrap ### headings with badge markup
def upgrade_h3(match):
    inner = match.group(1)
    # extract "1-1" style badge
    badge_m = re.match(r"^(\d+-\d+)\s+(.*)", inner.strip())
    if badge_m:
        badge = badge_m.group(1)
        title = badge_m.group(2)
    else:
        badge = "▸"
        title = inner.strip()
    return (
        f'<h3><span class="sub-badge">{badge}</span>'
        f'<span class="sub-title">{title}</span></h3>'
    )

html_body = re.sub(r"<h3>(.*?)</h3>", upgrade_h3, html_body)

# ── 7. CSS ───────────────────────────────────────────────────────────────────
CSS = """
/* ── Page setup ─────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

@page {
  size: A4;
  margin: 10mm 12mm 12mm 12mm;
  @bottom-center {
    content: "TripCraft Korea  ·  " counter(page) " / 5";
    font-family: 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif;
    font-size: 8pt;
    color: #6b7280;
    padding-top: 4pt;
    border-top: 0.5pt solid #cbd5e1;
  }
}

/* ── CSS variables ───────────────────────────────────────────────────────── */
:root {
  --blue:        #1a56db;
  --blue-dark:   #1241a8;
  --blue-light:  #dbeafe;
  --blue-bg:     #f1f5ff;
  --orange:      #FF6B35;
  --green:       #10B981;
  --text:        #1f2937;
  --text-light:  #4b5563;
  --border:      #cbd5e1;
  --row-alt:     #f0f6ff;
}

/* ── Reset ───────────────────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }
html, body {
  font-family: 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
  font-size: 12pt;
  line-height: 1.35;
  color: var(--text);
  margin: 0;
  padding: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* ── Cover block ─────────────────────────────────────────────────────────── */
.cover {
  background: linear-gradient(135deg, #0d3a8e 0%, var(--blue) 60%, #2563eb 100%);
  color: #fff;
  padding: 10pt 18pt 8pt 18pt;
  margin: 0 0 7pt 0;
  border-radius: 4pt;
  page-break-after: avoid;
}
.cover-label {
  font-size: 8.5pt;
  font-weight: 500;
  letter-spacing: 0.04em;
  opacity: 0.85;
  margin-bottom: 3pt;
  text-transform: uppercase;
}
.cover-title {
  font-size: 26pt;
  font-weight: 900;
  letter-spacing: -0.02em;
  line-height: 1.05;
  margin-bottom: 3pt;
}
.cover-subtitle {
  font-size: 13pt;
  font-weight: 500;
  color: #bfdbfe;
  margin-bottom: 4pt;
}
.cover-slogan {
  display: inline-block;
  background: rgba(255,107,53,0.92);
  color: #fff;
  font-size: 10pt;
  font-weight: 700;
  padding: 2pt 8pt;
  border-radius: 2pt;
  margin-bottom: 4pt;
}
.cover-meta {
  font-size: 9pt;
  color: #bfdbfe;
  margin-top: 1pt;
}
.cover-meta .sep { margin: 0 4pt; opacity: 0.6; }

/* ── Section (##) band headers ───────────────────────────────────────────── */
h2 {
  display: flex;
  align-items: center;
  gap: 0;
  background: linear-gradient(90deg, var(--blue) 0%, #2563eb 70%, #3b82f6 100%);
  color: #fff;
  margin: 7pt 0 3pt 0;
  padding: 0;
  border-radius: 3pt;
  page-break-after: avoid;
  overflow: hidden;
  font-size: 12pt;
}
.sec-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 22pt;
  height: 100%;
  background: rgba(0,0,0,0.20);
  font-size: 12pt;
  font-weight: 900;
  padding: 4pt 6pt;
  align-self: stretch;
}
.sec-title {
  padding: 4pt 8pt;
  font-weight: 700;
  letter-spacing: 0.01em;
}

/* ── Sub-section (###) headers ───────────────────────────────────────────── */
h3 {
  display: flex;
  align-items: baseline;
  gap: 5pt;
  margin: 5pt 0 2pt 0;
  padding-bottom: 2pt;
  border-bottom: 1.5pt solid var(--blue-light);
  page-break-after: avoid;
}
.sub-badge {
  display: inline-block;
  background: var(--blue);
  color: #fff;
  font-size: 8.5pt;
  font-weight: 700;
  padding: 0.5pt 4pt 1pt;
  border-radius: 2pt;
  letter-spacing: 0.03em;
  white-space: nowrap;
  flex-shrink: 0;
}
.sub-title {
  font-size: 12pt;
  font-weight: 700;
  color: var(--text);
}

/* ── Body text ───────────────────────────────────────────────────────────── */
p {
  margin: 2pt 0;
  font-size: 12pt;
  line-height: 1.35;
  text-align: justify;
}
li {
  font-size: 12pt;
  margin: 1pt 0;
  line-height: 1.35;
}
ul, ol { margin: 2pt 0 2pt 16pt; }
strong { color: var(--blue-dark); font-weight: 700; }
em { color: var(--text-light); }

/* ── Blockquotes as callout boxes ────────────────────────────────────────── */
blockquote {
  border-left: 4pt solid var(--blue);
  background: var(--blue-bg);
  margin: 3pt 0;
  padding: 3pt 8pt;
  font-size: 12pt;
  color: var(--text);
  border-radius: 0 3pt 3pt 0;
}

/* ── Tables ──────────────────────────────────────────────────────────────── */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 3pt 0;
  font-size: 11pt;
  font-variant-numeric: tabular-nums;
}
th {
  background: var(--blue);
  color: #fff;
  font-weight: 700;
  font-size: 11.5pt;
  padding: 4pt 6pt;
  text-align: left;
  vertical-align: middle;
  border: 1pt solid var(--blue-dark);
  line-height: 1.3;
}
td {
  border: 0.5pt solid var(--border);
  padding: 4pt 6pt;
  vertical-align: top;
  text-align: left;
  line-height: 1.3;
}
tr:nth-child(even) td { background: var(--row-alt); }
tr:nth-child(odd)  td { background: #fff; }

/* center-aligned cells (comparison table) */
td:nth-child(2), td:nth-child(3), td:nth-child(4), td:nth-child(5) {
  text-align: center;
}
/* but first col always left */
td:first-child { text-align: left; }
th:nth-child(2), th:nth-child(3), th:nth-child(4), th:nth-child(5) {
  text-align: center;
}
th:first-child { text-align: left; }

/* Bold numbers and percentages */
td strong { color: var(--blue-dark); }

/* Accent last column in comparison tables */
td:last-child { background: rgba(26,86,219,0.08) !important; font-weight: 600; }
td:first-child { background: inherit; font-weight: 400; }

/* ── Images ──────────────────────────────────────────────────────────────── */
img {
  max-width: 95%;
  height: auto;
  display: block;
  margin: 4pt auto 2pt;
  border: 1pt solid var(--border);
  border-radius: 4pt;
  box-shadow: 0 1pt 4pt rgba(0,0,0,0.10);
  page-break-inside: avoid;
}
img[src*="screen-flow"]   { max-width: 100%; max-height: 600px; object-fit: contain; margin: 6pt auto 3pt; border-radius: 8pt; box-shadow: 0 4pt 18pt rgba(0,0,0,0.15); }
img[src*="hero-mockup"]   { max-width: 42%; max-height: 320px; object-fit: contain; }
img[src*="architecture"]  { max-width: 70%; }

/* Image caption (em tag immediately after img) */
img + em, p > img + em {
  display: block;
  text-align: center;
  font-size: 10pt;
  color: var(--text-light);
  font-style: italic;
  margin: 0 auto 2pt;
}

/* ── Code ────────────────────────────────────────────────────────────────── */
code {
  background: #f1f5f9;
  padding: 0 3pt;
  border-radius: 2pt;
  font-size: 11.5pt;
}
pre {
  background: #0f172a;
  color: #e2e8f0;
  padding: 5pt 8pt;
  border-radius: 3pt;
  font-size: 11pt;
  line-height: 1.3;
  page-break-inside: avoid;
  overflow-x: hidden;
  white-space: pre-wrap;
  margin: 3pt 0;
}
pre code { background: transparent; color: inherit; padding: 0; }

/* ── HR ──────────────────────────────────────────────────────────────────── */
hr { border: none; border-top: 0.5pt solid var(--border); margin: 4pt 0; }

/* ── Page breaks ─────────────────────────────────────────────────────────── */
h2 { page-break-inside: avoid; }
h3 { page-break-inside: avoid; }
table { page-break-inside: auto; }
tr    { page-break-inside: avoid; }

/* ── Utility: footer italic line (작성일 line) ───────────────────────────── */
body > p:last-child {
  font-size: 10pt;
  color: var(--text-light);
  text-align: center;
  margin-top: 8pt;
  border-top: 0.5pt solid var(--border);
  padding-top: 4pt;
}
"""

# ── 8. Assemble full HTML ─────────────────────────────────────────────────────
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

# ── 9. Chrome headless → PDF ──────────────────────────────────────────────────
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-first-run",
    "--no-default-browser-check",
    "--disable-extensions",
    "--virtual-time-budget=8000",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF}",
    f"file://{HTML.resolve()}",
]
result = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
if PDF.exists():
    print(f"[OK] PDF built:  {PDF} ({PDF.stat().st_size:,} bytes)")
else:
    print("[ERR] PDF not produced")
    print(result.stderr)
