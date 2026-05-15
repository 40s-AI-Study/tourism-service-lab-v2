#!/usr/bin/env python3
"""For each of the 6 big-data/concentration/audio APIs that returned 0 items with manual params,
visit their data.go.kr detail page, click 미리보기 buttons to capture the auto-generated
sample request URLs (which include correct param formats), then re-call to save real samples."""
import asyncio, json, re, urllib.request, ssl
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path("/Users/sklee01/tourism-service-lab-v2")
META = json.load(open(ROOT/"scripts/datago-apis.json", encoding="utf-8"))
CAPTURE = ROOT / "scripts/preview-urls.json"
CTX = ssl.create_default_context()
CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
SK = "e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e"
LIST_URL = "https://www.data.go.kr/iim/api/selectAcountList.do"


async def capture_for_api(page, call):
    """Navigate to detail page, click each 미리보기, capture window.open URL."""
    args = call["args"]
    print(f"  navigate: {call['title'][:60]}")
    # ensure we are on list page
    if "selectAcountList" not in page.url:
        await page.goto(LIST_URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(1200)
    await page.evaluate(f"fn_detail('{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}')")
    try:
        await page.wait_for_url(re.compile(r"selectAPIAcountView|openapi"), timeout=20000)
    except: pass
    await page.wait_for_load_state("domcontentloaded")
    await page.wait_for_timeout(1500)

    # Capture popup URLs by overriding window.open
    await page.evaluate(r"""
        () => {
          window.__capturedUrls = [];
          const orig = window.open;
          window.open = function(url, ...rest) {
            window.__capturedUrls.push(url);
            return { closed: true, close(){}, focus(){}, document: {} };
          };
        }
    """)
    # Find all 미리보기 buttons / links and click them
    preview_buttons = await page.query_selector_all(
        "button:has-text('미리보기'), a:has-text('미리보기'), input[value='미리보기']"
    )
    print(f"    found {len(preview_buttons)} preview buttons")
    # buttons may be JS handlers using onclick="fn_preview(...)" or similar
    for btn in preview_buttons:
        try:
            await btn.click()
            await page.wait_for_timeout(800)
        except Exception as e:
            pass
    captured = await page.evaluate("window.__capturedUrls || []")
    return captured


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        page = None
        for pg in ctx.pages:
            if "selectAcountList" in pg.url:
                page = pg; break
        if not page:
            page = await ctx.new_page()
            await page.goto(LIST_URL, wait_until="domcontentloaded")
        await page.bring_to_front()

        targets = []
        keywords = ["빅데이터", "집중률", "다양성", "수요-강도", "수요 강도", "자원-수요", "자원 수요", "기초지자체"]
        for item in META:
            title = item["title"]
            if any(k in title for k in keywords):
                targets.append(item)
        print(f"targets: {len(targets)}")

        results = {}
        for t in targets:
            urls = await capture_for_api(page, t)
            results[t["title"]] = urls
            print(f"  captured {len(urls)} urls for {t['title'][:50]}")
            for u in urls[:6]:
                print(f"    -> {u[:120]}")
            CAPTURE.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote {CAPTURE}")

asyncio.run(main())
