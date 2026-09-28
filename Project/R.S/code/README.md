<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../README.md) › [Project](../../README.md) › [R.S](../README.md) › **Code**</sub>

# 💻 Code snapshot — Taste Trip recommenders

> **Question —** which recommender family (popularity, content-based, matrix factorization, hybrid) suits a small, very sparse local-venue dataset?

| | |
|---|---|
| **Status** | ✅ research archive — code only, no data, no trained weights |
| **Provenance** | copied unchanged from [heoneyzi/Taste_Trip_Recommender-System](https://github.com/heoneyzi/Taste_Trip_Recommender-System) `main` @ `5f876f6` (2026-09-12); original code from the `jiheon` branch (Apr 2025 upload of the 2024 deep daiv. project) — see [SOURCE.md](SOURCE.md) |
| **Model / data** | PyTorch MF (10-d embeddings) · 100-d word2vec tag/category vectors (not published) · 51,705 users × 337 venues score matrix (public `jiheon` branch only) |
| **Headline** | no archived scores — Precision@5 / Recall@5 are printed at run time and were never saved |

## Setup

Run everything from this folder (`taste_trip/paths.py` resolves `data/`, `data/images/` and `outputs/` relative to it, or from `TASTE_TRIP_DATA_DIR`, `TASTE_TRIP_IMAGE_DIR`, `TASTE_TRIP_OUTPUT_DIR`).

```bash
python -m pip install -r requirements.txt
python -m taste_trip.check_data --workflow demo      # also: mf, poprec, content, hybrid, hybrid3, imputation
python -m streamlit run demo/demo.py
python -m model.Matrix_Factorization                # trains and prints Precision@5 / Recall@5
```

`check_data.py` only checks that the required files exist; the full data schema (column positions, `DEMO_USER` row, image names) is documented in the [upstream README](https://github.com/heoneyzi/Taste_Trip_Recommender-System#data-schemas-and-original-assumptions).

## Files

| File | What it is |
|---|---|
| [`model/PopRec.py`](model/PopRec.py) | Popularity baseline: rank venues by summed scores; Precision@5 / Recall@5 against a held-out matrix |
| [`model/Contents_Based_flitering.py`](model/Contents_Based_flitering.py) | Content-based ranking from tag/category vectors after six interactive ratings (original filename kept) |
| [`model/Matrix_Factorization.py`](model/Matrix_Factorization.py) | PyTorch MF with a per-user 80/20 split, 10 epochs, Adam |
| [`model/model1.py`](model/model1.py) · [`model2.py`](model/model2.py) · [`model3.py`](model/model3.py) | Hybrid experiments: CBF → MF, MF → CBF, weighted MF + CBF (per commit messages) |
| [`preprocess/imputation.py`](preprocess/imputation.py) | Similarity-based score imputation for users with 1–4 scored venues |
| [`preprocess/plotting.py`](preprocess/plotting.py) · [`preprocess.md`](preprocess/preprocess.md) | Fragment that plots tag/category similarity histograms; one-line note |
| [`demo/demo.py`](demo/demo.py) | Korean Streamlit prototype: rate six venues → pick a restaurant → pick a café in the same area → details |
| [`taste_trip/`](taste_trip/) | Portable path helpers and the prerequisite checker (added in the 2026 restoration) |
| [`requirements.txt`](requirements.txt) · [`SOURCE.md`](SOURCE.md) | Compatibility ranges (not a lockfile) · restoration and provenance notes |

## Known issues (kept as in the source)

- `Contents_Based_flitering.py` line 146 uses an undefined name `store_category` (the loaded dict is `store_category_vectors`), so the final ranking step raises `NameError`.
- `preprocess/plotting.py` expects `tag_df` / `cate_df` from an earlier notebook session.
- `model1–3.py` define the content-based / hybrid helpers, but their `evaluate_performance` calls the MF recommender only — as written they score MF, not the hybrids.
- The demo builds an **untrained** MF model (the interface says so), so its rankings are illustrative.

No license file was present in the source snapshot; the code is shown here for the portfolio record, and the upstream repository's notes on contributor and dataset rights apply.

---
<sub>[← Taste Trip project](../README.md) · [Notes](../notes/README.md) · [🏠 Portfolio](https://github.com/heoneyzi)</sub>
