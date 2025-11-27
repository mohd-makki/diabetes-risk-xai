# Milestone 4 — Model Tuning & Improvement ⚙️

## Description 📝

This milestone focuses on improving the predictive performance and robustness  
of the diabetes-risk model through systematic hyperparameter tuning,
cross-validation, and careful validation.

## Objective 🎯

The main goals are:

- Improve recall for the positive (diabetic) class while keeping precision
  and overall calibration acceptable.
- Produce a reproducible tuning workflow with artifacts, logs, and best-model  
  artifacts saved in `/models` and `/results`.
- Produce a compact, reproducible Jupyter notebook to run tuning and produce  
  figures for reports.

## What is included in Milestone 4 ✅

- `milestone4.md` — Detailed milestone write-up (objectives, method, outcomes).
- `milestone4_tuning.py` (script-style notebook) — Full top-tier tuning
  workflow (cells compatible with Jupyter/VSCode). You can rename to `.ipynb`  
  after converting.
- `tuning_log.txt` — A machine- and human-readable log of tuning runs and the  
  final chosen parameters.
- `results/` — Directory where tuning artifacts will be saved (model files,
  plots, metadata).

## How to run ▶️

1. Create and activate the project's virtual environment and install
   dependencies from `requirements.txt`.
2. From the repo root, run the notebook or the `.py` script inside  
   `milestones/milestone4_model_tuning/`.
   - In Jupyter: open `milestone4_tuning.ipynb` and run top-to-bottom.
     (Recommended: restart kernel → run all.)
   - In terminal (script mode):
     `python milestones/milestone4_model_tuning/milestone4_tuning.py` (this
     will run a non-interactive tuning and save artifacts).
3. Check `milestones/milestone4_model_tuning/results/` for the saved model,
   plots, and `tuning_log.txt`.

## Notes & best practices 🛠️

- The tuning workflow uses reproducible random seeds and stratified splits to  
  ensure stable results.
- Hyperparameter ranges are deliberately conservative to balance runtime and  
  result quality.
- in case we want to run a larger grid or Bayesian optimization, we have to
  increase the `n_iter` and expand the parameter ranges in the notebook.

## Deliverables 📦

- Tuned and evaluated ML/DL models.
- Performance comparison charts.
- Final selected model exported for deployment.

---
