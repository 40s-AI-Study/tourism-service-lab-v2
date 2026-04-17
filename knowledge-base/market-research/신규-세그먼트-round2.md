---
type: research
id: new-segments-round2
title: "신규 세그먼트 조사 + 경쟁사 앱 분석 Round 2"
author_agent: market-researcher
author_model: claude-sonnet-4-6
created: 2026-04-17T21:00:00+09:00
status: draft
round: 2
board_directive: "경쟁사 앱 분석 섹션 필수 포함 (2026-04-17 board 지시)"
sources:
  - https://www.koreatimes.co.kr/southkorea/society/20251221/record-influx-of-medical-tourists-delivers-247-bil-economic-windfall-for-korea
  - https://beautsgo.cceeo.com/en/blog/aboutme/
  - https://www.yeoshin.co.kr/en
  - https://valueradar.tistory.com/m/88
  - https://kimchilandguide.com/entry/naver-map-vs-kakaomap-korea
  - https://www.mk.co.kr/en/society/11476243
  - https://en.sedaily.com/technology/2026/02/27/naver-kakao-face-unlimited-competition-with-global-big-tech
  - https://static2.statista.com/statistics/1290736/south-korea-international-tourists-visiting-seoul-by-country/
  - https://static4.statista.com/statistics/1133384/south-korea-average-length-of-stay-for-visitors-by-origin/
aliases: ["신규 세그먼트 조사 Round 2"]
---

# 신규 세그먼트 조사 + 경쟁사 앱 분석 Round 2

> **Board 지시 반영 (2026-04-17)**: 경쟁사 앱 분석 섹션이 필수 포함 요건으로 추가됨.
> Round 1에서 다루지 않은 신규 세그먼트 2개 + 심화 경쟁사 앱 분석을 수행합니다.

---

## Part 1. 신규 세그먼트

### 세그먼트 1: 의료관광객 (Medical Tourists)

#### 1.1 시장 규모 및 특성

**2024년 핵심 지표 (확정 데이터)**

| 지표 | 수치 | 출처 |
|---|---|---|
| 방한 의료관광객 총계 | **약 117~120만명** (역대 최고) | 한국보건산업진흥원, Statista 2025 |
| 경제적 파급효과 | **2.47조원** (비의료 소비 포함) | Korea Times, 2025.12 |
| 의료 서비스 직접 지출 | 1.4조원 (38.3%) | Korea Times, 2025.12 |
| 1인당 평균 지출 | **약 400만원** | Korea Times, 2025.12 |
| 피부과 지출 | 5,855억원 (1위) | Chosun English, 2025.10 |
| 성형외과 지출 | 3,594억원 (2위) | Chosun English, 2025.10 |

**국적별 분포 (2024)**

| 국적 | 인원 순위 | 소비 순위 | 의료 지출 비중 | 특성 |
|---|---|---|---|---|
| 일본 | 1위 (28.2만명) | 2위 | 49% | 피부과·K-뷰티 중심 |
| 미국 | 2위 | **1위** (1조원+) | 높음 | 정밀검진·고급 의료 |
| 대만 | 3위 | 3위 | 46.5% | 한류 + 의료 복합 |
| 중국 | 4위 | 4위 | 중간 | 성형·K-뷰티 |
| 카자흐스탄 | — | — | **60%** (최고) | 러시아어권, 신뢰도 최상 |
| 인도네시아 | — | — | 56.3% | 무슬림, 할랄 케어 니즈 |
| 태국 | — | — | 45.1% | K-뷰티 영향 |

**서울 집중도**: 의료 지출의 87.6%가 서울 집중 → 부산(3.2B), 경기(7.9B)는 성장 여지

#### 1.2 의료관광객 여행 여정 (Patient Journey)

```
[여행 전]                    [현지 체류]              [귀국 후]
자국 온라인 커뮤니티     →   시술/치료            →   회복 체류
(중: 小红书, 일: X)          ↓                        SNS 후기
의료 정보 탐색               관광+쇼핑                 재방문 계획
비교 견적 수집               (400만원/인 지출)
예약 (앱/에이전시)

취약점:
- 사전 의료+관광 통합 플래닝 앱 없음
- 시술 후 회복 동선 추천 없음
- 다국어 의료 커뮤니케이션 도구 부족
```

#### 1.3 서비스 기획 기회

**기회 1: 의료+관광 통합 여정 플래너**

```
입력: "피부 시술 3박 4일 (일본인, 서울)"
출력:
  1일차: 도착 → 경복궁·북촌 관광 (시술 전 에너지 소모 최소)
  2일차: 오전 피부과 시술 → 숙소 휴식 (근처 웰니스 스파 추천)
  3일차: 회복 + 동대문 쇼핑 (가벼운 동선)
  4일차: 인천공항 출국 전 올리브영 쇼핑
API 활용: medical-tourism + related-attractions + wellness-tourism + tourism-info-japanese
```

**기회 2: CIS 의료관광 특화 (러시아어)**

- 카자흐스탄·우즈베키스탄 방한 의료관광객: 의료 지출 비중 60%로 최고
- 러시아어 한국 의료관광 정보 앱: **전무**
- API 조합: `medical-tourism` + `tourism-info-russian`

**기회 3: 할랄 의료관광 (인도네시아·말레이시아)**

- 인도네시아 의료 지출 비중 56.3%
- 할랄 음식 + 의료관광 통합 정보 수요
- 현재 대응 서비스: 없음

---

### 세그먼트 2: 유럽 장기 체류 여행자

#### 2.1 시장 특성

**2024년 체류 기간 데이터 (Statista)**

| 국적 | 평균 체류일 | 특성 |
|---|---|---|
| **프랑스** | **전체 국적 최장** | 역사·문화·미식 중심 |
| **독일** | 2위 | 하이킹·자연·역사 |
| 인도 | 3위 | — |
| 미국/캐나다 | 7.1일 | K-컬처·역사 |
| (비교) 중국 | 4.2일 | 쇼핑 중심 |
| (비교) 일본 | 3.8일 | 단기 반복 방문 |

**핵심 인사이트**: 프랑스·독일 여행자는 체류 기간이 가장 길어 1인당 총 소비가 높지만, 현재 이들을 위한 한국어 관광 앱이 전무합니다.

#### 2.2 프랑스 여행자 상세 프로파일

**방문 동기**: 역사·문화(1순위) > 미식(2순위) > 자연경관(3순위) > K-컬처(4순위)

**정보 탐색**: Google + Lonely Planet + 프랑스어 여행 블로그

**선호 여행 스타일**:
- 유럽 배낭여행식: 한 곳에서 거점 삶 방식 (경주, 전주 장기 체류)
- 박물관·유적 심층 탐방
- 현지인 접점 선호 (에코투어, 농촌 체험)

**Visit Korea API 연계**:
- `tourism-info-french` → 프랑스어 관광정보
- `audio-guide` → 역사 유적 오디오 해설 (프랑스어 개발 가치 ⭐⭐⭐⭐⭐)
- `eco-tourism` + `durunubi-trails` → 자연 심층 탐방
- `area-tourism-demand-density` → 덜 붐비는 지역 체류강도 기반 추천

#### 2.3 독일 여행자 상세 프로파일

**방문 동기**: 자연·하이킹(1순위) > 역사·문화(2순위) > K-컬처(3순위)

**선호 여행 스타일**:
- 아웃도어 액티비티 (독일 연간 아웃바운드 1.08억회, 자연 선호도 높음)
- 접근성 중시 (독일은 접근성 관광 인식 선진국)
- 장거리 하이킹 코스 선호

**Visit Korea API 연계**:
- `tourism-info-german` → 독일어 관광정보
- `durunubi-trails` → 걷기·자전거 코스
- `barrier-free-travel` → 접근성 관광 (독일 수요 높음)
- `eco-tourism` → 친환경 관광

---

## Part 2. 경쟁사 앱 분석 (Board 지시 필수 항목)

### 2.1 국내외 관광 앱 전체 경쟁 지도

#### OTA (숙박·여행 예약 플랫폼)

| 앱 | 현황 | 핵심 기능 | 한계 | 우리 기회 |
|---|---|---|---|---|
| **Agoda** | 2025.11 기준 국내 사용 1위 OTA (Yanolja 추월) | 글로벌 숙박 예약, 가격 비교 | 관광 정보·동선 없음 | 관광+예약 통합 |
| **Yanolja (NOL)** | 국내 OTA 전통 강자, Agoda에 1위 내줌 | 숙박·레저·항공 예약 | 관광 콘텐츠 빈약, 개인화 없음 | 상동 |
| **여기어때** | OTA 2위 (소비자 선호 2위 유지) | 숙박·레저 예약 | 콘텐츠 약함 | 상동 |
| **Trip.com** | 글로벌 OTA, 한국 진출 가속 | 항공·호텔·기차 통합 | 한국 특화 로컬 정보 없음 | 로컬 데이터 차별화 |

**시사점**: 예약 중심 플랫폼 경쟁은 Agoda·Yanolja가 지배. **관광 정보 + AI 코스 생성 영역은 공백.**

---

#### 지도·내비 앱

| 앱 | 현황 | 강점 | 한계 | 우리 기회 |
|---|---|---|---|---|
| **Naver Maps** | 국내 1위 지도 앱 (내국인) | 대중교통 정확도, 로드뷰, 한국어 | 외국인 UI 불친절, 영어 번역 부정확 | 외국인 특화 |
| **Kakao Maps** | 국내 2위 | 카카오 생태계 연동 | 외국어 지원 미흡 | 상동 |
| **Google Maps** | 외국인 1위 사용 앱 | 글로벌 UX | 한국 로컬 정보 불일치 잦음 | 공식 KTO 데이터 신뢰성 |

**2026년 경쟁 심화**: Naver·Kakao vs Google·Apple Maps — "글로벌 빅테크 무제한 경쟁" (Seoul Economic Daily, 2026.02). **관광 특화 정보 앱은 지도 앱과 다른 포지션으로 충돌 최소화 가능.**

---

#### 여행 계획·코스 앱

| 앱 | 타겟 | 핵심 기능 | 한계 | 우리 기회 |
|---|---|---|---|---|
| **트리플 (Triple)** | 국내 20-30대 | 여행 코스 공유, 타임라인 | AI 자동 생성 없음, 실시간 데이터 없음 | AI 자동 코스 생성 |
| **마이리얼트립** | 국내+해외 | 투어·액티비티 중개 | 예약 중심, 동선 연계 없음 | 관광 데이터 통합 |
| **Klook** | 아시아 외국인 | 액티비티 예약 | 현지 정보·동선 없음 | 공식 데이터 기반 |
| **TripAdvisor** | 글로벌 외국인 | 리뷰·평점 | 한국 콘텐츠 부족, 정보 오래됨 | 실시간 KTO 데이터 |

---

#### 의료관광 특화 앱

| 앱 | 타겟 | 핵심 기능 | 한계 | 우리 기회 |
|---|---|---|---|---|
| **YeoTi** (여신티켓) | 국내+외국인 | 피부과·성형 예약, K-뷰티 이벤트, 1M+ 다운로드 | 관광 연계 없음, 의료 여정 플래닝 없음 | 의료+관광 통합 |
| **BeautsGO** (피차미) | 중국인 특화 | 1,200개 피부과·성형외과 예약 | 중국어만, 관광 정보 없음 | 다국어 + 관광 연계 |
| **Visit Korea (공식)** | 전체 외국인 | 공식 관광정보 다국어 | UI 구식, 의료관광 섹션 없음 | 현대 UX로 재포장 |

---

### 2.2 경쟁 공백 히트맵

```
                    [예약 기능]     [관광 정보]    [AI 코스]    [의료관광]   [다국어]
Agoda/Yanolja          ✅             ❌            ❌           ❌         ⚠️
Naver/Kakao Maps       ❌             ✅            ❌           ❌         ❌
트리플                  ❌             ✅            ❌           ❌         ❌
Visit Korea 공식        ❌             ✅            ❌           ⚠️         ✅
YeoTi/BeautsGO         ✅             ❌            ❌           ✅         ⚠️

🎯 우리 서비스 포지션:
                       ⚠️             ✅            ✅           ✅         ✅
```

**모든 경쟁사가 커버하지 못하는 조합**: `공식 데이터 기반 관광 정보 + AI 코스 생성 + 의료관광 + 완전 다국어`

---

### 2.3 경쟁사별 심층 Gap 분석

#### Gap A: AI 코스 자동 생성 — **전체 경쟁사 공백**

- 트리플: 사용자가 직접 코스 작성
- 네이버: 실험적 AI 도입 시작 단계
- 여행 AI 코스 자동 생성 특화 앱: 한국 관광 특화는 **0개**

**우리 API 조합**: `related-attractions` + `central-attractions-by-municipality` + `visitor-concentration-forecast` + `area-tourism-demand-density`

---

#### Gap B: 의료관광 × 일반관광 통합 — **전체 경쟁사 공백**

- YeoTi/BeautsGO: 의료 예약만, 관광 없음
- Agoda/트리플: 관광/숙박만, 의료 없음
- **두 영역 통합 앱: 전무**

**우리 API 조합**: `medical-tourism` + `related-attractions` + `wellness-tourism` + 해당 언어 i18n API

---

#### Gap C: 유럽 언어권 한국 관광 앱 — **전체 경쟁사 공백**

- Visit Korea 공식 앱: 불어·독어·스페인어·러시아어 지원하나 UX 구식
- 전용 여행 앱: **전무** (영어·중국어·일본어 집중)

**우리 API 조합**: `tourism-info-french/german/spanish/russian` + `audio-guide` + `durunubi-trails`

---

### 2.4 전략적 포지셔닝 결론

> **"한국 공식 데이터 × 현대 UX × AI 개인화 × 의료관광 통합 × 완전 다국어 (9개 언어)"**

| 차별화 요소 | 경쟁사 | 우리 |
|---|---|---|
| 데이터 공신력 | 비공식·구글 의존 | 한국관광공사 공식 27개 API |
| AI 코스 생성 | 없음 | `related-attractions` + 빅데이터 조합 |
| 의료관광 연계 | 예약만 or 관광만 | 의료+관광 통합 여정 |
| 언어 지원 | 영/중/일 3개 | 최대 9개 (유럽 4개 포함) |
| 실시간 정보 | Google Popular Times | `visitor-concentration-forecast` (30일 예측) |

---

## Part 3. Round 2 인사이트 종합

### 신규 발견 기회 (Round 1 대비 추가)

1. **의료관광 통합 플랫폼**: 120만명 시장, 기존 앱 격차 명확
2. **CIS(카자흐스탄·우즈베키스탄) 러시아어 의료관광**: 의료 지출 비중 60%, 완전 블루오션
3. **유럽 장기 체류 여행자**: 프랑스·독일 체류 기간 최장 → 고가치 세그먼트, 앱 공백
4. **할랄 의료관광**: 인도네시아·말레이 무슬림 의료관광객 급증

### Round 2 추천 API 활용 조합

| 서비스 기능 | 핵심 API | 신규 API (Round 2) |
|---|---|---|
| 의료관광 여정 | `medical-tourism`, `wellness-tourism` | 신규: `tourism-info-russian`, `tourism-info-french` |
| 유럽 관광객 심층 탐방 | `eco-tourism`, `durunubi-trails` | 신규: `tourism-info-french`, `tourism-info-german` |
| 빅데이터 숨은 명소 발굴 | `visitor-concentration-forecast` | 신규: `area-tourism-resource-demand`, `area-tourism-diversity` |
| 지역 소비 인텔리전스 | `tourism-big-data` | 신규: `area-tourism-demand-density` |

---

*출처: Korea Times (2025.12.21), Chosun English (2025.10), Statista 2025, MK.co.kr (2025.11), Seoul Economic Daily (2026.02), BeautsGO 공식, YeoTi Google Play, Statista Korea average length of stay 2024*
