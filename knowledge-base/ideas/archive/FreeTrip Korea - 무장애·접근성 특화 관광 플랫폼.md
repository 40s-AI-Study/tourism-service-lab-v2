---
type: idea
id: barrier-free-travel
title: "FreeTrip Korea — 무장애·접근성 특화 관광 플랫폼"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T10:00:00Z
status: final
llm_compatibility: universal
aliases: ["FreeTrip Korea — 무장애·접근성 특화 관광 플랫폼"]
---

# 아이디어 4: FreeTrip Korea

## 한 줄 정의
장애인·시니어·영유아 동반 가족이 접근 가능한 관광지 정보를 제공하고, 무장애 경로 + 혼잡도 + 편의시설 정보를 통합 제공하는 접근성 특화 관광 앱.

## 타겟 사용자
- **1차**: 40-50대 장애인·시니어 동반 가족 여행자 (한국 장애인 263만 + 65세 이상 970만)
- **2차**: 30-40대 영유아(유모차) 동반 부모

## 핵심 기능
1. **접근성 등급 표시**: 관광지별 휠체어 접근 가능 여부, 엘리베이터·경사로 유무 세분화
2. **무장애 코스 자동 생성**: 이동 보조 도구(휠체어·유모차) 기준 최적 동선
3. **편의시설 실시간 위치**: 장애인 화장실, 수유실, 휠체어 대여소 지도 표시
4. **혼잡 시간대 회피**: 이동이 느린 이용자를 위한 한산한 시간대 우선 추천
5. **대중교통 무장애 연계**: 저상버스·지하철 엘리베이터 경로 정보 통합

## 활용 API
- `barrier-free-travel` — 장애인·어르신·영유아 동반 관광지 접근성 데이터 (핵심)
- `visitor-concentration-forecast` — 혼잡도 예측 (이동 취약자 배려)
- `tourism-info-korean` / `tourism-info-english` — 기본 관광지 정보
- `related-attractions` — 접근성 확보된 연관 관광지 추천

## 차별화 포인트
- 공식 Visit Korea `barrier-free-travel` API를 실용적 앱으로 구현한 서비스 전무
- 고령화 사회(2026년 초고령사회 진입 예정) 트렌드에 선제 대응
- 공모전 **사회적 가치** 심사 항목 직접 연계 → 가점 가능성

## 공모전 강점
- 사회적 약자 배려 → 심사위원 긍정 평가 기대
- 지역 특화 가점(RTO 연계) — 접근성 우수 지역 특화 가능

## 예상 사용 시나리오
```
사용자: 80세 어머니와 함께 경주 여행 계획 →
  "휠체어 가능" 필터 ON →
  불국사 (휠체어 접근로 있음, 오전 9시 한산) →
  첨성대 (야외 평지, 접근 용이) →
  경주 한식당 (장애인 화장실 있음) →
  숙소: 배리어프리 인증 호텔
```

## 리스크
- API 데이터 현실과 괴리 (현장 점검 정보가 오래됐을 수 있음) → 크라우드 소싱 보완
- 앱 인지도 확보 난이도 — 복지관·요양원 B2B 파트너십으로 초기 사용자 확보 전략

---

## 관련 페이지

**활용 API**
- [[tourism-api/한국관광공사_무장애 여행 정보|API: 무장애 여행 정보]]
- [[tourism-api/한국관광공사_관광지별 연관 관광지 정보|API: 관광지별 연관 관광지 정보]]
- [[tourism-api/한국관광공사_국문 관광정보 서비스|API: 국문 관광정보 서비스]]
- [[tourism-api/한국관광공사_관광지 집중률 방문자 추이 예측 정보|API: 관광지 집중률 방문자 추이 예측 정보]]
- [[tourism-api/한국관광공사_영문 관광정보서비스|API: 영문 관광정보서비스]]

**타겟 페르소나**
- [[personas/최동훈, 44세, 중학교 교사 (초등생 자녀 2명)|최동훈 (40대 가족)]]

**평가**
- [[ideas/아이디어 10개 사업성 점수화 (Stage 3-B)|사업성 점수화]]

**대회**
- [[competition/2026 관광데이터 활용 공모전 - ① 웹·앱 개발 부문|공모전 개요]]

**유사: AI코스, 가족여행**
- [[ideas/K-Camp Finder - AI 추천 캠핑·글램핑 플랫폼|K-Camp Finder]]
- [[ideas/KoreaPath AI - 개인화 동선 자동 생성 + 혼잡도 최적화 앱|KoreaPath AI]]
- [[ideas/PetTrip Korea - 반려동물 동반 여행 전문 플랫폼|PetTrip Korea]]
- [[ideas/AccessKorea - 무장애 여행 통합 플랫폼|AccessKorea]]
- [[ideas/FamilyKorea - 가족여행 올인원 스마트 플래너|FamilyKorea]]

**유사: AI코스, 혼잡회피**
- [[ideas/KoreaTrend Radar - 관광 빅데이터 기반 실시간 핫플 추천 앱|KoreaTrend Radar]]
- [[ideas/K-Universe - K-컬처 성지순례 + 팬 여행 앱|K-Universe]]
- [[ideas/PetKorea - 반려동물 동반 여행 올인원 앱|PetKorea]]
- [[ideas/NightKorea - 한국 야간 관광 특화 앱|NightKorea]]
- [[ideas/K-Guide Global - 외국인 전용 다국어 통합 한국 관광 가이드|K-Guide Global]]
- [[ideas/WellKorea - 웰니스 여행 큐레이터 앱|WellKorea]]
- [[ideas/GreenTrail Korea - 에코 투어 & 트레킹 가이드|GreenTrail Korea]]
- [[ideas/LocalSecret - 혼잡 회피 + 숨은 명소 발견 앱|LocalSecret]]
- [[ideas/K-Local Explorer - 지역 특화 숨은 명소 발굴 앱|K-Local Explorer]]
- [[ideas/KoreaWellness - 번아웃 직장인을 위한 웰니스 관광 큐레이션|KoreaWellness]]

