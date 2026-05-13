---
type: simulation
id: sim-24-koreapath-ai-x-amina-said
title: "KoreaPath AI × 아미나 사이드 (말레이시아 무슬림)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T16:30:00Z
status: final
round: 2
llm_compatibility: universal
related:
  - "[[KoreaPath AI - 개인화 동선 자동 생성 + 혼잡도 최적화 앱]]"
  - "[[P9 아미나 사이드 - 말레이시아 무슬림 여행자]]"
aliases: ["KoreaPath AI × 아미나 사이드 (말레이시아 무슬림)"]
---

# SIM-24: KoreaPath AI × 아미나 사이드 (말레이시아 무슬림)

## 시나리오

30세 말레이시아 인플루언서 아미나 사이드는 할랄 음식 확인, 기도 시간 준수, 기도실 위치 파악을 동시에 챙기면서 한국 여행 일정을 짜는 것이 늘 큰 부담이었다. KoreaPath AI에 "할랄 레스토랑 포함, 기도 시간 고려, 5박 6일" 조건을 영어로 입력하자 AI가 기도 5회 시간대에 맞춰 이동 구간을 자동 배치하고 할랄 인증 식당을 코스에 통합한 일정을 생성했다. 아미나는 무슬림 여행의 복잡한 제약 조건이 단번에 해소되는 경험을 한다.

---

## 사용자 여정

### 1단계: 진입

아미나가 말레이시아 무슬림 여행 커뮤니티 페이스북 그룹에서 "KoreaPath AI — halal-friendly tour planner" 후기 게시물을 보고 앱을 설치한다. 앱 실행 후 언어를 English로 설정하고, 프로필에서 "Muslim Traveller" 모드를 활성화한다. "Muslim Traveller Mode enabled — Halal dining, prayer time scheduling, and prayer room locator are now integrated into your itinerary" 알림이 화면 상단에 표시된다. 아미나는 "This is exactly what I needed"라고 혼자 중얼거리며 조건 입력 화면으로 진입한다.

### 2단계: 행동 (핵심 기능 3회 이상 사용 장면)

**인터랙션 1 — 무슬림 특화 조건 입력**
아미나가 영어 조건 입력 화면에서 다음을 설정한다.
- Destination: Seoul + Gyeongju
- Duration: 5 nights / 6 days
- Travellers: 1 adult
- Budget: USD 100/day
- Dietary requirement: Halal certified restaurants only
- Prayer schedule: Auto-integrate 5 daily prayers (Fajr, Dhuhr, Asr, Maghrib, Isha)
- Prayer location: Show nearest prayer room / mosque at each stop
- Interests: Traditional culture, street food, photography spots
- Crowd preference: Avoid peak hours for better photo opportunities

"Generate AI Itinerary" 버튼을 탭하면 accommodation-info API, related-attractions API, area-tourism-demand-density API가 호출되고 15초 후 6일치 통합 일정이 생성된다. 화면 상단에 "Prayer times auto-scheduled based on your location each day. Halal restaurants confirmed within 500m of each attraction" 배너가 표시된다.

**인터랙션 2 — 기도 시간 통합 일정 확인**
2일차 일정 화면을 펼치면 관광 일정 사이사이에 기도 블록이 녹색 카드로 삽입되어 있다.

```
08:30  Fajr prayer — hotel room (5 min)
09:00  Gyeongbokgung Palace (2h, low crowd: ★)
11:30  Dhuhr prayer — Itaewon Mosque (15 min, 2.1km from palace)
12:00  Halal lunch — Makan Malaysian-Korean Fusion ★★★★
13:30  Bukchon Hanok Village (1.5h)
15:15  Asr prayer — Seoul Central Mosque (8 min walk)
16:00  Insadong shopping & café
18:30  Maghrib prayer — Itaewon Mosque (prayer room reserved)
19:00  Halal dinner — Moslem Restaurant Itaewon ★★★★☆
20:30  Isha prayer — hotel room
```

아미나가 Dhuhr prayer 카드를 탭하면 이태원 모스크까지의 도보 경로, 예배 시설 사진, 여성 기도실 이용 가능 여부(✅ 가능)가 표시된다. "Add to map for offline use" 버튼으로 오프라인 저장도 가능하다.

**인터랙션 3 — 할랄 식당 필터 및 상세 확인**
일정 내 "Halal lunch — Makan Malaysian-Korean Fusion" 카드를 탭하면 상세 정보가 표시된다.
- 할랄 인증 배지: "Korea Muslim Federation Certified (2025)"
- 메뉴 하이라이트: Halal Bulgogi Rice, Kimchi Jjigae (no pork), Tteokbokki
- 리뷰: "말레이 여행객 리뷰 47개 — 4.8/5"
- 예약: "Book table" 버튼 (앱 내 직접 예약)

아미나가 "More halal options nearby" 버튼을 누르면 반경 1km 내 할랄 인증 식당 8곳이 지도에 핀으로 표시된다. 각 핀을 탭하면 인증 기관, 유효 기간, 메뉴 미리보기가 팝업으로 나타난다.

**인터랙션 4 — 인플루언서 콘텐츠 연동**
아미나가 경복궁 일정 카드의 "Content Creator Tips" 버튼을 탭하면 "Low-crowd golden hour: 9:00–9:45 AM (crowd index 14)" 안내와 함께 히잡 착용자에게 어울리는 포토 스팟 3곳이 추천된다. 각 스팟에는 "Muslim travel blogger @aminasaid_travels visited here" 배지와 함께 유사 구도 참고 사진이 제공된다. 아미나가 방문 후 사진을 업로드하면 자동으로 "Halal-friendly Korea" 해시태그 세트가 제안된다.

### 3단계: 결과

아미나는 5박 6일 동안 기도 시간을 한 번도 놓치지 않았고, 할랄 인증을 일일이 확인하는 수고 없이 매 끼니를 안심하고 즐겼다. 여행 중 인스타그램 릴스 7개를 올렸고, 그 중 경복궁 히잡 포토 릴스가 12만 뷰를 기록했다. 귀국 후 팔로워들에게 "KoreaPath AI — the only app you need for halal travel in Korea"를 강력 추천하는 후기 영상을 게시했다.

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **10** | 할랄 식당 + 기도 시간 + 기도실 위치를 AI가 자동 통합하여 무슬림 여행의 3대 Pain Point를 완전히 해소 |
| 사용 편의 | **9** | 영어 UI, Muslim Traveller 모드 원클릭 활성화, 오프라인 저장 지원으로 해외 사용자 친화적 |
| 구현 타당성 | **8** | 할랄 인증 DB 연동과 기도 시간 API(위치 기반 계산)는 기술적으로 구현 가능. 할랄 인증 식당 데이터 커버리지가 서울 외 지역에서 제한될 수 있음 |

**종합 점수: 27/30**

---

## Pass/Fail 판정

> **✅ PASS**

무슬림 여행자가 한국에서 겪는 핵심 불편(할랄 식당 탐색, 기도 시간 관리, 기도실 위치 파악)을 AI가 여행 계획 단계에서 선제적으로 통합 해결한다. 인플루언서 아미나의 SNS 활동과 연계된 콘텐츠 팁 기능은 앱의 말레이시아·동남아 무슬림 커뮤니티 내 자연 홍보 효과를 기대할 수 있다.

---

## 개선 제안

1. **할랄 인증 실시간 검증**: 한국이슬람교중앙회(KMF) API와 직접 연동해 인증 만료·취소 식당을 실시간 필터링하여 신뢰도 유지
2. **라마단 모드**: 라마단 기간 사후르·이프타르 시간을 기준으로 일정을 재구성하는 시즌별 특화 모드 추가
3. **말레이어 UI 지원**: 영어 외 말레이어(bahasa Malaysia) UI를 추가하여 영어에 불편한 중장년 무슬림 여행자 접근성 확대
