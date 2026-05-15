# 한국관광공사_무장애 여행 정보 — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/무장애-여행-정보/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_무장애 여행 정보 |
| 카탈로그 ID | uddi:KorWithService2 |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/KorWithService2` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: 무장애(배리어프리) 관광정보 전용. detailWithTour2로 접근성 세부정보 제공.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `areaBasedList2` | `/areaBasedList2` | 지역코드 기반 관광정보 목록 조회 | - | ✅ |
| `areaBasedSyncList2` | `/areaBasedSyncList2` | 변경된 관광정보 동기화 목록 조회 | - | ✅ |
| `areaCode2` | `/areaCode2` | 지역코드 조회 | - | ✅ |
| `categoryCode2` | `/categoryCode2` | 서비스분류코드 조회 | - | ✅ |
| `detailCommon2` | `/detailCommon2` | 콘텐츠 공통정보 상세 조회 | contentId(콘텐츠ID) | ✅ |
| `detailImage2` | `/detailImage2` | 이미지 목록 조회 | contentId | ✅ |
| `detailInfo2` | `/detailInfo2` | 반복정보(상세 추가정보) 조회 | contentId, contentTypeId | ❌ |
| `detailIntro2` | `/detailIntro2` | 콘텐츠 소개정보 상세 조회 | contentId, contentTypeId | ✅ |
| `detailWithTour2` | `/detailWithTour2` | 무장애 여행정보 상세 조회 | contentId, contentTypeId | ❌ |
| `lclsSystmCode2` | `/lclsSystmCode2` | 관광분류체계 코드 조회 | - | ✅ |
| `ldongCode2` | `/ldongCode2` | 법정동코드 조회 | - | ✅ |
| `locationBasedList2` | `/locationBasedList2` | 위치(위경도) 기반 반경 내 관광정보 목록 조회 | mapX(경도), mapY(위도), radius(반경m) | ✅ |
| `searchKeyword2` | `/searchKeyword2` | 키워드 검색 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `areaBasedList2`

**용도**: 지역코드 기반 관광정보 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/areaBasedList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&arrange=A&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 충청북도 청주시 흥덕구 가경동 | - |
| `addr2` | 상세주소 | number | 1438 | - |
| `areacode` | 지역코드 | code | 33 | - |
| `cat1` | 대분류 코드 | string | A04 | - |
| `cat2` | 중분류 코드 | string | A0401 | - |
| `cat3` | 소분류 코드 | string | A04010200 | - |
| `contentid` | 콘텐츠 ID | code | 1433504 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 38 | - |
| `createdtime` | 등록일시 | datetime | 20111111014944 | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/50/3492550_image2_ | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/50/3492550_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 127.4341171334 | - |
| `mapy` | 위도(WGS84) | coord | 36.6286485111 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20250521105928 | - |
| `sigungucode` | 시군구코드 | code | 10 | - |
| `tel` | 전화번호 | string |  | - |
| `title` | 관광지명 | string | 가경 터미널시장 | - |
| `zipcode` | 우편번호 | code | 28398 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 43 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 113 | - |
| `lclsSystm1` | 관광분류체계1 | string | SH | - |
| `lclsSystm2` | 관광분류체계2 | string | SH06 | - |
| `lclsSystm3` | 관광분류체계3 | string | SH060200 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "충청북도 청주시 흥덕구 가경동", "addr2": "1438", "areacode": "33", "cat1": "A04", "cat2": "A0401", "cat3": "A04010200", "contentid": "1433504", "contenttypeid": "38", "createdtime": "20111111014944", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/50/3492550_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/50/3492550_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "127.4341171334", "mapy": "36.6286485111", "mlevel": "6", "modifiedtime": "20250521105928", "sigungucode": "10", "tel": "", "title": "가경 터미널시장", "zipcode": "28398", "lDongRegnCd": "43", "lDongSignguCd": "113", "lclsSystm1": "SH", "lclsSystm2": "SH06", "lclsSystm3": "SH060200"}
{"addr1": "전라남도 진도군 고군면 신비의바닷길 47", "addr2": "(고군면)", "areacode": "38", "cat1": "A01", "cat2": "A0101", "cat3": "A01011200", "contentid": "126273", "contenttypeid": "12", "createdtime": "20031107090000", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/36/3079736_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/36/3079736_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.3547412438", "mapy": "34.4354594945", "mlevel": "6", "modifiedtime": "20250808090412", "sigungucode": "21", "tel": "", "title": "가계해수욕장", "zipcode": "58911", "lDongRegnCd": "46", "lDongSignguCd": "900", "lclsSystm1": "NA", "lclsSystm2": "NA02", "lclsSystm3": "NA020900"}
{"addr1": "서울특별시 종로구 평창30길 28 (평창동)", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "129854", "contenttypeid": "14", "createdtime": "20071106103314", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/11/3506711_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/11/3506711_image3_1.jpg", "cpyrhtDivCd": "Type1", "mapx": "126.97512913242", "mapy": "37.6122904729365", "mlevel": "6", "modifiedtime": "20260311100340", "sigungucode": "", "tel": "", "title": "가나아트센터", "zipcode": "03004", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "VE", "lclsSystm2": "VE07", "lclsSystm3": "VE070600"}
```

**TripCraft 활용 포인트**: 지역별 무장애 관광지 목록.

---

### 3.2 `areaBasedSyncList2`

**용도**: 변경된 관광정보 동기화 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/areaBasedSyncList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 충청북도 청주시 흥덕구 가경동 | - |
| `addr2` | 상세주소 | number | 1438 | - |
| `areacode` | 지역코드 | code | 33 | - |
| `cat1` | 대분류 코드 | string | A04 | - |
| `cat2` | 중분류 코드 | string | A0401 | - |
| `cat3` | 소분류 코드 | string | A04010200 | - |
| `contentid` | 콘텐츠 ID | code | 1433504 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 38 | - |
| `createdtime` | 등록일시 | datetime | 20111111014944 | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/50/3492550_image2_ | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/50/3492550_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 127.4341171334 | - |
| `mapy` | 위도(WGS84) | coord | 36.6286485111 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20250521105928 | - |
| `sigungucode` | 시군구코드 | code | 10 | - |
| `tel` | 전화번호 | string |  | - |
| `title` | 관광지명 | string | 가경 터미널시장 | - |
| `zipcode` | 우편번호 | code | 28398 | - |
| `showflag` | showflag | number | 1 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 43 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 113 | - |
| `lclsSystm1` | 관광분류체계1 | string | SH | - |
| `lclsSystm2` | 관광분류체계2 | string | SH06 | - |
| `lclsSystm3` | 관광분류체계3 | string | SH060200 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "충청북도 청주시 흥덕구 가경동", "addr2": "1438", "areacode": "33", "cat1": "A04", "cat2": "A0401", "cat3": "A04010200", "contentid": "1433504", "contenttypeid": "38", "createdtime": "20111111014944", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/50/3492550_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/50/3492550_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "127.4341171334", "mapy": "36.6286485111", "mlevel": "6", "modifiedtime": "20250521105928", "sigungucode": "10", "tel": "", "title": "가경 터미널시장", "zipcode": "28398", "showflag": "1", "lDongRegnCd": "43", "lDongSignguCd": "113", "lclsSystm1": "SH", "lclsSystm2": "SH06", "lclsSystm3": "SH060200"}
{"addr1": "전라남도 진도군 고군면 신비의바닷길 47", "addr2": "(고군면)", "areacode": "38", "cat1": "A01", "cat2": "A0101", "cat3": "A01011200", "contentid": "126273", "contenttypeid": "12", "createdtime": "20031107090000", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/36/3079736_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/36/3079736_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.3547412438", "mapy": "34.4354594945", "mlevel": "6", "modifiedtime": "20250808090412", "sigungucode": "21", "tel": "", "title": "가계해수욕장", "zipcode": "58911", "showflag": "1", "lDongRegnCd": "46", "lDongSignguCd": "900", "lclsSystm1": "NA", "lclsSystm2": "NA02", "lclsSystm3": "NA020900"}
{"addr1": "서울특별시 종로구 평창30길 28 (평창동)", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "129854", "contenttypeid": "14", "createdtime": "20071106103314", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/11/3506711_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/11/3506711_image3_1.jpg", "cpyrhtDivCd": "Type1", "mapx": "126.97512913242", "mapy": "37.6122904729365", "mlevel": "6", "modifiedtime": "20260311100340", "sigungucode": "", "tel": "", "title": "가나아트센터", "zipcode": "03004", "showflag": "1", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "VE", "lclsSystm2": "VE07", "lclsSystm3": "VE070600"}
```

**TripCraft 활용 포인트**: TripCraft 변경된 관광정보 동기화 목록 조회 기능에 활용.

---

### 3.3 `areaCode2`

**용도**: 지역코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/areaCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `name` | name | string | 서울 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"rnum": 1, "code": "1", "name": "서울"}
{"rnum": 2, "code": "2", "name": "인천"}
{"rnum": 3, "code": "3", "name": "대전"}
```

**TripCraft 활용 포인트**: TripCraft 지역코드 조회 기능에 활용.

---

### 3.4 `categoryCode2`

**용도**: 서비스분류코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/categoryCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `name` | name | string | 자연 | - |
| `rnum` | rnum | number | 1 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"code": "A01", "name": "자연", "rnum": 1}
{"code": "A02", "name": "인문(문화/예술/역사)", "rnum": 2}
{"code": "A03", "name": "레포츠", "rnum": 3}
```

**TripCraft 활용 포인트**: TripCraft 서비스분류코드 조회 기능에 활용.

---

### 3.5 `detailCommon2`

**용도**: 콘텐츠 공통정보 상세 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/detailCommon2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&serviceKey=${SERVICE_KEY}
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

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `contentid` | 콘텐츠 ID | code | 126508 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 12 | - |
| `title` | 관광지명 | string | 경복궁 | - |
| `createdtime` | 등록일시 | datetime | 20041230090000 | - |
| `modifiedtime` | 수정일시 | datetime | 20251112134824 | - |
| `tel` | 전화번호 | string |  | - |
| `telname` | 전화번호 명칭 | string |  | - |
| `homepage` | 홈페이지 | url | <a href="https://royal.khs.go.kr/ROYAL/contents/menuInfo-gbg | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/98/3487598_image2_ | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/98/3487598_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type1 | - |
| `areacode` | 지역코드 | code | 1 | - |
| `sigungucode` | 시군구코드 | code | 23 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 11 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 110 | - |
| `lclsSystm1` | 관광분류체계1 | string | HS | - |
| `lclsSystm2` | 관광분류체계2 | string | HS01 | - |
| `lclsSystm3` | 관광분류체계3 | string | HS010100 | - |
| `cat1` | 대분류 코드 | string | A02 | - |
| `cat2` | 중분류 코드 | string | A0201 | - |
| `cat3` | 소분류 코드 | string | A02010100 | - |
| `addr1` | 주소 | string | 서울특별시 종로구 사직로 161 (세종로) | - |
| `addr2` | 상세주소 | string |  | - |
| `zipcode` | 우편번호 | code | 03045 | - |
| `mapx` | 경도(WGS84) | coord | 126.9767375783 | - |
| `mapy` | 위도(WGS84) | coord | 37.5760836609 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `overview` | 개요/설명 | string | 경복궁은 1392년 조선 건국 후 1395년(태조 4)에 창건한 조선왕조 제일의 법궁이다. 경복궁은 백악산( | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"contentid": "126508", "contenttypeid": "12", "title": "경복궁", "createdtime": "20041230090000", "modifiedtime": "20251112134824", "tel": "", "telname": "", "homepage": "<a href=\"https://royal.khs.go.kr/ROYAL/contents/menuInfo-gbg.do?grpCode=gbg\" target=\"_blank\" title=\"새창 : 궁능유적본부 홈페이지로 이동\">https://royal.khs.go.kr/</a>", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/98/3487598_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/98/3487598_image3_1.jpg", "cpyrhtDivCd": "Type1", "areacode": "1", "sigungucode": "23", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "HS", "lclsSystm2": "HS01", "lclsSystm3": "HS010100", "cat1": "A02", "cat2": "A0201", "cat3": "A02010100", "addr1": "서울특별시 종로구 사직로 161 (세종로)", "addr2": "", "zipcode": "03045", "mapx": "126.9767375783", "mapy": "37.5760836609", "mlevel": "6", "overview": "경복궁은 1392년 조선 건국 후 1395년(태조 4)에 창건한 조선왕조 제일의 법궁이다. 경복궁은 백악산(북악산)을 주산으로 넓은 지형에 건물을 배치하였고 정문인 광화문 앞으로 넓은 육조거리가 펼쳐진 한양의 중심이었다. ‘경복’의 이름은 ‘새 왕조가 큰 복을 누려 번영할 것’이라는 의미가 담겨있으며, 이곳에서 세종 대에 훈민정음이 창제되어 반포되기도 하였다. 또한, 동궐(창덕궁)이나 서궐(경희궁)에 비해 위치가 북쪽에 있어 ‘북궐’이라 불리기도 했다.\n경복궁 근정전에서 즉위식을 가진 왕들을 보면 제2대 정종, 제4대 세종, 제6대 단종, 제7대 세조, 제9대 성종, 제11대 중종, 제13대 명종 등이 있다. \n경복궁은 1592년(선조 25) 임진왜란으로 소실되었는데, 그 후 복구되지 못하였다가 270여 년이 지난 1867년(고종 4)에 다시 지어졌다. 고종 대에 들어 건청궁과 태원전, 집옥재 등이 조성되었으며, 특히 건청궁 옥호루는 1895년 을미사변으로 명성황후가 시해되는 비운의 장소이기도 하다.\n1910년 경술국치 후 경복궁은 계획적으로 훼손되기 시작하여 1915년 조선물산공진회를 개최한다는 명분으로 대부분의 전각들이 철거되었고, 1926년에는 조선총독부 청사를 지어 경복궁의 경관을 훼손하였다. 이후 1990년대부터 본격적으로 경복궁 복원공사가 진행되었고, 1995년부터 1997년까지 조선총독부 청사를 철거하였으며 흥례문 일원, 침전 권역, 건청궁과 태원전, 그리고 광화문 등이 복원되어 현재에 이르고 있다.\n경복궁에는 조선시대의 대표적인 건축물인 경회루와 향원정의 연못이 원형대로 남아 있으며, 근정전의 월대와 조각상들은 당시의 조각미술을 대표한다. 현재 흥례문 밖 서편에는 국립고궁 박물관이 위치하고 있고, 경복궁 내 향원정의 동편에는 국립민속 박물관이 위치하고 있다.\n경복궁의 주요 문화재로는 사적 경복궁, 국보 경복궁 근정전, 국보 경복궁 경회루, 보물 경복궁 자경전, 보물 경복궁 자경전 십장생 굴뚝, 보물 경복궁 아미산굴뚝, 보물 경복궁 근정문 및 행각, 보물 경복궁 풍기대 등이 있다. \n\n◎ 한류의 매력을 만나는 여행 정보\n미국의 국민 TV 쇼 ‘더 투나잇 쇼 스타링 지미 팰런’에서는 ‘BTS위크’라는 이름을 붙여 닷새간 BTS 특별 방송을 진행했는데, 그중 BTS가 ‘맵 오브 더 솔 : 페르소나’ 미니앨범 수록곡 ‘소우주’와 ‘IDOL’을 부른 장소가 화제다. 그 장소는 바로 조선시대의 궁궐 중 하나인 ‘경복궁’의 경회루와 근정전이다. 보랏빛 조명에 아름답게 빛나던 경복궁에서 한국의 과거를 체험해 보길 추천한다."}
```

**TripCraft 활용 포인트**: 무장애 관광지 공통 상세정보.

---

### 3.6 `detailImage2`

**용도**: 이미지 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/detailImage2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&serviceKey=${SERVICE_KEY}
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

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `contentid` | 콘텐츠 ID | code | 126508 | - |
| `originimgurl` | originimgurl | url | http://tong.visitkorea.or.kr/cms/resource/94/3487594_image2_ | - |
| `imgname` | imgname | url | 경복궁 | - |
| `smallimageurl` | smallimageurl | url | http://tong.visitkorea.or.kr/cms/resource/94/3487594_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type1 | - |
| `serialnum` | serialnum | number | 3487594_5 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"contentid": "126508", "originimgurl": "http://tong.visitkorea.or.kr/cms/resource/94/3487594_image2_1.jpg", "imgname": "경복궁", "smallimageurl": "http://tong.visitkorea.or.kr/cms/resource/94/3487594_image3_1.jpg", "cpyrhtDivCd": "Type1", "serialnum": "3487594_5"}
{"contentid": "126508", "originimgurl": "http://tong.visitkorea.or.kr/cms/resource/95/3487595_image2_1.jpg", "imgname": "경복궁", "smallimageurl": "http://tong.visitkorea.or.kr/cms/resource/95/3487595_image3_1.jpg", "cpyrhtDivCd": "Type1", "serialnum": "3487595_1"}
{"contentid": "126508", "originimgurl": "http://tong.visitkorea.or.kr/cms/resource/97/3487597_image2_1.jpg", "imgname": "경복궁", "smallimageurl": "http://tong.visitkorea.or.kr/cms/resource/97/3487597_image3_1.jpg", "cpyrhtDivCd": "Type1", "serialnum": "3487597_3"}
```

**TripCraft 활용 포인트**: TripCraft 이미지 목록 조회 기능에 활용.

---

### 3.7 `detailInfo2`

**용도**: 반복정보(상세 추가정보) 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/detailInfo2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=142785&contentTypeId=32&serviceKey=${SERVICE_KEY}
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
https://apis.data.go.kr/B551011/KorWithService2/detailIntro2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&contentTypeId=12&serviceKey=${SERVICE_KEY}
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

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `contentid` | 콘텐츠 ID | code | 126508 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 12 | - |
| `heritage1` | heritage1 | number | 0 | - |
| `heritage2` | heritage2 | number | 0 | - |
| `heritage3` | heritage3 | number | 0 | - |
| `infocenter` | infocenter | string | 02-3700-3900 | - |
| `opendate` | opendate | datetime |  | - |
| `restdate` | restdate | datetime | 매주 화요일 <br>※ 단, 정기휴일이 공휴일 및 대체공휴일과 겹칠 경우에는 개방하며, 그 다음의 첫 번째  | - |
| `expguide` | expguide | code |  | - |
| `expagerange` | expagerange | string |  | - |
| `accomcount` | accomcount | number |  | - |
| `useseason` | useseason | string |  | - |
| `usetime` | usetime | datetime | [1월~2월/11월~12월]<br>
09:00~17:00 (입장마감 16:00)<br>
[3월~5월/9월~1 | - |
| `parking` | parking | string | 가능 (승용차 240대 / 버스 50대) | - |
| `chkbabycarriage` | chkbabycarriage | string |  | - |
| `chkpet` | chkpet | string |  | - |
| `chkcreditcard` | chkcreditcard | string |  | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"contentid": "126508", "contenttypeid": "12", "heritage1": "0", "heritage2": "0", "heritage3": "0", "infocenter": "02-3700-3900", "opendate": "", "restdate": "매주 화요일 <br>※ 단, 정기휴일이 공휴일 및 대체공휴일과 겹칠 경우에는 개방하며, 그 다음의 첫 번째 비공휴일이 정기휴일임", "expguide": "", "expagerange": "", "accomcount": "", "useseason": "", "usetime": "[1월~2월/11월~12월]<br>\n09:00~17:00 (입장마감 16:00)<br>\n[3월~5월/9월~10월]<br>\n09:00~18:00 (입장마감 17:00)<br>\n[6월~8월] 09:00~18:30 (입장마감 17:30)", "parking": "가능 (승용차 240대 / 버스 50대)", "chkbabycarriage": "", "chkpet": "", "chkcreditcard": ""}
```

**TripCraft 활용 포인트**: TripCraft 콘텐츠 소개정보 상세 조회 기능에 활용.

---

### 3.9 `detailWithTour2`

**용도**: 무장애 여행정보 상세 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/detailWithTour2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

**TripCraft 활용 포인트**: 무장애 접근성 상세정보. 엘리베이터·경사로·주차 등 접근성 정보 표시.

---

### 3.10 `lclsSystmCode2`

**용도**: 관광분류체계 코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/lclsSystmCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `name` | name | string | 숙박 | - |
| `rnum` | rnum | number | 1 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"code": "AC", "name": "숙박", "rnum": 1}
{"code": "C01", "name": "추천코스", "rnum": 2}
{"code": "EV", "name": "축제/공연/행사", "rnum": 3}
```

**TripCraft 활용 포인트**: TripCraft 관광분류체계 코드 조회 기능에 활용.

---

### 3.11 `ldongCode2`

**용도**: 법정동코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/ldongCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `name` | name | string | 서울특별시 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"rnum": 1, "code": "11", "name": "서울특별시"}
{"rnum": 2, "code": "26", "name": "부산광역시"}
{"rnum": 3, "code": "27", "name": "대구광역시"}
```

**TripCraft 활용 포인트**: TripCraft 법정동코드 조회 기능에 활용.

---

### 3.12 `locationBasedList2`

**용도**: 위치(위경도) 기반 반경 내 관광정보 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/locationBasedList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&mapX=126.9779692&mapY=37.566535&radius=2000&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 서울특별시 중구 세종대로 110 | - |
| `addr2` | 상세주소 | string | (태평로1가) | - |
| `zipcode` | 우편번호 | code | 04524 | - |
| `areacode` | 지역코드 | code | 1 | - |
| `cat1` | 대분류 코드 | string | A02 | - |
| `cat2` | 중분류 코드 | string | A0206 | - |
| `cat3` | 소분류 코드 | string | A02060900 | - |
| `contentid` | 콘텐츠 ID | code | 130183 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 14 | - |
| `createdtime` | 등록일시 | datetime | 20071106104558 | - |
| `dist` | 거리(m) | number | 36.41538270629469 | - |
| `firstimage` | 대표 이미지 URL | url |  | - |
| `firstimage2` | 썸네일 URL | url |  | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code |  | - |
| `mapx` | 경도(WGS84) | coord | 126.9783710306 | - |
| `mapy` | 위도(WGS84) | coord | 37.5665986816 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20251208091315 | - |
| `sigungucode` | 시군구코드 | code | 24 | - |
| `tel` | 전화번호 | string |  | - |
| `title` | 관광지명 | string | 서울도서관 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 11 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 140 | - |
| `lclsSystm1` | 관광분류체계1 | string | VE | - |
| `lclsSystm2` | 관광분류체계2 | string | VE09 | - |
| `lclsSystm3` | 관광분류체계3 | string | VE090300 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "서울특별시 중구 세종대로 110", "addr2": "(태평로1가)", "zipcode": "04524", "areacode": "1", "cat1": "A02", "cat2": "A0206", "cat3": "A02060900", "contentid": "130183", "contenttypeid": "14", "createdtime": "20071106104558", "dist": "36.41538270629469", "firstimage": "", "firstimage2": "", "cpyrhtDivCd": "", "mapx": "126.9783710306", "mapy": "37.5665986816", "mlevel": "6", "modifiedtime": "20251208091315", "sigungucode": "24", "tel": "", "title": "서울도서관", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "VE", "lclsSystm2": "VE09", "lclsSystm3": "VE090300"}
{"addr1": "서울특별시 중구 무교로 17-13 (무교동)", "addr2": "", "zipcode": "04520", "areacode": "1", "cat1": "A05", "cat2": "A0502", "cat3": "A05020100", "contentid": "750982", "contenttypeid": "39", "createdtime": "20090610203902", "dist": "100.23284169207301", "firstimage": "", "firstimage2": "", "cpyrhtDivCd": "", "mapx": "126.9785598824", "mapy": "37.5673041577", "mlevel": "6", "modifiedtime": "20250317173157", "sigungucode": "24", "tel": "02-776-7361", "title": "이북만두", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "FD", "lclsSystm2": "FD01", "lclsSystm3": "FD010100"}
{"addr1": "서울특별시 중구 을지로 19 (을지로1가)", "addr2": "지하1층", "zipcode": "04523", "areacode": "1", "cat1": "A05", "cat2": "A0502", "cat3": "A05020200", "contentid": "836324", "contenttypeid": "39", "createdtime": "20091028024236", "dist": "179.00932922530794", "firstimage": "", "firstimage2": "", "cpyrhtDivCd": "", "mapx": "126.9799708922", "mapy": "37.5663598490", "mlevel": "6", "modifiedtime": "20250319102800", "sigungucode": "24", "tel": "02-777-2579", "title": "라칸티나", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "FD", "lclsSystm2": "FD02", "lclsSystm3": "FD020300"}
```

**TripCraft 활용 포인트**: 무장애 여행 위치기반 검색. 접근성 필터 ON 시 휠체어·고령자 가능 시설 표시.

---

### 3.13 `searchKeyword2`

**용도**: 키워드 검색 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorWithService2/searchKeyword2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&keyword=%EA%B2%BD%EB%B3%B5%EA%B6%81&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 서울특별시 종로구 사직로 161 (세종로) | - |
| `addr2` | 상세주소 | string |  | - |
| `zipcode` | 우편번호 | code | 03045 | - |
| `areacode` | 지역코드 | code | 1 | - |
| `cat1` | 대분류 코드 | string | A02 | - |
| `cat2` | 중분류 코드 | string | A0201 | - |
| `cat3` | 소분류 코드 | string | A02010100 | - |
| `contentid` | 콘텐츠 ID | code | 126508 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 12 | - |
| `createdtime` | 등록일시 | datetime | 20041230090000 | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/98/3487598_image2_ | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/98/3487598_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type1 | - |
| `mapx` | 경도(WGS84) | coord | 126.9767375783 | - |
| `mapy` | 위도(WGS84) | coord | 37.5760836609 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20251112134824 | - |
| `sigungucode` | 시군구코드 | code | 23 | - |
| `tel` | 전화번호 | string |  | - |
| `title` | 관광지명 | string | 경복궁 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 11 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 110 | - |
| `lclsSystm1` | 관광분류체계1 | string | HS | - |
| `lclsSystm2` | 관광분류체계2 | string | HS01 | - |
| `lclsSystm3` | 관광분류체계3 | string | HS010100 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "서울특별시 종로구 사직로 161 (세종로)", "addr2": "", "zipcode": "03045", "areacode": "1", "cat1": "A02", "cat2": "A0201", "cat3": "A02010100", "contentid": "126508", "contenttypeid": "12", "createdtime": "20041230090000", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/98/3487598_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/98/3487598_image3_1.jpg", "cpyrhtDivCd": "Type1", "mapx": "126.9767375783", "mapy": "37.5760836609", "mlevel": "6", "modifiedtime": "20251112134824", "sigungucode": "23", "tel": "", "title": "경복궁", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "HS", "lclsSystm2": "HS01", "lclsSystm3": "HS010100"}
{"addr1": "경상북도 김천시 대항면 황학동길 11-8", "addr2": "", "zipcode": "39565", "areacode": "35", "cat1": "A05", "cat2": "A0502", "cat3": "A05020100", "contentid": "2629723", "contenttypeid": "39", "createdtime": "20191024004003", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/44/2630244_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/44/2630244_image2_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "128.0164320969", "mapy": "36.1148427197", "mlevel": "6", "modifiedtime": "20250918141914", "sigungucode": "6", "tel": "", "title": "[백년가게]경복궁식당", "lDongRegnCd": "47", "lDongSignguCd": "150", "lclsSystm1": "FD", "lclsSystm2": "FD01", "lclsSystm3": "FD010100"}
```

**TripCraft 활용 포인트**: TripCraft 키워드 검색 조회 기능에 활용.

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

