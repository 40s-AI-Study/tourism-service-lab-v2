#!/usr/bin/env python3
"""
KTO OpenAPI Sample Data Fetcher - v2
Fetches real sample data from all 27 Korea Tourism Organization OpenAPI endpoints.

Service paths extracted from actual docx manuals in _raw/extracted/.
"""

import json
import os
import subprocess
import time
import sys
from datetime import datetime, timezone
from pathlib import Path

# Configuration
SERVICE_KEY = "e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e"
BASE_URL = "http://apis.data.go.kr/B551011"
COMMON_PARAMS = {
    "serviceKey": SERVICE_KEY,
    "numOfRows": "5",
    "pageNo": "1",
    "MobileOS": "ETC",
    "MobileApp": "TripCraftKorea",
    "_type": "json",
}
FETCH_DATE = "2026-05-15"
OUTPUT_DIR = Path("/Users/sklee01/tourism-service-lab-v2/docs/data-samples")
MAX_FILE_BYTES = 50 * 1024  # 50KB

# ------------------------------------------------------------------
# API configuration: service paths extracted from docx manuals
# ------------------------------------------------------------------
API_CONFIG = [
    {
        "id": "area-tourism-resource-demand",
        "title": "한국관광공사_지역별 관광 자원 수요",
        "service": "AreaTarResDemService",
        "operations": [
            {"name": "areaCulResDemList", "extra": {"areaCd": "11", "baseYm": "202412"}},
            {"name": "areaTarSvcDemList", "extra": {"areaCd": "11", "baseYm": "202412"}},
        ],
    },
    {
        "id": "area-tourism-demand-density",
        "title": "한국관광공사_지역별 관광 수요 강도",
        "service": "AreaTarDemDsService",
        "operations": [
            {"name": "areaTarExpDsList", "extra": {"areaCd": "11", "baseYm": "202412"}},
            {"name": "areaTarSjrnDsList", "extra": {"areaCd": "11", "baseYm": "202412"}},
        ],
    },
    {
        "id": "area-tourism-diversity",
        "title": "한국관광공사_지역별 관광 다양성",
        "service": "AreaTarDivService",
        "operations": [
            {"name": "areaExpDivList", "extra": {"areaCd": "11", "baseYm": "202412"}},
            {"name": "areaIntlDivList", "extra": {"areaCd": "11", "baseYm": "202412"}},
            {"name": "areaTouDivList", "extra": {"areaCd": "11", "baseYm": "202412"}},
        ],
    },
    {
        "id": "photo-contest-winners",
        "title": "한국관광공사_관광공모전(사진) 수상작 정보",
        "service": "PhokoAwrdService",
        "operations": [
            {"name": "phokoAwrdList", "extra": {}},
            {"name": "phokoAwrdSyncList", "extra": {}},
            {"name": "koKeyword", "extra": {}},
            {"name": "enKeyword", "extra": {}},
            {"name": "orgImage", "extra": {"contentId": "1"}},
            {"name": "thumbImage", "extra": {"contentId": "1"}},
        ],
    },
    {
        "id": "wellness-tourism",
        "title": "한국관광공사_웰니스관광정보",
        "service": "WellnessTursmService",
        "operations": [
            {"name": "areaBasedList", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword", "extra": {"keyword": "서울"}},
            {"name": "detailCommon", "extra": {"contentId": "125431"}},
            {"name": "detailInfo", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage", "extra": {"contentId": "125431"}},
            {"name": "lDongListYn", "extra": {"areaCode": "1"}},
            {"name": "orgImage", "extra": {"contentId": "125431"}},
            {"name": "thumbImage", "extra": {"contentId": "125431"}},
            {"name": "wellnessTursmSyncList", "extra": {}},
        ],
    },
    {
        "id": "medical-tourism",
        "title": "한국관광공사_의료관광정보",
        "service": "MdclTursmService",
        "operations": [
            {"name": "areaBasedList", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword", "extra": {"keyword": "서울"}},
            {"name": "detailCommon", "extra": {"contentId": "125431"}},
            {"name": "lDongListYn", "extra": {"areaCode": "1"}},
            {"name": "mdclTursmDivInfo", "extra": {}},
            {"name": "mdclTursmSyncList", "extra": {}},
        ],
    },
    {
        "id": "pet-friendly-travel",
        "title": "한국관광공사_반려동물_동반여행_서비스",
        "service": "KorPetTourService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "etcAcmpyInfo", "extra": {"contentId": "125431"}},
            {"name": "lDongListYn", "extra": {"areaCode": "1"}},
            {"name": "petTourSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "related-attractions",
        "title": "한국관광공사_관광지별 연관 관광지 정보",
        "service": "TarRlteTarService1",
        "operations": [
            {"name": "areaBasedList1", "extra": {"areaCode": "1"}},
            {"name": "searchKeyword", "extra": {"keyword": "서울"}},
            {"name": "searchKeyword1", "extra": {"keyword": "서울"}},
        ],
    },
    {
        "id": "central-attractions-by-municipality",
        "title": "한국관광공사_기초지자체 중심 관광지 정보",
        "service": "LocgoHubTarService1",
        "operations": [
            {"name": "areaBasedList", "extra": {"areaCode": "1"}},
            {"name": "areaBasedList1", "extra": {"areaCode": "1"}},
        ],
    },
    {
        "id": "visitor-concentration-forecast",
        "title": "한국관광공사_관광지 집중률 방문자 추이 예측 정보",
        "service": "TatsCnctrRateService",
        "operations": [
            {"name": "tatsCnctrRateList", "extra": {"areaCode": "1"}},
            {"name": "tatsCnctrRatedList", "extra": {"areaCode": "1"}},
        ],
    },
    {
        "id": "tourism-jobs",
        "title": "한국관광공사_관광인_채용정보_서비스",
        "service": "tursmService",
        "operations": [
            {"name": "empmnInfoList", "extra": {}},
            {"name": "empmnInfoDetail", "extra": {"recruitInfoSeq": "1"}},
            {"name": "empmnInfoNo", "extra": {}},
            {"name": "labrrNumInfo", "extra": {}},
            {"name": "srchRecruitInfoSeq", "extra": {"keyword": "관광"}},
            {"name": "syncList", "extra": {}},
            {"name": "tursmEmpmnInfoURL", "extra": {}},
        ],
    },
    {
        "id": "durunubi-trails",
        "title": "한국관광공사_두루누비 정보 서비스",
        "service": "Durunubi",
        "operations": [
            {"name": "routeList", "extra": {}},
            {"name": "courseList", "extra": {}},
            {"name": "crsTourInfo", "extra": {"courseId": "1"}},
        ],
    },
    {
        "id": "tourism-big-data",
        "title": "한국관광공사_관광빅데이터 정보서비스",
        "service": "DataLabService",
        "operations": [
            {"name": "locgoRegnVisitrDDList", "extra": {"areaCode": "1", "baseYmd": "20241201"}},
            {"name": "metcoRegnVisitrDDList", "extra": {"areaCode": "1", "baseYmd": "20241201"}},
        ],
    },
    {
        "id": "audio-guide",
        "title": "한국관광공사_관광지 오디오 가이드정보",
        "service": "Odii",
        "operations": [
            {"name": "themeBasedList", "extra": {}},
            {"name": "themeLocationBasedList", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "themeSearchList", "extra": {"keyword": "경복궁"}},
            {"name": "themeBasedSyncList", "extra": {}},
            {"name": "themeCategory", "extra": {}},
            {"name": "storyBasedList", "extra": {"areaCode": "1"}},
            {"name": "storyLocationBasedList", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "storySearchList", "extra": {"keyword": "경복궁"}},
            {"name": "storyBasedSyncList", "extra": {}},
        ],
    },
    {
        "id": "gocamping",
        "title": "한국관광공사_고캠핑 정보 조회서비스",
        "service": "GoCamping",
        "operations": [
            {"name": "basedList", "extra": {}},
            {"name": "locationBasedList", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "20000"}},
            {"name": "searchList", "extra": {"keyword": "캠핑"}},
            {"name": "imageList", "extra": {}},
            {"name": "basedSyncList", "extra": {}},
        ],
    },
    {
        "id": "tourism-photos",
        "title": "한국관광공사_관광사진 정보",
        "service": "PhotoGalleryService1",
        "operations": [
            {"name": "galleryList1", "extra": {"areaCode": "1"}},
            {"name": "gallerySearchList1", "extra": {"keyword": "서울"}},
            {"name": "galSearchKeyword", "extra": {"keyword": "서울"}},
            {"name": "galPhotographyLocation", "extra": {}},
            {"name": "gallerySyncDetailList1", "extra": {}},
        ],
    },
    {
        "id": "eco-tourism",
        "title": "한국관광공사_생태 관광 정보",
        "service": "GreenTourService1",
        "operations": [
            {"name": "areaBasedList", "extra": {}},
            {"name": "areaBasedList1", "extra": {"areaCode": "1"}},
            {"name": "areaBasedSyncList1", "extra": {}},
        ],
    },
    {
        "id": "barrier-free-travel",
        "title": "한국관광공사_무장애 여행 정보",
        "service": "KorWithService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-russian",
        "title": "한국관광공사_노어 관광정보서비스",
        "service": "RusService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-spanish",
        "title": "한국관광공사_서어 관광정보서비스",
        "service": "SpnService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-french",
        "title": "한국관광공사_불어 관광정보서비스",
        "service": "FreService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-german",
        "title": "한국관광공사_독어 관광정보서비스",
        "service": "GerService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-japanese",
        "title": "한국관광공사_일문 관광정보서비스",
        "service": "JpnService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-chinese-traditional",
        "title": "한국관광공사_중문 번체 관광정보서비스",
        "service": "ChtService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-chinese-simplified",
        "title": "한국관광공사_중문 간체 관광정보서비스",
        "service": "ChsService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "서울"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-english",
        "title": "한국관광공사_영문 관광정보서비스",
        "service": "EngService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "Seoul"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
    {
        "id": "tourism-info-korean",
        "title": "한국관광공사_국문 관광정보 서비스",
        "service": "KorService2",
        "operations": [
            {"name": "areaBasedList2", "extra": {"areaCode": "1"}},
            {"name": "locationBasedList2", "extra": {"mapX": "126.977", "mapY": "37.5796", "radius": "2000"}},
            {"name": "searchKeyword2", "extra": {"keyword": "경복궁"}},
            {"name": "searchFestival2", "extra": {"areaCode": "1", "eventStartDate": "20241201"}},
            {"name": "detailCommon2", "extra": {"contentId": "125431", "contentTypeId": "12", "defaultYN": "Y", "firstImageYN": "Y", "areacodeYN": "Y", "catcodeYN": "Y", "addrinfoYN": "Y", "mapinfoYN": "Y", "overviewYN": "Y"}},
            {"name": "detailInfo2", "extra": {"contentId": "125431", "contentTypeId": "12"}},
            {"name": "detailImage2", "extra": {"contentId": "125431", "imageYN": "Y", "subImageYN": "Y"}},
            {"name": "areaBasedSyncList2", "extra": {}},
            {"name": "subImageYN", "extra": {"contentId": "125431"}},
        ],
    },
]


def build_url(service: str, operation: str, extra: dict) -> str:
    params = dict(COMMON_PARAMS)
    params.update(extra)
    qs = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{BASE_URL}/{service}/{operation}?{qs}"


def fetch_url(url: str, timeout: int = 15) -> tuple:
    """Return (http_status_int, body_str)."""
    cmd = ["curl", "-sS", "--max-time", str(timeout), "-w", "\n__HTTP__%{http_code}", url]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
        out = result.stdout
        if "__HTTP__" in out:
            body, status = out.rsplit("__HTTP__", 1)
            return int(status.strip()), body.strip()
        return 0, out or result.stderr
    except subprocess.TimeoutExpired:
        return 0, "TIMEOUT"
    except Exception as e:
        return 0, str(e)


def trim_json(data: dict) -> dict:
    """Trim items array to first 5 items."""
    try:
        body = data.get("response", {}).get("body", {})
        items = body.get("items", {})
        if isinstance(items, dict):
            item = items.get("item", [])
            if isinstance(item, list) and len(item) > 5:
                data["response"]["body"]["items"]["item"] = item[:5]
            elif isinstance(item, dict):
                data["response"]["body"]["items"]["item"] = [item]
    except Exception:
        pass
    return data


def fetch_operation(api_id: str, service: str, op_name: str, extra: dict) -> dict:
    url = build_url(service, op_name, extra)
    print(f"  {api_id}/{op_name} ...", flush=True)

    status, body = fetch_url(url)
    result = {
        "api_id": api_id, "operation": op_name, "url": url,
        "http_status": status, "success": False, "error": None, "data": None,
    }

    if status == 200:
        try:
            data = json.loads(body)
            data = trim_json(data)
            result["success"] = True
            result["data"] = data
            # Check API-level result code
            try:
                hdr = data.get("response", {}).get("header", {})
                rc = hdr.get("resultCode", "")
                if rc and rc != "0000":
                    result["api_result_code"] = rc
                    result["api_result_msg"] = hdr.get("resultMsg", "")
            except Exception:
                pass
            return result
        except json.JSONDecodeError:
            if "<?xml" in body or "<OpenAPI_ServiceResponse>" in body:
                result["error"] = f"XML_RESPONSE: {body[:300]}"
            else:
                result["error"] = f"JSON_PARSE_ERROR: {body[:300]}"
    elif status == 403:
        result["error"] = f"HTTP_403_FORBIDDEN: Service key not authorized for {service}"
    elif status == 404:
        result["error"] = f"HTTP_404_NOT_FOUND: {service}/{op_name} endpoint does not exist"
    elif status == 500:
        result["error"] = f"HTTP_500_SERVER_ERROR: {body[:200]}"
    elif status == 0:
        result["error"] = f"NETWORK_ERROR: {body[:200]}"
    else:
        result["error"] = f"HTTP_{status}: {body[:200]}"

    # Retry once on rate limit or timeout
    if status in (429, 0):
        time.sleep(1)
        status2, body2 = fetch_url(url)
        if status2 == 200:
            try:
                data = json.loads(body2)
                data = trim_json(data)
                result["success"] = True
                result["data"] = data
                result["http_status"] = status2
                result["error"] = None
                return result
            except Exception:
                pass
        result["http_status"] = status2
        result["error"] = f"RETRY_HTTP_{status2}: {body2[:200]}"

    return result


def process_api(api: dict) -> dict:
    api_id = api["id"]
    service = api["service"]
    title = api["title"]
    operations = api["operations"]

    print(f"\n[{api_id}] service={service}", flush=True)

    out_dir = OUTPUT_DIR / api_id
    out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    errors = []

    for op in operations:
        op_name = op["name"]
        extra = op.get("extra", {})
        res = fetch_operation(api_id, service, op_name, extra)
        results.append(res)
        time.sleep(0.15)

        if res["success"] and res["data"] is not None:
            json_str = json.dumps(res["data"], ensure_ascii=False, indent=2)
            # Aggressively trim if over 50KB
            if len(json_str.encode("utf-8")) > 50 * 1024:
                try:
                    item = res["data"]["response"]["body"]["items"]["item"]
                    if isinstance(item, list):
                        res["data"]["response"]["body"]["items"]["item"] = item[:3]
                except Exception:
                    pass
                json_str = json.dumps(res["data"], ensure_ascii=False, indent=2)

            out_file = out_dir / f"{op_name}.json"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(json_str)

            tc = 0
            try:
                tc = res["data"]["response"]["body"].get("totalCount", 0)
            except Exception:
                pass
            rc_info = res.get("api_result_code", "0000")
            print(f"    OK  [{op_name}] rc={rc_info} totalCount={tc}", flush=True)
        else:
            errors.append(f"{op_name}: {res['error']}")
            print(f"    FAIL[{op_name}] {res['error'][:80]}", flush=True)

    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    # Categorize failures
    fail_403 = [r for r in failed if "403" in (r.get("error") or "")]
    fail_500 = [r for r in failed if "500" in (r.get("error") or "")]
    fail_404 = [r for r in failed if "404" in (r.get("error") or "")]

    meta = {
        "api_id": api_id,
        "title": title,
        "service": service,
        "base_url": f"{BASE_URL}/{service}",
        "operations_total": len(operations),
        "operations_success": len(successful),
        "operations_failed": len(failed),
        "fail_breakdown": {
            "http_403_forbidden": len(fail_403),
            "http_500_server_error": len(fail_500),
            "http_404_not_found": len(fail_404),
            "other": len(failed) - len(fail_403) - len(fail_500) - len(fail_404),
        },
        "fetch_date": FETCH_DATE,
        "fetch_timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    with open(out_dir / "_meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    if errors:
        with open(out_dir / "errors.log", "w", encoding="utf-8") as f:
            f.write(f"# {title}\n# {FETCH_DATE}\n# Service: {BASE_URL}/{service}\n\n")
            for e in errors:
                f.write(e + "\n")

    return {
        "api_id": api_id,
        "title": title,
        "service": service,
        "operations_total": len(operations),
        "operations_success": len(successful),
        "operations_failed": len(failed),
        "fail_breakdown": meta["fail_breakdown"],
        "failed_operation_names": [r["operation"] for r in failed],
    }


def generate_readme(results: list):
    total_ops = sum(r["operations_total"] for r in results)
    total_ok = sum(r["operations_success"] for r in results)
    total_fail = total_ops - total_ok

    lines = [
        "# 한국관광공사 OpenAPI 샘플 데이터",
        "",
        f"> 페치 일자: {FETCH_DATE} | ServiceKey 기반 직접 호출 (개발계정)",
        "",
        "## 개요",
        "",
        f"- 총 API 수: **{len(results)}**",
        f"- 총 오퍼레이션 수: **{total_ops}**",
        f"- 성공: **{total_ok}**",
        f"- 실패: **{total_fail}**",
        f"- 성공률: **{total_ok/total_ops*100:.1f}%**" if total_ops else "",
        "",
        "> **참고**: 개발계정(Development Key)은 data.go.kr에서 승인된 서비스에 대해서만 사용 가능합니다.",
        "> HTTP 403 = 해당 서비스 미승인, HTTP 500 = 서비스 경로 오류 또는 미승인",
        "",
        "## API 목록",
        "",
        "| API 한글명 | ID | 서비스명 | 오퍼레이션 | 성공 | 실패 | 샘플 파일 |",
        "|---|---|---|:---:|:---:|:---:|---|",
    ]

    for r in results:
        api_id = r["api_id"]
        title = r["title"]
        svc = r["service"]
        total = r["operations_total"]
        success = r["operations_success"]
        failed = r["operations_failed"]

        op_dir = OUTPUT_DIR / api_id
        sample_files = sorted(op_dir.glob("*.json")) if op_dir.exists() else []
        links = " ".join(
            f"[{f.stem}](./{api_id}/{f.name})"
            for f in sample_files if not f.stem.startswith("_")
        )
        if not links:
            links = "_없음_"

        lines.append(f"| {title} | [{api_id}](./{api_id}/) | `{svc}` | {total} | {success} | {failed} | {links} |")

    lines += [
        "",
        "## 실패 원인 분석",
        "",
        "| 오류 유형 | 건수 | 원인 |",
        "|---|:---:|---|",
    ]

    total_403 = sum(r.get("fail_breakdown", {}).get("http_403_forbidden", 0) for r in results)
    total_500 = sum(r.get("fail_breakdown", {}).get("http_500_server_error", 0) for r in results)
    total_404 = sum(r.get("fail_breakdown", {}).get("http_404_not_found", 0) for r in results)

    lines += [
        f"| HTTP 403 Forbidden | {total_403} | 서비스 키 미승인 (해당 API 미신청) |",
        f"| HTTP 500 Server Error | {total_500} | 서비스 경로 오류 또는 키 미승인 |",
        f"| HTTP 404 Not Found | {total_404} | 엔드포인트 없음 |",
        "",
        "## 디렉토리 구조",
        "",
        "```",
        "docs/data-samples/",
        "├── README.md            이 파일",
        "├── _summary.json        머신 리더블 요약",
        "└── {api-id}/",
        "    ├── _meta.json       API 메타정보 + 페치 결과",
        "    ├── {operation}.json 응답 샘플 (성공 시)",
        "    └── errors.log       실패 기록",
        "```",
    ]

    with open(OUTPUT_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"README written: {OUTPUT_DIR / 'README.md'}")


def generate_summary(results: list):
    total_ops = sum(r["operations_total"] for r in results)
    total_ok = sum(r["operations_success"] for r in results)
    summary = {
        "schema_version": "1.0",
        "fetch_date": FETCH_DATE,
        "fetch_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "total_apis": len(results),
        "total_operations": total_ops,
        "total_success": total_ok,
        "total_failed": total_ops - total_ok,
        "success_rate_pct": round(total_ok / total_ops * 100, 1) if total_ops else 0,
        "apis": results,
    }
    with open(OUTPUT_DIR / "_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"Summary written: {OUTPUT_DIR / '_summary.json'}")


def main():
    print("KTO OpenAPI Sample Fetcher v2")
    print(f"Output: {OUTPUT_DIR}")
    print(f"APIs: {len(API_CONFIG)}")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_results = []
    for api in API_CONFIG:
        res = process_api(api)
        all_results.append(res)

    print("\n" + "=" * 60)
    generate_readme(all_results)
    generate_summary(all_results)

    total_ops = sum(r["operations_total"] for r in all_results)
    total_ok = sum(r["operations_success"] for r in all_results)
    json_files = len([f for f in OUTPUT_DIR.rglob("*.json")
                      if not f.name.startswith("_") and f.parent != OUTPUT_DIR])

    print(f"\nDONE: {total_ok}/{total_ops} operations successful")
    print(f"JSON sample files: {json_files}")


if __name__ == "__main__":
    main()
