---
type: idea
id: eurokorea-gateway
title: "EuroKorea Gateway - 유럽어권 관광객 특화 다국어 허브"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T12:20:00Z
status: draft
llm_compatibility: universal
round: 2
apis_used:
  - tourism-info-russian
  - tourism-info-spanish
  - tourism-info-french
  - tourism-info-german
  - audio-guide
  - central-attractions-by-municipality
  - related-attractions
  - tourism-photos
api_count: 8
target_users:
  - 러시아어권 관광객 (러시아·CIS)
  - 스페인어권 관광객 (스페인·중남미)
  - 프랑스어권 관광객 (프랑스·벨기에·캐나다·아프리카)
  - 독일어권 관광객 (독일·오스트리아·스위스)
---

# EuroKorea Gateway - 유럽어권 관광객 특화 다국어 허브

## 서비스 개요

한국 관광 정보의 4개 유럽어(러시아·스페인·프랑스·독일) 진공지대를 메우는 앱. 방한 유럽 관광객은 체류 기간이 평균 7-8일로 가장 길고 1인 지출도 높지만, 모국어 관광 앱이 사실상 없음. **Round 1 및 경쟁 앱 모두 미활용한 4개 유럽어 API를 독점적으로 결합**.

## Round 1과의 차별화

- **K-Guide Global**: 영·일·중 위주, 유럽어 미포함
- **EuroKorea Gateway**: 러·스·프·독 4개 유럽어 API만으로 구성, 체류 기간이 긴 유럽 관광객의 심층 탐방 니즈에 특화

## 핵심 문제 (Pain Point)

- 유럽어권 관광객은 구글 번역으로 한국 관광 정보를 접근 → 오역·누락 빈번
- 영어를 선호하지 않는 러시아·프랑스·스페인어권 사용자 배제
- 장기 체류(7-8일) 여행자를 위한 심층 코스 없음
- 유럽인은 역사·문화·자연 관심 높지만 관련 콘텐츠 모국어 미제공

## 핵심 기능

### 1. 4개 언어 완전 현지화 인터페이스
- `tourism-info-russian` / `tourism-info-spanish` / `tourism-info-french` / `tourism-info-german`
- 입력 언어 자동 감지 → 해당 언어 DB 전환
- 유럽 공휴일 기준 여행 시즌 캘린더

### 2. 모국어 오디오 가이드
- `audio-guide` API: 한/영/중/일 음성 + 대본 제공 (스크립트 번역 연계)
- 현장에서 이어폰으로 듣는 역사·문화 해설 → 유럽인 선호 방식

### 3. 지역별 중심 명소 심층 탐방
- `central-attractions-by-municipality` API: 지역별 중심 관광지 100위 → 7박 여정 최적화
- `related-attractions` API: 관광지 간 연관성 데이터로 심층 탐방 코스 생성
- "서울 5일 + 부산 2일" 장기 체류 코스 자동 생성

### 4. 비주얼 목적지 갤러리
- `tourism-photos` API: 고화질 관광지 사진 → 유럽 여행자 사전 답사용
- 지역·테마·계절별 사진 필터

## API 활용 요약

| API | 활용 방법 |
|---|---|
| `tourism-info-russian` | 러시아·CIS 관광객 모국어 관광 정보 (Round 1 미활용) |
| `tourism-info-spanish` | 스페인·중남미 관광객 모국어 관광 정보 (Round 1 미활용) |
| `tourism-info-french` | 프랑스어권 관광객 모국어 관광 정보 (Round 1 미활용) |
| `tourism-info-german` | 독어권 관광객 모국어 관광 정보 (Round 1 미활용) |
| `audio-guide` | 현장 오디오 역사 해설 (유럽인 선호) |
| `central-attractions-by-municipality` | 지역 핵심 명소 → 장기 체류 코스 |
| `related-attractions` | 연관 관광지 심층 탐방 연결 |
| `tourism-photos` | 여행 전 비주얼 목적지 탐색 |

## 차별화 포인트

- **미개척 시장**: 한국 관광 앱의 유럽어 공백을 최초로 메움
- 4개 언어 API 동시 활용 → 공모전 데이터 활용도 최고점
- 장기 체류·고지출 유럽 관광객 → 관광 산업 고부가가치 세그먼트
- 유럽어 사용 인구: 러시아어 2.6억, 스페인어 5.9억, 프랑스어 3.5억, 독일어 1억+ → 잠재 시장 규모 거대

## 공모전 배점 전략

- **데이터 활용(20점)**: 8개 API, Round 1 미활용 4개 언어 API 모두 포함 → 만점 노림
- **기획력(30점)**: 명확한 미개척 타겟, 실제 수요 데이터(유럽 체류기간·지출 최고)
- **심사위원 임팩트**: "공모전 출품작 중 유럽어 4개 API 사용은 우리뿐"
