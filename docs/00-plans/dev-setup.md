---
type: guide
id: dev-setup
title: "TripCraft Korea — Phase 2 개발 환경 셋업 가이드"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-05-13T00:00:00+09:00
status: draft
trigger: 예비심사 통과 후 Sprint 1 시작 시 활성화
llm_compatibility: universal
---

# TripCraft Korea — Phase 2 개발 환경 셋업 가이드

> **소요 시간**: 약 30~60분 (패키지 다운로드 포함)  
> **전제**: Python 3.11+, Node.js 18+, Git 설치 완료

---

## 1. 레포지토리 셋업

```bash
# 새 앱 레포 생성 (기획 레포와 분리)
gh repo create 40s-AI-Study/tripcraft-korea-app --public
git clone https://github.com/40s-AI-Study/tripcraft-korea-app
cd tripcraft-korea-app
```

### 디렉터리 구조 초기화

```
tripcraft-korea-app/
├── backend/           # FastAPI 백엔드
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   └── services/
│   ├── requirements.txt
│   └── .env.example
├── frontend/          # HTML/CSS/JS → 추후 React
│   ├── index.html
│   ├── css/
│   └── js/
├── data/              # TourAPI 임베딩 캐시
│   └── chroma/
├── scripts/           # 빌드·배포 스크립트
└── README.md
```

---

## 2. 백엔드 셋업 (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install fastapi uvicorn httpx python-dotenv \
            sentence-transformers chromadb \
            pillow exifread  # 스탬프 EXIF 인증용
```

### `.env` 파일 생성

```bash
cp .env.example .env
# 아래 값 채우기
```

`.env.example`:
```env
# KTO TourAPI
KTO_API_KEY=your_kto_api_key_here
KTO_BASE_URL=https://apis.data.go.kr/B551011

# 카카오 API
KAKAO_REST_API_KEY=your_kakao_rest_api_key_here
KAKAO_JAVASCRIPT_KEY=your_kakao_js_key_here

# 서비스 설정
APP_ENV=development
CHROMA_PERSIST_DIR=./data/chroma
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 서버 실행

```bash
uvicorn app.main:app --reload --port 8000
# → http://localhost:8000/docs (Swagger UI)
```

---

## 3. KTO API Key 발급

1. [data.go.kr](https://data.go.kr) 로그인
2. **마이페이지 → 오픈API → 활용신청**
3. 필수 신청 API (12종):

| # | 서비스명 | 오퍼레이션 |
|---|---|---|
| 1 | 한국관광공사_국문관광정보 서비스 | `areaBasedList2`, `searchKeyword2`, `detailCommon2` |
| 2 | 한국관광공사_연관관광지정보 서비스 | `relatedTour2` |
| 3 | 한국관광공사_기초지자체 중심관광지정보 서비스 | `middlePerformanceRanking` |
| 4 | 한국관광공사_관광지 집중률 방문자 추이 예측 정보 | `getPredictVisitorList` |
| 5 | 한국관광공사_관광빅데이터 정보서비스 | `visitAreaTrend` |
| 6 | 한국관광공사_관광지 오디오가이드 정보서비스 | `audioGuide` |
| 7 | 한국관광공사_다국어 관광정보 서비스(영어) | `areaBasedList2` |
| 8 | 한국관광공사_다국어 관광정보 서비스(중국어) | `areaBasedList2` |
| 9 | 한국관광공사_다국어 관광정보 서비스(일본어) | `areaBasedList2` |
| 10 | 한국관광공사_지역별 관광 다양성 정보 서비스 | `areaTourismDiversity` |
| 11 | 한국관광공사_관광 사진 공모전 수상작 정보 서비스 | `photoContestWinners` |
| 12 | 한국관광공사_무장애 여행정보 서비스 | `barrierFreeInfo` |

> ⚠️ 승인까지 1~3 영업일 소요. OT 직후 즉시 신청 권장.

---

## 4. 카카오 개발자 앱 등록

1. [developers.kakao.com](https://developers.kakao.com) 로그인
2. **내 애플리케이션 → 애플리케이션 추가하기**
3. 앱 이름: `TripCraft Korea`
4. **활성화 필요 API**:

| API | 설정 항목 |
|---|---|
| 카카오맵 | JavaScript 키 → 도메인 등록 |
| 카카오 로그인 | Redirect URI 등록 (`http://localhost:3000/oauth/callback`) |
| 카카오 모빌리티 | REST API 키 |

---

## 5. 프론트엔드 셋업 (Vanilla)

```bash
cd frontend
# 별도 빌드 없음 — 직접 브라우저에서 열기
open index.html
# 또는 로컬 서버
python3 -m http.server 3000
# → http://localhost:3000
```

---

## 6. TourAPI 데이터 임베딩 (Sprint 1 필수)

```bash
cd backend
python scripts/embed_tourapi.py \
  --api-key $KTO_API_KEY \
  --limit 260000 \
  --output ../data/chroma
# 소요 시간: 약 2~4시간 (API 호출 한도에 따라)
```

> 💡 임베딩 완료 후 `data/chroma/` 폴더를 팀 공유 드라이브에 백업 권장.

---

## 7. 로컬 개발 서버 실행 (전체)

```bash
# 터미널 1: 백엔드
cd backend && uvicorn app.main:app --reload --port 8000

# 터미널 2: 프론트엔드
cd frontend && python3 -m http.server 3000

# 접속
open http://localhost:3000
```

---

## 8. 기존 프로토타입 뷰어 실행

현재 기획 레포의 프로토타입을 참고용으로 볼 때:

```bash
cd ~/tourism-service-lab-v2
python3 -m http.server 3300
open http://127.0.0.1:3300/docs/prototypes/
```

---

## 참고 문서

- [Phase 2 개발 계획](./2026-phase2-dev-plan.md)
- [ADR-006 기술 스택 결정](../01-decisions/006-phase2-tech-stack.md)
- [TripCraft Korea API 활용 명세](../deliverables/proposal-tripcraft/04-api-utilization.md)
- KTO TourAPI Swagger: https://api.visitkorea.or.kr

*작성: 📋 기획님 (PM) | 2026-05-13*
