# Milestone 4 — Model Tuning & Improvement

## Objective

Enhance the baseline XGBoost model produced in Milestone 2 and analyzed in  
Milestone 3.
The tuning objective chosen: Optimize a balanced metric that emphasizes  
**recall for the positive class** while maintaining acceptable precision and  
overall AUC. This is consistent with clinical priorities for screening where  
missing positive cases is costly.

## Summary of Approach

1. **Reproducible data split**: Use the same train/test split from
   Milestone 2. Maintain scaler and preprocessing pipeline (loaded from  
   `models/scaler.joblib`).
2. **Evaluation metric**: Primary objective: `Recall` (positive class).
   Secondary: `ROC-AUC`, `Precision`, and `F1`. For final selection, use a  
   composite score that weights recall/auc.
3. **Tuning method**: Use **Bayesian optimization** via `skopt`'s  
   `BayesSearchCV` or `Optuna` (default is Optuna-style random search if  
   `optuna` not installed). For speed and reproducibility we'll include a  
   stable `RandomizedSearchCV` fallback.
4. **Pipelines**: Use `sklearn.pipeline.Pipeline` to ensure scaler + model
   are chained if needed; we reuse the saved scaler to avoid data leakage.
5. **Model candidates**: Primary — `XGBoost` (XGBClassifier). Optionally
   compare RandomForest and LogisticRegression to confirm gains.
6. **Output**: Save best model (`joblib`), tuning log (`tuning_log.txt`), and  
   plots (learning curves, partial dependence / feature importance,
   calibration curve). Save everything to
   `milestones/milestone4_model_tuning/results/`.

## Deliverables

- `milestone4_tuning.ipynb` (or `.py`) — reproducible tuning notebook
- `tuning_log.txt` — full log
- Updated `/models` with `xgb_tuned.joblib` (best model) if improvement found
- `results/` plots

## Key decisions & rationale

- **Severity-aware tuning**: Because you selected Severity Option B (discrete  
  categorical severity output), the model retains its binary target for
  tuning. Severity classification will be implemented in a downstream
  calibration/thresholding step and mapped using predicted probability
  thresholds to severity bins (Low/Moderate/High).

- **Tuning objective**: prioritizing recall reduces false negatives (missed
  diabetes cases). We apply class weighting and threshold tuning after
  hyperparameter search for additional control.

- **Model choice**: XGBoost offers speed, regularization, and feature
  importance interpretability — it is the primary target for tuning.

## Recommended next steps after tuning

1. Evaluate best model on holdout test and produce a short A/B comparison vs
   baseline (accuracy, recall, precision, AUC).
2. Run calibration (isotonic or Platt) and threshold selection to produce
   severity bins and color-coded outputs for the app.
3. Integrate best model and artifacts into the Streamlit app (Milestone 5)
   with SHAP/LIME visualizations preserved.
