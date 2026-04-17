---
type: persona
id: p5-foreign-30s-business-leisure
title: "David Park, 35, Senior Product Manager (USA)"
author_agent: uxdesigner
author_model: claude-sonnet-4-6
created: 2026-04-17T09:00:00Z
status: draft
llm_compatibility: universal
aliases: ["David Park, 35, Senior Product Manager (USA)"]
---

# P5: David Park — 외국인 30대 비즈니스/여가 혼합 여행자

## 기본 정보

- **이름**: David Park (박도윤)
- **나이**: 35세
- **직업**: 미국 테크 기업 시니어 PM
- **국적**: 미국 (재미교포 2세)
- **언어**: 영어(모국어), 한국어(기초 회화 가능), 중국어(없음)
- **방문 패턴**: 출장 + 여가 혼합, 연 2-3회, 체류 7-10일

## 배경 (서사)

도윤은 한국계 미국인으로 부모님 방문 겸 출장을 자주 온다. 비즈니스 일정이 끝나면 3-4일을 여가로 활용하는 "블레저(Bleisure)" 여행자다. 미국에서는 Google Maps와 Yelp로 모든 것을 해결하는 데 익숙하지만, 한국에서는 Google Maps 데이터가 부정확하고 좋은 영어 정보 소스가 없어 불편을 느낀다. K-컬처에 관심이 높고 서울 외 지방(경주, 제주) 심층 탐방을 원하지만 영어 투어 정보가 부족하다.

## 목표 (Goals)

- Google Maps 수준의 정확한 영어 관광 정보를 한국 전국에서 사용
- 바쁜 출장 중 짬나는 시간(반나절~하루)에 맞는 간결한 코스 추천
- 제주·경주 등 지방 여행 시 영어 오디오 가이드로 역사·문화 이해
- 한국 음식 문화 탐방 (Reddit r/koreatravel 추천 기반 맛집)

## 고민 (Pain Points)

- **Google Maps 데이터 불일치**: 폐업·이전된 식당이 여전히 등록, 현지 도착 후 낭패
- **영어 정보 단절**: 서울 외 지방에서 영어 안내판·메뉴 부족, 투어 정보도 한국어 위주
- **짧은 시간 최적화 부재**: "오후 3시간짜리 코스" 같은 시간 기반 추천 서비스 없음

## 관광 패턴

- **여행 빈도**: 연 2-3회 (7-10일 체류, 블레저)
- **선호 유형**: K-컬처·역사 탐방, 미식 모험, 자연(제주 하이킹, 설악산), 커피 문화
- **예산**: 1박 10-20만원 (비즈니스 호텔 선호), 식비 제한 없음
- **동반자**: 혼자(50%), 출장 동료(30%), 파트너(20%)
- **정보 탐색 채널**: Google, Reddit (r/koreatravel), TripAdvisor, 유튜브 영어 채널

## 기술 친숙도

very high — PM으로서 UX에 민감, 앱 품질에 높은 기준, 불편한 UX 즉시 이탈

## 대표 시나리오

서울 출장 중 수요일 오후가 비었다. 앱에 "지금 위치 기준 3시간, 영어, K-역사"를 입력하면 앱이 경복궁→북촌 한옥마을→인사동 코스를 제안하고, 각 장소에서 영어 오디오 가이드를 자동 재생한다. 주말엔 경주 당일치기를 위해 실시간 혼잡도를 확인하고 KTX 시간을 함께 조회한다.

## 관련 API 시사점

- `tourism-info-english` — 전국 관광지 영어 상세 정보
- `audio-guide` — 영어 현장 오디오 해설 (경복궁, 경주 등)
- `visitor-concentration-forecast` — 인기 관광지 혼잡도 예측
- `durunubi-trails` — 제주 올레 등 트레킹 코스 영어 안내

---

## 관련 페이지

**기반 리서치**
- [[market-research/20-40대 한국인 관광 니즈 Raw Data (UXDesigner 입력용)|20-40대 한국인 관광 니즈 Raw Data (UXD]]
- [[market-research/경쟁 서비스 Gap 분석 + 기회 영역|경쟁 서비스 Gap 분석 + 기회 영역]]
- [[market-research/한국 관광 트렌드 통계 (2024-2025)|한국 관광 트렌드 통계 (2024-2025)]]
- [[market-research/기존 관광 서비스 상세 기능 비교 매트릭스|기존 관광 서비스 상세 기능 비교 매트릭스]]
- [[market-research/외국인 관광객 니즈 분석|외국인 관광객 니즈 분석]]

