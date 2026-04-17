---
type: simulation
id: sim-154-photohunt-korea-x-emmachen
title: "PhotoHunt Korea × Emma Chen (외국인 20대 백패커)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T14:00:00Z
status: draft
llm_compatibility: universal
related:
  - "[[PhotoHunt Korea - AI 포토 스팟 큐레이터 & 포토 투어 앱]]"
  - "[[Emma Chen, 23, Freelance Photographer (Taiwan)]]"
aliases: ["PhotoHunt Korea × Emma Chen (외국인 20대 백패커)"]
---

# SIM-154: PhotoHunt Korea × Emma Chen (외국인 20대 백패커)

## 시나리오

에마는 대만 출신 프리랜서 사진작가로 인스타그램 팔로워 5만 명에게 한국 숨은 명소를 소개한다. 이번 한국 방문에서 전주·경주 지방 여행을 계획하며 "공식 검증된 포토스팟"을 찾고 있었다. 대만 여행 커뮤니티 PTT에서 "PhotoHunt Korea, 한국관광공사 공식 사진 DB 기반이라 신뢰도 높음"이라는 후기를 발견하고 즉시 설치했다. 프리랜서 사진작가로서 공모전 수상작 기반 큐레이션이 특히 매력적으로 느껴졌다.

---

## 사용자 여정

### 1단계: 진입
- PTT 후기 → 앱스토어에서 영문 설명 확인 (영문 지원 여부 확인 후 설치)
- 앱 실행: 영어 UI로 즉시 전환 성공 — "Finally a Korean travel app with proper English!" 반응
- 온보딩: "Photography", "Architecture", "Nature" 카테고리 선택

### 2단계: 행동
- 전주 한옥마을 검색 → `tourism-photos` + `photo-contest-winners` 기반 스팟 18곳 표시
- 공모전 수상작 탭: 촬영 각도·계절·시간대 정보 포함된 수상작 사진 10장 확인 — "This is exactly what I needed" 반응
- `visitor-concentration-forecast`: 전주 한옥마을 다음날 오전 8시 방문자 12%, 오후 2시 89% — 오전 일찍 출발 확정
- 경주 포토 투어 코스 생성: 첨성대 → 동궁과 월지(야경) → 양동마을 코스, `area-tourism-diversity` 높은 점수 확인
- `tourism-info-english` 기반 각 스팟 영문 상세 설명으로 역사 맥락까지 이해
- 방문 후 앱 내 SNS 공유 기능: 위치·영문 해시태그 자동 생성 → 인스타그램 바로 게시

### 3단계: 결과
- 전주 오전 8시 한옥마을: 혼잡 없이 원하는 각도에서 전문 수준 사진 촬영 성공
- 인스타그램 포스트 조회수 12만 → 댓글에 "What app did you use?" 다수
- 팔로워에게 앱 적극 추천 스토리 게시
- 경주 2일차에도 앱 코스 그대로 활용, 야경 사진 포트폴리오 추가

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **10** | 프리랜서 사진작가의 모든 니즈(공식 스팟, 촬영 팁, 혼잡도, 영문 정보)가 충족됨 |
| 사용 편의 | **9** | 영문 UI 완전 지원, SNS 연동까지 끊김 없는 흐름, 사진작가 특화 UI |
| 구현 타당성 | **9** | 포토 API 2개(tourism-photos + photo-contest-winners) + 영문 정보 API의 조합이 외국인 크리에이터에 최적 |

**종합 점수: 28/30**

---

## Pass/Fail 판정

> **✅ PASS**

Emma Chen은 PhotoHunt Korea의 이상적 타깃 중 하나다. 프리랜서 사진작가라는 직업적 특성과 인스타그램 크리에이터 활동이 앱의 모든 핵심 기능과 완벽히 맞아떨어졌다. 영문 UI 지원과 공모전 수상작 기반 촬영 팁이 차별화 포인트로 작동했으며, 팔로워 5만 명에 대한 자발적 추천은 강력한 국제 바이럴 효과를 창출한다.

---

## 개선 제안

1. 사진작가 크리에이터 전용 모드: 일반 여행자용 추천 외에 "프로 촬영 팁" 심화 탭 추가 — 조리개·셔터스피드·렌즈 추천 등 기술적 정보 제공으로 사진 전문가 락인
2. 번체 중국어 UI 추가: 대만·홍콩 사용자를 위한 번체 중국어 지원으로 동아시아 크리에이터 시장 확장 (에마 같은 인플루언서의 자연 바이럴 극대화)
