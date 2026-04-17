---
type: api-catalog
id: visitkorea-openapi-catalog
title: 한국관광공사 OpenAPI 전체 카탈로그
created: 2026-04-17
author_agent: claude-code
author_model: claude-opus-4-7
category: api
source: https://api.visitkorea.or.kr/#/useUtilExercises
total_count: 27
llm_compatibility: universal
---

# 한국관광공사 OpenAPI 전체 카탈로그 (27개)

## 카테고리 분류

| 카테고리 | 개수 | 설명 |
|---|---|---|
| **i18n** (다국어 관광정보) | 8 | 국문/영문/일문/중문 번체·간체/독어/불어/서어/노어 |
| **thematic** (테마 관광) | 7 | 웰니스/의료/반려동물/두루누비/고캠핑/생태/무장애 |
| **big-data-index** (관광지수) | 4 | 자원수요/수요강도/다양성/빅데이터 |
| **content** (콘텐츠) | 3 | 공모전수상작/오디오가이드/관광사진 |
| **big-data-network** (연관성) | 2 | 연관관광지/중심관광지 |
| **big-data-forecast** (예측) | 1 | 방문자 집중률 추이 |
| **industry** (산업) | 1 | 관광인 채용 |
| **기타** | 1 | 관광공모전(사진) 수상작 |

## 다국어 관광정보 서비스 (i18n) — 8개

기본 관광정보 제공. 언어별 엔드포인트 분리. **외국인 관광 서비스의 핵심 API**.

| ID | 언어 | 제목 |
|---|---|---|
| tourism-info-korean | 🇰🇷 국문 | 한국관광공사_국문 관광정보 서비스 |
| tourism-info-english | 🇬🇧 영문 | 한국관광공사_영문 관광정보서비스 |
| tourism-info-japanese | 🇯🇵 일문 | 한국관광공사_일문 관광정보서비스 |
| tourism-info-chinese-simplified | 🇨🇳 중문 간체 | 한국관광공사_중문 간체 관광정보서비스 |
| tourism-info-chinese-traditional | 🇹🇼 중문 번체 | 한국관광공사_중문 번체 관광정보서비스 |
| tourism-info-german | 🇩🇪 독어 | 한국관광공사_독어 관광정보서비스 |
| tourism-info-french | 🇫🇷 불어 | 한국관광공사_불어 관광정보서비스 |
| tourism-info-spanish | 🇪🇸 서어 | 한국관광공사_서어 관광정보서비스 |
| tourism-info-russian | 🇷🇺 노어 | 한국관광공사_노어 관광정보서비스 |

공통 기능: 코드조회 + 통합/상세검색 + 위치기반 + 지역기반 국내 관광정보

**활용 시나리오**: 외국인 대상 서비스의 핵심 데이터 소스. 영/일/중(간/번)은 특히 관광객 비중 높음.

## 테마 관광 API (thematic) — 7개

특정 여행 테마에 특화된 정보.

| ID | 제목 | 핵심 |
|---|---|---|
| wellness-tourism | 웰니스 관광정보 | 지역/위치기반 웰니스 관광지 |
| medical-tourism | 의료관광정보 | 의료 관광 |
| pet-friendly-travel | 반려동물_동반여행 | 관광지/문화시설/축제/숙박/음식점/레포츠/쇼핑 |
| durunubi-trails | 두루누비 정보 | 걷기·자전거 코스 + 주변 관광정보 |
| gocamping | 고캠핑 정보 | 캠핑장 정보 |
| eco-tourism | 생태 관광 정보 | 친환경/공정관광 |
| barrier-free-travel | 무장애 여행 정보 | 장애인/어르신/영유아 동반 |

**활용 시나리오**: 타겟 니치 서비스 (예: 반려인 동반여행, 웰니스 투어, 접근성 여행 등)

## 빅데이터 지수 API (big-data-index) — 4개

관광 수요/트렌드 분석용 메트릭 데이터. "한국관광 데이터랩(DataLab)" 계열.

| ID | 제목 | 지표 구성 |
|---|---|---|
| area-tourism-resource-demand | 지역별 관광 자원 수요 | 관광 서비스 수요, 문화 자원 수요 |
| area-tourism-demand-density | 지역별 관광 수요 강도 | 관광 체류 강도, 관광 소비 강도 |
| area-tourism-diversity | 지역별 관광 다양성 | 관광객 다양성, 관광 소비 다양성, 국제적 다양성 |
| tourism-big-data | 관광빅데이터 정보서비스 | 이동통신, 신용카드, 내비게이션, 관광통계, 조사연구 |

**활용 시나리오**: 트렌드 분석, 지역 추천 알고리즘, 관광 활성도 대시보드

## 콘텐츠 API (content) — 3개

| ID | 제목 | 내용 |
|---|---|---|
| photo-contest-winners | 관광공모전(사진) 수상작 정보 | 제목, 촬영일, 촬영지, 키워드, 이미지 |
| audio-guide | 관광지 오디오 가이드정보 | 한/영/중/일 음성, 대본, 사진 ('odii' 서비스) |
| tourism-photos | 관광사진 정보 | 관광지 사진 |

**활용 시나리오**: 오디오 가이드 앱, 사진 기반 여행지 추천, 비주얼 큐레이션

## 연관성/중심성 API (big-data-network) — 2개

관광지 간 네트워크 분석.

| ID | 제목 | 핵심 |
|---|---|---|
| central-attractions-by-municipality | 기초지자체 중심 관광지 정보 | 지자체별 중심관광지 100위 |
| related-attractions | 관광지별 연관 관광지 정보 | 관광지+음식+숙박 유형별 50위 |

**활용 시나리오**: "이 관광지를 가면 함께 가는 곳" 추천, 여행 코스 자동 생성

## 예측 API (big-data-forecast) — 1개

| ID | 제목 | 내용 |
|---|---|---|
| visitor-concentration-forecast | 관광지 집중률 방문자 추이 예측 | 향후 30일 예측 |

**활용 시나리오**: 혼잡도 회피, 시간대별 추천, 비수기 프로모션

## 산업 API — 1개

| ID | 제목 |
|---|---|
| tourism-jobs | 관광인_채용정보_서비스 |

## 기타 — 1개

| ID | 제목 |
|---|---|
| photo-contest-winners | 관광공모전(사진) 수상작 정보 |

## 핵심 전략적 통찰

### 🎯 우리 공모전 관점의 API 우선순위

#### 1순위 (필수 활용 후보)
- **tourism-info-korean / english**: 기본 관광정보 (모든 앱의 뼈대)
- **tourism-big-data**: 빅데이터 기반 트렌드 (차별화 가능)

#### 2순위 (차별화 가능 조합)
- **visitor-concentration-forecast** (예측) + **related-attractions** (연관) = 코스 자동 생성
- **barrier-free-travel** + **pet-friendly-travel** = 특수 니즈 기반 서비스

#### 3순위 (니치/가점용)
- **durunubi-trails** / **gocamping** / **eco-tourism** 등 테마 특화
- 다국어 API 다수 활용 → 외국인 타겟 어필

### 외국인 관광객 공략 포인트
- **다국어 API 8종 전부 활용** 가능 → 범용성 큰 장점
- 영어/중국어/일본어는 관광객 수 기준 필수

### 20-40대 공략 포인트
- **big-data-index** 기반 트렌드 (20-40대가 데이터/트렌드 민감)
- **audio-guide** + **photo-contest-winners** → 비주얼·스토리 풍부
- **pet-friendly** / **wellness** / **eco** 등 라이프스타일 코드

### 지역 특화 (가점 2점 + RTO 특별상)
- **central-attractions-by-municipality** + 특정 지자체 데이터
- 대상 지역: 부산, 대전, 광주, 세종, 충남, 경북, 강원, 제주

## 다음 단계 (Phase 1-3)

1. 각 API의 매뉴얼 ZIP 다운로드 완료 → `_raw/` 디렉토리
2. 각 매뉴얼을 unzip + 파싱
3. 개별 API 스펙 파일 생성: `knowledge-base/tourism-api/{id}.md`
   - 인증 방식
   - Endpoint 목록
   - Request 파라미터 (필수/선택)
   - Response 스키마
   - 샘플 요청/응답
   - 활용 시나리오 예시
4. llm-wiki 저장 (wiki_ingest)
5. GitHub Wiki 페이지별 업데이트

## 원본

- JSON: `00-api-catalog.json` (27개 전체)
- 매뉴얼 ZIP: `_raw/{id}.zip` (다운로드 진행 중)
- 원본 URL: https://api.visitkorea.or.kr/#/useUtilExercises
