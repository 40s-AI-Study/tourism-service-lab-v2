---
type: simulation
id: sim-155-photohunt-korea-x-davidpark
title: "PhotoHunt Korea × David Park (외국인 30대 블레저)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T14:00:00Z
status: final
llm_compatibility: universal
related:
  - "[[PhotoHunt Korea - AI 포토 스팟 큐레이터 & 포토 투어 앱]]"
  - "[[David Park, 35, Senior Product Manager (USA)]]"
aliases: ["PhotoHunt Korea × David Park (외국인 30대 블레저)"]
---

# SIM-155: PhotoHunt Korea × David Park (외국인 30대 블레저)

## 시나리오

도윤은 서울 출장 중 수요일 오후 3시간이 비었다. Google Maps에서 경복궁 주변 포토스팟을 검색하다 결과가 부정확해 불만을 느끼던 차에, Reddit r/koreatravel에서 "PhotoHunt Korea — way better than Google Maps for photo spots in Korea"라는 상위 추천 댓글을 보고 설치했다. PM으로서 앱 UX 품질을 즉시 평가하는 습관이 있어 설치 후 첫 30초가 중요했다.

---

## 사용자 여정

### 1단계: 진입
- Reddit 추천 → 앱스토어 영문 설명 확인 → 설치 (1분 이내)
- 앱 실행: 영문 UI 기본값 — "Clean UI, good first impression" 평가
- 온보딩: "History & Culture", "Architecture", "Street Photography" 선택

### 2단계: 행동
- 현재 위치 기반 검색 → 경복궁 주변 포토스팟 지도 즉시 표시
- `visitor-concentration-forecast`: 지금 오후 3시 방문자 집중률 58%, 오전 9시 22% — 지금이 적당히 활기차지만 감당 가능한 수준
- 경복궁 서북쪽 각도 수상작 촬영 팁 확인 → "Right side of Gwanghwamun, shoot toward Bugaksan" 영문 팁
- `tourism-info-english` 기반 경복궁 역사 설명 읽으며 이동 — Google Maps보다 훨씬 풍부한 콘텐츠
- 북촌 한옥마을 연계 코스 자동 생성, 3시간 내 완성 가능 동선 확인

### 3단계: 결과
- 경복궁→북촌 2시간 반 코스 성공적 완료
- 찍은 사진을 파트너에게 전송 "Korea is so photogenic!"
- 앱 평가: "Best Korean travel app I've used. Google Maps should learn from this."
- 주말 경주 방문 계획에도 동일하게 활용 예정, 앱 유지

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **9** | Google Maps 대체재로서 영문 포토스팟 정보 + 혼잡도 + 역사 설명의 3중 가치 제공 |
| 사용 편의 | **9** | PM 기준에서도 합격점인 UX, 영문 UI 완성도 높음, 위치 기반 즉시 추천 우수 |
| 구현 타당성 | **9** | tourism-info-english + tourism-photos + visitor-concentration-forecast의 외국인 특화 조합 타당 |

**종합 점수: 27/30**

---

## Pass/Fail 판정

> **✅ PASS**

David Park은 PhotoHunt Korea의 주요 타깃은 아니지만(포토그래퍼보다는 일반 여행자), 영문 UI와 풍부한 영어 콘텐츠 덕분에 높은 만족도를 보였다. 특히 Google Maps의 한국 데이터 한계를 정확히 채우는 포지셔닝이 유효했다. PM 관점의 긍정 평가는 앱 품질 신호이며, Reddit 같은 영어권 커뮤니티에서의 입소문 효과가 기대된다.

---

## 개선 제안

1. 시간 기반 코스 필터: "나에게 2시간 있어" 같은 가용 시간 입력 시 최적 포토 투어 코스를 자동 생성하는 기능 — 블레저 여행자의 핵심 니즈 직접 충족
2. Google Maps 연동 내보내기: 생성된 포토 투어 코스를 Google Maps 경로로 내보내는 기능으로, Google Maps 친숙한 외국인 사용자의 진입 장벽 추가 제거
