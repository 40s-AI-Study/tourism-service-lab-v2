---
type: idea
id: tastedata-korea
title: "TasteData Korea - 빅데이터 기반 로컬 미식 여행 큐레이터"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:20:00Z
status: final
llm_compatibility: universal
round: 2
apis_used:
  - tourism-big-data
  - area-tourism-demand-density
  - area-tourism-resource-demand
  - tourism-info-korean
  - tourism-info-english
  - tourism-info-japanese
  - related-attractions
  - tourism-photos
api_count: 8
target_users:
  - 30-40대 미식 여행자 (국내·외국인)
  - "진짜 로컬 맛집"을 찾는 MZ 세대
  - 일본인 관광객 (한식 체험 1순위)
  - 음식 콘텐츠 크리에이터
---

# TasteData Korea - 빅데이터 기반 로컬 미식 여행 큐레이터

## 서비스 개요

신용카드·이동통신 빅데이터를 기반으로 **"진짜 현지인이 가는 맛집 지역"**을 발굴하는 미식 여행 앱. 광고 블로그와 협찬 리뷰에 지친 여행자에게 데이터가 보증하는 로컬 미식 정보를 제공. 방한 목적 1-2위인 한식 체험(일본 관광객 최고 선호)을 데이터 드리븐으로 연결.

## 핵심 문제 (Pain Point)

- 맛집 블로그 80%+ 광고성 → "진짜 현지인 맛집" 신뢰 불가
- 관광지 주변 식당은 관광객 가격, 내국인은 골목 안 로컬 식당 선호
- 지역 특산 음식이 어느 지역에서 가장 활성화되어 있는지 데이터 없음
- 일본인 관광객은 한식을 가장 좋아하지만 맛집 정보를 일본어로 접근 어려움

## 핵심 기능

### 1. 빅데이터 기반 로컬 소비 지역 발굴
- `tourism-big-data` API: 신용카드 소비 데이터 → 현지인 실제 소비 집중 지역 분석
- `area-tourism-demand-density` API: 소비 강도 기반 미식 핫스팟 지역 히트맵
- `area-tourism-resource-demand` API: 음식 서비스 자원 수요 → 공급보다 수요가 높은 숨은 미식 지역

### 2. 지역 특산 음식 + 관광 코스 연결
- `tourism-info-korean` / `tourism-info-english` / `tourism-info-japanese`: 지역별 음식 관광지 정보
- `related-attractions` API: 맛집 지역 기반 연관 관광지·카페·시장 연결
- 음식 테마별 코스: 전통 한정식·길거리 음식·파인다이닝·지역 특산물

### 3. 미식 포토 큐레이션
- `tourism-photos` API: 지역 음식 관련 공식 관광 사진
- 음식 촬영 포토 스팟 연동 (음식 + 장소 인증샷 문화)
- "이 지역 대표 음식 비주얼" 갤러리

### 4. 다국어 미식 가이드
- 일본어 특화 한식 용어 사전 + 발음 가이드 내장
- 알레르기·할랄 필터 적용 (동남아·이슬람 방문자 대응)
- 계절별 제철 음식 추천 기능

## 사용자 여정

```
지역 선택 → 소비 데이터 기반 맛집 지역 확인 → 음식 코스 생성 → 포토 촬영
     ↓                   ↓                          ↓              ↓
tourism-info     tourism-big-data            related-attractions  tourism-photos
                 demand-density
                 resource-demand
```

## API 활용 요약

| API | 활용 방법 |
|---|---|
| `tourism-big-data` | 신용카드·이동통신 데이터 → 로컬 소비 지역 발굴 |
| `area-tourism-demand-density` | 소비 강도 히트맵 → 미식 핫스팟 |
| `area-tourism-resource-demand` | 음식 자원 수요 분석 → 숨은 미식 지역 (Round 1 미활용) |
| `tourism-info-korean` | 지역 음식 관광 정보 국문 |
| `tourism-info-english` | 영어권 방문자 안내 |
| `tourism-info-japanese` | 한식 체험 1순위 일본 방문자 안내 |
| `related-attractions` | 맛집 지역 연관 관광·카페·시장 |
| `tourism-photos` | 음식·지역 비주얼 큐레이션 |

## 차별화 포인트

- **광고 없는 맛집**: 신용카드 실소비 데이터 기반 → 광고성 블로그 대체 가치
- `area-tourism-resource-demand` 활용: Round 1 미활용, 음식 서비스 수요 분석에 신선한 활용
- 방한 목적 상위인 "한식 체험" 직접 공략
- 음식 크리에이터·유튜버 협업 채널로 바이럴 가능

## 공모전 배점 전략

- **데이터 활용(20점)**: 빅데이터 3종 + 다국어 3종 + 포토·연관 API = 8개
- **기획력(30점)**: "광고 없는 데이터 기반 맛집" → 시대적 Pain Point 직결
- **지역 가점**: 전주(한식), 부산(해산물), 전남(남도음식) 지역 특화 가능
