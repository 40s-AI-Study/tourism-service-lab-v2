# 한국관광공사_반려동물_동반여행_서비스 — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/반려동물_동반여행_서비스/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_반려동물_동반여행_서비스 |
| 카탈로그 ID | uddi:KorPetTourService2 |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/KorPetTourService2` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: 반려동물 동반 가능 시설 전용. detailPetTour2로 동반 규정 상세 제공.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `areaBasedList2` | `/areaBasedList2` | 지역코드 기반 관광정보 목록 조회 | - | ✅ |
| `areaCode2` | `/areaCode2` | 지역코드 조회 | - | ✅ |
| `categoryCode2` | `/categoryCode2` | 서비스분류코드 조회 | - | ✅ |
| `detailCommon2` | `/detailCommon2` | 콘텐츠 공통정보 상세 조회 | contentId(콘텐츠ID) | ❌ |
| `detailImage2` | `/detailImage2` | 이미지 목록 조회 | contentId | ❌ |
| `detailInfo2` | `/detailInfo2` | 반복정보(상세 추가정보) 조회 | contentId, contentTypeId | ❌ |
| `detailIntro2` | `/detailIntro2` | 콘텐츠 소개정보 상세 조회 | contentId, contentTypeId | ❌ |
| `detailPetTour2` | `/detailPetTour2` | 반려동물 동반 여행정보 조회 | contentId, contentTypeId | ❌ |
| `lclsSystmCode2` | `/lclsSystmCode2` | 관광분류체계 코드 조회 | - | ✅ |
| `ldongCode2` | `/ldongCode2` | 법정동코드 조회 | - | ✅ |
| `locationBasedList2` | `/locationBasedList2` | 위치(위경도) 기반 반경 내 관광정보 목록 조회 | mapX(경도), mapY(위도), radius(반경m) | ✅ |
| `petTourSyncList2` | `/petTourSyncList2` | 반려동물 동반여행 동기화 목록 | - | ✅ |
| `searchKeyword2` | `/searchKeyword2` | 키워드 검색 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `areaBasedList2`

**용도**: 지역코드 기반 관광정보 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/areaBasedList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&arrange=A&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 부산광역시 부산진구 가야대로 779 (부전동) | - |
| `addr2` | 상세주소 | string |  | - |
| `areacode` | 지역코드 | code |  | - |
| `cat1` | 대분류 코드 | string |  | - |
| `cat2` | 중분류 코드 | string |  | - |
| `cat3` | 소분류 코드 | string |  | - |
| `contentid` | 콘텐츠 ID | code | 2930927 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 38 | - |
| `createdtime` | 등록일시 | datetime | 20221030154457 | - |
| `firstimage` | 대표 이미지 URL | url | https://tong.visitkorea.or.kr/cms/resource/90/4017190_image2 | - |
| `firstimage2` | 썸네일 URL | url | https://tong.visitkorea.or.kr/cms/resource/90/4017190_image3 | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 129.056805686045 | - |
| `mapy` | 위도(WGS84) | coord | 35.1579550616706 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20260316103559 | - |
| `sigungucode` | 시군구코드 | code |  | - |
| `tel` | 전화번호 | string | 051-819-1421 | - |
| `title` | 관광지명 | string | 가까운약국 | - |
| `zipcode` | 우편번호 | code | 47257 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 26 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 230 | - |
| `lclsSystm1` | 관광분류체계1 | string | SH | - |
| `lclsSystm2` | 관광분류체계2 | string | SH04 | - |
| `lclsSystm3` | 관광분류체계3 | string | SH040300 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "부산광역시 부산진구 가야대로 779 (부전동)", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "2930927", "contenttypeid": "38", "createdtime": "20221030154457", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/90/4017190_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/90/4017190_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "129.056805686045", "mapy": "35.1579550616706", "mlevel": "6", "modifiedtime": "20260316103559", "sigungucode": "", "tel": "051-819-1421", "title": "가까운약국", "zipcode": "47257", "lDongRegnCd": "26", "lDongSignguCd": "230", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
{"addr1": "서울특별시 중구 명동8가길 33 (충무로2가)", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4012773", "contenttypeid": "38", "createdtime": "20260207014737", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/09/4024409_image2_1.jpeg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/09/4024409_image3_1.jpeg", "cpyrhtDivCd": "Type3", "mapx": "126.986903352805", "mapy": "37.5619124538241", "mlevel": "", "modifiedtime": "20260318101005", "sigungucode": "", "tel": "", "title": "가나안경원 명동점", "zipcode": "04537", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
{"addr1": "서울특별시 강서구 마곡동로 166 (마곡동)", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4008808", "contenttypeid": "38", "createdtime": "20260130015059", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/70/4021070_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/70/4021070_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.836784043269", "mapy": "37.5690918473471", "mlevel": "", "modifiedtime": "20260406201517", "sigungucode": "", "tel": "", "title": "가든뷰", "zipcode": "07790", "lDongRegnCd": "11", "lDongSignguCd": "500", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
```

**TripCraft 활용 포인트**: 지역별 반려동물 동반 가능 관광지 목록.

---

### 3.2 `areaCode2`

**용도**: 지역코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/areaCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

### 3.3 `categoryCode2`

**용도**: 서비스분류코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/categoryCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

### 3.4 `detailCommon2`

**용도**: 콘텐츠 공통정보 상세 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/detailCommon2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&serviceKey=${SERVICE_KEY}
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

**TripCraft 활용 포인트**: TripCraft 콘텐츠 공통정보 상세 조회 기능에 활용.

---

### 3.5 `detailImage2`

**용도**: 이미지 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/detailImage2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&serviceKey=${SERVICE_KEY}
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

### 3.6 `detailInfo2`

**용도**: 반복정보(상세 추가정보) 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/detailInfo2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=142785&contentTypeId=32&serviceKey=${SERVICE_KEY}
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

### 3.7 `detailIntro2`

**용도**: 콘텐츠 소개정보 상세 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/detailIntro2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&contentId=126508&contentTypeId=12&serviceKey=${SERVICE_KEY}
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

### 3.8 `detailPetTour2`

**용도**: 반려동물 동반 여행정보 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/detailPetTour2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

**TripCraft 활용 포인트**: 반려동물 동반 상세 규정. 입장 조건·동반 규모 제한 표시.

---

### 3.9 `lclsSystmCode2`

**용도**: 관광분류체계 코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/lclsSystmCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

### 3.10 `ldongCode2`

**용도**: 법정동코드 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/ldongCode2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

### 3.11 `locationBasedList2`

**용도**: 위치(위경도) 기반 반경 내 관광정보 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/locationBasedList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&mapX=126.9779692&mapY=37.566535&radius=2000&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 서울특별시 중구 퇴계로 67 | - |
| `addr2` | 상세주소 | string |  | - |
| `zipcode` | 우편번호 | code | 04529 | - |
| `areacode` | 지역코드 | code | 1 | - |
| `cat1` | 대분류 코드 | string | B02 | - |
| `cat2` | 중분류 코드 | string | B0201 | - |
| `cat3` | 소분류 코드 | string | B02010100 | - |
| `contentid` | 콘텐츠 ID | code | 2586384 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 32 | - |
| `createdtime` | 등록일시 | datetime | 20190109184205 | - |
| `dist` | 거리(m) | number | 769.6406848936854 | - |
| `firstimage` | 대표 이미지 URL | url | http://tong.visitkorea.or.kr/cms/resource/20/2821120_image2_ | - |
| `firstimage2` | 썸네일 URL | url | http://tong.visitkorea.or.kr/cms/resource/20/2821120_image3_ | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 126.9795572285 | - |
| `mapy` | 위도(WGS84) | coord | 37.5597189467 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20250514093340 | - |
| `sigungucode` | 시군구코드 | code | 24 | - |
| `tel` | 전화번호 | string | 02-317-4000 | - |
| `title` | 관광지명 | string | 레스케이프 호텔(L’Escape Hotel) | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 11 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 140 | - |
| `lclsSystm1` | 관광분류체계1 | string | AC | - |
| `lclsSystm2` | 관광분류체계2 | string | AC01 | - |
| `lclsSystm3` | 관광분류체계3 | string | AC010100 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "서울특별시 중구 퇴계로 67", "addr2": "", "zipcode": "04529", "areacode": "1", "cat1": "B02", "cat2": "B0201", "cat3": "B02010100", "contentid": "2586384", "contenttypeid": "32", "createdtime": "20190109184205", "dist": "769.6406848936854", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/20/2821120_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/20/2821120_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.9795572285", "mapy": "37.5597189467", "mlevel": "6", "modifiedtime": "20250514093340", "sigungucode": "24", "tel": "02-317-4000", "title": "레스케이프 호텔(L’Escape Hotel)", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "AC", "lclsSystm2": "AC01", "lclsSystm3": "AC010100"}
{"addr1": "서울특별시 중구 명동2가", "addr2": "", "zipcode": "04536", "areacode": "1", "cat1": "A02", "cat2": "A0203", "cat3": "A02030400", "contentid": "264311", "contenttypeid": "12", "createdtime": "20021219014622", "dist": "786.1100143793194", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/96/3548996_image2_1.jpg", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/96/3548996_image3_1.jpg", "cpyrhtDivCd": "Type1", "mapx": "126.9849150050", "mapy": "37.5621520930", "mlevel": "6", "modifiedtime": "20251023143000", "sigungucode": "24", "tel": "", "title": "명동", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "EX", "lclsSystm2": "EX07", "lclsSystm3": "EX070200"}
{"addr1": "서울특별시 종로구 인사동길 62 (관훈동)", "addr2": "", "zipcode": "03146", "areacode": "1", "cat1": "A02", "cat2": "A0203", "cat3": "A02030400", "contentid": "264353", "contenttypeid": "12", "createdtime": "20021218231629", "dist": "1107.0572775665653", "firstimage": "http://tong.visitkorea.or.kr/cms/resource/03/3412103_image2_1.JPG", "firstimage2": "http://tong.visitkorea.or.kr/cms/resource/03/3412103_image3_1.JPG", "cpyrhtDivCd": "Type3", "mapx": "126.9835230884", "mapy": "37.5754616322", "mlevel": "6", "modifiedtime": "20251127162913", "sigungucode": "23", "tel": "", "title": "인사동", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "EX", "lclsSystm2": "EX07", "lclsSystm3": "EX070200"}
```

**TripCraft 활용 포인트**: 반려동물 동반 가능 시설 위치기반 검색. 펫 필터 기능.

---

### 3.12 `petTourSyncList2`

**용도**: 반려동물 동반여행 동기화 목록

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/petTourSyncList2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 부산광역시 부산진구 가야대로 779 (부전동) | - |
| `addr2` | 상세주소 | string |  | - |
| `areacode` | 지역코드 | code |  | - |
| `cat1` | 대분류 코드 | string |  | - |
| `cat2` | 중분류 코드 | string |  | - |
| `cat3` | 소분류 코드 | string |  | - |
| `contentid` | 콘텐츠 ID | code | 2930927 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 38 | - |
| `createdtime` | 등록일시 | datetime | 20221030154457 | - |
| `firstimage` | 대표 이미지 URL | url | https://tong.visitkorea.or.kr/cms/resource/90/4017190_image2 | - |
| `firstimage2` | 썸네일 URL | url | https://tong.visitkorea.or.kr/cms/resource/90/4017190_image3 | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 129.056805686045 | - |
| `mapy` | 위도(WGS84) | coord | 35.1579550616706 | - |
| `mlevel` | 지도 레벨 | number | 6 | - |
| `modifiedtime` | 수정일시 | datetime | 20260316103559 | - |
| `sigungucode` | 시군구코드 | code |  | - |
| `tel` | 전화번호 | string | 051-819-1421 | - |
| `title` | 관광지명 | string | 가까운약국 | - |
| `zipcode` | 우편번호 | code | 47257 | - |
| `showflag` | showflag | number | 1 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 26 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 230 | - |
| `lclsSystm1` | 관광분류체계1 | string | SH | - |
| `lclsSystm2` | 관광분류체계2 | string | SH04 | - |
| `lclsSystm3` | 관광분류체계3 | string | SH040300 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "부산광역시 부산진구 가야대로 779 (부전동)", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "2930927", "contenttypeid": "38", "createdtime": "20221030154457", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/90/4017190_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/90/4017190_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "129.056805686045", "mapy": "35.1579550616706", "mlevel": "6", "modifiedtime": "20260316103559", "sigungucode": "", "tel": "051-819-1421", "title": "가까운약국", "zipcode": "47257", "showflag": "1", "lDongRegnCd": "26", "lDongSignguCd": "230", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
{"addr1": "서울특별시 중구 명동8가길 33 (충무로2가)", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4012773", "contenttypeid": "38", "createdtime": "20260207014737", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/09/4024409_image2_1.jpeg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/09/4024409_image3_1.jpeg", "cpyrhtDivCd": "Type3", "mapx": "126.986903352805", "mapy": "37.5619124538241", "mlevel": "", "modifiedtime": "20260318101005", "sigungucode": "", "tel": "", "title": "가나안경원 명동점", "zipcode": "04537", "showflag": "1", "lDongRegnCd": "11", "lDongSignguCd": "140", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
{"addr1": "서울특별시 강서구 마곡동로 166 (마곡동)", "addr2": "", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4008808", "contenttypeid": "38", "createdtime": "20260130015059", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/70/4021070_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/70/4021070_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.836784043269", "mapy": "37.5690918473471", "mlevel": "", "modifiedtime": "20260406201517", "sigungucode": "", "tel": "", "title": "가든뷰", "zipcode": "07790", "showflag": "1", "lDongRegnCd": "11", "lDongSignguCd": "500", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
```

**TripCraft 활용 포인트**: TripCraft 반려동물 동반여행 동기화 목록 기능에 활용.

---

### 3.13 `searchKeyword2`

**용도**: 키워드 검색 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/KorPetTourService2/searchKeyword2?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&keyword=%EA%B2%BD%EB%B3%B5%EA%B6%81&serviceKey=${SERVICE_KEY}
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
| `addr1` | 주소 | string | 서울특별시 종로구 자하문로2길 4 (적선동) | - |
| `addr2` | 상세주소 | string |  | - |
| `zipcode` | 우편번호 | code | 03044 | - |
| `areacode` | 지역코드 | code |  | - |
| `cat1` | 대분류 코드 | string |  | - |
| `cat2` | 중분류 코드 | string |  | - |
| `cat3` | 소분류 코드 | string |  | - |
| `contentid` | 콘텐츠 ID | code | 4025882 | - |
| `contenttypeid` | 콘텐츠 타입 코드 | code | 38 | - |
| `createdtime` | 등록일시 | datetime | 20260227134741 | - |
| `firstimage` | 대표 이미지 URL | url | https://tong.visitkorea.or.kr/cms/resource/67/4029467_image2 | - |
| `firstimage2` | 썸네일 URL | url | https://tong.visitkorea.or.kr/cms/resource/67/4029467_image3 | - |
| `cpyrhtDivCd` | 저작권 구분코드 | code | Type3 | - |
| `mapx` | 경도(WGS84) | coord | 126.972859321085 | - |
| `mapy` | 위도(WGS84) | coord | 37.576377886406 | - |
| `mlevel` | 지도 레벨 | string |  | - |
| `modifiedtime` | 수정일시 | datetime | 20260319042713 | - |
| `sigungucode` | 시군구코드 | code |  | - |
| `tel` | 전화번호 | string |  | - |
| `title` | 관광지명 | string | 다이소 경복궁역점 | - |
| `lDongRegnCd` | 법정동 시도코드 | code | 11 | - |
| `lDongSignguCd` | 법정동 시군구코드 | code | 110 | - |
| `lclsSystm1` | 관광분류체계1 | string | SH | - |
| `lclsSystm2` | 관광분류체계2 | string | SH04 | - |
| `lclsSystm3` | 관광분류체계3 | string | SH040300 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"addr1": "서울특별시 종로구 자하문로2길 4 (적선동)", "addr2": "", "zipcode": "03044", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4025882", "contenttypeid": "38", "createdtime": "20260227134741", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/67/4029467_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/67/4029467_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.972859321085", "mapy": "37.576377886406", "mlevel": "", "modifiedtime": "20260319042713", "sigungucode": "", "tel": "", "title": "다이소 경복궁역점", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
{"addr1": "서울특별시 종로구 윤보선길 42 (안국동)", "addr2": "", "zipcode": "03060", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4012713", "contenttypeid": "38", "createdtime": "20260207004013", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/17/4024517_image2_1.jpg", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/17/4024517_image3_1.jpg", "cpyrhtDivCd": "Type3", "mapx": "126.983821068557", "mapy": "37.5779865507226", "mlevel": "", "modifiedtime": "20260318101005", "sigungucode": "", "tel": "", "title": "앤더슨벨 경복궁 플래그쉽 스토어", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
{"addr1": "서울특별시 종로구 자하문로 9 (체부동)", "addr2": "1,2층", "zipcode": "03041", "areacode": "", "cat1": "", "cat2": "", "cat3": "", "contentid": "4009449", "contenttypeid": "38", "createdtime": "20260130201705", "firstimage": "https://tong.visitkorea.or.kr/cms/resource/98/4028798_image2_1.png", "firstimage2": "https://tong.visitkorea.or.kr/cms/resource/98/4028798_image3_1.png", "cpyrhtDivCd": "Type3", "mapx": "126.972141061212", "mapy": "37.5769157929272", "mlevel": "", "modifiedtime": "20260309093631", "sigungucode": "", "tel": "", "title": "올리브영 경복궁역점", "lDongRegnCd": "11", "lDongSignguCd": "110", "lclsSystm1": "SH", "lclsSystm2": "SH04", "lclsSystm3": "SH040300"}
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

