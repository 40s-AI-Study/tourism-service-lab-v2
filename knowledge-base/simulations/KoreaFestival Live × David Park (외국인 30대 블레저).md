---
type: simulation
id: sim-165-koreafestival-live-x-p5-foreign-30s-bleisure
title: "KoreaFestival Live × David Park (외국인 30대 블레저)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T14:00:00Z
status: final
llm_compatibility: universal
related:
  - "[[KoreaFestival Live - 실시간 축제·이벤트 여행 레이더]]"
  - "[[David Park, 35, Senior Product Manager (USA)]]"
aliases: ["KoreaFestival Live × David Park (외국인 30대 블레저)"]
---

# SIM-165: KoreaFestival Live × David Park (외국인 30대 블레저)

## 시나리오

서울 출장 5일차, 도윤은 주말 이틀이 완전히 비어있다. Reddit r/koreatravel에서 "봄에 한국 가면 꼭 가야 할 축제"를 검색하다가 KoreaFestival Live 앱 추천 댓글을 발견한다. PM으로서 앱 UX에 민감한 도윤은 처음 화면만 봐도 "데이터가 진짜네"라는 인상을 받는다. 영어로 전국 축제 달력을 훑다가 진해군항제(벚꽃 축제)를 발견하고, 방문자 집중률 예측에서 토요일 오전 10시가 혼잡도 최고점임을 파악한다. 일요일 새벽 출발로 계획을 조정하고, "반나절 코스" 자동 생성 기능으로 KTX + 현지 이동까지 포함된 4시간짜리 일정을 받아든다.

---

## 사용자 여정

### 1단계: 진입
- Reddit 추천 → 앱스토어 검색 → 4.7점 리뷰 확인 후 신뢰하고 설치
- 영어 UI 자동 감지, 온보딩에서 "얼마나 자유 시간이 있나요?" 인풋 → "2일" 선택
- 전국 축제 지도 뷰에서 서울 기준 2시간 이내 거리 필터 적용

### 2단계: 행동
- 진해군항제 상세 페이지 → tourism-info-english API 기반 영어 역사 배경 + 이동 정보 완비
- 혼잡도 예측 그래프에서 일요일 오전 7시~9시 혼잡도 23% 확인
- "3시간 코스 생성" → 여좌천 로망스 다리 → 경화역 벚꽃 터널 → 해군사관학교 박물관 순서 자동 배치
- 지역 다양성 지수 ★★★ — 단기 방문에는 충분한 볼거리 확인
- tourism-big-data 기반 "외국인 방문자 실제 체류 시간 평균 3.2시간" 데이터 참고해 계획 확정

### 3단계: 결과
- 일요일 새벽 6시 30분 KTX 출발, 오전 중 벚꽃 만개 현장을 혼잡 없이 경험
- Reddit에 "This app actually has real-time crowd data unlike any Korean app I've seen" 후기 게시
- PM 관점에서 "데이터 기반 UX" 아이디어 메모 → 개인 링크드인 포스팅으로 앱 홍보

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **9** | "짧은 시간 최적화" 페인포인트를 "N시간 코스 생성" 기능이 직접 해결. 영어 완비 축제 정보는 블레저 여행자에게 결정적 가치 |
| 사용 편의 | **9** | 높은 UX 기준을 가진 PM이 "데이터가 진짜네"라는 첫인상을 가질 만큼 인터페이스 완성도가 중요. 시간 기반 필터가 블레저 여행 패턴과 정확히 맞아떨어짐 |
| 구현 타당성 | **8** | tourism-info-english + visitor-concentration-forecast 조합은 기술적으로 가장 성숙한 부분 — 도윤 같은 검증적 사용자에게도 신뢰 획득 가능 |

**종합 점수: 26/30**

---

## Pass/Fail 판정

> **✅ PASS**

KoreaFestival Live는 David Park의 "짧은 시간 최적화"와 "정확한 영어 정보" 두 가지 핵심 니즈를 모두 충족한다. PM 특성상 앱 품질에 즉시 이탈하는 성향이 있으나, 실시간 데이터 기반 인터페이스는 이 페르소나가 요구하는 신뢰 기준을 통과할 가능성이 높다. Reddit·LinkedIn 등 영향력 채널을 통한 자발적 홍보 효과도 기대할 수 있다.

---

## 개선 제안

1. "Bleisure Mode" 특화 기능 추가: 출장 도시·자유 시간 입력 시 KTX/버스 이동 시간을 포함한 반나절~하루 코스를 자동 계산해 제공 — 비즈니스 여행자의 가장 큰 고민인 "동선 최적화"를 앱 혼자 해결
2. 관광 빅데이터에서 "외국인 평균 체류 시간" 수치를 각 축제 페이지에 명시 — PM 같은 데이터 지향 사용자에게 신뢰도를 높이고 방문 전 시간 계획 수립에 실질적으로 기여
