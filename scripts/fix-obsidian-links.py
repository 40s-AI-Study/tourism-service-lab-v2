#!/usr/bin/env python3
"""Convert slug IDs in related: frontmatter and body [[slug]] links to [[파일명]] format."""

import os
import re

# Slug → actual filename (without .md) mapping
SLUG_MAP = {
    "ai-course-generator": "KoreaPath AI - 개인화 동선 자동 생성 + 혼잡도 최적화 앱",
    "multilingual-guide": "K-Guide Global - 외국인 전용 다국어 통합 한국 관광 가이드",
    "pet-friendly-travel": "PetTrip Korea - 반려동물 동반 여행 전문 플랫폼",
    "barrier-free-travel": "FreeTrip Korea - 무장애·접근성 특화 관광 플랫폼",
    "wellness-tour": "WellKorea - 웰니스 여행 큐레이터 앱",
    "kculture-pilgrimage": "K-Universe - K-컬처 성지순례 + 팬 여행 앱",
    "hidden-spot-congestion": "LocalSecret - 혼잡 회피 + 숨은 명소 발견 앱",
    "family-trip-planner": "FamilyKorea - 가족여행 올인원 스마트 플래너",
    "eco-green-trail": "GreenTrail Korea - 에코 투어 & 트레킹 가이드",
    "night-tourism": "NightKorea - 한국 야간 관광 특화 앱",
    "access-korea": "AccessKorea - 무장애 여행 통합 플랫폼",
    "p1-korean-20s-solo": "김지원, 25세, 그래픽 디자이너",
    "p2-korean-30s-couple": "박민준 & 이수연, 3331세, 직장인 커플",
    "p3-korean-40s-family": "최동훈, 44세, 중학교 교사 (초등생 자녀 2명)",
    "p4-foreign-20s-backpacker": "Emma Chen, 23, Freelance Photographer (Taiwan)",
    "p5-foreign-30s-business-leisure": "David Park, 35, Senior Product Manager (USA)",
}

def convert_related_line(line):
    """Convert `related: [slug1, slug2]` to multi-line `related:\n  - "[[name]]"\n  - "[[name]]"` format."""
    match = re.match(r'^related:\s*\[([^\]]+)\]\s*$', line)
    if not match:
        return line, False

    slugs = [s.strip() for s in match.group(1).split(',')]
    items = []
    for slug in slugs:
        if slug in SLUG_MAP:
            items.append(f'  - "[[{SLUG_MAP[slug]}]]"')
        else:
            items.append(f'  - "[[{slug}]]"')  # unknown slug, keep as-is wrapped
            print(f"  WARNING: unknown slug '{slug}', wrapped as-is")

    return "related:\n" + "\n".join(items), True

def convert_body_slugs(text):
    """Replace [[slug-id]] with [[파일명]] in body text."""
    def replace_match(m):
        slug = m.group(1)
        if slug in SLUG_MAP:
            return f"[[{SLUG_MAP[slug]}]]"
        return m.group(0)

    return re.sub(r'\[\[([a-z][a-z0-9-]+)\]\]', replace_match, text)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Split into frontmatter and body
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front = parts[1]
            body = parts[2]

            # Convert related: line in frontmatter
            new_front_lines = []
            changed = False
            for line in front.split('\n'):
                new_line, was_changed = convert_related_line(line)
                new_front_lines.append(new_line)
                if was_changed:
                    changed = True

            new_front = '\n'.join(new_front_lines)
            # Convert [[slug]] in body
            new_body = convert_body_slugs(body)

            content = '---' + new_front + '---' + new_body
        else:
            content = convert_body_slugs(content)
    else:
        content = convert_body_slugs(content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kb = os.path.join(base, 'knowledge-base')

    changed_files = []
    for root, dirs, files in os.walk(kb):
        # Skip hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, base)
            if process_file(fpath):
                changed_files.append(rel)
                print(f"  FIXED: {rel}")

    print(f"\nTotal files changed: {len(changed_files)}")
    return changed_files

if __name__ == '__main__':
    main()
