# Diabetes Risk Prediction with Explainable AI (XAI) 🩺

Efficient and explainable AI for diabetes risk prediction (capstone project).

---

This repository hosts my capstone project for the Computer and Data Science
program at MIT.
The project develops machine learning and deep learning models to predict
diabetes risk, with a focus on efficiency and explainability.

---

## Project Overview 🧭

This project aims to build an interpretable machine learning system that
predicts the risk of diabetes based on clinical data.
the project combines predictive models (Logistic Regression, Random Forest,
XGBoost) with Explainable AI (XAI) techniques such as **SHAP** and **LIME**
to help clinicians understand *why* predictions are made. the goal is not only  
to achieve accurate predictions but also to make model decisions transparent  
and understandable for healthcare professionals and patients.
The project is developed to demonstrate end-to-end AI model development,  
from data collection to real-world deployment.

## Project Objectives 🎯

1. Develop a machine learning model to predict diabetes risk.
2. Compare classical ML models (Logistic Regression, Random Forest, XGBoost)  
   with deep learning approaches.
3. Integrate explainable AI (XAI) methods such as SHAP and LIME for model
   transparency.
4. Apply explainability techniques to highlight the most influential health
   factors driving predictions.
5. Evaluate model performance and interpretability using standardized metrics.
6. Deploy an interactive Streamlit app for user testing and visualization.
7. Document the full data science lifecycle across milestones.

---

## DatasetSource 🌐

**Source&nbsp;&nbsp;&nbsp;:** Pima Indians Diabetes Database; Machine Learning  
Repository (UCI), openML.org, and ResearchGate, [[Pima DataSet Link](  
https://bit.ly/43TRitR)].  
**Features:** 8 medical and lifestyle factors (e.g., Glucose, BMI, Age).  
**Target&nbsp;&nbsp;&nbsp;&nbsp;:** Binary classification (Diabetes / No
Diabetes).

---

## Tech Stack 🧠

- **Languages &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:** Python
- **Libraries&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:**
    Pandas, Numpy, scikit-learn, TensorFlow/Keras, XGBoost, Explainable AI
    (SHAP and LIME), Deployment (Streamlit), Visualization (MatPlotLib and
    Seaborn)
- **Environment&nbsp;&nbsp;&nbsp;&nbsp;:** JupyterNotebook + VS Code
- **Version Control:** Git / GitHub

---

## Project Milestones 🚩

**Milestone 1** 📌 — Problem Identification & Data Collection

*Objective:* \
Define the problem, justify dataset selection, and perform a preliminary study  
on diabetes prediction.

*Deliverables:*  

- Project overview and motivation
- Dataset selection rationale
- Description of data source (Pima Indians Diabetes dataset)

**Milestone 2** 🔍 — Data Exploration & Baseline Modeling  

*Objective:*
Explore data, visualize feature relationships, and build a baseline predictive
model.

*Deliverables:*  

- Jupyter notebook with EDA and data cleaning
- Baseline logistic regression model
- Performance metrics and confusion matrix

**Milestone 3** 🧭 — Explainable AI (XAI) Integration

*Objective:*
Implement and interpret model predictions using SHAP and LIME for transparency.

*Deliverables:*

- XAI integration notebook
- SHAP summary plots and LIME explanations
- Discussion on interpretability insights

**Milestone 4** ⚙️ — Model Tuning & Improvement

*Objective:*

optimize model performance using hyperparameter tuning and ensemble methods
(combining multiple models  to improve prediction accuracy and reduce errors.).

*Deliverables:*

- Updated notebook with model tuning
- Comparative evaluation of baseline vs tuned models
- Final model selection rationale

**Milestone 5** 🚀 — Deployment (Streamlit App)

*Objective:*

Deploy an interactive Streamlit web app that enables users to input data
and view diabetes risk predictions with SHAP/LIME visualizations.

*Deliverables:*

- Streamlit app script (app.py)
- Example user interface screenshots
- Deployment guide

**Milestone 6** 📁 — Final Report & Documentation

*Objective:*

Compile all results, findings, and visualizations into a cohesive final report  
and presentation.

*Deliverables:* 🎯

- Comprehensive technical report
- Slide deck for project defense
- Updated README and GitHub documentation

---

## Repository Structure 📁

|      Folder        | Description |
|--------------------|--------------|
| `data/`            | Raw dataset and data download scripts |
| `models/`          | Trained models and scalers |
| `notebooks/`       | Scratch notebooks for testing ideas |
| `app/`             | Streamlit deployment app |
| `milestones/`      | Organized project phases |
| `.vscode/`         | VS Code configuration |
| `requirements.txt` | List of dependencies |

<!-- markdownlint-disable MD033 -->

```text

diabetes-risk-xai/
│
├── README.md
├── results/
│   └── .gitkeep
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── data/
│   ├── download_data.py
│   ├── pima.csv
│   └── .gitkeep
│
├── models/
│   ├── xgb_final_model.joblib
│   ├── logreg_baseline.joblib  
│   ├── scaler.joblib
│   └── .gitkeep
│
├── notebooks/
│   └── exploratory_tests.ipynb
│
├── app/
│   └── streamlit_app.py
│
├── milestones/
│   ├── milestone1_problem_data/
│   │   ├── milestone1.md
│   │   ├── data_verification_report.md
│   │   └── README.md
│   │
│   ├── milestone2_EDA_baseline/
│   │   ├── milestone2.md
│   │   ├── baseline_metrics.txt
│   │   ├── notebooks/
│   │   │   └── 01+02_exploration.ipynb
│   │   └── README.md
│   │
│   ├── milestone3_xai/
│   │   ├── milestone3.md
│   │   ├── notebooks/
│   │   │   └── 03_explainability.ipynb
│   │   └── README.md
│   │
│   ├── milestone4_model_tuning/
│   │   ├── milestone4.md
│   │   ├── tuning_log.txt
│   │   └── README.md
│   │
│   ├── milestone5_deployment/
│   │   ├── milestone5.md
│   │   ├── app/
│   │   │   └── streamlit_app.py
│   │   └── README.md
│   │
│   └── milestone6_final_report/
│       ├── milestone6.md
│       ├── final_presentation.pptx
│       ├── final_report.pdf
│       └── README.md
│
└── .vscode/
    └── settings.json 

```
<!-- markdownlint-enable MD033 -->

---

## License 📜

This project is licensed under the MIT License — free to use with attribution.
