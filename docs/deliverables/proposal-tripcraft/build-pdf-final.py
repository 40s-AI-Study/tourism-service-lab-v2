#!/usr/bin/env python3
"""Build PROPOSAL_FINAL.pdf from PROPOSAL_FINAL.md via headless Chrome.
   Redesigned: formal Korean government-style 제안서 aesthetic.
   v3: Fix1(cover replaces H1), Fix2+3(3 screens, distinct capture), Fix5(table CSS+colgroup).
"""
import markdown
import subprocess
import re
import base64
import hashlib
import sys
from pathlib import Path

ROOT        = Path(__file__).parent
MD          = ROOT / "PROPOSAL_FINAL.md"
HTML        = ROOT / "PROPOSAL_FINAL.html"
PDF         = ROOT / "PROPOSAL_FINAL.pdf"
PROTO       = ROOT.parent.parent / "prototypes" / "tripcraft-korea" / "index.html"
SCREENS_DIR = ROOT / "assets" / "screens"
SCREEN_FLOW = ROOT / "assets" / "screen-flow.svg"

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ════════════════════════════════════════════════════════════════════════════
# STEP A — Capture 3 prototype screen PNGs via Chrome headless
# Targets: s3 (코스 추천), s4 (오디오 가이드), s6 (팔도 스탬프)
# ════════════════════════════════════════════════════════════════════════════

def extract_section(source, sid):
    """Extract the complete .phone-shell wrapper containing screen-area#sid.
    Handles nested tags robustly by walking character-by-character after finding
    the opening tag, counting open/close div tags until balance returns to 0.
    """
    # Find the .phone-shell div that contains id="{sid}"
    # First locate the position of id="{sid}"
    marker = f'id="{sid}"'
    pos = source.find(marker)
    if pos == -1:
        return None

    # Walk backwards to find the enclosing <div class="phone-shell">
    search_back = source[:pos]
    shell_start = search_back.rfind('<div class="phone-shell">')
    if shell_start == -1:
        return None

    # Now extract from shell_start forward, counting div depth
    chunk = source[shell_start:]
    depth = 0
    i = 0
    while i < len(chunk):
        if chunk[i] == '<':
            if chunk[i:i+5] == '</div':
                depth -= 1
                if depth == 0:
                    # Find the closing >
                    end = chunk.index('>', i)
                    return chunk[:end + 1]
                i += 5
                continue
            elif chunk[i:i+4] == '<div':
                depth += 1
        i += 1
    return None


def capture_screens():
    """Capture 3 specific screens from index.html as standalone renders."""
    SCREENS_DIR.mkdir(parents=True, exist_ok=True)

    source = PROTO.read_text(encoding="utf-8")

    # Extract ALL <style> blocks from the prototype
    styles = "\n".join(re.findall(r"<style>(.*?)</style>", source, re.DOTALL))

    targets = [
        ("s3", "course",  "① 코스 추천"),
        ("s4", "audio",   "② 오디오 가이드"),
        ("s6", "stamp",   "③ 팔도 스탬프"),
    ]

    pngs = {}
    labels = {}

    for sid, name, label in targets:
        shell_html = extract_section(source, sid)
        if not shell_html:
            print(f"[WARN] Could not extract phone-shell for {sid}")
            continue

        # Build standalone HTML: phone shell centered, sized to visible area
        frame_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>TripCraft {sid}</title>
<style>
{styles}
/* Override: show phone shell at exact design dimensions */
html, body {{
  margin: 0; padding: 0;
  background: #060609;
  width: 375px;
  height: 812px;
  overflow: hidden;
}}
.phone-shell {{
  position: relative !important;
  margin: 0 !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  width: 375px !important;
  height: 812px !important;
  overflow: hidden !important;
}}
.screen-area {{
  overflow: hidden !important;
  height: calc(812px - 50px) !important;
}}
/* Ensure animated elements render in static state */
* {{ animation-play-state: paused !important; }}
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
            "--virtual-time-budget=5000",
            "--run-all-compositor-stages-before-draw",
            "--force-device-scale-factor=2",
            f"--window-size=375,812",
            f"--screenshot={tmp_png}",
            f"file://{tmp_html.resolve()}",
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        if tmp_png.exists() and tmp_png.stat().st_size > 5000:
            dest = SCREENS_DIR / f"{name}.png"
            dest.write_bytes(tmp_png.read_bytes())
            pngs[name] = dest
            labels[name] = label
            md5 = hashlib.md5(tmp_png.read_bytes()).hexdigest()
            print(f"[OK] Screenshot {sid} ({name}): {tmp_png.stat().st_size:,} bytes → {dest} | md5={md5}")
        else:
            print(f"[WARN] Screenshot {sid} failed or too small. stderr: {result.stderr[:300]}")

    # Verify all 3 PNGs are distinct
    if len(pngs) == 3:
        hashes = [hashlib.md5(p.read_bytes()).hexdigest() for p in pngs.values()]
        names  = list(pngs.keys())
        if len(set(hashes)) < 3:
            print(f"[ERR] Some PNG files are identical! Hashes: {list(zip(names, hashes))}")
        else:
            print(f"[OK] All 3 PNGs are visually distinct (different md5 hashes)")
        for n, h in zip(names, hashes):
            print(f"     {n}.png  md5={h}")

    return pngs, labels


def build_screen_flow_svg(pngs, labels):
    """Build a self-contained SVG with 3 base64-embedded PNGs, horizontal layout.
    viewBox 1000×640, 3-wide, fits nicely in A4 portrait page.
    """
    # Layout constants
    SVG_W  = 1000
    SVG_H  = 580
    IMG_W  = 250
    IMG_H  = 460
    PAD_X  = 60    # left/right outer padding
    GAP_X  = 65    # gap between columns
    TOP_Y  = 72    # image top Y (below title bar)

    # 3 columns: x positions
    total_imgs = IMG_W * 3 + GAP_X * 2
    start_x = (SVG_W - total_imgs) // 2

    screen_names = ["course", "audio", "stamp"]
    badge_labels = [
        labels.get("course", "① 코스 추천"),
        labels.get("audio",  "② 오디오 가이드"),
        labels.get("stamp",  "③ 팔도 스탬프"),
    ]

    cells = []
    for i, (sname, badge_text) in enumerate(zip(screen_names, badge_labels)):
        x = start_x + i * (IMG_W + GAP_X)
        y = TOP_Y

        label_cx = x + IMG_W // 2
        label_y  = y + IMG_H + 22

        if sname in pngs:
            raw = pngs[sname].read_bytes()
            b64 = base64.b64encode(raw).decode("ascii")
            clip_id = f"clip{i}"
            clip_def = (
                f'<clipPath id="{clip_id}">'
                f'<rect x="{x}" y="{y}" width="{IMG_W}" height="{IMG_H}" rx="12" ry="12"/>'
                f'</clipPath>'
            )
            shadow = (
                f'<rect x="{x+4}" y="{y+4}" width="{IMG_W}" height="{IMG_H}" '
                f'rx="12" ry="12" fill="#000000" opacity="0.30"/>'
            )
            img_tag = (
                f'<image x="{x}" y="{y}" width="{IMG_W}" height="{IMG_H}" '
                f'preserveAspectRatio="xMidYMid slice" '
                f'href="data:image/png;base64,{b64}" '
                f'clip-path="url(#{clip_id})" />'
            )
            border = (
                f'<rect x="{x}" y="{y}" width="{IMG_W}" height="{IMG_H}" '
                f'rx="12" ry="12" fill="none" stroke="#2D5BFF" stroke-width="1.5" opacity="0.7"/>'
            )
        else:
            clip_def = ""
            shadow   = ""
            img_tag  = (
                f'<rect x="{x}" y="{y}" width="{IMG_W}" height="{IMG_H}" '
                f'rx="12" ry="12" fill="#13131A" stroke="#2D5BFF" stroke-width="1.5"/>'
                f'<text x="{x + IMG_W//2}" y="{y + IMG_H//2}" text-anchor="middle" '
                f'font-family="sans-serif" font-size="14" fill="#5E5E72">{sname}</text>'
            )
            border = ""

        # Badge pill below image
        badge_w = max(len(badge_text) * 12 + 24, 100)
        badge_x = label_cx - badge_w // 2
        badge = (
            f'<rect x="{badge_x}" y="{label_y - 14}" width="{badge_w}" height="22" '
            f'rx="11" fill="#1a3a8a"/>'
            f'<text x="{label_cx}" y="{label_y + 3}" text-anchor="middle" '
            f'font-family="\'Apple SD Gothic Neo\', \'Noto Sans KR\', sans-serif" '
            f'font-size="13" font-weight="700" fill="#93C5FD">{badge_text}</text>'
        )

        cells.append((clip_def, shadow, img_tag, border, badge))

    defs_parts   = "\n  ".join(c[0] for c in cells if c[0])
    shadow_parts = "\n  ".join(c[1] for c in cells if c[1])
    img_parts    = "\n  ".join(c[2] for c in cells)
    border_parts = "\n  ".join(c[3] for c in cells if c[3])
    badge_parts  = "\n  ".join(c[4] for c in cells)

    title_text = "TripCraft Korea 핵심 화면 (코스 추천 · 오디오 가이드 · 팔도 스탬프)"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {SVG_W} {SVG_H}" width="{SVG_W}" height="{SVG_H}">
  <defs>
  {defs_parts}
  </defs>

  <!-- Background -->
  <rect width="{SVG_W}" height="{SVG_H}" fill="#060609" rx="12"/>

  <!-- Title bar -->
  <rect x="0" y="0" width="{SVG_W}" height="56" fill="#0D0D13" rx="12"/>
  <rect x="0" y="44" width="{SVG_W}" height="12" fill="#0D0D13"/>
  <text x="{SVG_W // 2}" y="34" text-anchor="middle"
        font-family="'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif"
        font-size="18" font-weight="700" fill="#1a56db">{title_text}</text>

  <!-- Shadows -->
  {shadow_parts}

  <!-- Phone screenshots -->
  {img_parts}

  <!-- Borders -->
  {border_parts}

  <!-- Labels -->
  {badge_parts}
</svg>"""

    SCREEN_FLOW.write_text(svg, encoding="utf-8")
    print(f"[OK] screen-flow.svg built: {SCREEN_FLOW.stat().st_size:,} bytes")
    return SCREEN_FLOW


# ════════════════════════════════════════════════════════════════════════════
# STEP B — Build PDF
# ════════════════════════════════════════════════════════════════════════════

# ── 1. Capture screens first (so SVG is ready before HTML build) ─────────────
pngs, labels = capture_screens()
build_screen_flow_svg(pngs, labels)

# ── 2. Read & strip YAML frontmatter ────────────────────────────────────────
text = MD.read_text(encoding="utf-8")
text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

# ── 3. FIX 1: Remove the H1 line (and optional subtitle bold line after it)
#    This ensures the markdown-rendered HTML has NO <h1> — cover replaces it.
text = re.sub(r"^#\s+[^\n]+\n(\*\*TripCraft Korea\*\*[^\n]*\n)?", "", text, count=1)

# ── 4. Render markdown → HTML ────────────────────────────────────────────────
html_body = markdown.markdown(
    text,
    extensions=["tables", "fenced_code", "attr_list"],
)

# ── 5. FIX 1 guard: Remove any stray <h1>…</h1> that markdown might emit ────
html_body = re.sub(r"<h1[^>]*>.*?</h1>", "", html_body, flags=re.DOTALL)

# ── 6. Resolve image paths to absolute file:// URIs ─────────────────────────
def fix_img(match):
    src = match.group(1)
    if src.startswith("http"):
        return match.group(0)
    abs_path = (ROOT / src).resolve()
    return f'src="file://{abs_path}"'

html_body = re.sub(r'src="([^"]+)"', fix_img, html_body)

# ── 7. Inject formal cover block BEFORE body content ────────────────────────
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

# ── 8. Post-process: wrap ## headings with section-band markup ───────────────
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

# ── 9. FIX 5: Inject <colgroup> for specific tables ─────────────────────────
#
# Strategy: detect the h3 badge text preceding each table, then inject
# <colgroup> right after <table> in the next table element.

def inject_colgroup(html, h3_badge_text, col_widths):
    """Find the first <table> after the h3 with given badge text, inject colgroup."""
    # Find the h3 containing the badge text
    h3_pat = re.escape(h3_badge_text)
    m = re.search(h3_pat, html)
    if not m:
        return html, False
    pos_after_h3 = m.end()
    # Find the next <table> after that position
    table_m = re.search(r"<table>", html[pos_after_h3:])
    if not table_m:
        return html, False
    insert_pos = pos_after_h3 + table_m.end()
    # Build colgroup
    cols = "".join(f'<col style="width:{w}%">' for w in col_widths)
    colgroup = f"<colgroup>{cols}</colgroup>"
    html = html[:insert_pos] + colgroup + html[insert_pos:]
    return html, True

colgroup_count = 0

# 2-2 main features table: 4 columns (# / 핵심 기능 / 작동 방식 / 활용 데이터)
html_body, ok = inject_colgroup(html_body, "2-2", [6, 18, 48, 28])
if ok: colgroup_count += 1; print("[OK] colgroup injected: 2-2 features table")

# 2-3 차별점 5행 table: 3 columns (핵심 차별점 / 기존 서비스 / TripCraft Korea)
# This is the FIRST table after 2-3
html_body, ok = inject_colgroup(html_body, "2-3", [28, 30, 42])
if ok: colgroup_count += 1; print("[OK] colgroup injected: 2-3 차별점 table")

# 3-1 KTO 14종 table: 2 columns
html_body, ok = inject_colgroup(html_body, "3-1", [36, 64])
if ok: colgroup_count += 1; print("[OK] colgroup injected: 3-1 KTO table")

# 4-1 로드맵 table: 4 columns (단계 / 핵심 기능 / 월 이용자 목표 / 파트너십)
html_body, ok = inject_colgroup(html_body, "4-1", [14, 36, 18, 32])
if ok: colgroup_count += 1; print("[OK] colgroup injected: 4-1 roadmap table")

print(f"[OK] Total colgroup injections: {colgroup_count}")

# Also inject colgroup for the カカオ 4종 table (second table in 3-1 section)
# Find second <table> after 3-1 badge
m = re.search(r"3-1", html_body)
if m:
    rest = html_body[m.end():]
    # Find second table
    t1 = re.search(r"<table>", rest)
    if t1:
        rest2 = rest[t1.end():]
        t2 = re.search(r"<table>", rest2)
        if t2:
            abs_pos = m.end() + t1.end() + t2.end()
            cols = "<colgroup><col style='width:26%'><col style='width:74%'></colgroup>"
            html_body = html_body[:abs_pos] + cols + html_body[abs_pos:]
            colgroup_count += 1
            print("[OK] colgroup injected: 3-1 kakao table")

# ── 10. CSS ──────────────────────────────────────────────────────────────────
CSS = """
/* ── Page setup ─────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

@page {
  size: A4;
  margin: 8mm 11mm 10mm 11mm;
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
  margin: 5pt 0 2pt 0;
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
  margin: 3pt 0 1pt 0;
  padding-bottom: 1pt;
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
  margin: 1pt 0;
  font-size: 12pt;
  line-height: 1.3;
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
  margin: 2pt 0;
  padding: 2pt 7pt;
  font-size: 11pt;
  color: var(--text);
  border-radius: 0 3pt 3pt 0;
  page-break-inside: avoid;
}

/* ── FIX 5: Tables — fixed layout, Korean word-break, clean cell wrapping ── */
table {
  table-layout: fixed;
  width: 100%;
  border-collapse: collapse;
  margin: 4pt 0;
  font-size: 11pt;
  line-height: 1.4;
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
  font-size: 10.5pt;
  padding: 4pt 6pt;
  text-align: left;
  vertical-align: middle;
  border: 1pt solid var(--blue-dark);
  line-height: 1.3;
  word-break: keep-all;
  overflow-wrap: break-word;
  hyphens: none;
}
td {
  border: 0.5pt solid var(--border);
  padding: 4pt 6pt;
  vertical-align: middle;
  text-align: left;
  line-height: 1.3;
  word-break: keep-all;
  overflow-wrap: break-word;
  hyphens: none;
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
img[src*="screen-flow"]   { max-width: 100%; max-height: 420px; object-fit: contain; margin: 3pt auto 2pt; border-radius: 8pt; box-shadow: 0 4pt 18pt rgba(0,0,0,0.15); }
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

# ── 11. Assemble full HTML ────────────────────────────────────────────────────
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

# ── 12. FIX 1 verification: grep for <h1> in output HTML ─────────────────────
h1_count = len(re.findall(r"<h1[^>]*>", full_html))
if h1_count == 0:
    print(f"[OK] Fix 1 verified: zero <h1> tags in output HTML")
else:
    print(f"[WARN] Fix 1 FAILED: found {h1_count} <h1> tag(s) in output HTML")

# ── 13. Chrome headless → PDF ─────────────────────────────────────────────────
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
