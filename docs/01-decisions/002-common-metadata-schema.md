---
type: decision
number: 002
date: 2026-04-17
status: accepted
title: 공통 산출물 메타데이터 JSON 스키마
---

# ADR-002: 공통 산출물 메타데이터 스키마

## Context

에이전트가 생성하는 모든 산출물(아이디어, 페르소나, 시뮬레이션, 분석 등)은 **어떤 LLM이 어떤 시점에 만들었는지 추적** 가능해야 한다. 특히 AI 스터디 목적상 모델별 품질 비교가 필요하다.

## Decision

모든 산출물에 **공통 메타데이터 헤더**를 적용한다.

## Markdown Frontmatter 스키마

모든 `.md` 파일 상단에 YAML frontmatter:

```yaml
---
# 필수
type: idea | persona | simulation | decision | research | api-spec | session-log
id: {slug-or-uuid}           # 파일 고유 ID
title: "{사람이 읽을 제목}"
created: 2026-04-17T15:30:00+09:00  # ISO 8601
author_agent: {agent-name}    # ceo, pm, market-researcher, ...
author_model: {model-id}      # gpt-4o, claude-opus-4-7, supergemma4-26b, ...

# 권장
category: competition | api | research | design | business | technical
tags: [tag1, tag2, tag3]
status: draft | in-review | approved | deprecated
llm_compatibility: universal | claude | gpt | local

# 선택 (타입별)
parent: {parent-file-slug}    # 연관 산출물
supersedes: {old-file-slug}   # 대체 대상
related: [slug1, slug2]       # 관련 문서
---
```

## 타입별 Content 스키마

### idea (서비스 아이디어)
```markdown
## 제목
한 문장 요약

## 대상 사용자
- 페르소나 ID 또는 설명

## 핵심 기능 (3-5개)
1. 기능 1
2. 기능 2

## 활용 API
- api-slug-1
- api-slug-2

## 차별화 포인트
...

## 예상 사업성 (1-10)
- 시장 규모: N
- 차별화: N
- 구현 난이도: N
- 총점: N
```

### persona
```markdown
## 이름, 나이, 직업
김민수, 28, 회사원

## 배경
...

## 목표 (Goals)
- ...

## 고민 (Pain Points)
- ...

## 관광 패턴
- 여행 빈도: N회/년
- 선호 유형: ...
- 정보 탐색: ...

## 기술 친숙도
low | medium | high
```

### simulation (시뮬레이션 결과)
```markdown
## 시나리오
- 서비스: {idea-id}
- 페르소나: {persona-id}
- 상황: ...

## 사용자 여정 단계별
1. 진입 → 행동 → 결과
2. ...

## 평가 (1-10)
- 유용성: N
- 사용 편의: N
- 구현 타당성: N
- 종합: N

## Pass/Fail
pass | fail

## 개선 제안
- ...
```

### api-spec
```markdown
## 기본 정보
- API 명: ...
- 공급처: 한국관광공사
- 인증: API key / OAuth
- Base URL: ...

## 엔드포인트 목록
| Path | Method | 용도 |
|------|--------|------|

## 요청 파라미터
| Name | Type | Required | Description |

## 응답 데이터
```json
{...}
```

## 활용 시나리오
- ...
```

## JSON (구조화된 데이터)

순수 JSON 파일이 필요한 경우 (`*.json`):
```json
{
  "schema_version": "1.0",
  "metadata": {
    "type": "...",
    "id": "...",
    "title": "...",
    "created": "2026-04-17T15:30:00+09:00",
    "author_agent": "...",
    "author_model": "...",
    "category": "...",
    "tags": [],
    "status": "..."
  },
  "content": {
    /* 타입별 구조 */
  }
}
```

## 파일명 규칙

`{type}/{YYYY-MM-DD}-{slug}.md`

예:
- `knowledge-base/ideas/2026-04-17-tourism-ar-guide.md`
- `knowledge-base/personas/2026-04-17-foreign-backpacker.md`
- `knowledge-base/simulations/2026-04-17-sim-001-ar-guide-x-backpacker.md`

## 검증

모든 에이전트는 산출물 생성 시:
1. frontmatter 포함
2. `author_agent`, `author_model` 정확히 기재
3. 파일명 규칙 준수

CI 스크립트 `scripts/validate-metadata.sh` 로 검증 예정 (Phase 0-5).

## Consequences

### 긍정
- 모든 산출물 추적 가능 (누가 언제 어떤 모델로)
- 모델별 품질 비교 가능 (AI 스터디 핵심 데이터)
- 버전 관리 용이 (supersedes 체인)

### 부정
- 에이전트 지침에 frontmatter 작성 로직 추가 필요
- 초기 작성 부담

## Status

- Proposed: 2026-04-17
- Accepted: 2026-04-17
