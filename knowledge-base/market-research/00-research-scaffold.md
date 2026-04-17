---
type: research-scaffold
id: market-research-scaffold
title: 기초 시장 조사 스캐폴드
created: 2026-04-17
author_agent: claude-code
author_model: claude-opus-4-7
category: research
status: scaffold
llm_compatibility: universal
---

# 기초 시장 조사 스캐폴드

> **이 파일은 뼈대 문서입니다.** 상세 리서치는 Phase 3 Stage 1에서 `MarketResearcher` 에이전트가 수행합니다.

## 리서치 영역 (5개)

### 1. 한국 관광 트렌드 통계 (2024-2025)
- 국내 관광 총 인구/횟수
- 인바운드 관광객 통계 (국가별, 월별)
- 연령대별 관광 빈도
- **20-40대 집중 데이터**

**조사 대상 출처**:
- 한국관광공사 관광지식정보시스템 (tour.go.kr)
- 통계청 (KOSIS)
- 한국문화관광연구원
- `tourism-big-data` API (우리 데이터)

### 2. 20-40대 관광 선호도
- 연령대별 차이: 20대 / 30대 / 40대
- 여행 형태: 솔로 / 커플 / 가족 / 친구그룹
- 선호 테마: 자연, 도시, 문화, 체험, 미식, 웰니스, 쇼핑
- 예산 범위
- 정보 탐색 채널 (인스타, 유튜브, 블로그, 앱 등)

**조사 방법**:
- 블로그/커뮤니티 크롤링 (네이버 블로그, 디시, 더쿠)
- 인스타그램 해시태그 분석 (#국내여행, #혼자여행)
- 설문조사 결과 (한국관광공사 발간 자료)

### 3. 외국인 관광객 특성
- 국가별 점유율 (중국, 일본, 동남아, 미주, 유럽)
- 체류 기간
- 주요 방문지
- 정보 탐색 (Google Maps, Tripadvisor, 자국 블로그)
- 언어/결제 pain point

**조사 대상 출처**:
- Visit Korea (영문) 공식 통계
- Reddit r/korea, r/travel, r/koreatravel
- Tripadvisor, Klook 리뷰
- 자국어 블로그 (JP/CN/EN)

### 4. 기존 관광 서비스 분석 (기능 매트릭스)

| 서비스 | 타겟 | 핵심 기능 | 한계 |
|---|---|---|---|
| Visit Korea 공식 | 외국인 | 다국어 가이드 | UI 구식, 개인화 없음 |
| 트리플 (Triple) | 국내 20-30대 | 코스 공유, 타임라인 | 실시간 데이터 부족 |
| 야놀자 | 국내 전 연령 | 숙박 중심 | 예약 외 기능 약함 |
| 여기어때 | 국내 | 숙박 + 레저 | 콘텐츠 부족 |
| 마이리얼트립 | 국내 + 해외 | 투어/액티비티 중개 | 예약 중심 |
| Google Maps | 글로벌 | 네비 + 리뷰 | 한국 특화 부족 |
| Tripadvisor | 글로벌 | 리뷰 | 한국 콘텐츠 부족 |
| Klook | 아시아 | 액티비티 예약 | 현지 정보 약함 |

*(Phase 3 Stage 1에서 각 서비스 실사용 평가 + 상세 기능 추가)*

### 5. 경쟁 Gap 분석

**현재 기존 서비스가 커버 못 하는 영역**:
- ⚠️ 실시간 혼잡도 (visitor-concentration-forecast 활용 가능 영역)
- ⚠️ 다국어 통합 (대부분 국문 중심)
- ⚠️ 연관 코스 자동 생성 (related-attractions 활용 가능)
- ⚠️ 테마 특화 (웰니스/펫/무장애/에코) 전용 앱 부재
- ⚠️ AI 기반 개인화 (트렌드 기반 추천)
- ⚠️ 지역 특화 서비스 (RTO 특별상 기회)
- ⚠️ 외국인 전용 통합 플랫폼 (9개 언어 통합)

## Phase 3 Stage 1 실행 시 MarketResearcher 지시사항

### 입력
- 이 스캐폴드 문서
- Visit Korea API 카탈로그 (`00-api-catalog.md`)
- 공모전 개요 (`competition/overview.md`)

### 출력 (필수 산출물 5개)

1. `tourism-trends-2025.md` — 한국 관광 최신 통계
2. `existing-apps-matrix.md` — 경쟁 앱 상세 기능 비교
3. `competitive-gaps.md` — Gap 분석 + 기회 영역
4. `foreign-tourist-needs.md` — 외국인 관광객 니즈
5. `korean-20-40-personas-input.md` — 20-40대 니즈 raw data (UXDesigner 입력용)

### 제약
- 모든 출처 URL 명시 (신뢰성 추적)
- 자동 추정/환각 금지 — 확인된 데이터만
- 외국인 데이터는 외국어 소스 원문 인용

### 산출물 메타데이터 (ADR-002 준수)
각 MD 파일에 frontmatter 필수:
```yaml
---
type: research
id: {slug}
author_agent: market-researcher
author_model: gpt-4o-mini
created: ...
sources: [url1, url2, ...]
---
```

## 진행 상태

- 2026-04-17: 스캐폴드 작성 완료
- Phase 3 Stage 1에서 MarketResearcher가 이 문서 기반 리서치 수행 예정
