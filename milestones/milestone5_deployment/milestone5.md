# Milestone 5 — Evaluation, Validation, and Communication of Results

## 1. Overview

Milestone 5 focuses on assessing the performance of the diabetes-risk
prediction model, validating its reliability, stress-testing it against
various metrics, and communicating findings clearly to technical and
non-technical stakeholders.

This milestone also finalizes the interpretability narrative (SHAP-based) and
prepares the project for deployment in Milestone 6.

---

## 2. Objective

Deliver a production-ready interactive web app (Streamlit) that:

- Accepts user input for patient features
- Produces a diabetes risk probability using the tuned model
- Maps predicted probability to a clinical Severity bucket (Low / Moderate /  
  High)
- Displays interactive explainability artifacts (SHAP force HTML, LIME HTML)
- Provides downloads for artifacts and the model

## 3. Severity mapping (chosen approach)

We use **probability thresholds** to map risk probability (p) to severity:

- **Low** : p < 0.20 (green)
- **Moderate** : 0.20 ≤ p < 0.50 (amber)
- **High** : p ≥ 0.50 (red)

These thresholds are tunable and should be reviewed with clinical stakeholders.

## 4. Model Evaluation

### - Metrics Used

- **Accuracy**
- **Precision / Recall**
- **F1-score**
- **ROC-AUC**
- **Confusion Matrix**
- **Calibration curves**
- **SHAP consistency checks**

---

## 5. Results Summary

| Metric | Value |
|--------|--------|
| Accuracy | ~ **0.87** |
| Precision | ~ **0.85** |
| Recall | ~ **0.89** |
| F1-score | ~ **0.87** |
| ROC-AUC | ~ **0.92** |

*These values represent strong performance and good predictive reliability.*

---

## 6. Error Analysis

- False negatives reduced by tuning recall-focused thresholding.
- Misclassifications mostly linked to missing values or edge cases (extremely
  high glucose but low BMI).

---

## 7. Interpretability (XAI)

SHAP analysis highlights:

- Glucose level as strongest driver of prediction.
- BMI and Diabetes Pedigree Function strongly influence risk.
- Model behavior matches established clinical findings.

---

## 8. Communication & Reporting

This milestone includes:

- **technical results** (evaluation_report.md)  
- **business-friendly summary** (stakeholder_summary.md)  
- **visual communication assets** (PowerPoint prepared in next task)  

---

## 9. Files Created in This Milestone

- `milestone5.md`
- `README.md`
- `communication_results.md`
- `evaluation_report.md`
- `stakeholder_summary.md`

## 10. Deliverables

- `app/streamlit_app.py` — main Streamlit app (this directory)
- `README.md` — deployment/readme
- Model artifacts (expected in root `models/`):
  - `xgb_tuned.joblib` (preferred)
  - fallback: `xgb_final_model.joblib`
- `results/` — explainability artifacts (SHAP force HTMLs, LIME htmls) created
   by Milestone 3 notebook

## 11. How the app supports reproducibility & transparency

- The app does not compute SHAP/LIME live. It reads pre-computed artifacts from
  `results/` (fast and stable).
- SHAP force plots are saved as HTML (interactive) and embedded via
  `components.html`.
- LIME is saved as HTML and displayed within the app.

## 12. Security and privacy

- This app is for demonstration only and **must not** be used for clinical
  decision-making without proper validation.
- Avoid putting real patient data into demo/demo servers.
