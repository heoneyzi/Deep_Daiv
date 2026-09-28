# 주차별 계획 — Weeks 5–9

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../README.md) › [Project](../../README.md) › [NLP](../README.md) › [Notes](README.md) › **Weekly plan**</sub>

> [!NOTE]
> Team document of deep daiv. NLP Transformer team 2 **"자양강장제"** (강민재 · 강지헌 (Team Lead) · 장래영 · 장윤경), converted from the team's Notion workspace and kept in the original Korean.

*Week-by-week plan of the project phase (checkboxes as they stood when the workspace was archived).*

#### 5주차 (\~12.08)

- [x] PoC
- ChatGPT를 활용하여 프로젝트 실현 가능성 검증
- [x] 데이터 명세
- 나무위키 데이터
- SNS 데이터
- [ ] 데이터 전처리 방법 정의
- 나무위키 문서 중 어떤 부분을 사용할 것인지
    - [ ] 어떤 문서의 참조 문서를 함께 사용할 것인지 (배경 지식 증강)
    - [ ] 동명이인 처리 방법
- [ ] SNS 데이터 중 필요한 것을 어떻게 필터링할 것인지

크롤링 코드 구현

- [x] 나무위키 크롤링
- [ ] 인스타그램, X 크롤링

#### 6주차 (\~12.15)

RAG 파이프라인 구축

- 수집한 데이터를 정제한 데이터를 언어 모델에 전달하는 코드 구현
- LangChain의 Web-based retriever를 참고하기

프롬프트 엔지니어링 연구

- 어떤 프롬프트를 사용해야 지시를 잘 따르게 될 지
- 일반화된 프롬프트를 자동으로 설계할 수 있는 방법

#### 7주차 (\~12.22)

프롬프트 엔지니어링 심화

- 프롬프트 설계에 대한 연구
- End tn end 파이프라인 구축

#### 8주차 (\~12.29)

모델 성능 향상

- 프롬프트 엔지니어링
- 데이터 전처리 개선

End to end 파이프라인 마무리

#### 9주차 (\~01.05)

미정

- 가능할 경우, Gradio, Streamlit등을 활용하여 간단한 웹 데모 만들기

---
<sub>[← Notes index](README.md) · [💬 Persona chatbot project](../README.md)</sub>
