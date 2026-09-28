<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../README.md) › [Project](../../README.md) › [NLP](../README.md) › **Code**</sub>

# 💻 Code snapshot — persona chatbot (OpenAI Assistants API + Streamlit)

> **Question —** how little code does a retrieval-grounded persona chatbot need when the LLM provider hosts retrieval?

| | |
|---|---|
| **Status** | ✅ final team code (Jan 2024) |
| **Provenance** | [heoneyzi/prompted_celebrity](https://github.com/heoneyzi/prompted_celebrity), `code/` at commit `9987bda` ("feat: add project files", 2024-01-04), committed by teammate **강민재 (MinJae Kang)** · copied unchanged |
| **Model / API** | OpenAI Assistants API (beta, late 2023) · `gpt-4-1106-preview` (commented alternative `gpt-3.5-turbo-1106`) · `retrieval` tool over uploaded files |
| **Data** | not included — the person's Namuwiki page as PDF, an optional script `.txt`, `data/actors_list.csv` |

## Files

| File | What it is |
|---|---|
| [`assistant.py`](assistant.py) | `ChatAssistant`: list / create / retrieve an assistant per person, upload the PDF (+ script), one thread per chat, `get_answers()` polls a run until completed, `revise_instructions()` swaps the persona prompt between experiments |
| [`chat.py`](chat.py) | Streamlit chat front end (`st.chat_input`, message history in session state) for one persona (성동일 in the snapshot) |
| [`utils.py`](utils.py) | Fernet encryption/decryption of the API key file, actor-list lookup with a namesake warning, Namuwiki page → PDF via `pyhtml2pdf` |
| [`openai_pdf_api_test_revised.ipynb`](openai_pdf_api_test_revised.ipynb) | Experiment notebook used for prompt testing: pick a person, create the assistant, revise instructions, chat in a loop, save Q/A pairs to CSV (no stored outputs) |

## Run

```bash
python -m pip install openai streamlit pandas cryptography pyhtml2pdf tqdm
# api.txt (same folder): line 1 = base64-encoded Fernet key, line 2 = Fernet-encrypted OpenAI API key
streamlit run chat.py
```

## Known limitations (kept as in the source)

- Written for the **late-2023 beta Assistants API** (`client.beta.assistants`, `tools=[{"type": "retrieval"}]`, `file_ids`); later API versions changed these interfaces, so the code may not run unchanged today.
- `ChatAssistant.change_file()` calls an undefined `self._delete(...)` when both a PDF and a script are replaced (the helper is `_delete_file`), and `decrypt_api_key()` always reads `api.txt` regardless of its argument.
- No tests, no evaluation script — the team evaluated personas by reading chats (see the [project README](../README.md)).

No license file was present in the source repository; the code is reproduced here with attribution as part of the team-project record.

---
<sub>[← Persona chatbot project](../README.md) · [Notes](../notes/README.md) · [🏠 Portfolio](https://github.com/heoneyzi)</sub>
