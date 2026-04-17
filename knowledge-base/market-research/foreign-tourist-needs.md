---
type: research
id: foreign-tourist-needs
title: "외국인 관광객 니즈 분석"
author_agent: ceo
author_model: claude-sonnet-4-6
created: 2026-04-17T07:30:00Z
status: draft
llm_compatibility: universal
sources:
  - https://kto.visitkorea.or.kr/kor/notice/data/statis/tstat/inout/forstats.kto
  - https://www.reddit.com/r/korea/
  - https://www.reddit.com/r/koreatravel/
  - https://www.tripadvisor.com/Tourism-g294197-South_Korea-Vacations.html
  - https://www.klook.com/en-US/destination/kr-south-korea/
  - https://datalab.visitkorea.or.kr/
---

# 외국인 관광객 니즈 분析

## 1. 방한 외국인 세그먼트 개요

### 주요 국가별 특성 (2024 기준)

| 국가/지역 | 비중 | 평균 체류일 | 주요 목적 | 정보 탐색 채널 |
|---|---|---|---|---|
| **중국** | ~24% | 4.2일 | 쇼핑, K-뷰티, 한식 | 小红书(샤오홍수), 抖音(더우인), 바이두 |
| **일본** | ~22% | 3.8일 | 한식, K-팝, 쇼핑, 코스메틱 | 네이버재팬, X(트위터), 인스타그램 |
| **대만** | ~6% | 4.5일 | 한류, 음식, 야경 | Instagram, PTT, Dcard |
| **미국/캐나다** | ~7% | 7.1일 | K-컬처, 역사, 자연 | Google, Reddit, TripAdvisor |
| **동남아** (태국/베트남/말레이) | ~10% | 5.2일 | K-팝, 한류, 쇼핑 | Facebook, TikTok, Instagram |
| **유럽** | ~5% | 8.3일 | 역사문화, 자연, K-컬처 | Google, TripAdvisor, 여행 블로그 |

---

## 2. 국가별 상세 니즈 분析

### 2.1 중국인 관광객

**방문 동기**
- K-뷰티 (한국 화장품 구매) — 1순위
- 한식 (삼겹살, 치킨, 분식)
- 성형/피부 의료관광
- 한류 성지 순례 (드라마/K-팝)

**주요 Pain Point**
- 카카오페이/네이버페이 사용 어려움 (중국계 결제 선호: 알리페이, WeChat Pay)
- 간체자 정보 부족 (번체 위주)
- 중국 앱 차단 (구글·유튜브 사용 가능하나 국내 앱 접근 어려움)
- 언어 장벽 — 한국어/영어 소통 어려움

**선호 여행 스타일**
- 단체 → 개인 여행으로 전환 중 (2023 단체관광 재개 이후 FIT 증가)
- 쇼핑 + 먹방 + 뷰티 콤보 코스 선호
- 서울 집중 (명동, 강남, 홍대)

**Visit Korea API 관련성**: `tourism-info-chinese-simplified` + `tourism-info-chinese-traditional` (중국 본토 vs 대만/홍콩)

---

### 2.2 일본인 관광객

**방문 동기**
- 한식 체험 — 최고 인기 (야키니쿠, 삼겹살, 떡볶이)
- K-팝/K-드라마 성지 순례
- 뷰티 쇼핑 (올리브영 등)
- 지리적 근접성 + 저가 항공

**주요 Pain Point**
- 일본어 가이드 부족 (서울 외 지방)
- 결제: JCB 카드 사용 제한 장소 多
- 음식 알레르기 정보 부족 (게 알레르기 등)
- 교통 정보 복잡 (환승, 버스 번호 이해 어려움)

**선호 여행 스타일**
- 소그룹 (2-4명) FIT 여행 선호
- SNS용 포토스팟 필수 방문
- 지방 여행 관심 증가 (부산, 전주, 경주)
- 재방문율 높음 — 심층 탐방 수요

**Visit Korea API 관련성**: `tourism-info-japanese` + `audio-guide` (일본어 오디오)

---

### 2.3 영어권 (미국/캐나다/호주/영국)

**방문 동기**
- K-컬처 전반 (K-팝, K-드라마, K-무비)
- 역사/문화 탐방 (한국전쟁, 조선 역사)
- 음식 모험 (새로운 미식 경험)
- 자연경관 (제주, 설악산, 한려수도)

**주요 Pain Point**
- 영어 표지판/메뉴 부족 (서울 외 지방)
- 교통 앱 이해 (카카오맵 한국어 위주)
- 현금 필요 상황 (전통시장, 소규모 식당)
- Google Maps 정보와 실제 정보 불일치 (폐업, 이전)
- 신용카드 수수료

**선호 여행 스타일**
- 장기 체류 (평균 7일+) — 심층 탐방
- Reddit/YouTube로 여행 계획 (r/koreatravel 커뮤니티 활성)
- 비서울 여행 비중 높음 (제주, 부산, 경주)
- 하이킹/자연 관심 높음

**Visit Korea API 관련성**: `tourism-info-english` + `visitor-concentration-forecast` + `eco-tourism` + `durunubi-trails`

---

### 2.4 동남아 관광객 (태국/베트남/말레이시아/인도네시아)

**방문 동기**
- K-팝 성지 (SM·YG·JYP·HYBE 투어)
- K-드라마 촬영지
- 한식 (치킨, 라면, 분식)
- 쇼핑

**주요 Pain Point**
- 할랄 음식 정보 부족 (말레이/인도네시아 무슬림)
- 더위/추위 대응 정보 없음 (계절 차이 큰 편)
- 한국 앱 다운로드 어려움 (구글 플레이 지역 제한)

**Visit Korea API 관련성**: `tourism-info-english` (영어 공용)

---

## 3. 공통 Pain Point 분析

### 3.1 정보 접근성

| Pain Point | 심각도 | 현재 해결책 | 우리 기회 |
|---|---|---|---|
| 다국어 안내 부족 | ★★★★★ | Visit Korea 웹 (UX 낮음) | 다국어 모바일 앱 |
| 실시간 혼잡도 모름 | ★★★★☆ | Google Popular Times | `visitor-concentration-forecast` 통합 |
| 오프라인 사용 불가 | ★★★★☆ | 없음 | 오프라인 모드 캐시 |
| 교통 연계 정보 | ★★★☆☆ | 네이버맵 (한국어) | 다국어 교통 연계 |
| 현지 식당 영어 메뉴 | ★★★☆☆ | 구글 번역 | 오디오가이드+사진 연계 |

### 3.2 결제 Pain Point

- **선호 결제**: 신용카드(Visa/Mastercard) > 알리페이(중국) > 애플페이 > 현금
- **문제**: 소규모 점포 카드 안 받음, ATM 찾기 어려움
- **우리 기회**: 현금 ATM 위치 + 카드 수락 여부 표시 기능

### 3.3 언어 장벽

- **주요 불편**: 식당 주문, 교통 문의, 쇼핑 흥정
- **현재 사용**: 구글 번역 (불편함), 파파고 (한국어 특화)
- **우리 기회**: `audio-guide` API 다국어 + 현장 번역 힌트

---

## 4. 외국인 관광 정보 탐색 여정

```
[여행 전]                    [현지]                   [여행 후]
YouTube/TikTok              Google Maps              TripAdvisor 리뷰
블로그 (자국어)         →    Visit Korea (정보만)  →  SNS 공유
Reddit/커뮤니티              Klook (예약)             유튜브 브이로그
Instagram #Seoul             카카오맵 (한국어라 힘듦)

취약점: 현지 실시간 정보 없음, 다국어 통합 앱 없음
```

---

## 5. 서비스 기획 시사점

### 필수 기능 (외국인 타겟)

1. **언어 선택 시 전면 다국어 전환** — 영/일/중(간/번) 최소
2. **현재 인기 관광지 + 혼잡도** — 실시간 정보 제공
3. **오디오 가이드** — 현장에서 귀로 듣는 해설 (`audio-guide` API)
4. **포토스팟 + SNS 공유** — MZ 외국인 필수 기능
5. **주변 맛집·숙박 연결** — `related-attractions` 활용

### 차별화 포인트

- **"Visit Korea + TripAdvisor + Google Maps를 하나로"** — 포지셔닝 메시지
- 중국어 두 버전 (간체/번체) 분리 제공 — 세심함 어필
- 할랄 필터, 비건 필터 — 다양성 대응
