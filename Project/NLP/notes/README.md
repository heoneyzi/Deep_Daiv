<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../README.md) › [Project](../../README.md) › [NLP](../README.md) › **Notes**</sub>

# 🗒️ Persona chatbot — Notion archive

The team's Notion workspace for the persona chatbot (deep daiv. NLP Transformer team 2 **"자양강장제"**: 강민재 · 강지헌 (Team Lead) · 장래영 · 장윤경), converted to Markdown and **kept in the original Korean**. Each page carries a short English note on who wrote it and what was changed for the public copy.

> [!NOTE]
> Curation: the duplicate copy of this workspace under *WIL › NLP 논문 › 프롬프트 프로젝트* was skipped; so were an earlier draft of the final report, the empty collaboration-rules page, the bookmark-only resource page, and setup/tooling cards (virtual-env notes, GitHub/Notion setup, API-key sharing, a Streamlit tutorial copy, attachment-only cards).

## 📚 Team documents

| # | Page | What it is |
|---|---|---|
| 01 | [프로젝트 정리 — 내가 좋아하는 배우와 일상을 공유한다면?](01_project_writeup.md) | Blog-style final write-up: fine-tuning vs prompting, in-context learning, CoT, prompt patterns, how the chatbot works, prompt evolution, results |
| 02 | [결과보고서](02_final_report.md) | Formal final report: motivation, architecture and user scenario, data, RAG, Assistants API, results, significance and limits |
| 03 | [팀 세미나 보고서](03_midterm_seminar_report.md) | Mid-term seminar: paper study (InstructGPT, GPT-4, LoRA, QLoRA, CoT, ReAct) and the project plan |
| 04 | [주차별 계획](04_weekly_plan.md) | Weeks 5–9 plan with the checkboxes as they stood |

## 🧪 Work log (Kanban cards) → [worklog/](worklog/README.md)

| Card | Owner | Why it is here |
|---|---|---|
| [PoC](worklog/01_poc.md) | 강민재 | Feasibility test in ChatGPT that motivated few-shot lines |
| [나무위키 크롤링](worklog/02_namuwiki_crawling.md) · [Preprocess Scheme](worklog/03_preprocess_scheme.md) | 강민재 | The original crawl-and-parse plan, later replaced by PDF upload |
| [〈더 글로리〉 박연진 페르소나](worklog/04_persona_park_yeonjin.md) | **강지헌** | Jiheon's prompt iteration log |
| [〈응답하라 1988〉 성동일 페르소나](worklog/05_persona_sung_dongil.md) | 장윤경 | Parallel prompt experiments on a second character |
| [프롬프트 정리](worklog/06_prompt_comparison.md) | not recorded | Final prompt × character lines comparison |
| [날짜 · 날씨 · 뉴스 정보 입력](worklog/07_date_weather_news.md) | 장윤경 | Real-time context injection |
| [Final TODOs](worklog/08_final_todos.md) · [데모 포스터 피드백](worklog/09_demo_poster_feedback.md) | not recorded | Pre-demo checklist and poster wording |

## Decision log

Condensed from the [meeting notes](meetings/README.md) (dates are meeting dates).

| Date | Decision / finding |
|---|---|
| 2023-12-05 | Namuwiki tables of contents differ per person; long documents in the prompt already produced off-target answers → need a selection rule for sections |
| 2023-12-07 | Milestones for weeks 5–9; GitHub/Notion conventions; persona-style data (personality, habits, speech) identified as the missing ingredient |
| 2023-12-15 | Crawler done; idea of a small initial profile plus ReAct-style lookup of the relevant section per question; scope fixed to RAG + prompt engineering, no model tuning |
| 2023-12-19 | Word-frequency importance would drop famous but rare topics; check whether the GPT API can reference documents directly; multi-turn memory |
| 2023-12-22 | 90% of section titles occur only once → try noun frequencies instead |
| 2023-12-27 | **Pivot:** upload the Namuwiki page as a PDF to an OpenAI Assistant; the crawler may be unnecessary; focus on prompt engineering |
| 2023-12-29 | Assistant API implementation done; Streamlit demo next; grounding check with 송강's page works (peach allergy), speech style not yet |
| 2024-01-03 | Rehearsal feedback: explain why prompting over fine-tuning, show the prompt trial-and-error; the date/location context was praised |

## 📖 Study notes → [wil/](wil/README.md)

Jiheon's own *What I Learned* notes from the same period: RAG, Mistral 7B, Seq2seq, WaveNet and an AI glossary.

---
<sub>[← Persona chatbot project](../README.md) · [🏠 Portfolio](https://github.com/heoneyzi)</sub>
