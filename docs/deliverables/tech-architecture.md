---
type: deliverable
id: tech-architecture
title: "KoreaPath AI — 기술 아키텍처"
author_agent: apispecialist
author_model: claude-opus-4-7
created: 2026-04-17T18:30:00+09:00
status: draft
llm_compatibility: universal
related: [service-plan, wireframes, business-model]
---

# KoreaPath AI — 기술 아키텍처

> Visit Korea Open API 15개+를 핵심 데이터 소스로, AI 코스 생성 엔진과 실시간 혼잡도 예측을 결합한 서비스의 기술 설계서.

---

## 1. 하이레벨 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                        Clients                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│  │  iOS App   │  │ Android    │  │  Web PWA   │            │
│  │ (Swift/UIK)│  │ (Kotlin)   │  │ (Next.js)  │            │
│  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘            │
└────────┼────────────────┼────────────────┼─────────────────┘
         │                │                │
         └────────────────┼────────────────┘
                          ▼
               ┌──────────────────────┐
               │   CDN (CloudFront)   │
               └──────────┬───────────┘
                          ▼
               ┌──────────────────────┐
               │  API Gateway (REST)  │
               │    + Rate limiter    │
               │    + WAF             │
               └──────────┬───────────┘
                          ▼
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
┌───────────────┐ ┌──────────────┐ ┌───────────────┐
│  Auth Service │ │ Course Engine│ │ Realtime Svc  │
│  (JWT + OAuth)│ │ (Python/FastAPI)│ │ (Node/WS)   │
└───────┬───────┘ └──────┬───────┘ └──────┬────────┘
        │                │                │
        └────────────────┼────────────────┘
                         ▼
        ┌────────────────────────────────┐
        │        Data Layer              │
        │  ┌──────────┐  ┌─────────────┐ │
        │  │PostgreSQL│  │  Redis      │ │
        │  │ (user,   │  │  (cache,    │ │
        │  │  course) │  │   session)  │ │
        │  └──────────┘  └─────────────┘ │
        │  ┌──────────┐  ┌─────────────┐ │
        │  │   S3     │  │ ClickHouse  │ │
        │  │ (media)  │  │ (analytics) │ │
        │  └──────────┘  └─────────────┘ │
        └────────┬───────────────────────┘
                 ▼
  ┌──────────────────────────────────┐
  │  External APIs                    │
  │  ┌────────────────────────────┐   │
  │  │ Visit Korea OpenAPI (15개+)│   │
  │  └────────────────────────────┘   │
  │  ┌────────────────────────────┐   │
  │  │ OpenAI GPT-4o (course gen) │   │
  │  │ Local LLM (cost optimal)   │   │
  │  └────────────────────────────┘   │
  │  ┌────────────────────────────┐   │
  │  │ Naver Map · Google Maps    │   │
  │  └────────────────────────────┘   │
  │  ┌────────────────────────────┐   │
  │  │ Payment (Toss · Stripe)    │   │
  │  └────────────────────────────┘   │
  └──────────────────────────────────┘
```

---

## 2. Visit Korea API 활용 매트릭스 (핵심 15종)

### 2-1. API별 기능 매핑

| # | API 명 | 용도 | 호출 빈도 | 캐시 TTL |
|---|---|---|---|---|
| 1 | `related-attractions` (관광지별 연관 관광지) | 코스 생성 — 연관 POI 50개 | 코스 생성마다 | 24h |
| 2 | `visitor-concentration-forecast` (집중률·방문자 예측) | 혼잡도 배지, 재조정 | 시간당/현장 체크 | 1h |
| 3 | `central-attractions-by-municipality` (기초지자체 중심 관광지) | 지역별 앵커 POI | 월 1회 | 30d |
| 4 | `area-tourism-demand-density` (지역별 관광 수요 강도) | 숨은 명소 발굴 | 주 1회 | 7d |
| 5 | `tourism-big-data` (관광 빅데이터) | 트렌드 추천, 계절 요소 | 주 1회 | 7d |
| 6 | `tourism-info-korean` (국문 관광정보) | 기본 POI 메타 | 신규/업데이트 | 24h |
| 7 | `tourism-info-english` (영문) | 외국인 UI 콘텐츠 | 동 위 | 24h |
| 8 | `tourism-info-chinese-simplified` (중문 간체) | 동 위 | 동 위 | 24h |
| 9 | `tourism-info-japanese` (일문) | 동 위 | 동 위 | 24h |
| 10 | `barrier-free-travel` (무장애 여행) | 접근성 필터 | 코스 생성마다 | 24h |
| 11 | `audio-guide` (오디오 가이드) | POI 상세 음성 | 재생마다 | 30d |
| 12 | `pet-friendly-travel` (반려동물) | Phase 2 | 코스 생성마다 | 24h |
| 13 | `gocamping` (고캠핑) | Phase 2 | 코스 생성마다 | 24h |
| 14 | `durunubi-trails` (두루누비 도보길) | Phase 2 | 월 1회 | 30d |
| 15 | `photo-contest-winners` (관광사진 수상작) | 포토스팟 큐레이션 | 월 1회 | 30d |

### 2-2. 코스 생성 API 조합 흐름

```
[사용자 입력: 지역·일수·테마·동반·예산]
              │
              ▼
┌─────────────────────────────────────────────┐
│ 1. 앵커 POI 선정                             │
│   central-attractions-by-municipality        │
│   + tourism-big-data (계절 트렌드)           │
└─────────────┬───────────────────────────────┘
              ▼
┌─────────────────────────────────────────────┐
│ 2. 연관 POI 확장                             │
│   related-attractions (앵커당 10-20개)       │
│   + area-tourism-demand-density (숨은 명소) │
└─────────────┬───────────────────────────────┘
              ▼
┌─────────────────────────────────────────────┐
│ 3. 접근성 필터링 (옵션)                      │
│   barrier-free-travel (휠체어/노인 모드)    │
└─────────────┬───────────────────────────────┘
              ▼
┌─────────────────────────────────────────────┐
│ 4. 시간대별 혼잡도 매핑                      │
│   visitor-concentration-forecast (30일 예측) │
└─────────────┬───────────────────────────────┘
              ▼
┌─────────────────────────────────────────────┐
│ 5. 최적 동선 계산 (TSP + 제약 + 예산)        │
│   내부 알고리즘 + LLM 보조                   │
└─────────────┬───────────────────────────────┘
              ▼
┌─────────────────────────────────────────────┐
│ 6. 언어 로컬라이즈                           │
│   tourism-info-{ko|en|zh|ja}                │
│   + audio-guide (옵션)                      │
└─────────────┬───────────────────────────────┘
              ▼
      [최종 코스 JSON 반환]
```

---

## 3. 핵심 서브시스템

### 3-1. Course Engine (Python / FastAPI)

- **입력**: `(region, days, theme, companions, budget, accessibility)`
- **처리**:
  1. 후보 POI 풀 생성 (앵커 + 연관)
  2. 제약 필터링 (접근성, 예산)
  3. 시간대별 혼잡도 스코어링
  4. 경로 최적화 — `TSP + Time Window` (or-tools)
  5. LLM 리파이너 — "자연스러운 내러티브" 생성
- **출력**: Course JSON (Day·Slot·POI·Congestion·Budget)
- **SLA**: p95 < 3초

### 3-2. Realtime Service (Node.js + WebSocket)

- **기능**: 체크인 시 다음 POI 혼잡도 폴링(5분 주기), 임계치 70% 초과 시 대안 계산
- **알고리즘**: 거리 기반 KNN + 테마 유사도 + 실시간 혼잡도
- **Push**: FCM (Android) / APNs (iOS)
- **SLA**: 체크인 → 대안 제시 p95 < 2초

### 3-3. AI/LLM Layer

| 용도 | 1차 선택 | 폴백 | 비고 |
|---|---|---|---|
| 코스 자연어 설명 | OpenAI GPT-4o | Claude Haiku | 월 10만 호출 예상 |
| 다국어 요약 | Claude Sonnet | GPT-4o-mini | 품질 > 비용 |
| 로컬 추천 (비용 최적) | Qwen2.5-32B on-prem | GPT-4o-mini | Phase 3부터 |
| 내부 에이전트 | Claude Opus | GPT-4o | 운영·분석용 |

**비용 통제**:
- 캐시 히트율 목표 70%+
- 토큰 사용량 대시보드 (Langfuse)
- 규칙 기반 → LLM 호출 감소 5:1 이상

---

## 4. 데이터 파이프라인

### 4-1. Batch ETL (매일 03:00 KST)

```
Visit Korea API  →  Airbyte  →  S3 (Raw)  →  dbt  →  PostgreSQL
                                                 ↘
                                                   ClickHouse (Analytics)
```

- **스케줄러**: Prefect
- **스키마 변화 대응**: Great Expectations 검증
- **데이터 지연**: Visit Korea API 업데이트 + 1시간 이내

### 4-2. Realtime Stream (혼잡도)

```
visitor-concentration-forecast ─► Kafka ─► Redis (hot cache)
                                      ↘
                                        ClickHouse (audit)
```

- **TTL**: 1시간 (예측 신뢰도 구간)
- **장애 대응**: Redis Down 시 Postgres fallback

### 4-3. Feature Store

| 피처 | 저장소 | 갱신 |
|---|---|---|
| POI 메타 (이름·좌표·카테고리) | Postgres | 일 배치 |
| 혼잡도 시그널 | Redis | 1h |
| 사용자 선호 임베딩 | pgvector | 세션 종료 시 |
| 코스 템플릿 | S3 | 수동 + 주간 자동 |

---

## 5. 보안 & 개인정보

### 5-1. 인증/인가

- **OAuth 2.0** (Kakao, Google, Apple, Email)
- **JWT** (RS256, 15분 access + 30일 refresh)
- **API Gateway WAF** — OWASP Top 10 차단

### 5-2. 데이터 보호

| 데이터 | 보호 |
|---|---|
| 이메일·전화 | AES-256 at rest, TLS 1.3 in transit |
| 위치 정보 | GPS 저장 금지, 세션 종료 시 폐기 |
| 결제 | PG사 토큰화, 카드 번호 미저장 |
| 사용 로그 | 90일 후 익명화 (k-anonymity k=5) |

### 5-3. 개인정보 최소 수집

공모전 심사 기준 준수:
- 이메일, 닉네임, 국가코드만 필수
- 위치·나이는 선택
- 제3자 제공 없음 (선택 동의 제외)

---

## 6. 스케일링 전략

### 6-1. 트래픽 예측

| 단계 | MAU | Peak QPS | 인프라 규모 |
|---|---|---|---|
| MVP | 5천 | 5 | t3.medium × 2 |
| Beta | 10만 | 200 | t3.xlarge × 4 + RDS |
| V1.0 | 100만 | 3,000 | EKS 20 pods + RDS r6g.2xl |

### 6-2. 오토스케일

- **앱 컨테이너**: HPA (CPU 70%, RPS 500/pod)
- **DB**: RDS Aurora, read replica × 3
- **캐시**: ElastiCache Redis Cluster
- **CDN**: CloudFront (정적 자원·이미지)

### 6-3. 비용 최적화

| 항목 | 최적화 기법 |
|---|---|
| LLM | 규칙 기반 우선 + 캐시 + 온프레 LLM Phase 3 |
| API 호출 | 공격적 캐시 (혼잡도 1h, 정적 24h~30d) |
| 이미지 | WebP + Responsive |
| Cold path | Serverless Lambda (배치 ETL) |

---

## 7. 개발 스택

### 7-1. 백엔드
- **언어**: Python 3.12 (Course Engine), Node.js 20 (Realtime)
- **프레임워크**: FastAPI, NestJS
- **ORM**: SQLAlchemy, Prisma
- **최적화 엔진**: Google OR-Tools

### 7-2. 프론트엔드
- **iOS**: Swift 5.9 + SwiftUI
- **Android**: Kotlin + Jetpack Compose
- **Web**: Next.js 14 (App Router) + React 18
- **공통**: TypeScript + React Query

### 7-3. 인프라
- **Cloud**: AWS (ap-northeast-2 서울)
- **IaC**: Terraform
- **CI/CD**: GitHub Actions + ArgoCD
- **관측**: Datadog + Sentry + Langfuse

---

## 8. DevOps 및 품질

| 항목 | 정책 |
|---|---|
| 테스트 커버리지 | 백엔드 80%, 프론트 60% |
| 빌드 | PR당 자동 빌드 + E2E (Playwright) |
| 배포 | Blue/Green, 카나리 5% → 100% |
| SLO | API p95 < 500ms, 가용성 99.9% |
| 관측 | Trace ID 전파, 알림 임계치 자동화 |

---

## 9. Visit Korea API 제약 대응

| 제약 | 대응 |
|---|---|
| Rate Limit | 캐시 + 배치 Pre-fetch + 키 로테이션 |
| 응답 지연 | Circuit Breaker + 타임아웃 2s + Fallback DB |
| 스키마 변경 | Contract Test (CI) + 버전별 어댑터 |
| 영어 데이터 일관성 | 누락 시 LLM 번역 Fallback |
| 혼잡도 데이터 공백 | 과거 30일 평균 추정치 사용 |

---

## 10. 공모전 제출 단계 기술 완성도

| 체크 | 항목 | 상태 |
|---|---|---|
| ✅ | Visit Korea API 5개 MVP 연결 | 문서화 |
| ✅ | 코스 생성 규칙 기반 알고리즘 | 설계 완료 |
| ✅ | 다국어 UI 4개 (ko/en/zh/ja) | 설계 완료 |
| ✅ | 접근성 필터 (barrier-free) | 설계 완료 |
| ✅ | 시뮬레이션 5건 사용자 여정 검증 | 완료 (`knowledge-base/simulations/`) |
| 🔄 | 프로토타입 구현 | 10월 최종 심사까지 |
| 🔄 | 보안/개인정보 컴플라이언스 | 본격 개발 시 |

---

## 11. 마일스톤

| 시기 | 마일스톤 |
|---|---|
| 2026-05-06 | 공모전 제안서 제출 (설계·시뮬레이션 기반) |
| 2026-07 | MVP 백엔드 (Course Engine + 5 API) |
| 2026-08 | iOS/Android Alpha |
| 2026-09 | Beta 배포, 1만 사용자 테스트 |
| 2026-10 | 공모전 1차 심사 (기능 완성) |
| 2026-11 | 공모전 최종 심사 (PT) |

---

*작성: APISpecialist | 참조: `knowledge-base/tourism-api/한국관광공사 OpenAPI 전체 카탈로그.md`, `docs/deliverables/service-plan.md`*
