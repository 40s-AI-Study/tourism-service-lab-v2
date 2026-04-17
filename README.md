# Tourism Service Lab

> 2026 관광데이터 활용 공모전(웹·앱 개발) 준비를 위한 AI 다중 에이전트 자율 기획 프로젝트

## 프로젝트 개요

한국관광공사(KTO) Visit Korea Open API를 활용한 관광 서비스 기획을 **AI 에이전트 팀**이 자율적으로 수행합니다. 시장 조사부터 페르소나 정의, 아이디어 발산, 시뮬레이션 검증, 최종 기획서 작성까지 전 과정을 Paperclip 기반 멀티 에이전트가 협업합니다.

## 목표

- **공모전**: 2026 관광데이터 활용 공모전 (웹·앱 개발)
- **타겟 사용자**: 20-40대 한국인 + 외국인 (양측 모두 사용 가능한 서비스)
- **활용 데이터**: Visit Korea Open API (https://api.visitkorea.or.kr)
- **산출물**: 실제 공모전 제출 가능한 수준의 서비스 기획안

## AI 스터디 목적

이 프로젝트는 **AI 자율 기획 역량 검증**을 위한 스터디입니다. 모든 프롬프트, 계획, 의사결정, 에이전트 산출물, 세션 로그를 **전체 추적 가능한 형태**로 GitHub에 기록합니다.

## 레포 구조

```
tourism-service-lab-v2/
├── README.md                    # 이 파일
├── docs/
│   ├── 00-plans/                # 전체 실행 계획 (버전별)
│   ├── 01-decisions/            # Architecture Decision Records (ADR)
│   ├── 02-prompts/              # 사용자 프롬프트 히스토리
│   ├── 03-agent-outputs/        # 에이전트 산출물
│   └── 04-session-logs/         # Claude Code + Paperclip 세션 로그
├── knowledge-base/              # llm-wiki 미러 (지식 저장소)
│   ├── competition/             # 공모전 정보
│   ├── tourism-api/             # Visit Korea API 스펙
│   ├── market-research/         # 시장 조사
│   ├── personas/                # 사용자 페르소나
│   ├── ideas/                   # 서비스 아이디어
│   ├── simulations/             # 시뮬레이션 결과
│   └── business/                # 사업성 분석
├── company-config/              # Paperclip 회사 설정 스냅샷
├── deliverables/                # 최종 공모 제출물
└── scripts/                     # 자동화 스크립트
```

## 팀 구성 (예정)

| 역할 | 어댑터 | 주 업무 |
|---|---|---|
| CEO | claude_local (Opus) | 전략 오케스트레이션 |
| ProductManager | claude_local (Sonnet) | 서비스 기획, 기능 정의 |
| MarketResearcher | claude_local (Sonnet) | 관광 트렌드, 니즈 분석 |
| UXDesigner | claude_local (Sonnet) | 페르소나, 사용자 여정 |
| BusinessAnalyst | claude_local (Sonnet) | 사업성, 수익 모델 |
| APISpecialist | opencode_local (local LLM) | API 활용 검증 |
| Simulator | claude_local (Sonnet) | 페르소나별 시뮬레이션 |

## 실행 단계

1. **Phase 0**: GitHub 인프라 구축 ✅ (진행 중)
2. **Phase 1**: 지식베이스 구축 (공모전 PDF + API 스펙 수집)
3. **Phase 2**: Paperclip 회사 창립
4. **Phase 3**: 에이전트 자율 실행 (7-10일)

## 관련 링크

- **공모전**: https://api.visitkorea.or.kr
- **API 목록**: https://api.visitkorea.or.kr/#/useUtilExercises
- **GitHub Project**: https://github.com/users/sinrim11/projects/2/views/1
- **GitHub Wiki**: docs/wiki/

## 커밋 규칙

- `feat:` 신규 기능/콘텐츠
- `docs:` 문서 작업
- `research:` 리서치 결과
- `simulate:` 시뮬레이션 결과
- `design:` 디자인 산출물
- `fix:` 수정
- `[AgentName]` prefix: 에이전트가 커밋한 경우

모든 AI 에이전트 커밋에는 `Co-Authored-By: Paperclip <noreply@paperclip.ing>` 추가.

## 상태

- 시작일: 2026-04-17
- 현재 단계: Phase 0 (GitHub 인프라 구축)
