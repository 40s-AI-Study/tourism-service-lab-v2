---
type: api-scenarios
id: api-scenarios-20
title: "Visit Korea OpenAPI 조합 시나리오 20개"
author_agent: ceo
author_model: claude-sonnet-4-6
created: 2026-04-17T07:30:00Z
status: final
llm_compatibility: universal
total_scenarios: 20
sources:
  - https://api.visitkorea.or.kr/#/useUtilExercises
  - knowledge-base/tourism-api/00-api-catalog.md
aliases: ["Visit Korea OpenAPI 조합 시나리오 20개"]
---

# Visit Korea OpenAPI 조합 시나리오 20개

> 공모전 심사 기준: 데이터 활용 적절성 20점 — API 조합의 창의성과 실제 사용자 가치를 기준으로 작성.

---

## 시나리오 분류

| 분류 | 시나리오 수 | 시나리오 번호 |
|---|---|---|
| AI 개인화 & 코스 추천 | 5 | 1-5 |
| 외국인 특화 서비스 | 4 | 6-9 |
| 테마 여행 특화 | 5 | 10-14 |
| 빅데이터 & 예측 | 3 | 15-17 |
| 콘텐츠 & 미디어 결합 | 3 | 18-20 |

---

## 카테고리 1: AI 개인화 & 코스 추천

### 시나리오 1: AI 맞춤 당일치기 코스 자동 생성

**API 조합**
- `related-attractions` (연관 관광지)
- `central-attractions-by-municipality` (지자체 중심 관광지)
- `visitor-concentration-forecast` (혼잡도 예측)
- `tourism-info-korean` (상세 정보)

**타겟 페르소나**
- 20-30대 주말 당일치기 여행자
- 계획 세우기 귀찮아하는 즉흥 여행자

**시나리오 흐름**
```
1. 사용자: "서울에서 당일치기, 내일 오전 출발"
2. 시스템: central-attractions-by-municipality → 해당 날 접근 가능한 지역 추출
3. 시스템: visitor-concentration-forecast → 내일 혼잡도 낮은 관광지 필터
4. 시스템: related-attractions → A 관광지 방문 시 연관 B, C 자동 연결
5. 출력: "경복궁(오전 9시, 혼잡도 낮음) → 통인시장 점심 → 북촌한옥마을(오후, 혼잡도 중간) → 창덕궁(오후 3시, 야간 개장)"
```

**기대효과**
- 여행 계획 시간 90% 단축
- 혼잡 회피로 사용자 만족도 향상
- 이탈률 감소 (계획 단계에서 포기하는 사용자 방지)

**공모전 차별화**: 기존 서비스 어디도 이 조합 없음 — "AI 코스 생성 + 혼잡도 회피" 최초

---

### 시나리오 2: 2박 3일 테마 여행 자동 일정표

**API 조합**
- `tourism-info-korean` (기본 관광정보)
- `related-attractions` (연관 관광지)
- `visitor-concentration-forecast` (혼잡도)
- `area-tourism-demand-density` (지역 수요 강도)
- `gocamping` or `wellness-tourism` (테마 선택)

**타겟 페르소나**
- 30대 커플, 2박 3일 여행 계획 중
- 웰니스 테마 or 캠핑 테마 선택

**시나리오 흐름**
```
1. 사용자: "강원도 2박 3일, 커플, 웰니스 테마"
2. 시스템: wellness-tourism → 강원 웰니스 관광지 목록
3. 시스템: area-tourism-demand-density → 강원 지역별 관광 수요 강도 (붐비는 곳 제외)
4. 시스템: related-attractions → 웰니스 장소 A 근처 맛집, 숙박 연관 정보
5. 시스템: visitor-concentration-forecast → 3일간 시간대별 혼잡도 최적화
6. 출력: 3일치 시간대별 일정 + 지도 + 예약 링크
```

**기대효과**
- 파편화된 정보 통합 → 계획 시간 80% 감소
- 테마 일관성 있는 여행 경험

---

### 시나리오 3: 실시간 여행 도우미 (현장 추천)

**API 조합**
- `tourism-info-korean` (현재 위치 기반 주변 관광지)
- `related-attractions` (현재 장소의 연관 장소)
- `visitor-concentration-forecast` (다음 목적지 혼잡도)

**타겟 페르소나**
- 현장에서 즉흥적으로 다음 목적지 결정하는 여행자
- 20-30대 솔로/커플

**시나리오 흐름**
```
1. 사용자: (경복궁에서) "다음 어디 갈까?"
2. 시스템: related-attractions → 경복궁 방문자가 함께 가는 TOP 10
3. 시스템: visitor-concentration-forecast → 각 장소 지금 혼잡도 체크
4. 출력: "지금 북촌한옥마을 한산(혼잡도 25%), 인사동 약간 붐빔(55%) → 북촌 추천"
```

**기대효과**
- 현장 의사결정 지원
- 혼잡한 장소 회피 → 여행 만족도 향상

---

### 시나리오 4: 지역 빅데이터 기반 '숨은 명소' 발견

**API 조합**
- `tourism-big-data` (관광빅데이터 — 이동통신/카드/내비 데이터)
- `area-tourism-diversity` (관광 다양성 지수)
- `tourism-info-korean` (상세 정보)

**타겟 페르소나**
- 재방문 여행자 (서울은 다 가봤음)
- '남들이 모르는 곳' 선호하는 20-30대

**시나리오 흐름**
```
1. 사용자: "서울 자주 가봤는데, 덜 알려진 곳 추천해줘"
2. 시스템: tourism-big-data → 실제 방문 데이터 기반 트렌드 상승 중인 지역 감지
3. 시스템: area-tourism-diversity → 다양성 지수 높은 (=관광 일변도 아닌) 지역 필터
4. 출력: "성수동 세부 골목, 망원동 로컬 카페 거리, 을지로 힙한 골목" — 빅데이터 기반
```

**기대효과**
- 오버투어리즘 분산 효과 (관광공사 정책 목표와 일치)
- 차별화된 여행 경험 제공

---

### 시나리오 5: 계절/날씨 연동 여행지 추천

**API 조합**
- `area-tourism-resource-demand` (지역별 관광 자원 수요)
- `tourism-big-data` (계절별 트렌드 데이터)
- `visitor-concentration-forecast` (향후 30일 예측)
- `tourism-info-korean` (관광지 상세)

**타겟 페르소나**
- "이번 주말 어디 갈까" — 계절·날씨 고려하는 30-40대

**시나리오 흐름**
```
1. 사용자: "다음 주 토요일, 봄꽃 명소 추천"
2. 시스템: tourism-big-data → 현재 시즌 급상승 관광지 (벚꽃 = 여의도, 진해)
3. 시스템: visitor-concentration-forecast → 당일 혼잡도 예측 (진해 오전 vs 오후)
4. 시스템: area-tourism-resource-demand → 해당 지역 관광 자원 수요 체크
5. 출력: "진해 군항제 오전 8-10시 방문 추천 (혼잡도 낮음), 코스: 경화역 → 여좌천 → 진해루"
```

---

## 카테고리 2: 외국인 특화 서비스

### 시나리오 6: 외국인 다국어 통합 가이드

**API 조합**
- `tourism-info-english` / `tourism-info-japanese` / `tourism-info-chinese-simplified` / `tourism-info-chinese-traditional` (4개 다국어)
- `audio-guide` (다국어 오디오)
- `related-attractions` (연관 장소)

**타겟 페르소나**
- 방한 외국인 — 일본/중국/영어권
- 언어 장벽으로 현지 탐색 어려운 관광객

**시나리오 흐름**
```
1. 사용자(일본어 선택): "경복궁 가이드 해줘"
2. 시스템: tourism-info-japanese → 경복궁 일본어 공식 정보 로드
3. 시스템: audio-guide → 경복궁 일본어 오디오 가이드 스트리밍
4. 시스템: related-attractions → 일본어로 "함께 가면 좋은 곳" 추천
5. 출력: 일본어 전면 전환 + 오디오 재생 + 연관 장소 일본어 안내
```

**기대효과**
- 방한 외국인 2024년 1,600만명 시장 직접 공략
- 공식 데이터 신뢰성 + 현대적 UX = Visit Korea의 약점 보완

---

### 시나리오 7: 외국인 한국 입국 후 즉시 사용 앱

**API 조합**
- `tourism-info-english` (공항·서울 정보)
- `central-attractions-by-municipality` (서울 중심 관광지 TOP 100)
- `visitor-concentration-forecast` (현재 혼잡도)
- `area-tourism-demand-density` (지역별 관광 활성도)

**타겟 페르소나**
- 인천/김포 공항 도착 직후 외국인 관광객
- 사전 계획 없이 즉흥 방한

**시나리오 흐름**
```
1. (공항 위치 감지) 사용자: 앱 첫 실행
2. 시스템: "안녕하세요! 어느 나라에서 오셨나요?" → 언어 선택
3. 시스템: central-attractions-by-municipality → 서울 핵심 관광지 TOP 10 표시
4. 시스템: visitor-concentration-forecast → 지금 당장 가기 좋은 곳 (혼잡도 낮음)
5. 출력: "지금 경복궁 한산해요! 공항에서 지하철 1시간" 즉시 추천
```

---

### 시나리오 8: K-팝/K-드라마 성지순례 가이드

**API 조합**
- `tourism-info-english` / `tourism-info-japanese` (외국인 다국어)
- `tourism-info-korean` (성지순례 장소 상세 정보)
- `audio-guide` (현장 해설)
- `photo-contest-winners` (촬영지 사진)

**타겟 페르소나**
- K-팝 팬 외국인 20대 — 일본, 동남아, 서구권
- K-드라마 촬영지 방문 희망

**시나리오 흐름**
```
1. 사용자: "BTS 관련 장소 보여줘" (일본어)
2. 시스템: 큐레이션 데이터 + tourism-info-japanese → 관련 장소 목록
3. 시스템: photo-contest-winners → 해당 장소 공식 사진
4. 시스템: visitor-concentration-forecast → 현재 혼잡도
5. 출력: 장소별 팬 코스 + 사진 스팟 + 오디오 해설 (일본어)
```

---

### 시나리오 9: 외국인 맞춤 식도락 여행

**API 조합**
- `tourism-info-english` (위치기반 식당 정보)
- `related-attractions` (관광지 근처 식당 연관)
- `central-attractions-by-municipality` (지역별 음식 명소)

**타겟 페르소나**
- 미식 목적 방한 외국인 — 서구권, 일본
- 할랄/비건/알레르기 필터 필요한 여행자

**시나리오 흐름**
```
1. 사용자(영어): "Korean BBQ near Myeongdong"
2. 시스템: tourism-info-english 위치기반 검색 → 명동 주변 한식 목록
3. 시스템: related-attractions → 명동 방문자가 같이 가는 음식점 TOP
4. 출력: 영어 메뉴 있는 곳 필터 + 거리순 정렬 + 오픈 시간 + 가격대
```

---

## 카테고리 3: 테마 여행 특화

### 시나리오 10: 반려동물 동반 완전 여행 플래너

**API 조합**
- `pet-friendly-travel` (핵심 — 7개 카테고리 전부)
- `related-attractions` (반려동물 OK 장소 연관)
- `visitor-concentration-forecast` (혼잡도)
- `gocamping` (펫 캠핑장)

**타겟 페르소나**
- 반려견/반려묘 보유 30-40대
- 펫 동반 여행 정보를 블로그로 찾는 사람

**시나리오 흐름**
```
1. 사용자: "강아지와 함께, 제주도 1박 2일"
2. 시스템: pet-friendly-travel → 제주 반려동물 동반 관광지/숙박/음식점 목록
3. 시스템: gocamping → 제주 펫 허용 캠핑장 + 글램핑
4. 시스템: visitor-concentration-forecast → 동선 최적화 (반려동물 스트레스 최소화)
5. 출력: 펫 동반 완성 코스 "함덕해수욕장(펫 허용 구간 있음) → 펫카페 → 반려동물 동반 숙소"
```

**기대효과**
- 반려동물 가구 600만 시장 직접 공략
- 기존 블로그 탐색 대비 시간 절감 90%

---

### 시나리오 11: 웰니스 & 힐링 여행 큐레이터

**API 조합**
- `wellness-tourism` (웰니스 핵심)
- `eco-tourism` (자연 기반 힐링)
- `visitor-concentration-forecast` (조용한 시간대)
- `area-tourism-diversity` (관광 다양성)

**타겟 페르소나**
- 번아웃 직장인 30대, 회복 여행 원함
- 의료관광이 아닌 일상 웰니스 추구

**시나리오 흐름**
```
1. 사용자: "스트레스 해소, 자연 속 힐링 2박"
2. 시스템: wellness-tourism → 온천/스파/산림욕 장소
3. 시스템: eco-tourism → 친환경 자연 관광지 (조용한 곳)
4. 시스템: visitor-concentration-forecast → 비수기 시간대 추천
5. 출력: "속초 설악산 산림욕 → 노천온천 → 조용한 독채 펜션" 웰니스 코스
```

---

### 시나리오 12: 무장애 & 접근성 여행 서비스

**API 조합**
- `barrier-free-travel` (핵심 — 장애인/어르신/영유아)
- `tourism-info-korean` (접근성 상세 정보)
- `related-attractions` (접근 가능한 연관 장소)
- `audio-guide` (시각장애인 오디오 가이드)

**타겟 페르소나**
- 휠체어 이용 장애인
- 유모차 동반 영유아 부모
- 거동 불편한 부모 모시는 40대

**시나리오 흐름**
```
1. 사용자: "휠체어로 갈 수 있는 서울 관광지"
2. 시스템: barrier-free-travel → 서울 무장애 인증 관광지 목록
3. 시스템: tourism-info-korean → 경사로/엘리베이터/장애인 화장실 상세
4. 시스템: audio-guide → 시각장애인용 오디오 해설
5. 출력: 휠체어 이동 가능 코스 + 대중교통 접근성 + 편의시설 안내
```

**공모전 사회적 가치**: 접근성 서비스 → 심사위원 긍정 평가 기대

---

### 시나리오 13: 에코·그린 여행 플래너

**API 조합**
- `eco-tourism` (생태/공정관광)
- `durunubi-trails` (걷기·자전거 코스)
- `central-attractions-by-municipality` (지역 자연 명소)
- `area-tourism-diversity` (관광 다양성)

**타겟 페르소나**
- MZ 세대 환경 의식 있는 여행자
- 자전거·트레킹 좋아하는 30-40대

**시나리오 흐름**
```
1. 사용자: "탄소발자국 최소 여행, 제주 3일"
2. 시스템: eco-tourism → 제주 생태관광 인증 장소
3. 시스템: durunubi-trails → 제주 올레길 구간별 정보
4. 시스템: central-attractions-by-municipality → 제주시/서귀포시 자연 명소 TOP
5. 출력: 대중교통·자전거 이동 에코 코스 + 인증 생태 숙소 + 로컬 식당
```

---

### 시나리오 14: 글램핑 & 아웃도어 여행 플래너

**API 조합**
- `gocamping` (캠핑장 핵심 데이터)
- `eco-tourism` (자연 인접 생태지)
- `visitor-concentration-forecast` (주말 혼잡도)
- `area-tourism-resource-demand` (캠핑 수요 높은 지역)

**타겟 페르소나**
- 캠핑/글램핑 입문 30대 커플·가족
- 자연 속 럭셔리 경험 원하는 여행자

**시나리오 흐름**
```
1. 사용자: "이번 주말 글램핑, 수도권 1박"
2. 시스템: gocamping → 수도권 글램핑 시설 목록 + 시설 정보
3. 시스템: visitor-concentration-forecast → 이번 주말 캠핑장 혼잡도 예측
4. 시스템: area-tourism-resource-demand → 캠핑 수요 낮은 (경쟁 적은) 지역 추천
5. 출력: "가평 글램핑 추천 TOP 3 + 혼잡도 낮은 순위" 즉시 예약 연동
```

---

## 카테고리 4: 빅데이터 & 예측

### 시나리오 15: 관광 트렌드 대시보드 (지역별)

**API 조합**
- `area-tourism-demand-density` (수요 강도)
- `area-tourism-resource-demand` (자원 수요)
- `area-tourism-diversity` (다양성)
- `tourism-big-data` (이동통신·카드 빅데이터)

**타겟 페르소나**
- 지자체 관광 담당자 (B2G)
- 여행 콘텐츠 크리에이터 (트렌드 파악용)
- 여행 계획 꼼꼼히 세우는 30-40대

**시나리오 흐름**
```
1. 사용자: "요즘 어느 지역이 뜨고 있어?"
2. 시스템: area-tourism-demand-density → 지역별 관광 수요 강도 순위
3. 시스템: tourism-big-data → 이동통신 데이터 기반 최근 이동 증가 지역
4. 출력: 지역별 트렌드 차트 + "최근 3개월 급상승 지역: 강릉, 전주, 통영"
```

---

### 시나리오 16: 혼잡도 기반 스마트 방문 시간 알림

**API 조합**
- `visitor-concentration-forecast` (향후 30일 예측)
- `tourism-info-korean` (관광지 기본정보)
- `central-attractions-by-municipality` (인기 관광지 목록)

**타겟 페르소나**
- 혼잡한 곳 싫어하는 모든 연령대
- 특정 관광지 방문 계획 중인 사용자

**시나리오 흐름**
```
1. 사용자: "경주 불국사 이번 달 언제 한산해?"
2. 시스템: visitor-concentration-forecast → 불국사 향후 30일 집중률 캘린더
3. 출력: 캘린더 뷰 "이번 달 17일(화) 오전 9시 집중률 22% — 최적"
        → "알림 설정" 기능 제공
```

**기대효과**
- 오버투어리즘 해소 기여
- 방문자 경험 질 향상

---

### 시나리오 17: 지역 관광 다양성 기반 여행 추천

**API 조합**
- `area-tourism-diversity` (관광객 다양성 + 소비 다양성 + 국제 다양성)
- `tourism-big-data` (트렌드)
- `tourism-info-korean` (관광지 정보)

**타겟 페르소나**
- 외국인 비율 높은 글로벌한 여행지 원하는 사용자
- 또는 반대로 로컬한 장소 원하는 사용자

**시나리오 흐름**
```
1. 사용자: "외국인도 많고 국제적인 분위기 여행지"
2. 시스템: area-tourism-diversity → 국제 다양성 지수 높은 지역 추출
3. 출력: "홍대, 이태원, 강남 → 국제 다양성 최상위 / 반대로 진주, 안동 → 가장 로컬한 분위기"
```

---

## 카테고리 5: 콘텐츠 & 미디어 결합

### 시나리오 18: 사진 기반 여행지 발견 & 공유

**API 조합**
- `tourism-photos` (관광지 공식 사진)
- `photo-contest-winners` (공모전 수상 사진 — 촬영지 + 계절)
- `tourism-info-korean` (사진 속 장소 상세 정보)

**타겟 페르소나**
- 인스타그램/SNS 활발한 20-30대
- 포토스팟 탐색이 여행 목적인 사용자

**시나리오 흐름**
```
1. 앱 피드: 공모전 수상 사진 (촬영지: 제주 성산일출봉, 10월 새벽)
2. 사용자: 사진 탭 → "이 장소 가고 싶어"
3. 시스템: photo-contest-winners → 촬영일/촬영지/키워드 자동 연결
4. 시스템: tourism-info-korean → 성산일출봉 상세 정보
5. 시스템: visitor-concentration-forecast → "10월 일출 시간대 집중률 70% — 주의"
6. 출력: 사진 → 장소 → 코스 → 예약 원스톱
```

---

### 시나리오 19: 오디오 가이드 통합 미술관·문화재 투어

**API 조합**
- `audio-guide` (한/영/중/일 오디오 + 대본 + 사진)
- `tourism-info-korean` / `tourism-info-english` (문화재 정보)
- `barrier-free-travel` (접근성 정보 병행)

**타겟 페르소나**
- 역사·문화 관심 40대 국내 여행자
- 가이드 없이 심층 투어 원하는 외국인

**시나리오 흐름**
```
1. 사용자: (창덕궁 앞) "여기 설명 들려줘" (영어 선택)
2. 시스템: audio-guide → 창덕궁 영어 오디오 스트리밍 시작
3. 시스템: tourism-info-english → 텍스트 자막 병행 표시
4. 다음 이동 → 오디오 자동 전환
5. 출력: 이어폰으로 전문 가이드 수준 해설 + 사진 자료
```

---

### 시나리오 20: 글로벌 통합 관광 앱 — 9개 언어 완전 지원

**API 조합**
- `tourism-info-korean` + `tourism-info-english` + `tourism-info-japanese` + `tourism-info-chinese-simplified` + `tourism-info-chinese-traditional` + `tourism-info-german` + `tourism-info-french` + `tourism-info-spanish` + `tourism-info-russian` (9개 전부)
- `audio-guide` (다국어 오디오)
- `tourism-big-data` (트렌드)
- `visitor-concentration-forecast` (혼잡도)

**타겟 페르소나**
- 모든 언어권 외국인 관광객
- 공모전 심사위원 (데이터 활용 극대화 시연용)

**시나리오 흐름**
```
1. 앱 첫 실행: 언어 선택 (9개 언어)
2. 언어 선택 즉시: 해당 언어 API로 전체 콘텐츠 전환
3. 관광지 검색 → 해당 언어 공식 정보 표시
4. 오디오 가이드 → 선택 언어로 자동 재생
5. 트렌드 → 빅데이터 기반 지금 인기 관광지
6. 혼잡도 → 실시간 방문 최적 시간 안내
```

**공모전 관점**: 27개 API 중 최대 활용 (다국어 9개 + 오디오 + 빅데이터 + 예측 = 12개 API 활용)
→ 데이터 활용 적절성 20점 만점 목표

---

## 전체 시나리오 API 활용 매핑

| API | 사용 시나리오 | 활용 횟수 |
|---|---|---|
| `tourism-info-korean` | 1,3,4,5,9,12,18,19 | 8 |
| `related-attractions` | 1,2,3,6,10 | 5 |
| `visitor-concentration-forecast` | 1,2,3,5,10,11,14,16,18 | 9 |
| `tourism-info-english` | 6,7,9,19,20 | 5 |
| `tourism-info-japanese` | 6,8,20 | 3 |
| `tourism-info-chinese-simplified` | 6,20 | 2 |
| `tourism-info-chinese-traditional` | 6,20 | 2 |
| `tourism-info-german/french/spanish/russian` | 20 | 각 1 |
| `central-attractions-by-municipality` | 1,7,13,16 | 4 |
| `pet-friendly-travel` | 10 | 1 |
| `wellness-tourism` | 11 | 1 |
| `eco-tourism` | 11,13,14 | 3 |
| `barrier-free-travel` | 12,19 | 2 |
| `durunubi-trails` | 13 | 1 |
| `gocamping` | 10,14 | 2 |
| `audio-guide` | 6,8,12,19,20 | 5 |
| `tourism-big-data` | 4,5,15,17,20 | 5 |
| `area-tourism-demand-density` | 2,15 | 2 |
| `area-tourism-diversity` | 4,15,17 | 3 |
| `area-tourism-resource-demand` | 5,14,15 | 3 |
| `tourism-photos` | 18 | 1 |
| `photo-contest-winners` | 8,18 | 2 |

**총 활용 API 수: 27개 중 22개** (81%)
