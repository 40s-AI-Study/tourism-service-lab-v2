# 한국관광공사_일문 관광정보서비스_GW — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/일문-관광정보서비스/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_일문 관광정보서비스_GW |
| 카탈로그 ID | uddi:JpnService2 |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/JpnService2` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: 일본어 관광정보 전용. 국문서비스(KorService2)와 동일 구조, 콘텐츠는 일어.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `areaBasedList2` | `/areaBasedList2` | 지역코드 기반 관광정보 목록 조회 | - | ✅ |
| `areaBasedSyncList2` | `/areaBasedSyncList2` | 변경된 관광정보 동기화 목록 조회 | - | ✅ |
| `areaCode2` | `/areaCode2` | 지역코드 조회 | - | ✅ |
| `categoryCode2` | `/categoryCode2` | 서비스분류코드 조회 | - | ✅ |
| `detailCommon2` | `/detailCommon2` | 콘텐츠 공통정보 상세 조회 | contentId(콘텐츠ID) | ❌ |
| `detailImage2` | `/detailImage2` | 이미지 목록 조회 | contentId | ❌ |
| `detailInfo2` | `/detailInfo2` | 반복정보(상세 추가정보) 조회 | contentId, contentTypeId | ❌ |
| `detailIntro2` | `/detailIntro2` | 콘텐츠 소개정보 상세 조회 | contentId, contentTypeId | ❌ |
| `lclsSystmCode2` | `/lclsSystmCode2` | 관광분류체계 코드 조회 | - | ✅ |
| `ldongCode2` | `/ldongCode2` | 법정동코드 조회 | - | ✅ |
| `locationBasedList2` | `/locationBasedList2` | 위치(위경도) 기반 반경 내 관광정보 목록 조회 | mapX(경도), mapY(위도), radius(반경m) | ✅ |
| `searchFestival2` | `/searchFestival2` | 행사/축제 정보 조회 | eventStartDate(행사시작일 YYYYMMDD) | ✅ |
| `searchKeyword2` | `/searchKeyword2` | 키워드 검색 조회 | - | ✅ |
| `searchStay2` | `/searchStay2` | 숙박정보 목록 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `areaBasedList2`

**용도**: 지역코드 기반 관광정보 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/areaBasedList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&arrange=A&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | ソウル特別市カンナム区アプクジョンロ416 | - |
| `addr2` | 상세주소 | string | (청담동) | - |
| `areacode` | 지역코드 | code | 1 | - |
| `cat1` | 대분류 코드 | string | A04 | - |
| `cat2` | 중분류 코드 | string | A0401 | - |
| `cat3` | 소분류 코드 | string | A04010600 | - |
| `contentid` | 콘텐츠 ID | code | 3390494 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 79 | - |
| `createdtime` | 등록일시 | datetime | 20230202222603 | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/71/2778971_image2_ | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/71/2778971_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 127.0424468728 | - |
| `mapy` | 위도(WGS84) | coord | 37.5269655478 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20251028133326 | - |
| `sigungucode` | 시군구코드 | code | 1 | - |
| `tel` | 전화번호 | string |  | - |
| `title` | 관광지명 | string | 10 Corso Como 淸潭店(10꼬르소꼬모 청담점) | - |
| `zipcode` | 우편번호 | code | 06015 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 11 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 680 | - |
| `lclsSystm1` | 관광분류체계1 | string | SH | - |
| `lclsSystm2` | 관광분류체계2 | string | SH05 | - |
| `lclsSystm3` | 관광분류체계3 | string | SH050200 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "ソウル特別市カンナム区アプクジョンロ416", "addr2": "(청담동)", "areacode": "1", "cat1": "A04", "cat2": "A0401", "cat3": "A04010600", "contentid": "3390494", "contenttypeid": "79", "createdtime": "20230202222603", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/71/2778971_image2_1.png", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/71/2778971_image3_1.png", "cpyrhtDivCd": "Type3", "mapx": "127.0424468728", "mapy": "37.5269655478", "mlevel": "6", "modifiedtime": "20251028133326", "sigungucode": "1", "tel": "", "title": "10 Corso Como 淸潭店(10꼬르소꼬모 청담점)", "zipcode": "06015", "lDongRegnCd": "11", "lDongSignguCd": "680", "lclsSystm1": "SH", "lclsSystm2": "SH05", "lclsSystm3": "SH050200"}
{"addr1": "チョンラナム道シンアン郡チャウンソブ2ギル508-65", "addr2": "", "areacode": "38", "cat1": "A02", "cat2": "A0202", "cat3": "A02020600", "contentid": "3102897", "contenttypeid": "76", "createdtime": "20240220121138", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/48/3007148_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/48/3007148_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "125.9959235736", "mapy": "34.8779816821", "mlevel": "6", "modifiedtime": "20240417102745", "sigungucode": "12", "tel": "", "title": "1004ミュージアムパーク（1004 뮤지엄파크）", "zipcode": "58831", "lDongRegnCd": "46", "lDongSignguCd": "910", "lclsSystm1": "VE", "lclsSystm2": "VE02", "lclsSystm3": "VE020100"}
{"addr1": "キョンサンブクト　キョンジュシ　ウォンヒョロ　141", "addr2": "", "areacode": "35", "cat1": "B02", "cat2": "B0201", "cat3": "B02010900", "contentid": "2025574", "contenttypeid": "80", "createdtime": "20150827231322", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/21/2577221_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/21/2577221_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "129.2164644431", "mapy": "35.8422236040", "mlevel": "6", "modifiedtime": "20241219181527", "sigungucode": "2", "tel": "+82-54-742-8502~3", "title": "141ミニホテル（141미니호텔）", "zipcode": "38153", "lDongRegnCd": "47", "lDongSignguCd": "130", "lclsSystm1": "AC", "lclsSystm2": "AC04", "lclsSystm3": "AC040100"}
```

**TripCraft 활용 포인트**: 일본어 지역별 관광지 목록 제공.

---

### 3.2 `areaBasedSyncList2`

**용도**: 변경된 관광정보 동기화 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/areaBasedSyncList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 울산광역시 울주군 상북면 알프스온천2길 58 | - |
| `addr2` | 상세주소 | string | (상북면) | - |
| `areacode` | 지역코드 | code | 7 | - |
| `cat1` | 대분류 코드 | string | B02 | - |
| `cat2` | 중분류 코드 | string | B0201 | - |
| `cat3` | 소분류 코드 | string | B02010900 | - |
| `contentid` | 콘텐츠 ID | code | 2368071 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 80 | - |
| `createdtime` | 등록일시 | datetime | 20160216191925 | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/72/826072_image2_1 | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/72/826072_image3_1 | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 129.0746322333 | - |
| `mapy` | 위도(WGS84) | coord | 35.5531229737 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20220520165315 | - |
| `sigungucode` | 시군구코드 | code | 5 | - |
| `tel` | 전화번호 | string | +82-52-254-8890 | - |
| `title` | 관광지명 | string | 샌디아모텔 | - |
| `zipcode` | 우편번호 | code | 44952 | - |
| `showflag` | showflag | number | 0 | - |
| `lDongRegnCd` | 법정동 시도코드 | code |  | - |
| `lDongSignguCd` | 법정동 시군구코드 | code |  | - |
| `lclsSystm1` | 관광분류체계1 | string |  | - |
| `lclsSystm2` | 관광분류체계2 | string |  | - |
| `lclsSystm3` | 관광분류체계3 | string |  | - |
| `oldContentid` | oldContentid | code | 2368071 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "울산광역시 울주군 상북면 알프스온천2길 58", "addr2": "(상북면)", "areacode": "7", "cat1": "B02", "cat2": "B0201", "cat3": "B02010900", "contentid": "2368071", "contenttypeid": "80", "createdtime": "20160216191925", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/72/826072_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/72/826072_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "129.0746322333", "mapy": "35.5531229737", "mlevel": "6", "modifiedtime": "20220520165315", "sigungucode": "5", "tel": "+82-52-254-8890", "title": "샌디아모텔", "zipcode": "44952", "showflag": "0", "lDongRegnCd": "", "lDongSignguCd": "", "lclsSystm1": "", "lclsSystm2": "", "lclsSystm3": "", "oldContentid": "2368071"}
{"addr1": "ソウル特別市カンナム区アプクジョンロ416", "addr2": "(청담동)", "areacode": "1", "cat1": "A04", "cat2": "A0401", "cat3": "A04010600", "contentid": "3390494", "contenttypeid": "79", "createdtime": "20230202222603", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/71/2778971_image2_1.png", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/71/2778971_image3_1.png", "cpyrhtDivCd": "Type3", "mapx": "127.0424468728", "mapy": "37.5269655478", "mlevel": "6", "modifiedtime": "20251028133326", "sigungucode": "1", "tel": "", "title": "10 Corso Como 淸潭店(10꼬르소꼬모 청담점)", "zipcode": "06015", "showflag": "1", "lDongRegnCd": "11", "lDongSignguCd": "680", "lclsSystm1": "SH", "lclsSystm2": "SH05", "lclsSystm3": "SH050200", "oldContentid": "3390494"}
{"addr1": "チョンラナム道シンアン郡チャウンソブ2ギル508-65", "addr2": "", "areacode": "38", "cat1": "A02", "cat2": "A0202", "cat3": "A02020600", "contentid": "3102897", "contenttypeid": "76", "createdtime": "20240220121138", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/48/3007148_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/48/3007148_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "125.9959235736", "mapy": "34.8779816821", "mlevel": "6", "modifiedtime": "20240417102745", "sigungucode": "12", "tel": "", "title": "1004ミュージアムパーク（1004 뮤지엄파크）", "zipcode": "58831", "showflag": "1", "lDongRegnCd": "46", "lDongSignguCd": "910", "lclsSystm1": "VE", "lclsSystm2": "VE02", "lclsSystm3": "VE020100", "oldContentid": "3102897"}
```

**TripCraft 활용 포인트**: TripCraft 변경된 관광정보 동기화 목록 조회 기능에 활용.

---

### 3.3 `areaCode2`

**용도**: 지역코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/areaCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `rnum` | rnum | number | 1 | - |
| `code` | code | code | 1 | - |
| `name` | name | string | ソウル特別市 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"rnum": 1, "code": "1", "name": "ソウル特別市"}
{"rnum": 2, "code": "2", "name": "仁川広域市"}
{"rnum": 3, "code": "3", "name": "大田広域市"}
```

**TripCraft 활용 포인트**: TripCraft 지역코드 조회 기능에 활용.

---

### 3.4 `categoryCode2`

**용도**: 서비스분류코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/categoryCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `code` | code | code | A01 | - |
| `name` | name | string | 自然 | - |
| `rnum` | rnum | number | 1 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"code": "A01", "name": "自然", "rnum": 1}
{"code": "A02", "name": "人文（文化／芸術／歴史）", "rnum": 2}
{"code": "A03", "name": "レジャースポーツ", "rnum": 3}
```

**TripCraft 활용 포인트**: TripCraft 서비스분류코드 조회 기능에 활용.

---

### 3.5 `detailCommon2`

**용도**: 콘텐츠 공통정보 상세 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/detailCommon2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&serviceKey=${SERVICE_KEY}
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
| contentId | - | 필수 | string | - | 콘텐츠ID |

**응답 필드**:

> ⚠️ 수집 시 데이터 없음 (필수 파라미터 미충족 또는 결과 없음)

**응답 예시 (최대 3건 발췌)**:

> 샘플 없음

**TripCraft 활용 포인트**: 일본어 관광지 상세 공통정보.

---

### 3.6 `detailImage2`

**용도**: 이미지 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/detailImage2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&serviceKey=${SERVICE_KEY}
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
| contentId | - | 필수 | string | - | - |

**응답 필드**:

> ⚠️ 수집 시 데이터 없음 (필수 파라미터 미충족 또는 결과 없음)

**응답 예시 (최대 3건 발췌)**:

> 샘플 없음

**TripCraft 활용 포인트**: TripCraft 이미지 목록 조회 기능에 활용.

---

### 3.7 `detailInfo2`

**용도**: 반복정보(상세 추가정보) 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/detailInfo2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=142785&contentTypeId=32&serviceKey=${SERVICE_KEY}
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
| contentId | - | 필수 | string | - | - |
| contentTypeId | - | 필수 | string | - | - |

**응답 필드**:

> ⚠️ 수집 시 데이터 없음 (필수 파라미터 미충족 또는 결과 없음)

**응답 예시 (최대 3건 발췌)**:

> 샘플 없음

**TripCraft 활용 포인트**: TripCraft 반복정보(상세 추가정보) 조회 기능에 활용.

---

### 3.8 `detailIntro2`

**용도**: 콘텐츠 소개정보 상세 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/detailIntro2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&contentTypeId=12&serviceKey=${SERVICE_KEY}
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
| contentId | - | 필수 | string | - | - |
| contentTypeId | - | 필수 | string | - | - |

**응답 필드**:

> ⚠️ 수집 시 데이터 없음 (필수 파라미터 미충족 또는 결과 없음)

**응답 예시 (최대 3건 발췌)**:

> 샘플 없음

**TripCraft 활용 포인트**: TripCraft 콘텐츠 소개정보 상세 조회 기능에 활용.

---

### 3.9 `lclsSystmCode2`

**용도**: 관광분류체계 코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/lclsSystmCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `code` | code | code | AC | - |
| `name` | name | string | 宿泊 | - |
| `rnum` | rnum | number | 1 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"code": "AC", "name": "宿泊", "rnum": 1}
{"code": "EV", "name": "フェスティバル/パフォーマンス/イベント", "rnum": 2}
{"code": "EX", "name": "体験観光", "rnum": 3}
```

**TripCraft 활용 포인트**: TripCraft 관광분류체계 코드 조회 기능에 활용.

---

### 3.10 `ldongCode2`

**용도**: 법정동코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/ldongCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `rnum` | rnum | number | 1 | - |
| `code` | code | code | 11 | - |
| `name` | name | string | ソウル特別市 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"rnum": 1, "code": "11", "name": "ソウル特別市"}
{"rnum": 2, "code": "26", "name": "プサン(釜山)広域市"}
{"rnum": 3, "code": "27", "name": "テグ(大邱)広域市"}
```

**TripCraft 활용 포인트**: TripCraft 법정동코드 조회 기능에 활용.

---

### 3.11 `locationBasedList2`

**용도**: 위치(위경도) 기반 반경 내 관광정보 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/locationBasedList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&mapX=126.9779692&mapY=37.566535&radius=2000&serviceKey=${SERVICE_KEY}
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
| mapX | - | 필수 | string | - | 경도 |
| mapY | - | 필수 | string | - | 위도 |
| radius | - | 필수 | string | - | 반경m |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `addr1` | 주소 | string | ソウル特別市 中区 世宗大路 110 | - |
| `addr2` | 상세주소 | string | （太平路1街） | - |
| `areacode` | 지역코드 | code | 1 | - |
| `cat1` | 대분류 코드 | string | A02 | - |
| `cat2` | 중분류 코드 | string | A0206 | - |
| `cat3` | 소분류 코드 | string | A02060900 | - |
| `contentid` | 콘텐츠 ID | code | 2035563 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 78 | - |
| `createdtime` | 등록일시 | datetime | 20151027003000 | - |
| `dist` | 거리(m) | number | 36.41538270629469 | - |
| `firstimage` | 대표 이미지 URL | url |  | - |
| `firstimage2` | 썸네일 URL | url |  | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code |  | - |
| `mapx` | 경도(WGS84) | coord | 126.9783710306 | - |
| `mapy` | 위도(WGS84) | coord | 37.5665986816 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20221214112903 | - |
| `sigungucode` | 시군구코드 | code | 24 | - |
| `tel` | 전화번호 | string |  | - |
| `title` | 관광지명 | string | ソウル図書館（서울도서관） | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 11 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 140 | - |
| `lclsSystm1` | 관광분류체계1 | string | VE | - |
| `lclsSystm2` | 관광분류체계2 | string | VE09 | - |
| `lclsSystm3` | 관광분류체계3 | string | VE090300 | - |
| `zipcode` | 우편번호 | code | 04524 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "ソウル特別市 中区 世宗大路 110", "addr2": "（太平路1街）", "areacode": "1", "cat1": "A02", "cat2": "A0206", "cat3": "A02060900", "contentid": "2035563", "contenttypeid": "78", "createdtime": "20151027003000", "dist": "36.41538270629469", "firstimage": "", "firstimage2": "", "cpyrhtDivCd": "", "mapx": "126.9783710306", "mapy": "37.5665986816", "mlevel": "6", "modifiedtime": "20221214112903", "sigungucode": "24", "tel": "", "title": "ソウル図書館（서울도서관）", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "VE", "lclsSystm2": "VE09", "lclsSystm3": "VE090300", "zipcode": "04524"}
{"addr1": "ソウル特別市チュン区セジョンデロ110", "addr2": "", "areacode": "1", "cat1": "A02", "cat2": "A0208", "cat3": "A02081300", "contentid": "3544324", "contenttypeid": "85", "createdtime": "20250925144744", "dist": "37.92616508764378", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/57/3535457_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/57/3535457_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.9777210995", "mapy": "37.5662570431", "mlevel": "6", "modifiedtime": "20251023143000", "sigungucode": "24", "tel": "+82-2-2000-9324", "title": "K-POPカバーダンスフェスティバルワールドファイナル（K-POP 커버댄스 페스티벌 월드 파이널）", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "EV", "lclsSystm2": "EV03", "lclsSystm3": "EV030400", "zipcode": "04524"}
{"addr1": "ソウル特別市チュン区セジョンデロ110", "addr2": "", "areacode": "1", "cat1": "A02", "cat2": "A0202", "cat3": "A02020700", "contentid": "281901", "contenttypeid": "76", "createdtime": "20040202232513", "dist": "91.67985289352555", "firstimage": "", "firstimage2": "", "cpyrhtDivCd": "", "mapx": "126.9780155330", "mapy": "37.5657098894", "mlevel": "6", "modifiedtime": "20240619164133", "sigungucode": "24", "tel": "", "title": "ソウル広場（서울광장）", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "VE", "lclsSystm2": "VE03", "lclsSystm3": "VE030500", "zipcode": "04524"}
```

**TripCraft 활용 포인트**: 일본어 사용자 대상 위치기반 관광지 검색. 다국어 TripCraft 일어 버전 지도 뷰.

---

### 3.12 `searchFestival2`

**용도**: 행사/축제 정보 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/searchFestival2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&eventStartDate=20260101&serviceKey=${SERVICE_KEY}
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
| eventStartDate | - | 필수 | string | - | 행사시작일 YYYYMMDD |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `addr1` | 주소 | string | キョンギ道アニャン市マナン区イェスルゴンウォンロ180 | - |
| `addr2` | 상세주소 | string |  | - |
| `zipcode` | 우편번호 | code | 13911 | - |
| `cat1` | 대분류 코드 | string |  | - |
| `cat2` | 중분류 코드 | string |  | - |
| `cat3` | 소분류 코드 | string |  | - |
| `contentid` | 콘텐츠 ID | code | 3113653 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 85 | - |
| `createdtime` | 등록일시 | datetime | 20240412172541 | - |
| `eventstartdate` | eventstartdate | datetime | 20260310 | - |
| `eventenddate` | eventenddate | datetime | 20261130 | - |
| `firstimage` | 대표 이미지 URL | url |  | - |
| `firstimage2` | 썸네일 URL | url |  | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code |  | - |
| `mapx` | 경도(WGS84) | coord | 126.92561681569023 | - |
| `mapy` | 위도(WGS84) | coord | 37.41945269174406 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20260407132547 | - |
| `areacode` | 지역코드 | code |  | - |
| `sigungucode` | 시군구코드 | code |  | - |
| `tel` | 전화번호 | string | +82-31-687-0548 | - |
| `title` | 관광지명 | string | APAP作品ツアー（安養公共芸術プロジェクト）（APAP 작품투어（안양공공예술프로젝트）） | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 41 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 171 | - |
| `lclsSystm1` | 관광분류체계1 | string | EV | - |
| `lclsSystm2` | 관광분류체계2 | string | EV03 | - |
| `lclsSystm3` | 관광분류체계3 | string | EV030400 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "キョンギ道アニャン市マナン区イェスルゴンウォンロ180", "addr2": "", "zipcode": "13911", "cat1": "", "cat2": "", "cat3": "", "contentid": "3113653", "contenttypeid": "85", "createdtime": "20240412172541", "eventstartdate": "20260310", "eventenddate": "20261130", "firstimage": "", "firstimage2": "", "cpyrhtDivCd": "", "mapx": "126.92561681569023", "mapy": "37.41945269174406", "mlevel": "6", "modifiedtime": "20260407132547", "areacode": "", "sigungucode": "", "tel": "+82-31-687-0548", "title": "APAP作品ツアー（安養公共芸術プロジェクト）（APAP 작품투어（안양공공예술프로젝트））", "lDongRegnCd": "41", "lDongSignguCd": "171", "lclsSystm1": "EV", "lclsSystm2": "EV03", "lclsSystm3": "EV030400"}
{"addr1": "テグ広域市タルソ区トゥリュゴンウォンロ200", "addr2": "", "zipcode": "42666", "cat1": "A02", "cat2": "A0207", "cat3": "A02070200", "contentid": "2042147", "contenttypeid": "85", "createdtime": "20151120235220", "eventstartdate": "20251115", "eventenddate": "20260228", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/84/3019684_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/84/3019684_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "128.5648324581", "mapy": "35.8548822436", "mlevel": "6", "modifiedtime": "20251112133620", "areacode": "4", "sigungucode": "2", "tel": "+82-70-7549-8112", "title": "E-WORLDイルミネーション（이월드 일루미네이션）", "lDongRegnCd": "27", "lDongSignguCd": "290", "lclsSystm1": "EV", "lclsSystm2": "EV01", "lclsSystm3": "EV010200"}
{"addr1": "전북특별자치도 남원시 양림길 54 (어현동)", "addr2": "国立民俗国楽院イェウォンダン", "zipcode": "55795", "cat1": "", "cat2": "", "cat3": "", "contentid": "3436865", "contenttypeid": "85", "createdtime": "20241204161811", "eventstartdate": "20260314", "eventenddate": "20261212", "firstimage": "", "firstimage2": "", "cpyrhtDivCd": "", "mapx": "127.3908846008636", "mapy": "35.40217923512243", "mlevel": "6", "modifiedtime": "20260416140652", "areacode": "", "sigungucode": "", "tel": "", "title": "K-国楽ステージ(K-국악 스테이지)", "lDongRegnCd": "52", "lDongSignguCd": "190", "lclsSystm1": "EV", "lclsSystm2": "EV02", "lclsSystm3": "EV020100"}
```

**TripCraft 활용 포인트**: 일본어 축제 일정 검색.

---

### 3.13 `searchKeyword2`

**용도**: 키워드 검색 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/searchKeyword2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&keyword=%EA%B2%BD%EB%B3%B5%EA%B6%81&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | ソウル特別市 道峰区 トボンロ610 | - |
| `addr2` | 상세주소 | string |  | - |
| `areacode` | 지역코드 | code | 1 | - |
| `cat1` | 대분류 코드 | string | A05 | - |
| `cat2` | 중분류 코드 | string | A0502 | - |
| `cat3` | 소분류 코드 | string | A05020100 | - |
| `contentid` | 콘텐츠 ID | code | 2696129 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 82 | - |
| `createdtime` | 등록일시 | datetime | 20201210202832 | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/27/3339327_image2_ | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/27/3339327_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 127.0412487847 | - |
| `mapy` | 위도(WGS84) | coord | 37.6589779599 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20240731112710 | - |
| `sigungucode` | 시군구코드 | code | 10 | - |
| `tel` | 전화번호 | string | +82-2-992-6777 | - |
| `title` | 관광지명 | string | Kyungbokkung 倉洞 ( 경복궁 창동 ) | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 11 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 320 | - |
| `lclsSystm1` | 관광분류체계1 | string | FD | - |
| `lclsSystm2` | 관광분류체계2 | string | FD01 | - |
| `lclsSystm3` | 관광분류체계3 | string | FD010100 | - |
| `zipcode` | 우편번호 | code | 01401 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "ソウル特別市 道峰区 トボンロ610", "addr2": "", "areacode": "1", "cat1": "A05", "cat2": "A0502", "cat3": "A05020100", "contentid": "2696129", "contenttypeid": "82", "createdtime": "20201210202832", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/27/3339327_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/27/3339327_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "127.0412487847", "mapy": "37.6589779599", "mlevel": "6", "modifiedtime": "20240731112710", "sigungucode": "10", "tel": "+82-2-992-6777", "title": "Kyungbokkung 倉洞 ( 경복궁 창동 )", "lDongRegnCd": "11", "lDongSignguCd": "320", "lclsSystm1": "FD", "lclsSystm2": "FD01", "lclsSystm3": "FD010100", "zipcode": "01401"}
{"addr1": "ソウル特別市チョンノ区ユンボソンギル42", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4034391", "contenttypeid": "79", "createdtime": "20260307035722", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/17/4024517_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/17/4024517_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.983821068557", "mapy": "37.5779865507226", "mlevel": "", "modifiedtime": "20260318101007", "sigungucode": "", "tel": "", "title": "[事後免税店]ANDERSSON BELL（アンダーソンベル）・キョンボックン（景福宮）フラッグシップストア(앤더슨벨 경복궁 플래그쉽 스토어)", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300", "zipcode": "03060"}
{"addr1": "ソウル特別市チョンノ区チャハムンロ2ギル4", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4033932", "contenttypeid": "79", "createdtime": "20260307010642", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/67/4029467_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/67/4029467_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.972859321085", "mapy": "37.576377886406", "mlevel": "", "modifiedtime": "20260323102555", "sigungucode": "", "tel": "", "title": "[事後免税店]DAISO（ダイソー）・キョンボックン（景福宮）駅店(다이소 경복궁역점)", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300", "zipcode": "03044"}
```

**TripCraft 활용 포인트**: 일본어 키워드 통합 검색.

---

### 3.14 `searchStay2`

**용도**: 숙박정보 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/JpnService2/searchStay2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | キョンサンブクト　キョンジュシ　ウォンヒョロ　141 | - |
| `addr2` | 상세주소 | string |  | - |
| `areacode` | 지역코드 | code | 35 | - |
| `sigungucode` | 시군구코드 | code | 2 | - |
| `cat1` | 대분류 코드 | string | B02 | - |
| `cat2` | 중분류 코드 | string | B0201 | - |
| `cat3` | 소분류 코드 | string | B02010900 | - |
| `contentid` | 콘텐츠 ID | code | 2025574 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 80 | - |
| `createdtime` | 등록일시 | datetime | 20150827231322 | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/21/2577221_image2_ | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/21/2577221_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 129.2164644431 | - |
| `mapy` | 위도(WGS84) | coord | 35.8422236040 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20241219181527 | - |
| `tel` | 전화번호 | string | +82-54-742-8502~3 | - |
| `title` | 관광지명 | string | 141ミニホテル（141미니호텔） | - |
| `zipcode` | 우편번호 | code | 38153 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 47 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 130 | - |
| `lclsSystm1` | 관광분류체계1 | string | AC | - |
| `lclsSystm2` | 관광분류체계2 | string | AC04 | - |
| `lclsSystm3` | 관광분류체계3 | string | AC040100 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "キョンサンブクト　キョンジュシ　ウォンヒョロ　141", "addr2": "", "areacode": "35", "sigungucode": "2", "cat1": "B02", "cat2": "B0201", "cat3": "B02010900", "contentid": "2025574", "contenttypeid": "80", "createdtime": "20150827231322", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/21/2577221_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/21/2577221_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "129.2164644431", "mapy": "35.8422236040", "mlevel": "6", "modifiedtime": "20241219181527", "tel": "+82-54-742-8502~3", "title": "141ミニホテル（141미니호텔）", "zipcode": "38153", "lDongRegnCd": "47", "lDongSignguCd": "130", "lclsSystm1": "AC", "lclsSystm2": "AC04", "lclsSystm3": "AC040100"}
{"addr1": "チョンラナムド　ナジュシ　キョドン2（イ）ギル　17-4", "addr2": "", "areacode": "38", "sigungucode": "6", "cat1": "B02", "cat2": "B0201", "cat3": "B02011600", "contentid": "2709773", "contenttypeid": "80", "createdtime": "20210312225143", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/24/2706124_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/24/2706124_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.7108537370", "mapy": "35.0333369927", "mlevel": "6", "modifiedtime": "20241223194913", "tel": "+82-61-331-3917", "title": "3917マジュン（出迎え）（3917마중）", "zipcode": "58248", "lDongRegnCd": "46", "lDongSignguCd": "170", "lclsSystm1": "AC", "lclsSystm2": "AC03", "lclsSystm3": "AC030200"}
{"addr1": "キョンサンナムド　チャンウォンシ　ソンサング　ヨンジロ　102　（ケナリ総合商店街）", "addr2": "", "areacode": "36", "sigungucode": "16", "cat1": "B02", "cat2": "B0201", "cat3": "B02010100", "contentid": "2814697", "contenttypeid": "80", "createdtime": "20220331133718", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/07/2808507_image2_1.png", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/07/2808507_image2_1.png", "cpyrhtDivCd": "Type3", "mapx": "128.6783758898", "mapy": "35.2245192728", "mlevel": "6", "modifiedtime": "20241030110931", "tel": "+82-55-266-3600", "title": "ATビジネスホテル (AT비지니스호텔)", "zipcode": "51515", "lDongRegnCd": "48", "lDongSignguCd": "123", "lclsSystm1": "AC", "lclsSystm2": "AC01", "lclsSystm3": "AC010100"}
```

**TripCraft 활용 포인트**: TripCraft 숙박정보 목록 조회 기능에 활용.

---

## 4. contentTypeId 매핑

| 코드 | 분류명 |
|------|--------|
| 12 | 관광지 |
| 14 | 문화시설 |
| 15 | 축제공연행사 |
| 25 | 여행코스 |
| 28 | 레포츠 |
| 32 | 숙박 |
| 38 | 쇼핑 |
| 39 | 음식점 |

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

