# 한국관광공사_두루누비 정보 서비스_GW — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/두루누비-정보-서비스/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_두루누비 정보 서비스_GW |
| 카탈로그 ID | uddi:Durunubi |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/Durunubi` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: 걷기·자전거 여행길 전용. 코스/노선 2가지 오퍼레이션.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `courseList` | `/courseList` | 두루누비 코스 목록 조회 | - | ✅ |
| `routeList` | `/routeList` | 두루누비 노선 목록 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `courseList`

**용도**: 두루누비 코스 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Durunubi/courseList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1
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
| `routeIdx` | 코스 인덱스 | code | T_ROUTE_MNG0000000001 | - |
| `crsIdx` | crsIdx | code | T_CRS_MNG0000005117 | - |
| `crsKorNm` | crsKorNm | string | 남파랑길 2코스 | - |
| `crsDstnc` | crsDstnc | number | 19 | - |
| `crsTotlRqrmHour` | crsTotlRqrmHour | number | 450 | - |
| `crsLevel` | crsLevel | number | 2 | - |
| `crsCycle` | crsCycle | string | 비순환형 | - |
| `crsContents` | crsContents | string | 갈맷길 3-3구간과 중첩되는 구간으로 부산대교에서 영도구로 진입하여 영도대교로 돌아나오는 구간이다.  영도구 | - |
| `crsSummary` | crsSummary | string | - 부산역에서 시작하여 걷기 좋은 봉래산을 지나 흰여울문화마을로 이어지는 코스 <br>- 영도구에 조성되어  | - |
| `crsTourInfo` | crsTourInfo | string | - 산책을 하기 좋고 약수터 물맛 좋은 '봉래산' <br>- 바다와 배가 어우러진 풍경을 만나는 ‘절영해안길 | - |
| `travelerinfo` | travelerinfo | string | - 시점 : 부산역 (부산 동구 중앙대로 210) <br>교통편) 부산지하철 1호선 부산역<br>- 종점 : | - |
| `sigun` | sigun | string | 부산 중구 | - |
| `brdDiv` | brdDiv | string | DNWW | - |
| `gpxpath` | gpxpath | string | https://www.durunubi.kr/editImgUp.do?filePath=/data/koreamob | - |
| `createdtime` | 등록일시 | datetime | 20200216031049 | - |
| `modifiedtime` | 수정일시 | datetime | 20250716071617 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"routeIdx": "T_ROUTE_MNG0000000001", "crsIdx": "T_CRS_MNG0000005117", "crsKorNm": "남파랑길 2코스", "crsDstnc": "19", "crsTotlRqrmHour": "450", "crsLevel": "2", "crsCycle": "비순환형", "crsContents": "갈맷길 3-3구간과 중첩되는 구간으로 부산대교에서 영도구로 진입하여 영도대교로 돌아나오는 구간이다.  영도구에 조성되어 있는 봉래산 둘레길 및 태종대 일원을 걷는 구간이 포함되어 있어 숲길과 바닷길, 마을길 등을 다양하게 접할 수 있는 매력을 보유하고 있다. 6.25전쟁 때 피난민의 추억과 애환이 서린 부산 최초의 연육교인 영도대교를 포하하여 태종대의 절경을 감상할 수 있으며, 영도구 원도심 개발에 따라 핫 스페이스로 떠오르고 있는 깡깡이 예술마을, 흰여울 마을 등이 인접하고 있어 매력적인 걷기여행이 가능한 구간이다. ", "crsSummary": "- 부산역에서 시작하여 걷기 좋은 봉래산을 지나 흰여울문화마을로 이어지는 코스 <br>- 영도구에 조성되어 있는 봉래산 둘레길 및 태종대 일원을 걷는 구간이 포함되어 있어 숲길과 바닷길, 마을길 등을 다양하게 접할 수 있는 매력을 보유하고 있는 구간<br>- 6.25전쟁 때 피난민의 추억과 애환이 서린 부산 최초의 연륙교인 영도대교를 포하하여 영도구 원도심 개발에 따라 핫 스페이스로 떠오르고 있는 깡깡이 예술마을, 흰여울 마을 등이 인접하고 있어 매력적인 걷기여행이 가능한 코스<br>- 부산의 갈맷길 3-3코스가 포함된 구간으로 초보자에게도 어렵지 않은 코스", "crsTourInfo": "- 산책을 하기 좋고 약수터 물맛 좋은 '봉래산' <br>- 바다와 배가 어우러진 풍경을 만나는 ‘절영해안길’<br>- 멋있는 절경과 아름다운 벽화를 볼 수 있는 '흰여울 문화마을'", "travelerinfo": "- 시점 : 부산역 (부산 동구 중앙대로 210) <br>교통편) 부산지하철 1호선 부산역<br>- 종점 : 영도대교 입구(부산 중구 태종로 8) <br>교통편) 지하철 남포역 하차 후 도보 이동<br>- 길이 어렵지 않아 편히 걸을 수 있는 길이며 주변에 편의시설이 많아 부담이 없음 ", "sigun": "부산 중구", "brdDiv": "DNWW", "gpxpath": "https://www.durunubi.kr/editImgUp.do?filePath=/data/koreamobility/course/summap/T_CRS_MNG0000005117.gpx", "createdtime": "20200216031049", "modifiedtime": "20250716071617"}
{"routeIdx": "T_ROUTE_MNG0000000001", "crsIdx": "T_CRS_MNG0000005118", "crsKorNm": "남파랑길 3코스", "crsDstnc": "14", "crsTotlRqrmHour": "330", "crsLevel": "2", "crsCycle": "비순환형", "crsContents": "갈맷길 4-1구간과 중첩되는 구간으로 최근 부산에서 가장 떠오르는 관광명소인 송도해상케이블카, 송도해수욕장, 암남공원, 감천항까지 이어지는 구간이다. <br>구간내 입지한 송도해수욕장은 우리나라 제1호 해수욕장으로 동양의 나폴리라고 칭송받을 만큼 아름다운 해안선이 유명하며 송도해상케이블카는 해상을 지나는 케이블카로 최근 많은 관광객들이 방문하고 있다. ", "crsSummary": "- 부산의 가장 떠오르는 관광명소인 송도해상케이블카와 송도해수욕장, 암남공원, 감천항까지 이어지는 코스<br>- 부산의 유명 관광지들을 둘러볼 수 있는 다채로운 코스이자 동양의 나폴리라 불리울 만큼 바다와 자연을 어우르는 아름다운 해안경관을 감상할 수 있는 구간<br>- 부산 갈맷길 4-1코스가 포함되어 있는 코스", "crsTourInfo": "- 부산의 유명한 관광지인 용두산공원, 국제시장, 활기찬 '자갈치 수산시장'<br>- 우리나라 제1호 해수욕장으로 동양의 나폴리라고 칭송받을 만큼 아름다운 해안선이 유명한 '송도해수욕장'<br>- 두도전망대까지 이어지는 숲과 해안절경이 어우러진 '암남공원’<br>- 단층면의 윗부분이 아래로 떨어진 정단층을 만날 수 있는 '지질생태탐방로'", "travelerinfo": "- 시점 : 영도대교 입구(부산 중구 태종로 8)<br>교통편) 지하철 남포역 6번출구 도보 이동<br>- 종점 : 감천사거리(부산 사하구 감천동 447-6)<br>교통편) 부산역 17번 버스, 감천우체국 하차 <br>- 영도대교에서 출발하므로 교통편 편리하며 부산역에서 지하철, 버스편 다수 있음 <br>- 국제시장, 자갈치 충무동, 송도해수욕장, 암남공원 등에 식당, 카페 다수 있어 이용 편리함<br>- 영도대교 도개시간은 오후 2시부터 2시15분까지로 다리가 열리는 모습을 볼 수 있음 ", "sigun": "부산 영도구", "brdDiv": "DNWW", "gpxpath": "https://www.durunubi.kr/editImgUp.do?filePath=/data/koreamobility/file/2025/05/5917b2c95528439596244d4f3275258b.gpx", "createdtime": "20200216031659", "modifiedtime": "20250716071729"}
{"routeIdx": "T_ROUTE_MNG0000000001", "crsIdx": "T_CRS_MNG0000005119", "crsKorNm": "남파랑길 4코스", "crsDstnc": "22", "crsTotlRqrmHour": "450", "crsLevel": "2", "crsCycle": "비순환형", "crsContents": "갈맷길 4-2, 4-3구간 중첩되는 구간으로 몰운대, 다대포해변공원, 아미산전망대를 거쳐 사하구 신평동 교차로까지 이어지는 구간이다.  기암괴석과 해송으로 우거진 숲, 수려한 모래해안으로 빼어난 겨관을 자랑하고, 국가지질공원에 포함된 몰운대를 포함하여 낙동강 하구를 조망할 수 있는 아미산 전망대는 일몰 명소로 각광받는 부산의 새로운 관광명소로 자리잡아가고 있다.  다대포 해변공원에는 화려한 조명과 음악과 함껙 작동되는 꿈의낙조 분수가 있어 낭만적인 야간관광 명소로서의 특징을 보유하고 있다.  ", "crsSummary": "- 몰운대, 다대포 해변공원, 아미산 전망대를 거쳐 사하구까지 이어지는 구간으로 국가지질공원으로 지정된 주요 자원을 두루 살펴볼 수 있는 코스<br>- 기암괴석과 해송으로 우거진 숲, 수려한 모래해안으로 빼어난 경관을 자랑하고, 국가지질공원에 포함된 몰운대와 일몰 명소 아미산 전망대가 포함된 부산의 각광받는 관광명소<br>- 다대포항을 지나면서 어촌 골목 곳곳을 구경할 수 있으며 해송이 우거진 숲길이 있는 몰운대가 있어 걷기 좋은 최고의 코스<br>- 부산의 갈맷길 4-1, 4-2코스가 포함된 코스", "crsTourInfo": "- 확 트인 바다 경치를 볼 수 있는 '두송반도전망대'와 멸치떼를 볼 수 있는 '야망대' <br>- 화려한 조명과 음악과 함껙 작동되는 꿈의낙조 분수가 있어 낭만적인 야간관광 명소 '다대포 해수욕장'<br>- 낙동강 하구를 조망할 수 있는 일몰 명소 '아미산 전망대'", "travelerinfo": "- 시점 : 감천사거리(부산 사하구 감천동 449-2) <br>교통편) 부산역 17번 버스, 감천우체국 하차<br>- 종점 : 사하구 신평동교차로(부산 사하구 신평동 642-17)<br> 교통편) 지하철1호선 신평역 도보 이동<br>- 시내에 있으나 산길과 돌길이 많으므로 등산화 혹은 러닝화를 착용하는 것이 좋음", "sigun": "부산 사하구", "brdDiv": "DNWW", "gpxpath": "https://www.durunubi.kr/editImgUp.do?filePath=/data/koreamobility/course/summap/T_CRS_MNG0000005119.gpx", "createdtime": "20200216032154", "modifiedtime": "20260424064007"}
```

**TripCraft 활용 포인트**: 걷기·자전거 코스 목록. 액티비티 여행 코스 추천.

---

### 3.2 `routeList`

**용도**: 두루누비 노선 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Durunubi/routeList?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `routeIdx` | 코스 인덱스 | code | T_ROUTE_MNG0000000001 | - |
| `themeNm` | themeNm | string | 남파랑길 | - |
| `linemsg` | linemsg | string | 남쪽의 쪽빛 바다와 함께 걷는 길 | - |
| `themedescs` | themedescs | string | <p><span style=font-size: 11pt; font-family: 굴림, gulim;>'남파랑 | - |
| `brdDiv` | brdDiv | string | DNWW | - |
| `createdtime` | 등록일시 | datetime | 20210308064716 | - |
| `modifiedtime` | 수정일시 | datetime | 20210507030000 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"routeIdx": "T_ROUTE_MNG0000000001", "themeNm": "남파랑길", "linemsg": "남쪽의 쪽빛 바다와 함께 걷는 길", "themedescs": "<p><span style=font-size: 11pt; font-family: 굴림, gulim;>'남파랑길'은 '남쪽의 쪽빛 바다와 함께 걷는 길'이라는 뜻으로,부산 오륙도 해맞이 공원에서 전남 해남 땅끝마을까지 남해안을 따라 연결된 총 90개 코스, 1,470km의 걷기 여행이다.\t\t\t\t\t\t\t </span><br><span style=font-size: 11pt; font-family: 굴림, gulim;>남해의 수려한 해안경관과 대도시의 화려함,&nbsp;농촌어촌마을의 소박함을 모두 체험할 수 있는 길이다. &nbsp;</span></p>", "brdDiv": "DNWW", "createdtime": "20210308064716", "modifiedtime": "20210507030000"}
{"routeIdx": "T_ROUTE_MNG0000000043", "themeNm": "서해랑길", "linemsg": "서쪽의 바다와 함께 걷는길", "themedescs": "<p style=margin-left: 40px;>&nbsp;</p><p>서해랑길은 전남 해남 땅끝탑에서 인천 강화를 연결하는 109개 코스, 1,800km의 걷기여행길로, 서쪽(西)의 바다(파도)와 함께(랑) 걷는 길을 의미합니다.<br>                        서해랑길 을 따라 천천히 걷다보면 유네스코 세계유산으로 지정된 드넓은 갯벌과 황홀한 일몰, 종교와 문물교류의 역사를 만나게 됩니다.                    </p>", "brdDiv": "DNWW", "createdtime": "20220623060800", "modifiedtime": "20220623060800"}
{"routeIdx": "T_ROUTE_MNG0000000047", "themeNm": "DMZ 평화의 길", "linemsg": "평화와 통일의 의미를 되새기는 길", "themedescs": "<p>‘DMZ 평화의 길’은 한반도의 마지막 청정 자연환경을 자랑하는 DMZ 일대를 따라 구축한 총 35개 코스, 510km의 걷기여행길입니다.<br>DMZ 초입인 민간인통제선 인근에 자리한 최전방 마을, 전적지, 평야와 강, 산악 지형을 지나며 한반도 중부의 아름다운 풍경을 감상하고,<br>평화와 통일의 의미를 되새길 수 있는 길입니다. &nbsp;</p>", "brdDiv": "DNWW", "createdtime": "20240918085625", "modifiedtime": "20240918085625"}
```

**TripCraft 활용 포인트**: 두루누비 노선 정보. 장거리 트레일 코스 계획.

---

## 5. 코드 카탈로그

