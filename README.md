# diabetes-risk-xai

Efficient and explainable AI for diabetes risk prediction (capstone project).

---

This repository hosts my capstone project for the Computer and Data Science program at MIT.
The project develops machine learning and deep learning models to predict diabetes risk, with a focus on efficiency and explainability.

---

📌 Project Overview
Diabetes is a growing global health challenge, and early detection of at-risk individuals is essential for prevention. While AI models have shown promise in disease prediction, many are computationally heavy and function as “black boxes”, limiting their real-world adoption in healthcare.
This project addresses these challenges by:
Comparing classical ML models with deep learning approaches.
Improving efficiency using lightweight methods.
Applying explainability techniques to highlight the most important health factors.
Delivering a Streamlit web app for real-time risk prediction with explanations.

---

🎯 Objectives
Preprocess and analyze the Pima Indians Diabetes dataset.
Build and evaluate baseline ML models and a deep learning model.
Improve model efficiency while maintaining strong predictive accuracy.
Apply SHAP and LIME for model interpretability.
Deploy the final model in a Streamlit app for interactive use.

---

📊 Dataset
Source: Pima Indians Diabetes Database (UCI)
Features: 8 medical and lifestyle factors (e.g., Glucose, BMI, Age).
Target: Binary classification (Diabetes / No Diabetes).

---

🛠️ Tech Stack
Languages & Tools: Python, Jupyter Notebook, GitHub
Libraries: scikit-learn, TensorFlow/Keras, XGBoost, SHAP, LIME, Streamlit, pandas, matplotlib, seaborn

---

📂 Repository Structure
diabetes-risk-xai/

│── data/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Dataset or download instructions_

│── notebooks/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Jupyter notebooks (EDA, models, results)_

│── src/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Python scripts (preprocessing, training, explainability)_

│── app/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Streamlit app code_

│── results/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Metrics, plots, SHAP/LIME visuals_

│── README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Project overview_

│── requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_# Python dependencies_

---

🚀 Deliverables
    Comparative analysis of ML and DL models.
    SHAP/LIME visualizations of feature importance.
    Efficiency benchmarks (model size, runtime).
    Streamlit app for interactive prediction + explanation.
    Final research report (capstone submission).

---

📖 License
This project is licensed under the MIT License — free to use with attribution.
