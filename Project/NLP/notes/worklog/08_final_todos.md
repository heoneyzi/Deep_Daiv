# Final TODOs — 데모 전 마무리 작업

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../../README.md) › [Project](../../../README.md) › [NLP](../../README.md) › [Notes](../README.md) › [Work log](README.md) › **Final TODOs**</sub>

> [!NOTE]
> Kanban card · **Owner:** not recorded · **Tag:** Research · **Status at archive time:** 개발 중 (in progress)
> Converted from the team Notion board and kept in the original Korean.

### 업무 내용

- [x] Streamlit 데모 구현 (Assistant api 연결)
    - [ ] 파일 업로드 구현
- [x] 멀티턴 구현 (Assistant에서 자체적으로 수행하는 것으로 확인)
- [ ] 사용자 입장에서 동명이인 처리
- [ ] 대사 수집 자동화
- [ ] 논문에서 근거 찾아보기
    - [x] Prompt Ensemble
    - [x] Contrastive Chain of thought
- [ ] 코드 리팩토링 (가능하면)
- [x] 날짜, 날씨, 뉴스 정보 api를 통해 가져오기

#### 💡 코드 관련

코드 관련해서는 구현 근거만 있다면 향후 발전 방향으로 제시해도 될 것 같음

1. 날짜, 날씨, 뉴스 정보
- [케이웨더 api](https://weather.joins.com/apiguide/present.html)를 사용해서 `time` 모듈로 받아온 날짜에 대한 날씨 정보를 instruction에 포함
- 네이버 개발자 포털에서 제공하는 [뉴스 검색 api](https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4-%EA%B2%80%EC%83%89-api-%EB%A0%88%ED%8D%BC%EB%9F%B0%EC%8A%A4)를 사용하여 최근 뉴스에 대한 정보를 제공

> 💡 **구현을 통해 보여줘야 하는 내용<br>**<br>코드를 통해 날짜, 날씨, 뉴스 정보를 제공하진 않더라도, 해당 내용을 instruction에 포함한 후 유의미한 결과를 내는지는 확인 필요

→ [날짜, 날씨,뉴스 정보 입력](07_date_weather_news.md)

1. 매번 대화에 RAG 기반 응답 생성
- Query와 Document(나무위키 문서의 각 문단)의 TF-IDF 또는 dense representation의 유사도를 바탕으로 document를 query 앞에 붙여서 프롬프트로 사용하는 방식
    - TF-IDF의 경우 exact match를 기반으로 하기 때문에 threshold를 설정하여 유사도가 임곗값을 넘을 경우에만 document를 제시

> 💡 **구현을 통해 보여줘야 하는 내용<br>**<br>사용자의 입력과 관련이 있을 거라고 판단되는 나무위키 문서 일부를 입력하고 결과가 유의미하게 변하는지 확인 필요<br><br>ex) 아저씨 요새도 주식 하세요?<br><br>성동일(응답하라1988) 문서 중에서 ’2.16 16화’ 부분을 프롬프트에 포함한 후 이게 있을 때랑 없을 때 응답이 어떻게 달라지는지 확인하기

1. 사용자 입장에서 동명이인 처리
    - 개발 단계에서는 동명이인이 존재할 경우 직접 나무위키 url을 추가하도록 되어 있음
    - Chat Demo에서는 나무위키 개요 일부를 제시한 후 둘 중 한 누구를 선택할 지 질의를 주고 받은 후 사용자 응답에서 개체명 인식을 통해 인물을 특정할 수 있음

    > 💡 **구현을 통해 보여줘야 하는 내용<br>**<br>[대한민국 배우 목록 문서](https://namu.wiki/w/%EB%B0%B0%EC%9A%B0/%ED%95%9C%EA%B5%AD)를 보면 중복되는 이름이 꽤 있는데, 이 중에서 중복되는 이름 아무나 선택한 다음 유저가 고르는 상황을 가정한 후 개체명 인식이 제대로 이루어지는지 확인하기<br><br>(이 부분은 아직 방법이 정리되지 않았는데, 좋은 의견이 떠오르면 실험해도 되고 아니면 일단 넘겨도 괜찮을 듯)


---
<sub>[← Work log](README.md) · [Notes index](../README.md) · [💬 Persona chatbot project](../../README.md)</sub>
