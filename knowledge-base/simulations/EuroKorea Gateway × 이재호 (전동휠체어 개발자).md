---
type: simulation
id: sim-107-eurokorea-gateway-x-leejaeho
title: "EuroKorea Gateway × 이재호 (전동휠체어 개발자)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T14:00:00Z
status: draft
llm_compatibility: universal
related:
  - "[[EuroKorea Gateway - 유럽어권 관광객 특화 다국어 허브]]"
  - "[[이재호, 38세, IT 개발자 (전동휠체어)]]"
aliases: ["EuroKorea Gateway × 이재호 (전동휠체어 개발자)"]
---

# SIM-107: EuroKorea Gateway × 이재호 (전동휠체어 개발자)

## 시나리오

백엔드 개발자인 재호는 앱스토어에서 새로운 한국 관광 앱을 발견할 때마다 "혹시 무장애 정보가 있을까" 하는 기대로 설치해본다. EuroKorea Gateway를 설치하고 실행하지만, 첫 화면의 언어 선택지가 러·스·프·독뿐임을 확인한다. 개발자 시각으로 API 구조를 추론해보니 이 앱은 유럽어권 관광객 전용 다국어 허브로 설계된 것임을 즉시 파악한다. 무장애 동선, 휠체어 경사도 데이터, 충전 포인트 정보는 API 목록 어디에도 없다. 기술적으로 흥미로운 API 설계이지만 재호에게는 아무 쓸모가 없다.

---

## 사용자 여정

### 1단계: 진입
- 앱스토어 한국 관광 앱 신규 출시 탐색 중 발견
- "혹시 barrier-free 필터가 있을까" 기대하며 설치
- 첫 화면: 유럽어 4개 선택지 — 한국어·무장애 관련 기능 없음 즉각 파악

### 2단계: 행동
- 개발자답게 앱 구조를 체계적으로 탐색 (2-3분)
- 활용 API 목록 추론: tourism-info-russian/spanish/french/german, audio-guide, central-attractions, related-attractions, tourism-photos
- 무장애 관련 API (`barrier-free-travel`) 미포함 확인
- 한국어 인터페이스 없어 실질적 탐색 불가

### 3단계: 결과
- 앱 삭제. "유럽어권 외국인 관광객 전용. 무장애 데이터 없음" 내부 메모
- 장애인 여행 카페 네이버로 복귀

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **1** | 무장애 데이터 전무. 전동휠체어 사용자에게 제공 가치 없음 |
| 사용 편의 | **3** | 개발자로서 앱 구조 파악은 가능하나 한국어 미지원으로 실용 탐색 불가 |
| 구현 타당성 | **8** | 유럽어권 외국인 대상 서비스로는 기술적으로 잘 설계됨 |

**종합 점수: 12/30**

---

## Pass/Fail 판정

> **❌ FAIL**

이재호가 절대적으로 필요한 무장애 동선 데이터, 전동휠체어 진입 가능 여부, 충전 포인트 정보는 EuroKorea Gateway의 설계 범위에 포함되지 않는다. 한국어 인터페이스조차 없어 내국인 장애인 사용자의 접근이 원천 차단된다. 종합 12점, FAIL.

---

## 개선 제안

1. 유럽어권 장애인 관광객도 한국을 방문하므로, 향후 `barrier-free-travel` API를 연동하면 유럽어권 장애인 여행자라는 틈새 시장 공략 가능
2. 무장애 필터는 현재 앱 설계와 독립적으로 추가할 수 있는 레이어로, 다음 버전 로드맵에 포함할 것을 검토 권장
