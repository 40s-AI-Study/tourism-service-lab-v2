#!/usr/bin/env python3
"""Final fixer: uses EXACT sample params scraped from data.go.kr detail pages.
Each operation gets its spec sample params first, with light fallback variants."""
import json, ssl, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path("/Users/sklee01/tourism-service-lab-v2")
OUT_DIR = ROOT/"docs/data-samples-v2"
CTX = ssl.create_default_context()
CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
SK = "e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e"
COMMON = {"MobileOS": "ETC", "MobileApp": "TripCraftKorea", "_type": "json",
          "numOfRows": "5", "pageNo": "1"}

# Spec sample params straight from data.go.kr detail pages (verified working).
SPEC_PARAMS = [
    ("빅데이터_지역별-방문자수", "DataLabService", "metcoRegnVisitrDDList",
     [{"startYmd": "20210513", "endYmd": "20210513"},
      {"startYmd": "20240101", "endYmd": "20240131"}]),
    ("빅데이터_지역별-방문자수", "DataLabService", "locgoRegnVisitrDDList",
     [{"startYmd": "20210513", "endYmd": "20210513"},
      {"startYmd": "20240101", "endYmd": "20240131"}]),
    ("관광지-집중률-방문자-추이-예측-정보", "TatsCnctrRateService", "tatsCnctrRatedList",
     [{"areaCd": "51", "signguCd": "51130", "tAtsNm": urllib.parse.quote("간현관광지")},
      {"areaCd": "51", "signguCd": "51130"},
      {"areaCd": "11", "signguCd": "11110"}]),
    ("기초지자체-중심-관광지-정보", "LocgoHubTarService1", "areaBasedList1",
     [{"baseYm": "202503", "areaCd": "11", "signguCd": "11530"},
      {"baseYm": "202502", "areaCd": "11", "signguCd": "11530"},
      {"baseYm": "202401", "areaCd": "11", "signguCd": "11110"}]),
    ("지역별-관광-다양성", "AreaTarDivService", "areaTouDivList",
     [{"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "touDivIxCd": "3103"},
      {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "touDivIxCd": "31"},
      {"baseYm": "202401", "areaCd": "11", "signguCd": "11110", "touDivIxCd": "31"}]),
    ("지역별-관광-다양성", "AreaTarDivService", "areaExpDivList",
     [{"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "expDivIxCd": "3201"},
      {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "expDivIxCd": "32"},
      {"baseYm": "202401", "areaCd": "11", "signguCd": "11110", "expDivIxCd": "32"}]),
    ("지역별-관광-다양성", "AreaTarDivService", "areaIntlDivList",
     [{"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "intlDivIxCd": "3301"},
      {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "intlDivIxCd": "33"},
      {"baseYm": "202401", "areaCd": "11", "signguCd": "11110", "intlDivIxCd": "33"}]),
    ("지역별-관광-수요-강도", "AreaTarDemDsService", "areaTarSjrnDsList",
     [{"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarSjrnDsIxCd": "2103"},
      {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarSjrnDsIxCd": "21"},
      {"baseYm": "202401", "areaCd": "11", "signguCd": "11110", "tarSjrnDsIxCd": "21"}]),
    ("지역별-관광-수요-강도", "AreaTarDemDsService", "areaTarExpDsList",
     [{"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarExpDsIxCd": "2201"},
      {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarExpDsIxCd": "22"},
      {"baseYm": "202401", "areaCd": "11", "signguCd": "11110", "tarExpDsIxCd": "22"}]),
    ("지역별-관광-자원-수요", "AreaTarResDemService", "areaTarSvcDemList",
     [{"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarSvcDemIxCd": "1101"},
      {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarSvcDemIxCd": "11"},
      {"baseYm": "202401", "areaCd": "11", "signguCd": "11110", "tarSvcDemIxCd": "11"}]),
    ("지역별-관광-자원-수요", "AreaTarResDemService", "areaCulResDemList",
     [{"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "culResDemIxCd": "1201"},
      {"baseYm": "202401", "areaCd": "11", "signguCd": "11110", "culResDemIxCd": "12"}]),
]


def http_get(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, str(e)


def call(base, op, params):
    qp = {"serviceKey": SK, **COMMON, **params}
    qs = "&".join(f"{k}={v}" for k, v in qp.items())
    url = f"{base}/{op}?{qs}"
    status, body = http_get(url)
    try: j = json.loads(body)
    except Exception: j = {"raw": body[:500]}
    items = 0; total = 0; rcode = None; rmsg = None
    if isinstance(j, dict):
        resp = j.get("response", {})
        hdr = resp.get("header") if isinstance(resp, dict) else None
        if hdr: rcode = hdr.get("resultCode"); rmsg = hdr.get("resultMsg")
        body_ = resp.get("body") if isinstance(resp, dict) else None
        if isinstance(body_, dict):
            total = body_.get("totalCount", 0) or 0
            its = body_.get("items")
            if isinstance(its, dict):
                arr = its.get("item")
                if isinstance(arr, list): items = len(arr)
                elif isinstance(arr, dict): items = 1
            elif isinstance(its, list): items = len(its)
        if "resultCode" in j and "responseTime" in j:
            rcode = j["resultCode"]; rmsg = j.get("resultMsg")
    return {"url": url, "status": status, "items": items, "totalCount": total,
            "resultCode": rcode, "resultMsg": rmsg, "json": j}


summary = []
working_by_slug = {}
for slug, svc, op, candidates in SPEC_PARAMS:
    base = f"https://apis.data.go.kr/B551011/{svc}"
    d = OUT_DIR / slug
    d.mkdir(parents=True, exist_ok=True)
    success = None
    attempts_logged = []
    for params in candidates:
        # retry up to 3 times on 429
        for retry in range(3):
            r = call(base, op, params)
            if r["status"] == 429:
                time.sleep(5); continue
            break
        attempts_logged.append({"params": params, "items": r["items"], "total": r["totalCount"],
                                "code": r["resultCode"], "msg": r["resultMsg"]})
        if r["items"] > 0:
            success = (params, r); break
        time.sleep(0.3)
    if success:
        params, r = success
        (d / f"{op}.json").write_text(json.dumps({
            "ok": True, "status": r["status"], "url": r["url"],
            "params_used": params, "items_count": r["items"],
            "totalCount": r["totalCount"], "json": r["json"],
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        working_by_slug.setdefault(slug, {})[op] = params
        print(f"OK  {op:<25} items={r['items']} total={r['totalCount']} params={params}")
    else:
        print(f"FAIL {op:<25} attempts={len(attempts_logged)} last={attempts_logged[-1]}")
    summary.append({"slug": slug, "op": op,
                    "items": (success[1]["items"] if success else 0),
                    "total": (success[1]["totalCount"] if success else 0),
                    "params": success[0] if success else None,
                    "attempts": attempts_logged})

for slug, w in working_by_slug.items():
    (OUT_DIR/slug/"_working-params.json").write_text(
        json.dumps(w, ensure_ascii=False, indent=2), encoding="utf-8")

(ROOT/"scripts/fix-empty-apis-report.json").write_text(
    json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
ok = sum(1 for s in summary if s["items"] > 0)
print(f"\nSUMMARY: {ok}/{len(summary)} ops returned data")
