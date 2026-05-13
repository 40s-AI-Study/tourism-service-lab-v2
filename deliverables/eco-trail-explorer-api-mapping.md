---
type: deliverable
id: eco-trail-explorer-api-mapping
title: "Eco-Trail Explorer — Visit Korea OpenAPI 매핑 설계"
author_agent: apispecialist
author_model: claude-sonnet-4-6
created: 2026-05-01T13:30:00Z
status: final
llm_compatibility: universal
idea_ref: eco-trail-explorer
---

# Eco-Trail Explorer — Visit Korea OpenAPI 매핑 설계

## 1. 사용 API 선정 (9개)

| # | API ID | 한국어 명칭 | 역할 | 우선순위 |
|---|---|---|---|---|
| 1 | `durunubi-trails` | 두루누비 정보 서비스 | 걷기·자전거 트레일 코스 데이터 (핵심) | Must |
| 2 | `eco-tourism` | 생태 관광 정보 | 친환경·공정관광지 목록 (핵심) | Must |
| 3 | `tourism-info-ko` | 국문 관광정보 서비스 | 관광지 상세·이미지·한국어 정보 | Must |
| 4 | `tourism-info-en` | 영문 관광정보서비스 | 외국인 대상 영문 콘텐츠 | Must |
| 5 | `visitor-concentration-forecast` | 관광지 집중률 방문자 추이 예측 | 향후 30일 혼잡도 예측 → 비혼잡 트레일 추천 | Must |
| 6 | `tourism-big-data` | 관광빅데이터 정보서비스 | 지역 방문자 수 트렌드 (탄소절감 임팩트 계산 기반) | Should |
| 7 | `related-attractions` | 관광지별 연관 관광지 정보 | 트레일 주변 연관 에코 스팟 네트워크 | Should |
| 8 | `barrier-free` | 무장애 여행 정보 | 접근성 약자 페르소나 지원 (휠체어·저이동성) | Should |
| 9 | `camping` | 고캠핑 정보 조회서비스 | 에코 캠핑지 정보 (트레일 종점 숙박 연계) | Could |

---

## 2. API별 핵심 오퍼레이션 명세

### 2-1. 두루누비 정보 서비스 (`durunubi-trails`)

**Base URL**: `https://apis.data.go.kr/B551011/Durunubi`

| 오퍼레이션 | 엔드포인트 | 주요 파라미터 | 응답 핵심 필드 | 용도 |
|---|---|---|---|---|
| `courseList` | `/courseList` | `brdDiv` (코스 구분), `pageNo`, `numOfRows` | `courseName`, `cpCont` (코스 설명), `distance`, `mvmn` (이동수단) | 트레일 목록 피드 |
| `crsTourInfo` | `/crsTourInfo` | `crsIdx` (코스 인덱스), `crsCode` | `tourIdx`, `tourName`, `distance`, `latitude`, `longitude` | 코스 내 관광 스팟 |
| `routeList` | `/routeList` | `crsCode`, `pageNo` | `wayIdx`, `wayName`, `gpsX`, `gpsY`, `wayLen` | 경로 웨이포인트 (지도 렌더링) |

**탄소 절감 계산 연동**:
```
trailDistance (km) × (carEmissionFactor - walkEmissionFactor)
= 절감 CO2 (kg)

carEmissionFactor = 0.21 kg CO2/km (IPCC 2023 표준)
walkEmissionFactor = 0.00 kg CO2/km
bikeEmissionFactor = 0.00 kg CO2/km
```

---

### 2-2. 생태 관광 정보 (`eco-tourism`)

**Base URL**: `https://apis.data.go.kr/B551011/EcoTour`

| 오퍼레이션 | 엔드포인트 | 주요 파라미터 | 응답 핵심 필드 | 용도 |
|---|---|---|---|---|
| `areaBasedList` | `/areaBasedList` | `areaCode`, `sigunguCode`, `pageNo` | `title`, `addr1`, `mapx`, `mapy`, `firstimage` | 지역별 에코 스팟 목록 |
| `areaBasedList1` | `/areaBasedList1` | `areaCode`, `contentTypeId` | `contentid`, `title`, `overview`, `tel` | 에코 스팟 상세 |
| `areaBasedSyncList1` | `/areaBasedSyncList1` | `modifiedtime` | (전체 필드) | 주기적 동기화 (DB 갱신용) |

**에코 등급 태깅 로직** (자체 계산):
- 생태관광지 API 출처 → `ECO_CERTIFIED` 뱃지
- 두루누비 코스 연결 → `TRAIL_LINKED` 뱃지
- 교통수단 자전거/도보만 접근 → `LOW_CARBON` 뱃지

---

### 2-3. 국문/영문 관광정보 서비스

**Base URL**: `https://apis.data.go.kr/B551011/KorService1` (한국어)  
**Base URL**: `https://apis.data.go.kr/B551011/EngService1` (영문)

| 오퍼레이션 | 용도 |
|---|---|
| `areaBasedList1` | 지역 관광지 목록 (에코 스팟 보완) |
| `detailCommon1` | 관광지 상세 (주소, 전화, 홈페이지) |
| `detailImage2` | 관광지 이미지 (UI 카드용) |
| `detailIntro1` | 관광지 소개 텍스트 |

**다국어 라우팅**:
```
User locale == 'ko' → KorService1
User locale == 'en' → EngService1
User locale == 'ja' → JpnService1
User locale == 'zh-CN' → ChsService1
```

---

### 2-4. 관광지 집중률 방문자 추이 예측 (`visitor-concentration-forecast`)

**Base URL**: `https://apis.data.go.kr/B551011/DataLabService`

| 오퍼레이션 | 파라미터 | 응답 핵심 필드 | 용도 |
|---|---|---|---|
| `tatsCnctrRateList` | `contentId`, `startYmd`, `endYmd` | `baseYmd`, `daywkDivNm`, `cnctrRate` (집중률 0-100) | 30일 혼잡도 예측 그래프 |
| `tatsCnctrRatedList` | `areaCode`, `sigunguCode` | `contentId`, `title`, `avgCnctrRate` | 지역 내 혼잡 순위 |

**비혼잡 트레일 추천 알고리즘**:
```
score = (100 - cnctrRate) × 0.5
      + ecoGrade × 0.3
      + distance_match × 0.2

추천 조건: score >= 70 AND cnctrRate < 40
```

---

### 2-5. 관광빅데이터 정보서비스 (`tourism-big-data`)

| 오퍼레이션 | 파라미터 | 용도 |
|---|---|---|
| `locgoRegnVisitrDDList` | `areaCode`, `startYmd`, `endYmd` | 기초지자체별 일별 방문자 수 |
| `metcoRegnVisitrDDList` | `areaCode` | 광역시도별 방문자 수 |

**탄소 임팩트 대시보드 활용**:
- 트레일 이용자 수 × 절감 CO2/인 = 지역 월간 탄소절감 추정치

---

### 2-6. 연관 관광지 정보 (`related-attractions`)

| 오퍼레이션 | 파라미터 | 응답 핵심 필드 | 용도 |
|---|---|---|---|
| `areaBasedList` | `contentId` (트레일 ID) | `relatedContentId`, `title`, `distance` | 트레일 주변 에코 스팟 네트워크 |

---

### 2-7. 무장애 여행 정보 (`barrier-free`)

| 오퍼레이션 | 파라미터 | 응답 핵심 필드 | 용도 |
|---|---|---|---|
| `areaBasedList` | `areaCode` | `title`, `wheelchairRental`, `exitNum`, `braileGuide` | 접근성 필터링 |
| `detailWithTour` | `contentId` | `wheelchairRental`, `guideDogYn`, `audioGuideYn` | 접근성 상세 정보 |

---

## 3. API 호출 시퀀스 (메인 플로우)

### 시퀀스 A: 트레일 탐색 화면 초기 로딩

```
[사용자 앱 진입]
        │
        ▼
[1] durunubi: courseList?brdDiv=W&numOfRows=20
    → 걷기 트레일 20개 목록 취득
        │
        ▼ (병렬)
[2a] eco-tourism: areaBasedList?areaCode={지역}
     → 에코 스팟 목록
[2b] visitor-forecast: tatsCnctrRateList?contentId={각_ID}
     → 혼잡도 예측 (배치, 20개)
        │
        ▼ (병렬)
[3a] tourism-info-ko: detailImage2?contentId={각_ID}
     → 썸네일 이미지
[3b] 탄소절감 계산 (로컬)
     → distance × emissionFactor
        │
        ▼
[4] 응답 병합 → 추천 score 정렬 → 클라이언트 반환
```

---

### 시퀀스 B: 트레일 상세 + 경로 렌더링

```
[트레일 카드 클릭]
        │
        ▼ (병렬)
[1a] durunubi: crsTourInfo?crsCode={ID}
     → 코스 내 스팟 목록
[1b] durunubi: routeList?crsCode={ID}
     → 지도 웨이포인트 (GPS 좌표 배열)
[1c] tourism-info-ko: detailCommon1?contentId={ID}
     → 기본 정보 (주소, 전화, 운영시간)
        │
        ▼ (병렬)
[2a] related-attractions: areaBasedList?contentId={ID}
     → 주변 에코 스팟 3개
[2b] visitor-forecast: tatsCnctrRateList?contentId={ID}
     → 30일 혼잡도 그래프 데이터
[2c] barrier-free: detailWithTour?contentId={ID}
     → 접근성 정보 (사용자 설정에 따라 조건부)
        │
        ▼
[3] 교통수단 입력 받아 탄소발자국 계산 (로컬 엔진)
        │
        ▼
[4] 상세 페이지 렌더링 완료
```

---

### 시퀀스 C: 외국인 다국어 모드

```
[locale 감지 / 설정]
        │
        ├─ ko → KorService1
        ├─ en → EngService1
        ├─ ja → JpnService1
        └─ zh → ChsService1

[콘텐츠 ID는 공통]
→ 언어별 서비스에서 동일 contentId로 title/overview 조회
→ 이미지는 KorService1 detailImage2 (언어 무관 공용)
```

---

## 4. 캐싱 전략

| 데이터 유형 | TTL | 캐시 키 | 이유 |
|---|---|---|---|
| 트레일 목록 (courseList) | 24h | `durunubi:courses:{brdDiv}:{areaCode}` | 코스 정보 변경 빈도 낮음 |
| 에코 스팟 목록 | 24h | `eco:spots:{areaCode}:{sigungu}` | 인증 생태관광지는 월 단위 변경 |
| 관광지 이미지 | 7d | `img:{contentId}` | 이미지는 거의 변하지 않음 |
| 관광지 상세 정보 | 6h | `detail:{contentId}:{locale}` | 운영시간 등 일 단위 변경 가능 |
| 혼잡도 예측 | 1h | `forecast:{contentId}:{date}` | 예측치는 매일 갱신 |
| 빅데이터 방문자 수 | 12h | `bigdata:visitors:{areaCode}:{ym}` | 통계는 전날 집계 |
| 연관 관광지 | 24h | `related:{contentId}` | 연관 관계 변경 드묾 |

**캐시 구현**: Redis (Upstash Serverless)

```typescript
// 캐시 미들웨어 패턴
async function fetchWithCache<T>(
  key: string,
  ttlSeconds: number,
  fetcher: () => Promise<T>
): Promise<T> {
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);
  const data = await fetcher();
  await redis.setex(key, ttlSeconds, JSON.stringify(data));
  return data;
}

// 사용 예시
const trails = await fetchWithCache(
  `durunubi:courses:W:${areaCode}`,
  86400, // 24h
  () => durunubiApi.courseList({ brdDiv: 'W', areaCode })
);
```

---

## 5. 에러 핸들링 및 Fallback

| 장애 상황 | Fallback 전략 |
|---|---|
| 두루누비 API 응답 없음 | 에코 관광 정보 API만으로 카드 렌더링 (트레일 아이콘 표시 생략) |
| 혼잡도 예측 API 실패 | 혼잡도 배지 비표시, "정보 준비 중" 표시 |
| 영문 API 응답 없음 | 국문 API 원문 + DeepL 자동번역 (프론트 클라이언트 사이드) |
| 이미지 API 실패 | 관광지 유형별 기본 placeholder 이미지 |
| 전체 API Rate Limit | Stale-while-revalidate + 만료된 캐시 반환 |

---

## 6. API 호출 비용 최적화

```
초기 로딩: 최대 5회 API 호출 (병렬)
상세 조회: 최대 6회 API 호출 (병렬)
혼잡도 배치: 1회 호출 (20개 ID 배열 처리)

일일 예상 API 호출:
- MAU 1,000명 기준
- 페이지뷰 3,000/일 × 5호출 = 15,000회
- 캐시 히트율 70% → 실제 호출 4,500회/일
- 공공데이터포털 일 10,000회 제한 → 안전
```

---

## 7. contentTypeId 코드표 (생태 관련)

| contentTypeId | 분류 | Eco-Trail 활용 |
|---|---|---|
| 12 | 관광지 | 에코 스팟 |
| 28 | 레포츠 | 트레킹·자전거 |
| 32 | 숙박 | 에코 캠핑 (고캠핑 연계) |
| 38 | 쇼핑 | 로컬 파머스마켓 |
| 39 | 음식점 | 로컬푸드 레스토랑 |

---

*참고: 모든 API는 `serviceKey` (공공데이터포털 발급) + `MobileOS` + `MobileApp` 필수 파라미터 포함 필요*
