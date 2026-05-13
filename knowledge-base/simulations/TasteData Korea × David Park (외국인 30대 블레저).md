---
type: simulation
id: sim-195-tastedata-korea-x-p5-foreign-30s-bleisure
title: "TasteData Korea × David Park (외국인 30대 블레저)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T14:00:00Z
status: final
llm_compatibility: universal
related:
  - "[[TasteData Korea - 빅데이터 기반 로컬 미식 여행 큐레이터]]"
  - "[[David Park, 35, Senior Product Manager (USA)]]"
aliases: ["TasteData Korea × David Park (외국인 30대 블레저)"]
---

# SIM-195: TasteData Korea × David Park (외국인 30대 블레저)

## 시나리오

서울 출장 중 저녁 식사 자리를 찾던 David는 Reddit r/koreatravel에서 TasteData Korea 추천 댓글을 발견한다. "신용카드 데이터 기반 현지인 맛집 — Yelp의 한국판이지만 광고 없음"이라는 설명이 Google Maps 폐업 식당에 몇 번 데인 그에게 즉각적으로 설득력 있다. 영어 UI로 설치해 서울 강남 지역을 검색한다. PM 배경이라 앱 구조를 빠르게 파악하고, 소비 강도 히트맵에서 실제 현지인 직장인 점심 밀집 지역과 관광 밀집 지역이 구분되는 것을 보고 신뢰도가 높아진다.

---

## 사용자 여정

### 1단계: 진입
- Reddit 추천 댓글 → 설치 → 영어 전환 즉시 완료
- 강남 검색 → 현지인 소비 히트맵 탐색 → PM 시각: "데이터 소스(신용카드)가 명확해서 신뢰 가능"
- 첫 3분 내 앱 구조 파악 완료 — UX 학습 곡선 없음

### 2단계: 행동
- 강남 직장인 점심 소비 밀집 지역 탭: 역삼동 한식 코스요리 소비 강도 높음
- 음식 테마 선택: 한국 음식 문화 탐방 (외국인 입장에서의 첫 한식 깊이 탐방)
- 저녁 코스: 된장찌개 전문점 → 막걸리 선술집 → 야식 떡볶이 자동 생성
- 각 음식에 영어 설명(재료·조리법·문화 맥락)이 함께 제공 → David의 "음식 문화 이해" 니즈 충족
- 연관 관광지: 맛집 골목 주변 편집샵·카페 연결 → 저녁 식사 후 동선 자연 연장

### 3단계: 결과
- 역삼동 된장찌개집 방문 → 현지 직장인들 속에서 "진짜 한국 저녁" 경험 → 극도로 만족
- Reddit에 후기 게시: "TasteData Korea found me the most authentic Korean dinner of my trip" → 조회수 2,400
- 다음 출장 때도 첫 번째로 열 앱으로 지정. 미국 동료들에게도 추천

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **9** | Google Maps 폐업 식당 문제를 실제 소비 데이터로 해결. 영어 음식 설명이 외국인 문화 탐방 니즈 충족. 미식 모험 욕구와 완벽 정렬 |
| 사용 편의 | **9** | 영어 UI 완성도 높음. PM 수준의 UX 기준을 충족하는 완성도. 데이터 소스 투명성으로 신뢰 형성 |
| 구현 타당성 | **8** | 영어 음식 정보 + 소비 데이터 + 연관 관광지 조합 실현 가능. 영어권 사용자 대상 PMF 높음 |

**종합 점수: 26/30**

---

## Pass/Fail 판정

> **✅ PASS**

TasteData Korea는 David Park에게 최고 점수를 받는다. Google Maps의 한국 데이터 부정확성 문제를 실제 소비 데이터로 해결하고, 영어 음식 문화 설명이 재미교포 2세의 한식 탐방 니즈까지 충족한다. 유용성 9점, 종합 26점으로 20개 시뮬레이션 중 최고 수준이다. Reddit을 통한 자발적 후기 전파가 외국인 사용자 획득의 핵심 채널임을 확인했다.

---

## 개선 제안

1. Reddit·Tripadvisor 등 외국인 여행 커뮤니티 공유 최적화 — 영어 딥링크, OG 태그 완성도로 소셜 공유 시 미리보기 품질 향상
2. "출장자 모드" 도입 — 미팅 위치 기준 반경 내 저녁 식사 추천, 접대용·개인용 카테고리 분리로 블레저 여행자 특화 시나리오 지원
