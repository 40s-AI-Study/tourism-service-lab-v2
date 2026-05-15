# 한국관광공사_기초지자체 중심 관광지 정보 — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/기초지자체-중심-관광지-정보/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_기초지자체 중심 관광지 정보 |
| 카탈로그 ID | uddi:LocgoHubTarService1 |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/LocgoHubTarService1` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: 시군구 단위 대표 관광지 정보에 특화.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `areaBasedList1` | `/areaBasedList1` | 생태관광 지역기반 목록 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `areaBasedList1`

**용도**: 생태관광 지역기반 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/LocgoHubTarService1/areaBasedList1?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&baseYm=202509&areaCd=51&signguCd=51130
```

**요청 파라미터**:

| 파라미터명 | 한글명 | 필수/옵션 | 타입 | 샘플 값 | 설명 |
|-----------|--------|---------|------|--------|------|
| serviceKey | 인증키 | 필수 | string | ${SERVICE_KEY} | data.go.kr 발급 서비스키 |
| MobileOS | OS 구분 | 필수 | string | ETC | ETC/AND/IOS/WIN |
| MobileApp | 앱 명칭 | 필수 | string | TripCraftKorea | 앱 이름 |
| _type | 응답 형식 | 필수 | string | json | json/xml |
| numOfRows | 페이지당 결과수 | 옵션 | number | 5 | 기본값 10 |
| pageNo | 페이지 번호 | 옵션 | number | 1 | 기본값 1 |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `baseYm` | 기준연월 | number | 202509 | - |
| `mapX` | 경도 | coord | 127.813714745281000 | - |
| `mapY` | 위도 | coord | 37.438066364365100 | - |
| `areaCd` | 지역코드 | code | 51 | - |
| `areaNm` | 지역명 | string | 강원특별자치도 | - |
| `signguCd` | 시군구코드 | code | 51130 | - |
| `signguNm` | 시군구명 | string | 원주시 | - |
| `hubTatsCd` | hubTatsCd | code | 0b37553854f416b46ded92602ff89444 | - |
| `hubTatsNm` | hubTatsNm | string | 오크밸리CC | - |
| `hubCtgryLclsNm` | hubCtgryLclsNm | string | 관광지 | - |
| `hubCtgryMclsNm` | hubCtgryMclsNm | string | 레저스포츠 | - |
| `hubRank` | hubRank | number | 1 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"baseYm": "202509", "mapX": "127.813714745281000", "mapY": "37.438066364365100", "areaCd": "51", "areaNm": "강원특별자치도", "signguCd": "51130", "signguNm": "원주시", "hubTatsCd": "0b37553854f416b46ded92602ff89444", "hubTatsNm": "오크밸리CC", "hubCtgryLclsNm": "관광지", "hubCtgryMclsNm": "레저스포츠", "hubRank": "1"}
{"baseYm": "202509", "mapX": "127.819130966451000", "mapY": "37.434205734466800", "areaCd": "51", "areaNm": "강원특별자치도", "signguCd": "51130", "signguNm": "원주시", "hubTatsCd": "3816e6ec41e2c0ccbb821954d69a1e95", "hubTatsNm": "오크밸리리조트/빌리지센터", "hubCtgryLclsNm": "관광지", "hubCtgryMclsNm": "문화관광", "hubRank": "2"}
{"baseYm": "202509", "mapX": "127.822991893812000", "mapY": "37.418901966829300", "areaCd": "51", "areaNm": "강원특별자치도", "signguCd": "51130", "signguNm": "원주시", "hubTatsCd": "0bfeca2105aa7bf8d83e4622e5da19ec", "hubTatsNm": "뮤지엄산", "hubCtgryLclsNm": "관광지", "hubCtgryMclsNm": "문화관광", "hubRank": "3"}
```

**TripCraft 활용 포인트**: 시군구 핵심 관광지 목록. 지역 대표 관광지 추천 카드.

---

## 5. 코드 카탈로그

### 지역코드 (areacode)

| 코드 | 지역명 |
|------|--------|
| 1 | 서울 |
| 2 | 인천 |
| 3 | 대전 |
| 4 | 대구 |
| 5 | 광주 |
| 6 | 부산 |
| 7 | 울산 |
| 8 | 세종특별자치시 |
| 31 | 경기도 |
| 32 | 강원특별자치도 |
| 33 | 충청북도 |
| 34 | 충청남도 |
| 35 | 경상북도 |
| 36 | 경상남도 |
| 37 | 전라북도 |
| 38 | 전라남도 |
| 39 | 제주도 |

