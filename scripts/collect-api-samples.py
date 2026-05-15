#!/usr/bin/env python3
"""
한국관광공사 OpenAPI 27종 샘플데이터 수집 스크립트
Usage: python3 scripts/collect-api-samples.py --service-key YOUR_KEY
       python3 scripts/collect-api-samples.py --service-key YOUR_KEY --api gocamping
"""
import argparse
import json
import os
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime
from pathlib import Path

BASE_URL = "http://apis.data.go.kr/B551011"
OUTPUT_DIR = Path("docs/data-samples")
ERRORS_LOG = OUTPUT_DIR / "errors.log"

# 27개 API ID → (서비스명, 대표 파라미터) 매핑
API_MAP = {
    # ── i18n 다국어 관광정보 (8개) ──────────────────────────────────
    "tourism-info-korean": {
        "service": "KorService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-info-english": {
        "service": "EngService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-info-japanese": {
        "service": "JpnService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-info-chinese-simplified": {
        "service": "ChsService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-info-chinese-traditional": {
        "service": "ChtService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-info-german": {
        "service": "GerService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-info-french": {
        "service": "FreService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-info-spanish": {
        "service": "SpaService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-info-russian": {
        "service": "RusService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    # ── 테마 관광 (7개) ──────────────────────────────────────────────
    "gocamping": {
        "service": "GoCamping1",
        "params": {"numOfRows": "5", "pageNo": "1"},
    },
    "wellness-tourism": {
        "service": "WellnessTourismService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "medical-tourism": {
        "service": "MdcltourismService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "pet-friendly-travel": {
        "service": "PetTour1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "durunubi-trails": {
        "service": "DurunubiService1",
        "params": {"numOfRows": "5", "pageNo": "1"},
    },
    "eco-tourism": {
        "service": "EcoTourismService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "barrier-free-travel": {
        "service": "DisabledTourService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    # ── 콘텐츠 (3개) ────────────────────────────────────────────────
    "tourism-photos": {
        "service": "PhotoService1",
        "params": {"numOfRows": "5", "pageNo": "1"},
    },
    "photo-contest-winners": {
        "service": "PhotoAwardService1",
        "params": {"numOfRows": "5", "pageNo": "1"},
    },
    "audio-guide": {
        "service": "AudioGuideService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    # ── 빅데이터 지수 (4개) ──────────────────────────────────────────
    "area-tourism-resource-demand": {
        "service": "TouristAreaService1",
        "params": {"YM": "202312", "numOfRows": "5", "pageNo": "1"},
    },
    "area-tourism-demand-density": {
        "service": "TouristAreaService1",
        "params": {"YM": "202312", "numOfRows": "5", "pageNo": "1"},
    },
    "area-tourism-diversity": {
        "service": "TouristAreaService1",
        "params": {"YM": "202312", "numOfRows": "5", "pageNo": "1"},
    },
    "tourism-big-data": {
        "service": "TourBigDataService1",
        "params": {"YM": "202312", "numOfRows": "5", "pageNo": "1"},
    },
    # ── 연관성·예측 (3개) ────────────────────────────────────────────
    "related-attractions": {
        "service": "RelatedTourService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "central-attractions-by-municipality": {
        "service": "CentralTourService1",
        "params": {"areaCode": "1", "numOfRows": "5", "pageNo": "1"},
    },
    "visitor-concentration-forecast": {
        "service": "VisitorForecastService1",
        "params": {"YM": "202312", "numOfRows": "5", "pageNo": "1"},
    },
    # ── 산업 (1개) ───────────────────────────────────────────────────
    "tourism-jobs": {
        "service": "JobTourService1",
        "params": {"numOfRows": "5", "pageNo": "1"},
    },
}

# 각 API 오퍼레이션 목록
OPERATIONS = {
    "area-tourism-demand-density": ["areaTarExpDsList", "areaTarSjrnDsList"],
    "area-tourism-diversity": ["areaExpDivList", "areaIntlDivList", "areaTouDivList"],
    "area-tourism-resource-demand": ["areaCulResDemList", "areaTarSvcDemList"],
    "audio-guide": ["storyBasedList", "storyBasedSyncList", "storyLocationBasedList", "storySearchList",
                    "themeBaseSyncdList", "themeBasedList", "themeBasedSyncList", "themeCategory",
                    "themeLocationBasedList", "themeSearchList"],
    "barrier-free-travel": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2", "detailImage2",
                            "detailInfo2", "locationBasedList2", "searchKeyword2", "subImageYN"],
    "central-attractions-by-municipality": ["areaBasedList", "areaBasedList1"],
    "durunubi-trails": ["courseList", "crsTourInfo", "routeList"],
    "eco-tourism": ["areaBasedList", "areaBasedList1", "areaBasedSyncList1"],
    "gocamping": ["basedList", "basedSyncList", "firstImageUrl", "imageList", "locationBasedList", "searchList"],
    "medical-tourism": ["areaBasedList", "corprHsptlInfo", "detailCommon", "hmpgInfo", "insttDevInfo",
                        "lDongListYn", "locationBasedList", "mainMdlcSubjInfo", "mdclTursmDivInfo",
                        "mdclTursmSyncList", "orgImage", "prSnsInfo", "searchKeyword", "specFcltyInfo",
                        "specProcMdlcInfo"],
    "pet-friendly-travel": ["areaBasedList2", "detailCommon2", "detailImage2", "detailInfo2",
                            "etcAcmpyInfo", "lDongListYn", "locationBasedList2", "petTourSyncList2",
                            "searchKeyword2", "subImageYN"],
    "photo-contest-winners": ["enKeyword", "koKeyword", "orgImage", "phokoAwrdList", "phokoAwrdSyncList", "thumbImage"],
    "related-attractions": ["areaBasedList1", "searchKeyword", "searchKeyword1"],
    "tourism-big-data": ["locgoRegnVisitrDDList", "metcoRegnVisitrDDList"],
    "tourism-info-chinese-simplified": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                                        "detailImage2", "detailInfo2", "locationBasedList2",
                                        "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-info-chinese-traditional": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                                         "detailImage2", "detailInfo2", "locationBasedList2",
                                         "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-info-english": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                             "detailImage2", "detailInfo2", "locationBasedList2",
                             "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-info-french": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                            "detailImage2", "detailInfo2", "locationBasedList2",
                            "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-info-german": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                            "detailImage2", "detailInfo2", "locationBasedList2",
                            "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-info-japanese": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                              "detailImage2", "detailInfo2", "locationBasedList2",
                              "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-info-korean": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                            "detailImage2", "detailInfo2", "locationBasedList2",
                            "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-info-russian": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                             "detailImage2", "detailInfo2", "locationBasedList2",
                             "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-info-spanish": ["areaBasedList2", "areaBasedSyncList2", "detailCommon2",
                             "detailImage2", "detailInfo2", "locationBasedList2",
                             "searchFestival2", "searchKeyword2", "subImageYN"],
    "tourism-jobs": ["empmnInfoDetail", "empmnInfoList", "empmnInfoNo", "labrrNumInfo",
                     "srchRecruitInfoSeq", "syncList", "tursmEmpmnInfoURL"],
    "tourism-photos": ["galPhotographyLocation", "galSearchKeyword", "galWebImageUrl",
                       "galleryDetailList1", "galleryList1", "gallerySearchList1", "gallerySyncDetailList1"],
    "visitor-concentration-forecast": ["tatsCnctrRateList", "tatsCnctrRatedList"],
    "wellness-tourism": ["areaBasedList", "detailCommon", "detailImage", "detailInfo", "lDongListYn",
                         "locationBasedList", "orgImage", "searchKeyword", "thumbImage", "wellnessTursmSyncList"],
}


def call_api(service_key: str, service: str, operation: str, extra_params: dict) -> dict:
    params = {
        "serviceKey": service_key,
        "MobileOS": "ETC",
        "MobileApp": "TourismServiceLab",
        "_type": "json",
        **extra_params,
    }
    query = urllib.parse.urlencode(params)
    url = f"{BASE_URL}/{service}/{operation}?{query}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            raw = resp.read().decode("utf-8")
            return {"status": resp.status, "url": url, "body": json.loads(raw)}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"status": e.code, "url": url, "error": body}
    except Exception as e:
        return {"status": 0, "url": url, "error": str(e)}


def collect(service_key: str, target_api: str | None = None):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    errors = []
    stats = {"ok": 0, "error": 0, "skipped": 0}
    timestamp = datetime.utcnow().isoformat()

    apis_to_run = [target_api] if target_api else list(API_MAP.keys())

    for api_id in apis_to_run:
        if api_id not in API_MAP:
            print(f"[SKIP] Unknown api: {api_id}")
            stats["skipped"] += 1
            continue

        cfg = API_MAP[api_id]
        ops = OPERATIONS.get(api_id, [])
        api_dir = OUTPUT_DIR / api_id
        api_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n[{api_id}] service={cfg['service']} ops={len(ops)}")

        for op in ops:
            out_path = api_dir / f"{op}.json"
            result = call_api(service_key, cfg["service"], op, cfg["params"])

            if result.get("status") == 200 and "body" in result:
                with open(out_path, "w", encoding="utf-8") as f:
                    json.dump(result["body"], f, ensure_ascii=False, indent=2)
                print(f"  ✓ {op}")
                stats["ok"] += 1
            else:
                err_entry = {
                    "api_id": api_id,
                    "operation": op,
                    "service": cfg["service"],
                    "status": result.get("status"),
                    "url": result.get("url", ""),
                    "error": result.get("error", ""),
                    "timestamp": timestamp,
                }
                errors.append(err_entry)
                print(f"  ✗ {op} [{result.get('status')}] {result.get('error','')[:80]}")
                stats["error"] += 1

            time.sleep(0.3)  # rate limit

    # errors.log 저장
    with open(ERRORS_LOG, "w", encoding="utf-8") as f:
        f.write(f"# errors.log — generated {timestamp}\n\n")
        for e in errors:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    print(f"\n=== 완료: ok={stats['ok']}, error={stats['error']}, skipped={stats['skipped']} ===")
    return stats


def build_readme(stats: dict):
    lines = [
        "# docs/data-samples",
        "",
        f"> 생성일: {datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}  ",
        f"> ok={stats.get('ok',0)}, error={stats.get('error',0)}",
        "",
        "한국관광공사 OpenAPI 27종 샘플 응답 JSON.  ",
        "각 디렉토리 = `api-id/`, 파일 = `{operation}.json`.",
        "",
        "## API 목록",
        "",
        "| api-id | 서비스명 | 오퍼레이션 수 |",
        "|--------|----------|-------------|",
    ]
    for api_id, cfg in API_MAP.items():
        ops_count = len(OPERATIONS.get(api_id, []))
        lines.append(f"| {api_id} | {cfg['service']} | {ops_count} |")

    lines += [
        "",
        "## 오류 내역",
        "",
        "오류 발생 시 `errors.log` 참고.",
    ]

    readme_path = OUTPUT_DIR / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"README 생성: {readme_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="한국관광공사 OpenAPI 샘플데이터 수집")
    parser.add_argument("--service-key", required=True, help="공공데이터포털 ServiceKey")
    parser.add_argument("--api", default=None, help="특정 API만 수집 (예: gocamping)")
    args = parser.parse_args()

    stats = collect(args.service_key, args.api)
    build_readme(stats)
