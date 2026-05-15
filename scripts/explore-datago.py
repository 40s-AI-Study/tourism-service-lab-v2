#!/usr/bin/env python3
"""Connect to running Chrome via CDP, scrape data.go.kr account list page,
extract 17 API entries with detail URLs, and write metadata JSON."""
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright

OUT = Path(__file__).resolve().parent.parent / "scripts/datago-list.json"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        ctx = browser.contexts[0]
        # find data.go.kr account tab
        target = None
        for page in ctx.pages:
            if "selectAcountList" in page.url:
                target = page
                break
        if not target:
            target = await ctx.new_page()
            await target.goto("https://www.data.go.kr/iim/api/selectAcountList.do", wait_until="domcontentloaded")
            await target.wait_for_timeout(2000)

        print("URL:", target.url)
        # wait for list
        await target.wait_for_load_state("domcontentloaded")
        await target.wait_for_timeout(1500)

        # extract all API entries
        items = await target.evaluate("""
            () => {
              const rows = Array.from(document.querySelectorAll('div.result-list ul li, .api-list li, .acount-list li'));
              if (rows.length === 0) {
                // generic fallback: look for anchors that link to data detail pages
                const anchors = Array.from(document.querySelectorAll('a'));
                return anchors
                  .filter(a => /\\/data\\/\\d+\\/openapi/.test(a.getAttribute('href') || ''))
                  .map(a => ({title: (a.textContent||'').trim().slice(0,200), href: a.href}));
              }
              return rows.map(li => {
                const a = li.querySelector('a');
                return {
                  title: (a?.textContent || li.textContent || '').trim().slice(0, 200),
                  href: a?.href || ''
                };
              }).filter(x => x.href);
            }
        """)
        print(f"Found {len(items)} entries")
        # Dump page HTML for debugging if 0
        if not items:
            html = await target.content()
            (OUT.parent / "datago-list.html").write_text(html, encoding="utf-8")
            print("Saved HTML for inspection")
        OUT.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote {OUT}")

asyncio.run(main())
