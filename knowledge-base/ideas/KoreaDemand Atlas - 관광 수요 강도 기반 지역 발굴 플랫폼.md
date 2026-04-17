---
type: idea
id: koreadem-atlas
title: "KoreaDemand Atlas - 관광 수요 강도 기반 지역 발굴 플랫폼"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:20:00Z
status: draft
llm_compatibility: universal
round: 2
apis_used:
  - area-tourism-resource-demand
  - area-tourism-demand-density
  - area-tourism-diversity
  - tourism-big-data
  - central-attractions-by-municipality
  - visitor-concentration-forecast
  - tourism-info-korean
  - tourism-info-english
api_count: 8
target_users:
  - 30-40대 데이터 기반 계획형 여행자
  - 지역 관광 트렌드에 민감한 여행 파워유저
  - 여행 크리에이터·블로거
  - 외국인 장기 체류자 (한국 전체 탐방)
---

# KoreaDemand Atlas - 관광 수요 강도 기반 지역 발굴 플랫폼

## 서비스 개요

한국관광공사 빅데이터 지수 API 4종을 모두 통합한 **관광 수요 인텔리전스 지도**. 어느 지역이 지금 뜨고 있는지, 어디가 아직 숨겨진 보석인지를 데이터로 보여준다. "트렌디한 여행자가 남보다 먼저 발견하는 앱."

## Round 1과의 차별화

- **KoreaTrend Radar**: `area-tourism-demand-density` + `tourism-big-data` 위주, 핫플 추천
- **KoreaDemand Atlas**: 빅데이터 지수 4종 **전부** 통합 (`resource-demand` + `demand-density` + `diversity` + `big-data`), 수요 강도 지도 시각화에 집중. 발견 → 방문 예측 → 코스 생성 전 과정을 데이터 드리븐으로.

## 핵심 문제 (Pain Point)

- 빅데이터 관광 지수는 공개되어 있지만 일반인이 해석하기 어려움
- "이 지역이 뜨고 있다"는 정보를 데이터 기반으로 확인할 앱 없음
- 관광 자원 수요 vs. 소비 강도 간 불균형 → 저평가 지역을 파악해 방문하면 혼잡 없이 질 높은 경험 가능
- 여행 블로거·크리에이터는 "남들이 모르는 곳"을 원하지만 그 근거가 없음

## 핵심 기능

### 1. 관광 수요 강도 히트맵
- `area-tourism-demand-density` API: 체류 강도·소비 강도를 지역별 히트맵으로 시각화
- `area-tourism-resource-demand` API: 관광 서비스·문화 자원 수요 중첩 표시
- 두 지표 교차 분석 → "수요는 높지만 공급이 부족한 잠재력 지역" 자동 식별

### 2. 관광 다양성 + 빅데이터 종합 점수
- `area-tourism-diversity` API: 관광객 다양성·소비 다양성·국제 다양성 3지표
- `tourism-big-data` API: 이동통신·신용카드·내비게이션 실제 행동 데이터
- 지역별 "관광 잠재력 종합 점수" 산출 → 여행자 의사결정 지원

### 3. 수요 예측 기반 방문 타이밍
- `visitor-concentration-forecast` API: 30일 방문자 집중률 예측
- 수요 상승 중인 지역의 "아직 붐비지 않은 최적 방문 시점" 알림
- "이 지역 뜨기 전에 가세요" 알림 구독 기능

### 4. 지역 핵심 명소 + 코스 연동
- `central-attractions-by-municipality` API: 지역 중심 관광지 100위
- `tourism-info-korean` / `tourism-info-english`: 상세 관광 정보 이중 언어

## 사용자 여정

```
수요 히트맵 탐색 → 잠재력 지역 발견 → 방문 타이밍 확인 → 코스 생성
      ↓                    ↓                   ↓               ↓
demand-density      resource-demand        visitor-forecast  central-attractions
diversity           tourism-big-data                         tourism-info
```

## API 활용 요약

| API | 활용 방법 |
|---|---|
| `area-tourism-resource-demand` | 관광 자원 수요 → 공급 부족 지역 식별 (Round 1 미활용) |
| `area-tourism-demand-density` | 체류·소비 강도 히트맵 |
| `area-tourism-diversity` | 지역 다양성 지수 종합 평가 |
| `tourism-big-data` | 실제 행동 데이터 (이동통신·카드) |
| `central-attractions-by-municipality` | 지역 핵심 명소 코스화 |
| `visitor-concentration-forecast` | 방문 최적 타이밍 예측 |
| `tourism-info-korean` | 지역 상세 정보 국문 |
| `tourism-info-english` | 외국인 장기 체류자 영문 지원 |

## 차별화 포인트

- **빅데이터 4종 완전 통합**: `resource-demand` + `demand-density` + `diversity` + `big-data` 동시 활용한 서비스 전무
- `area-tourism-resource-demand`: Round 1 미활용, 공모전 희소 API
- 데이터 리터러시 높은 30-40대 파워 여행자 + 크리에이터 이코노미 공략
- "남보다 먼저 발견" → SNS 바이럴 동기 내재

## 공모전 배점 전략

- **데이터 활용(20점)**: 빅데이터 지수 4종 전부 + 예측 API = 8개 → 최고 점수
- **기획력(30점)**: 빅데이터를 일반인이 쉽게 쓰는 앱으로 전환한 기획 독창성
- **심사위원 임팩트**: 한국관광공사 자체 데이터 인프라를 가장 깊이 활용한 앱
