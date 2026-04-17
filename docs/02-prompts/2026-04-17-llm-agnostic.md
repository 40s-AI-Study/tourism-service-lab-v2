---
type: user-prompt
date: 2026-04-17
session: tourism-service-lab-kickoff
sequence: 3
summary: LLM 중립 설계 요구 (GPT/Claude/로컬 모두 호환)
---

# 사용자 프롬프트 #3 — LLM 중립 설계

## 원문

> 그리고 추후에 paperclip 의 운영은 주로 openai 모델인 gpt 모델이나 로컬 llm 으로 하고 부분적으로 중요한 부분은 claude 도 사용할 계획입니다. 즉 llm-wiki 및 지침들을 특정 llm 모델 claude 에만 국한되지 않고 chatgpt, 로컬llm (opencode) 등에서도 사용할 수 있도록 해주세요.

## 핵심 요청 정리

1. **장기 운영 모델**: OpenAI GPT + 로컬 LLM (opencode) 중심
2. **부분 사용**: Claude (중요한 부분만)
3. **설계 원칙**: 모든 llm-wiki / 지침 / 프롬프트가 **특정 LLM에 종속되지 않을 것**
4. **호환 대상**: ChatGPT, 로컬 LLM (opencode), Claude 모두

## 영향 범위

- llm-wiki 페이지 포맷 표준화
- AGENTS.md 템플릿 중립화
- 프롬프트 스타일 표준화 (XML 태그 등 모델 전용 기능 배제)
- 산출물 메타데이터 공통 스키마 정의

## 응답 (Claude)

v3 계획 작성 → [v3-plan.md](../00-plans/2026-04-17-v3-plan.md)

추가사항:
- Markdown + 표준 frontmatter 기반 지식베이스
- LLM-agnostic AGENTS.md 템플릿
- 공통 산출물 JSON 스키마
- 팀 구성 옵션 A/B/C (GPT 중심 / 혼합 / 전부 로컬)
- OpenAI API 연동 준비 (Phase 0-7)
