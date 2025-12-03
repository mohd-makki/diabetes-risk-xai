# Contributing to *diabetes-risk-xai*

Thank you for your interest in contributing! This project is designed for
open-source collaboration with a clean and professional workflow that ensures
high-quality contributions.

---

## 🧭 How to Contribute

All work in this project follows a structured flow:

1. **Open an Issue**

   * Every change begins with an issue.
   * Clearly describe the problem, feature request, or proposal.

2. **Assign Yourself**

   * Assign the issue to yourself or request assignment.

3. **Move Issue on the Project Board**

   * Move to **To Do**, then **In Progress**, then **Ready for Review**, etc.

4. **Create a Branch**
   Use the naming convention:

   ```bash
   feature/<short-description>
   fix/<short-description>
   docs/<short-description>
   refactor/<short-description>
   ```

5. **Implement Your Work**
   Follow best practices, write clean and readable code, and include tests
   where appropriate.

6. **Open a Pull Request (PR)**

   * Link to the Issue.
   * Use clear, descriptive titles.
   * Ensure CI tests pass.
   * Request review.

7. **Address Review Feedback**

   * Make updates as requested.
   * Keep communication clear and respectful.

8. **Merge After Approval**
   Only reviewers and maintainers can finalize the merge.

---

## 🧪 Testing Guidelines

* Add tests inside the `tests/` folder.
* Use pytest.
* Ensure coverage does not decrease.

---

## 📦 Documentation Guidelines

* Update documentation for any new feature or change.
* Use Markdown.
* Keep explanations concise but accurate.

---

## 📂 Folder Structure Expectations

Your contribution should respect the existing project layout:

```markdown
project_root/
├── data/
│ ├── download_data.py
│ ├── pima.csv
│ └── .gitkeep
├── models/
│ ├── xgb_final_model.joblib
│ ├── logreg_baseline.joblib
│ ├── scaler.joblib
│ ├── xgb_tuned.joblib
│ └── .gitkeep
├── notebooks/
│ └── exploratory_tests.ipynb
├── milestones/
│ ├── milestone0_repository_setup/
│ ├── milestone1_problem_data/
│ ├── milestone2_EDA_baseline/
│ ├── milestone3_xai/
│ ├── milestone4_model_tuning/
│ ├── milestone5_deployment/
│ └── milestone6_final_report/
├── results/
│ └── .gitkeep
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore

```

---

## 💬 Communication Standards

* Be clear and respectful.
* Keep discussion focused.
* Provide sources when making claims.

---

## 🔐 Code of Conduct

By contributing, you agree to maintain a professional environment that supports
all contributors.

---

## 🙌 Thank You

Every contribution, small or large, helps strengthen the diabetes-risk-xai
project. We appreciate your effort and look forward to collaborating!
