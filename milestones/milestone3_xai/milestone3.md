# Milestone 3 🧠 — Explainable AI (XAI)

## Objective 🎯

Apply Explainable AI methods to the selected final model (XGBoost) to produce  
rigorous global and local interpretability outputs that are clinician-friendly  
and technically robust. Deliver publication-grade visuals and saved artifacts  
for inclusion in the final report and the Streamlit app.

---

## Key Decisions 🧭

- **Primary model:** XGBoost (`models/xgb_final_model.joblib`)
- **Explainability tools:** SHAP (primary) and LIME (local corroboration)
- **Outputs saved:** SHAP summary plot, dependence plots for top features,
  local waterfall plots, LIME explanation for sample cases — all saved in  
  `results/`
- **Notebook:** `notebooks/03_explainability.ipynb` — contains reproducible,  
  documented steps and visuals.

---

## Methods & Rationale 🔬

1. **SHAP (Shapley Additive exPlanations)**  
   - Use `shap.TreeExplainer` on the XGBoost model for fast, accurate global
     and local explanations.
   - Produce a SHAP summary (beeswarm + bar), per-feature dependence plots,
     and waterfall/local explanations for selected patients.
   - `shap` provides both global feature impact and exact local attribution  
     consistent with cooperative game theory.

2. **LIME**  
   - Use LIME as a local, model-agnostic comparison for a few representative  
     cases (e.g., one true positive, one false negative) to illustrate method  
     agreement and differences.
   - LIME is helpful because clinicians sometimes prefer simpler local  
     surrogates.

---

## Notebook structure 🗂️ (03_explainability.ipynb)

1. Setup: imports, paths, requirements check.
2. Load data and preprocessing pipeline (load `scaler.joblib`), load  
   `xgb_final_model.joblib`.
3. Prepare test set (use same split or load test artifacts from Milestone 2).
4. Global explanations (SHAP):
   - SHAP TreeExplainer setup
   - SHAP summary plot (bar + beeswarm)
   - Top feature dependence plots (top 2)
   - Save plots to `results/`
5. Local explanations:
   - Pick representative records (TP, TN, FP, FN) using confusion matrix
   - SHAP waterfall and force plots for each selected record
   - LIME explanation for 1–2 same records, compare with SHAP
   - Store explanation JSONs / PNGs
6. Narrative & conclusions: clinician-friendly summaries of insights.
7. Save final artifacts and a short `xai_summary.txt` (or incorporate summary  
   in `milestone3.md`).

---

## Deliverables 📦

- `milestone3.md` (this document)
- `notebooks/03_explainability.ipynb` (runnable notebook)
- Saved images and artifacts in `/results/`:
  - `shap_summary.png`, `shap_beeswarm.png`, `shap_dependence_feature1.png`,  
    `shap_waterfall_caseTP.png`, `lime_caseTP.png`, etc.
- Short `README.md` inside the milestone folder describing how to run the
  notebook and how to surface visualizations in Streamlit.

---

## Next Steps (after XAI) 🔜

- Integrate chosen SHAP visualizations into the Streamlit app for interactive  
  explanation (Milestone 5).
- If time permits, compute feature stability across bootstrap samples to
  confirm robustness of top features.
- Document limitations and clinician-facing guidance for interpretation.
