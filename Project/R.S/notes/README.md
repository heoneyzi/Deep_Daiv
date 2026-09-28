<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../README.md) › [Project](../../README.md) › [R.S](../README.md) › **Notes**</sub>

# 📓 Taste Trip — study notes

Jiheon's *What I Learned* notes from the recommender-systems track (summer 2024), converted from Notion and kept in the original Korean.

| # | Note | What it covers |
|---|---|---|
| 01 | [웹 크롤링 공부](01_web_crawling_study.md) | requests / BeautifulSoup vs Selenium, headers and WebDriver; speeding up Naver Place review crawling by replacing a per-review `try/except` click with a "+"-marker check (9 min 20 s → about 4 min 20 s) |
| 02 | [웹 크롤링 코드 짜기 및 심화 공부](02_crawling_pipeline.md) | The three-stage pipeline — venue URLs → reviews and reviewers → each reviewer's history — chained through Excel files; `find_element` vs `find_elements` |
| 03 | [Wide & Deep Learning for Recommender Systems](03_wide_and_deep.md) | Paper review: memorization (wide, cross-product features) vs generalization (deep, embeddings), joint training, serving |

The crawler code in the notes targets Naver's page structure as of 2024 (CSS class names change often), and collected data is not included in this portfolio.

---
<sub>[← Taste Trip project](../README.md) · [🏠 Portfolio](https://github.com/heoneyzi)</sub>
