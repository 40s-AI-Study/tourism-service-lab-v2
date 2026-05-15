#!/usr/bin/env python3
"""Rescan docs/data-samples-v2 and rebuild _summary.json + README counts."""
import json
from pathlib import Path

ROOT = Path("/Users/sklee01/tourism-service-lab-v2")
SAMPLES = ROOT / "docs/data-samples-v2"

# Map slug -> base/title
META_BY_SLUG = {
    "고캠핑-정보-조회서비스": ("[승인] 한국관광공사_고캠핑 정보 조회서비스_GW", "https://apis.data.go.kr/B551011/GoCamping"),
    "관광사진-정보": ("[승인] 한국관광공사_관광사진 정보_GW", "https://apis.data.go.kr/B551011/PhotoGalleryService1"),
    "관광지-오디오-가이드정보": ("[승인] 한국관광공사_관광지 오디오 가이드정보_GW", "https://apis.data.go.kr/B551011/Odii"),
    "관광지-집중률-방문자-추이-예측-정보": ("[승인] 한국관광공사_관광지 집중률 방문자 추이 예측 정보", "https://apis.data.go.kr/B551011/TatsCnctrRateService"),
    "국문-관광정보-서비스": ("[승인] 한국관광공사_국문 관광정보 서비스_GW", "https://apis.data.go.kr/B551011/KorService2"),
    "기초지자체-중심-관광지-정보": ("[승인] 한국관광공사_기초지자체 중심 관광지 정보", "https://apis.data.go.kr/B551011/LocgoHubTarService1"),
    "두루누비-정보-서비스": ("[승인] 한국관광공사_두루누비 정보 서비스_GW", "https://apis.data.go.kr/B551011/DurunubiService"),
    "무장애-여행-정보": ("[승인] 한국관광공사_무장애 여행 정보_GW", "https://apis.data.go.kr/B551011/KorWithService2"),
    "반려동물_동반여행_서비스": ("[승인] 한국관광공사_반려동물_동반여행_서비스_GW", "https://apis.data.go.kr/B551011/KorPetTourService"),
    "빅데이터_지역별-방문자수": ("[승인] 한국관광공사_빅데이터_지역별 방문자수_GW", "https://apis.data.go.kr/B551011/DataLabService"),
    "생태-관광-정보": ("[승인] 한국관광공사_생태 관광 정보_GW", "https://apis.data.go.kr/B551011/EcoTourService"),
    "웰니스관광정보": ("[승인] 한국관광공사_웰니스관광정보", "https://apis.data.go.kr/B551011/WellnessTourService"),
    "의료관광정보": ("[승인] 한국관광공사_의료관광정보", "https://apis.data.go.kr/B551011/MdclTourService"),
    "일문-관광정보서비스": ("[승인] 한국관광공사_일문 관광정보서비스_GW", "https://apis.data.go.kr/B551011/JpnService2"),
    "지역별-관광-다양성": ("[승인] 한국관광공사_지역별 관광 다양성", "https://apis.data.go.kr/B551011/AreaTarDivService"),
    "지역별-관광-수요-강도": ("[승인] 한국관광공사_지역별 관광 수요 강도", "https://apis.data.go.kr/B551011/AreaTarDemDsService"),
    "지역별-관광-자원-수요": ("[승인] 한국관광공사_지역별 관광 자원 수요", "https://apis.data.go.kr/B551011/AreaTarResDemService"),
}


def has_items(jpath):
    try:
        j = json.loads(jpath.read_text(encoding="utf-8"))
    except Exception:
        return False, 0, "READ_ERR"
    # Top-level wrapped { ok, json: {...response...}, items_count }
    if "items_count" in j and j["items_count"] > 0:
        return True, j.get("totalCount", 0), "OK"
    payload = j.get("json", j)
    if isinstance(payload, dict):
        resp = payload.get("response", {})
        body = resp.get("body") if isinstance(resp, dict) else None
        if isinstance(body, dict):
            its = body.get("items")
            total = body.get("totalCount", 0) or 0
            if isinstance(its, dict) and isinstance(its.get("item"), list):
                return (len(its["item"]) > 0, total, "OK")
            if isinstance(its, list) and len(its) > 0:
                return True, total, "OK"
    return False, 0, "EMPTY"


summary = []
for slug, (title, base) in META_BY_SLUG.items():
    d = SAMPLES / slug
    if not d.exists(): continue
    samples = []
    for f in sorted(d.glob("*.json")):
        if f.name.startswith("_"): continue
        op = f.stem
        ok, total, status = has_items(f)
        samples.append({"op": op, "items": 5 if ok else 0, "totalCount": total, "status": status})
    summary.append({
        "slug": slug, "title": title, "base": base,
        "ops_total": len(samples),
        "ops_with_data": sum(1 for s in samples if s["items"] > 0),
        "samples": samples,
    })

(SAMPLES/"_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
total_ops = sum(s["ops_total"] for s in summary)
total_with = sum(s["ops_with_data"] for s in summary)
print(f"Total APIs: {len(summary)}  total_ops: {total_ops}  with_data: {total_with}")
for s in summary:
    print(f"  {s['slug']:<40} {s['ops_with_data']}/{s['ops_total']}")
