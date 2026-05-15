#!/usr/bin/env python3
"""Fetch real samples for all 17 approved KTO APIs using metadata
scraped from data.go.kr by scrape-datago-apis.py."""
import json, re, time, urllib.parse, urllib.request, ssl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "scripts/datago-apis.json"
OUT_DIR = ROOT / "docs/data-samples-v2"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

COMMON = {
    "MobileOS": "ETC",
    "MobileApp": "TripCraftKorea",
    "_type": "json",
    "numOfRows": "5",
    "pageNo": "1",
}

# extra parameters required per operation (where known)
# operation name lowercased -> dict of extra params
OP_EXTRAS = {
    "areabasedlist1": {"arrange": "A"},
    "areabasedlist2": {"arrange": "A"},
    "locationbasedlist1": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "2000"},
    "locationbasedlist2": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "2000"},
    "searchkeyword1": {"keyword": urllib.parse.quote("경복궁")},
    "searchkeyword2": {"keyword": urllib.parse.quote("경복궁")},
    "searchfestival1": {"eventStartDate": "20260101"},
    "searchfestival2": {"eventStartDate": "20260101"},
    "searchstay1": {},
    "searchstay2": {},
    "detailcommon1": {"contentId": "126508"},
    "detailcommon2": {"contentId": "126508"},
    "detailintro1": {"contentId": "126508", "contentTypeId": "12"},
    "detailintro2": {"contentId": "126508", "contentTypeId": "12"},
    "detailinfo1": {"contentId": "142785", "contentTypeId": "32"},
    "detailinfo2": {"contentId": "142785", "contentTypeId": "32"},
    "detailimage1": {"contentId": "126508"},
    "detailimage2": {"contentId": "126508"},
    "gallerylist1": {},
    "gallerysearchlist1": {"keyword": urllib.parse.quote("경복궁")},
    "ldongcode": {},
    "ldongcode2": {},
    "areacode1": {},
    "areacode2": {},
    "categorycode1": {},
    "categorycode2": {},
    "servicecategory1": {},
    "tatscnctrratelist": {"baseYmd": "20241201"},
    "tatscnctrratedlist": {"baseYmd": "20241201"},
    "metcoregnvisitrlist": {"baseYm": "202412"},
    "metcoregnvisitrddlist": {"baseYmd": "20241201"},
    "locgoregnvisitrddlist": {"baseYmd": "20241201"},
    "locgoregnvisitrlist": {"baseYm": "202412"},
    "areaculresdemlist": {"baseYm": "202412"},
    "areatarsvcdemlist": {"baseYm": "202412"},
    "areataresjrndslist": {"baseYm": "202412"},
    "areatarsjrndslist": {"baseYm": "202412"},
    "areatarexpdslist": {"baseYm": "202412"},
    "areatoudivlist": {"baseYm": "202412"},
    "areatarconsdivlist": {"baseYm": "202412"},
    "areatarforndivlist": {"baseYm": "202412"},
    "areatardomdivlist": {"baseYm": "202412"},
    "basedlist": {},  # gocamping
    "imagelist": {},
    "searchlist": {"keyword": urllib.parse.quote("캠핑")},
    "syncList": {"syncModTime": "20241201000000"},
    "synclist": {"syncModTime": "20241201000000"},
    "themebasedlist": {},
    "themelocationbasedlist": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "2000"},
    "themesearchlist": {"keyword": urllib.parse.quote("경복궁")},
    "storybasedlist": {"contentId": "1"},
    "storylocationbasedlist": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "2000"},
    "storysearchlist": {"keyword": urllib.parse.quote("경복궁")},
    "courselist": {},
    "courseimagelist": {"crsKorNm": urllib.parse.quote("북한산둘레길")},
    "subroutelist": {"crsIdx": "1"},
    "promotionlist": {},
    "courselocationbasedlist": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "5000"},
    "themelist": {},
    "withtouractivitylist": {},
    "ecotourrecmlocationbasedlist": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "5000"},
    "ecotourrecmlocationlist": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "5000"},
    "wellnessdongcodelist": {},
    "wellnessareacodelist": {},
    "wellnesscategorycodelist": {},
    "wellnessdetailcommon": {"contentId": "1"},
    "wellnessdetailimage": {"contentId": "1"},
    "wellnessareabasedlist": {"arrange": "A"},
    "wellnesslocationbasedlist": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "5000"},
    "wellnesssearchkeyword": {"keyword": urllib.parse.quote("스파")},
    "wellnesssearchfestival": {"eventStartDate": "20260101"},
    "wellnesssearchstay": {},
    "mdclareabasedlist": {"arrange": "A"},
    "mdcllocationbasedlist": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "5000"},
    "mdclsearchkeyword": {"keyword": urllib.parse.quote("의료")},
    "mdcldetailcommon": {"contentId": "1"},
    "mdclareacode": {},
    "petareacode2": {},
    "petareabasedlist2": {"arrange": "A"},
    "petsearchkeyword2": {"keyword": urllib.parse.quote("애견")},
    "petlocationbasedlist2": {"mapX": "126.9779692", "mapY": "37.566535", "radius": "5000"},
    "petdetailcommon2": {"contentId": "1"},
    "petdetailintro2": {"contentId": "1", "contentTypeId": "12"},
    "petdetailimage2": {"contentId": "1"},
    "petsearchfestival2": {"eventStartDate": "20260101"},
    "petsearchstay2": {},
    "petcategorycode2": {},
    "petldongcode2": {},
}

# Title to slug mapping
def slugify(title):
    t = re.sub(r'^\[승인\]\s*한국관광공사_', '', title)
    t = re.sub(r'\s*_GW\s*$', '', t)
    t = re.sub(r'[^\w가-힣]+', '-', t).strip('-')
    return t


def extract_operations(detail):
    """Walk __operations__ tables and harvest operation names."""
    ops = set()
    for t in detail.get("__operations__", []):
        for r in t.get("rows", []):
            for cell in r:
                # operation name patterns: alphabet+digit camelCase, length 5-40
                for m in re.finditer(r'\b([a-zA-Z][a-zA-Z0-9]{4,39})\b', cell):
                    cand = m.group(1)
                    if cand in ("MobileOS","MobileApp","contentTypeId","contentId","arrange",
                                "numOfRows","pageNo","serviceKey","mapX","mapY","baseYmd",
                                "baseYm","keyword","radius","eventStartDate","cat1","cat2","cat3"):
                        continue
                    # heuristic: must contain at least one lowercase + camelcase pattern OR endswith List/list etc.
                    if re.search(r'[a-z][A-Z]', cand) or cand.endswith("List") or cand.endswith("list") \
                       or cand.endswith("Code") or cand.endswith("code"):
                        ops.add(cand)
    return sorted(ops)


def get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "TripCraftKorea/1.0"})
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        body = r.read()
        ct = r.headers.get("Content-Type","")
        return r.status, ct, body


def call_op(base, op, service_key):
    extras = OP_EXTRAS.get(op.lower(), {})
    params = {**COMMON, **extras, "serviceKey": service_key}
    q = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{base.rstrip('/')}/{op}?{q}"
    try:
        st, ct, body = get(url, timeout=20)
    except Exception as e:
        return {"ok": False, "error": str(e), "url": url}
    txt = body.decode("utf-8", errors="replace")
    out = {"ok": st == 200, "status": st, "contentType": ct, "url": url}
    # try JSON parse
    try:
        out["json"] = json.loads(txt)
    except:
        out["text"] = txt[:8000]
    # Check resultCode from KTO standard envelope
    if "json" in out and isinstance(out["json"], dict):
        rc = (out["json"].get("response", {}).get("header", {}) or {}).get("resultCode")
        if rc and rc != "0000":
            out["ok"] = False
            out["resultCode"] = rc
            out["resultMsg"] = out["json"].get("response", {}).get("header", {}).get("resultMsg", "")
    return out


def main():
    meta = json.load(open(META, encoding="utf-8"))
    summary = []
    for api in meta:
        title = api["title"]
        slug = slugify(title)
        d = api.get("detail", {})
        endpoints = d.get("__endpoints__", [])
        # base URL = first endpoint without operation path
        base = None
        for e in endpoints:
            # bare service base = /B551011/{Service}
            m = re.match(r'^https?://apis?\.data\.go\.kr/(B[0-9A-Za-z]+)/([A-Za-z][A-Za-z0-9_]+)(?:/|$)', e)
            if m:
                base = f"https://apis.data.go.kr/{m.group(1)}/{m.group(2)}"
                break
        keys = d.get("__serviceKeys__", [])
        skey = keys[0] if keys else ""
        ops = extract_operations(d)
        # also include operation names appearing in endpoints
        for e in endpoints:
            m = re.match(r'.+/(B[0-9A-Za-z]+)/[A-Za-z0-9_]+/([A-Za-z][A-Za-z0-9_]+)', e)
            if m:
                op = m.group(2)
                if op and op not in ops:
                    ops.append(op)
        ops = sorted(set(ops))
        api_dir = OUT_DIR / slug
        api_dir.mkdir(exist_ok=True, parents=True)
        meta_path = api_dir / "_meta.json"
        meta_path.write_text(json.dumps({
            "title": title,
            "base": base,
            "endpoints": endpoints,
            "operations_attempted": ops,
            "serviceKey_present": bool(skey),
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        if not base or not skey:
            summary.append({"slug": slug, "title": title, "ops": len(ops), "success": 0, "fail": len(ops), "note": "missing base or key"})
            continue
        success = fail = 0
        errors = []
        for op in ops:
            res = call_op(base, op, skey)
            # save trimmed
            outfile = api_dir / f"{op}.json"
            payload = {k: v for k, v in res.items() if k != "json"}
            if "json" in res:
                # trim
                try:
                    j = res["json"]
                    items = j.get("response", {}).get("body", {}).get("items", {})
                    if isinstance(items, dict) and isinstance(items.get("item"), list):
                        items["item"] = items["item"][:5]
                    payload["json"] = j
                except:
                    payload["json"] = res["json"]
            outfile.write_text(json.dumps(payload, ensure_ascii=False, indent=2)[:60000], encoding="utf-8")
            if res["ok"]:
                success += 1
                print(f"  [OK] {slug}/{op}")
            else:
                fail += 1
                errors.append(f"{op}: {res.get('resultCode') or res.get('status') or res.get('error')}")
                print(f"  [FAIL {res.get('status','?')}] {slug}/{op}: {res.get('resultCode') or res.get('error','')}")
        (api_dir / "errors.log").write_text("\n".join(errors), encoding="utf-8")
        summary.append({"slug": slug, "title": title, "ops": len(ops), "success": success, "fail": fail})
        print(f"==> {slug}: {success}/{len(ops)} success")
    (OUT_DIR / "_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
