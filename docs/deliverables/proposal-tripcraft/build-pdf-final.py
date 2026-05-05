#!/usr/bin/env python3
"""Build PROPOSAL_FINAL.pdf from PROPOSAL_FINAL.md via headless Chrome.
   Redesigned: formal Korean government-style 제안서 aesthetic.
   v2: cover cleanup, real prototype screenshots, page-break hardening.
"""
import markdown
import subprocess
import re
import base64
import sys
from pathlib import Path

ROOT   = Path(__file__).parent
MD     = ROOT / "PROPOSAL_FINAL.md"
HTML   = ROOT / "PROPOSAL_FINAL.html"
PDF    = ROOT / "PROPOSAL_FINAL.pdf"
PROTO  = ROOT.parent.parent / "prototypes" / "tripcraft-korea" / "index.html"
SCREENS_DIR = ROOT / "assets" / "screens"
SCREEN_FLOW = ROOT / "assets" / "screen-flow.svg"

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ════════════════════════════════════════════════════════════════════════════
# STEP A — Capture 6 prototype screen PNGs via Chrome headless
# ════════════════════════════════════════════════════════════════════════════

def capture_screens():
    """Extract each screen section from index.html, render to PNG via Chrome."""
    SCREENS_DIR.mkdir(parents=True, exist_ok=True)

    source = PROTO.read_text(encoding="utf-8")

    # Extract all <style> blocks from the prototype
    styles = "\n".join(re.findall(r"<style>(.*?)</style>", source, re.DOTALL))

    # Titles for each screen (for the SVG labels)
    titles = {
        "s1": "① 카테고리 선택",
        "s2": "② 지역 선택",
        "s3": "③ 여행 코스",
        "s4": "④ 오디오 가이드",
        "s5": "⑤ 경비 요약",
        "s6": "⑥ 팔도 스탬프",
    }

    pngs = {}

    for sid in ["s1", "s2", "s3", "s4", "s5", "s6"]:
        # Extract the phone-shell wrapper that contains this screen-area
        # The structure is: .phone-shell > .phone-island + .status-bar + .screen-area#sN
        # We extract from the enclosing .phone-shell div
        pattern = rf'(<div class="phone-shell">.*?<div class="screen-area" id="{sid}">.*?</div>\s*</div>\s*</div>)'
        m = re.search(pattern, source, re.DOTALL)
        if not m:
            # Fallback: just grab the screen-area itself
            pattern2 = rf'(<div class="screen-area" id="{sid}">.*?</div>\s*</div>)'
            m = re.search(pattern2, source, re.DOTALL)

        if not m:
            print(f"[WARN] Could not extract {sid} from prototype HTML")
            continue

        shell_html = m.group(1)

        # Build standalone HTML for this frame
        frame_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TripCraft {sid}</title>
<style>
{styles}
/* Override body/page to show just the phone shell centered */
html, body {{
  margin: 0; padding: 0;
  background: #060609;
  width: 375px;
  height: 812px;
  overflow: hidden;
}}
.phone-shell {{
  position: relative;
  margin: 0;
  border-radius: 0;
  box-shadow: none;
  width: 375px;
  height: 812px;
  overflow: hidden;
}}
.screen-area {{
  overflow: hidden !important;
}}
</style>
</head>
<body>
{shell_html}
</body>
</html>"""

        tmp_html = Path(f"/tmp/tcraft_{sid}.html")
        tmp_png  = Path(f"/tmp/tcraft_{sid}.png")
        tmp_html.write_text(frame_html, encoding="utf-8")

        cmd = [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-extensions",
            "--hide-scrollbars",
            "--virtual-time-budget=4000",
            "--force-device-scale-factor=2",
            f"--window-size=375,812",
            f"--screenshot={tmp_png}",
            f"file://{tmp_html.resolve()}",
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        if tmp_png.exists() and tmp_png.stat().st_size > 5000:
            dest = SCREENS_DIR / f"{sid}.png"
            dest.write_bytes(tmp_png.read_bytes())
            pngs[sid] = dest
            print(f"[OK] Screenshot {sid}: {tmp_png.stat().st_size:,} bytes → {dest}")
        else:
            print(f"[WARN] Screenshot {sid} failed or too small. stderr: {result.stderr[:200]}")

    return pngs, titles


def build_screen_flow_svg(pngs, titles):
    """Build a self-contained SVG with base64-embedded PNGs in a 3×2 grid."""

    # Grid layout: 3 columns × 2 rows
    # SVG viewBox: 1000 × 760 (tighter than 920, fits in PDF page)
    COL_W    = 280
    ROW_H    = 420
    PAD_X    = 30
    PAD_Y    = 50
    GAP_X    = 30
    GAP_Y    = 38
    IMG_W    = 220
    IMG_H    = 380
    LABEL_Y  = 14  # label offset below image

    svg_w = PAD_X * 2 + COL_W * 3 + GAP_X * 2
    svg_h = PAD_Y + 28 + (ROW_H * 2 + GAP_Y) + 20   # title + 2 rows + bottom pad

    cells = []
    for i, sid in enumerate(["s1", "s2", "s3", "s4", "s5", "s6"]):
        col = i % 3
        row = i // 3
        x = PAD_X + col * (COL_W + GAP_X) + (COL_W - IMG_W) // 2
        y = PAD_Y + 32 + row * (ROW_H + GAP_Y)
        lx = PAD_X + col * (COL_W + GAP_X) + COL_W // 2
        ly = y + IMG_H + LABEL_Y

        if sid in pngs:
            raw = pngs[sid].read_bytes()
            b64 = base64.b64encode(raw).decode("ascii")
            img_tag = (
                f'<image x="{x}" y="{y}" width="{IMG_W}" height="{IMG_H}" '
                f'preserveAspectRatio="xMidYMid meet" '
                f'href="data:image/png;base64,{b64}" '
                f'clip-path="url(#rr{i})" />'
            )
            clip_def = (
                f'<clipPath id="rr{i}">'
                f'<rect x="{x}" y="{y}" width="{IMG_W}" height="{IMG_H}" rx="10" ry="10"/>'
                f'</clipPath>'
            )
        else:
            # Fallback placeholder
            img_tag = (
                f'<rect x="{x}" y="{y}" width="{IMG_W}" height="{IMG_H}" '
                f'rx="10" ry="10" fill="#13131A" stroke="#2D5BFF" stroke-width="1.5"/>'
                f'<text x="{x + IMG_W//2}" y="{y + IMG_H//2}" text-anchor="middle" '
                f'font-family="sans-serif" font-size="14" fill="#5E5E72">{sid}</text>'
            )
            clip_def = ""

        # Shadow rect (drawn before image for layering)
        shadow = (
            f'<rect x="{x+3}" y="{y+3}" width="{IMG_W}" height="{IMG_H}" '
            f'rx="10" ry="10" fill="rgba(0,0,0,0.25)"/>'
        )
        # Border rect (drawn after image)
        border = (
            f'<rect x="{x}" y="{y}" width="{IMG_W}" height="{IMG_H}" '
            f'rx="10" ry="10" fill="none" stroke="#2D5BFF" stroke-width="1.2" opacity="0.6"/>'
        )
        # Label badge
        label_text = titles.get(sid, sid)
        badge_w = len(label_text) * 8.5 + 14
        badge_x = lx - badge_w / 2
        label = (
            f'<rect x="{badge_x:.0f}" y="{ly - 11}" width="{badge_w:.0f}" height="16" '
            f'rx="8" fill="#1a3a8a"/>'
            f'<text x="{lx}" y="{ly + 1}" text-anchor="middle" '
            f'font-family="\'Apple SD Gothic Neo\', \'Noto Sans KR\', sans-serif" '
            f'font-size="10" font-weight="700" fill="#93C5FD">{label_text}</text>'
        )

        cells.append((clip_def, shadow, img_tag, border, label))

    # Assemble SVG
    defs_parts   = "\n  ".join(c[0] for c in cells if c[0])
    shadow_parts = "\n  ".join(c[1] for c in cells)
    img_parts    = "\n  ".join(c[2] for c in cells)
    border_parts = "\n  ".join(c[3] for c in cells)
    label_parts  = "\n  ".join(c[4] for c in cells)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">
  <defs>
  {defs_parts}
  </defs>

  <!-- Background -->
  <rect width="{svg_w}" height="{svg_h}" fill="#060609" rx="10"/>

  <!-- Title bar -->
  <rect x="0" y="0" width="{svg_w}" height="36" fill="#0D0D13" rx="10"/>
  <rect x="0" y="26" width="{svg_w}" height="10" fill="#0D0D13"/>
  <text x="{svg_w//2}" y="22" text-anchor="middle"
        font-family="'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif"
        font-size="13" font-weight="700" fill="#F4F4F8">TripCraft Korea 주요 화면 구성도</text>

  <!-- Shadows -->
  {shadow_parts}

  <!-- Phone screenshots -->
  {img_parts}

  <!-- Borders -->
  {border_parts}

  <!-- Labels -->
  {label_parts}
</svg>"""

    SCREEN_FLOW.write_text(svg, encoding="utf-8")
    print(f"[OK] screen-flow.svg built: {SCREEN_FLOW.stat().st_size:,} bytes")
    return SCREEN_FLOW


# ════════════════════════════════════════════════════════════════════════════
# STEP B — Build PDF
# ════════════════════════════════════════════════════════════════════════════

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
# Subtitle line REMOVED; meta updated with platform info
COVER = """
<header class="cover">
  <div class="cover-label">2026 관광데이터 활용 공모전 · ① 웹·앱 개발 부문 제안서</div>
  <div class="cover-title">TripCraft Korea</div>
  <div class="cover-slogan">데이터 가치를 넘어, 서비스로 실현하다 — 관광데이터 스케일 UP</div>
  <div class="cover-meta">
    <span>작성일&nbsp;2026-05-06</span>
    <span class="sep">·</span>
    <span>부문 ① 웹·앱 개발</span>
    <span class="sep">·</span>
    <span>플랫폼 모바일 앱(iOS / Android)</span>
  </div>
</header>
"""

html_body = COVER + html_body

# ── 6. Post-process: wrap ## headings with section-band markup ───────────────
def upgrade_h2(match):
    inner = match.group(1)
    num_m = re.match(r"^(\d+)\)", inner.strip())
    num   = num_m.group(1) if num_m else "●"
    title = inner.strip()
    return (
        f'<h2><span class="sec-num">{num}</span>'
        f'<span class="sec-title">{title}</span></h2>'
    )

html_body = re.sub(r"<h2>(.*?)</h2>", upgrade_h2, html_body)

def upgrade_h3(match):
    inner = match.group(1)
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
  padding: 9pt 18pt 7pt 18pt;
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
  margin-bottom: 4pt;
}
/* cover-subtitle REMOVED */
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
  page-break-before: auto;
  page-break-after: avoid;
  page-break-inside: avoid;
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
  page-break-inside: avoid;
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
  orphans: 3;
  widows: 3;
}
li {
  font-size: 12pt;
  margin: 1pt 0;
  line-height: 1.35;
}
ul, ol { margin: 2pt 0 2pt 16pt; }
strong { color: var(--blue-dark); font-weight: 700; }
em { color: var(--text-light); }

/* ── First content after h3 must stay with the heading ───────────────────── */
h3 + p,
h3 + table,
h3 + ul,
h3 + ol,
h3 + blockquote {
  page-break-before: avoid;
}

/* ── Blockquotes as callout boxes ────────────────────────────────────────── */
blockquote {
  border-left: 4pt solid var(--blue);
  background: var(--blue-bg);
  margin: 3pt 0;
  padding: 3pt 8pt;
  font-size: 12pt;
  color: var(--text);
  border-radius: 0 3pt 3pt 0;
  page-break-inside: avoid;
}

/* ── Tables ──────────────────────────────────────────────────────────────── */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 3pt 0;
  font-size: 11pt;
  font-variant-numeric: tabular-nums;
  page-break-inside: auto;
}
tr {
  page-break-inside: avoid;
  page-break-after: auto;
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
  page-break-after: avoid;
}
img[src*="screen-flow"]   { max-width: 100%; max-height: 560px; object-fit: contain; margin: 6pt auto 3pt; border-radius: 8pt; box-shadow: 0 4pt 18pt rgba(0,0,0,0.15); }
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

/* ── Utility: footer italic line ─────────────────────────────────────────── */
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
cmd = [
    CHROME,
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
