---
type: adr
id: adr-004-tripcraft-korea-final-submission
title: "ADR-004: TripCraft Korea — 최종 공모전 제출 서비스 결정"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-05-13T00:00:00Z
status: approved
llm_compatibility: universal
---

# ADR-004: TripCraft Korea — 최종 공모전 제출 서비스 결정

## 상태

`approved` — 공모전 제출 완료 (2026-05-06)

## 맥락

Round 1~7을 거쳐 59개 아이디어를 발산하고 150점 통합 매트릭스로 상위 10개를 확정했다. 최종 제출 단계(D-2, 2026-05-04)에서 초기 제출 후보였던 **KoreaPath AI** 단독 제출 대신 **4개 아이디어를 통합한 TripCraft Korea**를 최종 제출 서비스로 선택했다.

### 배경

| 항목 | 내용 |
|---|---|
| 초기 후보 | KoreaPath AI (2위, 119/150점) — 초기 제안서 초안 작성 완료 |
| 최종 결정 | TripCraft Korea (4개 아이디어 통합) |
| 결정일 | 2026-05-05 |
| 제출일 | 2026-05-06 16:00 |

## 결정

KoreaPath AI 단독 대신 **TripCraft Korea (4개 아이디어 통합)**를 제출한다.

### 통합 구성

| 소스 아이디어 | 핵심 기여 기능 |
|---|---|
| KoreaPath AI (2위, 119점) | 카테고리 테마 코스 자동 생성, 혼잡도 예측 |
| Audio Story Korea v2 (공동 5위) | 위치 기반 오디오 가이드 자동재생 |
| 아이디어 A+ (치유여정 류) | CLIP 유사도 대안 추천, 소외 지역 가중치 |
| 아이디어 B+ (LocalSecret 류) | 경비 자동 합산, 팔도 스탬프 리워드 |

## 근거

### 통합이 단독보다 나은 이유

1. **심사 기준 전체 커버**: 단독 아이디어는 특정 심사 항목에 강점이 편중됨. 통합을 통해 데이터 활용(20점)·기획력(30점)·완성도(30점)·발전성(20점) 전 항목 균형 달성.

2. **KTO 정책 정합성 강화**: 소외 지역 균형(LocalSecret 류) + 지역 특화 가점(+2점) 요건을 더 강하게 충족.

3. **API 활용도 극대화**: 단독 아이디어 대비 KTO OpenAPI 활용 종수가 12종으로 증가 (단독 최대 7~8종).

4. **차별성 강화**: 기존 서비스(트리플·야놀자·Klook)와 5개 축 이상 차별화 — 단독 아이디어로는 3개 축 차별화 한계.

5. **사회적 가치 서사**: 오버투어리즘 해소 + 소외 지역 균형 + 외국인 FIT 지원 3가지 사회적 가치를 하나의 플랫폼에서 설명 가능.

### LocalSecret v2(1위, 123점)를 선택하지 않은 이유

1위였으나 단독 제출 시 API 활용 종수 부족 (데이터 활용 배점 20점 리스크).
통합 서비스에 LocalSecret의 핵심 기능(혼잡도 역발상, 소외 지역 가중치)이 포함됨으로써 실질적으로 1위 아이디어의 강점을 흡수.

## 결과

- 제출 파일: `docs/deliverables/proposal-tripcraft/PROPOSAL_FINAL.pdf`
- PDF 최종 크기: 약 1.1MB (5페이지)
- 주요 기능: 6대 기능 × 7개 카테고리
- API 활용: KTO OpenAPI 12종 + 카카오 4종 = 16종

## 관련 문서

- [서비스 기획서](../deliverables/service-plan.md)
- [TripCraft Korea 통합 컨셉](../deliverables/proposal-tripcraft/01-unified-concept.md)
- [최종 랭킹](../../knowledge-base/business/round6-final-ranking.md)
- [ADR-003](./003-top3-idea-selection.md) — 이전 결정 (Stage 3 상위 3 선정)
