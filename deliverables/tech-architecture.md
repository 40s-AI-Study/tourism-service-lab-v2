---
type: deliverable
id: tech-architecture-koreadem-atlas
title: "KoreaDemand Atlas — 기술 아키텍처"
author_agent: apispecialist
author_model: claude-sonnet-4-6
created: 2026-04-17T14:45:00Z
status: draft
llm_compatibility: universal
idea_ref: koreadem-atlas
---

# KoreaDemand Atlas — 기술 아키텍처

## 시스템 구조도 (ASCII)

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT (Web/PWA)                         │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐  │
│  │  히트맵 뷰    │  │  지역 상세   │  │  연관 스팟 네트워크    │  │
│  │  (Mapbox GL) │  │  카드 뷰     │  │  그래프 (D3.js)       │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬────────────┘  │
└─────────┼─────────────────┼────────────────────┼────────────────┘
          │                 │                    │
          ▼                 ▼                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                     BFF / API Gateway (Next.js)                 │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐  │
│  │  /api/heatmap│  │  /api/detail │  │  /api/network         │  │
│  │  (지수 집계) │  │  (관광지 상세│  │  (연관 스팟)          │  │
│  │              │  │   + 예약 URL)│  │                       │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬────────────┘  │
│         │                 │                     │               │
│  ┌──────▼─────────────────▼─────────────────────▼────────────┐  │
│  │                  Cache Layer (Redis, TTL 1h)               │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────┬──────────────────────────────────────────────────────-┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│               Visit Korea OpenAPI (9개)                         │
│                                                                 │
│  Big-Data Index (4)        Big-Data Network (2)                 │
│  ┌──────────────────┐      ┌─────────────────────────────────┐  │
│  │ resource-demand  │      │ central-attractions-by-muni     │  │
│  │ demand-density   │      │ related-attractions  ← NEW      │  │
│  │ diversity        │      └─────────────────────────────────┘  │
│  │ tourism-big-data │                                           │
│  └──────────────────┘      Forecast (1)                        │
│                             ┌─────────────────────┐            │
│  i18n Info (2)              │ visitor-concentration│            │
│  ┌──────────────────┐       │ -forecast            │            │
│  │ tourism-info-ko  │       └─────────────────────┘            │
│  │ tourism-info-en  │                                           │
│  └──────────────────┘                                           │
└─────────────────────────────────────────────────────────────────┘
```

## 기술 스택

### Frontend
| 레이어 | 기술 | 선택 이유 |
|---|---|---|
| Framework | Next.js 14 (App Router) | SSR + PWA 지원, SEO |
| 지도 시각화 | Mapbox GL JS | 히트맵 레이어, 커스텀 마커 |
| 데이터 시각화 | D3.js | 연관 스팟 네트워크 그래프 |
| 차트 | Recharts | 수요 강도 시계열 차트 |
| 상태 관리 | Zustand | 경량, 지도 필터 상태 |
| 국제화 | next-intl | 한/영 UI 전환 |

### Backend (BFF)
| 레이어 | 기술 | 선택 이유 |
|---|---|---|
| Runtime | Node.js 20 + Next.js API Routes | FE와 단일 레포 |
| Cache | Redis (Upstash) | 관광 지수 API TTL 1h 캐시 |
| 인증 | Visit Korea API Key (env) | 공모전 서비스키 |

### Infra
| 항목 | 기술 |
|---|---|
| 배포 | Vercel (Frontend + BFF) |
| DB | 불필요 (API 응답 캐시만 사용) |
| CDN | Vercel Edge Network |

## API 호출 플로우

### 1. 히트맵 초기 로딩

```
Client → GET /api/heatmap?sido={시도코드}
  ├── [Cache Hit] Redis → 응답 반환
  └── [Cache Miss]
        ├── area-tourism-demand-density (체류·소비 강도)
        ├── area-tourism-resource-demand (자원 수요)
        ├── area-tourism-diversity (다양성 지수)
        └── tourism-big-data (실제 행동 데이터)
        → 4개 API 병렬 호출 → 집계 → Redis 저장 (TTL 1h) → 응답
```

### 2. 지역 상세 + 예약 URL

```
Client → GET /api/detail?contentId={id}&lang={ko|en}
  ├── tourism-info-korean 또는 tourism-info-english
  │     └── 응답 필드: title, addr, tel, homepage, reservationUrl, overview
  └── visitor-concentration-forecast (방문 최적 시점)
  → reservationUrl 있으면 "예약하기" 버튼 활성화
  → reservationUrl 없으면 homepageUrl 폴백
```

### 3. 연관 스팟 네트워크 (발굴 도구)

```
Client → GET /api/network?contentId={id}
  ├── central-attractions-by-municipality (지역 중심 관광지)
  └── related-attractions (연관 관광지·음식·숙박 50위)
  → D3.js force-directed graph 렌더링
  → 숙박 노드 클릭 → reservationUrl 딥링크
```

## 데이터 집계 로직 — 잠재력 점수

지역별 "관광 잠재력 종합 점수" 산출 공식:

```
잠재력 점수 = (
  resource_demand_score * 0.25 +   // 자원 수요 (공급 부족 지역 식별)
  demand_density_score  * 0.30 +   // 체류·소비 강도 (실제 인기도)
  diversity_score       * 0.20 +   // 다양성 (니치 가능성)
  big_data_score        * 0.25     // 실제 행동 데이터 (이동·카드)
)
→ 정규화 [0-100]
→ 히트맵 색상 매핑 (낮음: 파랑 → 높음: 빨강)
```

"숨겨진 보석" 필터: `resource_demand_score 높음 AND demand_density_score 낮음`
→ 수요는 있지만 아직 덜 알려진 지역

## 예약 연동 구현 상세

### reservationUrl 필드 처리

```typescript
// tourism-info-korean API 응답 활용
interface TourismDetailResponse {
  contentid: string;
  title: string;
  homepage: string;        // 공식 홈페이지
  reservationUrl?: string; // 예약 URL (있는 경우)
  // ...
}

function getBookingUrl(detail: TourismDetailResponse): string | null {
  if (detail.reservationUrl) return detail.reservationUrl; // 1순위
  if (detail.homepage) return detail.homepage;             // 2순위 폴백
  return null;
}
```

### 향후 수익화 경로 (앱 출시 후)

1. **제휴 링크 치환**: reservationUrl → 야놀자/여기어때 딥링크 + 제휴 파라미터
2. **숙박 추천 카드**: `related-attractions` 숙박 타입 데이터 → 숙박 예약 UI
3. **프리미엄 알림**: "이 지역 뜨기 전에 가세요" 알림 구독 = 유료 기능

## 공모전 기술 체크리스트

| 항목 | 상태 | 근거 |
|---|---|---|
| Visit Korea OpenAPI 활용 | ✅ | 9개 API 활용 |
| 빅데이터 4종 통합 | ✅ | resource-demand + demand-density + diversity + big-data |
| 예측 API 활용 | ✅ | visitor-concentration-forecast |
| 다국어 지원 | ✅ | tourism-info-korean + tourism-info-english |
| 연관성 API 활용 | ✅ | related-attractions + central-attractions |
| 외국인 타겟 | ✅ | 영문 API + 한/영 UI 전환 |
| 20-40대 타겟 | ✅ | 데이터 기반 발견 UX, 크리에이터 바이럴 |
| 예약 연동 | ✅ | reservationUrl 필드 활용 (외부 API 불필요) |
