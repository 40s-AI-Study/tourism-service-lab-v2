---
type: idea
id: koreadem-atlas
title: "KoreaDemand Atlas - 관광 수요 강도 기반 지역 발굴 플랫폼"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:20:00Z
updated: 2026-04-17T14:40:00Z
status: final
llm_compatibility: universal
round: 2
peer_review_score: 7/10
peer_review_by: ba-agent
apis_used:
  - area-tourism-resource-demand
  - area-tourism-demand-density
  - area-tourism-diversity
  - tourism-big-data
  - central-attractions-by-municipality
  - visitor-concentration-forecast
  - related-attractions
  - tourism-info-korean
  - tourism-info-english
api_count: 9
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
| `related-attractions` | 발굴 지역 연관 관광지·음식·숙박 네트워크 (발굴 도구 강화) |
| `tourism-info-korean` | 지역 상세 정보 + `reservationUrl` 필드로 예약 딥링크 제공 |
| `tourism-info-english` | 외국인 장기 체류자 영문 지원 + 영문 예약 URL |

## 차별화 포인트

- **빅데이터 4종 완전 통합**: `resource-demand` + `demand-density` + `diversity` + `big-data` 동시 활용한 서비스 전무
- `area-tourism-resource-demand`: Round 1 미활용, 공모전 희소 API
- 데이터 리터러시 높은 30-40대 파워 여행자 + 크리에이터 이코노미 공략
- "남보다 먼저 발견" → SNS 바이럴 동기 내재

## 🔧 API 기술 검토 — BA 피어 리뷰 개선 (v2)

> APISpecialist 검토 결과 (2026-04-17). BA 7/10 점수 기반 2가지 약점 해소.

### 약점 1: 발굴 도구 한계 → `related-attractions` API 추가

**문제**: 히트맵으로 지역은 발견하지만, 그 지역 내 "뭘 할 수 있는지" 탐색 경로가 약함.

**해결**: `related-attractions` API (기존 미활용) 추가
- 중심관광지와 높은 연결성을 가진 연관관광지·음식·숙박 유형별 50위 데이터
- "발굴 지역 클릭 → 연관 스팟 네트워크 그래프" 시각화
- `central-attractions-by-municipality`와 결합: 중심 관광지 → 연관 스팟 drill-down
- API 수: 8개 → **9개** (공모전 데이터 활용 점수 추가 가점)

### 약점 2: 수익화 경로 불명확 (예약 연동 부재) → `reservationUrl` 필드 활용

**문제**: 예약 연동 없어 사용자 여정이 "발견" 에서 끊김. 별도 예약 API 없음.

**해결**: Visit Korea OpenAPI 내장 필드 활용 — 외부 API 추가 불필요
- `tourism-info-korean` / `tourism-info-english` 상세 응답에 `reservationUrl`, `homepageUrl` 필드 포함
- `related-attractions` 숙박(숙박 유형) 데이터로 숙박 예약 딥링크
- 구현 방식: 관광지 상세 카드에 "예약하기" 버튼 → `reservationUrl`로 외부 연결
- 수익화: 제휴 예약 서비스(야놀자·여기어때) 파트너 링크로 전환 가능 (앱 출시 후)

**결론**: 27개 Visit Korea API 범위 안에서 두 약점 모두 해소. 별도 외부 API 연동 없음.

## 공모전 배점 전략

- **데이터 활용(20점)**: 빅데이터 지수 4종 전부 + 예측 API = 8개 → 최고 점수
- **기획력(30점)**: 빅데이터를 일반인이 쉽게 쓰는 앱으로 전환한 기획 독창성
- **심사위원 임팩트**: 한국관광공사 자체 데이터 인프라를 가장 깊이 활용한 앱
