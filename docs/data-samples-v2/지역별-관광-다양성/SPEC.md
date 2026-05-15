# 한국관광공사_지역별 관광 다양성 — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/지역별-관광-다양성/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_지역별 관광 다양성 |
| 카탈로그 ID | uddi:AreaTarDivService |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/AreaTarDivService` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: baseYm(YYYYMM) 기준연월 필수. touDivIxCd 코드로 지수 종류 선택.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `areaExpDivList` | `/areaExpDivList` | 지역별 체험관광 다양성 지수 목록 조회 | baseYm(YYYYMM) | ✅ |
| `areaIntlDivList` | `/areaIntlDivList` | 지역별 국제관광 다양성 지수 목록 조회 | baseYm(YYYYMM) | ✅ |
| `areaTouDivList` | `/areaTouDivList` | 지역별 관광다양성 지수 목록 조회 | baseYm(YYYYMM), areaCd, touDivIxCd | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `areaExpDivList`

**용도**: 지역별 체험관광 다양성 지수 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/AreaTarDivService/areaExpDivList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&baseYm=202509&areaCd=11&signguCd=11530&expDivIxCd=3201
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
| baseYm | - | 필수 | string | - | YYYYMM |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `baseYm` | 기준연월 | number | 202509 | - |
| `areaCd` | 지역코드 | code | 11 | - |
| `areaNm` | 지역명 | string | 서울특별시 | - |
| `signguCd` | 시군구코드 | code | 11530 | - |
| `signguNm` | 시군구명 | string | 구로구 | - |
| `expDivIxCd` | expDivIxCd | code | 3201 | - |
| `expDivIxNm` | expDivIxNm | string | 10대 소비액 | - |
| `expDivIxVal` | expDivIxVal | number | 73.62 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"baseYm": "202509", "areaCd": "11", "areaNm": "서울특별시", "signguCd": "11530", "signguNm": "구로구", "expDivIxCd": "3201", "expDivIxNm": "10대 소비액", "expDivIxVal": "73.62"}
```

**TripCraft 활용 포인트**: TripCraft 지역별 체험관광 다양성 지수 목록 조회 기능에 활용.

---

### 3.2 `areaIntlDivList`

**용도**: 지역별 국제관광 다양성 지수 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/AreaTarDivService/areaIntlDivList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&baseYm=202509&areaCd=11&signguCd=11530&intlDivIxCd=3301
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
| baseYm | - | 필수 | string | - | YYYYMM |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `baseYm` | 기준연월 | number | 202509 | - |
| `areaCd` | 지역코드 | code | 11 | - |
| `areaNm` | 지역명 | string | 서울특별시 | - |
| `signguCd` | 시군구코드 | code | 11530 | - |
| `signguNm` | 시군구명 | string | 구로구 | - |
| `intlDivIxCd` | intlDivIxCd | code | 3301 | - |
| `intlDivIxNm` | intlDivIxNm | string | 외국인 소비액 | - |
| `intlDivIxVal` | intlDivIxVal | number | 75.29 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"baseYm": "202509", "areaCd": "11", "areaNm": "서울특별시", "signguCd": "11530", "signguNm": "구로구", "intlDivIxCd": "3301", "intlDivIxNm": "외국인 소비액", "intlDivIxVal": "75.29"}
```

**TripCraft 활용 포인트**: TripCraft 지역별 국제관광 다양성 지수 목록 조회 기능에 활용.

---

### 3.3 `areaTouDivList`

**용도**: 지역별 관광다양성 지수 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/AreaTarDivService/areaTouDivList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&baseYm=202509&areaCd=11&signguCd=11530&touDivIxCd=3103
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
| baseYm | - | 필수 | string | - | YYYYMM |
| areaCd | - | 필수 | string | - | - |
| touDivIxCd | - | 필수 | string | - | - |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `baseYm` | 기준연월 | number | 202509 | - |
| `areaCd` | 지역코드 | code | 11 | - |
| `areaNm` | 지역명 | string | 서울특별시 | - |
| `signguCd` | 시군구코드 | code | 11530 | - |
| `signguNm` | 시군구명 | string | 구로구 | - |
| `touDivIxCd` | 관광다양성지수코드 | code | 3103 | - |
| `touDivIxNm` | 관광다양성지수명 | string | 30대 방문객수 | - |
| `touDivIxVal` | 관광다양성지수값 | number | 96.46 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"baseYm": "202509", "areaCd": "11", "areaNm": "서울특별시", "signguCd": "11530", "signguNm": "구로구", "touDivIxCd": "3103", "touDivIxNm": "30대 방문객수", "touDivIxVal": "96.46"}
```

**TripCraft 활용 포인트**: 지역 관광다양성 지수. 여행지 다양성 점수 표시 및 추천 알고리즘.

---

## 5. 코드 카탈로그

### 관광다양성지수 코드 (touDivIxCd)

| 코드 | 지수명 |
|------|--------|
| 3101 | 10대 방문객수 |
| 3102 | 20대 방문객수 |
| 3103 | 30대 방문객수 |
| 3104 | 40대 방문객수 |
| 3105 | 50대 방문객수 |
| 3106 | 60대 이상 방문객수 |

