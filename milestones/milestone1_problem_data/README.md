# Milestone 1 — Problem Definition & Data Collection 🧭

## Objective 🎯

Establish the foundation of the project by identifying the real-world
healthcare problem, justifying the dataset selection, and defining the data
acquisition and validation process.

---

## Description 📘

This milestone defines the problem of predicting diabetes risk using machine
learning and explainable AI.
**Source:**: The chosen dataset is the **PIMA Indians Diabetes Database** from  
the UCI Machine Learning Repository, and ResearchGate, [[Pima DataSet Link](  
https://bit.ly/43TRitR)].  selected due to its reliability, structure, and  
relevance to clinical prediction research.
**Data Size:** 768 samples, 8 features
**Target Variable:** `Outcome` (1 = Diabetic, 0 = Non-Diabetic)
**Key Features:** Glucose, Blood Pressure, BMI, Insulin, Age, Pregnancies,  
Skin Thickness, Diabetes Pedigree Function.

---

## Key Tasks 🧩

1. Define the research problem and motivation.
2. Identify the dataset source and assess data quality.
3. Implement data download script (data/download_data.py).
4. Verify dataset integrity and structure (shape, features, and missing values)
5. Generate a `data_verification_report.md` summarizing findings.
6. Stored data in the `/data` folder and ensured reproducibility via script:

      ```bash
   python data/download_data.py

---

## Deliverables 📦

- `milestone1.md` – Detailed milestone report  
- `data_verification_report.md` – Data quality & verification results  
- `README.md` – Overview of milestone goals and progress  

---

## Tools & Libraries 🧰

- **Python** 🐍, **pandas** 🗃️, **NumPy** 🔢
- **Jupyter Notebook** 📓
- Basic data visualization with **matplotlib** and **seaborn** 📊
