---
type: idea
id: photohunt-korea
title: "PhotoHunt Korea - AI 포토 스팟 큐레이터 & 포토 투어 앱"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:10:00Z
status: final
llm_compatibility: universal
round: 2
apis_used:
  - tourism-photos
  - photo-contest-winners
  - visitor-concentration-forecast
  - tourism-info-korean
  - tourism-info-english
  - area-tourism-diversity
  - related-attractions
api_count: 7
target_users:
  - 20-30대 사진 취미 여행자 (인스타그래머, 포토그래퍼)
  - 외국인 관광객 (사진 여행 목적)
  - 사진 작가 지망생
---

# PhotoHunt Korea - AI 포토 스팟 큐레이터 & 포토 투어 앱

## 서비스 개요

한국관광공사 공식 관광 사진 DB와 공모전 수상작을 기반으로 **검증된 포토 스팟**을 AI가 큐레이션하는 앱. 인스타 감성 MZ 여행자의 "어디서 찍어야 예쁘게 나오지?" 고민을 해결. 혼잡도 예측으로 "골든 타임" 촬영 시점까지 안내.

## Round 1과의 차별화

- **Audio Story Korea**: 오디오 스토리텔링 중심
- **PhotoHunt Korea**: `tourism-photos`(일반 관광사진) + `photo-contest-winners`(수상작) 두 포토 API 동시 활용으로 포토 큐레이션에 집중. `visitor-concentration-forecast`로 "덜 붐비는 골든 타임" 촬영 최적화

## 핵심 문제 (Pain Point)

- 유명 포토 스팟은 SNS에서 발견하지만 **혼잡도가 높아 원하는 사진 불가**
- 공식 관광 사진 DB(`tourism-photos`)는 존재하지만 접근성 낮고 앱으로 없음
- 공모전 수상작처럼 **촬영 각도·계절·시간대** 정보 없음
- 20대 여행 결정 트리거 1위: SNS 발견(61%) → 사진 중심 서비스 수요 명확

## 핵심 기능

### 1. 공식 포토 DB 큐레이션
- `tourism-photos` API: 한국관광공사 공식 관광지 고화질 사진 전체 DB
- `photo-contest-winners` API: 공모전 수상작 (제목·촬영일·촬영지·키워드 포함)
- 두 데이터 통합 → "공식 인증 포토 스팟" 지도 생성

### 2. 골든 타임 촬영 알림
- `visitor-concentration-forecast` API: 포토 스팟의 향후 30일 방문자 집중률 예측
- "이번 주 수요일 오전 7시 방문자 20% → 골든 타임!"
- 계절별 빛·날씨 기반 촬영 최적 시간대 추천

### 3. 포토 투어 코스 생성
- `related-attractions` API: 포토 스팟 A에서 함께 방문하는 스팟 B, C 자동 연결
- `area-tourism-diversity` API: 지역 관광 다양성 → 한 지역에서 다양한 촬영 주제 가능성 평가
- 테마별 포토 투어: 건축/자연/음식/야경/사람 5개 카테고리

### 4. 다국어 포토 스팟 공유
- `tourism-info-korean` / `tourism-info-english`: 포토 스팟 상세 정보 이중 언어
- SNS 공유 최적화: 위치·태그·해시태그 자동 생성

## 사용자 여정

```
포토 스팟 탐색 → 골든 타임 확인 → 포토 투어 코스 생성 → 현장 촬영 → SNS 공유
      ↓                ↓                    ↓
 tourism-photos   visitor-concentration  related-attractions
 photo-contest    -forecast             area-tourism-diversity
```

## API 활용 요약

| API | 활용 방법 |
|---|---|
| `tourism-photos` | 공식 관광지 사진 DB → 포토 스팟 지도 (Round 1 미활용) |
| `photo-contest-winners` | 수상작 촬영지 정보 → 검증된 명소 |
| `visitor-concentration-forecast` | 혼잡도 예측 → 골든 타임 촬영 안내 |
| `tourism-info-korean` | 포토 스팟 국문 상세 정보 |
| `tourism-info-english` | 외국인 포토그래퍼 영문 안내 |
| `area-tourism-diversity` | 지역 촬영 주제 다양성 평가 |
| `related-attractions` | 포토 스팟 연계 투어 코스 |

## 차별화 포인트

- `tourism-photos` API: **Round 1 미활용**, 공모전 출품작 중 포토 특화 앱 희소
- "공식 사진 DB × 혼잡도 예측 × AI 코스" 3중 결합은 전 세계 어디에도 없는 조합
- 20대 인스타그래머(74% 인스타 사용) → 가장 큰 잠재 사용자 그룹 직접 공략

## 공모전 배점 전략

- **데이터 활용(20점)**: `tourism-photos` + `photo-contest-winners` 포토 API 2개 동시 활용 차별화
- **기획력(30점)**: MZ 여행 트렌드(포토스팟) × 실시간 혼잡도 해소 → 명확한 Pain Point 해결
- **시각적 완성도**: 사진 중심 앱 → 시연 데모 임팩트 높음
