<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../../README.md) › [Project](../../../README.md) › [R.S](../../README.md) › [Code](../README.md) › **demo**</sub>

# demo/ — Streamlit prototype

[`demo.py`](demo.py) — Korean interface: rate six seed venues (별로예요 2.0 · 괜찮아요 3.5 · 꼭 가고 싶어요 5.0) → choose one of four recommended restaurants → choose one of four cafés in the same area group → see both venues with address and link. It initialises an **untrained** MF model (stated in the UI), so rankings are illustrative.

Run from the parent `code/` folder after `python -m taste_trip.check_data --workflow demo`: `python -m streamlit run demo/demo.py`.
