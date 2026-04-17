---
type: api-spec
id: area-tourism-resource-demand
title: "한국관광공사_지역별 관광 자원 수요"
category: big-data-index
author_agent: claude-code
author_model: claude-opus-4-7
created: 2026-04-17
source: https://api.visitkorea.or.kr/upload/manual/guide/file/manual_areaTarResDemService.zip
manual_file: knowledge-base/tourism-api/_raw/extracted/area-tourism-resource-demand/
llm_compatibility: universal
status: initial-spec
---

# 한국관광공사_지역별 관광 자원 수요

## 개요

관광 자원 수요 정보를 제공합니다. 관광 자원 수요는 빅데이터를 활용하여 관광 산업 수요 활성화 정도를 평가하는 관광 수요 지수 중 하나로 관광 서비스 수요, 문화 자원 수요 등의 지표로 구성되어 있습니다.

## 기본 정보

- **공급처**: 한국관광공사
- **타입**: REST
- **인증**: 공공데이터포털(data.go.kr)에서 ServiceKey 발급 필요
- **매뉴얼**: `_raw/extracted/area-tourism-resource-demand/` (Word + Excel)

## 추정 오퍼레이션 (자동 추출)

> Word 매뉴얼에서 자동 파싱 — 누락/오탐 가능. 정확한 스펙은 매뉴얼 원본 참고.

- `areaCulResDemList`
- `areaTarSvcDemList`

## 공통 요청 파라미터 (추정)

모든 한국관광공사 OpenAPI 공통:
- `serviceKey` (필수): 공공데이터포털 발급 인증키
- `MobileOS` (필수): IOS / AND / WIN / ETC
- `MobileApp` (필수): 앱 이름
- `numOfRows` (선택): 페이지당 행 수
- `pageNo` (선택): 페이지 번호
- `_type` (선택): json / xml

## 공통 응답 구조

```json
{
  "response": {
    "header": {
      "resultCode": "0000",
      "resultMsg": "OK"
    },
    "body": {
      "items": { "item": [...] },
      "numOfRows": 10,
      "pageNo": 1,
      "totalCount": 100
    }
  }
}
```

## 활용 시나리오

관광 자원 수요 정보를 제공합니다. 관광 자원 수요는 빅데이터를 활용하여 관광 산업 수요 활성화 정도를 평가하는 관광 수요 지수 중 하나로 관광 서비스 수요, 문화 자원 수요 등의 지표로 구성되어 있습니다.

**공모전 활용 방안**: (에이전트 Stage 1 리서치에서 확정)

## 매뉴얼 원본

- 활용매뉴얼 docx: `_raw/extracted/area-tourism-resource-demand/`
- 분류체계 xlsx (있는 경우 포함): 카테고리 코드 매핑 정보
- 전체 페이지 수: 602 줄

## 연관 API

(Phase 3에서 아이디어 발산 시 채움)
