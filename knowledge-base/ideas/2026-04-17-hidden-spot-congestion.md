---
type: idea
id: hidden-spot-congestion
title: "LocalSecret — 혼잡 회피 + 숨은 명소 발견 앱"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T10:00:00Z
status: draft
llm_compatibility: universal
aliases: ["LocalSecret — 혼잡 회피 + 숨은 명소 발견 앱"]
---

# 아이디어 7: LocalSecret

## 한 줄 정의
실시간 혼잡도 데이터와 빅데이터 트렌드를 기반으로 붐비지 않는 숨은 명소와 최적 방문 타이밍을 추천하는 혼잡 회피 특화 앱.

## 타겟 사용자
- **1차**: 20-30대 한국인 — SNS에서 본 관광지가 사람으로 가득 찬 경험을 한 MZ세대
- **2차**: 영어권 외국인 — 서울 관광지 외 "진짜 한국"을 찾는 여행자

## 핵심 기능
1. **실시간 혼잡도 지도**: 현재 관광지별 혼잡도 히트맵 표시
2. **"지금 한산한 곳" 즉시 추천**: 내 주변 반경 X km 내 현재 혼잡도 낮은 관광지 목록
3. **방문 타이밍 알림**: "경복궁 혼잡도 40% 이하 알림 받기" 설정 → 푸시 알림
4. **지역 관광 다양성 지수**: `area-tourism-diversity` 활용 — 덜 알려진 지역 발굴
5. **숨은 명소 피드**: 빅데이터 기반 "요즘 뜨는 곳" vs "아직 알려지지 않은 곳" 탭 구분

## 활용 API
- `visitor-concentration-forecast` — 향후 30일 관광지 혼잡도 예측 (핵심)
- `area-tourism-demand-density` — 지역별 관광 수요 밀집도
- `area-tourism-diversity` — 관광 다양성 지수 (덜 알려진 지역 발굴)
- `related-attractions` — 혼잡한 곳의 대체 관광지 추천
- `tourism-big-data` — 빅데이터 트렌드 기반 "뜨는 곳" 추천

## 차별화 포인트
- Google Maps Popular Times는 주간 평균치 — 본 앱은 **향후 30일 예측** 데이터 제공
- MZ세대 55% 이상이 혼잡 회피 여행 선호 (Nielsen 2024) → 명확한 수요
- "숨은 명소" 카테고리 + 혼잡도 결합 = 완전히 새로운 여행 발견 경험

## 공모전 강점
- `visitor-concentration-forecast` API의 핵심 가치를 가장 직접적으로 구현
- 차별화 포인트가 경쟁 서비스 대비 명확하게 설명 가능

## 예상 사용 시나리오
```
사용자: 이번 주말 서울 근교 여행 계획 →
  현재 화면: "북한산 혼잡도 82% (매우 붐빔)" →
  앱 추천: "대신 여기 어때요? 양주 불곡산 혼잡도 12% (한산)" →
  "남양주 수종사 — 요즘 뜨는 곳, 아직 덜 알려짐" →
  방문 타이밍: "토요일 오전 7시-10시가 가장 한산"
```

## 리스크
- 앱이 추천한 곳이 유명해지면 역설적으로 혼잡해지는 문제 → 추천 다양화 알고리즘 필요
- 혼잡도 예측 정확도 의존 → API 데이터 신뢰성이 서비스 품질 좌우

---

## 관련 페이지

**활용 API**
- [[tourism-api/tourism-big-data|API: 관광빅데이터 정보서비스]]
- [[tourism-api/related-attractions|API: 관광지별 연관 관광지 정보]]
- [[tourism-api/area-tourism-diversity|API: 지역별 관광 다양성]]
- [[tourism-api/visitor-concentration-forecast|API: 관광지 집중률 방문자 추이 예측 정보]]
- [[tourism-api/area-tourism-demand-density|API: 지역별 관광 수요 강도]]

**평가**
- [[ideas/00-business-scoring|사업성 점수화]]

**대회**
- [[competition/overview|공모전 개요]]

**유사: AI코스, 혼잡회피**
- [[ideas/2026-04-17-k-camp-finder|K-Camp Finder]]
- [[ideas/2026-04-17-ai-course-generator|KoreaPath AI]]
- [[ideas/2026-04-17-barrier-free-travel|FreeTrip Korea]]
- [[ideas/2026-04-17-korea-trend-radar|KoreaTrend Radar]]
- [[ideas/2026-04-17-kculture-pilgrimage|K-Universe]]
- [[ideas/2026-04-17-pet-korea|PetKorea]]
- [[ideas/2026-04-17-night-tourism|NightKorea]]
- [[ideas/2026-04-17-multilingual-guide|K-Guide Global]]
- [[ideas/2026-04-17-pet-friendly-travel|PetTrip Korea]]
- [[ideas/2026-04-17-wellness-tour|WellKorea]]
- [[ideas/2026-04-17-eco-green-trail|GreenTrail Korea]]
- [[ideas/2026-04-17-k-local-explorer|K-Local Explorer]]
- [[ideas/2026-04-17-korea-wellness|KoreaWellness]]

