# 한국관광공사_관광사진 정보_GW — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/관광사진-정보/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_관광사진 정보_GW |
| 카탈로그 ID | uddi:관광사진 |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/PhotoGalleryService1` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: galContentId 기반 상세 조회. 이미지 저작권(cpyrhtDivCd) 확인 필수.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `galleryDetailList1` | `/galleryDetailList1` | 관광사진 상세 목록 조회 | galContentId | ❌ |
| `galleryList1` | `/galleryList1` | 관광사진 갤러리 목록 조회 | - | ✅ |
| `gallerySearchList1` | `/gallerySearchList1` | 관광사진 키워드 검색 조회 | - | ✅ |
| `gallerySyncDetailList1` | `/gallerySyncDetailList1` | 관광사진 동기화 상세 목록 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `galleryDetailList1`

**용도**: 관광사진 상세 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/PhotoGalleryService1/galleryDetailList1?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| galContentId | - | 필수 | string | - | - |

**응답 필드**:

> ⚠️ 수집 시 데이터 없음 (필수 파라미터 미충족 또는 결과 없음)

**응답 예시 (최대 3건 발췌)**:

> 샘플 없음

**TripCraft 활용 포인트**: TripCraft 관광사진 상세 목록 조회 기능에 활용.

---

### 3.2 `galleryList1`

**용도**: 관광사진 갤러리 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `galContentId` | 갤러리 콘텐츠 ID | code | 1002144 | - |
| `galContentTypeId` | 갤러리 콘텐츠 타입 코드 | code | 17 | - |
| `galTitle` | 갤러리 제목 | string | 청설모 | - |
| `galWebImageUrl` | 웹 이미지 URL | url | http://tong.visitkorea.or.kr/cms2/website/44/1002144.jpg | - |
| `galCreatedtime` | 등록일시 | datetime | 20100420024817 | - |
| `galModifiedtime` | 수정일시 | datetime | 20240709171727 | - |
| `galPhotographyMonth` | 촬영월 | url | 201004 | - |
| `galPhotographyLocation` | 촬영장소 | url | 서울 경복궁 | - |
| `galPhotographer` | 작가명 | url | 한국관광공사 김지호 | - |
| `galSearchKeyword` | 검색키워드 | string | 청설모, 동물 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"galContentId": "1002144", "galContentTypeId": "17", "galTitle": "청설모", "galWebImageUrl": "http://tong.visitkorea.or.kr/cms2/website/44/1002144.jpg", "galCreatedtime": "20100420024817", "galModifiedtime": "20240709171727", "galPhotographyMonth": "201004", "galPhotographyLocation": "서울 경복궁", "galPhotographer": "한국관광공사 김지호", "galSearchKeyword": "청설모, 동물"}
{"galContentId": "1002619", "galContentTypeId": "17", "galTitle": "경복궁 꽃담", "galWebImageUrl": "http://tong.visitkorea.or.kr/cms2/website/19/1002619.jpg", "galCreatedtime": "20100420222711", "galModifiedtime": "20150818233000", "galPhotographyMonth": "201004", "galPhotographyLocation": "서울", "galPhotographer": "한국관광공사 김지호", "galSearchKeyword": "경복궁 자경전 꽃담 문양, 고궁"}
{"galContentId": "1004457", "galContentTypeId": "17", "galTitle": "국립고궁박물관", "galWebImageUrl": "http://tong.visitkorea.or.kr/cms2/website/57/1004457.jpg", "galCreatedtime": "20100421150936", "galModifiedtime": "20150818154827", "galPhotographyMonth": "201004", "galPhotographyLocation": "서울 경복궁", "galPhotographer": "한국관광공사 김지호", "galSearchKeyword": "국립고궁박물관"}
```

**TripCraft 활용 포인트**: 관광지 관련 고품질 공식 사진 제공. 콘텐츠 상세 페이지 비주얼 보강.

---

### 3.3 `gallerySearchList1`

**용도**: 관광사진 키워드 검색 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&keyword=%EA%B2%BD%EB%B3%B5%EA%B6%81&serviceKey=${SERVICE_KEY}
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
| `galContentId` | 갤러리 콘텐츠 ID | code | 1002175 | - |
| `galContentTypeId` | 갤러리 콘텐츠 타입 코드 | code | 17 | - |
| `galTitle` | 갤러리 제목 | string | 경복궁 수문장 교대의식 | - |
| `galWebImageUrl` | 웹 이미지 URL | url | http://tong.visitkorea.or.kr/cms2/website/75/1002175.jpg | - |
| `galCreatedtime` | 등록일시 | datetime | 20100420030247 | - |
| `galModifiedtime` | 수정일시 | datetime | 20230422223324 | - |
| `galPhotographyMonth` | 촬영월 | url | 201004 | - |
| `galPhotographyLocation` | 촬영장소 | url | 서울특별시 종로구 | - |
| `galPhotographer` | 작가명 | url | 한국관광공사 김지호 | - |
| `galSearchKeyword` | 검색키워드 | string | 경복궁 수문장 교대의식, 서울특별시 종로구, 전통 행사, 전통 의식 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"galContentId": "1002175", "galContentTypeId": "17", "galTitle": "경복궁 수문장 교대의식", "galWebImageUrl": "http://tong.visitkorea.or.kr/cms2/website/75/1002175.jpg", "galCreatedtime": "20100420030247", "galModifiedtime": "20230422223324", "galPhotographyMonth": "201004", "galPhotographyLocation": "서울특별시 종로구", "galPhotographer": "한국관광공사 김지호", "galSearchKeyword": "경복궁 수문장 교대의식, 서울특별시 종로구, 전통 행사, 전통 의식"}
{"galContentId": "1002211", "galContentTypeId": "17", "galTitle": "국립민속박물관", "galWebImageUrl": "http://tong.visitkorea.or.kr/cms2/website/11/1002211.jpg", "galCreatedtime": "20100420181930", "galModifiedtime": "20150818232140", "galPhotographyMonth": "201004", "galPhotographyLocation": "서울", "galPhotographer": "한국관광공사 김지호", "galSearchKeyword": "경복궁, 자경전, 꽃담, 봄, 살구꽃"}
{"galContentId": "1002218", "galContentTypeId": "17", "galTitle": "국립민속박물관", "galWebImageUrl": "http://tong.visitkorea.or.kr/cms2/website/18/1002218.jpg", "galCreatedtime": "20100420182658", "galModifiedtime": "20150818232111", "galPhotographyMonth": "201004", "galPhotographyLocation": "서울", "galPhotographer": "한국관광공사 김지호", "galSearchKeyword": "경복궁, 자경전, 꽃담, 봄, 살구꽃"}
```

**TripCraft 활용 포인트**: 키워드로 관광 사진 검색. 콘텐츠 연관 이미지 발굴.

---

### 3.4 `gallerySyncDetailList1`

**용도**: 관광사진 동기화 상세 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySyncDetailList1?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `galContentId` | 갤러리 콘텐츠 ID | code |  | - |
| `galContentTypeId` | 갤러리 콘텐츠 타입 코드 | code | 17 | - |
| `galTitle` | 갤러리 제목 | string | 가리왕산 | - |
| `galWebImageUrl` | 웹 이미지 URL | url |  | - |
| `galCreatedtime` | 등록일시 | datetime | 20241231134753 | - |
| `galModifiedtime` | 수정일시 | datetime | 20260311132611 | - |
| `galPhotographyMonth` | 촬영월 | url | 202410 | - |
| `galPhotographyLocation` | 촬영장소 | url | 강원특별자치도 정선군 정선읍 | - |
| `galPhotographer` | 작가명 | url | 홍정표 | - |
| `galSearchKeyword` | 검색키워드 | string | 가리왕산, 강원특별자치도 정선군, 강원도, 케이블카, 파노라마, 10월 추천여행지, 사진기자단, 프레임코리아 | - |
| `galUseFlag` | galUseFlag | number | 1 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"galContentId": "", "galContentTypeId": "17", "galTitle": "가리왕산", "galWebImageUrl": "", "galCreatedtime": "20241231134753", "galModifiedtime": "20260311132611", "galPhotographyMonth": "202410", "galPhotographyLocation": "강원특별자치도 정선군 정선읍", "galPhotographer": "홍정표", "galSearchKeyword": "가리왕산, 강원특별자치도 정선군, 강원도, 케이블카, 파노라마, 10월 추천여행지, 사진기자단, 프레임코리아2기", "galUseFlag": "1"}
{"galContentId": "1002124", "galContentTypeId": "17", "galTitle": "청설모", "galWebImageUrl": "http://tong.visitkorea.or.kr/cms2/website/24/1002124.jpg", "galCreatedtime": "20100420023750", "galModifiedtime": "20240709172021", "galPhotographyMonth": "201004", "galPhotographyLocation": "서울 경복궁", "galPhotographer": "한국관광공사 김지호", "galSearchKeyword": "청설모, 동물", "galUseFlag": "1"}
{"galContentId": "1002129", "galContentTypeId": "17", "galTitle": "청설모", "galWebImageUrl": "http://tong.visitkorea.or.kr/cms2/website/29/1002129.jpg", "galCreatedtime": "20100420024205", "galModifiedtime": "20150818231430", "galPhotographyMonth": "201004", "galPhotographyLocation": "서울 경복궁", "galPhotographer": "한국관광공사 김지호", "galSearchKeyword": "청설모, 동물", "galUseFlag": "1"}
```

**TripCraft 활용 포인트**: 전체 갤러리 이미지 동기화. 이미지 데이터베이스 구축.

---

## 5. 코드 카탈로그

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

