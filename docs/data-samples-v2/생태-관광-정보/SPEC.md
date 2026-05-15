# 한국관광공사_생태 관광 정보_GW — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/생태-관광-정보/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_생태 관광 정보_GW |
| 카탈로그 ID | uddi:GreenTourService1 |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/GreenTourService1` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: 생태관광지 전용. 일반 KorService2와 필드 유사하나 생태 특화 콘텐츠.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `areaBasedList1` | `/areaBasedList1` | 생태관광 지역기반 목록 조회 | - | ✅ |
| `areaBasedSyncList1` | `/areaBasedSyncList1` | 생태관광 동기화 목록 조회 | - | ✅ |
| `areaCode1` | `/areaCode1` | 지역코드 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `areaBasedList1`

**용도**: 생태관광 지역기반 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/GreenTourService1/areaBasedList1?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&arrange=A&serviceKey=${SERVICE_KEY}
```

**요청 파라미터**:

| 파라미터명 | 한글명 | 필수/옵션 | 타입 | 샘플 값 | 설명 |
|-----------|--------|---------|------|--------|------|
| serviceKey | 인증키 | 필수 | string | ${SERVICE_KEY} | data.go.kr 발급 서비스키 |
| MobileOS | OS 구분 | 필수 | string | ETC | ETC/AND/IOS/WIN |
| MobileApp | 앱 명칭 | 필수 | string | TripCraftKorea | 앱 이름 |
| _type | 응답 형식 | 필수 | string | json | json/xml |
| numOfRows | 페이지당 결과수 | 옵션 | number | 5 | 기본값 10 |
| pageNo | 페이지 번호 | 옵션 | number | 1 | 기본값 1 |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `addr` | addr | string | 부산광역시 사하구 다대동 일대 | - |
| `areacode` | 지역코드 | code | 6 | - |
| `contentid` | 콘텐츠 ID | code | 2547516 | - |
| `createdtime` | 등록일시 | datetime | 20180513231114 | - |
| `mainimage` | mainimage | url | http://tong.visitkorea.or.kr/cms/resource/68/2547068_image2_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `modifiedtime` | 수정일시 | datetime | 20250117165959 | - |
| `sigungucode` | 시군구코드 | code | 10 | - |
| `subtitle` | subtitle | string |  | - |
| `summary` | summary | string | 두송반도는 다대포항의 동쪽에 위치한 좁고 긴 반도로 주변에는 조선소와 공장지대가 발달해 있다. 공룡의 전성시 | - |
| `tel` | 전화번호 | string | 051-888-3636 | - |
| `telname` | 전화번호 명칭 | string | 부산광역시 환경보전과 | - |
| `title` | 관광지명 | string | 두송반도명소 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr": "부산광역시 사하구 다대동 일대", "areacode": "6", "contentid": "2547516", "createdtime": "20180513231114", "mainimage": "http://tong.visitkorea.or.kr/cms/resource/68/2547068_image2_1.jpg", "cpyrhtDivCd": "Type3", "modifiedtime": "20250117165959", "sigungucode": "10", "subtitle": "", "summary": "두송반도는 다대포항의 동쪽에 위치한 좁고 긴 반도로 주변에는 조선소와 공장지대가 발달해 있다. 공룡의 전성시대였던 백악기 말의 부산지역 지질의 모습을 한눈에 보여주는 으뜸 명소이다. 특히 과거 지진이 기록된 다양한 산출 상태의 쇄설성 암맥과 고지진암이 절경이다. 퇴적층에서는 공룡알둥지와 파편화석이 나타나고, 이회암, 석화목, 환원점, 석회질고토양등의 흥미로운 지질특성들은 높은 학술적 가치를 가진다.\n\n* 문의 : 051-888-3636\n* 관련 홈페이지 : <a href=\"https://www.busan.go.kr/geopark/dusong\" target=\"_blank\" title=\"새창 : 홈페이지로 이동\">https://www.busan.go.kr/geopark/dusong</a>  \n\n◎이용안내\n- 이용요금 : 무료\n- 화장실 : 있음(남녀구분)\n- 장애인 편의시설 : 장애인화장실 있음(남녀구분)\n- 주차시설 : 없음", "tel": "051-888-3636", "telname": "부산광역시 환경보전과", "title": "두송반도명소"}
{"addr": "경상북도 울진군 근남면 성류굴로 225", "areacode": "35", "contentid": "2549195", "createdtime": "20180526000919", "mainimage": "http://tong.visitkorea.or.kr/cms/resource/38/2548938_image2_1.jpg", "cpyrhtDivCd": "Type3", "modifiedtime": "20251210100153", "sigungucode": "18", "subtitle": "", "summary": "성류굴은 울창한 측백나무와 함께 사계절 관광객이 찾는 천연석회암 동굴로서 천연기념물이다. 총길이 472m의 동굴은 종유석과 석순이 끝없이 펼쳐져 있고, 왕피천과 통하고 있는 12개의 광장과 5개의 연못에는 많은 어류가 서식하고 있다. 성류굴이라는 지금의 이름은 임진왜란 때 생겨났다. 임진왜란이 일어나자 굴 앞의 사찰에 있던 불상을 이 굴속에 피난시켰는데, 여기서 ‘성불(聖佛)이 유(留)한 굴’이라고 ‘성류굴’이라 부르게 된 것이다. 부처님 세 분이 일렬로 서 있는 듯한 삼불상이 특히 유명하다. 임진왜란 때는 인근 주민들이 왜적을 피해 이 성류굴로 피난했는데, 이를 탐지한 왜병들이 동굴입구를 막아 모두 굶어 죽었다 하며, 그 뒤 동굴 곳곳에서 사람의 뼈가 수도 없이 발견되었다는 슬픈 역사가 깃들어 있다.\n\n* 문의 : 054-789-5400\n* 이용시간 : 09:00~18:00 (11월~2월 09:00~17:00) \n* 쉬는 날 : 매주 월요일 / 단, 공휴일인 경우 개관 후 다음날 휴관\n* 홈페이지 : <a href=\"https://www.uljin.go.kr/tour/board/view.uljin?boardId=BBS_ATTRACTION_TU&menuCd=DOM_000000202001000000&orderBy=REGISTER_DATE%20DESC&startPage=1&searchType=DATA_TITLE&searchOperation=AND&categoryCode1=A01&dataSid=565\"target=\"_blank\" title=\"새창 : 울진군 문화관광 이동\">https://www.uljin.go.kr/</a>\n\n◎이용안내\n- 입장료 \n[개인]\n어른 5,000원 / 청소년·군인 3,000원 / 어린이 2,500원 / 노인 1,000원\n[단체(30인 이상)]\n어른 4,000원 / 청소년·군인 2,500원 / 어린이 2,000원 / 노인 1,000원", "tel": "054-789-5404", "telname": "성류굴관리사무소", "title": "성류굴"}
{"addr": "전라남도 완도군 청산면 도청길 일대", "areacode": "38", "contentid": "2509451", "createdtime": "20180612180007", "mainimage": "", "cpyrhtDivCd": "", "modifiedtime": "20241211091612", "sigungucode": "18", "subtitle": "", "summary": "청산도는 완도에서 19.2km 떨어진 다도해 최남단 섬으로 배를 타고 50분 정도 걸린다. 예로부터 공기가 맑고 산과 바다가 푸른 청산도는 청산여수(靑山麗水), 선원도(仙源島) 등 갖고 있는 이름도 많다. 1960년대에 고등어와 삼치가 많이 잡혀 파시(波市)가 열리는 등 어업전진기지 역할을 하기도 했으며, 임권택 감독의 ‘서편제’를 비롯해 다수의 영화와 드라마의 배경이 됐다. 구들장논, 해녀, 돌담장 등 섬 고유의 전통문화가 어우러진 청산도는 2007년 아시아 최초의 슬로시티로 선정된 데 이어 2011년 세계 슬로길 제1호 공식 인증을 거쳐 2013년 재인증됐다. 특히 청산도 구들장논은 2013년 국가중요농업유산 제1호로 지정된 데 이어 2014년 세계중요농업유산에 등재됐다. \n\n청산도 슬로길은 11개 코스(17길)가 있다. 슬로길을 걷다 보면 바람이 불 때 바위틈에서 범이 우는 소리가 난다 해서 이름 붙인 범바위, 역사성과 지역성을 살려 구현한 향토역사문화전시관, 편지 받고 싶은 달을 선택할 수 있는 12개의 월별 느림 우체통이 있는 느린 걸음 느림 카페, 파시문화거리, 섬갤러리, 포토존 등 이채로운 관광지가 발길을 잡는다. 관광객은 조개공예, 느림 우체통 편지 쓰기, 슬로푸드 등을 체험할 수 있고, 유채꽃이 만발하는 매년 4월이면 ‘느림은 행복이다’라는 주제로 슬로 걷기 축제의 막이 오른다.", "tel": "061-550-5114", "telname": "완도군 관광안내소", "title": "전남 완도 청산도 [슬로시티]"}
```

**TripCraft 활용 포인트**: 생태관광지 목록. 자연·에코 테마 여행 코스 생성.

---

### 3.2 `areaBasedSyncList1`

**용도**: 생태관광 동기화 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/GreenTourService1/areaBasedSyncList1?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
```

**요청 파라미터**:

| 파라미터명 | 한글명 | 필수/옵션 | 타입 | 샘플 값 | 설명 |
|-----------|--------|---------|------|--------|------|
| serviceKey | 인증키 | 필수 | string | ${SERVICE_KEY} | data.go.kr 발급 서비스키 |
| MobileOS | OS 구분 | 필수 | string | ETC | ETC/AND/IOS/WIN |
| MobileApp | 앱 명칭 | 필수 | string | TripCraftKorea | 앱 이름 |
| _type | 응답 형식 | 필수 | string | json | json/xml |
| numOfRows | 페이지당 결과수 | 옵션 | number | 5 | 기본값 10 |
| pageNo | 페이지 번호 | 옵션 | number | 1 | 기본값 1 |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `addr` | addr | string | 충청북도 제천시 청전동 240-1 일원 | - |
| `areacode` | 지역코드 | code | 33 | - |
| `contentid` | 콘텐츠 ID | code | 2547353 | - |
| `createdtime` | 등록일시 | datetime | 20180513211140 | - |
| `mainimage` | mainimage | url | http://tong.visitkorea.or.kr/cms/resource/33/2547233_image2_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `modifiedtime` | 수정일시 | datetime | 20251211113506 | - |
| `sigungucode` | 시군구코드 | code | 7 | - |
| `subtitle` | subtitle | string |  | - |
| `summary` | summary | string | 2005년 11월부터 2006년 11월까지 1년간 청전제천 21 실천협의회 연구분과위원회에서 연구, 조사를  | - |
| `tel` | 전화번호 | string | 043-641-6731~3 | - |
| `telname` | 전화번호 명칭 | string | 제천시청 문화관광과 | - |
| `title` | 관광지명 | string | 제천솔방죽 생태공원 | - |
| `showflag` | showflag | number | 0 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr": "충청북도 제천시 청전동 240-1 일원", "areacode": "33", "contentid": "2547353", "createdtime": "20180513211140", "mainimage": "http://tong.visitkorea.or.kr/cms/resource/33/2547233_image2_1.jpg", "cpyrhtDivCd": "Type3", "modifiedtime": "20251211113506", "sigungucode": "7", "subtitle": "", "summary": "2005년 11월부터 2006년 11월까지 1년간 청전제천 21 실천협의회 연구분과위원회에서 연구, 조사를 위탁하고 모니터링하여 사업비 14억 6천7백만 원 을 들여 시내권 내에 조성한 생태공원이다. 솔방죽의 저수 유입은 비룡담(제2 의림지)으로부터 농업용수를 사용 후 잠시 이곳에 저장된다. 원래의 연못은 1872년에 제작된 군, 현 지도에 ‘유등지’로 표기되었으나 ‘작은 연못’으로 불렸는데 청정제천 21 실천협의회에서 공원화 조성에 따라 ‘솔방죽’으로 이름을 붙였으며 제천시에서 처음으로 생태공원이라는 이름을 붙여 조성한 곳이다. 생태공원의 규모는 연면적 28,096㎡ 로 동서 220m, 남북 80~100m의 크기 저수지에 3개의 지역으로 나누어 조성되었다.\n\n\n* 문의 : 043-641-6731~3 \n* 휴무일 : 연중무휴 \n \n\n◎이용안내\n- 이용요금 : 무료\n- 화장실 : 있음(남녀구분) \n- 장애인 편의시설 : 장애인화장실 있음(남녀공용)\n- 주차시설 : 불가능", "tel": "043-641-6731~3", "telname": "제천시청 문화관광과", "title": "제천솔방죽 생태공원", "showflag": "0"}
{"addr": "충청북도 단양군 대강면 방곡리 일대", "areacode": "33", "contentid": "2547350", "createdtime": "20180513210229", "mainimage": "http://tong.visitkorea.or.kr/cms/resource/27/2547227_image2_1.jpg", "cpyrhtDivCd": "Type3", "modifiedtime": "20251211113317", "sigungucode": "2", "subtitle": "", "summary": "신선이 노닐다 간 자리라고 하여 퇴계 이황 선생이 친히 ‘삼선구곡(三仙九曲)’이라는 이름을 붙여 준 선암계곡은 10km에 이르는 청정계곡으로 농촌풍경길(사인암∼단성생활체육공원 8.4㎞) 등로와 가까이 있어서 시원하게 드라이브를 즐기면서 맑은 물과 눈부시게 하얀 너럭바위가 옹기종기 모인 풍경을 감상할 수 있는 코스이다. \n\n* 문의 : 043-420-2552\n* 관련 홈페이지 : <a href=\"https://www.danyang.go.kr/tour/527\" target=\"_blank\" title=\"새창 : 단양군 문화관광 홈페이지로 이동\">https://www.danyang.go.kr/tour/527</a>\n\n◎ 이용안내\n- 이용요금 : 무료 \n- 화장실 : 없음\n- 장애인 편의시설 : 없음\n- 주차시설 : 불가", "tel": "043-420-2552", "telname": "단양군청 문화관광과", "title": "선암골생태유람길(숲소리길)", "showflag": "0"}
{"addr": "충청북도 보은군 속리산면 법주사로 84", "areacode": "33", "contentid": "2547328", "createdtime": "20180513203608", "mainimage": "http://tong.visitkorea.or.kr/cms/resource/95/2547195_image2_1.jpg", "cpyrhtDivCd": "Type3", "modifiedtime": "20251211113302", "sigungucode": "3", "subtitle": "", "summary": "1970년 6번째 국립공원으로 지정되었으며 예로부터 제2금강 또는 소금강이라 불릴 만큼 경관이 빼어나다.\n총면적 274.766k㎡에 달하는 속리산국립공원은 충북과 경북의 여러 지역에 걸쳐 바위로 이루어진 산으로, 주요 봉우리인 천왕봉과 비로봉, 문장대는 백두대간의 장엄한 산줄기를 잇고 있어 암봉과 암릉이 잘 발달되어 있다. 속리산에는 많은 산들이 접해 있으며, 남쪽의 천왕봉(1,058m)을 중심으로 비로봉, 문장대, 관음봉 등 8개의 봉우리가 활처럼 휘어져 뻗어나간다.\n\n\n* 문의 : 043-542-5267\n* 관련 홈페이지 : <a href=\"http://songni.knps.or.kr/\" target=\"_blank\" title=\"새창 : 속리산국립공원 홈페이지로 이동\">http://songni.knps.or.kr/</a>\n\n◎이용안내\n- 이용요금 : 시설 이용료 상이, 홈페이지 참조\n- 화장실 : 있음(남녀구분)\n- 장애인 편의시설 : 장애인 주차장 있음(10여 대)\n- 주차시설 : 가능", "tel": "043-542-5267", "telname": "속리산국립공원관리사무소", "title": "속리산국립공원", "showflag": "0"}
```

**TripCraft 활용 포인트**: 생태관광 데이터 동기화.

---

### 3.3 `areaCode1`

**용도**: 지역코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/GreenTourService1/areaCode1?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
```

**요청 파라미터**:

| 파라미터명 | 한글명 | 필수/옵션 | 타입 | 샘플 값 | 설명 |
|-----------|--------|---------|------|--------|------|
| serviceKey | 인증키 | 필수 | string | ${SERVICE_KEY} | data.go.kr 발급 서비스키 |
| MobileOS | OS 구분 | 필수 | string | ETC | ETC/AND/IOS/WIN |
| MobileApp | 앱 명칭 | 필수 | string | TripCraftKorea | 앱 이름 |
| _type | 응답 형식 | 필수 | string | json | json/xml |
| numOfRows | 페이지당 결과수 | 옵션 | number | 5 | 기본값 10 |
| pageNo | 페이지 번호 | 옵션 | number | 1 | 기본값 1 |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `code` | code | code | 1 | - |
| `name` | name | string | 서울 | - |
| `rnum` | rnum | number | 1 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"code": "1", "name": "서울", "rnum": 1}
{"code": "2", "name": "인천", "rnum": 2}
{"code": "3", "name": "대전", "rnum": 3}
```

**TripCraft 활용 포인트**: 생태관광 지역코드 조회.

---

## 5. 코드 카탈로그

### 지역코드 (areacode)

| 코드 | 지역명 |
|------|--------|
| 1 | 서울 |
| 2 | 인천 |
| 3 | 대전 |
| 4 | 대구 |
| 5 | 광주 |
| 6 | 부산 |
| 7 | 울산 |
| 8 | 세종특별자치시 |
| 31 | 경기도 |
| 32 | 강원특별자치도 |
| 33 | 충청북도 |
| 34 | 충청남도 |
| 35 | 경상북도 |
| 36 | 경상남도 |
| 37 | 전라북도 |
| 38 | 전라남도 |
| 39 | 제주도 |

### 분류 코드 (cat1/cat2/cat3)

| 대분류(cat1) | 설명 |
|-------------|------|
| A01 | 자연 |
| A02 | 인문(문화/예술/역사) |
| A03 | 레포츠 |
| A04 | 쇼핑 |
| A05 | 음식 |
| B02 | 숙박 |
| C01 | 추천코스 |

