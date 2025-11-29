# Milestone 2 🔍 — Exploratory Data Analysis (EDA) & Baseline Modeling

---

## Objective 🎯

This milestone focuses on understanding the dataset, performing exploratory  
data analysis (EDA), preprocessing, and establishing a strong baseline
machine learning models for diabetes risk prediction; identifying important  
characteristics, detecting issues, before moving into more advanced modeling  
and interpretability (XAI).
The goal was to understand the dataset structure, identify key patterns, and
set a performance benchmark for future explainability and optimization
milestones.

---

## 1. Exploratory Data Analysis

### 1.1 Data Overview

   • Dataset shape, column names, data types\
   • Distribution of numerical features\
   • Class balance check (Diabetes vs. No Diabetes)\
   • Summary statistics

### 1.2 Data Cleaning & Preprocessing

   • Handling missing values\
   • Detecting outliers\
   • Normalization/standardization decisions\
   • Encoding categorical variables if required

### 1.3 Visualization & Insights

   • Histograms/kde plots for key features\
   • Correlation heatmap\
   • Boxplots for outlier inspection\
   • Relationship plots: BMI vs. Outcome, Glucose vs. Outcome, Age vs.
     Outcome, etc.

### Key EDA Findings 🔎

- **Missing values:** Some medical measurements (e.g., Insulin, BloodPressure)
  contained zeros that are physiologically impossible. These were treated as
  missing and handled during preprocessing.

- **Class distribution:** Dataset shows mild imbalance — ~65% non-diabetic
  vs. ~35% diabetic cases.

- **Feature correlations:**

  - Glucose shows the strongest positive correlation with diabetes outcome.

  - BMI and Age show moderate correlation.

- **Outliers:** Visible in variables like Glucose and BMI, confirmed via
  boxplots. No removal was done to preserve the dataset’s integrity.

- **Scaling:** Standardization using StandardScaler was applied to stabilize
  model training and ensure fair comparison between models.

---

## 2. Baseline Model

### 2.1 Model Choice

selecting a Logistic Regression model due to its:\
   • Interpretability\
   • Fast training\
   • Suitability for baseline comparison

### 2.2 Preprocessing for Baseline

   • StandardScaler applied to numerical features\
   • Train/validation split

### 2.3 Baseline Performance

Metrics:\
   • Accuracy\
   • Precision\
   • Recall\
   • F1-score\
   • ROC-AUC

**Important note:** The baseline is not expected to be highly optimized but
should set a performance benchmark for future model improvements.

**Baseline Model Development** 🧮

Three classifiers were evaluated using a standardized preprocessing pipeline.  
The dataset was split into 80/20 (train/test) using train_test_split.

<!-- markdownlint-disable MD033 -->

```text

-------------------------------------------------------------------------------
 Model               | Accuracy | ROC AUC | Key Notes
-------------------------------------------------------------------------------
 Logistic Regression |          |         | Simple interpretable baseline,
                     | 0.70780  | 0.8130  | used to establish performance
                     |          |         | floor
-------------------------------------------------------------------------------
 Random Forest       | 0.7468   | 0.8237  | Captured nonlinear relationships
                     |          |         | and improved recall
-------------------------------------------------------------------------------
 XGBoost             |          |         | Consistent accuracy with better 
                     | 0.7468   | 0.8281  |    AUC selected as final baseline 
                     |          |         |    model
-------------------------------------------------------------------------------


```
<!-- markdownlint-enable MD033 -->

---

**Baseline Model Rationale** 🧠

The milestone initially focused on Logistic Regression due to its
interpretability. However, additional experiments with Random Forest and
XGBoost demonstrated better handling of nonlinear dynamics.

➡ XGBoost was selected as the final baseline model.

**Why XGBoost Was Selected** 🧠

- Demonstrated the highest AUC score.
- Handled nonlinear relationships effectively.
- More consistent predictive performance across metrics.
- Provides explainability-friendly outputs for the next milestone (XAI).

Best model: XGBoost
Accuracy: 0.7468
ROC AUC: 0.8281

**Confusion Matrix (XGBoost)** \
[[82 18] \
[21 33]]

**Artifacts Produced** 💾

- baseline_metrics.txt — *detailed evaluation results*
- logreg_baseline.joblib — *logistic regression model*
- scaler.joblib — *fitted StandardScaler*
- xgb_final_model.joblib — *selected baseline model*
- 01+02_exploration.ipynb — *full EDA and baseline modeling code*

---

## 3. Summary

Milestone 2 successfully:

- Completed a full EDA.
- Identified key predictive variables and data challenges.
- Built and evaluated three baseline models.
- Selected XGBoost as the strongest baseline classifier.
- Produced serialized artifacts for future milestones.

This provides a solid analytical foundation for Milestone 3 (XAI), where we  
will begin interpreting model decisions using SHAP and other tools.

---

**Milestone Outcome:**  
Established a solid preprocessing and baseline modeling foundation with the
XGBoost classifier achieving the best trade-off between accuracy and ROC AUC.  
These results will guide model interpretability in the next milestone.

---

**Milestone Outcome:**  
Established a solid preprocessing and baseline modeling foundation with the
XGBoost classifier achieving the best trade-off between accuracy and ROC AUC.  
These results will guide model interpretability in the next milestone.

---

## Next Steps (Milestone 3) 🔜

- Apply **Explainable AI (XAI)** methods (SHAP, LIME) to interpret model  
  decisions.  
- Investigate feature importance and local explanations for individual
  predictions.  
- Explore model fairness and sensitivity to data imbalance.
  