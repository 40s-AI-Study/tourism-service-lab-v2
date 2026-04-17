---
type: simulation
id: sim-158-photohunt-korea-x-rachelkim
title: "PhotoHunt Korea × 레이첼 김 (교포 2세)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T14:00:00Z
status: draft
llm_compatibility: universal
related:
  - "[[PhotoHunt Korea - AI 포토 스팟 큐레이터 & 포토 투어 앱]]"
  - "[[레이첼 김, 42세, 한국계 미국인 교포]]"
aliases: ["PhotoHunt Korea × 레이첼 김 (교포 2세)"]
---

# SIM-158: PhotoHunt Korea × 레이첼 김 (교포 2세)

## 시나리오

래희는 건축가로 전주 한옥마을에 큰 관심을 갖고 방문했다. 딸(10세)에게 한국 문화를 사진으로 기록해주고 싶은 마음도 있다. 영어 한국 여행 블로그에서 "PhotoHunt Korea helps you find the best angles for architectural photography"라는 소개를 읽고 즉시 설치했다. 건축가로서 단순 관광 사진이 아닌 구도·빛·각도를 고려한 촬영에 관심이 많았다.

---

## 사용자 여정

### 1단계: 진입
- 영어 여행 블로그 링크 → 앱스토어 영문 설명 확인 → 설치
- 앱 실행: 영문 UI 기본 지원 — 즉각적 편의감
- 온보딩: "Architecture", "Traditional Culture", "Street" 카테고리 선택

### 2단계: 행동
- 전주 한옥마을 검색 → `photo-contest-winners` 기반 수상작 12장 확인
- 건축가 시각으로 수상작 분석: "이 사진은 처마 곡선을 포착했고, 이건 마당의 원근감을 활용했네" — 촬영 팁 직접 적용 가능한 수준의 정보
- `visitor-concentration-forecast`: 다음날 오전 7-8시 방문자 8% — 이른 아침 건축 사진 촬영을 위한 최적 타이밍 확인
- `tourism-info-english` 기반 한옥 건축 설명: "기둥·보·도리 구조" 등 영문 건축 용어 포함 — "I can use this for my lecture" 반응
- 딸에게 각 스팟에서 "Look at how the roof curves — this is called a 처마" 설명하며 함께 탐색
- 포토 투어 코스: 한옥마을 건축 집중 코스 생성, 오전 7시 출발 일정 확정

### 3단계: 결과
- 오전 7시 반 한옥마을: 안개 낀 이른 아침, 처마 곡선 사진 포트폴리오급 촬영 성공
- 딸: "엄마 이 앱이 사진 잘 찍는 법 알려줘요?" — 딸도 앱에 흥미를 보임
- 래희: LA 건축 사무소 동료들에게 앱 소개 의향 ("Great for architectural travel photography")
- `tourism-info-english` 한옥 건축 해설 텍스트를 스크린샷으로 저장 → 사무소 강의 자료 활용 계획

### 3단계: 결과 보완
- 앱 유지 및 경주 방문 시 재사용 예정
- 10살 딸 맞춤 콘텐츠 부재는 아쉬움으로 남음

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **8** | 건축 사진 특화 촬영 팁 + 영문 건축 해설 + 혼잡도 예측이 래희 니즈와 잘 맞음 |
| 사용 편의 | **8** | 영문 UI 완전 지원, 수상작 기반 촬영 팁이 건축가 직업군에 직관적으로 유용 |
| 구현 타당성 | **8** | photo-contest-winners + tourism-info-english 조합이 전문직 여행자에게도 가치 창출 |

**종합 점수: 24/30**

---

## Pass/Fail 판정

> **✅ PASS**

레이첼 김은 PhotoHunt Korea의 예상치 못한 고가치 사용자다. 건축가 시각에서 공모전 수상작의 구도·각도 정보와 영문 건축 해설을 전문적으로 활용했으며, 이른 아침 최적 타이밍 촬영까지 완벽히 실행했다. 교포 2세의 영어 우선 사용 환경에서 영문 UI가 핵심 진입 조건이 됐으며, 건축 전문직이라는 틈새 사용층에서도 앱이 유효함을 증명했다.

---

## 개선 제안

1. 건축·문화유산 테마 심화 포토 투어: 한옥·사찰·근대 건축 등 카테고리별 건축 촬영 특화 코스를 전문가 수준의 촬영 팁과 함께 제공하는 "Architecture Edition" 컨텐츠 라인 신설
2. 어린이 동반 포토 체험 모드: 10세 전후 아이가 함께 사진을 배울 수 있도록 쉬운 설명의 "어린이 포토 팁"을 스팟별로 추가, 가족 단위 교육 여행 시장 공략
