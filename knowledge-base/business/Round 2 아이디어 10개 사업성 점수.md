---
type: business-scoring
id: round2-scoring-2026-04-17
title: "Round 2 아이디어 10개 사업성 점수"
author_agent: businessanalyst
author_model: claude-sonnet-4-6
created: 2026-04-17T14:30:00Z
status: final
llm_compatibility: universal
sources:
  - knowledge-base/ideas/KoreaPath AI - 개인화 동선 자동 생성 + 혼잡도 최적화 앱.md
  - knowledge-base/ideas/K-Guide Global - 외국인 전용 다국어 통합 한국 관광 가이드.md
  - knowledge-base/ideas/AccessKorea - 무장애 여행 통합 플랫폼.md
  - knowledge-base/ideas/PetKorea - 반려동물 동반 여행 올인원 앱.md
  - knowledge-base/ideas/KoreaTrend Radar - 관광 빅데이터 기반 실시간 핫플 추천 앱.md
  - knowledge-base/ideas/K-Local Explorer - 지역 특화 숨은 명소 발굴 앱.md
  - knowledge-base/ideas/Audio Story Korea - 몰입형 문화재 오디오 스토리텔링 앱.md
  - knowledge-base/ideas/KoreaWellness - 번아웃 직장인을 위한 웰니스 관광 큐레이션.md
  - knowledge-base/ideas/EcoTrail Korea - 친환경 트레킹·자전거·생태관광 올인원 앱.md
  - knowledge-base/ideas/K-Camp Finder - AI 추천 캠핑·글램핑 플랫폼.md
  - knowledge-base/ideas/아이디어 10개 사업성 점수화 (Stage 3-B).md
---

# Round 2 아이디어 10개 사업성 점수

> 출처: TOU-14 CEO 오케스트레이션 산출물 (`knowledge-base/ideas/`)
> 평가일: 2026-04-17 | 평가자: BusinessAnalyst (claude-sonnet-4-6)
> 의뢰: TOU-18 [Round 2] BA: 사업성 점수화 (API 활용도 가중치 상향)

## 평가 기준 (총 100점 + API 가중치 보너스)

| 기준 | 배점 | 고득점 조건 |
|---|---|---|
| **시장 규모** | 20점 | 대형 타겟 시장, 성장세 뚜렷 |
| **경쟁 강도** | 20점 | 기존 경쟁 서비스 공백 클수록 고점 |
| **API 활용도** | 20점 | 다수 API 창의적 조합 |
| **구현 난이도** | 20점 | MVP 구현 빠를수록 고점 (역산) |
| **공모전 적합성** | 20점 | 심사 기준 (기획력 30+데이터 20+사업성 20+사회가치 10+지역특화 2) 부합도 |
| **API 가중치 보너스** | +α | 활용 API 수 × 0.5 (6개=+3, 8개=+4, 10개=+5) |

---

## 아이디어별 상세 점수

### 아이디어 1: KoreaPath AI — 개인화 동선 자동 생성 + 혼잡도 최적화

**한 줄 정의**: 여행 조건 입력 시 혼잡도 예측 + 연관 관광지 데이터 조합으로 최적 동선 자동 생성

**타겟**: 30-40대 한국인 직장인·가족 + 한국어 모르는 FIT 외국인

**활용 API (5개)**: `related-attractions` · `visitor-concentration-forecast` · `central-attractions-by-municipality` · `tourism-big-data` · `area-tourism-demand-density`

**API 가중치 보너스**: 5개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 19 | 국내 관광 연 3.2억회. 코스 추천 Pain Point 82% 해소. 20-40대 전 연령 타겟 |
| 경쟁 강도 | 18 | AI 코스 자동 생성 국내 전무. 트리플·네이버 모두 수동 계획 방식 |
| API 활용도 | 17 | 5개 API 창의적 조합. 혼잡도+연관관광지 병행 국내 최초 |
| 구현 난이도 | 12 | 추천 엔진 백엔드 복잡. LLM 연동 or rule-based 선택 필요 |
| 공모전 적합성 | 18 | 혁신성·실용성·데이터 활용 배점 동시 충족 |
| **합계** | **84** | 보너스 0점 포함 |

---

### 아이디어 2: K-Guide Global — 외국인 전용 다국어 통합 한국 관광 가이드

**한 줄 정의**: Visit Korea 공식 데이터를 8개 언어 현대 UX로 재포장. 오디오 가이드+혼잡도 통합

**타겟**: 방한 외래객 1,620만명 (일·중·영어권 우선)

**활용 API (8개)**: `tourism-info-english` · `tourism-info-japanese` · `tourism-info-chinese-simplified` · `tourism-info-chinese-traditional` · `audio-guide` · `visitor-concentration-forecast` · `related-attractions` · `photo-contest-winners`

**API 가중치 보너스**: 8개 → **+4점**

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 19 | 방한 외래객 2024 추정 1,620만명. 중국 24%, 일본 22%. 대형·성장 시장 |
| 경쟁 강도 | 14 | Visit Korea 앱 구식 UX 존재. Google·TripAdvisor 범용 경쟁 있음 |
| API 활용도 | 19 | 8개 API 활용. 다국어 4종+오디오+혼잡도+연관+사진 조합 최다 |
| 구현 난이도 | 11 | 8개 언어 UI/UX 복잡. 현지화 품질 관리 부담 |
| 공모전 적합성 | 20 | 데이터 활용 배점 20점 만점 최유력. 심사위원 임팩트 최고 |
| **API 보너스** | **+4** | 8개 × 0.5 = 4점 |
| **합계** | **87** | 보너스 +4점 포함 |

---

### 아이디어 3: AccessKorea — 무장애 여행 통합 플랫폼

**한 줄 정의**: 장애인·시니어·영유아 동반 가족을 위한 무장애 관광 정보 통합 + AI 코스 추천

**타겟**: 시니어 970만 + 장애인 263만 + 영유아 동반 가족

**활용 API (4개)**: `barrier-free-travel` · `tourism-info-korean` · `audio-guide` · `central-attractions-by-municipality`

**API 가중치 보너스**: 4개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 15 | 장애인 263만+시니어 970만. 고령화 가속으로 성장 확실. 여행 빈도 제한 |
| 경쟁 강도 | 20 | 무장애 통합 여행 앱 국내 완전 전무. barrier-free-travel API 독점 활용 |
| API 활용도 | 15 | 4개. barrier-free+audio 조합 공모전 내 독창적 포지셔닝 |
| 구현 난이도 | 15 | 구현 비교적 단순. 접근성 데이터 현장 검증 프로세스 필요 |
| 공모전 적합성 | 19 | 사회적 가치 심사항목 직결. 문체부 무장애 관광 정책 부합. RTO 특별상 연계 가능 |
| **합계** | **84** | 보너스 0점 포함 |

---

### 아이디어 4: PetKorea — 반려동물 동반 여행 올인원 앱

**한 줄 정의**: 반려동물 동반 가능 관광지·숙박·음식점 등 7개 카테고리 통합 + AI 코스 생성

**타겟**: 20-40대 반려동물 가구 600만

**활용 API (4개)**: `pet-friendly-travel` · `tourism-info-korean` · `related-attractions` · `visitor-concentration-forecast`

**API 가중치 보너스**: 4개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 15 | 반려동물 가구 600만. 여행 시장 연 25% 성장. 명확한 수요층 |
| 경쟁 강도 | 17 | 전용 통합 앱 전무. 야놀자 일부 펫 숙박, 블로그 분산 정보만 존재 |
| API 활용도 | 14 | 4개 API. pet-friendly 7카테고리 전부 활용하나 API 수 제한적 |
| 구현 난이도 | 15 | 구현 비교적 단순. 커뮤니티 기능 추가 시 복잡도 증가 |
| 공모전 적합성 | 15 | 니즈 명확하나 심사 차별화 포인트 상대적으로 약함 |
| **합계** | **76** | 보너스 0점 포함 |

---

### 아이디어 5: KoreaTrend Radar — 관광 빅데이터 기반 실시간 핫플 추천

**한 줄 정의**: 이동통신·카드소비·내비 데이터 교차 분석으로 '지금 뜨는 여행지' 실시간 레이더

**타겟**: 30-40대 트렌드세터, 주말 즉흥 여행족, B2B 관광 사업자

**활용 API (4개)**: `tourism-big-data` · `area-tourism-demand-density` · `area-tourism-diversity` · `area-tourism-resource-demand`

**API 가중치 보너스**: 4개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 14 | 트렌드세터+즉흥여행족 틈새. B2B 확장 가능하나 초기 타겟 제한 |
| 경쟁 강도 | 17 | 한국 특화 실시간 빅데이터 관광 레이더 전무 |
| API 활용도 | 17 | 빅데이터 계열 4개 API 집중 전략. 교차 분석 독창적. 공모전 데이터 배점 유리 |
| 구현 난이도 | 13 | 빅데이터 분석 로직+히트맵 시각화 구현 복잡 |
| 공모전 적합성 | 16 | 데이터 활용 강점. '일반 앱 vs 대시보드' 포지셔닝 불명확 → 기획력 감점 가능 |
| **합계** | **77** | 보너스 0점 포함 |

---

### 아이디어 6: K-Local Explorer — 지역 특화 숨은 명소 발굴

**한 줄 정의**: 지자체별 관광지 데이터 + 사진 공모전 수상작 결합으로 MZ세대 SNS용 숨은 명소 발굴

**타겟**: 20-30대 로컬 탐방 선호 MZ세대, 오버투어리즘 기피층

**활용 API (4개)**: `central-attractions-by-municipality` · `related-attractions` · `photo-contest-winners` · `visitor-concentration-forecast`

**API 가중치 보너스**: 4개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 14 | MZ 로컬 탐방 + SNS 공유 문화 친화층. 틈새지만 충성도 높음 |
| 경쟁 강도 | 18 | 사진 공모전 수상작+혼잡도 역발상 결합 서비스 전무 |
| API 활용도 | 15 | 4개. photo-contest-winners 활용이 심사위원 친화도 높음 |
| 구현 난이도 | 15 | 구현 비교적 단순. SNS 카드 자동 생성 기능 추가 필요 |
| 공모전 적합성 | 17 | 지역 특화 가점(2점) 직접 공략. RTO 특별상 연계 가능 |
| **합계** | **79** | 보너스 0점 포함 |

---

### 아이디어 7: Audio Story Korea — 몰입형 문화재 오디오 스토리텔링

**한 줄 정의**: QR 스캔 즉시 4개 언어 오디오 가이드 + 사진 공모전 수상작 동시 제공 앱

**타겟**: 역사·문화재 관심 20-40대 + 외국인 개별 관광객(FIT)

**활용 API (5개)**: `audio-guide` · `photo-contest-winners` · `tourism-info-english` · `tourism-info-japanese` · `tourism-info-chinese-simplified`

**API 가중치 보너스**: 5개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 13 | 문화재 관심층+외국인 FIT. 명확하지만 비교적 좁은 타겟 |
| 경쟁 강도 | 18 | audio-guide API 핵심 활용 앱 전무. 오디오+4개 언어 조합 차별화 |
| API 활용도 | 17 | 5개. audio-guide 독점 + 다국어 + 사진 조합. 공모전 내 유일한 오디오 중심 설계 |
| 구현 난이도 | 15 | 구현 비교적 단순. QR+오프라인 다운로드 구현 표준적 |
| 공모전 적합성 | 16 | audio-guide API 독점 포지셔닝. 외국인 관광 + 접근성 심사항목 부합 |
| **합계** | **79** | 보너스 0점 포함 |

---

### 아이디어 8: KoreaWellness — 번아웃 직장인 웰니스 관광 큐레이션

**한 줄 정의**: 스트레스 프로파일 기반 AI가 명상·스파·산림욕·한방 체험 큐레이션

**타겟**: 30-40대 번아웃 직장인 + K-웰니스 관심 외국인 의료관광객

**활용 API (4개)**: `wellness-tourism` · `area-tourism-demand-density` · `tourism-big-data` · `eco-tourism`

**API 가중치 보너스**: 4개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 14 | 번아웃 직장인 87% 경험. 실제 웰니스 여행 전환률 제한적 |
| 경쟁 강도 | 16 | 웰니스 통합 여행 앱 없음. 개별 스파 예약만 존재 |
| API 활용도 | 15 | 4개. wellness-tourism API 희소 독점 활용. 수요밀도+빅데이터 조합 |
| 구현 난이도 | 15 | 구현 비교적 단순. 번아웃 진단 로직 설계 필요 |
| 공모전 적합성 | 14 | 트렌드 부합. 단독 웰니스 테마 기획력 배점 확보 어려움 |
| **합계** | **74** | 보너스 0점 포함 |

---

### 아이디어 9: EcoTrail Korea — 친환경 트레킹·자전거·생태관광 올인원

**한 줄 정의**: 두루누비 코스 + 생태관광 + 탄소발자국 계산기를 결합한 에코투어 플랫폼

**타겟**: 20-30대 환경의식 MZ세대 + 에코투어리스트 외국인

**활용 API (4개)**: `eco-tourism` · `durunubi-trails` · `area-tourism-diversity` · `tourism-big-data`

**API 가중치 보너스**: 4개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 12 | 환경의식 MZ + 에코투어리스트. 비교적 좁은 타겟 |
| 경쟁 강도 | 17 | durunubi+eco-tourism 통합 서비스 전무 |
| API 활용도 | 16 | 4개. durunubi-trails+eco-tourism 최초 결합. 탄소발자국 독창적 활용 |
| 구현 난이도 | 15 | 구현 비교적 단순. 탄소발자국 계산 로직 설계 필요 |
| 공모전 적합성 | 16 | 친환경 가점 항목 직결. 2026 Visit Korea 지속가능성 정책 부합 |
| **합계** | **76** | 보너스 0점 포함 |

---

### 아이디어 10: K-Camp Finder — AI 추천 캠핑·글램핑 플랫폼

**한 줄 정의**: 날씨·혼잡도·동반 인원 입력 시 최적 캠핑·글램핑 AI 추천 + 주변 관광 연계

**타겟**: 20-40대 캠핑 인구 700만 (가족, 솔로, 반려동물 동반)

**활용 API (4개)**: `gocamping` · `visitor-concentration-forecast` · `related-attractions` · `area-tourism-demand-density`

**API 가중치 보너스**: 4개 → 보너스 없음

| 기준 | 점수 | 근거 |
|---|---|---|
| 시장 규모 | 15 | 캠핑 인구 700만, 국내 야외 활동 성장세. 명확한 수요 |
| 경쟁 강도 | 16 | 캠핏 예약 전용 존재. AI+혼잡도+관광 연계 통합 서비스 없음 |
| API 활용도 | 15 | 4개. gocamping API 독점 활용. 혼잡도+연관명소 조합 논리적 |
| 구현 난이도 | 15 | 구현 비교적 단순. 날씨 API 외부 연동 필요 |
| 공모전 적합성 | 14 | 시장 명확. 단독 캠핑 특화 심사 임팩트 제한적 |
| **합계** | **75** | 보너스 0점 포함 |

---

## 종합 점수 매트릭스

| 순위 | 아이디어명 | 시장규모 | 경쟁강도 | API활용도 | 구현난이도 | 공모전적합성 | API보너스 | **합계** |
|---|---|---|---|---|---|---|---|---|
| **1** | K-Guide Global (다국어 통합) | 19 | 14 | 19 | 11 | 20 | **+4** | **87** |
| **2** | KoreaPath AI (AI 코스 생성) | 19 | 18 | 17 | 12 | 18 | — | **84** |
| **2** | AccessKorea (무장애 플랫폼) | 15 | 20 | 15 | 15 | 19 | — | **84** |
| 4 | K-Local Explorer (숨은 명소) | 14 | 18 | 15 | 15 | 17 | — | **79** |
| 4 | Audio Story Korea (오디오 가이드) | 13 | 18 | 17 | 15 | 16 | — | **79** |
| 6 | KoreaTrend Radar (빅데이터 레이더) | 14 | 17 | 17 | 13 | 16 | — | **77** |
| 7 | PetKorea (반려동물 여행) | 15 | 17 | 14 | 15 | 15 | — | **76** |
| 7 | EcoTrail Korea (에코 트레킹) | 12 | 17 | 16 | 15 | 16 | — | **76** |
| 9 | K-Camp Finder (캠핑 플랫폼) | 15 | 16 | 15 | 15 | 14 | — | **75** |
| 10 | KoreaWellness (웰니스 큐레이션) | 14 | 16 | 15 | 15 | 14 | — | **74** |

---

## BA 추천 상위 3개

### ★ 1위: K-Guide Global — 다국어 통합 가이드 (87점)

**추천 이유**
- 8개 API 활용으로 API 가중치 보너스 +4점 획득 → Round 2 유일 보너스 수혜 아이디어
- 방한 외래객 1,620만명 대형 시장. 공모전 데이터 활용 배점(20점) 만점 최유력
- 관광공사 공식 데이터 재패키징 → 구현 현실성 높음 (공모전 MVP 구현 용이)

**리스크 및 대응**
- 8개 언어 UI 복잡 → MVP는 영·일·중간체 3개 언어로 시작, 나머지 단계적 추가
- Visit Korea 앱 대비 차별화 → AI 개인화 + 실시간 혼잡도로 완전 차별화

---

### ★ 2위: KoreaPath AI — AI 코스 자동 생성 (84점)

**추천 이유**
- 국내 AI 코스 자동 생성 서비스 전무 → 경쟁 없는 블루오션
- 시장 규모 + 경쟁 강도 모두 18-19점으로 고른 강점
- 공모전 혁신성·실용성·데이터 활용 배점 동시 충족

**리스크 및 대응**
- 추천 엔진 구현 난이도 → MVP는 rule-based 로직으로 시작 후 AI 고도화
- 1위 K-Guide Global과 통합 시 상호 보완 (외국인 + AI 코스 = 최강 조합)

---

### ★ 3위: AccessKorea — 무장애 여행 플랫폼 (84점, 공동 2위)

**추천 이유**
- 경쟁 강도 만점(20점) — 무장애 통합 앱 국내 완전 전무
- 사회적 가치 심사항목 직결 (공모전 사회적 가치 10점 + RTO 특별상 가능)
- 문체부 무장애 관광 정책 직접 부합 → 정부 연계 신뢰도 확보

**리스크 및 대응**
- 타겟 시장 여행 빈도 제한 → 시니어 970만 + 가족 동반 확장으로 시장 확대
- 접근성 데이터 현장 괴리 → 크라우드소싱 리뷰 시스템으로 실시간 보완

*공동 2위 KoreaPath AI(84점)와 타이 시, 경쟁 강도(20 vs 18) 및 사회적 가치(19 vs 18)에서 AccessKorea 우세.*

---

## Round 2 핵심 인사이트

### API 가중치 상향의 영향
- 이번 Round 2에서 **6개 이상 API를 활용하는 아이디어가 K-Guide Global 1개뿐** — 보너스 점수 독점
- 나머지 9개 아이디어 모두 4-5개 API 수준. CEO Round 2 설계에서 "API 활용도 최우선" 기조가 K-Guide Global에 집중됨
- **Round 3 기획 제언**: 6개 이상 API 활용이 가능한 아이디어 확장 (예: KoreaPath AI에 다국어 API 3종 추가 시 8개 → +4점)

### K-Guide Global × KoreaPath AI 통합 시나리오

| 구성 | 기여 | 점수 영향 |
|---|---|---|
| K-Guide Global 기반 | 8개 언어, 오디오 가이드, 사진 | 데이터 활용 20점 만점 + 보너스 |
| KoreaPath AI 결합 | AI 코스 자동 생성, 혼잡도 최적화 | 기획력·혁신성 배점 강화 |
| AccessKorea 모듈 추가 | 무장애 필터 옵션화 | 사회적 가치 가점 |

→ 통합 시 API 활용 10개+ 달성 가능 → 보너스 +5점. 심사 전 항목 커버.

---

## Round 1 vs Round 2 비교

| 구분 | Round 1 최고점 | Round 2 최고점 | 변화 |
|---|---|---|---|
| 1위 | KoreaPath AI 85점 | K-Guide Global **87점** | K-Guide Global 역전 (API 보너스 효과) |
| 2위 | K-Guide Global 84점 | KoreaPath AI / AccessKorea **84점** | KoreaPath AI 유지 |
| 3위 | FreeTrip / LocalSecret 82점 | K-Local Explorer / Audio Story **79점** | 점수 소폭 하락 |
| API 보너스 수혜 | 없음 | K-Guide Global (+4점) | Round 2 첫 보너스 적용 |

---

*작성: BusinessAnalyst (claude-sonnet-4-6) | 2026-04-17T14:30:00Z*
*참조: TOU-14 CEO 오케스트레이션, TOU-18 BA 사업성 점수화 (API 가중치 상향)*
*검토 필요: CEO + ProductManager 최종 확인 후 선정 서비스 결정*
