---
type: idea
id: kculture-pilgrimage
title: "K-Universe — K-컬처 성지순례 + 팬 여행 앱"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T10:00:00Z
status: final
llm_compatibility: universal
aliases: ["K-Universe — K-컬처 성지순례 + 팬 여행 앱"]
---

# 아이디어 6: K-Universe

## 한 줄 정의
K-팝·K-드라마·K-무비 촬영지 및 팬 명소를 다국어 오디오 가이드와 AR 포토 기능으로 체험하는 한류 팬 전용 성지순례 앱.

## 타겟 사용자
- **1차**: 일본·동남아·중국 20-30대 K-팝/K-드라마 팬 외국인 관광객
- **2차**: 한국인 20대 — 아이돌 성지, 드라마 촬영지 방문 콘텐츠 생성자

## 핵심 기능
1. **K-콘텐츠별 성지 지도**: 드라마명·아이돌명·영화명으로 검색 → 관련 방문지 맵핑
2. **현장 오디오 가이드**: "이 장소는 드라마 [이름] X화에서 주인공이 고백한 곳입니다" (다국어)
3. **AR 인증샷**: 드라마 속 명장면 배경과 합성 사진 촬영 기능
4. **팬 여행 코스**: "BTS 24시간 코스", "이민호 드라마 3일 코스" 등 테마 코스 큐레이션
5. **커뮤니티 인증 피드**: 방문 인증 게시 → 팬덤 공유 기능

## 활용 API
- `audio-guide` — 현장 다국어 오디오 해설
- `tourism-info-english` / `tourism-info-japanese` / `tourism-info-chinese-simplified` — 다국어 관광지 정보
- `tourism-photos` — 공식 고화질 관광 사진 (AR 배경 소스)
- `photo-contest-winners` — 감성 콘텐츠 강화
- `visitor-concentration-forecast` — 인기 성지 혼잡도 → 방문 타이밍 추천

## 차별화 포인트
- K-콘텐츠별 성지 정보를 체계화한 전문 앱 없음 (현재 팬들이 직접 조사)
- AR 인증샷 → SNS 바이럴 자연 발생 → 마케팅 비용 최소화
- 팬덤 커뮤니티 결합 → 높은 리텐션 기대

## 공모전 강점
- 한류 관광은 한국관광공사 핵심 추진 사업 → 심사위원 공감대 높음
- 2024년 K-팝 팬 방한 관광객 전체의 35% 추정 → 시장 규모 대형

## 예상 사용 시나리오
```
일본인 팬: "드라마 [이름] 촬영지 보고 싶어요" →
  서울 코스 5개 장소 → 오디오 가이드(일본어) ON →
  현장 AR 인증샷 → 인스타그램 공유 →
  "근처 출연 배우가 다녔다는 카페" 추천
```

## 리스크
- 콘텐츠 저작권 (드라마명·아이돌명 상업적 사용) → 관광 정보 범위로 한정
- 성지 장소 데이터 업데이트 주기 — 크라우드 소싱 + 편집팀 운영 필요

---

## 관련 페이지

**활용 API**
- [[tourism-api/한국관광공사_관광공모전(사진) 수상작 정보|API: 관광공모전(사진) 수상작 정보]]
- [[tourism-api/한국관광공사_일문 관광정보서비스|API: 일문 관광정보서비스]]
- [[tourism-api/한국관광공사_관광지 오디오 가이드정보|API: 관광지 오디오 가이드정보]]
- [[tourism-api/한국관광공사_관광사진 정보|API: 관광사진 정보]]
- [[tourism-api/한국관광공사_관광지 집중률 방문자 추이 예측 정보|API: 관광지 집중률 방문자 추이 예측 정보]]
- [[tourism-api/한국관광공사_영문 관광정보서비스|API: 영문 관광정보서비스]]
- [[tourism-api/한국관광공사_중문 간체 관광정보서비스|API: 중문 간체 관광정보서비스]]

**타겟 페르소나**
- [[personas/김지원, 25세, 그래픽 디자이너|김지원 (20대 솔로)]]

**평가**
- [[ideas/아이디어 10개 사업성 점수화 (Stage 3-B)|사업성 점수화]]

**대회**
- [[competition/2026 관광데이터 활용 공모전 - ① 웹·앱 개발 부문|공모전 개요]]

**유사: AI코스, K-컬처**
- [[ideas/K-Camp Finder - AI 추천 캠핑·글램핑 플랫폼|K-Camp Finder]]
- [[ideas/K-Guide Global - 외국인 전용 다국어 통합 한국 관광 가이드|K-Guide Global]]
- [[ideas/WellKorea - 웰니스 여행 큐레이터 앱|WellKorea]]
- [[ideas/K-Local Explorer - 지역 특화 숨은 명소 발굴 앱|K-Local Explorer]]
- [[ideas/KoreaWellness - 번아웃 직장인을 위한 웰니스 관광 큐레이션|KoreaWellness]]

**유사: AI코스, 혼잡회피**
- [[ideas/KoreaPath AI - 개인화 동선 자동 생성 + 혼잡도 최적화 앱|KoreaPath AI]]
- [[ideas/FreeTrip Korea - 무장애·접근성 특화 관광 플랫폼|FreeTrip Korea]]
- [[ideas/KoreaTrend Radar - 관광 빅데이터 기반 실시간 핫플 추천 앱|KoreaTrend Radar]]
- [[ideas/NightKorea - 한국 야간 관광 특화 앱|NightKorea]]
- [[ideas/PetTrip Korea - 반려동물 동반 여행 전문 플랫폼|PetTrip Korea]]
- [[ideas/LocalSecret - 혼잡 회피 + 숨은 명소 발견 앱|LocalSecret]]

**유사: AI코스, 다국어**
- [[ideas/PetKorea - 반려동물 동반 여행 올인원 앱|PetKorea]]
- [[ideas/GreenTrail Korea - 에코 투어 & 트레킹 가이드|GreenTrail Korea]]

