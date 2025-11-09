# Milestone 2 🔍 — Exploratory Data Analysis (EDA) & Baseline Modeling

---

## Objective 🎯

This milestone focused on performing exploratory data analysis (EDA),
preprocessing, and establishing baseline machine learning models for diabetes  
risk prediction. The goal was to understand the dataset structure, identify  
key patterns, and set a performance benchmark for future explainability and  
optimization milestones.

---

## Dataset Overview 🧩

The dataset used was derived from the Pima Indians Diabetes Database,
containing physiological and diagnostic attributes such as glucose, BMI, age,  
and insulin levels.

### Key EDA Findings 🔎

- **Missing values:** Identified zero-valued entries in certain medical
  variables (e.g., `Insulin`, `BloodPressure`), treated as missing and handled  
  appropriately.  
- **Class distribution:** Slight class imbalance with non-diabetic samples  
  (~65%) dominating.  
- **Correlations:** Strong positive correlation between `Glucose` and  
  `Outcome`. Moderate correlations for `BMI` and `Age`.  
- **Outliers:** Detected and visualized via boxplots; no removal was done at  
  this stage to preserve data integrity.  
- **Feature scaling:** Standardization was applied to numerical variables
  using `StandardScaler` to stabilize model training.

---

## Baseline Model Development 🧮

Three classifiers were trained using a standardized preprocessing pipeline.  
Data was split into training and testing subsets (80/20) using
`train_test_split` for consistent evaluation.

<!-- markdownlint-disable MD033 -->

```text

--------------------------------------------------------------------------
 Model               | Accuracy | ROC AUC | Key Notes
--------------------------------------------------------------------------
 Logistic Regression | 0.7078   | 0.8130  | Simple interpretable baseline,
                     |          |         | used to establish performance floor
--------------------------------------------------------------------------
 Random Forest       | 0.7468   | 0.8237  | Captured nonlinear relationships
                     |          |         | and improved recall
--------------------------------------------------------------------------
 XGBoost             | 0.7468   | 0.8281  | Consistent accuracy with better AUC
                     |          |         | selected as final baseline model
--------------------------------------------------------------------------


```
<!-- markdownlint-enable MD033 -->

---

## Baseline Model Rationale 🧠

**Logistic Regression** was selected as the first baseline due to its
simplicity, interpretability, and strong performance on tabular medical data.  
Subsequent experiments with **Random Forest** and **XGBoost** provided
comparative improvements in recall and AUC, highlighting the dataset’s
nonlinear characteristics.

---

## Results Summary 📊

- Best performing model: **XGBoost**
- Accuracy: **0.7468**
- ROC AUC: **0.8281**
- Confusion Matrix (XGBoost):  

[[82 18]
[21 33]]

- Both scaler and model artifacts were serialized using `joblib` and stored
  in the root-level `models/` directory.

---

## Artifacts 💾

- `baseline_metrics.txt` — Contains full model performance reports and
  confusion matrices.  
- `logreg_baseline.joblib`, `scaler.joblib`, `xgb_final_model.joblib` — Saved  
  preprocessing and model artifacts located in `/models/`.  
- `01_exploration.ipynb` — Jupyter notebook containing the complete workflow  
  and code execution.

---

## Next Steps (Milestone 3) 🔜

- Apply **Explainable AI (XAI)** methods (SHAP, LIME) to interpret model  
  decisions.  
- Investigate feature importance and local explanations for individual
  predictions.  
- Explore model fairness and sensitivity to data imbalance.

---

**Milestone Outcome:**  
Established a solid preprocessing and baseline modeling foundation with the
XGBoost classifier achieving the best trade-off between accuracy and ROC AUC.  
These results will guide model interpretability in the next milestone.
