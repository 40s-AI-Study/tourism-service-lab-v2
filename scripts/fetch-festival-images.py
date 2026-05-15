#!/usr/bin/env python3
"""Fetch festival background images from KTO API for Instagram card news."""
import json, urllib.parse, urllib.request, ssl, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "scripts/datago-apis.json"
OUT = ROOT / "deliverables/card-news-instagram/images"
OUT.mkdir(parents=True, exist_ok=True)

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

m = json.load(open(META, encoding="utf-8"))
SKEY = None
BASE = None
for api in m:
    if "국문 관광정보" in api["title"]:
        keys = api.get("detail", {}).get("__serviceKeys__", [])
        SKEY = keys[0] if keys else None
        for e in api.get("detail", {}).get("__endpoints__", []):
            if "/KorService2" in e:
                BASE = "https://apis.data.go.kr/B551011/KorService2"
                break
        break
assert SKEY and BASE, "missing key or base"

FESTIVALS = [
    ("01-lotus-lantern", ["연등회"]),
    ("02-global-culture", ["서울세계도시문화축제", "세계도시문화", "DDP 문화축제"]),
    ("03-jamsugyo-bridge", ["잠수교"]),
    ("04-rose-festival", ["중랑장미축제", "장미축제", "중랑 장미"]),
    ("05-garden-expo", ["서울국제정원박람회", "정원박람회", "국제정원"]),
]

COMMON = {
    "MobileOS": "ETC",
    "MobileApp": "TripCraftKorea",
    "_type": "json",
    "numOfRows": "10",
    "pageNo": "1",
    "serviceKey": SKEY,
}

def call(op, extra):
    qs = urllib.parse.urlencode({**COMMON, **extra})
    url = f"{BASE}/{op}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=CTX, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))

def items(resp):
    try:
        it = resp["response"]["body"]["items"]
        if isinstance(it, dict) and "item" in it:
            v = it["item"]
            return v if isinstance(v, list) else [v]
    except Exception:
        pass
    return []

results = {}
for slug, kws in FESTIVALS:
    print(f"\n=== {slug}: {kws} ===")
    its = []
    for kw in kws:
        r = call("searchKeyword2", {"keyword": kw, "contentTypeId": "15"})
        its = items(r)
        if its:
            print(f"  hit (festival): '{kw}' -> {len(its)}")
            break
        r = call("searchKeyword2", {"keyword": kw})
        its = items(r)
        if its:
            print(f"  hit (any): '{kw}' -> {len(its)}")
            break
    print(f"  found {len(its)} items")
    chosen = None
    for it in its:
        if it.get("firstimage"):
            chosen = it
            break
    if not chosen and its:
        chosen = its[0]
    if not chosen:
        print("  NO MATCH")
        continue
    cid = chosen.get("contentid")
    title = chosen.get("title")
    first = chosen.get("firstimage") or chosen.get("firstimage2")
    print(f"  pick: {title} (cid={cid}) firstimage={first}")
    urls = []
    if first:
        urls.append(first)
    # also fetch detail images
    try:
        di = call("detailImage2", {"contentId": cid, "imageYN": "Y"})
        for x in items(di):
            u = x.get("originimgurl")
            if u and u not in urls:
                urls.append(u)
    except Exception as e:
        print(f"  detailImage2 err: {e}")
    # download up to 3
    saved = []
    for i, u in enumerate(urls[:3]):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, context=CTX, timeout=20) as rr:
                data = rr.read()
            ext = ".jpg"
            if u.lower().endswith(".png"):
                ext = ".png"
            fname = f"{slug}-{i+1}{ext}"
            (OUT / fname).write_bytes(data)
            saved.append(fname)
            print(f"  saved {fname} ({len(data)//1024} KB)")
        except Exception as e:
            print(f"  dl err {u}: {e}")
    results[slug] = {"title": title, "contentid": cid, "files": saved}

(OUT / "manifest.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print("\nDONE. manifest:", OUT / "manifest.json")
