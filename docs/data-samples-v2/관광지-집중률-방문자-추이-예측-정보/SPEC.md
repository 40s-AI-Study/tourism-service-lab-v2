# 한국관광공사_관광지 집중률 방문자 추이 예측 정보 — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/관광지-집중률-방문자-추이-예측-정보/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_관광지 집중률 방문자 추이 예측 정보 |
| 카탈로그 ID | uddi:TatsCnctrRateService |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/TatsCnctrRateService` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: contentId(관광지 ID) 필수. 예측 모델 기반 데이터.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `tatsCnctrRatedList` | `/tatsCnctrRatedList` | 관광지 집중률/방문자 추이 예측 조회 | contentId(관광지ID), pageNo, numOfRows | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `tatsCnctrRatedList`

**용도**: 관광지 집중률/방문자 추이 예측 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/TatsCnctrRateService/tatsCnctrRatedList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&areaCd=51&signguCd=51130&tAtsNm=%EA%B0%84%ED%98%84%EA%B4%80%EA%B4%91%EC%A7%80
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
| contentId | - | 필수 | string | - | 관광지ID |
| pageNo | - | 필수 | string | - | - |
| numOfRows | - | 필수 | string | - | - |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `baseYmd` | 기준일자 | datetime | 20260515 | - |
| `areaCd` | 지역코드 | code | 51 | - |
| `areaNm` | 지역명 | string | 강원특별자치도 | - |
| `signguCd` | 시군구코드 | code | 51130 | - |
| `signguNm` | 시군구명 | string | 원주시 | - |
| `tAtsNm` | tAtsNm | string | 간현관광지 | - |
| `cnctrRate` | cnctrRate | number | 46.71 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"baseYmd": "20260515", "areaCd": "51", "areaNm": "강원특별자치도", "signguCd": "51130", "signguNm": "원주시", "tAtsNm": "간현관광지", "cnctrRate": "46.71"}
{"baseYmd": "20260516", "areaCd": "51", "areaNm": "강원특별자치도", "signguCd": "51130", "signguNm": "원주시", "tAtsNm": "간현관광지", "cnctrRate": "90.49"}
{"baseYmd": "20260517", "areaCd": "51", "areaNm": "강원특별자치도", "signguCd": "51130", "signguNm": "원주시", "tAtsNm": "간현관광지", "cnctrRate": "98.2"}
```

**TripCraft 활용 포인트**: 특정 관광지 집중률 예측. 붐비지 않는 시간대 추천 기능.

---

## 5. 코드 카탈로그

