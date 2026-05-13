---
type: plan
id: 2026-phase2-dev-plan
title: "TripCraft Korea — Phase 2 서비스 개발 계획 (2026년 5~9월)"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-05-13T00:00:00+09:00
status: draft
competition: 2026 관광데이터 활용 공모전
trigger: 예비심사 통과 시 활성화
---

# TripCraft Korea — Phase 2 서비스 개발 계획

> **전제**: 2026년 5월 예비심사 통과 시 활성화  
> **기간**: 2026-05 ~ 2026-09 (5개월)  
> **목표**: 2026년 10월 1차 심사(기능 심사)에 제출 가능한 **동작하는 MVP** 완성

---

## 1. 개발 목표 (MVP 범위)

### 필수 기능 6개 (공모전 제출 MVP)

| # | 기능 | 구현 방식 | 우선순위 |
|---|---|---|---|
| F1 | **관광 정보 검색** | KTO TourAPI `searchKeyword` + `areaBasedList` | Must |
| F2 | **맞춤형 코스 자동 생성** | `relatedTour` + `middlePerformanceRanking` 기반 동선 알고리즘 | Must |
| F3 | **혼잡도 회피 + 대안 추천** | `visitorConcentration` + CLIP 유사도 벡터 검색 | Must |
| F4 | **위치 기반 오디오 가이드** | `audioGuide` API + Geolocation 50m 트리거 | Must |
| F5 | **여행 경비 자동 합산** | TourAPI `detailInfo` 입장료 + 카카오 모빌리티 이동비 | Should |
| F6 | **팔도 스탬프 적립** | 위치 EXIF 인증 + 카카오 로그인 + 포인트 DB | Should |

---

## 2. 기술 스택

| 레이어 | 기술 | 이유 |
|---|---|---|
| **Frontend** | Vanilla HTML/CSS/JS (초기) → React (안정화 후) | 빠른 MVP 검증 우선 |
| **Backend** | Python FastAPI | KTO API 프록시 + 코스 생성 로직 |
| **벡터 DB** | Chroma (로컬) | TourAPI 26만 건 CLIP 임베딩 |
| **인증** | 카카오 로그인 SDK | 스탬프 + 코스 저장 연동 |
| **지도** | 카카오맵 API | 경로 시각화 + 마커 |
| **오디오** | KTO `audioGuide` + TTS | 위치 트리거 자동재생 |
| **배포** | GitHub Pages (프론트) + Render/Railway (백엔드) | 무료 티어로 시연 환경 |

---

## 3. 개발 일정 (5개월 스프린트)

### Sprint 1 — 2주차 (5월 말): 기반 설정
- [ ] KTO API Key 발급 + 연동 테스트 (전체 12종)
- [ ] 카카오 개발자 앱 등록 (지도 + 로그인 + 모빌리티)
- [ ] FastAPI 프로젝트 초기화 + GitHub 레포 분리 (`tripcraft-korea-app`)
- [ ] TourAPI 26만 건 CLIP 임베딩 파이프라인 구축

### Sprint 2 — 4주차 (6월 초): F1~F2 구현
- [ ] 관광 정보 검색 API (지역·키워드·카테고리)
- [ ] 코스 자동 생성 알고리즘 (1박2일 기본 템플릿)
- [ ] 프론트엔드 기본 UI (검색 + 코스 결과 화면)
- [ ] 카카오맵 코스 경로 시각화

### Sprint 3 — 6주차 (6월 말): F3 구현
- [ ] 혼잡도 데이터 파이프라인 (`visitorConcentration` + `visitAreaTrend`)
- [ ] CLIP 유사도 대안 추천 (상위 3개)
- [ ] 소외 지역 가중치 1.5배 알고리즘
- [ ] UI: 혼잡도 배지(🟢🟡🔴) + 대안 추천 카드

### Sprint 4 — 8주차 (7월 중): F4 구현
- [ ] `audioGuide` API 연동 + 음성 파일 스트리밍
- [ ] Geolocation API 50m 진입 감지
- [ ] 4개 언어 오디오 자동 전환 (한·영·중·일)
- [ ] 모바일 진동 + 자동재생 UX

### Sprint 5 — 10주차 (8월 초): F5~F6 + 통합
- [ ] 경비 자동 합산 (입장료·이동비·예상 식비)
- [ ] 카카오 로그인 + 팔도 스탬프 DB 설계
- [ ] 위치 EXIF 인증 + 스탬프 적립 UI
- [ ] 전체 기능 통합 테스트

### Sprint 6 — 12주차 (8월 말~9월): QA + 심사 준비
- [ ] 페르소나 10명 × 시나리오별 기능 검증
- [ ] 버그 수정 + 성능 최적화
- [ ] 심사 시연 스크립트 작성
- [ ] PT 자료 초안 (최종심사 대비)

---

## 4. 팀 역할 분담 (Phase 2)

| 에이전트 | Phase 2 역할 |
|---|---|
| 🎯 CEO | 스프린트 조율 + KTO·카카오 파트너십 협상 지원 |
| 📋 PM (기획님) | 기능 명세서 유지·업데이트, 스프린트 목표 관리 |
| 🔌 API 전문 | FastAPI 백엔드 구현, KTO/카카오 API 연동 |
| 🎨 UX | 프론트엔드 구현, 모바일 UX 최적화 |
| 💰 BA | KPI 추적, BEP 시뮬레이션 업데이트 |
| 🔍 MR | 경쟁사 동향 모니터링, 사용자 피드백 분석 |
| 🎭 Sim | 기능별 페르소나 시뮬레이션 검증 |

---

## 5. 성공 기준 (1차 심사 기준)

| 항목 | 목표 기준 |
|---|---|
| **서비스 완성도** | 6대 기능 전체 동작, 오류율 < 5% |
| **데이터 활용** | KTO OpenAPI 12종 실제 호출 로그 제출 가능 |
| **성능** | 코스 생성 5초 이내 (캐시 미스 기준) |
| **모바일 호환성** | iOS Safari + Android Chrome 정상 동작 |
| **시연 시나리오** | 페르소나 3종 × 전체 플로우 시연 완료 |

---

## 6. 리스크 & 대응

| 리스크 | 가능성 | 대응 |
|---|---|---|
| KTO API 할당량 초과 | 중 | Redis 캐시 + 배치 프리페치 |
| CLIP 임베딩 서버 비용 | 중 | 로컬 Chroma → 클라우드 마이그레이션은 Sprint 5 이후 |
| 카카오 API 심사 지연 | 저 | 미리 신청 (5월 예비심사 통과 즉시) |
| 팀 에이전트 동시 실행 한도 | 저 | maxConcurrentRuns=3 유지, 스프린트별 순차 우선 |

---

## 7. 활성화 조건

이 계획은 **예비심사 통과 통보 수신 시** 즉시 활성화됩니다.

- 통보 채널: gongmo@stunning.kr (이메일) 또는 api.visitkorea.or.kr 공지
- 활성화 시 CEO가 Sprint 1 서브이슈 생성 + 각 에이전트 할당
- 신규 레포: `40s-AI-Study/tripcraft-korea-app` 생성 권장

---

*작성: 📋 기획님 (PM) | 2026-05-13 | 활성화 대기 중*
