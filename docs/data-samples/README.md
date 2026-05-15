# 한국관광공사 OpenAPI 샘플 데이터

> 페치 일자: 2026-05-15 | ServiceKey 기반 직접 호출 (개발계정)

## 개요

- 총 API 수: **27**
- 총 오퍼레이션 수: **170**
- 성공: **2**
- 실패: **168**
- 성공률: **1.2%**

> **참고**: 개발계정(Development Key)은 data.go.kr에서 승인된 서비스에 대해서만 사용 가능합니다.
> HTTP 403 = 해당 서비스 미승인, HTTP 500 = 서비스 경로 오류 또는 미승인

## API 목록

| API 한글명 | ID | 서비스명 | 오퍼레이션 | 성공 | 실패 | 샘플 파일 |
|---|---|---|:---:|:---:|:---:|---|
| 한국관광공사_지역별 관광 자원 수요 | [area-tourism-resource-demand](./area-tourism-resource-demand/) | `AreaTarResDemService` | 2 | 2 | 0 | [areaCulResDemList](./area-tourism-resource-demand/areaCulResDemList.json) [areaTarSvcDemList](./area-tourism-resource-demand/areaTarSvcDemList.json) |
| 한국관광공사_지역별 관광 수요 강도 | [area-tourism-demand-density](./area-tourism-demand-density/) | `AreaTarDemDsService` | 2 | 0 | 2 | _없음_ |
| 한국관광공사_지역별 관광 다양성 | [area-tourism-diversity](./area-tourism-diversity/) | `AreaTarDivService` | 3 | 0 | 3 | _없음_ |
| 한국관광공사_관광공모전(사진) 수상작 정보 | [photo-contest-winners](./photo-contest-winners/) | `PhokoAwrdService` | 6 | 0 | 6 | _없음_ |
| 한국관광공사_웰니스관광정보 | [wellness-tourism](./wellness-tourism/) | `WellnessTursmService` | 10 | 0 | 10 | _없음_ |
| 한국관광공사_의료관광정보 | [medical-tourism](./medical-tourism/) | `MdclTursmService` | 7 | 0 | 7 | _없음_ |
| 한국관광공사_반려동물_동반여행_서비스 | [pet-friendly-travel](./pet-friendly-travel/) | `KorPetTourService2` | 10 | 0 | 10 | _없음_ |
| 한국관광공사_관광지별 연관 관광지 정보 | [related-attractions](./related-attractions/) | `TarRlteTarService1` | 3 | 0 | 3 | _없음_ |
| 한국관광공사_기초지자체 중심 관광지 정보 | [central-attractions-by-municipality](./central-attractions-by-municipality/) | `LocgoHubTarService1` | 2 | 0 | 2 | _없음_ |
| 한국관광공사_관광지 집중률 방문자 추이 예측 정보 | [visitor-concentration-forecast](./visitor-concentration-forecast/) | `TatsCnctrRateService` | 2 | 0 | 2 | _없음_ |
| 한국관광공사_관광인_채용정보_서비스 | [tourism-jobs](./tourism-jobs/) | `tursmService` | 7 | 0 | 7 | _없음_ |
| 한국관광공사_두루누비 정보 서비스 | [durunubi-trails](./durunubi-trails/) | `Durunubi` | 3 | 0 | 3 | _없음_ |
| 한국관광공사_관광빅데이터 정보서비스 | [tourism-big-data](./tourism-big-data/) | `DataLabService` | 2 | 0 | 2 | _없음_ |
| 한국관광공사_관광지 오디오 가이드정보 | [audio-guide](./audio-guide/) | `Odii` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_고캠핑 정보 조회서비스 | [gocamping](./gocamping/) | `GoCamping` | 5 | 0 | 5 | _없음_ |
| 한국관광공사_관광사진 정보 | [tourism-photos](./tourism-photos/) | `PhotoGalleryService1` | 5 | 0 | 5 | _없음_ |
| 한국관광공사_생태 관광 정보 | [eco-tourism](./eco-tourism/) | `GreenTourService1` | 3 | 0 | 3 | _없음_ |
| 한국관광공사_무장애 여행 정보 | [barrier-free-travel](./barrier-free-travel/) | `KorWithService2` | 8 | 0 | 8 | _없음_ |
| 한국관광공사_노어 관광정보서비스 | [tourism-info-russian](./tourism-info-russian/) | `RusService2` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_서어 관광정보서비스 | [tourism-info-spanish](./tourism-info-spanish/) | `SpnService2` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_불어 관광정보서비스 | [tourism-info-french](./tourism-info-french/) | `FreService2` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_독어 관광정보서비스 | [tourism-info-german](./tourism-info-german/) | `GerService2` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_일문 관광정보서비스 | [tourism-info-japanese](./tourism-info-japanese/) | `JpnService2` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_중문 번체 관광정보서비스 | [tourism-info-chinese-traditional](./tourism-info-chinese-traditional/) | `ChtService2` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_중문 간체 관광정보서비스 | [tourism-info-chinese-simplified](./tourism-info-chinese-simplified/) | `ChsService2` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_영문 관광정보서비스 | [tourism-info-english](./tourism-info-english/) | `EngService2` | 9 | 0 | 9 | _없음_ |
| 한국관광공사_국문 관광정보 서비스 | [tourism-info-korean](./tourism-info-korean/) | `KorService2` | 9 | 0 | 9 | _없음_ |

## 실패 원인 분석

| 오류 유형 | 건수 | 원인 |
|---|:---:|---|
| HTTP 403 Forbidden | 117 | 서비스 키 미승인 (해당 API 미신청) |
| HTTP 500 Server Error | 0 | 서비스 경로 오류 또는 키 미승인 |
| HTTP 404 Not Found | 31 | 엔드포인트 없음 |

## 디렉토리 구조

```
docs/data-samples/
├── README.md            이 파일
├── _summary.json        머신 리더블 요약
└── {api-id}/
    ├── _meta.json       API 메타정보 + 페치 결과
    ├── {operation}.json 응답 샘플 (성공 시)
    └── errors.log       실패 기록
```