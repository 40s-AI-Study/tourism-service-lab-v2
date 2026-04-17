---
type: decision
number: 001
date: 2026-04-17
status: accepted
title: LLM-agnostic AGENTS.md 템플릿 채택
---

# ADR-001: LLM-agnostic AGENTS.md 템플릿

## Context

이 프로젝트는 여러 LLM 모델(OpenAI GPT, Claude, 로컬 LLM)을 교체 사용할 계획이다. 각 에이전트의 지침(AGENTS.md)이 특정 모델에 종속되면 모델 교체 시 재작성 비용이 크다.

## Decision

모든 에이전트 지침을 **LLM-agnostic 표준 템플릿**으로 작성한다. 모델별 최적화는 부록(optional)으로 분리.

## 표준 템플릿

```markdown
# {Agent Name}

## Role
{한 문장 명확한 역할 정의}

## Responsibilities
- 책임 1 (동사로 시작)
- 책임 2
- 책임 3

## Workflow
1. 입력: {무엇을 받는가}
2. 처리: {어떤 절차로 처리하는가}
3. 출력: {무엇을 생성하는가}

## Input Schema
{JSON 또는 Markdown 구조로 입력 형식 명시}

## Output Schema
{JSON 또는 Markdown 구조로 출력 형식 명시}

## Constraints
- 반드시 지켜야 할 제약 1
- 제약 2

## Tools Available
| Tool | Purpose | Usage |
|------|---------|-------|
| bash | shell 명령 | {예시} |
| read | 파일 읽기 | {예시} |
| write | 파일 쓰기 | {예시} |

## Success Criteria
- 기준 1 (측정 가능)
- 기준 2

## Error Handling
- 실패 시 행동 1
- 실패 시 행동 2

## Communication
- 다른 에이전트와의 상호작용 규칙
- GitHub Issue/Comment 사용 방법

## Model-Specific Notes (Optional)
### Claude 사용 시
{Claude 특화 팁}

### GPT 사용 시
{GPT 특화 팁}

### 로컬 LLM 사용 시
{로컬 LLM 제약사항}
```

## 원칙

### 필수
1. **순수 Markdown** — 특정 모델 전용 문법 금지
2. **명시적 Input/Output 스키마** — 모델이 바뀌어도 해석 가능
3. **Tool 사용법 예시** — 모호성 제거
4. **Success Criteria** — 자기 검증 가능

### 금지
1. **Claude 전용 XML 태그** (`<thinking>`, `<answer>` 등) 사용 금지
2. **GPT 전용 function calling 스키마** 가정 금지
3. **모델별 system message 관용구** 의존 금지 ("You are a helpful assistant that..." 류의 상투어 최소화)
4. **토큰 제한 가정** 금지 (context window는 모델마다 다름)

## 검증 방법

새 AGENTS.md 작성 후 다음 3가지 조합에서 테스트:
1. `claude_local` + Claude Sonnet/Opus
2. `opencode_local` + GPT-4o
3. `opencode_local` + 로컬 LLM (supergemma4-26b 등)

같은 입력에 대해 비슷한 수준의 출력이 나오면 LLM-agnostic 합격.

## Consequences

### 긍정
- 모델 교체 비용 최소화
- 비용 최적화 가능 (저렴한 모델로 전환)
- 지식 자산의 장기 재활용성

### 부정
- 초기 작성 시간 증가
- 모델별 최적화 포기 (약간의 품질 손실 가능)

## Status

- Proposed: 2026-04-17
- Accepted: 2026-04-17
- Review: 회사 창립 후 첫 heartbeat 결과 기반 재검토
