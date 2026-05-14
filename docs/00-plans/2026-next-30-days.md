---
type: plan
id: 2026-next-30-days
title: "TripCraft Korea — 향후 30일 실행 계획 (2026-05-13 ~ 06-12)"
author_agent: productmanager
author_model: claude-sonnet-4-6
created: 2026-05-13T00:00:00+09:00
status: active
llm_compatibility: universal
---

# TripCraft Korea — 향후 30일 실행 계획

> **기준일**: 2026-05-13  
> **종료**: 2026-06-12  
> **핵심 이벤트**: 예비심사 결과 발표 (5월 중)

---

## 주차별 계획

### Week 1 (5/13~5/19) — 결과 대기 + 기반 정비

| 항목 | 담당 | 상태 |
|---|---|---|
| git push (기획 레포 36개 커밋) | Board | ⏳ **즉시** |
| 예비심사 결과 모니터링 | Board | 이메일·api.visitkorea.or.kr 공지 확인 |
| KTO API Key 신청 (data.go.kr) | Board | OT 전 선제 신청 권장 |
| 카카오 개발자 앱 등록 | Board | `TripCraft Korea` 앱 생성 |

### Week 2~3 (5/20~6/02) — 예비심사 결과 대응

**시나리오 A — 통과 (OT 참가)**
- [ ] OT 준비 가이드 실행 (`docs/00-plans/2026-ot-preparation.md`)
- [ ] ADR-006 상태 `proposed` → `approved`
- [ ] Phase 2 개발 레포 생성 (`tripcraft-korea-app`)
- [ ] Sprint 1 킥오프 이슈 생성 (Paperclip)

**시나리오 B — 미통과**
- [ ] 탈락 사유 문의 (gongmo@stunning.kr)
- [ ] 자산 보존 확인 (현재 레포 private, 프로토타입 27개 보존)
- [ ] 독립 서비스 출시 가능성 검토 회의

### Week 4 (6/03~6/12) — Phase 2 Sprint 1 (통과 시)

| Sprint 1 목표 | 담당 에이전트 | 기한 |
|---|---|---|
| FastAPI 프로젝트 초기화 + KTO API 연동 테스트 | 🔌 API | 6/07 |
| TourAPI 26만건 임베딩 파이프라인 구축 | 🔌 API | 6/10 |
| F1 관광 정보 검색 기본 동작 | 🔌 API + 🎨 UX | 6/12 |
| 기본 UI (검색 화면) 초안 | 🎨 UX | 6/12 |

---

## Board 즉시 액션 3가지

### 1. git push (지금 즉시)

```bash
cd ~/tourism-service-lab-v2 && git push
```

36개 PM 문서 커밋이 원격에 없는 상태. GitHub에서 팀 전체가 최신 문서를 볼 수 있도록.

### 2. KTO API Key 신청 (이번 주 내)

[data.go.kr](https://data.go.kr) → 오픈API 활용신청 → 12종 신청  
승인까지 1~3 영업일. OT 전에 받아두어야 Sprint 1 지연 없음.

### 3. 예비심사 결과 확인 채널

- 이메일: gongmo@stunning.kr (접수 시 사용한 이메일)
- 사이트: https://api.visitkorea.or.kr/#/cntSearchDetail?no=1

---

## 성공 지표 (30일 후)

| 지표 | 목표 |
|---|---|
| 예비심사 결과 확인 | ✅ 통과 or ✅ 피드백 수신 |
| git push 완료 | ✅ GitHub에 36개 커밋 |
| KTO API Key 발급 | ✅ 12종 승인 |
| Phase 2 시작 (통과 시) | ✅ Sprint 1 첫 데모 |

---

*작성: 📋 기획님 (PM) | 2026-05-13*
