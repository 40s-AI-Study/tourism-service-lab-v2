---
type: simulation
id: sim-175-koreawork-wander-x-p5-foreign-30s-bleisure
title: "KoreaWork & Wander × David Park (외국인 30대 블레저)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T14:00:00Z
status: final
llm_compatibility: universal
related:
  - "[[KoreaWork & Wander - 디지털 노마드 워케이션 인텔리전스]]"
  - "[[David Park, 35, Senior Product Manager (USA)]]"
aliases: ["KoreaWork & Wander × David Park (외국인 30대 블레저)"]
---

# SIM-175: KoreaWork & Wander × David Park (외국인 30대 블레저)

## 시나리오

도윤은 이번 한국 출장에서 일정을 2주로 늘려 마지막 1주는 제주에서 원격근무를 해보기로 했다. 회사 승인을 받고 "한국 워케이션 + 관광" 계획을 세우는 중에 Reddit r/digitalnomad에서 KoreaWork & Wander 앱 언급을 발견한다. PM으로서 앱을 설치하자마자 UX 품질을 평가하기 시작한다. 영어 UI, 제주 지역 관광 자원 수요 데이터, 고속 인터넷 글램핑 필터가 모두 갖춰진 앱 구성에 "이 앱 만든 사람이 뭘 아네"라는 반응을 보인다. 업무 환경과 업무 후 관광을 동시에 설계하는 기능이 블레저 여행자의 핵심 니즈를 정확히 겨냥한다는 것을 인식한다.

---

## 사용자 여정

### 1단계: 진입
- Reddit r/digitalnomad 추천 → 앱스토어 4.6점 확인 → 설치
- 영어 UI 즉시 작동, 온보딩에서 "얼마나 머물 예정인가요?" → "1주일" 선택
- 제주 선택 → area-tourism-resource-demand 대시보드: 제주 서부 추천, 동부 성수기 과밀 경고

### 2단계: 행동
- gocamping API: 와이파이·콘센트 확인된 제주 프리미엄 글램핑 3곳 (1박 15~20만원 범위 필터)
- 업무 환경 태그: "고속 인터넷(100Mbps+), 독립 작업 공간, 오션뷰" 조합 필터 적용
- area-tourism-diversity 지수: 제주 ★★★★★ — 비즈니스 후 관광 다양성 최고
- 업무 후 관광 자동 추천: 오전 원격근무 → 오후 올레길 하이킹 → 저녁 로컬 해산물 식당
- related-attractions API로 숙소 반경 20km 내 관광지 상세 매핑
- 주간 시간표 형태로 "업무 일정 + 관광 일정" 자동 배치 기능 확인

### 3단계: 결과
- 제주 서부 글램핑 1주일 예약, 오전 근무 + 오후 관광 루틴 완성
- LinkedIn에 "Finally found an app that actually supports bleisure travel in Korea" 포스팅 → 실리콘밸리 한국계 네트워크 공유
- PM 관점 피드백 이메일 앱 팀에 직접 발송 — 구체적 UX 개선 제안 포함

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **9** | 관광 자원 수요 분석 + 고속 인터넷 글램핑 필터 + 업무-관광 주간 일정 자동 배치가 블레저 여행자의 핵심 니즈를 완전히 커버 |
| 사용 편의 | **8** | 영어 완비 + 데이터 기반 지역 추천이 PM의 높은 UX 기준을 충족. 주간 일정 자동 배치 기능은 블레저 사용 패턴과 완벽 호환 |
| 구현 타당성 | **8** | area-tourism-resource-demand × gocamping × related-attractions 3종 API 조합이 이 서비스의 핵심 — 모두 구현 가능한 API이며 연계 로직이 타당 |

**종합 점수: 25/30**

---

## Pass/Fail 판정

> **✅ PASS**

KoreaWork & Wander는 David Park 페르소나에게 가장 높은 적합성을 보인다. 영어 지원 + 데이터 기반 지역 추천 + 업무-관광 통합 일정 설계가 블레저 여행자의 모든 핵심 니즈를 충족한다. PM의 LinkedIn·Reddit 영향력을 통한 실리콘밸리 한국계 네트워크 바이럴 효과도 기대할 수 있어 앱의 핵심 홍보대사 페르소나다.

---

## 개선 제안

1. "Bleisure Weekly Planner" 기능 강화: 사용자가 입력한 업무 시간(예: 오전 9~12시)을 기준으로 남은 시간을 관광으로 자동 채우는 주간 캘린더 뷰 제공 — PM처럼 시간 최적화에 민감한 블레저 여행자에게 최고의 차별화 기능
2. 비자 정보 탭 추가: 90일 무비자 입국 가능 국가 리스트와 체류 기간 계산기를 앱 내 제공 — 도윤 같은 미국 국적 원격근무자가 한국 장기 워케이션 결정 전 가장 먼저 확인하는 정보를 앱 내에서 해결하면 전환 결정 속도 향상
