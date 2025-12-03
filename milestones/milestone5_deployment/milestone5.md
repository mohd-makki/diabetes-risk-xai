# milestone5.md Deployment and Communication (Interactive Streamlit App)

## Objective

Deliver a production-ready interactive web app (Streamlit) that:

- Accepts user input for patient features
- Produces a diabetes risk probability using the tuned model
- Maps predicted probability to a clinical Severity bucket (Low / Moderate /  
  High)
- Displays interactive explainability artifacts (SHAP force HTML, LIME HTML)
- Provides downloads for artifacts and the model

## Severity mapping (chosen approach)

We use **probability thresholds** to map risk probability (p) to severity:

- **Low** : p < 0.20 (green)
- **Moderate** : 0.20 ≤ p < 0.50 (amber)
- **High** : p ≥ 0.50 (red)

These thresholds are tunable and should be reviewed with clinical stakeholders.

## Deliverables

- `app/streamlit_app.py` — main Streamlit app (this directory)
- `README.md` — deployment/readme
- Model artifacts (expected in root `models/`):
  - `xgb_tuned.joblib` (preferred)
  - fallback: `xgb_final_model.joblib`
- `results/` — explainability artifacts (SHAP force HTMLs, LIME htmls) created
   by Milestone 3 notebook

## How the app supports reproducibility & transparency

- The app does not compute SHAP/LIME live. It reads pre-computed artifacts from
  `results/` (fast and stable).
- SHAP force plots are saved as HTML (interactive) and embedded via
  `components.html`.
- LIME is saved as HTML and displayed within the app.

## Security and privacy

- This app is for demonstration only and **must not** be used for clinical
  decision-making without proper validation.
- Avoid putting real patient data into demo/demo servers.
