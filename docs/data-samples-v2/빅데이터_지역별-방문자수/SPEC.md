# 한국관광공사_빅데이터_지역별 방문자수_GW — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/빅데이터_지역별-방문자수/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_빅데이터_지역별 방문자수_GW |
| 카탈로그 ID | uddi:DataLabService |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/DataLabService` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: startYmd/endYmd(YYYYMMDD) 날짜 범위 필수. 현지인/외지인/외국인 구분 데이터.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `locgoRegnVisitrDDList` | `/locgoRegnVisitrDDList` | 기초지자체(시군구)별 일별 방문자수 조회 | startYmd(YYYYMMDD), endYmd(YYYYMMDD) | ✅ |
| `metcoRegnVisitrDDList` | `/metcoRegnVisitrDDList` | 광역시도별 일별 방문자수 조회 | startYmd(YYYYMMDD), endYmd(YYYYMMDD) | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `locgoRegnVisitrDDList`

**용도**: 기초지자체(시군구)별 일별 방문자수 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/DataLabService/locgoRegnVisitrDDList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&startYmd=20210513&endYmd=20210513
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
| startYmd | - | 필수 | string | - | YYYYMMDD |
| endYmd | - | 필수 | string | - | YYYYMMDD |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `signguCode` | 시군구 코드 | code | 11110 | - |
| `signguNm` | 시군구명 | string | 종로구 | - |
| `daywkDivCd` | 요일구분코드 | code | 4 | - |
| `daywkDivNm` | 요일구분명 | string | 목요일 | - |
| `touDivCd` | 관광객구분코드 | code | 1 | - |
| `touDivNm` | 관광객구분명 | string | 현지인(a) | - |
| `touNum` | 방문자수 | number | 176473.5 | - |
| `baseYmd` | 기준일자 | datetime | 20210513 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"signguCode": "11110", "signguNm": "종로구", "daywkDivCd": "4", "daywkDivNm": "목요일", "touDivCd": "1", "touDivNm": "현지인(a)", "touNum": "176473.5", "baseYmd": "20210513"}
{"signguCode": "11110", "signguNm": "종로구", "daywkDivCd": "4", "daywkDivNm": "목요일", "touDivCd": "2", "touDivNm": "외지인(b)", "touNum": "317425.5", "baseYmd": "20210513"}
{"signguCode": "11110", "signguNm": "종로구", "daywkDivCd": "4", "daywkDivNm": "목요일", "touDivCd": "3", "touDivNm": "외국인(c)", "touNum": "153.60999999999996", "baseYmd": "20210513"}
```

**TripCraft 활용 포인트**: 시군구별 일별 방문자수 집계. 혼잡도 예측 및 여행 최적 시기 추천에 활용.

---

### 3.2 `metcoRegnVisitrDDList`

**용도**: 광역시도별 일별 방문자수 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/DataLabService/metcoRegnVisitrDDList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&startYmd=20210513&endYmd=20210513
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
| startYmd | - | 필수 | string | - | YYYYMMDD |
| endYmd | - | 필수 | string | - | YYYYMMDD |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `areaCode` | areaCode | code | 11 | - |
| `areaNm` | 지역명 | string | 서울특별시 | - |
| `daywkDivCd` | 요일구분코드 | code | 4 | - |
| `daywkDivNm` | 요일구분명 | string | 목요일 | - |
| `touDivCd` | 관광객구분코드 | code | 1 | - |
| `touDivNm` | 관광객구분명 | string | 현지인(a) | - |
| `touNum` | 방문자수 | number | 4828435.5 | - |
| `baseYmd` | 기준일자 | datetime | 20210513 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"areaCode": "11", "areaNm": "서울특별시", "daywkDivCd": "4", "daywkDivNm": "목요일", "touDivCd": "1", "touDivNm": "현지인(a)", "touNum": "4828435.5", "baseYmd": "20210513"}
{"areaCode": "11", "areaNm": "서울특별시", "daywkDivCd": "4", "daywkDivNm": "목요일", "touDivCd": "2", "touDivNm": "외지인(b)", "touNum": "1255828.0", "baseYmd": "20210513"}
{"areaCode": "11", "areaNm": "서울특별시", "daywkDivCd": "4", "daywkDivNm": "목요일", "touDivCd": "3", "touDivNm": "외국인(c)", "touNum": "3994.5399999999995", "baseYmd": "20210513"}
```

**TripCraft 활용 포인트**: 광역시도별 방문자 트렌드. 지역 인기도 분석 및 여행 추천 알고리즘 입력.

---

## 5. 코드 카탈로그

### 관광객 구분 코드 (touDivCd)

| 코드 | 구분명 |
|------|--------|
| 1 | 현지인(a) |
| 2 | 외지인(b) |
| 3 | 외국인(c) |

