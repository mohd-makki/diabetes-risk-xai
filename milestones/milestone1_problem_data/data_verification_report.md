# Data Verification Report 🧾– Pima Indians Diabetes Dataset

## 1. Purpose 🎯

This report verifies data integrity, completeness, and consistency before  
analysis.  
It ensures that the dataset is properly structured for subsequent modeling  
steps.

---

## 2. Dataset Information 📚

**File:** `pima.csv`  
**Rows:** 768  
**Columns:** 9  

---

### Column Details 🧾

| Column | Non-Null Count | Missing | Zeros Found | Data Type | Valid Range |
|---------|----------------|----------|--------------|------------|-----------|
| Pregnancies | 768 | 0 | 111 | int | 0–17 |
| Glucose | 768 | 0 | 5 | int | 0–199 |
| BloodPressure | 768 | 0 | 35 | int | 0–122 |
| SkinThickness | 768 | 0 | 227 | int | 0–99 |
| Insulin | 768 | 0 | 374 | int | 0–846 |
| BMI | 768 | 0 | 11 | float | 0–67.1 |
| DiabetesPedigreeFunction | 768 | 0 | 0 | float | 0.08–2.42 |
| Age | 768 | 0 | 0 | int | 21–81 |
| Outcome | 768 | 0 | 500 | int | 0 or 1 |

---

## 3. Validation Checks Performed 🔎

- ✅ **File Readability** – CSV loaded successfully using pandas.  
- ✅ **Column Structure** – Matches expected schema (9 features).  
- ⚠️ **Zero Values Found** – Detected in Glucose, BMI, BloodPressure, etc.,
  which are physiologically invalid and must be handled.  
- ✅ **Duplicate Rows** – None found.  
- ✅ **Missing Values (NaN)** – None found.  
- ✅ **Data Types** – All numeric and compatible for modeling.

## 4. Recommended Actions 💡

- Replace or impute zero values using median or mean (by feature).  
- Normalize numeric variables (e.g., Min-Max or Standard Scaler).  
- Verify outcome class balance before model training.  

## 5. Conclusion ✍️

The dataset passes structural verification. However, several zero-value
anomalies should be addressed in the next phase.  
Proceed to **Milestone 2 (EDA & Baseline Modeling)** for in-depth statistical  
and visual exploration.

---

**Verified by:** ✔️ *the author* 🕶️  
**Date:** 📅 *Oct. 30th, 2025*  
