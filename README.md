# Diabetes Risk Prediction with Explainable AI (XAI)

Efficient and explainable AI for diabetes risk prediction (capstone project).

---

This repository hosts my capstone project for the Computer and Data Science
program at MIT.
The project develops machine learning and deep learning models to predict
diabetes risk, with a focus on efficiency and explainability.

---

## Project Overview

This project aims to build an interpretable machine learning system that
predicts the risk of diabetes based on clinical data.
Using Explainable AI (XAI) techniques like SHAP and LIME, the goal is not only  
to achieve accurate predictions but also to make model decisions transparent  
and understandable for healthcare professionals and patients.
The project is developed to demonstrate end-to-end AI model development,  
from data collection to real-world deployment.

This project addresses these challenges by:

- Comparing classical ML models with deep learning approaches.
- Improving efficiency using lightweight methods.
- Applying explainability techniques to highlight the most important health
  factors.
- Delivering a Streamlit web app for real-time risk prediction with
  explanations.

---

## Objectives

- Preprocess and analyze the Pima Indians Diabetes dataset.
- Build and evaluate baseline ML models and a deep learning model.
- Improve model efficiency while maintaining strong predictive accuracy.
- Apply SHAP and LIME for model interpretability.
- Deploy the final model in a Streamlit app for interactive use.

---

## DatasetSource

**Source&nbsp;&nbsp;&nbsp;:** Pima Indians Diabetes Database (UCI). / openml.org and
**Features:** 8 medical and lifestyle factors (e.g., Glucose, BMI, Age).  
**Target&nbsp;&nbsp;&nbsp;&nbsp;:** Binary classification (Diabetes / No
Diabetes).

---

## Tech Stack

- **Languages &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:** Python
- **Libraries&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:**
    scikit-learn, TensorFlow/Keras,
  XGBoost, SHAP, LIME, Streamlit, NumPy, Pandas, MatPlotLib, Seaborn
- **Environment&nbsp;&nbsp;&nbsp;&nbsp;:** JupyterNotebook + VS Code
- **Version Control:** Git / GitHub

---

## Project Milestones

**Milestone 1** — Problem Identification & Data Collection

*Objective:* \
Define the problem, justify dataset selection, and perform a preliminary study  
 on diabetes prediction.

*Deliverables:*  

- Project overview and motivation
- Dataset selection rationale
- Description of data source (Pima Indians Diabetes dataset)

**Milestone 2** — Data Exploration & Baseline Modeling  

*Objective:*
Explore data, visualize feature relationships, and build a baseline predictive
model.

*Deliverables:*  

- Jupyter notebook with EDA and data cleaning
- Baseline logistic regression model
- Performance metrics and confusion matrix

**Milestone 3** — Explainable AI (XAI) Integration

*Objective:*
Implement and interpret model predictions using SHAP and LIME for transparency.

*Deliverables:*

- XAI integration notebook
- SHAP summary plots and LIME explanations
- Discussion on interpretability insights

**Milestone 4** — Model Tuning & Improvement

*Objective:*

optimize model performance using hyperparameter tuning and ensemble methods
(combining multiple models  to improve prediction accuracy and reduce errors.).

*Deliverables:*

- Updated notebook with model tuning
- Comparative evaluation of baseline vs tuned models
- Final model selection rationale

**Milestone 5** — Deployment (Streamlit App)

*Objective:*

Deploy an interactive Streamlit web app that enables users to input data
and view diabetes risk predictions with SHAP/LIME visualizations.

*Deliverables:*

- Streamlit app script (app.py)
- Example user interface screenshots
- Deployment guide

**Milestone 6** — Final Report & Documentation

*Objective:*

Compile all results, findings, and visualizations into a cohesive final report  
and presentation.

*Deliverables:*

- Comprehensive technical report
- Slide deck for project defense
- Updated README and GitHub documentation

---

## Repository Structure

│── data/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*# Raw & processed data*  
│&nbsp;&nbsp;&nbsp;&nbsp;   └── pima.csv
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

│── notebooks/  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp; *# Jupyter notebooks for analysis*  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 01_exploration.ipynb

├── models/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*# Saved models and scalers*  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── xgb_final_model.joblib

│── app/  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;*# Streamlit app code*  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── app.py  
│── results/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*# Metrics, plots, SHAP/LIME visuals*  
│── src/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;*# Utility scripts (data prep, evaluation)*  
│── README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*# Project overview*  
│── requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;  
└── LICENSE

---

## Future Enhancements

- Integrate more clinical datasets for improved generalization.
- Explore federated learning to ensure data privacy.
- Extend app with patient-specific treatment recommendations.

---

## License

This project is licensed under the MIT License — free to use with attribution.
