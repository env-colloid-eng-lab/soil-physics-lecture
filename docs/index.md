# Soil Physics Lecture Hub

このリポジトリでできること
- 講義資料をトピック別にたどって学習できます。
- 演習・課題の素材を確認し、進行に合わせて取り組めます。
- コード（Python / Notebook）を使って計算・可視化を再現できます。

## 目次
- [授業概要](#授業概要)
- [講義一覧](#講義一覧)
- [課題一覧](#課題一覧)
- [コード](#コード)
- [Notebook](#notebook)
- [更新履歴](#更新履歴)

## 授業概要
土壌物理学の授業で使う資料・演習・課題・コードを、トピック単位のディレクトリで管理しています。

### Quick Start（受講者向け）
- 閲覧のみ: GitHub上で各トピックの `slides/`、`data/` と、リポジトリ直下の `docs/references/` を参照。
- ローカル実行:
  1. `git clone <this-repo-url>`
  2. `cd soil-physics-lecture`
  3. 各トピックの `examples/` または `notebooks/` を実行。

## 講義一覧
- `miller-miller/`
- `poiseuille/`
- `gas-diffusion/`
- `travel-time-analysis/`
- `unsaturated-conductivity/`
- `water-retention-fitting/`
- `sedimentation/`

## 課題一覧
- `exercise-2-2/`
- `exercise-2-3/`
- `exercises-2-7/`

## コード
- Python実装例: 各トピックの `examples/`
- 入力データ: 各トピックの `data/`
- 図版参照: `docs/references/figures/`

## Notebook
- Jupyter Notebook: 各トピックの `notebooks/`

## 更新履歴
### 旧名からの移行注記
旧プロジェクト名は **SoilPhysPy** です。既存の参照・検索互換のため、名称を明示的に残しています。

### ディレクトリ移行ルール（PSP系章構成）
- 章ディレクトリは英語スラッグで管理（例: `PSP_travelTimeAnalysis` -> `travel-time-analysis`）。
- トピック内コンテンツは `examples/`, `slides/`, `data/`, `notebooks/` へ整理。
- `.eps/.emf/.svg` は `docs/references/figures/`（または `slides/assets/`）へ集約し、コードと分離。
