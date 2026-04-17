---
type: api-spec
id: visitor-concentration-forecast
title: "한국관광공사_관광지 집중률 방문자 추이 예측 정보"
category: big-data-forecast
author_agent: claude-code
author_model: claude-opus-4-7
created: 2026-04-17
source: https://api.visitkorea.or.kr/upload/manual/guide/file/1725501618773.zip
manual_file: knowledge-base/tourism-api/_raw/extracted/visitor-concentration-forecast/
llm_compatibility: universal
status: initial-spec
aliases: ["한국관광공사_관광지 집중률 방문자 추이 예측 정보"]
---

# 한국관광공사_관광지 집중률 방문자 추이 예측 정보

## 개요

'한국관광 데이터랩(DataLab)'의 지역별 관광지별 조회일 기준 향후 30일 관광객 집중률 방문자 추이 예측 정보 등을 제공합니다.

## 기본 정보

- **공급처**: 한국관광공사
- **타입**: REST
- **인증**: 공공데이터포털(data.go.kr)에서 ServiceKey 발급 필요
- **매뉴얼**: `_raw/extracted/visitor-concentration-forecast/` (Word + Excel)

## 추정 오퍼레이션 (자동 추출)

> Word 매뉴얼에서 자동 파싱 — 누락/오탐 가능. 정확한 스펙은 매뉴얼 원본 참고.

- `tatsCnctrRateList`
- `tatsCnctrRatedList`

## 공통 요청 파라미터 (추정)

모든 한국관광공사 OpenAPI 공통:
- `serviceKey` (필수): 공공데이터포털 발급 인증키
- `MobileOS` (필수): IOS / AND / WIN / ETC
- `MobileApp` (필수): 앱 이름
- `numOfRows` (선택): 페이지당 행 수
- `pageNo` (선택): 페이지 번호
- `_type` (선택): json / xml

## 공통 응답 구조

```json
{
  "response": {
    "header": {
      "resultCode": "0000",
      "resultMsg": "OK"
    },
    "body": {
      "items": { "item": [...] },
      "numOfRows": 10,
      "pageNo": 1,
      "totalCount": 100
    }
  }
}
```

## 활용 시나리오

'한국관광 데이터랩(DataLab)'의 지역별 관광지별 조회일 기준 향후 30일 관광객 집중률 방문자 추이 예측 정보 등을 제공합니다.

**공모전 활용 방안**: (에이전트 Stage 1 리서치에서 확정)

## 매뉴얼 원본

- 활용매뉴얼 docx: `_raw/extracted/visitor-concentration-forecast/`
- 분류체계 xlsx (있는 경우 포함): 카테고리 코드 매핑 정보
- 전체 페이지 수: 660 줄

## 연관 API

(Phase 3에서 아이디어 발산 시 채움)

---

## 관련 페이지

**사용하는 아이디어**
- [[ideas/2026-04-17-k-camp-finder|K-Camp Finder]]
- [[ideas/2026-04-17-ai-course-generator|KoreaPath AI]]
- [[ideas/2026-04-17-barrier-free-travel|FreeTrip Korea]]
- [[ideas/2026-04-17-kculture-pilgrimage|K-Universe]]
- [[ideas/2026-04-17-pet-korea|PetKorea]]
- [[ideas/2026-04-17-night-tourism|NightKorea]]
- [[ideas/2026-04-17-multilingual-guide|K-Guide Global]]
- [[ideas/2026-04-17-pet-friendly-travel|PetTrip Korea]]
- [[ideas/2026-04-17-family-trip-planner|FamilyKorea]]
- [[ideas/2026-04-17-wellness-tour|WellKorea]]
- [[ideas/2026-04-17-eco-green-trail|GreenTrail Korea]]
- [[ideas/2026-04-17-hidden-spot-congestion|LocalSecret]]
- [[ideas/2026-04-17-k-local-explorer|K-Local Explorer]]

**카탈로그**
- [[tourism-api/00-api-catalog|API 카탈로그]]

