<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [🤿 DeepDaiv.](../../../README.md) › [Project](../../README.md) › [Multimodal](../README.md) › **Notes**</sub>

# 🗒️ Multimodal track · study notes

Jiheon's notes from the deep daiv. multimodal track (Oct 2024 – 2025), converted from Notion and kept in their original Korean. They follow the track in order: a hallucination paper for the entry assignment, video models, composed image retrieval, and the design notes of the team's own method, FTF-VTG. Each note is a folder whose `README.md` renders on GitHub, with its figures in `assets/`.

<details>
<summary><b>🇰🇷 한국어 요약</b></summary>

deep daiv. 멀티모달 트랙에서 정리한 노트 모음입니다(원문 한국어). 트랙 과제였던 M3ID 환각 논문 리뷰, VideoMamba·TFVTG 비디오 모델 공부, Composed Image Retrieval 논문 9편, 그리고 팀 연구 FTF-VTG의 후처리·점수 설계 노트 순서로 정리했습니다. 노트 안의 그림은 리뷰한 논문에서 가져온 캡처입니다.

</details>

| # | Note | What it covers | When |
|---|---|---|---|
| 1 | [M3ID review](01_m3id_hallucination_review/README.md) | *Multi-Modal Hallucination Control by Visual Information Grounding* (CVPR 2024) — why VLMs drift from the image as captions grow (conditioning dilution), the prompt-dependency measure (PDM), and M3ID / M3ID+DPO decoding. Two versions: an easy-read walkthrough and a paper-format summary with the equations | Oct–Nov 2024 |
| 2 | [VideoMamba](02_videomamba/README.md) | State-space (Mamba) blocks as an efficient video backbone: bidirectional scanning, self-distillation, masking | Nov 2024 |
| 3 | [TFVTG review](03_tfvtg_review/README.md) | *Training-free VTG using Large-scale Pre-trained Models* (ECCV 2024): LLM query decomposition, BLIP-2 dynamic/static proposal scores, IID and OOD results — the baseline FTF-VTG simplified | Nov 2024 |
| 4 | [CIR for remote sensing](04_cir_remote_sensing/README.md) | WEICOM: training-free weighting of normalised image and text similarities, a new remote-sensing CIR benchmark, λ ablation | Dec 2024 |
| 5 | [CIR reading list](05_cir_survey/README.md) | Composed image retrieval, eight papers (below) | Dec 2024 |
| 6 | [FTF-VTG design notes](06_ftfvtg_score_design/README.md) | The team's 8-hyper-parameter post-processing and segment-scoring design (smoothing, derivative thresholds, decayed dynamic score, gap merging) | 2025 |

**CIR reading list (note 5):**

| Setting | Papers |
|---|---|
| Supervised | [CIRR / CIRPLANT](05_cir_survey/01_cirr_cirplant/README.md) · [CLIP4Cir](05_cir_survey/02_clip4cir/README.md) · [Candidate re-ranking with a dual multi-modal encoder](05_cir_survey/03_candidate_reranking/README.md) |
| Zero-shot | [Pic2Word](05_cir_survey/04_pic2word/README.md) · [iSEARLE](05_cir_survey/05_isearle/README.md) · [CompoDiff](05_cir_survey/06_compodiff/README.md) |
| Training-free | [FREEDOM](05_cir_survey/07_freedom/README.md) · [Weighted modality fusion](05_cir_survey/08_weighted_modality_fusion/README.md) |

<sub>Months come from screenshot timestamps inside the Notion pages. Figures in the notes are screenshots from the papers under review. Converted with the portfolio's Notion converter (spec: <code>multimodal_papers.json</code>); the entry assignment's application-form answers and the paper's manuscript-draft page are not included.</sub>

---
<sub>[Multimodal track](../README.md) · [🏠 Portfolio](https://github.com/heoneyzi)</sub>
