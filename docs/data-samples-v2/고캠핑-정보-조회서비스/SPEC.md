# 한국관광공사_고캠핑 정보 조회서비스_GW — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/고캠핑-정보-조회서비스/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_고캠핑 정보 조회서비스_GW |
| 카탈로그 ID | uddi:고캠핑 |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/GoCamping` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: 별도 langCode 파라미터 불필요. 캠핑 특화 필드 다수.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `basedList` | `/basedList` | 캠핑장 기본 목록 조회 | - | ✅ |
| `basedSyncList` | `/basedSyncList` | 캠핑장 동기화 목록 조회 | - | ✅ |
| `imageList` | `/imageList` | 캠핑장 이미지 목록 조회 | contentId | ❌ |
| `locationBasedList` | `/locationBasedList` | 위치 기반 캠핑장 목록 조회 | mapX, mapY, radius, langDivCd(KOR) | ❌ |
| `searchList` | `/searchList` | 캠핑장 검색 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `basedList`

**용도**: 캠핑장 기본 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/GoCamping/basedList?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `contentId` | 콘텐츠 ID | code | 100128 | - |
| `facltNm` | 캠핑장명 | string | 숲속의아침 | - |
| `lineIntro` | 한줄 소개 | string |  | - |
| `intro` | 소개 | string | 영월군 무릉도원면 법흥계곡상류에 위치한 캠핑장입니다. 맑고 깨끗한 계곡물과 그림같은 산으로 둘러쌓인 아늑하고 | - |
| `allar` | 전체면적 | number | 0 | - |
| `insrncAt` | 보험가입여부 | string | Y | - |
| `trsagntNo` | 여행업등록번호 | number | 2021000004 | - |
| `bizrno` | 사업자등록번호 | string | 279-31-00949 | - |
| `facltDivNm` | 시설구분명 | string | 민간 | - |
| `mangeDivNm` | 관리구분명 | string | 직영 | - |
| `mgcDiv` | 관리자 | code | 이성민 | - |
| `manageSttus` | 운영상태 | string | 운영 | - |
| `hvofBgnde` | 휴무시작일 | string |  | - |
| `hvofEnddle` | 휴무종료일 | string |  | - |
| `featureNm` | 특징 | string | 법흥계곡 소나무 숲속 오토캠핑장  영월 법흥계곡을 끼고 있는 오토캠핑장이다. 캠핑장 주변으로 키카 큰 소나무 | - |
| `induty` | 업종 | string | 일반야영장 | - |
| `lctCl` | 입지구분 | string | 계곡 | - |
| `doNm` | 도명 | string | 강원특별자치도 | - |
| `sigunguNm` | 시군구명 | string | 영월군 | - |
| `zipcode` | 우편번호 | code | 26201 | - |
| `addr1` | 주소 | string | 강원특별자치도 영월군 무릉도원면 무릉법흥로 1115 | - |
| `addr2` | 상세주소 | string |  | - |
| `mapX` | 경도 | coord | 128.277787233221 | - |
| `mapY` | 위도 | coord | 37.3561953813393 | - |
| `direction` | direction | string |  | - |
| `tel` | 전화번호 | string | 033-372-8181 | - |
| `homepage` | 홈페이지 | url | https://blog.never.com/sungminlee9 | - |
| `resveUrl` | resveUrl | url |  | - |
| `resveCl` | resveCl | string | 온라인예약대기 | - |
| `manageNmpr` | manageNmpr | number | 1 | - |
| `gnrlSiteCo` | gnrlSiteCo | number | 14 | - |
| `autoSiteCo` | autoSiteCo | number | 0 | - |
| `glampSiteCo` | glampSiteCo | number | 0 | - |
| `caravSiteCo` | caravSiteCo | number | 0 | - |
| `indvdlCaravSiteCo` | indvdlCaravSiteCo | number | 0 | - |
| `sitedStnc` | sitedStnc | number | 0 | - |
| `siteMg1Width` | siteMg1Width | code | 0 | - |
| `siteMg2Width` | siteMg2Width | code | 0 | - |
| `siteMg3Width` | siteMg3Width | code | 0 | - |
| `siteMg1Vrticl` | siteMg1Vrticl | number | 0 | - |
| `siteMg2Vrticl` | siteMg2Vrticl | number | 0 | - |
| `siteMg3Vrticl` | siteMg3Vrticl | number | 0 | - |
| `siteMg1Co` | siteMg1Co | number | 4 | - |
| `siteMg2Co` | siteMg2Co | number | 5 | - |
| `siteMg3Co` | siteMg3Co | number | 14 | - |
| `siteBottomCl1` | siteBottomCl1 | number | 0 | - |
| `siteBottomCl2` | siteBottomCl2 | number | 14 | - |
| `siteBottomCl3` | siteBottomCl3 | number | 9 | - |
| `siteBottomCl4` | siteBottomCl4 | number | 0 | - |
| `siteBottomCl5` | siteBottomCl5 | number | 0 | - |
| `tooltip` | tooltip | string |  | - |
| `glampInnerFclty` | glampInnerFclty | string |  | - |
| `caravInnerFclty` | caravInnerFclty | string |  | - |
| `prmisnDe` | prmisnDe | string | 2021-09-03 | - |
| `operPdCl` | 운영기간구분 | string | 봄,여름,가을,겨울 | - |
| `operDeCl` | 운영요일구분 | string | 평일+주말 | - |
| `trlerAcmpnyAt` | trlerAcmpnyAt | string | Y | - |
| `caravAcmpnyAt` | caravAcmpnyAt | string | N | - |
| `toiletCo` | toiletCo | number | 3 | - |
| `swrmCo` | swrmCo | number | 6 | - |
| `wtrplCo` | wtrplCo | number | 6 | - |
| `brazierCl` | brazierCl | string | 개별 | - |
| `sbrsCl` | 부대시설구분 | string | 전기,무선인터넷,장작판매,온수,트렘폴린,운동시설 | - |
| `sbrsEtc` | 부대시설기타 | string |  | - |
| `posblFcltyCl` | 이용가능시설구분 | string | 계곡 물놀이 | - |
| `posblFcltyEtc` | posblFcltyEtc | string |  | - |
| `clturEventAt` | clturEventAt | string | N | - |
| `clturEvent` | clturEvent | string |  | - |
| `exprnProgrmAt` | exprnProgrmAt | string | N | - |
| `exprnProgrm` | exprnProgrm | string |  | - |
| `extshrCo` | extshrCo | number | 18 | - |
| `frprvtWrppCo` | frprvtWrppCo | number | 1 | - |
| `frprvtSandCo` | frprvtSandCo | number | 0 | - |
| `fireSensorCo` | fireSensorCo | number | 2 | - |
| `themaEnvrnCl` | 테마환경구분 | string | 여름물놀이,가을단풍명소 | - |
| `eqpmnLendCl` | 장비대여구분 | string | 텐트,화로대,난방기구 | - |
| `animalCmgCl` | 동물반입구분 | string | 가능 | - |
| `tourEraCl` | 관광시기구분 | string |  | - |
| `firstImageUrl` | 대표이미지 URL | url | https://gocamping.or.kr/upload/camp/100128/thumb/thumb_720_7 | - |
| `createdtime` | 등록일시 | datetime | 2021-10-07 | - |
| `modifiedtime` | 수정일시 | datetime | 2026-05-14 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"contentId": "100128", "facltNm": "숲속의아침", "lineIntro": "", "intro": "영월군 무릉도원면 법흥계곡상류에 위치한 캠핑장입니다. 맑고 깨끗한 계곡물과 그림같은 산으로 둘러쌓인 아늑하고 아름다운 힐링장소입니다. 조용하고 한적한 소나무숲속에서 진짜 &apos;쉼&apos;을 경험해 보세요", "allar": "0", "insrncAt": "Y", "trsagntNo": "2021000004", "bizrno": "279-31-00949", "facltDivNm": "민간", "mangeDivNm": "직영", "mgcDiv": "이성민", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "법흥계곡 소나무 숲속 오토캠핑장  영월 법흥계곡을 끼고 있는 오토캠핑장이다. 캠핑장 주변으로 키카 큰 소나무들이 즐비하여 충분한 그늘로 여름에도 시원하고, 캠핑장 건너편에는 법흥계곡이 있다. 여름에는 계곡에 차양막과 평상도 설치해 아이들과 물놀이 하기에도 좋다. 장기간 캠핑장 숙박 이용이 가능한 곳이고, 반려동물 동반도 가능한 곳이다.", "induty": "일반야영장", "lctCl": "계곡", "doNm": "강원특별자치도", "sigunguNm": "영월군", "zipcode": "26201", "addr1": "강원특별자치도 영월군 무릉도원면 무릉법흥로 1115", "addr2": "", "mapX": "128.277787233221", "mapY": "37.3561953813393", "direction": "", "tel": "033-372-8181", "homepage": "https://blog.never.com/sungminlee9", "resveUrl": "", "resveCl": "온라인예약대기", "manageNmpr": "1", "gnrlSiteCo": "14", "autoSiteCo": "0", "glampSiteCo": "0", "caravSiteCo": "0", "indvdlCaravSiteCo": "0", "sitedStnc": "0", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "4", "siteMg2Co": "5", "siteMg3Co": "14", "siteBottomCl1": "0", "siteBottomCl2": "14", "siteBottomCl3": "9", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "", "prmisnDe": "2021-09-03", "operPdCl": "봄,여름,가을,겨울", "operDeCl": "평일+주말", "trlerAcmpnyAt": "Y", "caravAcmpnyAt": "N", "toiletCo": "3", "swrmCo": "6", "wtrplCo": "6", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,트렘폴린,운동시설", "sbrsEtc": "", "posblFcltyCl": "계곡 물놀이", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "18", "frprvtWrppCo": "1", "frprvtSandCo": "0", "fireSensorCo": "2", "themaEnvrnCl": "여름물놀이,가을단풍명소", "eqpmnLendCl": "텐트,화로대,난방기구", "animalCmgCl": "가능", "tourEraCl": "", "firstImageUrl": "https://gocamping.or.kr/upload/camp/100128/thumb/thumb_720_77829z8O4r3LyRc3JjFUN2w8.jpg", "createdtime": "2021-10-07", "modifiedtime": "2026-05-14"}
{"contentId": "100177", "facltNm": "양양 고인돌 캠핑장", "lineIntro": "청정한 남대천 계곡에서 즐기는 힐링 감성 캠핑 공간", "intro": "양양 고인돌 캠핑장은 연어가 회귀하는 청정한 남대천계곡에서 시원한 물놀이를 즐길 수 있으며,  캠핑장 주변이 조용하고 맑으며 깨끗해 힐링과 감성, 캠핑의 낭만을 즐길 수 있는 곳입니다.", "allar": "8330", "insrncAt": "Y", "trsagntNo": "2016000001", "bizrno": "227-02-42860", "facltDivNm": "민간", "mangeDivNm": "직영", "mgcDiv": "이영희", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "남대천 물놀이와 별 보기 좋은  낭만적인 감성 캠핑장  청정지역인 강원도 양양의 남대천 상류, 고인돌 유적이 있는 범부리에 있다. &apos;사슴머리&apos;라는 이름을 갖고 있는 아늑한 뒷산이 캠핑장을 감싸고 있고, 앞에는 맑고 깨끗한 남대천 계곡이 흘러 사계절 모두 좋은 캠핑장이다. 연어가 돌아오는 남대천에서 시원한 물놀이를 즐기며, 숲의 고요함과 편안함을 만끽할 수 있는 곳이다. 파쇄석과 데크로 이루어진 캠핑존, 차박존과 방갈로 등 다양한 스타일의 캠핑을 즐길 수 있다. ", "induty": "자동차야영장", "lctCl": "계곡", "doNm": "강원특별자치도", "sigunguNm": "양양군", "zipcode": "25036", "addr1": "강원특별자치도 양양군 서면 고인돌길 200-49", "addr2": "", "mapX": "128.574197764713", "mapY": "38.0539374809579", "direction": "양양 고인돌캠핑장 서울양양고속도로의 양양IC를 빠져나와, &lt;범부리&gt; 도로표지판을 따라 나온다. &lt;서면교회&gt;를 지나 &lt;범부리고인돌&gt;방향 &lt;고인돌길&gt;의 마지막 끝까지 오면 양양 고인돌 캠핑장에 도착할 수 있다.  ", "tel": "010-5363-2632", "homepage": "https://naver.me/xSFTorgA", "resveUrl": "https://m.thankqcamping.com/resv/view.hbb?cseq=2285", "resveCl": "온라인실시간예약", "manageNmpr": "1", "gnrlSiteCo": "0", "autoSiteCo": "43", "glampSiteCo": "0", "caravSiteCo": "0", "indvdlCaravSiteCo": "0", "sitedStnc": "0", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "20", "siteMg2Co": "10", "siteMg3Co": "10", "siteBottomCl1": "0", "siteBottomCl2": "21", "siteBottomCl3": "22", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "", "prmisnDe": "2016-01-12", "operPdCl": "봄,여름,가을", "operDeCl": "평일+주말", "trlerAcmpnyAt": "Y", "caravAcmpnyAt": "N", "toiletCo": "0", "swrmCo": "0", "wtrplCo": "0", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,운동시설", "sbrsEtc": "", "posblFcltyCl": "계곡 물놀이", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "0", "frprvtWrppCo": "0", "frprvtSandCo": "0", "fireSensorCo": "0", "themaEnvrnCl": "", "eqpmnLendCl": "텐트,릴선,화로대", "animalCmgCl": "불가능", "tourEraCl": "", "firstImageUrl": "https://gocamping.or.kr/upload/camp/100177/thumb/thumb_720_4765KHt95RHJsGX6CPmZWqD5.jpg", "createdtime": "2021-11-22", "modifiedtime": "2026-05-14"}
{"contentId": "100863", "facltNm": "가곡 국민여가캠핑장", "lineIntro": "", "intro": "", "allar": "4208", "insrncAt": "N", "trsagntNo": "2023000001", "bizrno": "817-87-03804", "facltDivNm": "공립", "mangeDivNm": "위탁", "mgcDiv": "가곡온천마을협동조합", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "", "induty": "자동차야영장", "lctCl": "계곡", "doNm": "강원특별자치도", "sigunguNm": "삼척시", "zipcode": "25954", "addr1": "강원특별자치도 삼척시 가곡면 가곡천로 1512", "addr2": "", "mapX": "129.208437758367", "mapY": "37.1523654454082", "direction": "", "tel": "033-574-1700", "homepage": "", "resveUrl": "", "resveCl": "온라인실시간예약", "manageNmpr": "1", "gnrlSiteCo": "0", "autoSiteCo": "0", "glampSiteCo": "0", "caravSiteCo": "15", "indvdlCaravSiteCo": "0", "sitedStnc": "3", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "0", "siteMg2Co": "0", "siteMg3Co": "0", "siteBottomCl1": "0", "siteBottomCl2": "0", "siteBottomCl3": "0", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "침대,TV,에어컨,냉장고,유무선인터넷,난방기구,취사도구", "prmisnDe": "2023-04-05", "operPdCl": "봄,여름,가을,겨울", "operDeCl": "평일+주말", "trlerAcmpnyAt": "N", "caravAcmpnyAt": "N", "toiletCo": "0", "swrmCo": "0", "wtrplCo": "0", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,산책로", "sbrsEtc": "", "posblFcltyCl": "계곡 물놀이,산책로,농어촌체험시설", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "0", "frprvtWrppCo": "0", "frprvtSandCo": "0", "fireSensorCo": "0", "themaEnvrnCl": "여름물놀이,걷기길", "eqpmnLendCl": "", "animalCmgCl": "불가능", "tourEraCl": "봄,여름,가을,겨울", "firstImageUrl": "https://gocamping.or.kr/upload/camp/100863/thumb/thumb_720_7468zHO9t19x0oxqozJocytR.jpg", "createdtime": "2023-05-02", "modifiedtime": "2026-05-14"}
```

**TripCraft 활용 포인트**: 전국 캠핑장 목록 페이지. 캠핑 테마 여행 코스 생성에 활용.

---

### 3.2 `basedSyncList`

**용도**: 캠핑장 동기화 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/GoCamping/basedSyncList?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| `contentId` | 콘텐츠 ID | code | 100128 | - |
| `facltNm` | 캠핑장명 | string | 숲속의아침 | - |
| `lineIntro` | 한줄 소개 | string |  | - |
| `intro` | 소개 | string | 영월군 무릉도원면 법흥계곡상류에 위치한 캠핑장입니다. 맑고 깨끗한 계곡물과 그림같은 산으로 둘러쌓인 아늑하고 | - |
| `allar` | 전체면적 | number | 0 | - |
| `insrncAt` | 보험가입여부 | string | Y | - |
| `trsagntNo` | 여행업등록번호 | number | 2021000004 | - |
| `bizrno` | 사업자등록번호 | string | 279-31-00949 | - |
| `facltDivNm` | 시설구분명 | string | 민간 | - |
| `mangeDivNm` | 관리구분명 | string | 직영 | - |
| `mgcDiv` | 관리자 | code | 이성민 | - |
| `manageSttus` | 운영상태 | string | 운영 | - |
| `hvofBgnde` | 휴무시작일 | string |  | - |
| `hvofEnddle` | 휴무종료일 | string |  | - |
| `featureNm` | 특징 | string | 법흥계곡 소나무 숲속 오토캠핑장  영월 법흥계곡을 끼고 있는 오토캠핑장이다. 캠핑장 주변으로 키카 큰 소나무 | - |
| `induty` | 업종 | string | 일반야영장 | - |
| `lctCl` | 입지구분 | string | 계곡 | - |
| `doNm` | 도명 | string | 강원특별자치도 | - |
| `sigunguNm` | 시군구명 | string | 영월군 | - |
| `zipcode` | 우편번호 | code | 26201 | - |
| `addr1` | 주소 | string | 강원특별자치도 영월군 무릉도원면 무릉법흥로 1115 | - |
| `addr2` | 상세주소 | string |  | - |
| `mapX` | 경도 | coord | 128.277787233221 | - |
| `mapY` | 위도 | coord | 37.3561953813393 | - |
| `direction` | direction | string |  | - |
| `tel` | 전화번호 | string | 033-372-8181 | - |
| `homepage` | 홈페이지 | url | https://blog.never.com/sungminlee9 | - |
| `resveUrl` | resveUrl | url |  | - |
| `resveCl` | resveCl | string | 온라인예약대기 | - |
| `manageNmpr` | manageNmpr | number | 1 | - |
| `gnrlSiteCo` | gnrlSiteCo | number | 14 | - |
| `autoSiteCo` | autoSiteCo | number | 0 | - |
| `glampSiteCo` | glampSiteCo | number | 0 | - |
| `caravSiteCo` | caravSiteCo | number | 0 | - |
| `indvdlCaravSiteCo` | indvdlCaravSiteCo | number | 0 | - |
| `sitedStnc` | sitedStnc | number | 0 | - |
| `siteMg1Width` | siteMg1Width | code | 0 | - |
| `siteMg2Width` | siteMg2Width | code | 0 | - |
| `siteMg3Width` | siteMg3Width | code | 0 | - |
| `siteMg1Vrticl` | siteMg1Vrticl | number | 0 | - |
| `siteMg2Vrticl` | siteMg2Vrticl | number | 0 | - |
| `siteMg3Vrticl` | siteMg3Vrticl | number | 0 | - |
| `siteMg1Co` | siteMg1Co | number | 4 | - |
| `siteMg2Co` | siteMg2Co | number | 5 | - |
| `siteMg3Co` | siteMg3Co | number | 14 | - |
| `siteBottomCl1` | siteBottomCl1 | number | 0 | - |
| `siteBottomCl2` | siteBottomCl2 | number | 14 | - |
| `siteBottomCl3` | siteBottomCl3 | number | 9 | - |
| `siteBottomCl4` | siteBottomCl4 | number | 0 | - |
| `siteBottomCl5` | siteBottomCl5 | number | 0 | - |
| `tooltip` | tooltip | string |  | - |
| `glampInnerFclty` | glampInnerFclty | string |  | - |
| `caravInnerFclty` | caravInnerFclty | string |  | - |
| `prmisnDe` | prmisnDe | string | 2021-09-03 | - |
| `operPdCl` | 운영기간구분 | string | 봄,여름,가을,겨울 | - |
| `operDeCl` | 운영요일구분 | string | 평일+주말 | - |
| `trlerAcmpnyAt` | trlerAcmpnyAt | string | Y | - |
| `caravAcmpnyAt` | caravAcmpnyAt | string | N | - |
| `toiletCo` | toiletCo | number | 3 | - |
| `swrmCo` | swrmCo | number | 6 | - |
| `wtrplCo` | wtrplCo | number | 6 | - |
| `brazierCl` | brazierCl | string | 개별 | - |
| `sbrsCl` | 부대시설구분 | string | 전기,무선인터넷,장작판매,온수,트렘폴린,운동시설 | - |
| `sbrsEtc` | 부대시설기타 | string |  | - |
| `posblFcltyCl` | 이용가능시설구분 | string | 계곡 물놀이 | - |
| `posblFcltyEtc` | posblFcltyEtc | string |  | - |
| `clturEventAt` | clturEventAt | string | N | - |
| `clturEvent` | clturEvent | string |  | - |
| `exprnProgrmAt` | exprnProgrmAt | string | N | - |
| `exprnProgrm` | exprnProgrm | string |  | - |
| `extshrCo` | extshrCo | number | 18 | - |
| `frprvtWrppCo` | frprvtWrppCo | number | 1 | - |
| `frprvtSandCo` | frprvtSandCo | number | 0 | - |
| `fireSensorCo` | fireSensorCo | number | 2 | - |
| `themaEnvrnCl` | 테마환경구분 | string | 여름물놀이,가을단풍명소 | - |
| `eqpmnLendCl` | 장비대여구분 | string | 텐트,화로대,난방기구 | - |
| `animalCmgCl` | 동물반입구분 | string | 가능 | - |
| `tourEraCl` | 관광시기구분 | string |  | - |
| `firstImageUrl` | 대표이미지 URL | url | https://gocamping.or.kr/upload/camp/100128/thumb/thumb_720_7 | - |
| `createdtime` | 등록일시 | datetime | 2021-10-07 | - |
| `modifiedtime` | 수정일시 | datetime | 2026-05-14 | - |
| `syncStatus` | syncStatus | string | U | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"contentId": "100128", "facltNm": "숲속의아침", "lineIntro": "", "intro": "영월군 무릉도원면 법흥계곡상류에 위치한 캠핑장입니다. 맑고 깨끗한 계곡물과 그림같은 산으로 둘러쌓인 아늑하고 아름다운 힐링장소입니다. 조용하고 한적한 소나무숲속에서 진짜 &apos;쉼&apos;을 경험해 보세요", "allar": "0", "insrncAt": "Y", "trsagntNo": "2021000004", "bizrno": "279-31-00949", "facltDivNm": "민간", "mangeDivNm": "직영", "mgcDiv": "이성민", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "법흥계곡 소나무 숲속 오토캠핑장  영월 법흥계곡을 끼고 있는 오토캠핑장이다. 캠핑장 주변으로 키카 큰 소나무들이 즐비하여 충분한 그늘로 여름에도 시원하고, 캠핑장 건너편에는 법흥계곡이 있다. 여름에는 계곡에 차양막과 평상도 설치해 아이들과 물놀이 하기에도 좋다. 장기간 캠핑장 숙박 이용이 가능한 곳이고, 반려동물 동반도 가능한 곳이다.", "induty": "일반야영장", "lctCl": "계곡", "doNm": "강원특별자치도", "sigunguNm": "영월군", "zipcode": "26201", "addr1": "강원특별자치도 영월군 무릉도원면 무릉법흥로 1115", "addr2": "", "mapX": "128.277787233221", "mapY": "37.3561953813393", "direction": "", "tel": "033-372-8181", "homepage": "https://blog.never.com/sungminlee9", "resveUrl": "", "resveCl": "온라인예약대기", "manageNmpr": "1", "gnrlSiteCo": "14", "autoSiteCo": "0", "glampSiteCo": "0", "caravSiteCo": "0", "indvdlCaravSiteCo": "0", "sitedStnc": "0", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "4", "siteMg2Co": "5", "siteMg3Co": "14", "siteBottomCl1": "0", "siteBottomCl2": "14", "siteBottomCl3": "9", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "", "prmisnDe": "2021-09-03", "operPdCl": "봄,여름,가을,겨울", "operDeCl": "평일+주말", "trlerAcmpnyAt": "Y", "caravAcmpnyAt": "N", "toiletCo": "3", "swrmCo": "6", "wtrplCo": "6", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,트렘폴린,운동시설", "sbrsEtc": "", "posblFcltyCl": "계곡 물놀이", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "18", "frprvtWrppCo": "1", "frprvtSandCo": "0", "fireSensorCo": "2", "themaEnvrnCl": "여름물놀이,가을단풍명소", "eqpmnLendCl": "텐트,화로대,난방기구", "animalCmgCl": "가능", "tourEraCl": "", "firstImageUrl": "https://gocamping.or.kr/upload/camp/100128/thumb/thumb_720_77829z8O4r3LyRc3JjFUN2w8.jpg", "createdtime": "2021-10-07", "modifiedtime": "2026-05-14", "syncStatus": "U"}
{"contentId": "100177", "facltNm": "양양 고인돌 캠핑장", "lineIntro": "청정한 남대천 계곡에서 즐기는 힐링 감성 캠핑 공간", "intro": "양양 고인돌 캠핑장은 연어가 회귀하는 청정한 남대천계곡에서 시원한 물놀이를 즐길 수 있으며,  캠핑장 주변이 조용하고 맑으며 깨끗해 힐링과 감성, 캠핑의 낭만을 즐길 수 있는 곳입니다.", "allar": "8330", "insrncAt": "Y", "trsagntNo": "2016000001", "bizrno": "227-02-42860", "facltDivNm": "민간", "mangeDivNm": "직영", "mgcDiv": "이영희", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "남대천 물놀이와 별 보기 좋은  낭만적인 감성 캠핑장  청정지역인 강원도 양양의 남대천 상류, 고인돌 유적이 있는 범부리에 있다. &apos;사슴머리&apos;라는 이름을 갖고 있는 아늑한 뒷산이 캠핑장을 감싸고 있고, 앞에는 맑고 깨끗한 남대천 계곡이 흘러 사계절 모두 좋은 캠핑장이다. 연어가 돌아오는 남대천에서 시원한 물놀이를 즐기며, 숲의 고요함과 편안함을 만끽할 수 있는 곳이다. 파쇄석과 데크로 이루어진 캠핑존, 차박존과 방갈로 등 다양한 스타일의 캠핑을 즐길 수 있다. ", "induty": "자동차야영장", "lctCl": "계곡", "doNm": "강원특별자치도", "sigunguNm": "양양군", "zipcode": "25036", "addr1": "강원특별자치도 양양군 서면 고인돌길 200-49", "addr2": "", "mapX": "128.574197764713", "mapY": "38.0539374809579", "direction": "양양 고인돌캠핑장 서울양양고속도로의 양양IC를 빠져나와, &lt;범부리&gt; 도로표지판을 따라 나온다. &lt;서면교회&gt;를 지나 &lt;범부리고인돌&gt;방향 &lt;고인돌길&gt;의 마지막 끝까지 오면 양양 고인돌 캠핑장에 도착할 수 있다.  ", "tel": "010-5363-2632", "homepage": "https://naver.me/xSFTorgA", "resveUrl": "https://m.thankqcamping.com/resv/view.hbb?cseq=2285", "resveCl": "온라인실시간예약", "manageNmpr": "1", "gnrlSiteCo": "0", "autoSiteCo": "43", "glampSiteCo": "0", "caravSiteCo": "0", "indvdlCaravSiteCo": "0", "sitedStnc": "0", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "20", "siteMg2Co": "10", "siteMg3Co": "10", "siteBottomCl1": "0", "siteBottomCl2": "21", "siteBottomCl3": "22", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "", "prmisnDe": "2016-01-12", "operPdCl": "봄,여름,가을", "operDeCl": "평일+주말", "trlerAcmpnyAt": "Y", "caravAcmpnyAt": "N", "toiletCo": "0", "swrmCo": "0", "wtrplCo": "0", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,운동시설", "sbrsEtc": "", "posblFcltyCl": "계곡 물놀이", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "0", "frprvtWrppCo": "0", "frprvtSandCo": "0", "fireSensorCo": "0", "themaEnvrnCl": "", "eqpmnLendCl": "텐트,릴선,화로대", "animalCmgCl": "불가능", "tourEraCl": "", "firstImageUrl": "https://gocamping.or.kr/upload/camp/100177/thumb/thumb_720_4765KHt95RHJsGX6CPmZWqD5.jpg", "createdtime": "2021-11-22", "modifiedtime": "2026-05-14", "syncStatus": "U"}
{"contentId": "100863", "facltNm": "가곡 국민여가캠핑장", "lineIntro": "", "intro": "", "allar": "4208", "insrncAt": "N", "trsagntNo": "2023000001", "bizrno": "817-87-03804", "facltDivNm": "공립", "mangeDivNm": "위탁", "mgcDiv": "가곡온천마을협동조합", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "", "induty": "자동차야영장", "lctCl": "계곡", "doNm": "강원특별자치도", "sigunguNm": "삼척시", "zipcode": "25954", "addr1": "강원특별자치도 삼척시 가곡면 가곡천로 1512", "addr2": "", "mapX": "129.208437758367", "mapY": "37.1523654454082", "direction": "", "tel": "033-574-1700", "homepage": "", "resveUrl": "", "resveCl": "온라인실시간예약", "manageNmpr": "1", "gnrlSiteCo": "0", "autoSiteCo": "0", "glampSiteCo": "0", "caravSiteCo": "15", "indvdlCaravSiteCo": "0", "sitedStnc": "3", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "0", "siteMg2Co": "0", "siteMg3Co": "0", "siteBottomCl1": "0", "siteBottomCl2": "0", "siteBottomCl3": "0", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "침대,TV,에어컨,냉장고,유무선인터넷,난방기구,취사도구", "prmisnDe": "2023-04-05", "operPdCl": "봄,여름,가을,겨울", "operDeCl": "평일+주말", "trlerAcmpnyAt": "N", "caravAcmpnyAt": "N", "toiletCo": "0", "swrmCo": "0", "wtrplCo": "0", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,산책로", "sbrsEtc": "", "posblFcltyCl": "계곡 물놀이,산책로,농어촌체험시설", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "0", "frprvtWrppCo": "0", "frprvtSandCo": "0", "fireSensorCo": "0", "themaEnvrnCl": "여름물놀이,걷기길", "eqpmnLendCl": "", "animalCmgCl": "불가능", "tourEraCl": "봄,여름,가을,겨울", "firstImageUrl": "https://gocamping.or.kr/upload/camp/100863/thumb/thumb_720_7468zHO9t19x0oxqozJocytR.jpg", "createdtime": "2023-05-02", "modifiedtime": "2026-05-14", "syncStatus": "U"}
```

**TripCraft 활용 포인트**: 캠핑장 데이터 주기적 동기화. 신규/변경 캠핑장 로컬 DB 갱신.

---

### 3.3 `imageList`

**용도**: 캠핑장 이미지 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/GoCamping/imageList?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

**TripCraft 활용 포인트**: TripCraft 캠핑장 이미지 목록 조회 기능에 활용.

---

### 3.4 `locationBasedList`

**용도**: 위치 기반 캠핑장 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/GoCamping/locationBasedList?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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
| mapX | - | 필수 | string | - | - |
| mapY | - | 필수 | string | - | - |
| radius | - | 필수 | string | - | - |
| langDivCd | - | 필수 | string | - | KOR |

**응답 필드**:

> ⚠️ 수집 시 데이터 없음 (필수 파라미터 미충족 또는 결과 없음)

**응답 예시 (최대 3건 발췌)**:

> 샘플 없음

**TripCraft 활용 포인트**: TripCraft 위치 기반 캠핑장 목록 조회 기능에 활용.

---

### 3.5 `searchList`

**용도**: 캠핑장 검색 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/GoCamping/searchList?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&keyword=%EC%BA%A0%ED%95%91&serviceKey=${SERVICE_KEY}
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
| `contentId` | 콘텐츠 ID | code | 100177 | - |
| `facltNm` | 캠핑장명 | string | 양양 고인돌 캠핑장 | - |
| `lineIntro` | 한줄 소개 | string | 청정한 남대천 계곡에서 즐기는 힐링 감성 캠핑 공간 | - |
| `intro` | 소개 | string | 양양 고인돌 캠핑장은 연어가 회귀하는 청정한 남대천계곡에서 시원한 물놀이를 즐길 수 있으며,  캠핑장 주변이 | - |
| `allar` | 전체면적 | number | 8330 | - |
| `insrncAt` | 보험가입여부 | string | Y | - |
| `trsagntNo` | 여행업등록번호 | number | 2016000001 | - |
| `bizrno` | 사업자등록번호 | string | 227-02-42860 | - |
| `facltDivNm` | 시설구분명 | string | 민간 | - |
| `mangeDivNm` | 관리구분명 | string | 직영 | - |
| `mgcDiv` | 관리자 | code | 이영희 | - |
| `manageSttus` | 운영상태 | string | 운영 | - |
| `hvofBgnde` | 휴무시작일 | string |  | - |
| `hvofEnddle` | 휴무종료일 | string |  | - |
| `featureNm` | 특징 | string | 남대천 물놀이와 별 보기 좋은  낭만적인 감성 캠핑장  청정지역인 강원도 양양의 남대천 상류, 고인돌 유적이 | - |
| `induty` | 업종 | string | 자동차야영장 | - |
| `lctCl` | 입지구분 | string | 계곡 | - |
| `doNm` | 도명 | string | 강원특별자치도 | - |
| `sigunguNm` | 시군구명 | string | 양양군 | - |
| `zipcode` | 우편번호 | code | 25036 | - |
| `addr1` | 주소 | string | 강원특별자치도 양양군 서면 고인돌길 200-49 | - |
| `addr2` | 상세주소 | string |  | - |
| `mapX` | 경도 | coord | 128.574197764713 | - |
| `mapY` | 위도 | coord | 38.0539374809579 | - |
| `direction` | direction | string | 양양 고인돌캠핑장 서울양양고속도로의 양양IC를 빠져나와, &lt;범부리&gt; 도로표지판을 따라 나온다. & | - |
| `tel` | 전화번호 | string | 010-5363-2632 | - |
| `homepage` | 홈페이지 | url | https://naver.me/xSFTorgA | - |
| `resveUrl` | resveUrl | url | https://m.thankqcamping.com/resv/view.hbb?cseq=2285 | - |
| `resveCl` | resveCl | string | 온라인실시간예약 | - |
| `manageNmpr` | manageNmpr | number | 1 | - |
| `gnrlSiteCo` | gnrlSiteCo | number | 0 | - |
| `autoSiteCo` | autoSiteCo | number | 43 | - |
| `glampSiteCo` | glampSiteCo | number | 0 | - |
| `caravSiteCo` | caravSiteCo | number | 0 | - |
| `indvdlCaravSiteCo` | indvdlCaravSiteCo | number | 0 | - |
| `sitedStnc` | sitedStnc | number | 0 | - |
| `siteMg1Width` | siteMg1Width | code | 0 | - |
| `siteMg2Width` | siteMg2Width | code | 0 | - |
| `siteMg3Width` | siteMg3Width | code | 0 | - |
| `siteMg1Vrticl` | siteMg1Vrticl | number | 0 | - |
| `siteMg2Vrticl` | siteMg2Vrticl | number | 0 | - |
| `siteMg3Vrticl` | siteMg3Vrticl | number | 0 | - |
| `siteMg1Co` | siteMg1Co | number | 20 | - |
| `siteMg2Co` | siteMg2Co | number | 10 | - |
| `siteMg3Co` | siteMg3Co | number | 10 | - |
| `siteBottomCl1` | siteBottomCl1 | number | 0 | - |
| `siteBottomCl2` | siteBottomCl2 | number | 21 | - |
| `siteBottomCl3` | siteBottomCl3 | number | 22 | - |
| `siteBottomCl4` | siteBottomCl4 | number | 0 | - |
| `siteBottomCl5` | siteBottomCl5 | number | 0 | - |
| `tooltip` | tooltip | string |  | - |
| `glampInnerFclty` | glampInnerFclty | string |  | - |
| `caravInnerFclty` | caravInnerFclty | string |  | - |
| `prmisnDe` | prmisnDe | string | 2016-01-12 | - |
| `operPdCl` | 운영기간구분 | string | 봄,여름,가을 | - |
| `operDeCl` | 운영요일구분 | string | 평일+주말 | - |
| `trlerAcmpnyAt` | trlerAcmpnyAt | string | Y | - |
| `caravAcmpnyAt` | caravAcmpnyAt | string | N | - |
| `toiletCo` | toiletCo | number | 0 | - |
| `swrmCo` | swrmCo | number | 0 | - |
| `wtrplCo` | wtrplCo | number | 0 | - |
| `brazierCl` | brazierCl | string | 개별 | - |
| `sbrsCl` | 부대시설구분 | string | 전기,무선인터넷,장작판매,온수,운동시설 | - |
| `sbrsEtc` | 부대시설기타 | string |  | - |
| `posblFcltyCl` | 이용가능시설구분 | string | 계곡 물놀이 | - |
| `posblFcltyEtc` | posblFcltyEtc | string |  | - |
| `clturEventAt` | clturEventAt | string | N | - |
| `clturEvent` | clturEvent | string |  | - |
| `exprnProgrmAt` | exprnProgrmAt | string | N | - |
| `exprnProgrm` | exprnProgrm | string |  | - |
| `extshrCo` | extshrCo | number | 0 | - |
| `frprvtWrppCo` | frprvtWrppCo | number | 0 | - |
| `frprvtSandCo` | frprvtSandCo | number | 0 | - |
| `fireSensorCo` | fireSensorCo | number | 0 | - |
| `themaEnvrnCl` | 테마환경구분 | string |  | - |
| `eqpmnLendCl` | 장비대여구분 | string | 텐트,릴선,화로대 | - |
| `animalCmgCl` | 동물반입구분 | string | 불가능 | - |
| `tourEraCl` | 관광시기구분 | string |  | - |
| `firstImageUrl` | 대표이미지 URL | url | https://gocamping.or.kr/upload/camp/100177/thumb/thumb_720_4 | - |
| `createdtime` | 등록일시 | datetime | 2021-11-22 | - |
| `modifiedtime` | 수정일시 | datetime | 2026-05-14 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"contentId": "100177", "facltNm": "양양 고인돌 캠핑장", "lineIntro": "청정한 남대천 계곡에서 즐기는 힐링 감성 캠핑 공간", "intro": "양양 고인돌 캠핑장은 연어가 회귀하는 청정한 남대천계곡에서 시원한 물놀이를 즐길 수 있으며,  캠핑장 주변이 조용하고 맑으며 깨끗해 힐링과 감성, 캠핑의 낭만을 즐길 수 있는 곳입니다.", "allar": "8330", "insrncAt": "Y", "trsagntNo": "2016000001", "bizrno": "227-02-42860", "facltDivNm": "민간", "mangeDivNm": "직영", "mgcDiv": "이영희", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "남대천 물놀이와 별 보기 좋은  낭만적인 감성 캠핑장  청정지역인 강원도 양양의 남대천 상류, 고인돌 유적이 있는 범부리에 있다. &apos;사슴머리&apos;라는 이름을 갖고 있는 아늑한 뒷산이 캠핑장을 감싸고 있고, 앞에는 맑고 깨끗한 남대천 계곡이 흘러 사계절 모두 좋은 캠핑장이다. 연어가 돌아오는 남대천에서 시원한 물놀이를 즐기며, 숲의 고요함과 편안함을 만끽할 수 있는 곳이다. 파쇄석과 데크로 이루어진 캠핑존, 차박존과 방갈로 등 다양한 스타일의 캠핑을 즐길 수 있다. ", "induty": "자동차야영장", "lctCl": "계곡", "doNm": "강원특별자치도", "sigunguNm": "양양군", "zipcode": "25036", "addr1": "강원특별자치도 양양군 서면 고인돌길 200-49", "addr2": "", "mapX": "128.574197764713", "mapY": "38.0539374809579", "direction": "양양 고인돌캠핑장 서울양양고속도로의 양양IC를 빠져나와, &lt;범부리&gt; 도로표지판을 따라 나온다. &lt;서면교회&gt;를 지나 &lt;범부리고인돌&gt;방향 &lt;고인돌길&gt;의 마지막 끝까지 오면 양양 고인돌 캠핑장에 도착할 수 있다.  ", "tel": "010-5363-2632", "homepage": "https://naver.me/xSFTorgA", "resveUrl": "https://m.thankqcamping.com/resv/view.hbb?cseq=2285", "resveCl": "온라인실시간예약", "manageNmpr": "1", "gnrlSiteCo": "0", "autoSiteCo": "43", "glampSiteCo": "0", "caravSiteCo": "0", "indvdlCaravSiteCo": "0", "sitedStnc": "0", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "20", "siteMg2Co": "10", "siteMg3Co": "10", "siteBottomCl1": "0", "siteBottomCl2": "21", "siteBottomCl3": "22", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "", "prmisnDe": "2016-01-12", "operPdCl": "봄,여름,가을", "operDeCl": "평일+주말", "trlerAcmpnyAt": "Y", "caravAcmpnyAt": "N", "toiletCo": "0", "swrmCo": "0", "wtrplCo": "0", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,운동시설", "sbrsEtc": "", "posblFcltyCl": "계곡 물놀이", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "0", "frprvtWrppCo": "0", "frprvtSandCo": "0", "fireSensorCo": "0", "themaEnvrnCl": "", "eqpmnLendCl": "텐트,릴선,화로대", "animalCmgCl": "불가능", "tourEraCl": "", "firstImageUrl": "https://gocamping.or.kr/upload/camp/100177/thumb/thumb_720_4765KHt95RHJsGX6CPmZWqD5.jpg", "createdtime": "2021-11-22", "modifiedtime": "2026-05-14"}
{"contentId": "100863", "facltNm": "가곡 국민여가캠핑장", "lineIntro": "", "intro": "", "allar": "4208", "insrncAt": "N", "trsagntNo": "2023000001", "bizrno": "817-87-03804", "facltDivNm": "공립", "mangeDivNm": "위탁", "mgcDiv": "가곡온천마을협동조합", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "", "induty": "자동차야영장", "lctCl": "계곡", "doNm": "강원특별자치도", "sigunguNm": "삼척시", "zipcode": "25954", "addr1": "강원특별자치도 삼척시 가곡면 가곡천로 1512", "addr2": "", "mapX": "129.208437758367", "mapY": "37.1523654454082", "direction": "", "tel": "033-574-1700", "homepage": "", "resveUrl": "", "resveCl": "온라인실시간예약", "manageNmpr": "1", "gnrlSiteCo": "0", "autoSiteCo": "0", "glampSiteCo": "0", "caravSiteCo": "15", "indvdlCaravSiteCo": "0", "sitedStnc": "3", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "0", "siteMg2Co": "0", "siteMg3Co": "0", "siteBottomCl1": "0", "siteBottomCl2": "0", "siteBottomCl3": "0", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "침대,TV,에어컨,냉장고,유무선인터넷,난방기구,취사도구", "prmisnDe": "2023-04-05", "operPdCl": "봄,여름,가을,겨울", "operDeCl": "평일+주말", "trlerAcmpnyAt": "N", "caravAcmpnyAt": "N", "toiletCo": "0", "swrmCo": "0", "wtrplCo": "0", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,산책로", "sbrsEtc": "", "posblFcltyCl": "계곡 물놀이,산책로,농어촌체험시설", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "0", "frprvtWrppCo": "0", "frprvtSandCo": "0", "fireSensorCo": "0", "themaEnvrnCl": "여름물놀이,걷기길", "eqpmnLendCl": "", "animalCmgCl": "불가능", "tourEraCl": "봄,여름,가을,겨울", "firstImageUrl": "https://gocamping.or.kr/upload/camp/100863/thumb/thumb_720_7468zHO9t19x0oxqozJocytR.jpg", "createdtime": "2023-05-02", "modifiedtime": "2026-05-14"}
{"contentId": "101217", "facltNm": "양주르글램핑캠핑장", "lineIntro": "All about family fun! 송추 가마골에 있는 캠핑피크닉", "intro": "서울 근교에 자연 속에 준비물 없이 몸만 와서 편하고 무드 넘치게  글램핑 바베큐를 즐길 수 있도록 차별화 되어 만들어진  새롭고 편안한 경험을 하실 수 있는 양주르 입니다. ", "allar": "2856", "insrncAt": "Y", "trsagntNo": "2023000008", "bizrno": "874-87-02768", "facltDivNm": "민간", "mangeDivNm": "직영", "mgcDiv": "김미라", "manageSttus": "운영", "hvofBgnde": "", "hvofEnddle": "", "featureNm": "모든 텐트 안은 인조 잔디가 깔려 있고 캠핑 의자와 테이블, 냉난방기구 (에어컨, 써큘레이터, 히터, 난로) 가 설치되어 있으며 좌식 이용을 하고 싶으신 분들은 돗자리를 가져오셔서  넓고 편안하게 이용하시기를 권장 드립니다.", "induty": "일반야영장", "lctCl": "산", "doNm": "경기도", "sigunguNm": "양주시", "zipcode": "11521", "addr1": "경기도 양주시 장흥면 가마골로 188-56", "addr2": "", "mapX": "126.980297502473", "mapY": "37.734893051666", "direction": "양주르 : 경기도 양주시 장흥면 가마골로 188-50  양주르 주차장 : 경기도 양주시 장흥면 부곡리 39 (무료) ", "tel": "0507-1335-9901", "homepage": "https://www.instagram.com/yangjour.official", "resveUrl": "naver.me/xFrKvXPn", "resveCl": "온라인실시간예약", "manageNmpr": "1", "gnrlSiteCo": "15", "autoSiteCo": "0", "glampSiteCo": "0", "caravSiteCo": "0", "indvdlCaravSiteCo": "0", "sitedStnc": "0", "siteMg1Width": "0", "siteMg2Width": "0", "siteMg3Width": "0", "siteMg1Vrticl": "0", "siteMg2Vrticl": "0", "siteMg3Vrticl": "0", "siteMg1Co": "0", "siteMg2Co": "0", "siteMg3Co": "0", "siteBottomCl1": "0", "siteBottomCl2": "0", "siteBottomCl3": "0", "siteBottomCl4": "0", "siteBottomCl5": "0", "tooltip": "", "glampInnerFclty": "", "caravInnerFclty": "", "prmisnDe": "2023-12-05", "operPdCl": "봄,여름,가을,겨울", "operDeCl": "평일+주말", "trlerAcmpnyAt": "N", "caravAcmpnyAt": "N", "toiletCo": "6", "swrmCo": "8", "wtrplCo": "2", "brazierCl": "개별", "sbrsCl": "전기,무선인터넷,장작판매,온수,트렘폴린,물놀이장,마트.편의점", "sbrsEtc": "", "posblFcltyCl": "산책로,운동장,청소년체험시설,농어촌체험시설", "posblFcltyEtc": "", "clturEventAt": "N", "clturEvent": "", "exprnProgrmAt": "N", "exprnProgrm": "", "extshrCo": "15", "frprvtWrppCo": "1", "frprvtSandCo": "1", "fireSensorCo": "0", "themaEnvrnCl": "여름물놀이", "eqpmnLendCl": "", "animalCmgCl": "가능(소형견)", "tourEraCl": "봄,여름,가을,겨울", "firstImageUrl": "https://gocamping.or.kr/upload/camp/101217/thumb/thumb_720_4101mn6c0mTUCdzsZIzRlkOf.jpg", "createdtime": "2023-12-06", "modifiedtime": "2026-05-13"}
```

**TripCraft 활용 포인트**: 캠핑장 키워드 검색. 캠핑 테마 여행 시 장소 선택.

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

