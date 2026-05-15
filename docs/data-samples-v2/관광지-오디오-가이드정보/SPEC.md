# 한국관광공사_관광지 오디오 가이드정보_GW — 응답 데이터 스펙
> **파일 위치**: `docs/data-samples-v2/관광지-오디오-가이드정보/SPEC.md`  
> **최종 업데이트**: 2026-05-16

---

## 1. API 개요

| 항목 | 내용 |
|------|------|
| 정식명 | 한국관광공사_관광지 오디오 가이드정보_GW |
| 카탈로그 ID | uddi:Odii |
| Endpoint Base URL | `https://apis.data.go.kr/B551011/Odii` |
| 일일 트래픽 | 1,000건/일 |
| 활용기간 | 2026-05-16 ~ 2028-05-16 |
| 계정 구분 | 개발계정 (자동승인) |

**Service path 특이사항**: ⚠️ langCode 파라미터는 반드시 대문자(KO, EN, JA, ZH). 소문자 입력 시 결과 없음.

## 2. 오퍼레이션 목록

| 오퍼레이션명 | URL Path | 용도 | 인증 외 필수 파라미터 | 응답 데이터 보유 |
|------------|----------|------|---------------------|----------------|
| `storyBasedList` | `/storyBasedList` | 오디오 스토리 지역기반 목록 조회 | langCode(대문자: KO/EN/JA/ZH) | ✅ |
| `storyBasedSyncList` | `/storyBasedSyncList` | 오디오 스토리 동기화 목록 조회 | - | ❌ |
| `storyLocationBasedList` | `/storyLocationBasedList` | 오디오 스토리 위치기반 목록 조회 | mapX, mapY, radius, langCode(대문자: KO/EN/JA/ZH) | ✅ |
| `storySearchList` | `/storySearchList` | 오디오 스토리 검색 조회 | - | ✅ |
| `themeBasedList` | `/themeBasedList` | 오디오 테마 지역기반 목록 조회 | langCode(대문자: KO/EN/JA/ZH) | ✅ |
| `themeBasedSyncList` | `/themeBasedSyncList` | 오디오 테마 동기화 목록 조회 | - | ❌ |
| `themeLocationBasedList` | `/themeLocationBasedList` | 오디오 테마 위치기반 목록 조회 | mapX, mapY, radius, langCode | ✅ |
| `themeSearchList` | `/themeSearchList` | 오디오 테마 검색 조회 | - | ✅ |

## 3. 오퍼레이션별 상세

### 3.1 `storyBasedList`

**용도**: 오디오 스토리 지역기반 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Odii/storyBasedList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&langCode=ko&tid=1
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
| langCode | - | 필수 | string | - | 대문자: KO/EN/JA/ZH |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `tid` | tid | code | 1 | - |
| `tlid` | tlid | code | 1 | - |
| `stid` | stid | code | 1 | - |
| `stlid` | stlid | code | 1 | - |
| `title` | 관광지명 | string | 백제문화단지 - 입구 | - |
| `mapX` | 경도 | coord | 126.906603 | - |
| `mapY` | 위도 | coord | 36.3055904 | - |
| `audioTitle` | 오디오 제목 | string | 살아나는 백제, 백제문화단지 | - |
| `script` | script | string | 살아나는 백제, 백제문화단지  여러분이 지금 보시는 이곳은 백제의 역사와 문화를 한눈에 볼 수 있는 백제문화 | - |
| `playTime` | playTime | datetime | 122 | - |
| `audioUrl` | 오디오 URL | url |  | - |
| `langCode` | 언어코드 | code | ko | - |
| `imageUrl` | imageUrl | url |  | - |
| `createdtime` | 등록일시 | datetime | 20150608203200 | - |
| `modifiedtime` | 수정일시 | datetime | 20160728153604 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"tid": "1", "tlid": "1", "stid": "1", "stlid": "1", "title": "백제문화단지 - 입구", "mapX": "126.906603", "mapY": "36.3055904", "audioTitle": "살아나는 백제, 백제문화단지", "script": "살아나는 백제, 백제문화단지  여러분이 지금 보시는 이곳은 백제의 역사와 문화를 한눈에 볼 수 있는 백제문화단지예요. 첨단 기술을 활용해 백제시대의 다양한 모습을 생생하게 재현한 곳이죠. 그럼 지금부터 저와 함께 백제문화단지에 대해 알아볼까요?  여러분은 백제에 대해서 얼마나 알고 계세요? 삼국시대 한반도의 강국으로 군림했던 백제는 오랜 역사와 뛰어난 문화를 가지고 있었지만, 당시를 알 수 있는 것들이 많이 남아있지 않아서 사람들의 관심을 받지 못했어요. 그래서 찬란했던 백제시대의 역사와 문화를 전 세계에 알리고자 백제의 마지막 수도였던 부여에 백제문화단지를 조성하게 됐죠.  백제문화단지에는 역사서에 적혀있지만, 오랜 시간이 흘러 그 모습을 알 수 없던 백제의 다양한 문화유산이 한자리에 모여 있답니다. 대표적으로 백제 건국 당시의 도성인 위례성과 백제시대를 대표하는 고분들이 재현되어 있어요. 그리고 10여 년의 긴 시간 동안 충분한 고증을 거쳐 조성된 백제 최고의 궁성인 사비궁과 사비시대 왕족들이 나라의 안녕을 위해 기도 드렸던 능사도 보실 수 있죠. 마지막으로 국내 최초의 백제 역사 전문 박물관인 백제역사문화관도 관람하실 수 있으니 놓치지 말고 꼭 살펴보세요.   지금까지 제가 백제문화단지에 대해 간단하게 설명 드렸지만, 이곳에는 제가 말씀드린 것보다 더 많은 볼거리들이 가득하답니다. 그럼 지금부터 당시의 모습을 살펴보고, 체험하며 백제시대를 만끽하는 시간이 되시길 바래요.", "playTime": "122", "audioUrl": "", "langCode": "ko", "imageUrl": "", "createdtime": "20150608203200", "modifiedtime": "20160728153604"}
{"tid": "1", "tlid": "1", "stid": "2", "stlid": "4", "title": "백제문화단지 - 계획도시사비", "mapX": "126.9066245", "mapY": "36.3068354", "audioTitle": "계획도시 사비", "script": "계획도시 사비  [해설] 여러분이 보시는 이곳은 백제의 세 번째 수도 사비를 고증을 통해 재현한 곳이에요. 백제 사람들은 성을 중심으로 생활했는데 사비도성에는 사비궁을 비롯한 관청, 사원, 도로, 수리시설 등이 나성 안에 배치되었는데, 사비 천도를 목적으로 철저히 계획된 개발도시랍니다. 근데 왜 백제의 왕은 수도를 사비로 옮겼을까요? 그럼, 지금부터 왜 사비천도를 했는지 그 이유를 알아볼까요? 저기 성왕께서 사비천도문제를 놓고 신하와 얘기를 나누고 계시네요.   [성왕]  지금 우리가 살고 있는 웅진은 고구려의 침략을 피해 임시로 정한 수도였다. 방어에는 적합하지만 나라가 발전하기에는 부족한 것이 너무도 많다. 땅도 좁고, 간만의 차가 심해 국내뿐 아니라 다른 나라와의 교역도 원활하지 못해, 백성들이 살기에 너무도 불편하다는 것을 경들은 알 것이다. 하지만 새로운 수도가 될 사비는 대지도 넓을 뿐 아니라 북쪽으로 부소산이 솟아있고, 북에서 서쪽과 남쪽으로 흐르는 백마강이 최고의 방파제가 되니, 동쪽에 나성만 지으면, 외적의 침입을 막을 수 있는 최고의 장소이다.  [대신]   폐하. 사비는 오래전부터 물난리가 자주 나는 지역으로 사람이 살 수 없는 곳입니다. 사비는 백제의 수도로 적합하지 않습니다.   [성왕]  아니다. 백마강의 범람을 막기 위해 치수시설을 튼튼히 하면 될 것이다. 인공저수지를 만들어 파낸 흙은 땅을 다지고 성벽을 만드는 데 사용하고 모인 물은 생활용수와 홍수 조절에 이용하면 될 것이다. 이곳의 수운 또한 조수 간만의 차가 적어 상업 활동을 활발하게 할 수 있으니 백성들의 삶은 윤택해지고 백제가 부흥하는 데 최상의 적지가 될 것이야. 모든 대신들은 듣거라! 새로운 백제의 발전을 위해 사비로 수도를 천도하겠다. 백성들이 살기 좋은 새로운 성을 세우라!   [대신]  예, 폐하.   [해설]  불모지의 땅, 사비에서 새로운 백제를 꿈꾸던 성왕과 백제인들의 꿈. 화려한 백제의 부활을 이끌었던 그들의 꿈이 1400년이 지난 지금 우리들 눈앞에 펼쳐져 있습니다.  이제 백제의 미래도시, 사비성으로 들어가 보실까요?", "playTime": "175", "audioUrl": "", "langCode": "ko", "imageUrl": "", "createdtime": "20150612121419", "modifiedtime": "20160728154038"}
{"tid": "1", "tlid": "1", "stid": "3", "stlid": "7", "title": "백제문화단지 - 천정전", "mapX": "126.9066298", "mapY": "36.3073888", "audioTitle": "천정전", "script": "천정전  지금 보시는 건물은 백제 사비시기의 궁전을 재현해 놓은 곳이에요. 궁궐의 공간은 일반적으로 관청들이 배치되는 외조, 왕이 정치를 하는 치조, 왕과 왕비가 생활하는 연조, 휴식과 연회의 원유공간으로 나눠지는데, 새롭게 재현된 사비궁은 역사적 고증을 토대로 고대 궁궐의 기본배치 형식을 따라 왕의 대외적 공간인 치조권역을 재현해 놓았답니다.   사비궁의 정전인 천정전은 왕이 신하들과 함께 모여 나랏일을 하던 백제의 심장이라고 할 수 있죠. 이곳에서는 왕의 즉위의례, 신년행사 등 각종 국가의식이 거행되고, 외국 사신을 맞이했다고 해요.   그럼 사비궁 중앙에 웅장하고 화려하게 지어진 천정전의 이름은 어디에서 유래 됐는지 살펴볼까요?   고대 백제에는 국가의 큰 정사를 하늘에 고하고 결정했다는 천정대가 있었어요.   역사서에 보면 이곳 천정대를 정사암이라고 불렀는데, 백제에서 재상을 선출할 때 3~4인의 이름을 쓴 후 밀봉하여 바위에 두었다가 얼마 후에 뜯어보면 이름 위에 도장이 찍혀 있어 그 사람을 재상으로 삼았다고 합니다.  이처럼 백제에서는 국가중대사를 결정할 때 이곳 천정대에서 하늘에 제사를 지내고, 서로의 의견을 모아 나라의 중요한 일을 결정하는데, 하늘의 뜻에 따라 정치를 한다는 의미가 있었죠.   그래서 여러분이 지금 계신 천정전도 천정대의 이름을 따서 짓게 되었답니다.   사비궁을 바라보고 있으니 백제 왕국의 번영과 백성들의 안위를 위해 온 힘을 다해 노력하는 백제 왕들의 숨결이 느껴지네요.   사비궁을 나가서 오른쪽으로 가시면 능사와 고분공원이 있고, 왼쪽으로 가시면 생활문화마을과 위례성이 있으니 다른 시설도 보면서, 당시의 모습을 느낄 수 있는 시간이 되시길 바래요. ", "playTime": "142", "audioUrl": "", "langCode": "ko", "imageUrl": "", "createdtime": "20150615140942", "modifiedtime": "20160728161851"}
```

**TripCraft 활용 포인트**: 지역별 오디오 스토리 목록. AR/오디오 가이드 기능 구현.

---

### 3.2 `storyBasedSyncList`

**용도**: 오디오 스토리 동기화 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Odii/storyBasedSyncList?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

> ⚠️ 수집 시 데이터 없음 (필수 파라미터 미충족 또는 결과 없음)

**응답 예시 (최대 3건 발췌)**:

> 샘플 없음

**TripCraft 활용 포인트**: TripCraft 오디오 스토리 동기화 목록 조회 기능에 활용.

---

### 3.3 `storyLocationBasedList`

**용도**: 오디오 스토리 위치기반 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Odii/storyLocationBasedList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&langCode=ko&mapX=126.9779692&mapY=37.566535&radius=5000
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
| langCode | - | 필수 | string | - | 대문자: KO/EN/JA/ZH |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `tid` | tid | code | 43 | - |
| `tlid` | tlid | code | 135 | - |
| `stid` | stid | code | 5420 | - |
| `stlid` | stlid | code | 16418 | - |
| `title` | 관광지명 | string | 종묘 | - |
| `mapX` | 경도 | coord | 126.994143 | - |
| `mapY` | 위도 | coord | 37.574583 | - |
| `audioTitle` | 오디오 제목 | string | 종묘 | - |
| `script` | script | string |  옛사람들은 사람이 죽으면 귀신이 되고, 귀신도 사람처럼 먹고 마시며 잠을 잔다고 믿었어요. 그래서 귀신이  | - |
| `playTime` | playTime | datetime | 139 | - |
| `audioUrl` | 오디오 URL | url | https://sfj608538-sfj608538.ktcdn.co.kr/file/audio/56/16124. | - |
| `langCode` | 언어코드 | code | ko | - |
| `imageUrl` | imageUrl | url | https://sfj608538-sfj608538.ktcdn.co.kr/file/image/service/1 | - |
| `createdtime` | 등록일시 | datetime | 20230725121558 | - |
| `modifiedtime` | 수정일시 | datetime | 20230725121559 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"tid": "43", "tlid": "135", "stid": "5420", "stlid": "16418", "title": "종묘", "mapX": "126.994143", "mapY": "37.574583", "audioTitle": "종묘", "script": " 옛사람들은 사람이 죽으면 귀신이 되고, 귀신도 사람처럼 먹고 마시며 잠을 잔다고 믿었어요. 그래서 귀신이 생활하는 집을 짓고 음식을 차려 주었는데, 조상신을 모신 집을 사당이라 불렀지요. 조선 시대 양반가에서는 집집마다 사당을 지어 조상신을 모셨답니다.    종묘는 왕실의 조상신을 모신 사당입니다. 조선 왕조가 한양으로 도읍을 옮긴 해에 만들어지기 시작하여 이듬해에 완공되었죠. 산과 숲으로 둘러싸인 종묘는 왕과 왕비의 신주를 모신 정전과 영녕전, 제례 준비에 필요한 몇몇 부속 전각으로 이루어져 있습니다. 전각을 살펴보면 장식과 기교를 최대한 절제하고자 한 것이 느껴지는데요. 이는 종묘가 조상신의 영혼을 모신 엄숙하고 경건한 공간이기 때문에 최소한의 색만을 사용하고 화려한 단청을 하지 않았던 것으로 보입니다. 이러한 종묘는 조선 왕실이 무엇보다 가장 중요하게 여긴 곳이에요. 세종 시기 조선에는 많은 백성이 목숨을 잃을 정도의 큰 화재가 일어났었는데, 큰 화재로 인한 위기 속에서 소헌왕후는 종묘를 가장 먼저 지키라고 명령했었죠.   종묘에서는 매년 계절마다 조상의 이름을 쓴 위패를 모시고 제사를 지냈습니다. 왕비를 뽑거나 세자를 결정하는 등 왕실의 중요한 일이 생겨도 종묘에 가서 조상신에게 알리고 좋은 일이 계속되기를 기원했어요. 왕실 사람에게 큰 병이 나거나 나쁜 일이 생겨도 종묘를 찾았지요. 조상신의 도움으로 어려움을 해결할 수 있다고 믿었던 것입니다. 오늘날까지도 종묘제례라 불리는 제사 의례가 행해지고 있으며 제사에는 종묘제례악의 음악과 춤이 동반됩니다. 이는 세계무형유산으로 등재되었죠.   동아시아 유교 문화의 오랜 정신적 전통인 조상숭배 사상과 제사 의례를 바탕으로 엄격하게 지어진 종묘에서 종묘제례악을 즐겨 보시길 추천드립니다. 유형과 무형의 세계문화유산을 함께 감상할 수 있는 특별한 경험이 될 것입니다. ", "playTime": "139", "audioUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/audio/56/16124.mp3", "langCode": "ko", "imageUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/image/service/11309.jpg", "createdtime": "20230725121558", "modifiedtime": "20230725121559"}
{"tid": "43", "tlid": "135", "stid": "5421", "stlid": "16419", "title": "종묘 내 안내판", "mapX": "126.994417", "mapY": "37.572528", "audioTitle": "유네스코 세계유산 종묘의 위상", "script": "유네스코 세계유산 종묘의 위상  ‘종묘 안내판’에 도착하셨습니까?  종묘는 축구장 7개가 들어설 수 있을 정도의 넓은 곳에 조성된 조선의 국가 사당입니다. 태조 3년인 1394년에 짓기 시작해 고쳐 짓는 과정을 수차례 거친 뒤 헌종 2년인 1836년에 이르러 지금의 모습이 되었습니다.  종묘 안에는 조선의 역대 왕과 왕비의 신주를 모시고 제사를 지내는 장소인 ‘정전’과 ‘영녕전’을 비롯해 나라의 제사인 종묘제례를 준비하고 받들어 모시기 위해 마련된 여러 건물들이 자리합니다.   종묘가 1995년 유네스코 세계문화유산에 등재된 것은 인류문화사적으로 큰 가치가 있기 때문입니다. 종묘 제도는 동아시아의 중국, 베트남 등에도 있었지만, 이곳 조선의 종묘처럼 후손 대대로 전통적인 제례가 행해지는 곳은 세계적으로 찾아보기 어렵습니다. 종묘는 조선이라는 한 왕조의 유형, 무형의 제례문화가 고스란히 보존되고 계승되는 역사적인 장소인 것입니다.  또한, 종묘제례와 종묘제례 때 연주되는 음악인 종묘제례악도 2001년 유네스코 인류무형문화자산으로 지정되었습니다. 이렇듯 종묘는 조선 왕조의 제례문화가 고스란히 보존되고 계승되는 역사적인 장소라고 할 수 있습니다.   종묘의 외대문에서 정전 남신문까지는 길이 세 갈래로 나뉘어지는데요. 이 길을 ‘삼도’라고 합니다. 가운데 길은 조상신과 향을 든 제관만이 다닐 수 있는 ‘신향로’이고 정전의 위치에서 바라봤을 때 동쪽은 왕이 다니는 길인 ‘어로’, 서쪽은 세자가 다니는 길인 ‘세자로’입니다. 그럼 종묘 안을 한 번 걸어보시죠.", "playTime": "130", "audioUrl": "", "langCode": "ko", "imageUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/image/service/330.jpg", "createdtime": "20230725122059", "modifiedtime": "20230725122100"}
{"tid": "43", "tlid": "135", "stid": "5422", "stlid": "16420", "title": "지당", "mapX": "126.994351", "mapY": "37.572704", "audioTitle": "천지음양이 조화된 연못, 지당", "script": "천지음양이 조화된 연못, 지당  지금 보시는 망묘루 앞 연못은 종묘에 있는 세 개의 연못 가운데 하나입니다. 연못을 옛말로는 ‘지당’이라고 했죠. 종묘에 연못을 둔 것은 물에 비친 하늘의 기운을 받아서 땅으로 보내고자 하는 기원의 뜻이 담겨 있습니다.   자, 연못의 모습을 한 번 눈여겨보시지요. 네모난 못 안에 둥근 섬이 떠 있다고 해서 한자로 ‘천원지방(天圓地方)’이라고도 하는데요, 우리나라 고유의 연못 형태죠. 사각형의 연못 둘레는 땅을, 가운데의 둥근 섬은 하늘을 상징합니다. 그러니까 천지음양이 조화를 이루어 내내 평안하기를 바란다는 뜻이지요.   종묘는 조선시대 가장 중요한 존재였습니다. 그것을 보여주는 대표적인 예가 왕의 화재대책인데요! 그 이야기를 역사가를 통해서 들어 보시죠.  [인터뷰-건국대학교 사학과 신병주 교수] 조선시대에 도성에 불이 나면 왕은 종묘부터 구하라고 명을 내렸습니다. 종묘는 역대 왕과 왕비의 신주를 모시는 곳으로 조선왕실을 상징하는 곳이기 때문입니다. 그래서 왕은 화재에 대비한 대비책으로 당시 종묘에 많았던 소나무의 일부를 잘라내라는 명령을 내리기도 했습니다. 당시에는 종묘에 화재가 일어나면 나라의 존립 자체가 위험하다고 생각했기 때문에 왕은 종묘를 중요하게 생각했고 화재 대책에 만전을 기울였습니다. ", "playTime": "123", "audioUrl": "", "langCode": "ko", "imageUrl": "", "createdtime": "20230725122153", "modifiedtime": "20230725122154"}
```

**TripCraft 활용 포인트**: 위치 기반 오디오 스토리 탐색. 사용자 주변 오디오 가이드 자동 추천.

---

### 3.4 `storySearchList`

**용도**: 오디오 스토리 검색 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Odii/storySearchList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&langCode=ko&keyword=%EA%B2%BD%EB%B3%B5%EA%B6%81
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
| `tid` | tid | code | 2573 | - |
| `tlid` | tlid | code | 2573 | - |
| `stid` | stid | code | 5378 | - |
| `stlid` | stlid | code | 16376 | - |
| `title` | 관광지명 | string | 경복궁 | - |
| `mapX` | 경도 | coord | 126.976952 | - |
| `mapY` | 위도 | coord | 37.5806736 | - |
| `audioTitle` | 오디오 제목 | string | 경복궁 | - |
| `script` | script | string |  경복궁은 조선을 건국한 태조 이성계가 현재의 서울, 한양으로 천도를 결정하면서 건설한 조선왕조 최초의 궁궐 | - |
| `playTime` | playTime | datetime | 172 | - |
| `audioUrl` | 오디오 URL | url | https://sfj608538-sfj608538.ktcdn.co.kr/file/audio/56/16086. | - |
| `langCode` | 언어코드 | code | ko | - |
| `imageUrl` | imageUrl | url | https://sfj608538-sfj608538.ktcdn.co.kr/file/image/service/1 | - |
| `createdtime` | 등록일시 | datetime | 20230725102115 | - |
| `modifiedtime` | 수정일시 | datetime | 20250609093450 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"tid": "2573", "tlid": "2573", "stid": "5378", "stlid": "16376", "title": "경복궁", "mapX": "126.976952", "mapY": "37.5806736", "audioTitle": "경복궁", "script": " 경복궁은 조선을 건국한 태조 이성계가 현재의 서울, 한양으로 천도를 결정하면서 건설한 조선왕조 최초의 궁궐입니다. 임금이 사는 궁궐들 가운데 가장 으뜸이 되는 궁궐을 법궁이라고 하는데 경복궁은 조선왕조 최초이자 제일의 법궁입니다. 경복궁은 태조 이성계를 도와 조선을 세운 정도전이 붙인 이름으로‘새 왕조가 큰 복을 누려 번영할 것’이라는 뜻이 담겨 있어요.    경복궁은 조선의 으뜸 궁궐답게 짓는 기간이 길었습니다. 처음에는 꼭 필요한 건물만 짓고 사용했지만, 이후 지속적으로 늘리거나 고쳐지어 법궁의 모습을 완성해 나가기까지 무려 30여 년이라는 시간이 걸렸지요. 경복궁은 조선 왕조와 더불어 여러 번의 시련을 겪었습니다. 1592년 임진왜란으로 인해 주요 전각이 대부분 사라질 정도로 큰 피해를 입었고, 이후 300여 년 가까이 방치되었습니다. 1865년 흥선대원군 때가 되어서야 다시 지어질 수 있었죠. 그러나 일제에 의해 명성왕후가 시해되는 을미사변과 이로 인해 고종 임금이 러시아 공사관으로 피신을 가게 되어 경복궁은 한동안 주인을 잃은 빈 궁궐이 되기도 했습니다. 대한제국이 망하고 일제에 의해 경복궁은 많이 훼손되어 광화문이 옮겨지고 궐내각사가 철거되었으며, 특히 조선총독부 건물이 세워짐으로써 경복궁을 가리게 되어 버렸습니다. 때문에 많은 건물이 기존의 모습을 잃어버렸지만 이후 복원 사업이 계속된 덕분에, 궁궐의 위엄과 당당함은 지금도 느낄 수 있답니다.   경복궁은 정문인 광화문부터 왕의 침실인 강녕전, 왕비의 침실인 교태전까지 일직선을 이루고 있습니다. 광화문과 근정전을 잇는 일직선상의 길은 왕이 다니는 길이라고 하여‘어도’라고 불렀으며, 기하하적 질서에 따라 대칭적으로 건축되었습니다. 왕의 위엄과 질서를 잘 느낄 수 있지요. 그러나 중심부를 제외한 건축물들은 비대칭적으로 배치되어 변화와 통일의 아름다움을 함께 갖추고 있습니다.   우리의 역사와 아름다움이 깃든 경복궁의 구석구석을 살펴보며 격조 높은 조선 왕실 문화를 느껴 보시는 건 어떨까요? 수문장 교대 의식과 경회루 특별 관람도 진행하고 있으니 함께 관람하는 것을 추천드립니다. ", "playTime": "172", "audioUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/audio/56/16086.mp3", "langCode": "ko", "imageUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/image/service/11143.jpg", "createdtime": "20230725102115", "modifiedtime": "20250609093450"}
{"tid": "2573", "tlid": "2573", "stid": "5380", "stlid": "16378", "title": "경복궁 영제교", "mapX": "126.976846", "mapY": "37.576608", "audioTitle": "근정전으로 가는 다리", "script": "[김내관] 조선의 궁궐은 풍수지리, 음양오행 등 도교와 유교적 사상을 현실에 구현한 건축물입니다. 경복궁도 역시 풍수지리와 음양오행을 바탕으로 건축되었습니다. 경복궁의 중심 건물인 근정전으로 가기 위해서는 세 개의 문과 금천(錦川)을 반드시 지나가야 하는데, 금천을 건너가기 위한 다리가 바로 ‘영제교(永濟橋)’입니다.   예로부터 풍수지리적으로 좋은 집터는 ‘배산임수(背山臨水)’라 하여 뒤에 산을 두고 앞에 물을 둔 곳이 명당이라 했습니다. 산은 적을 막고 땔감과 먹을 것을 구할 수 있었고, 겨울에는 추운 바람을 막아주었기 때문에, 집 뒤에 두었습니다. 물은 나쁜 기운을 막고, 깨끗하게 씻어내는 정화의 의미가 있었습니다. 왕실 가족이 실제로 살고 있는 근정전과 내전을 집이라고 생각하면, 금천을 두어 배산임수의 효과를 낸 것이지요.  [김상궁] “저기, 김내관! 저 금천 벽에 있는 건 뭔가요? 무슨 동물같이 생겼는데요??”  [김내관] “바로 상상의 동물인 천록(天禄)이지요! 나쁜 기운이 들어오지 못하게 지켜보면서 궁궐과 왕을 수호하는 역할을 한답니다. 다리 난간 위에 있는 건 ‘서수(瑞獸)’라고 해서, 조선시대 상상의 동물들을 가리키는 말인데, 서수의 역할도 잡귀나 사악한 것을 물리쳐 법궁을 지키는 것이에요.”   [김상궁] “들어오는 다리부터 상상의 동물들이 눈을 부릅뜨고 지키고 있으니, 정말 나쁜 기운은 들어오지도 못하겠네요.”  [김내관] “이 영제교는 태조전하 때 처음 지었어요. 하지만 우리가 지나는 이 다리는 2000년대 복원공사를 진행하면서, 기존에 남아있는 영제교의 부재를 활용해 만든 것이에요. 영제교라는 이름도 세종 전하 때 집현전의 학자들이 지었는데, ‘깨끗한 물에 마음을 씻고, 백성을 편안하게 하여 태평성대를 이뤄보자~’고 생각하며 지나가라는 깊은 뜻이 있습니다.“  [김상궁] “우와- 다리를 지나며 깨끗해진 마음으로 입궐을 하는 것이니, 산뜻한 출발이네요!”  [김내관] “그렇지요, 그 기분을 가득 안고 안으로 더 들어가봐요!” ", "playTime": "156", "audioUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/audio/56/7075.mp3", "langCode": "ko", "imageUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/image/service/5355.jpg", "createdtime": "20230725103211", "modifiedtime": "20250609094144"}
{"tid": "2573", "tlid": "2573", "stid": "5381", "stlid": "16379", "title": "경복궁 근정문", "mapX": "126.976929", "mapY": "37.577715", "audioTitle": "경복궁 3문의 마지막", "script": "[김내관] 경복궁의 정전은 근정전으로, 광화문, 흥례문을 지나 근정문을 통과해야만 갈 수 있습니다. 그렇지만, 조선시대의 근정문은 항상 닫혀있는 문이었는데, 왕실가족과 중국(명나라, 청나라)사신 외에는 지나갈 수 없었기 때문입니다. 그래서 신하들이 조회를 위해 올 때는 근정문 왼쪽에 있는 작은 문을 이용해서 드나들었습니다. 근정문은 근정전에서 이뤄지는 국가와 왕실의 큰 행사를 위한 장소였는데, 외국의 사신이 오거나, 왕의 즉위식, 결혼식 등이 이뤄지는 중요한 장소였습니다.   [김상궁] “오늘은 왕세자께서 용상에 오르시는 중요한 날이지요!”  [김내관] “조선의 경사지요! 이제 곧 근정문 앞에서 서시면, 신하들과 백성들에게 자신의 의지가 담긴 글과 하실 일을 말씀해 주실거에요!.”  [김상궁] “근데 너무 멀어서 그런지 내용이 잘 안 들려요. 김내관은 교지 만들 때 미리 봤으니까, 내용 좀 말해줘봐요”  [김내관] “어차피 공표될 것, 제가 요약을 하자면! 오늘부로 억울한 죄인들을 분별해서 풀어주고, 관직에 있는 자들은 한 품계씩 올려주고, 백성들에게 곡식을 나눠주신다는 내용이에요. 또 신하들이 마음을 합해 임금님을 도와 조상님들을 욕보이지 않게 하고, 나라를 길이 보존하게 하라는 내용도 있답니다.”  [김상궁] “우와! 임금님이 즉위하는 날에는 곡식도 주고, 죄인도 풀어주고, 관직 품계도 올라가는 정말 좋은 날이었네요.!”  [김내관] “그렇지요. 이 근정문에서 즉위하신 조선의 왕은 총 네 분이 있는데, 모두 이러한 내용을 담은 교서를 반포하셨어요. 근정문은 새로운 임금의 시대가 시작된다는 것을 알려주는 매우 중요한 장소였지요.” ", "playTime": "131", "audioUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/audio/56/7076.mp3", "langCode": "ko", "imageUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/image/service/5358.jpg", "createdtime": "20230725103458", "modifiedtime": "20250609095157"}
```

**TripCraft 활용 포인트**: 오디오 스토리 검색. 특정 관광지 스토리 조회.

---

### 3.5 `themeBasedList`

**용도**: 오디오 테마 지역기반 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Odii/themeBasedList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&langCode=ko
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
| langCode | - | 필수 | string | - | 대문자: KO/EN/JA/ZH |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `tid` | tid | code | 1 | - |
| `tlid` | tlid | code | 1 | - |
| `themeCategory` | themeCategory | string | 백제역사여행 | - |
| `addr1` | 주소 | string | 충청남도 | - |
| `addr2` | 상세주소 | string | 부여군 | - |
| `title` | 관광지명 | string | 백제문화단지 | - |
| `mapX` | 경도 | coord | 126.905507 | - |
| `mapY` | 위도 | coord | 36.306984 | - |
| `langCheck` | langCheck | number | 11110 | - |
| `langCode` | 언어코드 | code | ko | - |
| `imageUrl` | imageUrl | url |  | - |
| `createdtime` | 등록일시 | datetime | 20190923193941 | - |
| `modifiedtime` | 수정일시 | datetime | 20241206125533 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"tid": "1", "tlid": "1", "themeCategory": "백제역사여행", "addr1": "충청남도", "addr2": "부여군", "title": "백제문화단지", "mapX": "126.905507", "mapY": "36.306984", "langCheck": "11110", "langCode": "ko", "imageUrl": "", "createdtime": "20190923193941", "modifiedtime": "20241206125533"}
{"tid": "2", "tlid": "5", "themeCategory": "신라역사여행", "addr1": "경상북도", "addr2": "경주시", "title": "경주 불국사", "mapX": "129.332099", "mapY": "35.790122", "langCheck": "11111", "langCode": "ko", "imageUrl": "", "createdtime": "20190923194000", "modifiedtime": "20250609183759"}
{"tid": "4", "tlid": "13", "themeCategory": "신라역사여행", "addr1": "경상북도", "addr2": "경주시", "title": "괘릉", "mapX": "129.320083", "mapY": "35.759648", "langCheck": "11110", "langCode": "ko", "imageUrl": "", "createdtime": "20190923194001", "modifiedtime": "20200921110253"}
```

**TripCraft 활용 포인트**: 테마별 오디오 가이드 목록. 테마 여행 코스에 오디오 가이드 연결.

---

### 3.6 `themeBasedSyncList`

**용도**: 오디오 테마 동기화 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Odii/themeBasedSyncList?MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&serviceKey=${SERVICE_KEY}
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

> ⚠️ 수집 시 데이터 없음 (필수 파라미터 미충족 또는 결과 없음)

**응답 예시 (최대 3건 발췌)**:

> 샘플 없음

**TripCraft 활용 포인트**: TripCraft 오디오 테마 동기화 목록 조회 기능에 활용.

---

### 3.7 `themeLocationBasedList`

**용도**: 오디오 테마 위치기반 목록 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Odii/themeLocationBasedList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&langCode=ko&mapX=126.9779692&mapY=37.566535&radius=5000
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
| langCode | - | 필수 | string | - | - |

**응답 필드**:

| 필드명 | 한글명 | 타입 | 예시 값 | 설명/용도 |
|--------|--------|------|---------|-----------|
| `tid` | tid | code | 43 | - |
| `tlid` | tlid | code | 135 | - |
| `themeCategory` | themeCategory | string | 조선역사여행 | - |
| `addr1` | 주소 | string | 서울 | - |
| `addr2` | 상세주소 | string | 종로구 | - |
| `title` | 관광지명 | string | 종묘 | - |
| `mapX` | 경도 | coord | 126.994611 | - |
| `mapY` | 위도 | coord | 37.572056 | - |
| `langCheck` | langCheck | number | 11111 | - |
| `langCode` | 언어코드 | code | ko | - |
| `imageUrl` | imageUrl | url |  | - |
| `createdtime` | 등록일시 | datetime | 20190923194007 | - |
| `modifiedtime` | 수정일시 | datetime | 20250609195754 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"tid": "43", "tlid": "135", "themeCategory": "조선역사여행", "addr1": "서울", "addr2": "종로구", "title": "종묘", "mapX": "126.994611", "mapY": "37.572056", "langCheck": "11111", "langCode": "ko", "imageUrl": "", "createdtime": "20190923194007", "modifiedtime": "20250609195754"}
{"tid": "47", "tlid": "151", "themeCategory": "박물관", "addr1": "서울", "addr2": "용산구", "title": "국립중앙박물관", "mapX": "126.980477", "mapY": "37.524024", "langCheck": "11000", "langCode": "ko", "imageUrl": "", "createdtime": "20190923194008", "modifiedtime": "20240904114345"}
{"tid": "52", "tlid": "164", "themeCategory": "", "addr1": "서울", "addr2": "종로구", "title": "청계광장", "mapX": "126.977909", "mapY": "37.569235", "langCheck": "11110", "langCode": "ko", "imageUrl": "", "createdtime": "20190923194009", "modifiedtime": "20250221145953"}
```

**TripCraft 활용 포인트**: 위치 기반 오디오 테마 탐색.

---

### 3.8 `themeSearchList`

**용도**: 오디오 테마 검색 조회

**호출 URL**:
```
https://apis.data.go.kr/B551011/Odii/themeSearchList?serviceKey=${SERVICE_KEY}&MobileOS=ETC&MobileApp=TripCraftKorea&_type=json&numOfRows=5&pageNo=1&langCode=ko&keyword=%EA%B2%BD%EB%B3%B5%EA%B6%81
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
| `tid` | tid | code | 2573 | - |
| `tlid` | tlid | code | 2573 | - |
| `themeCategory` | themeCategory | string |  | - |
| `addr1` | 주소 | string | 서울 | - |
| `addr2` | 상세주소 | string | 종로구 | - |
| `title` | 관광지명 | string | 경복궁 | - |
| `mapX` | 경도 | coord | 126.977041 | - |
| `mapY` | 위도 | coord | 37.579651 | - |
| `langCheck` | langCheck | number | 11111 | - |
| `langCode` | 언어코드 | code | ko | - |
| `imageUrl` | imageUrl | url |  | - |
| `createdtime` | 등록일시 | datetime | 20191108125351 | - |
| `modifiedtime` | 수정일시 | datetime | 20250609173523 | - |

**응답 예시 (최대 3건 발췌)**:

```json
{"tid": "2573", "tlid": "2573", "themeCategory": "", "addr1": "서울", "addr2": "종로구", "title": "경복궁", "mapX": "126.977041", "mapY": "37.579651", "langCheck": "11111", "langCode": "ko", "imageUrl": "", "createdtime": "20191108125351", "modifiedtime": "20250609173523"}
{"tid": "3375", "tlid": "5093", "themeCategory": "", "addr1": "서울", "addr2": "종로구", "title": "경복궁(고궁 스토리텔링)", "mapX": "126.97704", "mapY": "37.579617", "langCheck": "10000", "langCode": "ko", "imageUrl": "https://sfj608538-sfj608538.ktcdn.co.kr/file/sightImage/service/3375.jpg", "createdtime": "20240125120046", "modifiedtime": "20240125120100"}
```

**TripCraft 활용 포인트**: 오디오 테마 검색.

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

