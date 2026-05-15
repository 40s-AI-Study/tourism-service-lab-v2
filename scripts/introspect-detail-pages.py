#!/usr/bin/env python3
"""Open each target API detail page, click every 확인 button, then dump the full
HTML for offline parsing. This lets us see the real parameter spec."""
import asyncio, json, re
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path("/Users/sklee01/tourism-service-lab-v2")
META = json.load(open(ROOT/"scripts/datago-apis.json", encoding="utf-8"))
OUT = ROOT / "scripts/detail-pages"
OUT.mkdir(parents=True, exist_ok=True)
LIST_URL = "https://www.data.go.kr/iim/api/selectAcountList.do"

TARGETS = [
    "한국관광공사_빅데이터_지역별 방문자수",
    "관광지 집중률 방문자 추이 예측 정보",
    "기초지자체 중심 관광지 정보",
    "지역별 관광 다양성",
    "지역별 관광 수요 강도",
    "지역별 관광 자원 수요",
]


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = None
        for pg in ctx.pages:
            if "data.go.kr" in pg.url: page = pg; break
        if not page:
            page = await ctx.new_page()
        await page.bring_to_front()

        for needle in TARGETS:
            item = next((x for x in META if needle in x["title"]), None)
            if not item: continue
            args = item["args"]
            print(f"=== {needle}")
            await page.goto(LIST_URL, wait_until="domcontentloaded")
            await page.wait_for_timeout(1500)
            await page.evaluate(f"fn_detail('{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}')")
            await page.wait_for_load_state("domcontentloaded")
            await page.wait_for_timeout(2500)
            # Click all 확인 buttons
            try:
                await page.evaluate("""
                    () => {
                      document.querySelectorAll('button, a, input').forEach(el => {
                        const t = (el.textContent||'')+(el.value||'')+(el.getAttribute('onclick')||'');
                        if (t.includes('확인') || /fn_showParam|fn_detailParam|fn_parameter/.test(t)) {
                          try { el.click(); } catch(e) {}
                        }
                      });
                    }
                """)
                await page.wait_for_timeout(4000)
            except Exception as e:
                print(f"  click error {e}")
            html = await page.content()
            slug = re.sub(r"[^\w가-힣]+", "_", needle)
            (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
            print(f"  saved {slug}.html ({len(html)} chars)")
asyncio.run(main())
