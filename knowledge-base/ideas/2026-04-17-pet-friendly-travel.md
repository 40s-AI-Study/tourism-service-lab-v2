---
type: idea
id: pet-friendly-travel
title: "PetTrip Korea — 반려동물 동반 여행 전문 플랫폼"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T10:00:00Z
status: draft
llm_compatibility: universal
aliases: ["PetTrip Korea — 반려동물 동반 여행 전문 플랫폼"]
---

# 아이디어 3: PetTrip Korea

## 한 줄 정의
반려동물 가구 600만 시대, 펫 동반 가능한 숙소·맛집·관광지·레포츠를 한 앱에서 확인하고 반려인 커뮤니티와 연결되는 전문 여행 플랫폼.

## 타겟 사용자
- **1차**: 한국인 20-30대 반려동물 보호자 — 강아지/고양이와 여행하는 솔로/커플
- **2차**: 한국인 30-40대 가족 — 반려동물을 가족처럼 여기는 펫 가족

## 핵심 기능
1. **펫 동반 관광지 7개 카테고리 통합**: 관광지·문화시설·축제·숙박·음식점·레포츠·쇼핑 전 카테고리
2. **반려동물 프로필 기반 필터**: 견종·크기·나이 → 입장 가능 장소 자동 필터
3. **펫 동반 코스 추천**: 반려동물 동반 검증 코스 (산책로 + 카페 + 숙소 원스톱)
4. **반려인 커뮤니티**: 실제 방문 후기 + 팁 공유 (인증 기반)
5. **혼잡도 알림**: "이번 주말 반려동물 공원 혼잡도 낮은 시간대 추천"

## 활용 API
- `pet-friendly-travel` — 반려동물 동반 가능 7개 카테고리 관광 데이터 (핵심)
- `visitor-concentration-forecast` — 혼잡도 예측
- `tourism-info-korean` — 기본 관광지 정보 연계
- `related-attractions` — 반려동물 친화 연관 관광지 추천

## 차별화 포인트
- 단일 앱에서 펫 동반 **전 카테고리** 통합 정보 제공 — 기존 어떤 서비스도 없음
- 커뮤니티 기반 실제 방문 검증 → 광고성 정보 걸러냄
- 반려동물 프로필 기반 개인화 → "우리 강아지(소형견 5kg) 입장 가능"

## 공모전 강점
- `pet-friendly-travel` API 집중 활용 + 커뮤니티 효과 → 독창성 어필
- 반려동물 시장 25% 연간 성장 → 시장 타당성 명확

## 예상 사용 시나리오
```
사용자: 강아지(말티즈, 3kg) 프로필 등록 →
  "이번 주말 경기도 반려동물 코스" 요청 →
  가평 펫카페 → 반려동물 동반 글램핑 → 산책로 코스 제안 →
  커뮤니티에서 "가평 OO 카페 강아지 목줄 필수" 팁 확인
```

## 리스크
- `pet-friendly-travel` API 데이터 최신성 유지 (폐업·정책 변경)
- 커뮤니티 어뷰징 방지 운영 정책 필요

---

## 관련 페이지

**활용 API**
- [[tourism-api/related-attractions|API: 관광지별 연관 관광지 정보]]
- [[tourism-api/tourism-info-korean|API: 국문 관광정보 서비스]]
- [[tourism-api/pet-friendly-travel|API: 반려동물_동반여행_서비스]]
- [[tourism-api/visitor-concentration-forecast|API: 관광지 집중률 방문자 추이 예측 정보]]

**타겟 페르소나**
- [[personas/p1-korean-20s-solo|김지원 (20대 솔로)]]
- [[personas/p2-korean-30s-couple|박민준·이수연 (30대 커플)]]
- [[personas/p3-korean-40s-family|최동훈 (40대 가족)]]

**평가**
- [[ideas/00-business-scoring|사업성 점수화]]

**대회**
- [[competition/overview|공모전 개요]]

**유사: AI코스, 가족여행**
- [[ideas/2026-04-17-k-camp-finder|K-Camp Finder]]
- [[ideas/2026-04-17-ai-course-generator|KoreaPath AI]]
- [[ideas/2026-04-17-barrier-free-travel|FreeTrip Korea]]
- [[ideas/2026-04-17-access-korea|AccessKorea]]
- [[ideas/2026-04-17-family-trip-planner|FamilyKorea]]

**유사: AI코스, 혼잡회피**
- [[ideas/2026-04-17-korea-trend-radar|KoreaTrend Radar]]
- [[ideas/2026-04-17-kculture-pilgrimage|K-Universe]]
- [[ideas/2026-04-17-night-tourism|NightKorea]]
- [[ideas/2026-04-17-multilingual-guide|K-Guide Global]]
- [[ideas/2026-04-17-hidden-spot-congestion|LocalSecret]]
- [[ideas/2026-04-17-k-local-explorer|K-Local Explorer]]
- [[ideas/2026-04-17-korea-wellness|KoreaWellness]]

**유사: AI코스, 반려동물**
- [[ideas/2026-04-17-pet-korea|PetKorea]]

**유사: AI코스, 캠핑**
- [[ideas/2026-04-17-wellness-tour|WellKorea]]
- [[ideas/2026-04-17-eco-green-trail|GreenTrail Korea]]

