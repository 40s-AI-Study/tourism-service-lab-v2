---
type: idea
id: k-beautymed-tour
title: "K-BeautyMed Tour - K뷰티·성형 의료관광 외국인 특화 앱"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:20:00Z
status: draft
llm_compatibility: universal
round: 2
apis_used:
  - medical-tourism
  - tourism-info-chinese-simplified
  - tourism-info-japanese
  - tourism-info-english
  - area-tourism-demand-density
  - related-attractions
  - tourism-photos
  - visitor-concentration-forecast
api_count: 8
target_users:
  - 20-40대 중국·일본·동남아 여성 관광객
  - K-뷰티 성지순례 + 성형·피부 시술 목적 방문자
  - 의료관광 + 쇼핑 복합 방문자
---

# K-BeautyMed Tour - K뷰티·성형 의료관광 외국인 특화 앱

## 서비스 개요

K-뷰티·성형·피부과 시술 목적으로 방한하는 아시아 여성 관광객을 위한 특화 앱. `MediTrip Korea`가 일반 의료관광(검진·치과·척추 등)을 다룬다면, **K-BeautyMed Tour는 성형·피부·뷰티 쇼핑의 시너지 여정**에 집중. 강남 뷰티벨트(강남역~청담동~압구정)를 중심으로 시술 전후 K-뷰티 쇼핑·촬영 여정을 원스톱 안내.

## MediTrip Korea와의 차별화

| 구분 | MediTrip Korea | K-BeautyMed Tour |
|---|---|---|
| 타겟 | 의료관광 일반 (검진·치과·척추) | 뷰티·성형·피부 특화 |
| 주요 국가 | 중·일·영어권 (광범위) | 중국·일본·동남아 여성 집중 |
| 핵심 연계 | 치료 + 주변 관광 | 시술 + 올리브영 + 포토스팟 |
| API 구성 | 번체 포함, demand-density | visitor-forecast, tourism-photos 추가 |

## 핵심 문제 (Pain Point)

- 강남 피부과·성형외과 정보는 중국어(간체) 외에 동남아 영어권 정보 없음
- 시술 후 붓기 기간 중 "가벼운 쇼핑·관광"을 위한 코스 안내 없음
- 올리브영 투어, 화장품 쇼핑 + 피부과 일정을 통합한 앱 전무
- K-뷰티 관련 포토스팟(성수동 팝업, 압구정 명품 거리) 정보 분산

## 핵심 기능

### 1. K-뷰티 의료관광 병원 큐레이션
- `medical-tourism` API: 피부과·성형외과·한방 미용 클리닉 공식 인증 목록
- 시술 유형별 필터: 피부(레이저/보톡스), 성형(코·눈), 한방 미용
- `tourism-info-chinese-simplified` / `tourism-info-japanese` / `tourism-info-english`: 3개 언어 안내

### 2. 시술 후 붓기 단계별 활동 추천
- `related-attractions` API: 병원 주변 연관 관광지 (붓기 상태별 활동 강도 태그)
  - D+0~1 (실내 쇼핑): 백화점·올리브영
  - D+2~3 (야외 가능): 한강공원·경복궁
  - D+5+ (일반 관광): 전일 코스
- `visitor-concentration-forecast` API: 혼잡도 낮은 쇼핑·관광 시간대 추천

### 3. K-뷰티 쇼핑 + 포토스팟 코스
- `tourism-photos` API: K-뷰티 관련 포토스팟 고화질 사진 큐레이션
- `area-tourism-demand-density` API: 강남·홍대·성수 등 뷰티 핫플 소비 강도 분석
- 올리브영·시코르·뷰티 팝업 위치 연동 (외부 데이터 결합)

### 4. 비용·예약 준비 가이드
- 예상 시술 비용 범위 + 공식 의료관광 기관 연결
- 국가별 통관 제한 화장품 가이드 내장

## API 활용 요약

| API | 활용 방법 |
|---|---|
| `medical-tourism` | 공식 인증 뷰티·성형 클리닉 목록 |
| `tourism-info-chinese-simplified` | 중국 본토 방문자 안내 |
| `tourism-info-japanese` | 일본 방문자 안내 |
| `tourism-info-english` | 동남아·영어권 방문자 공용 |
| `area-tourism-demand-density` | 뷰티 핫플 소비 강도 분석 |
| `related-attractions` | 시술 후 붓기 단계별 주변 활동 추천 |
| `tourism-photos` | K-뷰티 포토스팟 사진 큐레이션 |
| `visitor-concentration-forecast` | 혼잡도 낮은 쇼핑·관광 타이밍 |

## 차별화 포인트

- K-뷰티 + 의료관광 + 쇼핑의 **최초 통합 여정 앱**
- `tourism-photos` + `visitor-concentration-forecast` 조합: 포토스팟에서 덜 붐비는 시간 방문
- 방한 중국 여성 관광객 1순위 목적 "K-뷰티 쇼핑"과 직결
- 인스타그램 성지 "뷰티 인증샷" 문화와 완전히 부합

## 공모전 배점 전략

- **데이터 활용(20점)**: 8개 API, medical-tourism 특화 활용
- **기획력(30점)**: K-뷰티 글로벌 트렌드 × 의료관광 시장 × 명확한 타겟
- **비즈니스 모델**: 병원 제휴 수수료 + 쇼핑몰 제휴 → 공모전 심사 설득력
