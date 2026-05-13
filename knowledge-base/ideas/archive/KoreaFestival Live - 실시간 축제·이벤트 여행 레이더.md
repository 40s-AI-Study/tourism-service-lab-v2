---
type: idea
id: koreafestival-live
title: "KoreaFestival Live - 실시간 축제·이벤트 여행 레이더"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:10:00Z
status: final
llm_compatibility: universal
round: 2
apis_used:
  - tourism-info-korean
  - tourism-info-english
  - visitor-concentration-forecast
  - area-tourism-demand-density
  - area-tourism-diversity
  - related-attractions
  - tourism-big-data
api_count: 7
target_users:
  - 20-40대 축제·이벤트 관심 국내 여행자
  - 한국 문화 축제를 경험하려는 외국인 관광객
  - 주말 여행 계획자 (당일치기/1박 2일)
---

# KoreaFestival Live - 실시간 축제·이벤트 여행 레이더

## 서비스 개요

한국의 지역 축제·계절 이벤트를 **실시간 데이터**로 추적하고, 방문 가치 점수·혼잡도 예측·연관 관광 코스를 자동 생성하는 축제 특화 앱. "이번 주말 어떤 축제가 있고, 얼마나 붐빌까?" 를 데이터로 답한다.

## Round 1과의 차별화

- **KoreaTrend Radar**: 빅데이터 기반 실시간 핫플 추천 (축제 아님, 일반 관광 트렌드)
- **KoreaFestival Live**: 축제·이벤트에만 집중, `visitor-concentration-forecast`로 축제 혼잡도 예측, `area-tourism-diversity`로 지역 다양성 지수 활용 → 축제 외 주변 관광 연계 강화

## 핵심 문제 (Pain Point)

- 한국 지역 축제 정보가 지자체별로 분산 (공식 통합 앱 없음)
- 축제 현장 혼잡도를 사전에 알 수 없어 "갔다가 포기"하는 경험 빈번
- 축제 + 주변 관광지 연계 정보 없음 → 축제만 보고 빠르게 귀가
- 외국인은 한국 전통 축제 정보를 영어로 접하기 어려움

## 핵심 기능

### 1. 전국 축제 레이더
- `tourism-info-korean` / `tourism-info-english` API: 전국 문화·계절·음식 축제 공식 데이터
- 날짜·테마·지역별 필터: 봄꽃/여름바다/가을단풍/겨울눈꽃 시즌 축제
- 달력 뷰 + 지도 뷰 동시 지원

### 2. 축제 혼잡도 + 방문 최적 시간대
- `visitor-concentration-forecast` API: 축제 개최지 30일 방문자 집중률 예측
- 축제 첫날 vs. 마지막 날 혼잡도 비교 → 최적 방문일 자동 추천
- `area-tourism-demand-density` API: 축제 지역 전반적 관광 소비 강도

### 3. 축제 가치 점수 + 지역 다양성 분석
- `area-tourism-diversity` API: 축제 지역의 관광 다양성 지수
- "이 지역은 축제 외에도 볼거리/먹거리 다양성 ★★★★" 표시
- `tourism-big-data` API: 이동통신·신용카드 데이터 기반 축제 실제 방문 패턴 분석

### 4. 축제 + 주변 관광 코스 자동 생성
- `related-attractions` API: 축제장 주변 연관 관광지·맛집·숙박 자동 연결
- 체류 시간별 코스: 당일 3시간 / 반나절 / 1박 2일

## 사용자 여정

```
축제 발견 → 혼잡도 확인 → 방문 결정 → 주변 코스 생성 → 현장 경험
     ↓              ↓              ↓              ↓
tourism-info  visitor-forecast  area-diversity  related-attractions
              demand-density    tourism-big-data
```

## API 활용 요약

| API | 활용 방법 |
|---|---|
| `tourism-info-korean` | 전국 축제 공식 정보 (국문) |
| `tourism-info-english` | 외국인 대상 축제 영문 안내 |
| `visitor-concentration-forecast` | 축제 혼잡도 예측 → 최적 방문일 |
| `area-tourism-demand-density` | 축제 지역 관광 소비 강도 분석 |
| `area-tourism-diversity` | 축제 지역 관광 다양성 → 체류 가치 평가 |
| `related-attractions` | 축제 + 주변 관광 코스 자동 연결 |
| `tourism-big-data` | 축제 실제 방문 패턴 빅데이터 |

## 차별화 포인트

- `area-tourism-diversity` API 활용: Round 1에서 미활용, 지역 다양성으로 "축제 이후 체류" 가치 극대화
- 혼잡도 + 축제 특화: KoreaTrend Radar와 다른 이벤트 중심 설계
- 외국인 문화 체험 수요 대응: 한국 전통 축제는 방한 목적 상위권

## 공모전 배점 전략

- **데이터 활용(20점)**: 빅데이터 API 3종 (`demand-density`, `diversity`, `tourism-big-data`) 동시 활용
- **기획력(30점)**: 축제 정보 분산 문제의 명확한 해결, 국내외 모두 타겟
- **지역 가점**: 진주남강유등축제(경남), 화천산천어축제(강원) 등 지역 특화 전략 가능
