# 한국관광공사_지역별 관광 자원 수요 — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/지역별-관광-자원-수요/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_지역별 관광 자원 수요 |
| 카탈로그 ID | uddi:AreaTarResDemService |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/AreaTarResDemService` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: baseYm(YYYYMM) 기준연월 필수. 문화자원/관광서비스 수요 2종 오퍼레이션.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `areaCulResDemList` | `/areaCulResDemList` | 지역별 문화관광자원 수요 목록 조회 | baseYm(YYYYMM) | ✅ |
| `areaTarSvcDemList` | `/areaTarSvcDemList` | 지역별 관광서비스 수요 목록 조회 | baseYm(YYYYMM) | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `areaCulResDemList`

**용도**: 지역별 문화관광자원 수요 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/AreaTarResDemService/areaCulResDemList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&baseYm=202509&areaCd=11&signguCd=11530&culResDemIxCd=1201
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
| `culResDemIxCd` | culResDemIxCd | code | 1201 | - |
| `culResDemIxNm` | culResDemIxNm | string | 내비게이션 문화관광유형 검색량 | - |
| `culResDemIxVal` | culResDemIxVal | number | 75.75 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"baseYm": "202509", "areaCd": "11", "areaNm": "서울특별시", "signguCd": "11530", "signguNm": "구로구", "culResDemIxCd": "1201", "culResDemIxNm": "내비게이션 문화관광유형 검색량", "culResDemIxVal": "75.75"}
```

**TripCraft 활용 포인트**: 지역 문화자원 수요. 문화콘텐츠 기반 여행지 추천.

---

### 3.2 `areaTarSvcDemList`

**용도**: 지역별 관광서비스 수요 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/AreaTarResDemService/areaTarSvcDemList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&baseYm=202509&areaCd=11&signguCd=11530&tarSvcDemIxCd=1101
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
| `tarSvcDemIxCd` | tarSvcDemIxCd | code | 1101 | - |
| `tarSvcDemIxNm` | tarSvcDemIxNm | code | 레포츠여행유형 SNS언급량 | - |
| `tarSvcDemIxVal` | tarSvcDemIxVal | code | 77.44 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"baseYm": "202509", "areaCd": "11", "areaNm": "서울특별시", "signguCd": "11530", "signguNm": "구로구", "tarSvcDemIxCd": "1101", "tarSvcDemIxNm": "레포츠여행유형 SNS언급량", "tarSvcDemIxVal": "77.44"}
```

**TripCraft 활용 포인트**: TripCraft 지역별 관광서비스 수요 목록 조회 기능에 활용.

---

## 5. 코드 카탈로그

