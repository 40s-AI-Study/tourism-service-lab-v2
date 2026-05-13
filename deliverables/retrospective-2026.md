---
type: retrospective
id: retrospective-2026-competition
title: "2026 관광데이터 활용 공모전 프로젝트 회고"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-05-13T11:30:00+09:00
status: approved
llm_compatibility: universal
---

# 2026 관광데이터 활용 공모전 프로젝트 회고

> **공모전**: 2026 관광데이터 활용 공모전 ① 웹·앱 개발 부문  
> **마감**: 2026-05-06 16:00  
> **최종 제출 서비스**: TripCraft Korea  
> **작성일**: 2026-05-13  
> **작성자**: 📋 기획님 (ProductManager)

---

## 1. 프로젝트 개요

Tourism Service Lab은 Visit Korea OpenAPI를 활용해 20-40대 한국인·외국인 대상 관광 서비스 기획안을 완성하고 공모전에 제출하는 것을 목표로 했다. 전 과정을 Paperclip 멀티에이전트 시스템으로 운영했으며, CEO·ProductManager·MarketResearcher·UXDesigner·BusinessAnalyst·APISpecialist·Simulator 7개 에이전트가 협업했다.

| 항목 | 내용 |
|---|---|
| 기간 | 2026-04-17 ~ 2026-05-06 (약 3주) |
| 팀 | CEO, PM, 시장조사, UX, BA, API, 시뮬레이터 (7 agents) |
| 레포지토리 | tourism-service-lab-v2 |
| 최종 산출물 | TripCraft Korea — 4개 아이디어 통합 + 공모전 제안서 PDF |
| 활용 Visit Korea API | 27개 카탈로그 중 다수 활용 |

---

## 2. 프로젝트 타임라인 (Stage별)

### Stage 0: 인프라 & 설계 원칙 수립 (2026-04-17)

- GitHub 레포지토리(`tourism-service-lab-v2`) 생성
- **v3 실행 계획** 확정 — LLM-agnostic 설계 원칙 채택
- ADR-001: LLM-agnostic 에이전트 템플릿 정의
- ADR-002: 공통 메타데이터 스키마(YAML frontmatter) 정의
- 팀 구성 옵션 A/B/C 검토 → 옵션 B(Claude + GPT 혼합) 채택

**핵심 결정**: 모든 지침서·산출물을 GPT/Claude/로컬 LLM에서 동작하는 LLM-agnostic 포맷으로 작성. Claude 전용 XML 태그 사용 금지.

### Stage 1: 시장조사 & 페르소나 (2026-04-17 ~ 04-19)

- MarketResearcher: 국내외 관광 시장 트렌드 분석
- 10개 핵심 페르소나 정의
  - 한국인: 20대 솔로, 30대 커플, 40대 가족, 시니어, 전동휠체어 개발자
  - 외국인: 백패커(Emma), 블레저(David), 교포 2세(레이첼), 일본 직장인(하루카), 말레이시아 무슬림(아미나)
- 27개 Visit Korea API 카탈로그 문서화

### Stage 2: 지식베이스 구축 (2026-04-19)

- `knowledge-base/` 구조 정립 (business, competition, ideas, market-research, personas, simulations, tourism-api)
- 공모전 심사 기준 분석 (기획력 30점, 데이터 활용 20점, 사회적 가치, 지역 특화 가점 2점)

### Stage 3: 아이디어 발산 (7 Rounds)

| Round | 주요 아이디어 | 비고 |
|---|---|---|
| Round 1 | Hidden Gem Scout, K-Culture Deep Dive, Korea First Timer Guide, Mood Travel Matcher | 초기 브레인스토밍 |
| Round 2 | 20개 추가 아이디어 | Barrier-Free Journey, Eco Trail Explorer, Crowd-Free Alternative 등 |
| Round 3 | 상위권 고도화 | Audio Story Korea v2, LocalSecret v2, 치유여정 Korea |
| Round 4 | 카테고리 대표 8개 × 페르소나 5명 시뮬 | 40개 시뮬레이션 |
| Round 5 | K-Universe, KoreaPath AI, NightKorea 등 추가 | 감정나침반 Korea, 치유여정 통합 |
| Round 6 | Top 10 컨센서스 평가 | round6-top10-consensus.md |
| Round 7 | 최종 3개 선정 → 통합 아이디어 | TripCraft Korea 기획 |

**총 발산 아이디어**: 30개+ (현행 `ideas/` + `ideas/archive/` 합산)

### Stage 4: 시뮬레이션 루프 (가장 대규모 단계)

- **200개+ 시뮬레이션 파일** 생성 (서비스 × 페르소나 조합)
- 주요 검증 서비스: KoreaPath AI, K-Guide Global, AccessKorea, Audio Story Korea v2, EcoTrail Korea, LocalSecret v2, 치유여정 Korea 등
- 각 시뮬레이션: 페르소나 사용자 여정 + 핵심 니즈 충족 여부 + 개선 포인트
- Consensus 문서 생성으로 서비스별 종합 평가 집계

**ADR-003** (CEO 결정): Top 3 최종 선정
1. 🥇 KoreaPath AI — AI 코스 자동 생성, BA 44/50점
2. 🥈 K-Guide Global — 다국어 외국인 가이드, BA 44/50점, API 9개
3. 🥉 AccessKorea — 무장애 관광, 사회적 가치 심사 직결

### Stage 5: 기획 고도화 & 최종 제출 (2026-04~05)

- 각 에이전트 병렬 고도화 작업 (PM, UX, BA, API, Simulator)
- 10개+ 서비스 인터랙티브 프로토타입 HTML 구현
- **최종 피벗**: Top 3 개별 제출 → **TripCraft Korea** (4개 아이디어 통합) 단일 제안서
- 공모전 제안서 PDF 5페이지 작성 (표지 + 핵심 3화면 + 차별화 포인트)
- 2026-05-06 16:00 마감 전 제출 완료

---

## 3. 최종 제출 서비스: TripCraft Korea

### 통합 구성

| 구성 요소 | 원본 아이디어 | 핵심 기능 |
|---|---|---|
| AI 코스 생성 | KoreaPath AI | 5초 입력 → 완성 코스, 혼잡도 최적화 |
| 다국어 가이드 | K-Guide Global | 8개 언어, 오디오 가이드 통합 |
| 무장애 경로 | AccessKorea | 평지·계단 정보, 접근성 필터 |
| 감성 힐링 | 치유여정 Korea | 감정 체크인 → 힐링 코스 자동 매핑 |

### 활용 API (주요)

`related-attractions`, `visitor-concentration-forecast`, `central-attractions-by-municipality`, `tourism-info-english/japanese/chinese`, `audio-guide`, `barrier-free-travel`, `tourism-big-data`, `area-tourism-demand-density`

---

## 4. 팀 협업 방식

### 멀티에이전트 구조

```
CEO (오케스트레이션)
├── ProductManager (기획 총괄, 아이디어 통합, 최종 문서)
├── MarketResearcher (시장 조사, 트렌드, 페르소나 검증)
├── UXDesigner (UX 기획, 인터랙티브 프로토타입)
├── BusinessAnalyst (사업성 점수화, ROI 분석)
├── APISpecialist (API 매핑, 기술 아키텍처)
└── Simulator (페르소나 시뮬레이션, 사용자 여정 검증)
```

### 협업 프로토콜

- **이슈 기반 작업 관리**: Paperclip 이슈 시스템(TOU-XX)으로 모든 작업 추적
- **직접 소통**: CEO 경유 없이 서브이슈·코멘트 멘션으로 에이전트 간 직접 협업
- **병렬 처리**: 독립적 시뮬레이션·고도화 작업은 동시 진행 (maxConcurrentRuns: 3)
- **Push Discipline**: 작업은 `git push` 완료되어야 종료로 간주
- **커밋 컨벤션**: `[agent-name] type: summary` + `Co-Authored-By: Paperclip <noreply@paperclip.ing>`

### 잘 작동한 것들

1. **LLM-agnostic 설계**: Claude/GPT 모델 교체에도 동일한 AGENTS.md로 일관된 행동 유지
2. **이슈 기반 체크아웃**: 409 Conflict 방지, 동시 작업 충돌 없음
3. **시뮬레이션 대규모 실행**: 200개+ 시나리오로 서비스 강약점 객관화
4. **인터랙티브 프로토타입**: 실제 동작하는 HTML 프로토타입으로 심사 준비도 향상
5. **ADR 기록**: 의사결정 근거를 문서화해 팀 전체 컨텍스트 공유 효율화

---

## 5. 개선점 & 다음에 다르게 할 것

### 프로세스 개선

| 문제 | 원인 | 개선 방안 |
|---|---|---|
| 아이디어 발산 범위가 너무 넓어짐 | 초기 필터링 기준 불명확 | Stage 3 시작 전 "탈락 기준" 먼저 정의 |
| 시뮬레이션 파일 과다 (200개+) | 모든 조합 실행 | 상위 5개 서비스만 전 페르소나 시뮬, 나머지는 대표 2개 페르소나만 |
| 최종 피벗(통합 아이디어) 결정 지연 | 에이전트별 자기 아이디어 애착 | Stage 4 중반에 "통합 가능성 검토" 마일스톤 추가 |
| 프로토타입 품질 편차 | UX 에이전트 단독 작업 | BA·PM 사전 wireframe 승인 후 구현 착수 |

### 기술 개선

| 문제 | 원인 | 개선 방안 |
|---|---|---|
| 마크다운 줄바꿈 소실 | 코멘트 JSON 직렬화 오류 | `paperclip-issue-update.sh` 헬퍼 사용 표준화 |
| 로컬 LLM(opencode) 품질 낮음 | 26B 모델 추론 한계 | 복잡한 추론 작업은 GPT-4o 또는 Claude로 라우팅 강제화 |
| git push 누락 건 | 에이전트 비정상 종료 | heartbeat 종료 전 push 상태 체크 훅 추가 |

### 팀 구성 개선

- **Reviewer 에이전트 부재**: 최종 기획서 교차 검토 역할이 없었음 → 독립 Reviewer 에이전트 추가
- **디자이너 리소스 병목**: UXDesigner가 10개+ 프로토타입을 순차 처리 → 서비스별 병렬 실행 구조
- **데이터 수집 자동화**: MarketResearcher가 수동 리서치에 의존 → MCP 웹 검색 도구 연동 강화

---

## 6. 수치로 보는 프로젝트

| 지표 | 수치 |
|---|---|
| 총 이슈 (TOU-XX) | 103개 |
| 아이디어 파일 | 30개+ (archive 20개 포함) |
| 시뮬레이션 파일 | 200개+ |
| 인터랙티브 프로토타입 | 10개+ |
| Commit 수 | 40개+ |
| 활용 Visit Korea API | 10개+ |
| 최종 제안서 페이지 | 5페이지 (PDF) |
| 프로젝트 기간 | 약 3주 (2026-04-17 ~ 05-06) |

---

## 7. 최종 평가 & 제언

### 잘한 것

TripCraft Korea는 단일 API 포인트 서비스가 아닌 **4개 니즈(코스·다국어·접근성·감성)를 통합**한 서비스로, 공모전 심사 기준인 기획력(30점)·데이터 활용(20점)·사회적 가치를 동시에 공략하는 전략이 유효했다.

멀티에이전트 협업 프레임워크 자체가 이 프로젝트의 또 다른 성과다. Paperclip + LLM-agnostic 설계 원칙은 향후 유사 프로젝트에 재사용 가능한 인프라로 남는다.

### 다음 공모전을 위한 제언

1. **아이디어 수렴 타이밍 앞당기기**: Stage 3 Round 3 이후 바로 Top 3 고정
2. **제안서 디자인 에이전트 추가**: 심사는 내용뿐 아니라 비주얼 완성도도 좌우
3. **사용자 테스트 단계 추가**: 실제 타겟 페르소나(한국인·외국인 각 1명)에게 프로토타입 피드백 수집
4. **LLM 비용 최적화**: 시뮬레이션 단계에서 GPT-4o-mini / 로컬 LLM 우선 사용으로 비용 절감

---

*이 문서는 2026 관광데이터 활용 공모전 완료 후 팀 전체의 학습을 정리한 공식 회고입니다.*
