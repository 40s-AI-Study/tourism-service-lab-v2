#!/usr/bin/env python3
"""Re-fetch 6 bigdata APIs that returned empty/error results in v2 run.

Root causes identified from manuals:
- DataLabService: uses startYmd/endYmd (not baseYmd), no areaCd filter
- LocgoHubTarService1: signguCd is mandatory (was missing)
- AreaTarDivService: index code params (touDivIxCd/expDivIxCd/intlDivIxCd) needed, baseYm=202509
- AreaTarDemDsService: index code params (tarSjrnDsIxCd/tarExpDsIxCd) needed, baseYm=202509
- AreaTarResDemService: index code params (culResDemIxCd/tarSvcDemIxCd) needed, baseYm=202509
- TatsCnctrRateService/tatsCnctrRatedList: needs areaCd+signguCd+tAtsNm
"""
import json, time, urllib.request, ssl
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "docs/data-samples-v2"
SERVICE_KEY = "e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e"

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

COMMON = "MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1"
BASE = "https://apis.data.go.kr/B551011"
SK = f"serviceKey={SERVICE_KEY}"

CALLS = [
    # 1. DataLabService - locgoRegnVisitrDDList (기초지자체 일별 방문자)
    {
        "dir": "빅데이터_지역별-방문자수",
        "op": "locgoRegnVisitrDDList",
        "url": f"{BASE}/DataLabService/locgoRegnVisitrDDList?{SK}&{COMMON}&startYmd=20210513&endYmd=20210513",
    },
    # 2. DataLabService - metcoRegnVisitrDDList (광역지자체 일별 방문자) - no areaCd
    {
        "dir": "빅데이터_지역별-방문자수",
        "op": "metcoRegnVisitrDDList",
        "url": f"{BASE}/DataLabService/metcoRegnVisitrDDList?{SK}&{COMMON}&startYmd=20210513&endYmd=20210513",
    },
    # 3. LocgoHubTarService1 - areaBasedList1 (기초지자체 중심관광지) - signguCd mandatory
    {
        "dir": "기초지자체-중심-관광지-정보",
        "op": "areaBasedList1",
        "url": f"{BASE}/LocgoHubTarService1/areaBasedList1?{SK}&{COMMON}&baseYm=202404&areaCd=11&signguCd=11530",
    },
    # 4. TatsCnctrRateService - tatsCnctrRatedList (관광지 집중률 예측) - needs areaCd+tAtsNm
    {
        "dir": "관광지-집중률-방문자-추이-예측",
        "op": "tatsCnctrRatedList",
        "url": f"{BASE}/TatsCnctrRateService/tatsCnctrRatedList?{SK}&{COMMON}&areaCd=51&signguCd=51130&tAtsNm=%EA%B0%84%ED%98%84%EA%B4%80%EA%B4%91%EC%A7%80",
    },
    # 5. AreaTarDivService - areaTouDivList (관광객 다양성)
    {
        "dir": "지역별-관광-다양성",
        "op": "areaTouDivList",
        "url": f"{BASE}/AreaTarDivService/areaTouDivList?{SK}&{COMMON}&baseYm=202509&areaCd=11&signguCd=11530&touDivIxCd=3101",
    },
    # 6. AreaTarDivService - areaExpDivList (관광 소비 다양성)
    {
        "dir": "지역별-관광-다양성",
        "op": "areaExpDivList",
        "url": f"{BASE}/AreaTarDivService/areaExpDivList?{SK}&{COMMON}&baseYm=202504&areaCd=51&signguCd=51130&expDivIxCd=3204",
    },
    # 7. AreaTarDivService - areaIntlDivList (국제적 다양성)
    {
        "dir": "지역별-관광-다양성",
        "op": "areaIntlDivList",
        "url": f"{BASE}/AreaTarDivService/areaIntlDivList?{SK}&{COMMON}&baseYm=202504&areaCd=11&signguCd=11530&intlDivIxCd=3303",
    },
    # 8. AreaTarDemDsService - areaTarSjrnDsList (관광 체류 강도)
    {
        "dir": "지역별-관광-수요-강도",
        "op": "areaTarSjrnDsList",
        "url": f"{BASE}/AreaTarDemDsService/areaTarSjrnDsList?{SK}&{COMMON}&baseYm=202509&areaCd=11&signguCd=11530&tarSjrnDsIxCd=2101",
    },
    # 9. AreaTarDemDsService - areaTarExpDsList (관광 소비 강도)
    {
        "dir": "지역별-관광-수요-강도",
        "op": "areaTarExpDsList",
        "url": f"{BASE}/AreaTarDemDsService/areaTarExpDsList?{SK}&{COMMON}&baseYm=202509&areaCd=11&signguCd=11530&tarExpDsIxCd=2201",
    },
    # 10. AreaTarResDemService - areaCulResDemList (문화 자원 수요)
    {
        "dir": "지역별-관광-자원-수요",
        "op": "areaCulResDemList",
        "url": f"{BASE}/AreaTarResDemService/areaCulResDemList?{SK}&{COMMON}&baseYm=202404&areaCd=11&signguCd=11530&culResDemIxCd=1205",
    },
    # 11. AreaTarResDemService - areaTarSvcDemList (관광 서비스 수요)
    {
        "dir": "지역별-관광-자원-수요",
        "op": "areaTarSvcDemList",
        "url": f"{BASE}/AreaTarResDemService/areaTarSvcDemList?{SK}&{COMMON}&baseYm=202509&areaCd=11&signguCd=11530&tarSvcDemIxCd=1112",
    },
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "TripCraftKorea/1.0"})
    with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
        body = r.read()
        ct = r.headers.get("Content-Type", "")
        return r.status, ct, body


def main():
    results = []
    for c in CALLS:
        api_dir = OUT_DIR / c["dir"]
        api_dir.mkdir(parents=True, exist_ok=True)
        out_path = api_dir / f"{c['op']}.json"
        print(f"Fetching {c['dir']}/{c['op']} ...")
        try:
            st, ct, body = fetch(c["url"])
            txt = body.decode("utf-8", errors="replace")
            payload = {"ok": st == 200, "status": st, "contentType": ct, "url": c["url"]}
            try:
                j = json.loads(txt)
                # Trim items list to 5
                try:
                    items = j["response"]["body"]["items"]
                    if isinstance(items, dict) and isinstance(items.get("item"), list):
                        items["item"] = items["item"][:5]
                except Exception:
                    pass
                payload["json"] = j
                # Check result code
                rc = j.get("response", {}).get("header", {}).get("resultCode", "")
                tc = j.get("response", {}).get("body", {}).get("totalCount", -1)
                if rc == "0000" and tc != 0:
                    payload["ok"] = True
                    print(f"  [OK] totalCount={tc}")
                elif rc == "0000" and tc == 0:
                    payload["ok"] = False
                    print(f"  [EMPTY] totalCount=0 - data may not exist for this period/area")
                else:
                    payload["ok"] = False
                    msg = j.get("response", {}).get("header", {}).get("resultMsg", "") or \
                          j.get("resultMsg", "")
                    print(f"  [FAIL] resultCode={rc} msg={msg}")
            except Exception:
                payload["text"] = txt[:8000]
                print(f"  [NON-JSON] status={st}")
        except Exception as e:
            payload = {"ok": False, "error": str(e), "url": c["url"]}
            print(f"  [ERROR] {e}")
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        results.append({"dir": c["dir"], "op": c["op"], "ok": payload.get("ok", False)})
        time.sleep(0.3)

    print("\n=== Summary ===")
    for r in results:
        status = "OK" if r["ok"] else "FAIL"
        print(f"  [{status}] {r['dir']}/{r['op']}")

    ok_count = sum(1 for r in results if r["ok"])
    print(f"\n{ok_count}/{len(results)} succeeded")
    return ok_count


if __name__ == "__main__":
    main()
