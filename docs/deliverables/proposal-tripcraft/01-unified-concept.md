# TripCraft Korea — 통합 컨셉 문서

> **카테고리 테마 기반 개인화 여행 플래너**  
> 오디오 가이드 × 혼잡도 최적화 × 경비 자동 산출 × 지역 균형 분산

---

## 1. 서비스 한 줄 정의

> **여행 카테고리와 지역을 고르면, TripCraft Korea가 혼잡도·유사도·경비를 실시간으로 계산해 최적 동선과 카테고리별 부가기능(오디오 가이드·예약·팔도 스탬프)이 붙은 원페이지 플랜을 자동 생성한다.**

---

## 2. 엘리베이터 피치 (60단어)

TripCraft Korea는 "문화유산", "미식", "K-컬처" 등 여행 카테고리를 선택하는 순간, 바이럴 장소 대신 유사 분위기의 여유로운 대안을 추천하고, 문화유산 근방 50m 진입 시 오디오 가이드를 자동 재생하며, 경비·혼잡도·이동 동선을 한 화면에 묶어 실행 가능한 플랜으로 제시합니다. 여행 계획의 파편화를 끝내고, 17개 시도 균형 분산을 동시에 달성합니다.

---

## 3. 핵심 가치 제안 (3가지)

| # | 가치 | 설명 |
|---|------|------|
| 1 | **카테고리 감성 보존 + 혼잡 없는 여행** | 인스타 바이럴 장소 대신 CLIP 유사도 91%+ 대안을 카테고리 맥락 안에서 제안. 분위기 포기 없이 줄 없는 여행 |
| 2 | **도착하면 바로 실행되는 플랜** | 오디오 자동 재생·예약 URL·경비 합산·카카오맵 경로가 원페이지에 통합. ChatGPT가 텍스트를 주는 자리에 TripCraft Korea는 실행을 준다 |
| 3 | **걸으면서 이야기가 따라오는 탐험 경험** | 문화유산 반경 50m 진입 시 오디오 가이드 자동 재생. 계절·언어·성향별 스토리 분기로 같은 장소도 다른 이야기 |

---

## 4. 소스 아이디어 기능 매핑 테이블

| 기능 | KoreaPath AI | Audio Story Korea v2 | 아이디어 A+ | 아이디어 B+ |
|------|:------------:|:--------------------:|:-----------:|:-----------:|
| 카테고리 테마 기반 여행 플랜 생성 | ✓ (테마 입력) | — | — | ✓ (catcode 큐레이션) |
| 혼잡도 예측 + 방문 타이밍 추천 | ✓ (핵심) | — | ✓ (여유로움 지수) | ✓ (집중률 등급) |
| 연관 관광지 API 기반 동선 | ✓ (related-attractions) | ✓ (다음 이야기 장소) | — | ✓ (자연 동선) |
| CLIP 유사도 기반 대안 장소 추천 | — | — | ✓ (핵심) | — |
| 17시도 소외 지역 균형 분산 | — | ✓ (area-tourism-diversity) | ✓ (핀 지도) | ✓ (가중 보정 1.5배) |
| 위치 감지 오디오 가이드 자동 재생 | — | ✓ (핵심) | — | — |
| 계절·성향별 스토리 분기 | — | ✓ (4계절×5성향) | — | — |
| 국내외 이중 렌즈 스토리 | — | ✓ (한국인/외국인 앵글) | — | — |
| 경비 자동 합산 (입장료·숙박·이동) | — | — | — | ✓ (핵심) |
| 팔도 스탬프 + 리워드 시스템 | — | — | — | ✓ (확장 레이어) |
| 카카오맵 경로 즉시 실행 | ✓ | — | ✓ | ✓ |
| 카카오톡 플랜 공유 | — | — | ✓ | ✓ |
| 관광 사진 콘텐츠 (공모전 수상작) | — | ✓ (photo-contest-winners) | — | ✓ |
| 소셜 트렌드 분석 (네이버 블로그) | — | — | — | ✓ |
| 바이럴 감지 (방문자 급증 탐지) | — | — | ✓ (핵심) | — |

---

## 5. 여행 카테고리 정의 (7개)

### 5-1. 카테고리 목록 및 활성화 기능

| 카테고리 | 한 줄 설명 | 활성화 API / 기능 |
|----------|-----------|-------------------|
| **문화유산** | 궁궐·고택·비석 등 역사 유산 탐방. 걸으면서 오디오 이야기가 자동 재생된다 | `audio-guide` 자동 재생 (반경 50m 진입 트리거) / `photo-contest-winners` 계절 비주얼 / `tourism-info-english|japanese|chinese-simplified` 다국어 스토리 분기 / `related-attractions` 다음 이야기 장소 추천 |
| **미식** | 지역 향토 음식·대표 식당·로컬 시장 중심 코스. 숨은 맛집을 발굴한다 | `tourism-info-korean` contentTypeId=38 음식점 / 네이버 블로그 API 트렌드 파싱 / `detailCommon2` 예약 URL 즉시 연결 / 경비 계산 (식비 기본값 1인 1.5만원) |
| **자연/에코트레일** | 국립공원·트레킹로·해변·생태 탐방. 혼잡 없는 자연 속 루트를 최적화한다 | `visitor-concentration-forecast` 혼잡도 예측 / `area-tourism-demand-density` 수요 밀집도 / `central-attractions-by-municipality` 지자체 핵심 자연지 / 이동 경로 거리 최적화 |
| **축제/이벤트** | 계절 축제·지역 행사·야간 관광 특화 코스. 날짜 기반 동적 큐레이션 | `tourism-big-data` 방문자 트렌드 / `visitor-concentration-forecast` 행사 기간 혼잡 예측 / `detailCommon2` 행사 일정·입장료 / `photo-contest-winners` 축제 수상 사진 |
| **힐링/웰니스** | 온천·템플스테이·명상 공간·한적한 숲길. 번아웃 여행자를 위한 저밀도 동선 | `area-tourism-diversity` 소외 지역 발굴 / `visitor-concentration-forecast` 저혼잡 시간대 추천 / `related-attractions` 인접 힐링 장소 연결 / 여유로움 지수 표시 |
| **포토스팟** | 인스타 감성 뷰·일출·야경 포인트. CLIP 유사도로 바이럴 장소 대안을 제시 | CLIP 이미지 임베딩 유사도 (코사인) / `tatsCnctrRateList` 바이럴 감지 / `photo-contest-winners` 수상 각도 가이드 / `tourism-photos` 고품질 비주얼 / 카카오맵 핀 16개 시도 대안 표시 |
| **K-컬처** | K-드라마 촬영지·K-팝 성지·웹툰 배경 장소. 팬 여행자를 위한 테마 동선 | `searchKeyword2` K-컬처 키워드 검색 / `related-attractions` 성지 간 연결 동선 / `tourism-big-data` 콘텐츠 트렌드 분석 / 카카오톡 팬 공유 기능 |

### 5-2. 카테고리별 contentTypeId 매핑

| 카테고리 | 주요 contentTypeId |
|----------|-------------------|
| 문화유산 | 14 (문화시설), 76 (문화재) |
| 미식 | 38 (음식점), 39 (카페) |
| 자연/에코트레일 | 12 (관광지 중 자연), 28 없음 |
| 축제/이벤트 | 15 (축제·행사) |
| 힐링/웰니스 | 32 (숙박 중 템플스테이), 12 (관광지) |
| 포토스팟 | 12 (관광지), 14 (문화시설) |
| K-컬처 | 12, 14, 28 (쇼핑·굿즈 포함) |

---

## 6. 통합 서비스 플로우 다이어그램

```
╔══════════════════════════════════════════════════════════════════════╗
║  [STEP 1] 입력                                                       ║
║  카테고리 선택 (문화유산·미식·자연·축제·힐링·포토스팟·K-컬처)          ║
║  + 지역 선택 (17개 시도 또는 자동 위치)                               ║
║  + 여행 기간 (당일 / 1박 2일 / 2박 3일)                              ║
╚══════════════════╦═══════════════════════════════════════════════════╝
                   ↓
╔══════════════════╩═══════════════════════════════════════════════════╗
║  [STEP 2] 후보 추출                                                  ║
║  ┌─────────────────────────────────────────────────────────────┐    ║
║  │ A. 트렌드 / 바이럴 감지                                      │    ║
║  │    tourism-big-data > locgoRegnVisitrDDList                 │    ║
║  │    visitor-concentration-forecast > tatsCnctrRateList       │    ║
║  │    → 방문자 급증 장소 자동 탐지 (최근 4주 +50% 이상 기준)     │    ║
║  ├─────────────────────────────────────────────────────────────┤    ║
║  │ B. 장소 풀 수집                                              │    ║
║  │    tourism-info-korean > areaBasedList2 (catcode 필터)      │    ║
║  │    tourism-info-korean > searchKeyword2 (카테고리 키워드)    │    ║
║  │    related-attractions > searchKeyword1 (연관 관광지 50위)   │    ║
║  └─────────────────────────────────────────────────────────────┘    ║
╚══════════════════╦═══════════════════════════════════════════════════╝
                   ↓
╔══════════════════╩═══════════════════════════════════════════════════╗
║  [STEP 3] 혼잡도 / 유사도 보정                                       ║
║  ┌─────────────────────────────────────────────────────────────┐    ║
║  │ 혼잡도 보정                                                  │    ║
║  │    visitor-concentration-forecast > tatsCnctrRatedList      │    ║
║  │    → 집중률 등급 상위 10% 장소 가중치 감소                    │    ║
║  │    여유로움 지수 = 바이럴 장소 방문자 / 해당 장소 방문자       │    ║
║  ├─────────────────────────────────────────────────────────────┤    ║
║  │ 유사도 보정 (포토스팟·문화유산 카테고리 강화)                  │    ║
║  │    CLIP 이미지 임베딩 코사인 유사도 × 40%                    │    ║
║  │    + catcode 소분류 일치 × 40%                              │    ║
║  │    + overview 텍스트 임베딩 유사도 × 20%                     │    ║
║  │    → Chroma DB 벡터 검색, 시도별 상위 3개 후보 추출           │    ║
║  ├─────────────────────────────────────────────────────────────┤    ║
║  │ 소외 지역 가중                                               │    ║
║  │    area-tourism-diversity > areaTouDivList                  │    ║
║  │    → 다양성 지수 하위 33% 시도: 노출 가중치 1.5배            │    ║
║  └─────────────────────────────────────────────────────────────┘    ║
╚══════════════════╦═══════════════════════════════════════════════════╝
                   ↓
╔══════════════════╩═══════════════════════════════════════════════════╗
║  [STEP 4] 동선 최적화                                                ║
║  ┌─────────────────────────────────────────────────────────────┐    ║
║  │ 거리 최적화: 카카오 모빌리티 API 이동 시간 행렬 계산           │    ║
║  │ 혼잡 타이밍 배치: tatsCnctrRatedList 기반 방문 순서 재배열     │    ║
║  │   → 오전(저혼잡) = 인기 관광지 / 오후(고혼잡 회피) = 대안 장소 │    ║
║  │ 카테고리별 장소 수 제한: 총 6곳 (정보 과부하 방지)             │    ║
║  │   예) 문화유산 2 + 미식 2 + 포토스팟 1 + 숙박 1              │    ║
║  └─────────────────────────────────────────────────────────────┘    ║
╚══════════════════╦═══════════════════════════════════════════════════╝
                   ↓
╔══════════════════╩═══════════════════════════════════════════════════╗
║  [STEP 5] 카테고리별 부가기능 부착                                    ║
║                                                                      ║
║  문화유산 장소 ──→ [오디오 가이드 자동 재생]                          ║
║                    위치 반경 50m 진입 감지                            ║
║                    + 계절/성향/언어 스토리 분기                       ║
║                    + 수상 사진 비주얼                                 ║
║                                                                      ║
║  미식 장소 ──────→ [예약 URL 즉시 연결]                               ║
║                    detailCommon2 > reservationUrl                   ║
║                    + 식비 자동 합산 (1.5만원/인/식)                   ║
║                                                                      ║
║  포토스팟 장소 ──→ [수상 사진 각도 가이드]                             ║
║                    photo-contest-winners 컨텍스트 카드                ║
║                    + 카카오맵 핀 (16개 시도 대안)                     ║
║                                                                      ║
║  모든 장소 ──────→ [경비 자동 합산]                                   ║
║                    입장료(usefee) + 숙박(roomrate)                   ║
║                    + 이동비(카카오 모빌리티 거리×단가)                 ║
║                                                                      ║
║  시도 방문 완료 ─→ [팔도 스탬프 적립]                                 ║
║                    인증사진 EXIF 위치 매칭                            ║
║                    + 소외 지역 방문 시 1.5~2배 리워드                 ║
╚══════════════════╦═══════════════════════════════════════════════════╝
                   ↓
╔══════════════════╩═══════════════════════════════════════════════════╗
║  [STEP 6] 최종 출력                                                  ║
║  원페이지 플랜 (Day1 / Day2 타임라인 카드)                            ║
║  → [카카오맵 경로 실행] [카카오톡 플랜 공유] [팔도 스탬프 현황]        ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 7. 오디오 가이드 자동 재생 트리거 조건

### 7-1. 트리거 발동 조건 (AND 조건)

```
조건 1: 현재 선택된 카테고리 = "문화유산" (contentTypeId 14 또는 76)
   AND
조건 2: 디바이스 GPS 위치가 해당 POI 좌표 기준 반경 50m 이내 진입
   AND
조건 3: audio-guide API에 해당 contentId 오디오 URL 존재
   AND
조건 4: 사용자가 오디오 자동 재생 권한 허용 (최초 1회 동의)

→ 위 4개 조건 충족 시: 진동 알림 + 오디오 자동 재생 시작
```

### 7-2. 스토리 분기 로직

```
오디오 재생 시작
   │
   ├─ 언어 설정 감지
   │    ├─ 한국어  → tourism-info-korean 오디오 + 한국인 앵글 스토리
   │    ├─ 영어    → tourism-info-english 오디오 + 외국인 비교 스토리
   │    ├─ 일본어  → tourism-info-japanese 오디오
   │    └─ 중국어  → tourism-info-chinese-simplified 오디오
   │
   ├─ 현재 계절 감지 (서버 날짜 기준)
   │    ├─ 봄 (3~5월)  → 봄 버전 스토리 + 해금 배경음
   │    ├─ 여름 (6~8월) → 여름 버전 스토리 + 대금 배경음
   │    ├─ 가을 (9~11월) → 가을 버전 스토리 + 아쟁 배경음
   │    └─ 겨울 (12~2월) → 겨울 버전 스토리 + 첼로 배경음
   │
   └─ 사용자 성향 프로필 (최초 온보딩 시 선택)
        ├─ 전통감성 → 역사·인물 중심 내레이션
        ├─ 계절사진 → 포토 포인트 + 수상작 각도 안내
        ├─ 조용한 탐험 → 잔잔한 배경음 + 짧은 서술
        ├─ 활달한 탐험 → 퀴즈·퀘스트 삽입형 스토리
        └─ 미식 연계 → 해당 문화재 인근 로컬 식당 스토리 연결
```

### 7-3. 재생 종료 후 동작

```
오디오 종료
→ "다음 이야기 장소" 추천 카드 팝업
   (related-attractions API 기반, 반경 500m 내 오디오 보유 POI)
→ 수상사진 각도 보기 버튼 (photo-contest-winners)
→ "이 장소 친구에게 공유" (카카오톡 공유 API)
→ 팔도 스탬프 획득 여부 확인 (방문 인증 트리거)
```

---

## 8. 혼잡도·경비·동선 통합 최적화 의사 알고리즘

```python
# TripCraft Korea — 핵심 최적화 로직 (의사 코드)

def generate_plan(category, region, duration_days, party_size):

    # ── STEP 1: 후보 풀 수집 ──────────────────────────────────────────
    candidates = []

    # 카테고리 contentTypeId 매핑
    type_ids = CATEGORY_TYPE_MAP[category]  # 예: 문화유산 → [14, 76]

    # TourAPI 장소 수집
    raw_places = tourapi.areaBasedList2(
        areaCode=REGION_CODE[region],
        contentTypeId=type_ids,
        numOfRows=50
    )

    # 연관 관광지 보완
    related = tourapi.related_attractions.searchKeyword1(
        keyword=f"{region} {category}",
        numOfRows=20
    )
    candidates = merge_and_deduplicate(raw_places + related)


    # ── STEP 2: 혼잡도 점수 산출 ────────────────────────────────────────
    for place in candidates:
        # 집중률 등급 조회 (1=한산 ~ 5=매우혼잡)
        crowd_grade = tourapi.visitor_concentration_forecast.tatsCnctrRatedList(
            contentId=place.id
        ).grade  # 1~5

        # 여유로움 지수 = 바이럴 기준 장소 방문자 / 해당 장소 방문자
        # (값이 클수록 여유로움)
        viral_visitors = tourapi.tourism_big_data.locgoRegnVisitrDDList(
            region=VIRAL_HOTSPOT[region]
        ).avg_last_6months

        place_visitors = tourapi.tourism_big_data.locgoRegnVisitrDDList(
            region=place.area
        ).avg_last_6months

        place.leisure_index = viral_visitors / max(place_visitors, 1)
        place.crowd_score = crowd_grade  # 낮을수록 좋음


    # ── STEP 3: 유사도 점수 산출 (포토스팟·문화유산 카테고리) ─────────────
    if category in ["포토스팟", "문화유산"]:
        viral_vector = chromadb.get_vector(VIRAL_HOTSPOT[region])

        for place in candidates:
            place_vector = chromadb.get_vector(place.id)

            sim_type   = catcode_match(place, VIRAL_HOTSPOT[region]) * 0.40
            sim_image  = cosine_similarity(
                             place_vector.clip_embedding,
                             viral_vector.clip_embedding
                         ) * 0.40
            sim_text   = cosine_similarity(
                             place_vector.text_embedding,
                             viral_vector.text_embedding
                         ) * 0.20

            place.similarity_score = sim_type + sim_image + sim_text


    # ── STEP 4: 소외 지역 가중치 보정 ────────────────────────────────────
    diversity_index = tourapi.area_tourism_diversity.areaTouDivList(
        areaCode=REGION_CODE[region]
    ).diversity_score

    # 다양성 지수 하위 33% 시도: 가중치 1.5배
    diversity_multiplier = 1.5 if diversity_index < DIVERSITY_THRESHOLD_33PCT else 1.0

    for place in candidates:
        place.final_score = (
            (1.0 / max(place.crowd_score, 1))   # 혼잡도 역수 (낮을수록 좋음)
            * place.leisure_index                # 여유로움 지수
            * getattr(place, "similarity_score", 1.0)  # 유사도 (해당 카테고리만)
            * diversity_multiplier               # 소외 지역 보정
        )


    # ── STEP 5: 상위 후보 선택 ────────────────────────────────────────────
    top_places = sorted(candidates, key=lambda p: p.final_score, reverse=True)

    # 카테고리 구성: 총 6곳 (정보 과부하 방지)
    # 예: 문화유산 2 + 미식 2 + 포토스팟 1 + 숙박 1
    selected = apply_category_quota(top_places, quota=CATEGORY_QUOTA[category])


    # ── STEP 6: 동선 최적화 ──────────────────────────────────────────────
    # 카카오 모빌리티 API로 장소 간 이동 시간 행렬 계산
    travel_matrix = kakao_mobility.get_travel_time_matrix(
        origins=[p.coordinates for p in selected],
        destinations=[p.coordinates for p in selected]
    )

    # 혼잡 타이밍 고려한 방문 순서 최적화
    # 오전 = 저혼잡 인기 장소, 오후 = 대안·여유 장소
    ordered_plan = optimize_visit_order(
        places=selected,
        travel_matrix=travel_matrix,
        crowd_schedule=get_crowd_schedule(selected),  # 시간대별 혼잡도
        duration_days=duration_days
    )


    # ── STEP 7: 경비 계산 ────────────────────────────────────────────────
    total_cost = 0
    cost_breakdown = {}

    for place in ordered_plan:
        detail = tourapi.tourism_info_korean.detailCommon2(contentId=place.id)

        # 입장료
        entry_fee = parse_fee(detail.usefee) * party_size
        cost_breakdown[place.name + "_입장료"] = entry_fee

        # 식비 (미식 카테고리 장소)
        if place.contentTypeId in [38, 39]:
            meal_cost = MEAL_DEFAULT_PRICE * party_size  # 1.5만원 × 인원
            cost_breakdown[place.name + "_식비"] = meal_cost

        # 숙박비
        if place.contentTypeId == 32:
            room_info = tourapi.tourism_info_korean.detailInfo2(contentId=place.id)
            stay_cost = parse_roomrate(room_info.roomrate)  # 2인 기준
            cost_breakdown[place.name + "_숙박"] = stay_cost

        total_cost += sum(cost_breakdown.values())

    # 이동비 = 카카오 모빌리티 거리(km) × 연비(12km/L) × 유가(1,700원/L)
    total_distance_km = sum(travel_matrix.distances(ordered_plan))
    transport_cost = (total_distance_km / 12) * 1700
    cost_breakdown["이동비_자가용"] = transport_cost
    total_cost += transport_cost


    # ── STEP 8: 카테고리별 부가기능 부착 ────────────────────────────────
    for place in ordered_plan:
        # 문화유산: 오디오 가이드 트리거 설정
        if place.contentTypeId in [14, 76]:
            place.audio_trigger = AudioTrigger(
                radius_meters=50,
                audio_url=tourapi.audio_guide.getAudioUrl(place.id),
                season=get_current_season(),
                language=user.language_preference,
                persona=user.travel_persona
            )

        # 예약 URL 첨부
        if detail.reservationUrl:
            place.booking_url = detail.reservationUrl

        # 포토스팟: 수상사진 각도 카드 첨부
        if category == "포토스팟":
            place.photo_guide = tourapi.photo_contest_winners.koKeyword(
                keyword=place.name
            )


    # ── STEP 9: 팔도 스탬프 체크 ────────────────────────────────────────
    stamp_status = get_user_stamp_status(user.id, region)
    stamp_reward_multiplier = diversity_multiplier  # 소외 지역 1.5~2배 리워드


    # ── 최종 반환 ─────────────────────────────────────────────────────────
    return TripPlan(
        region=region,
        category=category,
        days=ordered_plan,               # Day1, Day2, ... 타임라인 카드
        total_cost=total_cost,
        cost_breakdown=cost_breakdown,
        stamp_status=stamp_status,
        stamp_reward_multiplier=stamp_reward_multiplier,
        kakao_map_deeplink=build_kakao_map_route(ordered_plan)
    )
```

---

## 9. 활용 API 전체 목록

| 단계 | API ID | 오퍼레이션 | 용도 | 소스 아이디어 |
|------|--------|-----------|------|--------------|
| 바이럴 감지 | `visitor-concentration-forecast` | `tatsCnctrRateList` | 방문자 급증 장소 탐지 | A+ |
| 바이럴 감지 | `visitor-concentration-forecast` | `tatsCnctrRatedList` | 집중률 등급 (혼잡도 보정) | A+, B+ |
| 방문자 통계 | `tourism-big-data` | `locgoRegnVisitrDDList` | 여유로움 지수, 트렌딩 지역 | A+, B+ |
| 소외 지역 | `area-tourism-diversity` | `areaTouDivList` | 시도별 다양성 지수 (가중치 보정) | A+, B+, Audio v2 |
| 수요 밀집도 | `area-tourism-demand-density` | `areaTarExpDsList` | 지역별 관광 수요 강도 | A+, KoreaPath |
| 장소 수집 | `tourism-info-korean` | `areaBasedList2` | catcode 필터 장소 풀 수집 | A+, B+ |
| 장소 수집 | `tourism-info-korean` | `searchKeyword2` | 카테고리·키워드 장소 검색 | B+ |
| 장소 상세 | `tourism-info-korean` | `detailCommon2` | 입장료·예약URL·주소·좌표 | B+ |
| 숙박 정보 | `tourism-info-korean` | `detailInfo2` | 숙박비(roomrate) | B+ |
| 위치 기반 | `tourism-info-korean` | `locationBasedList2` | 주변 장소 조회 | B+ |
| 이미지 | `tourism-info-korean` | `detailImage2` | CLIP 임베딩용 이미지 URL | A+ |
| 연관 관광지 | `related-attractions` | `searchKeyword1` | 연관 관광지 동선 보완 | A+, B+, Audio v2, KoreaPath |
| 지자체 핵심 | `central-attractions-by-municipality` | `areaBasedList1` | 시도 핀 초기값, 핵심 자연지 | A+, KoreaPath |
| 오디오 가이드 | `audio-guide` | getAudioUrl | 문화유산 오디오 콘텐츠 | Audio v2 |
| 수상 사진 | `photo-contest-winners` | `koKeyword` | 계절 비주얼·포토 각도 가이드 | Audio v2, B+ |
| 관광 사진 | `tourism-photos` | `galSearchKeyword` | 카드 UI 고품질 이미지 | B+ |
| 다국어 (영) | `tourism-info-english` | — | 영어권 오디오 스토리 | Audio v2 |
| 다국어 (일) | `tourism-info-japanese` | — | 일본어 오디오 스토리 | Audio v2 |
| 다국어 (중) | `tourism-info-chinese-simplified` | — | 중국어 오디오 스토리 | Audio v2 |
| 서비스 수요 | `area-tourism-resource-demand` | `areaTarSvcDemList` | 인기 장소 유형 파악 | B+ |
| 경로 | 카카오맵 API | 길찾기 / 모빌리티 | 동선 실행·이동비 계산 | 전체 |
| 공유 | 카카오톡 공유 API | 메시지 공유 | 플랜 공유 | A+, B+ |
| 인증 | 카카오 로그인 API | OAuth 2.0 | 간편 로그인·스탬프 이력 | A+, B+ |
| 소셜 트렌드 | 네이버 블로그 검색 API | — | 지역 트렌드 장소 추출 | B+ |

---

## 10. 기술 스택

| 분류 | 스택 | 출처 |
|------|------|------|
| 이미지 유사도 | CLIP 모델 (로컬, 무료) | A+ |
| 텍스트 임베딩 | sentence-transformers (로컬, 무료) | A+ |
| 벡터 DB | Chroma DB (로컬, 무료) | A+ |
| 임베딩 전처리 | Google Colab GPU (무료 티어, 처리 시간 약 5~8시간) | A+ |
| TourAPI 베이스 | `http://apis.data.go.kr/B551011/KorService1/` | 전체 |
| 위치 감지 | 디바이스 GPS (HTML5 Geolocation API) | Audio v2 |
| 오디오 재생 | Web Audio API / HTML5 Audio | Audio v2 |
| 이동 경비 계산 | 카카오 모빌리티 거리 × 연비(12km/L) × 유가(1,700원/L) | B+ |
| 스탬프 인증 | 사진 EXIF 위치 + 국세청 오픈API (영수증 OCR) | B+ |
| 유료 API | 없음 (완전 로컬·무료 구현) | A+ |

---

## 11. 팔도 스탬프 시스템 (확장 레이어)

### 11-1. 인증 흐름

```
시도 방문 완료
→ 대표 관광지: 인증 사진 업로드
   (EXIF 위치 + 촬영 시점 24시간 이내 + TourAPI 장소 매칭)
→ 지역 식당: 영수증 등록
   (OCR → 사업자번호 → 국세청 API 조회 → 결제일 ±1일 확인)
→ 이미지 해시 중복 체크 (동일 사진 재사용 방지)
→ 스탬프 적립
```

### 11-2. 리워드 구조

| 리워드 | 기준 | 소외 지역 보정 |
|--------|------|---------------|
| 지역상품권 | 시도별 1개 | 다양성 지수 하위 33% 시도 → 1.5~2배 |
| 숙박 할인 쿠폰 | 야놀자·여기어때 제휴 | 동일 보정 적용 |
| 카카오페이 포인트 | 완주(17시도) 달성 시 | 보너스 지급 |

### 11-3. 3단계 여정 구조

```
단기 (오늘 여행)  →  중기 (지역 스탬프 수집)  →  장기 (17시도 전국 완주)
   원페이지 플랜          시도별 인증·리워드          전국 여행 달성 배지
```

---

## 12. 공모전 강점 요약

| 평가 항목 | 배점 | TripCraft Korea 대응 |
|-----------|------|----------------------|
| 서비스 기획력 | 30 | 4개 아이디어 통합 → 카테고리 기반 원스톱 플랜 생성. ChatGPT 대비 명확한 실행 차별화 |
| 서비스 완성도 | 30 | 오디오 자동 재생·경비·동선·스탬프 완결 플로우. 원페이지 실행형 UI |
| 데이터 활용 | 20 | TourAPI 13종 + 카카오 3종 + 네이버 1종 + 오디오 API + 다국어 3종 = 21개 API 교차 활용 |
| 서비스 발전성 | 20 | 팔도 스탬프 장기 여정·다국어·AR 연계·실시간 통신사 데이터 로드맵 |
| 가점: 지역 특화 | +2 | 소외 지역 가중치 1.5배 + 다양성 지수 기반 균형 분산 = KTO 정책 직결 |

---

## 13. 페르소나 × 카테고리 시나리오

### 시나리오 A — 20대 인스타 여행자 (포토스팟 카테고리)
이지수(27세, 마케터)가 강릉 안목해변이 인스타에서 바이럴 중임을 확인. TripCraft Korea에서 "포토스팟" 카테고리, 강원도 선택. CLIP 유사도 91%의 대안 3곳(시흥 오이도·화성 궁평항·안산 대부도)을 지도 핀으로 제시. "오이도 일몰 각도 공모전 수상작 보기" 버튼으로 촬영 가이드 확인 후 카카오맵 경로 실행.

### 시나리오 B — 40대 가족 여행자 (문화유산 카테고리)
최동훈(44세, 교사, 초등생 자녀 2명)이 "문화유산, 경주, 1박2일" 입력. 혼잡도 낮은 오전 시간대에 첨성대 배치, 가을 시즌 스토리 자동 감지. 반경 50m 진입 시 "신라의 밤하늘 — 가을 별자리와 첨성대 설계 이야기" 오디오 자동 재생. 경비 합산: 입장료 0원 + 숙박 12만원 + 이동비 3.2만원 = 총 15.2만원.

### 시나리오 C — 외국인 FIT 여행자 (문화유산 카테고리, 영어 모드)
프랑스인 Marc(35세)가 영어 모드로 서울 선택. 오디오 가이드가 창덕궁 후원에서 "UNESCO World Heritage — Korea's royal garden designed by Confucian philosophy" 영어 스토리 자동 재생. "HIDDEN STORIES" 모드로 관광 지도에 없는 비유명 문화유산(조선 궁중 우물터) 별 아이콘 발견.

### 시나리오 D — 30대 직장인 주말 여행 (미식 카테고리)
박현우(32세, 직장인)가 "미식, 대전, 당일치기" 입력. 네이버 블로그 트렌드 + 소외 지역 가중치 1.5배(대전 = 다양성 지수 중하위) 적용, 대전 성심당 외 지역 맛집 2곳 큐레이션. 원페이지에 예약 URL + 경비(식비 3만원) 자동 합산. 완료 후 팔도 스탬프 "대전" 획득, 지역상품권 1.5배 리워드.

---

## 14. 개인정보 및 법적 검토

| 항목 | 처리 방침 |
|------|----------|
| GPS 위치 | 오디오 트리거 전용. 사용자 동의 후 사용, 서버 저장 없음 |
| 인증 사진 EXIF | 장소 매칭 후 즉시 파기. 원본 좌표 미저장 |
| 영수증 이미지 | OCR 처리 후 사업자번호·결제일만 추출, 원본 즉시 파기 |
| 블로그 파싱 | 네이버 공식 검색 API (크롤링 아님) |
| 카카오 로그인 | 이름·이메일 최소 수집, 개인정보처리방침 명시 |
| 이용 데이터 | 장소 선택 이력은 익명 세션 집계만 사용 (개인 식별 불가) |

---

## 15. 개발 로드맵

| 기간 | 작업 | 담당 아이디어 기능 |
|------|------|------------------|
| D-14 ~ D-11 | TourAPI 26만건 수집 + CLIP 임베딩 파이프라인 (Colab GPU) | A+ |
| D-10 ~ D-9 | Chroma DB 구축 + 유사도 검색 API 서버 | A+ |
| D-8 ~ D-7 | 카테고리 큐레이션 알고리즘 + 혼잡도 점수 로직 | KoreaPath, A+ |
| D-6 ~ D-5 | 원페이지 플랜 UI + Day1/Day2 타임라인 카드 | B+ |
| D-4 ~ D-3 | 오디오 가이드 위치 감지 + 계절/언어 분기 로직 | Audio v2 |
| D-3 ~ D-2 | 경비 계산·팔도 스탬프·카카오 API (맵·톡·로그인) 연동 | B+ |
| D-1 | 전체 통합 QA + 발표 자료 준비 | — |
| D-Day | 제출 | — |

---

_작성일: 2026-05-05_  
_통합 소스: KoreaPath AI / Audio Story Korea v2 / 아이디어 A+ / 아이디어 B+_
