# TripCraft Korea — 한국관광공사 OpenAPI 17종 개발자 통합 가이드

본 문서는 TripCraft Korea 서비스에서 한국관광공사(KTO) 공공데이터포털 OpenAPI 17종을
실제 운용 가능하도록 통합하기 위한 개발자 통합 가이드입니다. 모든 호출 예시는
승인된 ServiceKey와 실제 호출 결과를 기준으로 작성되었으며 샘플 응답은
`docs/data-samples-v2/{slug}/{operation}.json` 에 저장되어 있습니다.

- 수집 일자: 2026-05-16
- ServiceKey: `e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e`
- 일일 한도: 1,000 호출 (개발용 계정)
- 응답 포맷: JSON+XML (요청 시 `_type=json` 으로 지정)

---

## 1. 개요

| 카테고리 | API 수 | 핵심 용도 |
|---|---:|---|
| **국제화 콘텐츠** | 3 | 국문/일문 관광정보, 다국어 검색 (Kor/Jpn 서비스) |
| **테마 특화 정보** | 6 | 고캠핑, 사진, 무장애, 반려동물, 웰니스, 의료관광 |
| **이동·체험** | 3 | 두루누비 코스, 생태관광, 오디오 가이드 |
| **빅데이터 분석** | 5 | 방문자수·집중률·다양성·수요강도·자원수요 |
| 합계 | **17** | |

### TripCraft Korea 통합 시나리오

| TripCraft 기능 | 주요 KTO API |
|---|---|
| 1) 다국어 키워드/지역/카테고리 검색 | KorService2, JpnService2 |
| 2) AI 코스 추천 (반경 기반) | KorService2 `locationBasedList2`, DurunubiService `courseList` |
| 3) 실시간 혼잡도 표시 | TatsCnctrRateService, DataLabService |
| 4) 오디오 스토리텔링 | Odii |
| 5) 경비 산정 (입장료·숙박) | KorService2 `detailIntro2`, GoCamping `basedList` |
| 6) 스탬프 투어 (관광지 인증) | KorService2 `areaBasedList2`, EcoTourService |

---

## 2. 인증 및 호출 기본 패턴

### 2.1 Base URL

```
https://apis.data.go.kr/B551011/{ServiceName}/{operation}
```

`ServiceName` 예: `KorService2`, `JpnService2`, `Odii`, `GoCamping`,
`PhotoGalleryService1`, `KorWithService2`, `KorPetTourService`,
`DurunubiService`, `EcoTourService`, `WellnessTourService`, `MdclTourService`,
`DataLabService`, `TatsCnctrRateService`, `LocgoHubTarService1`,
`AreaTarDivService`, `AreaTarDemDsService`, `AreaTarResDemService`.

### 2.2 공통 파라미터

| 이름 | 필수 | 설명 |
|---|:-:|---|
| `serviceKey` | 필수 | 공공데이터포털 인증키 (URL-encode된 상태로 그대로 사용) |
| `MobileOS` | 필수 | `ETC` 권장 (서버 호출), 모바일에서는 `IOS`/`AND`/`WEB` |
| `MobileApp` | 필수 | 서비스명 — TripCraft Korea 통일값 `TripCraftKorea` |
| `_type` | 필수 | `json` (기본 XML이므로 반드시 지정) |
| `numOfRows` | 옵션 | 페이지 결과 수 (1~100 권장, 기본 10) |
| `pageNo` | 옵션 | 페이지 번호 (1-indexed) |

### 2.3 응답 Envelope

```jsonc
{
  "response": {
    "header": {
      "resultCode": "0000",      // "0000" 또는 "00" 이 정상
      "resultMsg":  "OK"
    },
    "body": {
      "items": {
        "item": [ /* 실제 데이터 배열 */ ]
      },
      "numOfRows": 5,
      "pageNo":    1,
      "totalCount": 1581
    }
  }
}
```

- 정상 응답이라도 `totalCount: 0` 일 수 있음 (해당 조건의 데이터 부재).
- 빅데이터 API의 경우 일부 응답은 위 envelope을 따르지 않고 다음 형태로 옵니다:

```jsonc
{
  "responseTime": "2026-05-16T05:09:41.650",
  "resultCode":   "10",
  "resultMsg":    "INVALID_REQUEST_PARAMETER_ERROR(endYmd)"
}
```

### 2.4 KTO 에러 코드 표

| 코드 | 의미 | 대응 |
|---|---|---|
| `00` / `0000` | 정상 | — |
| `10` | INVALID_REQUEST_PARAMETER_ERROR | 파라미터 형식 오류 (날짜, 코드값 검증) |
| `11` | NO_MANDATORY_REQUEST_PARAMETERS_ERROR | 필수 파라미터 누락 |
| `12` | NO_OPENAPI_SERVICE_ERROR | 잘못된 ServiceName |
| `20` | SERVICE_ACCESS_DENIED_ERROR | 활용 권한 없음 (승인 대기) |
| `21` | LIMITED_NUMBER_OF_SERVICE_REQUESTS_EXCEEDS_ERROR | 일일 한도 초과 |
| `22` | LIMITED_NUMBER_OF_SERVICE_REQUESTS_PER_SECOND_EXCEEDS_ERROR | 초당 호출 한도 (보통 1초 1회) |
| `30` | SERVICE_KEY_IS_NOT_REGISTERED_ERROR | ServiceKey 미등록 |
| `31` | DEADLINE_HAS_EXPIRED_ERROR | ServiceKey 기간 만료 |
| `32` | UNREGISTERED_IP_ERROR | 등록되지 않은 IP |
| `33` | UNSIGNED_CALL_ERROR | 서명 오류 |
| HTTP 429 | Too Many Requests | 초당 호출 제한 — 1~5초 대기 후 재시도 |

---

## 3. API × 기능 활용 매트릭스

행: 17 API, 열: TripCraft Korea 6대 핵심 기능. ●: 핵심, ○: 보조.

| API | 검색 | 코스추천 | 혼잡도 | 오디오 | 경비산정 | 스탬프 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| KorService2 (국문) | ● | ● | ○ | – | ● | ● |
| JpnService2 (일문) | ● | ○ | – | – | ● | ○ |
| Odii (오디오 가이드) | ○ | ○ | – | ● | – | ○ |
| GoCamping (캠핑) | ● | ○ | – | – | ● | ○ |
| PhotoGalleryService1 (사진) | ○ | – | – | – | – | ○ |
| KorWithService2 (무장애) | ● | ● | – | – | ● | ○ |
| KorPetTourService (반려동물) | ● | ● | – | – | ● | ○ |
| DurunubiService (두루누비 코스) | ○ | ● | – | – | – | ○ |
| EcoTourService (생태) | ● | ○ | – | – | – | ● |
| WellnessTourService (웰니스) | ● | ○ | – | – | ● | ○ |
| MdclTourService (의료) | ● | – | – | – | ● | – |
| DataLabService (지역 방문자수) | – | – | ● | – | – | – |
| TatsCnctrRateService (집중률) | – | – | ● | – | – | – |
| LocgoHubTarService1 (기초지자체) | – | – | ● | – | – | – |
| AreaTarDivService (관광 다양성) | – | – | ● | – | – | – |
| AreaTarDemDsService (수요 강도) | – | – | ● | – | – | – |
| AreaTarResDemService (자원 수요) | – | – | ● | – | – | – |

---

## 4. TripCraft 6 카테고리별 활용 시나리오

### 4.1 문화유산 (heritage)

1. **카테고리 코드 확인**: `KorService2/categoryCode2?contentTypeId=12` →
   대분류(A02)·중분류(A0201) 확인
2. **지역 기반 목록**: `KorService2/areaBasedList2?contentTypeId=12&areaCode=1&cat1=A02&numOfRows=20`
3. **상세 정보**: `KorService2/detailCommon2?contentId={id}` (대표 정보) +
   `detailIntro2` (개관시간/입장료) + `detailImage2` (이미지)
4. **혼잡도 보강**: `TatsCnctrRateService/tatsCnctrRatedList?areaCd=51&signguCd=51130&tAtsNm={관광지명}`
5. **오디오 가이드**: `Odii/storyLocationBasedList?mapX&mapY&radius=500`

응답 예시 (`KorService2/areaBasedList2` 의 `item`):
```json
{
  "contentid": "126508",
  "contenttypeid": "12",
  "title": "경복궁",
  "addr1": "서울특별시 종로구 사직로 161",
  "mapx": "126.9769930795",
  "mapy": "37.5796466867",
  "firstimage": "http://tong.visitkorea.or.kr/..."
}
```

### 4.2 미식 (gourmet)

- `contentTypeId=39` (음식점)
- 지역 검색 → `KorService2/locationBasedList2?contentTypeId=39&mapX&mapY&radius=1000`
- 메뉴/영업시간 → `detailIntro2` 의 `firstmenu`, `treatmenu`, `opentimefood`

### 4.3 자연 (nature)

- `contentTypeId=12` + `cat1=A01` (자연)
- 생태탐방 → `EcoTourService/areaBasedList`
- 트래일 → `DurunubiService/courseList?cat2=B0207`

### 4.4 축제 (festival)

- `KorService2/searchFestival2?eventStartDate=20260101&areaCode=1&numOfRows=20`
- 정렬: `arrange=A` (제목순) / `R` (생성일 역순)
- 종료일 필터링은 클라이언트에서 `eventenddate` 기반 처리

### 4.5 힐링 (healing)

- `WellnessTourService/wellnessAreaBasedList?contentTypeId=12&arrange=A`
- 스파/명상/온천 카테고리는 `cat3` 으로 세분화

### 4.6 포토 (photo)

- `PhotoGalleryService1/galleryList1` — 최신순
- `PhotoGalleryService1/gallerySearchList1?keyword={지역명}`
- 상세 이미지 URL은 `galWebImageUrl` 사용 (`galOriginImageUrl` 은 대용량)

---

## 5. 개발 시 주의사항 (Service별 quirks)

### 5.1 ServiceName별 파라미터 차이

| Service | 다국어 파라미터 | 비고 |
|---|---|---|
| `KorService2` | (없음, 기본 한국어) | `contentTypeId`/`areaCode` 카멜케이스 |
| `JpnService2` | (없음, 기본 일본어) | 응답 필드 일본어 |
| `Odii` | `langCode` (대문자 C) | 다른 API는 `lang` |
| `KorWithService2` | (없음) | `wheelchair`, `parking` 등 무장애 플래그 |
| `KorPetTourService` | (없음) | `petAcptAbl` 동반가능 등 |

### 5.2 빅데이터 API 파라미터 규약

| Service | 핵심 필수 파라미터 | 예시 값 |
|---|---|---|
| `DataLabService/metcoRegnVisitrDDList` | `startYmd`, `endYmd` | `20210513`, `20210513` |
| `DataLabService/locgoRegnVisitrDDList` | `startYmd`, `endYmd` | 동일 |
| `TatsCnctrRateService/tatsCnctrRatedList` | `areaCd`, `signguCd`, (선택) `tAtsNm` | `51`, `51130`, `간현관광지` |
| `LocgoHubTarService1/areaBasedList1` | `baseYm`, `areaCd`, `signguCd` | `202503`, `11`, `11530` |
| `AreaTarDivService/*` | `baseYm`, `areaCd`, `signguCd`, `{IxCd}` | `202509`, `11`, `11530`, `3103` |
| `AreaTarDemDsService/*` | `baseYm`, `areaCd`, `signguCd`, `{IxCd}` | `202509`, `11`, `11530`, `2103` |
| `AreaTarResDemService/*` | `baseYm`, `areaCd`, `signguCd`, `{IxCd}` | `202509`, `11`, `11530`, `1201` |

지표코드(IxCd) 파라미터명:
- `areaTouDivList` → `touDivIxCd` (31 전체, 3101~3107 연령별)
- `areaExpDivList` → `expDivIxCd` (32 전체, 3201~ 소비처별)
- `areaIntlDivList` → `intlDivIxCd` (33 전체, 3301~ 국적별)
- `areaTarSjrnDsList` → `tarSjrnDsIxCd` (21 전체, 2101~2105 체류일수별)
- `areaTarExpDsList` → `tarExpDsIxCd` (22 전체, 2201~ 소비강도별)
- `areaTarSvcDemList` → `tarSvcDemIxCd` (11 전체, 1101~ 서비스 검색량)
- `areaCulResDemList` → `culResDemIxCd` (12 전체, 1201~1205 문화자원별)

### 5.3 캐시 전략 (TripCraft Korea 권장)

| 데이터 유형 | 캐시 TTL | 사유 |
|---|---|---|
| `areaCode2`, `categoryCode2`, `ldongCode2` | 30일 | 변경 거의 없음 |
| `areaBasedList2` (관광지 목록) | 24시간 | 일 단위 동기화 |
| `detailCommon2`/`detailIntro2`/`detailImage2` | 7일 | 운영정보 변경 빈도 |
| `searchFestival2` | 6시간 | 축제 기간 변동 |
| `tatsCnctrRatedList` (혼잡도) | 1시간 | 일일 집계, 시간 단위 미세 변동 |
| `metcoRegnVisitrDDList`/`locgoRegnVisitrDDList` | 24시간 | 일 단위 통계 |
| `area*DivList`/`area*DemDsList`/`area*ResDemList` | 7일 | 월 단위 통계 (baseYm) |
| `Odii/story*` | 24시간 | 콘텐츠 변경 드묾 |

### 5.4 호출 계획 (1,000건/일 한도 기준)

- **부트스트랩 (1회)**: 코드 테이블 5종 = 5 호출
- **일일 동기화**:
  - 관광지 목록 syncList (필요 페이지 수) ≈ 50 호출
  - 빅데이터 7종 × baseYm 1개 = 7 호출
- **사용자 트리거**: 평균 사용자당 검색·상세 3~5호출 → 1,000 한도 내 200 사용자/일 가능
- **여유 마진**: 30% 확보 (300 호출), 한도 임박 시 캐시 폴백

### 5.5 Rate Limit (초당)

- 일반적으로 1초 1회 권장. HTTP 429 시 지수 백오프 (1s → 2s → 5s).
- 빅데이터 API는 그보다 엄격하므로 0.5초 텀 두기를 권장.

---

## 6. 샘플 코드

### 6.1 Python (`requests`)

```python
import requests, time
from urllib.parse import urlencode

BASE = "https://apis.data.go.kr/B551011"
SERVICE_KEY = "e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e"

COMMON = {
    "serviceKey": SERVICE_KEY,
    "MobileOS":   "ETC",
    "MobileApp":  "TripCraftKorea",
    "_type":      "json",
}

def kto_call(service: str, op: str, **params):
    qp = {**COMMON, "numOfRows": 20, "pageNo": 1, **params}
    url = f"{BASE}/{service}/{op}?" + urlencode(qp, safe="")
    for attempt in range(3):
        r = requests.get(url, timeout=15)
        if r.status_code == 429:
            time.sleep(2 ** attempt); continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError("Rate-limited 3x")

# 예시: 서울 종로구 문화유산 목록
data = kto_call("KorService2", "areaBasedList2",
                contentTypeId=12, areaCode=1, sigunguCode=1, cat1="A02", arrange="A")
items = data["response"]["body"]["items"]["item"]
for it in items[:5]:
    print(it["title"], it["addr1"])
```

### 6.2 TypeScript (`fetch`)

```ts
const BASE = "https://apis.data.go.kr/B551011";
const SERVICE_KEY = process.env.KTO_SERVICE_KEY!;
const COMMON = {
  serviceKey: SERVICE_KEY,
  MobileOS:   "ETC",
  MobileApp:  "TripCraftKorea",
  _type:      "json",
};

export async function ktoCall<T = any>(
  service: string,
  op: string,
  params: Record<string, string | number> = {},
): Promise<T> {
  const qp = new URLSearchParams({ ...COMMON, numOfRows: "20", pageNo: "1", ...params } as any);
  const url = `${BASE}/${service}/${op}?${qp.toString()}`;
  for (let attempt = 0; attempt < 3; attempt++) {
    const res = await fetch(url, { signal: AbortSignal.timeout(15_000) });
    if (res.status === 429) { await new Promise(r => setTimeout(r, 1000 * 2 ** attempt)); continue; }
    if (!res.ok) throw new Error(`KTO ${op}: HTTP ${res.status}`);
    return res.json();
  }
  throw new Error("KTO rate-limited 3 times");
}

// 사용 예
const data = await ktoCall("KorService2", "areaBasedList2", {
  contentTypeId: 12, areaCode: 1, cat1: "A02", arrange: "A",
});
const items = data.response.body.items.item;
```

---

## 7. 데이터 모델 매핑 (KTO 응답 → TripCraft 내부 모델)

### 7.1 관광지 (Spot)

| KTO 필드 | TripCraft 필드 | 비고 |
|---|---|---|
| `contentid` | `spotId` | 핵심 식별자 |
| `contenttypeid` | `contentTypeId` | 12=관광지, 14=문화시설, 15=축제, 25=여행코스, 28=레포츠, 32=숙박, 38=쇼핑, 39=음식 |
| `title` | `name` | |
| `addr1` + ' ' + `addr2` | `fullAddress` | trim 처리 |
| `mapx`, `mapy` | `coordinates.lng`, `coordinates.lat` | 문자열 → number |
| `firstimage` | `coverImage` | https 변환 권장 |
| `firstimage2` | `thumbnail` | |
| `tel` | `phone` | |
| `homepage` | `website` | HTML 태그 제거 필요 |
| `cat1`/`cat2`/`cat3` | `category.{primary,secondary,tertiary}` | |
| `createdtime`/`modifiedtime` | `createdAt`/`updatedAt` | KTO 포맷 `YYYYMMDDHHMMSS` |

### 7.2 상세 (Detail)

| KTO 필드 | TripCraft | 비고 |
|---|---|---|
| `usefee` | `admissionFee` | HTML → 텍스트 |
| `usetime` | `operatingHours` | |
| `restdate` | `closedDays` | |
| `parking` | `parkingInfo` | |
| `chkbabycarriage` | `strollerAccess` | "가능"/"불가" → boolean |
| `chkcreditcard` | `acceptsCreditCard` | |
| `chkpet` | `petFriendly` | |
| `infocenter` | `contactCenter` | |

### 7.3 숙박 (Stay)

| KTO 필드 | TripCraft | 비고 |
|---|---|---|
| `roomtype` | `roomType` | |
| `roomcount` | `roomCount` | |
| `roomsize1`/`roomsize2` | `roomSize.m2`/`roomSize.pyeong` | |
| `roombasecount`/`roommaxcount` | `occupancy.base`/`occupancy.max` | |
| `roomoffseasonminfee1` | `lodgingPrice.lowSeasonWeekday` | |
| `roompeakseasonminfee1` | `lodgingPrice.peakSeasonWeekday` | |

### 7.4 축제 (Festival)

| KTO 필드 | TripCraft | 비고 |
|---|---|---|
| `eventstartdate` | `startDate` | `YYYYMMDD` → ISO |
| `eventenddate` | `endDate` | |
| `eventplace` | `venue` | |
| `usetimefestival` | `admissionFee` | |
| `sponsor1`/`sponsor2` | `organizers[]` | |

### 7.5 혼잡도 (Crowd)

| KTO 필드 | TripCraft | 비고 |
|---|---|---|
| `tAtsNm` | `spotName` | |
| `cnctrRate` | `concentrationRate` | 집중률(%) |
| `bsisDay` | `baseDate` | |
| `daywkDivNm` | `dayOfWeek` | |

### 7.6 빅데이터 (DataLab)

| KTO 필드 | TripCraft | 비고 |
|---|---|---|
| `areaCode`/`signguCode` | `regionCode` | |
| `areaNm`/`signguNm` | `regionName` | |
| `touDivCd`/`touDivNm` | `visitorType.code`/`.name` | 1=현지인, 2=외지인, 3=외국인 |
| `touNum` | `visitorCount` | 문자열 실수 → number |
| `baseYmd` | `date` | YYYYMMDD |

---

## 8. 샘플 데이터 인덱스 (17 API × 105 오퍼레이션)

| # | API 정식명 | 오퍼레이션 수 | 데이터 포함 | 빠른 참조 |
|---|---|:-:|:-:|---|
| 1 | 고캠핑 정보 조회서비스 | 5 | 3 | [샘플](./고캠핑-정보-조회서비스/) |
| 2 | 관광사진 정보 | 4 | 3 | [샘플](./관광사진-정보/) |
| 3 | 관광지 오디오 가이드정보 | 8 | 6 | [샘플](./관광지-오디오-가이드정보/) |
| 4 | 관광지 집중률 방문자 추이 예측 정보 | 1 | 1 | [샘플](./관광지-집중률-방문자-추이-예측-정보/) |
| 5 | 국문 관광정보 서비스 | 15 | 14 | [샘플](./국문-관광정보-서비스/) |
| 6 | 기초지자체 중심 관광지 정보 | 1 | 1 | [샘플](./기초지자체-중심-관광지-정보/) |
| 7 | 두루누비 정보 서비스 | 2 | 2 | [샘플](./두루누비-정보-서비스/) |
| 8 | 무장애 여행 정보 | 13 | 11 | [샘플](./무장애-여행-정보/) |
| 9 | 반려동물 동반여행 서비스 | 13 | 8 | [샘플](./반려동물_동반여행_서비스/) |
| 10 | 빅데이터 지역별 방문자수 | 2 | 2 | [샘플](./빅데이터_지역별-방문자수/) |
| 11 | 생태 관광 정보 | 3 | 3 | [샘플](./생태-관광-정보/) |
| 12 | 웰니스관광정보 | 9 | 0 | [샘플](./웰니스관광정보/) |
| 13 | 의료관광정보 | 8 | 0 | [샘플](./의료관광정보/) |
| 14 | 일문 관광정보서비스 | 14 | 10 | [샘플](./일문-관광정보서비스/) |
| 15 | 지역별 관광 다양성 | 3 | 3 | [샘플](./지역별-관광-다양성/) |
| 16 | 지역별 관광 수요 강도 | 2 | 2 | [샘플](./지역별-관광-수요-강도/) |
| 17 | 지역별 관광 자원 수요 | 2 | 2 | [샘플](./지역별-관광-자원-수요/) |
| **합계** | | **105** | **71** | |

### 빅데이터 API 학습 완료 파라미터 (TripCraft 운영 환경 적용용)

```json
{
  "metcoRegnVisitrDDList": {"startYmd": "20210513", "endYmd": "20210513"},
  "locgoRegnVisitrDDList": {"startYmd": "20210513", "endYmd": "20210513"},
  "tatsCnctrRatedList":    {"areaCd": "51", "signguCd": "51130"},
  "areaBasedList1":        {"baseYm": "202509", "areaCd": "51", "signguCd": "51130"},
  "areaTouDivList":        {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "touDivIxCd": "3103"},
  "areaExpDivList":        {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "expDivIxCd": "3201"},
  "areaIntlDivList":       {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "intlDivIxCd": "3301"},
  "areaTarSjrnDsList":     {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarSjrnDsIxCd": "2103"},
  "areaTarExpDsList":      {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarExpDsIxCd": "2201"},
  "areaTarSvcDemList":     {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "tarSvcDemIxCd": "1101"},
  "areaCulResDemList":     {"baseYm": "202509", "areaCd": "11", "signguCd": "11530", "culResDemIxCd": "1201"}
}
```

각 슬러그 디렉토리의 `_working-params.json` 파일에 운영 검증된 파라미터가 저장되어
있으니 통합 코드 작성 시 참조하세요.

---

## 부록 A. 추가 학습 필요 항목

- `WellnessTourService` (9 ops), `MdclTourService` (8 ops): 본 수집 시점(2026-05-16) 기준 다수 오퍼레이션의 실제 응답이 빈 결과로 옵니다. ServiceKey가 활용신청 후 데이터 적재 지연일 수 있으니 운영 적용 전 `_meta.json`의 endpoints를 참고하여 수동 재호출하거나 KTO 측 데이터셋 갱신 일정을 확인하세요.
- KTO는 인증키 IP 화이트리스트가 활성화되어 있을 수 있으므로, 운영 서버 IP를 공공데이터포털 활용신청 현황에서 등록할 것.
- 빅데이터 API는 1초 1회 호출 제한(HTTP 429)이 매우 엄격합니다. TripCraft Korea 백엔드 큐(예: BullMQ rate-limiter)에 적용하세요.

## 부록 B. 참고 자료

- 공공데이터포털 활용신청 현황: <https://www.data.go.kr/iim/api/selectAcountList.do>
- KorService2 매뉴얼: 공공데이터포털 → "참고문서 → 개방데이터_활용매뉴얼(국문).zip"
- 지역/시군구 코드 파일: 매뉴얼 zip 내부 `관광지_시군구_코드정보.xlsx`
- 본 가이드 작성에 사용된 스크립트: `scripts/fix-empty-apis.py`, `scripts/fetch-kto-samples-v2.py`
