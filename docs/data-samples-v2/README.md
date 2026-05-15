# 한국관광공사 OpenAPI 17종 실제 샘플 데이터

공공데이터포털 https://www.data.go.kr/iim/api/selectAcountList.do 에 등록·승인된
**17종 한국관광공사 OpenAPI**를 ServiceKey 인증으로 직접 호출하여 수집한 샘플 응답입니다.

- 수집 일자: 2026-05-16
- 방식: data.go.kr 활용신청 현황의 endpoint·ServiceKey를 Playwright로 추출 후 HTTPS 직접 호출
- 저장: `docs/data-samples-v2/{api-slug}/{operation}.json`

## 요약

| # | API 정식명 | 오퍼레이션 수 | 데이터 포함 | 비고 |
|---|---|:-:|:-:|---|
| 1 | [고캠핑 정보 조회서비스](./고캠핑-정보-조회서비스/) | 5 | 3 |  |
| 2 | [관광사진 정보](./관광사진-정보/) | 4 | 3 |  |
| 3 | [관광지 오디오 가이드정보](./관광지-오디오-가이드정보/) | 8 | 6 |  |
| 4 | [관광지 집중률 방문자 추이 예측 정보](./관광지-집중률-방문자-추이-예측-정보/) | 1 | 1 | TOU-107 재수집: areaCd+signguCd+tAtsNm 추가 |
| 5 | [국문 관광정보 서비스](./국문-관광정보-서비스/) | 15 | 14 |  |
| 6 | [기초지자체 중심 관광지 정보](./기초지자체-중심-관광지-정보/) | 1 | 1 | TOU-107 재수집: baseYm+areaCd+signguCd(필수) 추가 |
| 7 | [두루누비 정보 서비스](./두루누비-정보-서비스/) | 2 | 2 |  |
| 8 | [무장애 여행 정보](./무장애-여행-정보/) | 13 | 11 |  |
| 9 | [반려동물_동반여행_서비스](./반려동물_동반여행_서비스/) | 13 | 8 |  |
| 10 | [빅데이터_지역별 방문자수](./빅데이터_지역별-방문자수/) | 2 | 2 | TOU-107 재수집: baseYmd→startYmd/endYmd 수정 |
| 11 | [생태 관광 정보](./생태-관광-정보/) | 3 | 3 |  |
| 12 | [웰니스관광정보](./웰니스관광정보/) | 9 | 0 | 빅데이터 파라미터 추가 학습 필요 |
| 13 | [의료관광정보](./의료관광정보/) | 8 | 0 | 빅데이터 파라미터 추가 학습 필요 |
| 14 | [일문 관광정보서비스](./일문-관광정보서비스/) | 14 | 10 |  |
| 15 | [지역별 관광 다양성](./지역별-관광-다양성/) | 3 | 3 | TOU-107 재수집: touDivIxCd/expDivIxCd/intlDivIxCd 추가 |
| 16 | [지역별 관광 수요 강도](./지역별-관광-수요-강도/) | 2 | 2 | TOU-107 재수집: tarSjrnDsIxCd/tarExpDsIxCd 추가 |
| 17 | [지역별 관광 자원 수요](./지역별-관광-자원-수요/) | 2 | 2 | TOU-107 재수집: culResDemIxCd/tarSvcDemIxCd 추가 |

## 활용 가이드

각 API 디렉토리:
- `_meta.json`: endpoint, 시도된 오퍼레이션 목록, ServiceKey 확보 여부
- `{operation}.json`: 실제 HTTP 응답(JSON). `json.response.body.items.item` 에 데이터 배열.
- 응답이 비어있는 경우 `params_from_page` 또는 `url` 필드로 호출 URL을 확인 가능.

## 빌드 스크립트
- `scripts/scrape-datago-apis.py` — data.go.kr 활용신청 현황 크롤러 (Playwright + 크롬 디버그 포트 9222)
- `scripts/fetch-kto-samples-v2.py` — 추출 메타데이터로 17종 API 일괄 호출
- `scripts/fetch-bigdata-retry.py` — 빅데이터 6종 API 파라미터 수정 후 재수집 (TOU-107)