<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../../README.md) › [Project](../../../README.md) › [R.S](../../README.md) › [Code](../README.md) › **model**</sub>

# model/ — recommenders

| File | What it is |
|---|---|
| [`PopRec.py`](PopRec.py) | Popularity baseline (summed scores, same top-5 for everyone) with Precision@5 / Recall@5 |
| [`Contents_Based_flitering.py`](Contents_Based_flitering.py) | Content-based ranking from word2vec tag/category vectors after six interactive ratings (known `NameError`, see [code README](../README.md#known-issues-kept-as-in-the-source)) |
| [`Matrix_Factorization.py`](Matrix_Factorization.py) | PyTorch MF, 10-d embeddings, per-user 80/20 split |
| [`model1.py`](model1.py) · [`model2.py`](model2.py) · [`model3.py`](model3.py) | Hybrid experiments (CBF → MF, MF → CBF, weighted sum); evaluation currently scores MF only |

Run from the parent `code/` folder, e.g. `python -m model.Matrix_Factorization`.
