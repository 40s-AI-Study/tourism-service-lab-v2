---
type: adr
id: adr-003-top3-idea-selection
title: "ADR-003: 상위 3개 아이디어 선정 및 Stage 4 전환"
author_agent: ceo
author_model: claude-sonnet-4-6
created: 2026-04-17T13:30:00Z
status: approved
llm_compatibility: universal
---

# ADR-003: 상위 3개 아이디어 선정 및 Stage 4 전환

## 상태

`approved` — CEO 최종 결정 (2026-04-17)

## 맥락

Stage 3에서 10개 아이디어를 도출하고 BA가 사업성 점수화를 완료했다. 공모전 심사 기준(기획력 30점, 데이터 활용 20점, 사회적 가치, 지역 특화 가점 2점)을 종합 고려하여 CEO가 최종 3개 아이디어를 선정한다.

선정 기준:
1. BA 사업성 점수 (50점 만점)
2. 공모전 심사 항목과의 매핑 강도
3. 5개 페르소나 대상 서비스 범용성
4. API 활용 수 (데이터 활용 20점 확보)

## 결정

### 🥇 1순위: KoreaPath AI

**핵심 근거**: 한국 시장에 존재하지 않는 AI 코스 자동 생성 서비스. 심사위원 임팩트 최대.

- 사업성 점수: 44/50
- 활용 API: `related-attractions`, `visitor-concentration-forecast`, `central-attractions-by-municipality`, `tourism-big-data`, `area-tourism-demand-density` (5개)
- 타겟: 30-40대 한국인(코스 계획 시간 부족) + 외국인(한국 여행 최적화 니즈)
- 차별화: 트리플·네이버 여행 대비 "5초 입력 → 완성 코스" UX 혁신
- 경쟁 우위: visitor-concentration-forecast × related-attractions 조합 = 국내 유일

### 🥈 2순위: K-Guide Global

**핵심 근거**: 최대 시장(외래객 1,620만명) + 최다 API 활용(9개) → 데이터 활용 20점 만점 기대.

- 사업성 점수: 44/50
- 활용 API: `tourism-info-english`, `tourism-info-japanese`, `tourism-info-chinese-simplified`, `tourism-info-chinese-traditional`, `tourism-info-german`, `tourism-info-french`, `tourism-info-spanish`, `audio-guide`, `visitor-concentration-forecast` (9개)
- 타겟: 외국인 FIT 여행자 20-40대 (중국 24%, 일본 22%, 영어권 12%)
- 차별화: Visit Korea 공식 데이터 + 현대적 UX + 8개 언어 + 오디오 가이드 통합
- 경쟁 우위: "한국관광공사 공식 데이터 × 현대적 UX" 조합 = 공신력 + 사용성

### 🥉 3순위: AccessKorea

**핵심 근거**: 사회적 가치 심사 직결, 무장애 관광 시장 전무, 특별상 수상 가능성.

- 사업성 점수: 40/50
- 활용 API: `barrier-free-travel`, `tourism-info-korean`, `audio-guide`, `central-attractions-by-municipality` (4개)
- 타겟: 시니어(65세+ 970만명), 장애인(263만명), 영유아 동반 가족
- 차별화: 무장애 통합 플랫폼 한국 시장 전무. 공식 barrier-free-travel API 독점 활용
- 경쟁 우위: 사회적 포용성 + 고령화 메가트렌드 직격. 공모전 특별상 가능

## 탈락 이유 (상위 4-10위)

| 아이디어 | 탈락 이유 |
|---|---|
| PetKorea | 공모전 심사 차별성 포인트 약함. Stage 4 확장 후보 |
| KoreaTrend Radar | B2C 앱 vs 분석 대시보드 포지셔닝 불명확 |
| K-Local Explorer | KoreaPath AI와 코스 추천 기능 중복 |
| Audio Story Korea | K-Guide Global 내 포함 가능한 기능 수준 |
| KoreaWellness | 차별화 우위 부족, 기존 웰니스 앱 경쟁 심화 |
| EcoTrail Korea | 니치 시장, 수익성 낮음 |
| K-Camp Finder | 공모전 기획력 배점 확보 어려움 |

## Stage 4 전환 계획

선정된 3개 아이디어에 대해 5개 페르소나(p1~p5) × 3개 서비스 = 15개 시뮬레이션 실행.

| 페르소나 | 특성 | 주요 검증 항목 |
|---|---|---|
| p1 (한국 20대 솔로) | 혼자여행, SNS 중시 | KoreaPath AI 코스 공유 기능 |
| p2 (한국 30대 커플) | 웰니스, 프리미엄 | KoreaPath AI 맞춤 코스 만족도 |
| p3 (한국 40대 가족) | 아이 동반, 안전 | AccessKorea 무장애 정확도 |
| p4 (외국 20대 백패커) | 저예산, 다국어 | K-Guide Global 언어 지원 |
| p5 (외국 30대 비즈 레저) | 시간 효율, 프리미엄 | K-Guide Global + KoreaPath 조합 |

**Pass 기준**: 각 시뮬레이션에서 핵심 사용자 니즈 3개 이상 충족 시 Pass.

## 결과

Stage 4 Simulation Loop 이슈 생성 → Simulator 에이전트 15개 시뮬레이션 실행.
