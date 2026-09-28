# Preprocess Scheme — 나무위키 전처리 계획과 Context Window 문제

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../../README.md) › [Project](../../../README.md) › [NLP](../../README.md) › [Notes](../README.md) › [Work log](README.md) › **Preprocess scheme**</sub>

> [!NOTE]
> Kanban card · **Owner:** 강민재 · **Tag:** Data · **Status at archive time:** 개발 중 (superseded by the PDF-upload approach) · **Started:** 2023-12-18
> Converted from the team Notion board and kept in the original Korean.

### 업무 내용

#### 나무위키 크롤링 데이터 전처리 계획

1. 나무위키의 배우 또는 가수 목록 문서를 사용
2. 각 배우에 대한 문서를 순회하며 ToC의 제목들을 수집
3. Python Counter를 사용하여 title DB를 생성
4. 이후 임의의 인물에 대한 입력이 들어왔을 때 DB를 참고하여 타이틀이 존재하면 크롤링, 존재하지 않으면 중요도가 낮은 것으로 간주하여 스킵
5. 테이블 데이터에 대한 파싱 계획이 필요함

#### RAG와 Context Window 문제

GPT 3.5는 4k, GPT4는 8k/32k의 context window를 가짐

대부분의 실험은 우선 GPT 3.5를 사용해서 수행하고 이후 GPT4에 대한 scalability test만 진행해야 할 것으로 보임 (비용 문제)

비용 문제를 제외하더라도 context window 때문에 프롬프트에 포함할 수 있는 문서 요약본의 길이가 제한될 것임

`tiktoken` [패키지](https://github.com/openai/tiktoken)를 사용하여 프롬프트 길이에 대한 분석이 선행되어야 할 듯


---
<sub>[← Work log](README.md) · [Notes index](../README.md) · [💬 Persona chatbot project](../../README.md)</sub>
