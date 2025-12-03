# Milestone 2 — Data Exploration & Baseline Modeling 🔍

## Objective 🎯

Perform full Exploratory Data Analysis (EDA), clean and preprocess the dataset,
and build strong baseline machine-learning models to understand performance
limits before applying explainability or tuning.

## Overview 📘

This milestone establishes the analytical foundation of the project.
It includes:

- Understanding variable distributions and relationships
- Handling missing values and zero-encoded medical fields
- Detecting outliers
- Preparing data for modeling (scaling, splitting)
- Training multiple baseline models
- Selecting the best baseline for later XAI and tuning

## Key Tasks ⚙️

### 1. Exploratory Data Analysis (EDA)

- Distribution plots (histograms, density plots)
- Correlation heatmap
- Boxplots for outlier inspection
- Class distribution analysis
- Identification of zero-encoded missing values (e.g., Insulin,
  BloodPressure)

### 2. Data Cleaning & Preprocessing

- Replace zero-values where medically inappropriate
- Standardize numeric features using StandardScaler
- Train/test split (80/20)

### 3. Baseline Model Training

- Three baseline models were developed and evaluated
- Model Accuracy ROC AUC Notes
- Logistic Regression 0.7078 0.8130 Interpretable baseline; sets minimum  
  performance
- Random Forest 0.7468 0.8237 Captures nonlinear relationships
- XGBoost 0.7468 0.8281 Strongest baseline; best AUC

➡ XGBoost selected as the final baseline model.

### 4. Artifact Generation

- baseline_metrics.txt — evaluation logs
- scaler.joblib — standardized scaler
- logreg_baseline.joblib
- xgb_final_model.joblib
- 01+02_exploration.ipynb — complete analysis workflow

## Deliverables 📦

- Cleaned dataset
- Comprehensive EDA visualizations
- Baseline performance metrics
- Saved preprocessing + model artifacts in models/
- Updated notebook documenting all steps

## Why This Milestone Matters 💡

- This stage ensures the project has a reliable analytical foundation before
  introducing explainability or tuning:
- Confirms dataset quality
- Reveals patterns supporting the research question
- Defines baseline performance to compare future improvements
- Identifies which features influence model behavior (to be expanded in
  Milestone 3)

## What We Achieved ✔️

- Completed a full exploratory analysis
- Established a robust baseline model suite
- Selected XGBoost as the most suitable starting point for XAI
- Prepared all assets for interpretability and deployment

## Next Steps 🔜 (Milestone 3 — XAI)

We will now enhance the project by interpreting the baseline model using:

SHAP\
LIME\
Permutation importance\
Partial dependency plots\
Local + global explanations\

These insights will be crucial for communicating results to clinicians and
non-technical audiences later in the project.
