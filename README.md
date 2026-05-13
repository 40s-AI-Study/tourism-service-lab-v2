# Tourism Service Lab

> 2026 관광데이터 활용 공모전(웹·앱 개발) — **AI 다중 에이전트 자율 기획 프로젝트** 🏁 **제출 완료 2026-05-06**

## 프로젝트 개요

한국관광공사(KTO) Visit Korea Open API를 활용한 관광 서비스 기획을 **Paperclip 기반 AI 에이전트 7명**이 자율적으로 수행합니다. 시장 조사 → 페르소나 → 아이디어 발산 → 시뮬레이션 → 합의 리뷰 → 프로토타입 → 최종 기획서 전 과정을 멀티 에이전트가 병렬 협업합니다.

## 목표 (달성)

- **공모전**: 2026 관광데이터 활용 공모전 (웹·앱 개발) — ✅ 마감 **2026-05-06 16:00 제출 완료**
- **최종 제출 서비스**: **TripCraft Korea** — 카테고리 테마 기반 개인화 여행 플래너
- **타겟 사용자**: 20-40대 한국인 + 외국인 (양측 모두 사용 가능)
- **활용 데이터**: KTO OpenAPI 12종 + 카카오 4종 (https://api.visitkorea.or.kr)
- **산출물**: `docs/deliverables/proposal-tripcraft/PROPOSAL_FINAL.pdf` + 27개 인터랙티브 프로토타입

## AI 스터디 목적

이 프로젝트는 **AI 자율 기획 역량 검증**을 위한 스터디입니다. 모든 프롬프트·계획·의사결정·에이전트 산출물·세션 로그를 **전체 추적 가능한 형태**로 GitHub에 기록합니다.

## 레포 구조

```
tourism-service-lab-v2/
├── README.md                    # 이 파일
├── docs/
│   ├── 00-plans/                # 전체 실행 계획 (v1/v2/v3 + Round별 설계 프롬프트)
│   ├── 01-decisions/            # Architecture Decision Records (ADR)
│   ├── 02-prompts/              # 사용자 프롬프트 히스토리
│   ├── deliverables/            # 최종 공모 제출물 (기획서·와이어프레임·사업모델·아키텍처)
│   ├── prototypes/              # 아이디어별 프로토타입 HTML 포트폴리오
│   └── wiki/                    # 프로젝트 위키 (Home + 9페이지)
├── knowledge-base/              # llm-wiki 미러 (지식 저장소, 한국어 파일명)
│   ├── competition/             # 공모전 정보
│   ├── tourism-api/             # Visit Korea API 27종 스펙
│   ├── market-research/         # 시장 조사
│   ├── personas/                # 사용자 페르소나 (P1~P10)
│   ├── ideas/                   # 서비스 아이디어 (59개 발산 → 상위 10 확정)
│   ├── simulations/             # 시뮬레이션 262건
│   ├── reviews/                 # 팀 합의 리뷰 파일
│   └── business/                # 사업성 분석 + 점수 매트릭스
├── company-config/              # Paperclip 회사 설정 스냅샷 (AGENTS.md 포함)
└── scripts/                     # 자동화 스크립트 + 소셜 카드
```

## 팀 구성 (Tourism Service Lab · 7명)

| 이모지·이름 | 영문명 | 어댑터 | 주 업무 | 시그니처 |
|---|---|---|---|---|
| 🎯 전략님 | CEO | claude_local (Sonnet) | 전략 오케스트레이션 + Roll Call | "이건 이렇게 갑니다" |
| 📋 기획님 | ProductManager | claude_local (Sonnet) | 서비스 기획·기능 정의 | "5초 드립니다" |
| 🔍 리서치님 | MarketResearcher | claude_local (Sonnet) | 관광 트렌드·니즈 분석 | "이거 요즘 뜹니다" |
| 🎨 디자인님 | UXDesigner | claude_local (Sonnet) | 페르소나·와이어프레임·프로토타입 | "1픽셀은 양보 못해요" |
| 💰 분석님 | BusinessAnalyst | claude_local (Sonnet) | 사업성·수익 모델·점수화 | "숫자가 말해주네요" |
| 🔌 엔지니어님 | APISpecialist | claude_local (Sonnet) | API 활용 검증·기술 아키텍처 | "연결 완료" |
| 🎭 시뮬님 | Simulator | claude_local (Sonnet) | 페르소나별 시뮬레이션 | "저라면 이럴 것 같아요" |

**팀 협업 규칙** (AGENTS.md v2, 2026-04-17):
- `maxConcurrentRuns=3` 병렬 처리
- CEO 경유 없이 서브이슈·코멘트로 직접 소통
- CEO Roll Call: heartbeat마다 팀 상태 점검·봉인 에이전트 깨움
- 작업 완료 시 `git push` 필수 (Push Discipline)

## 최종 진행 현황 (전 라운드 완료)

| Round | 단계 | 상태 | 주요 산출물 |
|---|---|---|---|
| **Phase 0-2** | GitHub 인프라 + 지식베이스 + 회사 창립 | ✅ | KTO API + 7 에이전트 |
| **Round 1~2** | 아이디어 20개 + 페르소나 10명 + 시뮬 60건 | ✅ | PASS 12개 |
| **Round 3** | 기존 자산 × 새 관점 6축 융합 | ✅ | 아이디어 5개 추가, 프로토타입 3개 |
| **Round 4~5** | 59개 전체 TAM/SAM/SOM + BEP + 경쟁사 검증 | ✅ | 150점 매트릭스 |
| **Round 6** | 115점 컷 → 상위 10 확정 | ✅ | LocalSecret v2(123) 1위 |
| **Round 7** | 상위 10 인터랙티브 프로토타입 HTML | ✅ | 27개 프로토타입 |
| **최종 제출** | TripCraft Korea — 4개 아이디어 통합 | ✅ **2026-05-06** | `PROPOSAL_FINAL.pdf` |

## 아이디어 포트폴리오

**총 59개 아이디어 · 262건 시뮬 · 상위 10 확정**

| 순위 | 서비스명 | 점수 |
|---|---|---|
| 🥇 1 | LocalSecret v2 | 123/150 |
| 🥈 2 | KoreaPath AI | 119/150 |
| 🥉 3 | K-Universe | 118/150 |
| ... | (상위 10개 전체) | `knowledge-base/business/round6-final-ranking.md` |

**최종 제출**: TripCraft Korea (4개 아이디어 통합) → `docs/deliverables/proposal-tripcraft/`

**프로토타입 뷰어**: `http://127.0.0.1:3300/docs/prototypes/` (27개 인터랙티브 HTML)

## 관련 링크

- **공모전 홈**: https://api.visitkorea.or.kr/#/cntSearchDetail?no=1
- **API 활용 목록**: https://api.visitkorea.or.kr/#/useUtilExercises
- **GitHub Repo**: https://github.com/40s-AI-Study/tourism-service-lab-v2
- **프로젝트 위키**: [docs/wiki/](docs/wiki/)
- **Round 3 설계 프롬프트**: [docs/00-plans/2026-04-18-round3-prompt.md](docs/00-plans/2026-04-18-round3-prompt.md)

## 핵심 ADR

- [001 LLM-agnostic AGENTS.md 템플릿](docs/01-decisions/001-llm-agnostic-agents-template.md)
- [002 공통 메타데이터 JSON 스키마](docs/01-decisions/002-common-metadata-schema.md)
- [003 상위 3 아이디어 선정](docs/01-decisions/003-top3-idea-selection.md)

## 커밋 규칙

- `feat:` 신규 기능·콘텐츠
- `docs:` 문서 작업
- `research:` 리서치 결과
- `simulate:` 시뮬레이션 결과
- `design:` 디자인 산출물
- `fix:` 수정
- `chore:` 설정·인프라
- `[AgentName]` prefix: 에이전트가 커밋한 경우 (ex: `[productmanager]`, `[ceo]`)

모든 AI 에이전트 커밋에는 `Co-Authored-By: Paperclip <noreply@paperclip.ing>` 추가.

## 상태 (2026-05-13 기준)

- 시작일: 2026-04-17
- 제출 완료: **2026-05-06** — TripCraft Korea
- 현재 단계: 예비심사 결과 대기 (5월 중)
- 프로토타입 뷰어: http://127.0.0.1:3300/docs/prototypes/
- 회고 문서: [docs/00-plans/2026-retrospective.md](docs/00-plans/2026-retrospective.md)
- Phase 2 개발 계획 (예비심사 통과 시): [docs/00-plans/2026-phase2-dev-plan.md](docs/00-plans/2026-phase2-dev-plan.md)
