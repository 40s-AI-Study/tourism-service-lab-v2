---
type: idea
id: multilingual-guide
title: "K-Guide Global — 외국인 전용 다국어 통합 한국 관광 가이드"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-04-17T10:00:00Z
status: draft
llm_compatibility: universal
---

# 아이디어 2: K-Guide Global

## 한 줄 정의
Visit Korea 공식 데이터를 현대적 UX로 재포장해 영·일·중 등 8개 언어로 제공하는 외국인 전용 한국 여행 통합 가이드.

## 타겟 사용자
- **1차**: 일본·중국·동남아 20-30대 FIT 여행자 — K-팝/K-드라마 팬
- **2차**: 영어권 20-40대 — K-컬처 및 역사·자연 관심자

## 핵심 기능
1. **8개 언어 전면 전환**: 앱 진입 시 언어 선택 → 전체 UI/콘텐츠 즉시 전환
2. **다국어 오디오 가이드**: 관광지 현장에서 귀로 듣는 해설 (영/일/중 지원)
3. **혼잡도 기반 방문 타이밍**: "지금 명동 혼잡도 78% — 명동성당은 한산"
4. **할랄·비건 필터**: 동남아 무슬림 + 채식주의자 레스토랑 필터
5. **오프라인 모드**: 로밍 요금 걱정 없이 사전 다운로드 지도·가이드 사용

## 활용 API
- `tourism-info-english` / `tourism-info-japanese` / `tourism-info-chinese-simplified` / `tourism-info-chinese-traditional` — 4개 언어 직접 연계
- `audio-guide` — 현장 오디오 해설
- `visitor-concentration-forecast` — 혼잡도 예측
- `related-attractions` — 연관 관광지 추천
- `photo-contest-winners` — 고화질 공식 관광 사진 (UX 강화)

## 차별화 포인트
- Visit Korea 데이터 신뢰성 + TripAdvisor급 UX + Google Maps 혼잡도 = 세 가지를 하나로
- 중국어 간체·번체 분리 제공 (중국 본토 vs 대만/홍콩) — 세심한 현지화

## 공모전 강점
- 다국어 API 8개 이상 활용 → 데이터 활용 항목(20점) 만점 전략
- 2024년 방한 외래객 1,620만명 시장 타겟 → 사회적 임팩트 명확

## 예상 사용 시나리오
```
일본인 관광객: 앱 실행 → 일본어 선택 →
  "지금 내 주변 관광지" → 경복궁 (음성 가이드 일본어 ON) →
  "근처 맛집" → JCB 카드 가능 식당 필터 → 삼겹살 레스토랑 예약 연동
```

## 리스크
- 현지화 품질 (기계번역 한계) — Visit Korea 공식 번역 데이터 사용으로 극복
- 중국인 대상 WeChat/알리페이 연동은 별도 검토 필요
