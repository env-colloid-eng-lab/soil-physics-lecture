# Topic Layout Migration

## Directory rename (PSP chapter name -> educational slug)

- `PSP_MillerMiller` -> `miller-miller`
- `PSP_Poiseuille` -> `poiseuille`
- `PSP_gasDiffusion` -> `gas-diffusion`
- `PSP_travelTimeAnalysis` -> `travel-time-analysis`
- `PSP_unsaturatedConductivity` -> `unsaturated-conductivity`
- `PSP_waterRetentionFitting` -> `water-retention-fitting`
- `PSP_exercise2_2.py` -> `exercise-2-2/examples/`
- `PSP_exercise2_3.py` -> `exercise-2-3/examples/`
- `PSP_exercises2_7.ipynb` -> `exercises-2-7/notebooks/`
- `PSP_sedimentation.ipynb` -> `sedimentation/notebooks/`

## Topic-internal layout

Each topic directory now follows this shape:

- `examples/` for Python scripts and example code
- `slides/` for PDF handouts/slides
- `data/` for `.txt` / `.dat` datasets
- `notebooks/` for Jupyter notebooks

## Figure asset policy

All `.eps`, `.emf`, `.svg` files are consolidated under:

- `docs/references/figures/<topic-slug>/`

This separates figure assets from executable code and data.
