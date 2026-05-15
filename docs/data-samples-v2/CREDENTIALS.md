# KTO OpenAPI 인증키 보관 파일

> ⚠️ **보안 경고**: 본 파일은 로컬 개발 참조용입니다.  
> 실제 배포 시에는 반드시 **환경변수**로 분리하십시오. 상세 내용은 [보안 정책](#보안-정책) 참조.

---

## 서비스키 (ServiceKey)

| 항목 | 값 |
|------|-----|
| **Raw 64자 키** | `e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e` |
| **URL-encoded 키** | `e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e` ※ 특수문자 없음, raw와 동일 |
| 발급 플랫폼 | data.go.kr (공공데이터포털) |
| 계정 구분 | **개발계정** (자동승인, 활용신청) |
| 신청일 | 2026-05-16 |
| 만료 예정일 | **2028-05-16** (활용 종료 24개월 기준) |
| 갱신 주기 | 만료 전 data.go.kr 활용신청 갱신 필요 |

### Raw vs URL-encoded 차이

data.go.kr은 서비스키를 두 가지 형태로 제공합니다:

- **일반 인증키 (Raw)**: `e8422cf7...` — 특수문자 없는 hex 문자열. URL 쿼리에 그대로 사용 가능.
- **URL-encoded 키**: 특수문자(+, /, =)가 포함된 키는 `%2B`, `%2F`, `%3D`로 인코딩. 본 키는 hex 전용이므로 두 형태 동일.

---

## 승인된 API 목록 (17개)

| No | API 정식명 | Endpoint Base | 일일 트래픽 | 처리상태 | 만료일 |
|----|-----------|---------------|-----------|---------|-------|
| 1 | 한국관광공사_국문 관광정보 서비스_GW | `https://apis.data.go.kr/B551011/KorService2` | 1,000건/일 | 승인 | 2028-05-16 |
| 2 | 한국관광공사_일문 관광정보서비스_GW | `https://apis.data.go.kr/B551011/JpnService2` | 1,000건/일 | 승인 | 2028-05-16 |
| 3 | 한국관광공사_무장애 여행 정보 | `https://apis.data.go.kr/B551011/KorWithService2` | 1,000건/일 | 승인 | 2028-05-16 |
| 4 | 한국관광공사_생태 관광 정보_GW | `https://apis.data.go.kr/B551011/GreenTourService1` | 1,000건/일 | 승인 | 2028-05-16 |
| 5 | 한국관광공사_관광사진 정보_GW | `https://apis.data.go.kr/B551011/PhotoGalleryService1` | 1,000건/일 | 승인 | 2028-05-16 |
| 6 | 한국관광공사_고캠핑 정보 조회서비스_GW | `https://apis.data.go.kr/B551011/GoCamping` | 1,000건/일 | 승인 | 2028-05-16 |
| 7 | 한국관광공사_관광지 오디오 가이드정보_GW | `https://apis.data.go.kr/B551011/Odii` | 1,000건/일 | 승인 | 2028-05-16 |
| 8 | 한국관광공사_빅데이터_지역별 방문자수_GW | `https://apis.data.go.kr/B551011/DataLabService` | 1,000건/일 | 승인 | 2028-05-16 |
| 9 | 한국관광공사_두루누비 정보 서비스_GW | `https://apis.data.go.kr/B551011/Durunubi` | 1,000건/일 | 승인 | 2028-05-16 |
| 10 | 한국관광공사_관광지 집중률 방문자 추이 예측 정보 | `https://apis.data.go.kr/B551011/TatsCnctrRateService` | 1,000건/일 | 승인 | 2028-05-16 |
| 11 | 한국관광공사_기초지자체 중심 관광지 정보 | `https://apis.data.go.kr/B551011/LocgoHubTarService1` | 1,000건/일 | 승인 | 2028-05-16 |
| 12 | 한국관광공사_반려동물_동반여행_서비스 | `https://apis.data.go.kr/B551011/KorPetTourService2` | 1,000건/일 | 승인 | 2028-05-16 |
| 13 | 한국관광공사_의료관광정보 | `https://apis.data.go.kr/B551011/MdclTursmService` | 1,000건/일 | 승인 | 2028-05-16 |
| 14 | 한국관광공사_웰니스관광정보 | `https://apis.data.go.kr/B551011/WellnessTursmService` | 1,000건/일 | 승인 | 2028-05-16 |
| 15 | 한국관광공사_지역별 관광 다양성 | `https://apis.data.go.kr/B551011/AreaTarDivService` | 1,000건/일 | 승인 | 2028-05-16 |
| 16 | 한국관광공사_지역별 관광 수요 강도 | `https://apis.data.go.kr/B551011/AreaTarDemDsService` | 1,000건/일 | 승인 | 2028-05-16 |
| 17 | 한국관광공사_지역별 관광 자원 수요 | `https://apis.data.go.kr/B551011/AreaTarResDemService` | 1,000건/일 | 승인 | 2028-05-16 |

---

## 계정 정보

| 항목 | 내용 |
|------|------|
| 운영 계정 여부 | ❌ 개발계정 (활용신청 자동승인) |
| reqstStepCode | `PR0027` (승인 완료) |
| 심의 방식 | 자동승인 |
| 활용 목적 | 참고자료 / 관광공사 공모전 데이터 확인 |
| 이용허락범위 | 이용허락범위 제한 없음 |

> **개발계정 vs 운영계정**: 현재 키는 개발계정입니다. 상용 서비스 출시 전 운영계정으로 전환 신청 권장 (일일 트래픽 증가 가능).

---

## 보안 정책

### 실제 배포 시 환경변수 분리 방법

본 파일은 **로컬 개발 참조용**으로만 사용합니다.  
실제 배포 환경에서는 아래 방법으로 키를 분리하십시오.

#### 백엔드 (Node.js / Python)
```bash
# .env 파일 (절대 git에 커밋하지 않음)
KTO_SERVICE_KEY=e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e
```

```python
# Python
import os
service_key = os.environ.get('KTO_SERVICE_KEY')
```

```javascript
// Node.js
const serviceKey = process.env.KTO_SERVICE_KEY;
```

#### Next.js 프론트엔드
```bash
# .env.local (git ignore 대상)
KTO_SERVICE_KEY=e8422cf7d5e4738694576c32619297b2e82236329a46046ad5d64cdfef74756e
```

```javascript
// Next.js API Route에서만 사용 (클라이언트 노출 금지)
const serviceKey = process.env.KTO_SERVICE_KEY;
```

#### Vercel / Railway 배포
- Vercel: Dashboard → Settings → Environment Variables → `KTO_SERVICE_KEY` 추가
- Railway: Dashboard → Variables → `KTO_SERVICE_KEY` 추가

### 파일 보관 방침

- 본 `CREDENTIALS.md`는 사용자 요청에 따라 **git에 커밋하여 보관**합니다.
- 단, README 및 DEVELOPER_GUIDE에 **"실제 운영 시 환경변수로 분리하라"** 경고가 명시되어 있습니다.
- `.gitignore`에 추가하지 않음 (의도적 보관).

---

## 갱신 절차

1. 만료 1개월 전 data.go.kr 로그인 → 마이페이지 → 활용신청 현황
2. 해당 API 활용 연장 신청
3. 새 서비스키 발급 시 본 파일 및 `scripts/.env.local` 업데이트
4. 배포 환경 환경변수도 함께 갱신

