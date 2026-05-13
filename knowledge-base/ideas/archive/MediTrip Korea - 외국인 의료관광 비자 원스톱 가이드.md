---
type: idea
id: meditrip-korea
title: "MediTrip Korea - 외국인 의료관광 비자 원스톱 가이드"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:00:00Z
status: final
llm_compatibility: universal
round: 2
apis_used:
  - medical-tourism
  - tourism-info-chinese-simplified
  - tourism-info-chinese-traditional
  - tourism-info-japanese
  - tourism-info-english
  - related-attractions
  - area-tourism-demand-density
  - tourism-photos
api_count: 8
target_users:
  - 외국인 의료관광객 (중국/일본/동남아/영어권)
  - 20-50대 해외 방문객
---

# MediTrip Korea - 외국인 의료관광 비자 원스톱 가이드

## 서비스 개요

한국 의료관광 비자(Medical Tourism Visa) 취득부터 병원 예약, 치료 후 관광까지 전 여정을 지원하는 외국인 전용 원스톱 플랫폼. 2024년 방한 의료관광객 약 60만명(한국보건산업진흥원 추정) 시장을 정조준.

## 핵심 문제 (Pain Point)

- 의료관광 정보가 병원 사이트, 비자 안내, 숙박, 관광 정보로 **분산**되어 있음
- 중국·일본 방문자는 모국어 의료 정보 탐색이 불가능
- 치료 대기 기간 중 주변 관광지 안내 없음 → 체류 만족도 저하

## 핵심 기능

### 1. 의료관광 정보 허브
- `medical-tourism` API: 공식 인증 의료관광 병원·클리닉 목록
- 진료과별 필터: 성형/피부과, 치과, 척추, 한방, 검진
- 다국어 병원 안내 (`tourism-info-chinese-simplified`, `tourism-info-chinese-traditional`, `tourism-info-japanese`, `tourism-info-english`)

### 2. 치료 전·후 관광 코스 연동
- `related-attractions` API: 병원 주변 연관 관광지 자동 추천
- 대기일수 기반 관광 코스 생성 (예: 시술 후 회복 3일 = 경복궁 + 북촌 + 인사동 힐링 코스)
- `area-tourism-demand-density` API: 병원 밀집 지역(강남/신촌) 주변 수요 강도 기반 혼잡 회피

### 3. 비주얼 목적지 큐레이션
- `tourism-photos` API: 치료 후 방문 관광지 고화질 사진 미리 보기
- 회복 난이도별 관광지 분류 (안정 필요/가벼운 산책/활동적)

### 4. 다국어 의료 용어 가이드
- 4개 언어 병원 방문 필수 회화 내장
- 보험 처리·비자 서류 체크리스트 제공

## 사용자 여정

```
비자 신청 안내 → 병원 선택 (언어별) → 관광 코스 예약
    ↓                   ↓                    ↓
medical-tourism     i18n APIs           related-attractions
                                        tourism-photos
```

## API 활용 요약

| API | 활용 방법 |
|---|---|
| `medical-tourism` | 공식 인증 의료관광 병원 목록 + 상세 정보 |
| `tourism-info-chinese-simplified` | 중국 본토 방문자 다국어 관광 정보 |
| `tourism-info-chinese-traditional` | 대만/홍콩 방문자 다국어 관광 정보 |
| `tourism-info-japanese` | 일본 방문자 다국어 관광 정보 |
| `tourism-info-english` | 영어권 + 동남아 방문자 공용 정보 |
| `related-attractions` | 병원 주변 연관 관광지 추천 |
| `area-tourism-demand-density` | 지역 수요 강도 기반 혼잡 회피 |
| `tourism-photos` | 관광지 비주얼 미리 보기 |

## 차별화 포인트

- **Round 1 공백**: 의료관광 특화 앱 전무
- 공식 인증 병원 데이터(`medical-tourism`) + 관광 정보 **최초 통합**
- 치료 대기 기간을 '추가 여행'으로 전환하는 수익 모델 가능성
- 공모전 사회적 가치: 한국 의료관광 산업 활성화 기여

## 공모전 배점 전략

- **데이터 활용(20점)**: 8개 API 조합 → 고득점 기대
- **기획력(30점)**: 비자~치료~관광 통합 여정 → 명확한 사용자 가치
- **지역 가점**: 강남구(성형/피부) 또는 서울 의료특구 지정 지역
