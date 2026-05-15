#!/usr/bin/env python3
"""Resilient scraper for data.go.kr 활용신청 현황 (selectAcountList.do).
Each list entry calls fn_detail(uddi, publicDataPk, ...) which posts to
/iim/api/selectAPIAcountView.do — we invoke that function inside the page,
wait for the navigation, scrape the detail page, then go back via history."""
import asyncio, json, re
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
META_OUT = ROOT / "scripts/datago-apis.json"

LIST_URL = "https://www.data.go.kr/iim/api/selectAcountList.do"


async def collect_fn_detail_calls(page):
    """Return list of {title, fn_args=[uddi, pk, idx, prcd]} across all pages."""
    all_calls = []
    seen = set()
    for page_idx in range(1, 6):
        await page.wait_for_load_state("domcontentloaded")
        await page.wait_for_timeout(1200)
        calls = await page.evaluate(r"""
            () => {
              const out = [];
              const anchors = Array.from(document.querySelectorAll('a[href*="fn_detail"]'));
              for (const a of anchors) {
                const href = a.getAttribute('href') || '';
                const m = href.match(/fn_detail\('([^']+)','([^']+)','([^']+)','([^']+)'\)/);
                if (!m) continue;
                const li = a.closest('li,tr');
                out.push({
                  title: (a.textContent||'').replace(/\s+/g,' ').trim().slice(0,200),
                  args: [m[1], m[2], m[3], m[4]],
                  meta: (li?.textContent||'').replace(/\s+/g,' ').trim().slice(0,400)
                });
              }
              return out;
            }
        """)
        new_n = 0
        for c in calls:
            key = c["args"][1]  # publicDataPk
            if key not in seen:
                seen.add(key); all_calls.append(c); new_n += 1
        print(f"  page {page_idx}: +{new_n} (total {len(all_calls)})")
        if new_n == 0:
            break
        # try pagination
        clicked = await page.evaluate(f"""
            () => {{
              const tgt = {page_idx + 1};
              const links = Array.from(document.querySelectorAll('a'));
              for (const a of links) {{
                const hr = a.getAttribute('href') || '';
                const onclick = a.getAttribute('onclick') || '';
                const txt = a.textContent.trim();
                if (txt === String(tgt)) {{ a.click(); return true; }}
                const m = (hr + ' ' + onclick).match(/(?:fn_egov_link_page|pageIndex=|page=)\D*(\d+)/);
                if (m && parseInt(m[1]) === tgt) {{ a.click(); return true; }}
              }}
              const next = document.querySelector('a.next:not(.disabled), a[title=다음]:not(.disabled)');
              if (next) {{ next.click(); return true; }}
              return false;
            }}
        """)
        if not clicked:
            break
        await page.wait_for_timeout(1800)
    return all_calls


async def scrape_detail_for_call(page, call):
    """Run fn_detail in page context, wait for nav, extract info, then go back."""
    args = call["args"]
    # invoke the page's fn_detail function (it submits the form & navigates)
    try:
        await page.evaluate(f"fn_detail('{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}')")
        # wait for navigation away from list
        try:
            await page.wait_for_url(re.compile(r"selectAPIAcountView|openapi"), timeout=20000)
        except:
            pass
        await page.wait_for_load_state("domcontentloaded")
        await page.wait_for_timeout(1500)
    except Exception as e:
        return {"nav_error": str(e), "url": page.url}

    detail_url = page.url
    info = await page.evaluate(r"""
        () => {
          const out = {};
          const ths = Array.from(document.querySelectorAll('th'));
          for (const th of ths) {
            const key = (th.textContent||'').replace(/\s+/g,' ').trim();
            const td = th.nextElementSibling;
            if (td && td.tagName === 'TD') {
              const val = (td.textContent||'').replace(/\s+/g,' ').trim();
              if (key && val) out[key] = val.slice(0, 2500);
            }
          }
          const html = document.body.innerHTML;
          out.__endpoints__ = Array.from(new Set(
            (html.match(/https?:\/\/apis?\.data\.go\.kr\/[A-Za-z0-9_\-\/.?=&%]+/g) || [])
              .map(u => u.split('?')[0].replace(/\/$/, ''))
          )).slice(0,30);
          // any long-looking service keys (60+ chars, base64-safe + percent-encoded)
          const keys = Array.from(document.querySelectorAll('input,textarea')).map(el => (el.value||'').trim())
            .filter(v => v.length >= 50 && /^[A-Za-z0-9%+=\/_-]+$/.test(v));
          out.__serviceKeys__ = Array.from(new Set(keys)).slice(0,4);
          const ops = [];
          for (const t of document.querySelectorAll('table')) {
            const cap = (t.querySelector('caption')?.textContent || '').trim();
            const prev = (t.previousElementSibling?.textContent || '').trim();
            const hint = cap + ' / ' + prev;
            if (/(상세\s*기능|기능정보|오퍼레이션)/.test(hint)) {
              // header row
              const headers = Array.from(t.querySelectorAll('thead th, thead td')).map(c => (c.textContent||'').trim());
              const rows = [];
              for (const r of t.querySelectorAll('tbody tr')) {
                const cells = Array.from(r.querySelectorAll('td')).map(td => (td.textContent||'').replace(/\s+/g,' ').trim());
                if (cells.length >= 2) rows.push(cells);
              }
              if (rows.length) ops.push({hint: hint.slice(0,80), headers, rows});
            }
          }
          out.__operations__ = ops;
          out.__title__ = (document.querySelector('h2.tit, .page-title, .openapi-detail h2')?.textContent || document.title).trim();
          out.__refDocs__ = Array.from(document.querySelectorAll('a[href*=".doc"], a[href*=".pdf"], a[href*=".zip"], a[href*=".hwp"]'))
              .map(a => ({text:(a.textContent||'').trim(), href:a.href})).slice(0,10);
          out.__url__ = location.href;
          return out;
        }
    """)
    info["__url__"] = detail_url
    return info


def save_partial(results):
    META_OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")


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
        await page.wait_for_timeout(1500)

        print("Step 1: collect fn_detail calls ...")
        calls = await collect_fn_detail_calls(page)
        print(f"Total: {len(calls)}")
        save_partial(calls)

        print("Step 2: detail per entry (via fn_detail + back) ...")
        for i, call in enumerate(calls, 1):
            print(f"[{i}/{len(calls)}] {call['title'][:60]}")
            try:
                if "selectAcountList" not in page.url:
                    await page.goto(LIST_URL, wait_until="domcontentloaded")
                    await page.wait_for_timeout(1200)
                call["detail"] = await scrape_detail_for_call(page, call)
            except Exception as e:
                call["detail"] = {"error": str(e)}
                print(f"  ERROR: {e}")
                try:
                    await page.goto(LIST_URL, wait_until="domcontentloaded")
                except: pass
            save_partial(calls)
            await asyncio.sleep(0.4)
        print(f"Done. Wrote {META_OUT}")

asyncio.run(main())
