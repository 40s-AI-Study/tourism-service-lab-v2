---
type: adr
id: adr-006-phase2-tech-stack
title: "ADR-006: TripCraft Korea Phase 2 기술 스택 결정"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-05-13T00:00:00Z
status: proposed
trigger: 예비심사 통과 후 확정
llm_compatibility: universal
---

# ADR-006: TripCraft Korea Phase 2 기술 스택 결정

## 상태

`proposed` — 예비심사 통과 후 확정 예정

## 맥락

예비심사(5월 중)를 통과하면 2026-05~09월 5개월간 서비스 개발을 진행한다. 개발팀(API 전문 에이전트 + UX 에이전트 + 외부 개발자)이 일관된 기술 결정 기반에서 작업할 수 있도록 사전에 스택을 확정한다.

### 제약 조건

- 1인 또는 소규모 개발 → **운영 복잡도 최소화**
- 무료·저비용 배포 우선 (공모전 단계, 수익 없음)
- KTO OpenAPI + 카카오 API 의존 → **Python 또는 Node.js** 친화적
- MVP 완성 목표: **5개월 이내**

## 결정

### 프론트엔드: Vanilla HTML/CSS/JS → React (점진적 전환)

| 단계 | 스택 | 이유 |
|---|---|---|
| Sprint 1~3 (MVP) | Vanilla HTML/CSS/JS | 빠른 시작, 빌드 도구 불필요, 에이전트 코드 생성 친화적 |
| Sprint 4~6 (안정화) | React 18 + Vite | 컴포넌트 재사용, 상태 관리 필요 시 전환 |

### 백엔드: Python FastAPI

- KTO API 프록시, 코스 생성 알고리즘, 벡터 검색 로직
- 이유: Python 생태계(sentence-transformers, Chroma, numpy) 완비, 비동기 지원

### 벡터 DB: Chroma (로컬) → Pinecone (확장 시)

- TourAPI 26만 건 CLIP 임베딩 저장
- MVP: 로컬 Chroma (무료, 빠른 시작)
- 5만 MAU 이상: Pinecone 서버리스로 마이그레이션

### 외부 API 의존성

| API | 용도 | 인증 |
|---|---|---|
| KTO TourAPI (12종) | 관광지 검색, 코스 생성, 혼잡도 | API Key (data.go.kr) |
| 카카오맵 API | 지도, 경로, 마커 | JavaScript SDK Key |
| 카카오 로그인 | 사용자 인증, 스탬프 | REST API Key + Redirect URI |
| 카카오 모빌리티 | 이동 시간·거리 계산 | REST API Key |

### 배포: GitHub Pages + Render

| 레이어 | 플랫폼 | 비용 |
|---|---|---|
| 프론트엔드 | GitHub Pages | 무료 |
| 백엔드 API | Render 무료 티어 (또는 Railway) | 무료 (750시간/월) |
| 벡터 DB | 로컬 → Chroma Cloud 검토 | 무료 |

### 인증 저장: 로컬스토리지 + 카카오 세션

MVP 단계에서는 서버 세션 없이 카카오 로그인 토큰을 로컬스토리지에 저장.
보안 업그레이드는 Sprint 5 이후.

## 대안 검토

| 대안 | 기각 이유 |
|---|---|
| Next.js | 서버 컴포넌트 복잡도 불필요, Vercel 의존 |
| Django | FastAPI 대비 오버헤드 큼, API 서버 역할에 과함 |
| Supabase | PostgreSQL pgvector 성능이 Chroma 대비 낮음, 추가 의존성 |
| Cloudflare Workers | Python 미지원, KTO API 응답 캐시 제한 |

## 결과 (예상)

- 코스 생성 응답: 캐시 히트 **< 1초**, 캐시 미스 **< 5초**
- 배포 비용: **$0** (MVP 단계)
- 개발 인프라 셋업: **1~2일** (Sprint 1 첫 주)

## 확정 조건

예비심사 통과 통보 수신 즉시 이 ADR의 상태를 `proposed` → `approved`로 변경하고 Sprint 1 시작.

## 관련 문서

- [Phase 2 개발 계획](../00-plans/2026-phase2-dev-plan.md)
- [TripCraft Korea API 활용](../deliverables/proposal-tripcraft/04-api-utilization.md)
- [ADR-005 멀티에이전트 아키텍처](./005-multi-agent-architecture.md)
