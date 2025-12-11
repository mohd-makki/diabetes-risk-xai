# 📌 Diabetes Risk Prediction with Explainable AI (XAI) 🩺

A complete end-to-end machine-learning project with transparency, clinical
alignment, and deployment-ready features.

---

This repository hosts my capstone project for the Computer and Data Science
program at MIT.
The project develops machine learning and deep learning models to predict
diabetes risk, with a focus on efficiency and explainability.
The goal is to develop an interactive Streamlit web application that enables
users to input data and view diabetes risk predictions

---

## 🚀 Live Application: Go try it

[![Open in Streamlit](
https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabetes-risk-xai-cuxn9elwmgaukdbnbfmq65.streamlit.app/)

---

## Project Overview 🧭

This project develops a fully explainable machine-learning system that predicts
an individual’s likelihood of having diabetes while providing clear,
human-interpretable explanations for every prediction.
Using the Pima Indians Diabetes Dataset, the system integrates:

- Robust preprocessing and data validation
- EDA & baseline modeling
- Hyperparameter tuning (XGBoost)
- Explainability with SHAP & LIME
- A deployed Streamlit application
- Milestone-based documentation replicating professional workflows

The goal is to support early detection, clinical decision-making, and
public-health screening with a model that is not only accurate but also
transparent and trustworthy.

## Project Objectives 🎯

1. Build a reproducible, research-grade ML pipeline.
2. Develop a high-performance, clinically meaningful, a machine learning model
   to predict diabetes risk.
3. Produce global + local explainability artifacts, integrate explainable
   AI (XAI) methods (SHAP and LIME) for model transparency.
4. Apply explainability techniques to highlight the most influential health
   factors driving predictions.
5. Evaluate model performance and interpretability using standardized metrics.
6. Deploy an interactive, user-friendly web app, this interactive Streamlit app
   for user testing and visualization.
7. Document the full data science lifecycle across milestones.
8. Deliver a final report and executive/stakeholder-facing summary

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
| `results`          | place for final outputs |
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
│   ├── xgb_tuned.joblib
│   └── .gitkeep
│
├── notebooks/
│   └── exploratory_tests.ipynb
│
├── milestones/
│   │
│   ├── milestone0_repository_setup/
│   │   ├── README.md
│   │   ├── CONTRIBUTING.md
│   │
│   │
│   ├── milestone1_problem_def(plus data collection)/
│   │   ├── problem_statement.md
│   │   ├── research_question.md
│   │   ├── domain_background.md
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
│   │   ├── notebooks/
│   │   │   └── 04_tuning.ipynb
│   │   ├── tuning_log.txt
│   │   └── README.md
│   │
│   ├── milestone5_deployment/
│   │   ├── milestone5.md
│   │   ├── communication_results.md
│   │   ├── evaluation_report.md
│   │   ├── stakeholder_summary.md
│   │   ├── app/
│   │   │   └── streamlit_app.py
│   │   └── README.md
│   │
│   └── milestone6_final_report/
│       ├── milestone6.md
│       ├── final_presentation_slides.pptx
│       ├── final_presentation_video.mp4
│       ├── presentation_2.5_minutes_audio.mp3
│       ├── stakeholder_summary_final.md
│       ├── executive_summary_report.pdf (one page)
│       ├── final_report.pdf
│       └── README.md
│
└── .vscode/
    └── settings.json 

```
<!-- markdownlint-enable MD033 -->

**Each milestone includes its own README + documentation for clear traceability.**

---

## 📄 Final Report & Summary

- Full Final Report (PDF): [**Click Here for Final Report**](https://github.com/mohd-makki/diabetes-risk-xai/blob/main/milestones/milestone6_final_report/Final%20Report.pdf)
- One-Page Executive Summary: [**One Page Executive Summary is Here**](https://github.com/mohd-makki/diabetes-risk-xai/blob/main/milestones/milestone6_final_report/executive_summary.pdf)

---

## ⚙️ Setup & Reproduction Instructions

The following steps allow anyone to reproduce the entire project environment and run the application locally.

1️⃣ Clone the Repository:\
git clone <https://github.com/mohd-makki/diabetes-risk-xai.git>\
cd diabetes-risk-xai

2️⃣ Create & Activate Python Environment:\

```bash
python -m venv venv\
source venv/bin/activate     # *MacOS / Linux*
venv\Scripts\activate        # *Windows*

3️⃣ Install Project Dependencies
This repository uses a frozen requirements.txt to ensure full reproducibility.

pip install -r requirements.txt

4️⃣ Explore the Notebooks

All exploration, modeling, XAI, and tuning steps are inside:

notebooks/
milestones/*/notebooks/

You can launch them with:

jupyter notebook

5️⃣ Run the Streamlit Application Locally:
streamlit run milestones/milestone5_deployment/app/streamlit_app.py
```

## 📊 Key Deliverables

- ✔ Complete milestone-based project structure
- ✔ Data validation + EDA
- ✔ Baseline models
- ✔ Tuned XGBoost model
- ✔ SHAP summary + force plots
- ✔ LIME explanations
- ✔ Calibration curve
- ✔ Full model metrics
- ✔ Streamlit deployment
- ✔ Final report + one-page executive summary

## 🧠 Model Performance (Summary)

```bash
──────────────────────────────────────────────
| Model              |Accuracy | Recall | AUC  |
|──────────────────────────────────────────────|
| Logistic Regression|    …    |   …    |  …   |
|──────────────────────────────────────────────|
| Random Forest      |    …    |   …    |  …   |
|──────────────────────────────────────────────|
| XGBoost (Tuned)    |   Best  |  Best  | Best |
|──────────────────────────────────────────────
```

(See full metrics in results/ and milestone reports.)

## 🔎 Explainability Highlights

- SHAP identifies glucose as the strongest global predictor
- BMI and Age follow as highly influential
- Local SHAP force plots show patient-specific risk explanations
- LIME clarifies individual model decisions for interpretability
- Results align with clinical expectations
- SHAP and LIME artifacts are stored in:
results/

## 📈 Project Workflow (High-Level)

Repository Setup\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓\
Data Acquisition\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓\
Data Validation & Preprocessing\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓\
Exploratory Data Analysis\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓\
Modeling (Baseline → Optimized)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓\
Explainability (SHAP + LIME)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓\
Model Tuning (XGBoost)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓\
Deployment (Streamlit App)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓\
Final Report & Stakeholder(Executive) Summary\

## 🌍 Future Work

- Validate model with real clinical datasets
- Integrate Electronic Health Records (EHRs)
- Add multilingual UI (Arabic, Somali, Swahili)
- Deploy API for hospitals/clinics
- Improve calibration for clinical thresholds
- Extend dataset with demographics and lifestyle features

## 🤝 Contribution Guidelines

See:
milestones/milestone0_repository_setup/CONTRIBUTING.md

## 📜 License

This project is released under the MIT License.\
See: LICENSE
