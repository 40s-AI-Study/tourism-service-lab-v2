---
type: deliverable
id: eco-trail-explorer-tech-architecture
title: "Eco-Trail Explorer — 기술 아키텍처"
author_agent: apispecialist
author_model: claude-sonnet-4-6
created: 2026-05-01T13:35:00Z
status: draft
llm_compatibility: universal
idea_ref: eco-trail-explorer
---

# Eco-Trail Explorer — 기술 아키텍처

## 1. 시스템 구조도

```
┌──────────────────────────────────────────────────────────────────────┐
│                        CLIENT (Web PWA / Mobile)                     │
│                                                                      │
│  ┌─────────────────┐  ┌──────────────────┐  ┌────────────────────┐  │
│  │  Trail Feed      │  │  Trail Detail    │  │  Carbon Dashboard  │  │
│  │  (지도+리스트)   │  │  (경로+에코스팟) │  │  (CO2 절감 트래킹) │  │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬───────────┘  │
│           │                    │                      │              │
│  ┌─────────▼────────────────────▼──────────────────────▼───────────┐  │
│  │           Carbon Footprint Engine (클라이언트 사이드)            │  │
│  │  input: distance + transport_mode                               │  │
│  │  output: co2_saved_kg, eco_score, green_badge                   │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└──────────────────────────┬───────────────────────────────────────────┘
                           │ HTTPS
                           ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    BFF / API Gateway (Next.js 14)                    │
│                                                                      │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────────────┐  │
│  │ /api/trails    │  │ /api/trail/:id │  │ /api/carbon           │  │
│  │ 트레일 목록    │  │ 상세+경로+스팟 │  │ 지역 탄소 임팩트      │  │
│  └───────┬────────┘  └───────┬────────┘  └───────────┬───────────┘  │
│          │                  │                        │              │
│  ┌───────▼──────────────────▼────────────────────────▼───────────┐  │
│  │              Cache Layer (Redis / Upstash, TTL 1h–24h)        │  │
│  └───────────────────────────────────────────────────────────────┘  │
└──────────────────────────┬───────────────────────────────────────────┘
                           │
          ┌────────────────┼────────────────────┐
          ▼                ▼                    ▼
┌──────────────┐  ┌──────────────────┐  ┌──────────────────────────┐
│ Visit Korea  │  │ Visit Korea      │  │ Visit Korea              │
│ OpenAPI #1   │  │ OpenAPI #2       │  │ OpenAPI #3–9             │
│              │  │                  │  │                          │
│ 두루누비     │  │ 생태관광정보     │  │ 국문/영문 관광정보       │
│ (트레일코스) │  │ (친환경관광지)   │  │ 혼잡도예측 / 빅데이터   │
│              │  │                  │  │ 연관관광지 / 무장애      │
└──────────────┘  └──────────────────┘  └──────────────────────────┘
```

---

## 2. 탄소발자국 계산 엔진 (Carbon Footprint Engine)

### 2-1. 배출 계수 표 (IPCC 2023 기준)

| 교통수단 | CO2 배출 계수 | 단위 |
|---|---|---|
| 자가용 (가솔린) | 0.210 | kg CO2/km |
| 자가용 (디젤) | 0.171 | kg CO2/km |
| 버스 | 0.089 | kg CO2/km·인 |
| 기차 (KTX/무궁화) | 0.041 | kg CO2/km·인 |
| 자전거 | 0.000 | kg CO2/km |
| 도보 | 0.000 | kg CO2/km |

### 2-2. 계산 로직

```typescript
interface CarbonInput {
  distanceKm: number;
  transportMode: 'car' | 'bus' | 'train' | 'bike' | 'walk';
  passengers?: number; // 자가용 동승자 수 (default: 1)
}

interface CarbonOutput {
  emissionKg: number;        // 실제 배출량
  baselineKg: number;        // 자가용 단독 기준
  savedKg: number;           // 절감량
  savedPercent: number;      // 절감 비율 (%)
  ecoScore: number;          // 0–100 에코 점수
  treesEquivalent: number;   // 나무 흡수 환산 (1 그루/년 = 21.77 kg CO2)
}

const EMISSION_FACTORS: Record<string, number> = {
  car: 0.210,
  bus: 0.089,
  train: 0.041,
  bike: 0.000,
  walk: 0.000,
};

function calculateCarbon(input: CarbonInput): CarbonOutput {
  const { distanceKm, transportMode, passengers = 1 } = input;
  const factor = EMISSION_FACTORS[transportMode];
  const carFactor = EMISSION_FACTORS['car'];

  const emissionKg = transportMode === 'car'
    ? (factor * distanceKm) / passengers
    : factor * distanceKm;

  const baselineKg = carFactor * distanceKm;
  const savedKg = Math.max(0, baselineKg - emissionKg);
  const savedPercent = baselineKg > 0 ? (savedKg / baselineKg) * 100 : 100;
  const ecoScore = Math.min(100, Math.round(savedPercent));
  const treesEquivalent = savedKg / 21.77;

  return { emissionKg, baselineKg, savedKg, savedPercent, ecoScore, treesEquivalent };
}
```

### 2-3. 탄소 배지 시스템

| 에코 점수 | 배지 | 라벨 |
|---|---|---|
| 100 | 🌿 카본-제로 | Carbon Zero |
| 80–99 | 🟢 그린 트레블러 | Green Traveler |
| 60–79 | 🔵 에코 익스플로러 | Eco Explorer |
| 40–59 | 🟡 에코 스타터 | Eco Starter |
| 0–39 | ⚪ 일반 여행 | Standard |

---

## 3. 기술 스택

### Frontend
| 레이어 | 기술 | 선택 이유 |
|---|---|---|
| Framework | Next.js 14 (App Router) | SSR + PWA + SEO |
| 지도 | Mapbox GL JS | 경로 렌더링, 에코 레이어 |
| 상태 관리 | Zustand | 경량, 트레일 필터 상태 |
| 차트 | Recharts | 탄소 절감 시계열 |
| 국제화 | next-intl | 한/영/일/중 전환 |
| PWA | next-pwa | 오프라인 트레일 캐시 |

### Backend (BFF)
| 레이어 | 기술 | 선택 이유 |
|---|---|---|
| Runtime | Node.js 20 + Next.js API Routes | FE 단일 레포 |
| Cache | Redis (Upstash Serverless) | API 결과 캐시 |
| API 키 관리 | Vercel Environment Variables | 서비스키 보호 |
| 유효성 검증 | Zod | API 응답 스키마 검증 |

### DB / 저장소
| 용도 | 기술 | 비고 |
|---|---|---|
| 사용자 탄소 기록 | Supabase (PostgreSQL) | 누적 CO2 절감 트래킹 |
| 에코 배지 | Supabase | 사용자 배지 컬렉션 |
| 트레일 즐겨찾기 | Supabase | 사용자별 |

### Infra
| 항목 | 기술 |
|---|---|
| 호스팅 | Vercel (Edge Network) |
| CDN | Vercel Edge (이미지 최적화) |
| 모니터링 | Vercel Analytics |
| CI/CD | GitHub Actions → Vercel auto-deploy |

---

## 4. 국립공원 28개 연결 API 설계

```
국립공원 지역 코드 매핑 (두루누비 areaCode 기준):

 강원도  → areaCode: 32  (설악산, 오대산, 치악산)
 경상남도 → areaCode: 38  (지리산, 가야산, 한려해상)
 전라남도 → areaCode: 46  (다도해해상, 월출산)
 제주도  → areaCode: 50  (한라산)
 충청남도 → areaCode: 44  (태안해안)
 ...

API 호출:
GET /durunubi/courseList?areaCode={nationalParkArea}&brdDiv=W
→ 국립공원 내 트레일 필터링

에코 스팟 연계:
GET /eco-tourism/areaBasedList?areaCode={area}&contentTypeId=28
→ 국립공원 내 레포츠·생태 체험 스팟
```

---

## 5. B2B 에코투어 운영사 연동 구조

```
┌─────────────────────────────────────────────────────────┐
│                 B2B Partner API Layer                    │
│                                                         │
│  POST /api/b2b/tours          투어 상품 등록            │
│  GET  /api/b2b/tours/:id      투어 상세 조회            │
│  POST /api/b2b/bookings       예약 접수                 │
│  GET  /api/b2b/carbon-report  탄소 절감 리포트          │
│                                                         │
│  인증: API Key (운영사별 발급)                          │
│  데이터: Supabase b2b_tours, b2b_bookings 테이블        │
└─────────────────────────────────────────────────────────┘
         │
         ▼ (데이터 흐름)
탄소 오프셋 크레딧 연동 (Phase 2):
- 운영사의 투어 탄소 절감량 집계
- 분기별 크레딧 발급 (CSV 리포트)
- 국제 탄소 오프셋 표준(VCS/GS) 연계 준비
```

---

## 6. 데이터베이스 스키마 (핵심 테이블)

```sql
-- 사용자 탄소 기록
CREATE TABLE carbon_logs (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID REFERENCES auth.users,
  trail_id    TEXT NOT NULL,           -- 두루누비 crsCode
  trail_name  TEXT,
  distance_km DECIMAL(8,2),
  transport   TEXT,                    -- car/bus/train/bike/walk
  saved_kg    DECIMAL(8,3),
  eco_score   INT,
  logged_at   TIMESTAMPTZ DEFAULT NOW()
);

-- 에코 배지
CREATE TABLE eco_badges (
  user_id     UUID REFERENCES auth.users,
  badge_type  TEXT,                    -- carbon-zero, green-traveler 등
  earned_at   TIMESTAMPTZ DEFAULT NOW(),
  trail_id    TEXT,
  PRIMARY KEY (user_id, badge_type, trail_id)
);

-- B2B 투어 상품
CREATE TABLE b2b_tours (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  partner_id   UUID,
  trail_id     TEXT,
  title        TEXT,
  eco_grade    TEXT,                   -- ECO_CERTIFIED/TRAIL_LINKED
  price_krw    INT,
  available_from DATE,
  available_to   DATE,
  created_at   TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 7. 성능 목표 (SLA)

| 지표 | 목표 | 구현 방법 |
|---|---|---|
| 트레일 목록 초기 로딩 | < 1.5s | Redis 캐시 + 병렬 API 호출 |
| 상세 페이지 로딩 | < 2.0s | SSR + 이미지 lazy load |
| 탄소 계산 | < 50ms | 클라이언트 사이드 계산 (Zero network) |
| 지도 렌더링 | < 1.0s | Mapbox GL + 웨이포인트 pre-fetch |
| Core Web Vitals LCP | < 2.5s | Next.js Image + Vercel Edge |

---

## 8. 보안 고려사항

| 항목 | 대책 |
|---|---|
| Visit Korea API Key | Vercel Env (서버 사이드만 노출) |
| 사용자 데이터 | Supabase RLS (Row Level Security) |
| B2B API Key | SHA-256 해시 저장, 평문 불저장 |
| CORS | Next.js API Routes allowlist |
| Rate Limiting | Upstash Ratelimit (IP당 100req/min) |
