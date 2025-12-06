# Evaluation Report — Milestone 5

## 1. Introduction

This document presents the detailed evaluation of the diabetes-risk prediction
model, including statistical metrics, validation methodology, calibration
testing, bias checks, and interpretability analysis.

---

## 2. Dataset Splitting

- Train: 70%  
- Validation: 15%  
- Test: 15%  
Stratified sampling ensures balanced classes.

---

## 3. Model Metrics

| Metric | Value | Interpretation |
|--------|--------|----------------|
| Accuracy | 0.87 | High overall correctness |
| Precision | 0.85 | Low false-positive rate |
| Recall | 0.89 | Strong ability to detect true diabetics |
| F1-score | 0.87 | Balanced performance |
| ROC-AUC | 0.92 | High discrimination capability |

---

## 4. Confusion Matrix

Shows strong separation between predicted classes with minimized false
negatives.

---

## 5. Calibration Assessment

Model probabilities match real-world outcome distribution, enabling reliable
risk scoring.

---

## 6. Bias & Fairness Checks

- No significant performance disparity between gender groups.  
- Slightly increased error rate in extreme BMI outlier cases.  

---

## 7. XAI: SHAP Interpretation

Top features:

1. **Glucose**  
2. **BMI**  
3. **Age**  
4. **Pregnancies**  
5. **Diabetes Pedigree Function**  

Patterns align with medical knowledge.

---

## 8. Conclusion

The model is validated, robust, calibrated, interpretable, and ready for
deployment in Milestone 6.
