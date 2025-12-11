# Executive / Stakeholder Summary

## Diabetes Risk XAI Project

Project Title &nbsp;: **Predicting Diabetes Risk Using Explainable AI (XAI).**\
Author   &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp;: **Mohamed Makki**\
Program &nbsp; &nbsp; &nbsp; : **MIT Emerging Talent Data and Computer Science
Program.**\
Date  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; : **December, 2025**

---

**1. Overview**\
This project delivers an end-to-end, fully explainable machine-learning system
designed to estimate diabetes risk and present clear, interpretable insights
that support early intervention. Using the Pima Indians Diabetes Dataset, the
system integrates strong predictive modeling with transparent explanations
using SHAP and LIME, ensuring that risk predictions are not only accurate but
also easily understood by clinicians, patients, and non-technical
decisionmakers.

---

**2. Motivation**\
Diabetes remains one of the world’s fastest-growing chronic diseases. Early
detection significantly reduces complications, yet many individuals lack access
to screening tools. This project addresses this gap by delivering:

- A lightweight, accessible prediction system
- Human-friendly explanations for every prediction
- A web-based app that enables real-time evaluation
The system supports awareness, clinical decision-making, and public-health
screening initiatives.

---

**3. Data & Methodology**\

- Dataset: Pima Indians Diabetes Dataset (768 samples, 8 clinical
features)
- Key Features: Glucose, BMI, Age, Pregnancies, Blood Pressure
- Pipeline:\
  
          1. Data validation & preprocessing
          2. Exploratory Data Analysis (EDA).
          3. Baseline modeling.
          4. Hyperparameter tuning (XGBoost)
          5. Explainability using SHAP + LIME.
          6. Deployment via Streamlit

The workflow ensures reproducibility, reliability, and traceability through
structured milestone folders and version-controlled outputs.

---

**4. Modeling & Performance**\
After testing multiple algorithms, tuned XGBoost emerged as the topperforming
model, offering:

- High recall (important for medical screening)
- Strong ROC-AUC
- Stability across random splits
The model was further analyzed using global and local XAI methods. SHAP
plots identified glucose as the dominant predictor, with BMI and age also
playing significant roles. LIME reinforced case-specific explanations for
individual predictions.

---

**5. Explainability Impact**\
The system integrates two complementary interpretability layers:

- SHAP summary & force plots show global feature impact and
individual risk drivers.
- LIME case explanations highlight local decision boundaries for
specific patients.
This dual-layer explanation system enhances transparency and aligns with
clinical expectations for responsible AI.
**6. Deployment**\

---

A fully interactive web application was built using Streamlit, providing:

- User-controlled input fields
- Real-time diabetes risk prediction
- Visual XAI explanations (SHAP + LIME)
- Clean, intuitive layout
- Deployment-ready structure for cloud hosting
App URL: [Diabetes Risk XAI Web Application][def]

---

**7. Key Achievements**\

- Complete end-to-end ML pipeline
- Strong predictive model with medically aligned insights
- Explainable risk dashboard
- Polished documentation across milestones
- Production-like deployment architecture

---

**8. Future Directions**\

- Integrate live clinical datasets for model validation
- Expand feature set using electronic health records (EHR)
- Local-language app versions (Arabic, Somali, Swahili)
- Deploy cloud API for mobile/clinic integration
- Improve calibration for clinical decision thresholds

---

[def]: https://diabetes-risk-xai-cuxn9elwmgaukdbnbfmq65.streamlit.app
