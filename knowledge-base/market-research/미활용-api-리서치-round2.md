---
type: research
id: underutilized-api-research-round2
title: "미활용 API 리서치 Round 2"
author_agent: market-researcher
author_model: claude-sonnet-4-6
created: 2026-04-17T21:00:00+09:00
status: final
round: 2
sources:
  - https://api.visitkorea.or.kr/#/useUtilExercises
  - https://datalab.visitkorea.or.kr/
  - https://www.oecd.org/en/publications/using-alternative-data-sources-and-tools-to-measure-and-monitor-tourism_2a655ab8-en/the-korea-tourism-data-lab_1b634f3f-en.html
  - https://www.koreatimes.co.kr/southkorea/society/20251221/record-influx-of-medical-tourists-delivers-247-bil-economic-windfall-for-korea
aliases: ["미활용 API 리서치 Round 2"]
---

# 미활용 API 리서치 Round 2

> **Round 1 대비 추가 분석.** Round 1(`경쟁 서비스 Gap 분석`)에서 개략적으로 언급된 API 외, 본격적으로 분석되지 않은 9개 API를 심층 검토합니다.

---

## 분석 대상 (미활용 9개 API)

| API ID | 제목 | 카테고리 | Round 1 언급 여부 |
|---|---|---|---|
| `area-tourism-resource-demand` | 지역별 관광 자원 수요 | big-data-index | ❌ 미언급 |
| `area-tourism-demand-density` | 지역별 관광 수요 강도 | big-data-index | ⚠️ 이름만 언급 |
| `area-tourism-diversity` | 지역별 관광 다양성 | big-data-index | ❌ 미언급 |
| `medical-tourism` | 의료관광정보 | thematic | ❌ 미언급 |
| `tourism-jobs` | 관광인 채용정보 | industry | ❌ 미언급 |
| `tourism-info-russian` | 노어(러시아어) 관광정보 | i18n | ❌ 미언급 |
| `tourism-info-spanish` | 서어(스페인어) 관광정보 | i18n | ❌ 미언급 |
| `tourism-info-french` | 불어(프랑스어) 관광정보 | i18n | ❌ 미언급 |
| `tourism-info-german` | 독어(독일어) 관광정보 | i18n | ❌ 미언급 |

---

## 1. 빅데이터 지수 3종 (Big-Data Index)

### 1.1 지역별 관광 자원 수요 (`area-tourism-resource-demand`)

**API 개요**
- 오퍼레이션: `areaCulResDemList` (문화자원 수요), `areaTarSvcDemList` (관광서비스 수요)
- 지표 구성: 관광 서비스 수요 지수 + 문화 자원 수요 지수
- 데이터 기반: 한국관광 데이터랩 빅데이터 융합분석

**서비스 기획 시사점**

| 활용 시나리오 | 설명 | 타겟 |
|---|---|---|
| 지역별 관광 인프라 점수화 | 어느 지역이 관광 자원이 풍부한지 수요 지수로 비교 | 기획자, 여행 큐레이션 AI |
| 숨은 명소 발굴 | 자원 수요 지수는 낮지만 실제 자원은 풍부한 지역 → 덜 알려진 명소 | 혼잡 회피형 여행자 |
| 지역 추천 근거 제시 | AI 코스 추천 시 "이 지역은 관광 자원 다양성 지수 상위 10%"처럼 신뢰 데이터 제공 | 전 타겟 |

**공모전 활용 평가**: ⭐⭐⭐ — `visitor-concentration-forecast`와 조합 시 "자원은 풍부하나 방문자가 적은 숨은 명소" 발굴 기능으로 차별화 가능.

---

### 1.2 지역별 관광 수요 강도 (`area-tourism-demand-density`)

**API 개요**
- 오퍼레이션: `areaTarSjrnDsList` (체류 강도), `areaTarExpDsList` (소비 강도)
- 지표 구성: 관광 체류 강도 + 관광 소비 강도

**핵심 인사이트**

관광 수요 강도는 단순 방문자 수(volume)가 아닌 **체류 시간**과 **소비 금액** 기반 질적 지표입니다. 이는 방문자가 많아도 짧게 머물고 소비가 적은 지역(낮은 강도)과 방문자가 적어도 장기 체류·고소비 지역(높은 강도)을 구분합니다.

**서비스 기획 시나리오**

```
입력: 사용자 → "제주도 말고 비슷한 감성의 곳"
처리: 체류강도 지수 유사 지역 탐색 (전주, 통영, 거제)
출력: "전주 한옥마을: 평균 1.8일 체류, 소비강도 제주의 87% — 덜 붐비는 제주 대안"
```

**공모전 활용 평가**: ⭐⭐⭐⭐ — Round 1에서 이름만 언급됐으나 실제로 KoreaPath AI, KoreaTrend Radar, LocalSecret 등 6개 아이디어에 이미 연결된 핵심 지수. 적극 활용 권장.

---

### 1.3 지역별 관광 다양성 (`area-tourism-diversity`)

**API 개요**
- 오퍼레이션: `areaTouDivList` (관광객 다양성), `areaExpDivList` (소비 다양성), `areaIntlDivList` (국제적 다양성)
- 지표 구성: 관광객 다양성 + 관광 소비 다양성 + **국제적 다양성**

**특히 주목할 지표: 국제적 다양성 (`areaIntlDivList`)**

외국인 방문객의 국적 다양성을 지수화합니다. 서울은 국제적 다양성이 높지만, 지방 도시는 특정 국가(일본인 중심의 부산, 중국인 중심의 경주 등) 편중 경향.

**서비스 기획 시나리오**

```
활용: 다국어 앱에서 지역별 국제 방문객 다양성 히트맵 제공
→ "부산: 일본인 42% / 대만인 18% / 영어권 15%"
→ 해당 지역 방문 예정 외국인에게 "이 지역에 당신과 같은 나라 여행자가 많습니다" 커뮤니티 기능 연계
```

**공모전 활용 평가**: ⭐⭐⭐⭐ — EcoTrail Korea, KoreaTrend Radar, LocalSecret 아이디어에 연결. 국제적 다양성 지수는 다국어 플랫폼의 지역 타겟팅 전략 수립에 직접 활용 가능.

---

### 빅데이터 3종 통합 활용 전략

```
[관광 자원 수요] + [관광 수요 강도] + [관광 다양성]
         ↓
지역별 종합 관광 잠재력 스코어카드
         ↓
"자원은 풍부(高) + 혼잡도 낮음(低) + 국제 다양성 높음(高)" = 숨은 명소 추천
```

> **OECD 검증**: 한국관광 데이터랩은 2024년 기준 578종의 공공·민간 데이터 통합, 월 이용자 11.4만명 — OECD 사례 연구 대상 선정 (출처: OECD, 2025).

---

## 2. 의료관광정보 (`medical-tourism`)

**시장 현황 (2024년 확정 데이터)**

| 지표 | 수치 | 출처 |
|---|---|---|
| 방한 외국인 의료관광객 | **117~120만명** (역대 최고) | 한국보건산업진흥원, Statista 2025 |
| 경제적 파급효과 | **2.47조원** ($2.47B) | Korea Times, 2025.12 |
| 1인당 소비액 | **약 400만원** (의료+관광 통합) | Korea Times, 2025.12 |
| 진료과 1위 | 피부과 (5,855억원, 25.8%) | Chosun English, 2025.10 |
| 진료과 2위 | 성형외과 (3,594억원) | Chosun English, 2025.10 |
| 국적별 1위(인원) | 일본 (28.2만명) | Korea Times, 2025.12 |
| 국적별 1위(소비) | 미국 (1조원+) | Korea Times, 2025.12 |

**API 오퍼레이션 분석**

| 오퍼레이션 | 설명 | 서비스 활용 |
|---|---|---|
| `areaBasedList` / `locationBasedList` | 지역·위치 기반 의료기관 목록 | "내 주변 피부과/성형외과" 검색 |
| `corprHsptlInfo` | 법인 병원 정보 | 대형 의료관광 전문 병원 필터 |
| `mdclTursmDivInfo` | 의료관광 구분 정보 | 진료과별 분류 (피부/성형/검진/한방) |
| `specProcMdlcInfo` | 전문 시술 의료 정보 | 시술 유형별 필터링 |
| `mainMdlcSubjInfo` | 주요 진료과목 정보 | 진료과 네비게이션 |
| `hmpgInfo` | 홈페이지 정보 | 공식 링크 연결 |
| `prSnsInfo` | SNS 정보 | 인스타/유튜브 채널 연결 (신뢰도) |

**경쟁 앱 현황 (의료관광 특화)**

| 앱 | 타겟 | 기능 | 한계 |
|---|---|---|---|
| **YeoTi** (여신티켓) | 국내+외국인 | 피부과/성형 예약, K-뷰티, 1M+ 다운로드 | 주로 한국어·영어, 관광 정보 없음 |
| **BeautsGO** (피차미) | 중국인 특화 | 1,200+ 한국 피부과/성형 예약 | 중국어만, 관광 연계 없음 |

**우리 서비스 기회**

- 기존 의료관광 앱: 예약 중심, 관광 정보 없음
- `medical-tourism` API × `tourism-info-english/japanese` × `related-attractions` 조합 시
  → "치료 전날 경복궁 관광 → 시술 후 회복용 스파 숙소 추천" 통합 여정 기획 가능
- **특히 미국인 의료관광객 소비 1위** (1조원+) — 영어 서비스 필수

**공모전 활용 평가**: ⭐⭐⭐⭐⭐ — 역대 최고 시장 규모, 기존 앱 대비 차별점 명확 (관광+의료 통합), 공모전 혁신성 항목 강점.

---

## 3. 관광인 채용정보 (`tourism-jobs`)

**API 개요**
- 오퍼레이션: `empmnInfoList` (채용 목록), `empmnInfoDetail` (상세), `labrrNumInfo` (근로자수), `tursmEmpmnInfoURL` (공고 URL)
- 대상: 관광업계 전반 (호텔, 여행사, 관광지 운영사 등)

**서비스 기획 시사점**

관광 앱 사용자 타겟에 직접 포함되는 세그먼트는 아니나, 다음 B2B/B2B2C 확장 시나리오에서 활용 가능:

1. **가이드 매칭 플랫폼**: 관광 가이드 채용 데이터 → 프리랜서 가이드 커넥팅
2. **여행사 파트너 생태계**: 소규모 여행사 채용 데이터 → 파트너 네트워크 구축 신뢰 지표
3. **관광업 취업 지원 앱**: 관광 관련 취준생 타겟 서브 서비스

**공모전 활용 평가**: ⭐⭐ — 소비자 관광 앱의 핵심 기능과 직결도 낮음. 공모전 가점(데이터 다양성) 목적으로 부가 활용 수준. 우선순위 낮음.

---

## 4. 유럽권 i18n API 4종

### 공통 오퍼레이션 (4개 언어 공통)

| 오퍼레이션 | 설명 |
|---|---|
| `areaBasedList2` | 지역 기반 관광정보 (해당 언어) |
| `locationBasedList2` | 위치 기반 관광정보 |
| `searchKeyword2` | 키워드 검색 |
| `searchFestival2` | 축제 정보 |
| `detailCommon2` | 상세 공통 정보 |
| `detailImage2` | 이미지 정보 |
| `detailInfo2` | 소개 정보 |

### 4.1 노어 (러시아어) `tourism-info-russian`

**시장 현황 (2024)**
- 러시아 관광객 방한 규모: 제재 이후 소폭 감소하나 CIS 국가(카자흐스탄·우즈베키스탄)로 분산 방문
- 카자흐스탄 방한 의료관광객: 의료 지출 비중 60% (전체 국적 중 최고) — 한국 의료 신뢰도 최상
- 러시아어 인터넷 인구: 글로벌 5위권 (약 1.1억명 사용)

**서비스 기획 시사점**
- 카자흐스탄·우즈베키스탄 의료관광객은 러시아어 사용 → `tourism-info-russian` × `medical-tourism` 조합
- K-Culture 확산으로 중앙아시아 젊은층 방한 관심 증가
- 현재 러시아어 한국 관광 앱: **전무** → 블루오션

**공모전 활용 평가**: ⭐⭐⭐⭐ — 의료관광 × 러시아어 조합은 경쟁 공모전 팀이 거의 고려하지 않는 차별화 포인트.

---

### 4.2 스페인어 `tourism-info-spanish`

**시장 현황 (2024)**
- 스페인·라틴아메리카 방한객: 소규모이나 고성장 (K-컬처 글로벌화 효과)
- 스페인어 인터넷 인구: 글로벌 2위 (약 5.7억명 사용)
- 스페인 관광객 체류 기간: 8일+ (유럽 평균 이상 장기 체류 선호)

**서비스 기획 시사점**
- 남미(브라질 제외) K-팝·K-드라마 팬덤 급성장 → 팬덤 관광 특화 콘텐츠
- 스페인어 한국 관광 정보 앱: 사실상 **전무**

---

### 4.3 프랑스어 `tourism-info-french`

**시장 현황 (2024)**
- **프랑스인 한국 체류 기간: 전체 국적 중 최장** (Statista 2024 기준)
- 독일인이 2위로 뒤따름
- 프랑스 방한 목적: 역사·문화·미식 (K-뷰티보다 문화 강세)
- 평균 소비: 장기 체류 → 총 지출 높음

**서비스 기획 시사점**
- 장기 체류 → 심층 지역 탐방 수요 → `durunubi-trails` + `eco-tourism` + `tourism-info-french` 조합
- 프랑스어 한국 관광 앱: **전무**
- `audio-guide` API의 프랑스어 버전 개발 시 차별화 극대화

---

### 4.4 독어 (독일어) `tourism-info-german`

**시장 현황 (2024)**
- 독일인 한국 체류 기간: 전체 국적 중 2위 (프랑스에 이어)
- 독일 방한 목적: 하이킹·자연·역사 관심 높음
- 독일 아웃바운드 여행: 연 1.08억회 (2024) — 대형 아웃바운드 시장

**서비스 기획 시사점**
- 하이킹·트레킹 관심 → `durunubi-trails` + `eco-tourism` + `tourism-info-german`
- `barrier-free-travel`과 조합: 독일은 접근성 관광 인식 높음

---

### 유럽 i18n 4종 통합 전략

```
공통 아키텍처: 언어 선택 → 해당 i18n API 자동 라우팅
러시아어: medical-tourism + 중앙아시아 의료관광 특화
스페인어: K-문화 팬덤 + 장기 체류 코스
프랑스어: 역사·문화·미식 심층 탐방 + durunubi
독일어: 하이킹·에코 + 접근성 (barrier-free)
```

**공모전 활용 평가 (4종 합산)**: ⭐⭐⭐⭐ — 기존 경쟁팀 대부분 영/중/일 3개 언어에만 집중. 유럽 4개 언어 추가 시 "27개 API 중 최다 활용" 전략에서 핵심 가산점.

---

## 5. API 활용 우선순위 종합 (Round 2)

| 우선순위 | API | 평가 | 근거 |
|---|---|---|---|
| 🥇 **최고** | `medical-tourism` | ⭐⭐⭐⭐⭐ | 역대 최고 시장, 기존 앱 격차 명확 |
| 🥈 **높음** | `area-tourism-demand-density` | ⭐⭐⭐⭐ | 6개 기존 아이디어 이미 연결, 즉시 활용 |
| 🥈 **높음** | `area-tourism-diversity` | ⭐⭐⭐⭐ | 국제적 다양성 지수 → 다국어 플랫폼 타겟팅 |
| 🥉 **중간** | `tourism-info-russian` | ⭐⭐⭐⭐ | 의료관광 × CIS 블루오션 |
| 🥉 **중간** | `tourism-info-french` | ⭐⭐⭐⭐ | 체류 기간 최장 → 고가치 세그먼트 |
| 🥉 **중간** | `area-tourism-resource-demand` | ⭐⭐⭐ | 숨은 명소 발굴 기능 보완 |
| 🔵 **부가** | `tourism-info-spanish` | ⭐⭐⭐ | 라틴 K-팬덤 성장 중 |
| 🔵 **부가** | `tourism-info-german` | ⭐⭐⭐ | 에코·하이킹 특화 |
| ⚪ **낮음** | `tourism-jobs` | ⭐⭐ | B2C 앱 핵심 기능 연관성 낮음 |

---

*출처: 한국관광공사 OpenAPI 카탈로그, Korea Times (2025.12), Chosun English (2025.10), Statista (2025), OECD Tourism DataLab Case Study (2025)*
