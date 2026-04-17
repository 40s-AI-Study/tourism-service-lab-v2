---
type: idea
id: tourismcareer-korea
title: "TourismCareer Korea - 관광 취업·인턴십 + 지역 현장 탐방 앱"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:10:00Z
status: draft
llm_compatibility: universal
round: 2
apis_used:
  - tourism-jobs
  - tourism-info-korean
  - central-attractions-by-municipality
  - area-tourism-demand-density
  - tourism-big-data
  - related-attractions
api_count: 6
target_users:
  - 20-30대 관광학과 재학생·졸업생
  - 관광 산업 취업 준비생
  - 지역 관광 스타트업 관심자
---

# TourismCareer Korea - 관광 취업·인턴십 + 지역 현장 탐방 앱

## 서비스 개요

관광학과 학생·취업 준비생이 **구직 활동과 현장 탐방을 동시에** 할 수 있는 플랫폼. 관광인 채용 공고(`tourism-jobs`)를 탐색하면서 해당 채용 기업의 지역 관광 현황을 빅데이터로 이해하고, 현장 방문까지 연결. "내가 일할 지역의 관광 수요를 미리 파악한다."

## 핵심 문제 (Pain Point)

- 관광산업 취업 정보가 분산 (사람인, 잡코리아, 관광공사 개별 채용 페이지)
- 지역 관광 기업에 취업 시 "이 지역 관광 시장이 어떤지" 파악할 데이터 없음
- 취업 준비생이 현장 탐방 없이 서류만으로 지원 → 직무 미스매치 높음
- 관광 빅데이터 역량 요구 증가하나 실제 데이터를 접할 기회 없음

## 핵심 기능

### 1. 관광인 채용 공고 큐레이션
- `tourism-jobs` API: 한국관광공사 공식 관광 산업 채용 정보
- 직무별 필터: 가이드, 호텔, 여행사, 관광 스타트업, 공공기관
- 지역별 채용 공고 지도 표시

### 2. 채용 지역 관광 수요 분석
- `area-tourism-demand-density` API: 채용 기업 소재 지역의 관광 체류·소비 강도
- `tourism-big-data` API: 이동통신·신용카드 기반 지역 관광 실태 데이터
- "이 기업이 위치한 지역의 관광 수요는 상위 X% 입니다" → 취업 결정 근거

### 3. 현장 탐방 코스 생성
- `central-attractions-by-municipality` API: 채용 기업 지역의 중심 관광지 100위
- `related-attractions` API: 중심 관광지 기반 연관 관광지 추천
- 취업 전 "이 지역 관광 생태계를 몸으로 이해하는" 현장 답사 코스

### 4. 관광 국문 정보 학습 모드
- `tourism-info-korean` API: 관광지 공식 정보를 취업 준비 콘텐츠로 재활용
- 관광 해설사 자격증 준비용 관광지 퀴즈 기능

## 사용자 여정

```
채용 공고 검색 → 기업 지역 분석 → 현장 탐방 계획 → 답사 실행
      ↓                ↓                  ↓               ↓
 tourism-jobs   area-tourism-demand   central-attractions  related-attractions
                tourism-big-data      tourism-info-korean
```

## API 활용 요약

| API | 활용 방법 |
|---|---|
| `tourism-jobs` | 관광 산업 채용 공고 (핵심, Round 1 완전 미활용) |
| `tourism-info-korean` | 관광지 공식 정보 + 학습 콘텐츠 |
| `central-attractions-by-municipality` | 채용 지역 중심 관광지 현장 답사 |
| `area-tourism-demand-density` | 채용 지역 관광 수요·소비 강도 분석 |
| `tourism-big-data` | 지역 관광 실태 빅데이터 (취업 시장 분석) |
| `related-attractions` | 현장 탐방 연관 관광지 코스 |

## 차별화 포인트

- **`tourism-jobs` API 단독 특화**: Round 1·공모전 출품작 중 활용 사례 거의 없을 것
- 관광 취업 + 지역 탐방을 **처음으로 연결**한 서비스 개념
- B2B 확장 가능: 관광학과 대학교 × 지역 관광 기업 매칭 플랫폼

## 공모전 배점 전략

- **데이터 활용(20점)**: `tourism-jobs` 단독 활용으로 심사위원 주목도 ↑
- **기획력(30점)**: 취업-현장-데이터 3축 연결 → 독창적 기획
- **사회적 가치**: 청년 관광 취업난 해소 + 지역 관광 산업 인력 공급 기여
