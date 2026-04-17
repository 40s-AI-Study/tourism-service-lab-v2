---
type: simulation
id: sim-25-koreapath-ai-x-rachel-kim
title: "KoreaPath AI × 레이첼 김 (교포 2세)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T16:30:00Z
status: draft
round: 2
llm_compatibility: universal
related:
  - "[[KoreaPath AI - 개인화 동선 자동 생성 + 혼잡도 최적화 앱]]"
  - "[[P10 레이첼 김 - 한국계 미국인 교포 2세]]"
aliases: ["KoreaPath AI × 레이첼 김 (교포 2세)"]
---

# SIM-25: KoreaPath AI × 레이첼 김 (교포 2세)

## 시나리오

42세 LA 건축가 레이첼 김은 10살 딸 소피아와 함께 전주·남원 3박 4일 뿌리 탐방 여행을 계획하고 있다. 한국어에 서툰 교포 2세로서 영어로 심층 문화 정보를 얻기 어렵고, 건축가로서의 전문적 관심사(한옥 구조, 전통 건축 양식)와 10살 아이의 흥미(체험 활동, 음식)를 동시에 충족하는 코스를 설계하기 까다롭다. KoreaPath AI에 영어로 상세 조건을 입력하고, 건축가 시각과 아동 동반 조건을 모두 반영한 맞춤 코스를 받아낸다.

---

## 사용자 여정

### 1단계: 진입

레이첼이 미국 건축 전문지 블로그에서 "AI-powered heritage travel in Korea" 기사를 읽고 KoreaPath AI를 설치한다. 언어를 English로 설정하고, 프로필에서 "Heritage & Cultural Travel"과 "Travelling with Kids (Age 10)" 두 가지 태그를 동시에 활성화한다. 앱이 "We'll blend in-depth cultural context with kid-friendly activities to create the perfect mixed itinerary"라는 메시지를 표시한다. 레이첼은 "Finally — an app that gets it"이라고 생각하며 조건 입력 화면으로 넘어간다.

### 2단계: 행동 (핵심 기능 3회 이상 사용 장면)

**인터랙션 1 — 전문가 + 아동 혼합 조건 입력**
레이첼이 영어 조건 입력 화면에서 다음을 세밀하게 설정한다.
- Destination: Jeonju + Namwon
- Duration: 3 nights / 4 days
- Travellers: 1 adult (42F, architect) + 1 child (10F)
- Budget: USD 150/day
- Primary purpose: Korean heritage roots exploration + architectural study
- Adult interests: "Hanok architecture, traditional construction techniques, heritage preservation, urban fabric of old towns"
- Child interests: "Hands-on cultural activities, traditional food making, age-appropriate history"
- Language: English content preferred; some Korean cultural context welcome
- Pace: Thorough but not exhausting for a 10-year-old (max 4 sites/day)

"Generate AI Itinerary" 버튼을 탭하면 related-attractions API, accommodation-info API, area-tourism-demand-density API가 호출되며, "Analyzing architectural heritage sites and child-friendly activity availability…" 메시지와 함께 18초간 로딩된다. 결과 화면에 "Jeonju–Namwon Heritage Trail (4 days)" 타이틀과 함께 성인 건축 심층 콘텐츠와 아동 체험 콘텐츠가 병렬로 표시된 일정표가 나타난다.

**인터랙션 2 — 건축가 전용 심층 콘텐츠 레이어 확인**
1일차 전주 한옥마을 일정 카드를 탭하면 일반 관광 정보와 별도로 "Architect's Lens" 버튼이 표시된다. 탭하면 건축가 전용 영어 해설 레이어가 활성화된다.

- 최씨 고택: "Late Joseon period (c. 1850), T-shaped anchae layout demonstrating gender-segregated spatial planning. Note the proportional relationship between the daechung (대청, main hall) span and the bracket system under the eaves — a ratio of 1:0.38 consistent with Jeolla-do regional style."
- 경기전: "Originally constructed 1410, rebuilt 1614 post-Imjin War. Observe the three-tiered stone platform (월대) — a hierarchical spatial device signaling sacred vs. secular zones. Compare with Gyeongbokgung's use of same typology at larger scale."
- 전주향교: "The unusual north–south axial inversion relative to standard Confucian academy plans reflects topographic adaptation — the mountain behind demanded a modified approach sequence."

레이첼이 최씨 고택 해설을 읽으며 감탄하고, 곧바로 "Save to Architecture Notes" 버튼을 탭해 앱 내 여행 노트에 저장한다. 딸 소피아를 위한 "Kid's Version" 토글을 누르면 같은 장소가 "A family lived here 200 years ago — can you spot where the children would have slept?" 형태의 탐험 퀴즈로 전환된다.

**인터랙션 3 — 아동 체험 활동 연동 및 일정 조율**
2일차 오후 일정에 "전통 비빔밥 만들기 클래스 (90분, 한국요리학교)"와 "한지 공예 체험 (60분, 전주한지박물관)"이 배치되어 있다. 레이첼이 비빔밥 클래스 카드를 탭하면 "10-year-old friendly: ★★★★★ — hands-on cooking with simple Korean, instructor speaks basic English" 배지와 함께 예약 가능 잔여석(3석)이 실시간으로 표시된다. "Book Now" 버튼을 탭하면 앱 내 결제로 즉시 예약이 완료되고, 확인 메일이 영어로 발송된다.

레이첼이 "How does this fit Sophia's energy level?" 버튼을 누르면 "Cooking class scheduled after a 90-min architectural tour — good timing. Children typically remain engaged for 60–90 min hands-on sessions at this age. Suggest a 20-min snack break before the class."라는 AI 페이싱 조언이 표시된다.

**인터랙션 4 — 남원 뿌리 탐방 및 영어 해설 연동**
3일차 남원 광한루원 일정에서 "Roots Connection" 기능을 탭하면 "Your family name 김(Kim) traces to Gimhae Kim clan — one of Korea's largest clans originating in the Gaya Kingdom (42–532 CE). Namwon was a significant cultural hub during the Goryeo period your ancestors would have known." 영어 설명이 표시된다. 이어서 "Would you like a heritage walk connecting Kim clan history in the Namwon area?" 제안이 나타나고, 레이첼이 수락하면 관련 유적 2곳이 기존 일정에 추가된다. 소피아를 위한 Kid's Version에는 "Let's go on a treasure hunt to find clues about your great-great-grandparents' world!" 형식의 미션 카드로 변환된다.

### 3단계: 결과

레이첼은 전주 한옥마을에서 건축가로서 조선 후기 목구조 비례 체계를 직접 분석하며 메모를 가득 채웠고, 소피아는 비빔밥을 직접 만들며 "Mom, I want to live here"라고 외쳤다. 남원 광한루원에서 뿌리 해설을 읽으며 두 모녀가 함께 가족 역사를 이야기하는 특별한 순간을 가졌다. 귀국 후 레이첼은 건축 전문지 블로그에 "KoreaPath AI gave me both a scholar's itinerary and a child's adventure — in the same trip"이라는 후기를 기고했다.

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **10** | 건축가 전문 관심사 + 10살 아이 체험 요구를 단일 AI 코스에서 병렬로 충족. 영어 심층 해설과 뿌리 연결 기능은 교포 여행 특수 목적에 정확히 부합 |
| 사용 편의 | **9** | "Architect's Lens"와 "Kid's Version" 토글 전환이 직관적. 앱 내 예약·결제 통합으로 외부 플랫폼 이동 최소화 |
| 구현 타당성 | **7** | 건축 전문 해설 콘텐츠 DB 구축과 족보 연계 "Roots Connection" 기능은 기술보다 콘텐츠 운영 비용이 관건. 초기 주요 유산지 한정 구현 후 점진적 확장 필요 |

**종합 점수: 26/30**

---

## Pass/Fail 판정

> **✅ PASS**

AI 개인화 기능이 "건축가 + 교포 + 아동 동반"이라는 복합적이고 특수한 여행 목적을 단일 코스로 통합하는 데 성공한다. 영어 심층 해설 레이어와 Kid's Version 토글은 동반자 간 서로 다른 관심사를 충돌 없이 병렬 제공하는 혁신적 UX로, 일반 여행 앱이 제공하지 못하는 차별적 가치를 명확히 입증한다.

---

## 개선 제안

1. **건축 전문 해설 DB 확충**: 건축학과 교수·문화재청 전문가와 협업하여 주요 한옥·궁궐·향교의 영어 건축 해설 콘텐츠를 체계적으로 구축
2. **Roots Connection 족보 연동**: 안동 한국국학진흥원, 족보닷컴 등 공식 족보 DB와 API 연동하여 성씨별 뿌리 여행 경로를 데이터 기반으로 자동 생성
3. **아동 연령대 맞춤 세분화**: 현재 "Kids" 단일 카테고리를 5–7세 / 8–11세 / 12–15세로 세분화하여 연령별 적합한 체험·해설 콘텐츠 정교화
