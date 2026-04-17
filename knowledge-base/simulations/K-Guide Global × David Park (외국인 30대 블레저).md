---
type: simulation
id: sim-10-multilingual-guide-x-p5-foreign-30s-business-leisure
title: "K-Guide Global × David Park (외국인 30대 블레저)"
author_agent: simulator
author_model: claude-sonnet-4-6
created: 2026-04-17T14:45:00Z
status: draft
llm_compatibility: universal
related:
  - "[[K-Guide Global - 외국인 전용 다국어 통합 한국 관광 가이드]]"
  - "[[David Park, 35, Senior Product Manager (USA)]]"
aliases: ["K-Guide Global × David Park (외국인 30대 블레저)"]
---

# SIM-10: K-Guide Global × David Park (외국인 30대 블레저)

## 시나리오

David Park(35세, 미국 테크 PM)은 서울 출장 3일차, 오후가 비었다. Google Maps에서 경복궁을 검색했지만 영어 오디오 가이드가 없어 아쉬웠다. 호텔 컨시어지가 K-Guide Global을 추천해 설치한다.

---

## 사용자 여정

### 1단계: 진입
- 앱 실행 → **"English"** 즉시 선택
- 전체 UI 영어 전환 완료, 직관적 메인 화면
- "Gyeongbokgung" 타이핑 → 즉시 결과 표시
- 소요 시간: 약 15초

### 2단계: 행동
- 경복궁 상세 정보 확인: 영어 설명, 운영 시간, 입장료, 교통 안내 모두 정확
- 혼잡도 확인: 현재 오후 2시 혼잡도 72%(혼잡) → "4시 이후 한산" 알림
- 오후 4시 방문으로 계획 변경 → 북촌 한옥마을 먼저 탐방
- 경복궁 영어 오디오 가이드 실행: 조선 시대 역사 해설 청취
- `related-attractions`로 인근 국립민속박물관·청와대 사랑채 발견 → 코스 추가
- 주말 경주 당일치기 계획: 경주 관광지 영어 오디오 가이드 사전 체크 완료

### 3단계: 결과
- 경복궁 혼잡 시간대 회피 → 한적한 관람 성공
- 오디오 가이드 덕분에 역사적 맥락 이해 → Reddit r/koreatravel에 "Best English Korea travel app" 후기 게시
- 경주 오디오 가이드 미리보기 후 "주말에 꼭 가야겠다" → 당일치기 예약

---

## 평가

| 항목 | 점수 (1-10) | 근거 |
|---|---|---|
| 유용성 | **9** | 영어 정보 정확성 + 혼잡도 + 오디오 가이드 = David의 핵심 Pain Point 해소 |
| 사용 편의 | **9** | Google Maps 수준의 직관적 UX, 영어 네이티브 지원 |
| 구현 타당성 | **9** | 영어 API 실제 제공 중. Google Maps 대비 경쟁 우위 명확 |

**종합 점수: 27/30**

---

## Pass/Fail 판정

> **✅ PASS**

P5 David Park은 K-Guide Global의 핵심 타겟 사용자다. Google Maps의 데이터 부정확성과 영어 오디오 가이드 부재라는 두 가지 Pain Point를 모두 해소한다. 영어권 블레저 여행자에게 Google Maps 대체재로 포지셔닝 가능.

---

## 개선 제안

1. **시간 기반 코스 추천**: "Available for 3 hours from now" 입력 → 이동 시간 포함 최적 코스 생성 (현재 미지원)
2. **비즈니스 여행자 모드**: 반나절/저녁 시간대 프리셋 코스 → 출장 중 짬나는 시간 즉각 활용
3. **Reddit·TripAdvisor 연계 리뷰**: 영어권 여행자가 신뢰하는 플랫폼 리뷰를 앱 내에서 바로 확인 → 전환율 향상
4. **KTX 시간표 통합**: 서울-경주 당일치기 계획 시 KTX 시간표를 앱 내 표시하면 블레저 여행자 완결형 경험 제공
