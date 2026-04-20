# Topic Layout Migration

## 目的

旧 `PSP_*` 章構成を教育用途向けの英語スラッグへ統一し、トピック単位で次の4分類に整理します。

- `examples/`
- `slides/`
- `data/`
- `notebooks/`

また、`.eps/.emf/.svg` 図版はコードから分離し、`docs/references/figures/`（必要時は `<topic-slug>/slides/assets/`）へ集約します。

## Directory rename (`PSP_*` -> educational slug)

| Legacy chapter | New topic slug |
| --- | --- |
| `PSP_MillerMiller` | `miller-miller` |
| `PSP_Poiseuille` | `poiseuille` |
| `PSP_gasDiffusion` | `gas-diffusion` |
| `PSP_travelTimeAnalysis` | `travel-time-analysis` |
| `PSP_unsaturatedConductivity` | `unsaturated-conductivity` |
| `PSP_waterRetentionFitting` | `water-retention-fitting` |

課題・Notebook由来のファイルは次へ移設済みです。

- `PSP_exercise2_2.py` -> `exercise-2-2/examples/`
- `PSP_exercise2_3.py` -> `exercise-2-3/examples/`
- `PSP_exercises2_7.ipynb` -> `exercises-2-7/notebooks/`
- `PSP_sedimentation.ipynb` -> `sedimentation/notebooks/`

## Topic-internal layout

各トピックディレクトリは次の形を基準にします（必要なもののみ配置）。

- `examples/`: Pythonスクリプト・実装例
- `slides/`: 講義スライド・配布PDF
- `data/`: `.txt` / `.dat` 等の入力データ
- `notebooks/`: Jupyter Notebook

## Figure asset policy

図版アセットは以下に集約します。

- `docs/references/figures/<topic-slug>/`
- （スライド専用素材のみ）`<topic-slug>/slides/assets/`

上記により、実行コードと図版の責務分離を維持します。
