# milestones/milestone5_deployment/app/streamlit_app.py
"""
Milestone 5 Streamlit app: Diabetes Risk + XAI viewer

this file at:
milestones/milestone5_deployment/app/streamlit_app.py

Run (from repo root):
streamlit run milestones/milestone5_deployment/app/streamlit_app.py
"""

import json
from pathlib import Path
from typing import List, Optional

import joblib
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# -------------------------
# Config / paths
# -------------------------
HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]  # moves up to repo root (diabetes_risk_xia)
MODELS_DIR = REPO_ROOT / "models"
RESULTS_DIR = REPO_ROOT / "results"

# --- Model filenames ---
TUNED_MODEL = MODELS_DIR / "xgb_tuned.joblib"
FINAL_MODEL = MODELS_DIR / "xgb_final_model.joblib"
FALLBACK_MODEL = MODELS_DIR / "logreg_baseline.joblib"

# --- Severity thresholds ---
SEVERITY_THRESHOLDS = {
    "low": 0.20,
    "moderate": 0.50,  # p < 0.20 -> low; 0.20 <= p < 0.50 -> moderate; p >= 0.50 -> high
}

# --- Load model safely ---
if TUNED_MODEL.exists():
    model = joblib.load(TUNED_MODEL)
elif FINAL_MODEL.exists():
    model = joblib.load(FINAL_MODEL)
elif FALLBACK_MODEL.exists():
    model = joblib.load(FALLBACK_MODEL)
else:
    st.error(
        "❌ No model available. Please place a model file in /models/ and restart the app."
    )

# Example: load scaler if needed
scaler_path = MODELS_DIR / "scaler.joblib"
if scaler_path.exists():
    scaler = joblib.load(scaler_path)
else:
    scaler = None

# Nice colors for severity
SEVERITY_COLORS = {
    "low": "#2ecc71",  # green
    "moderate": "#f39c12",  # orange
    "high": "#e74c3c",  # red
}


# -------------------------
# Helpers
# -------------------------
def safe_load_model() -> Optional[object]:
    """Load the best available model (tuned -> final -> fallback)."""
    if TUNED_MODEL.exists():
        return joblib.load(TUNED_MODEL)
    if FINAL_MODEL.exists():
        return joblib.load(FINAL_MODEL)
    if FALLBACK_MODEL.exists():
        return joblib.load(FALLBACK_MODEL)
    return None


def list_html_artifacts(prefix: str) -> List[Path]:
    """List HTML artifacts in results folder with given prefix."""
    return sorted(list(RESULTS_DIR.glob(f"{prefix}*.html")))


def render_html_file(p: Path, height: int = 400) -> None:
    """Render an HTML artifact inside the app."""
    try:
        html = p.read_text(encoding="utf-8")
        components.html(html, height=height, scrolling=True)
    except (FileNotFoundError, OSError, ValueError) as e:
        st.error(f"Unable to render {p.name}: {e}")


def severity_bucket(probability: float) -> str:
    """Map probability to a severity label: low/moderate/high."""
    if probability < SEVERITY_THRESHOLDS["low"]:
        return "low"
    if probability < SEVERITY_THRESHOLDS["moderate"]:
        return "moderate"
    return "high"


# -------------------------
# App
# -------------------------
st.set_page_config(page_title="Diabetes Risk (XAI)", layout="wide")
st.title("Diabetes Risk — Predict & Explain (XAI)")

# Sidebar
st.sidebar.header("Model & Artifacts")
model = safe_load_model()
if model:
    st.sidebar.success(f"Loaded model: {model.__class__.__name__}")
else:
    st.sidebar.warning(
        "No model found in /models/ (place xgb_tuned.joblib or "
        "xgb_final_model.joblib)"
    )

st.sidebar.markdown(
    "**Explainability artifacts** (saved by `03_explainability.ipynb`):"
)
shap_htmls = list_html_artifacts("shap_force")
lime_htmls = list_html_artifacts("lime_case")
pngs = sorted(list(RESULTS_DIR.glob("*.png")))

if shap_htmls:
    st.sidebar.markdown(f"- {len(shap_htmls)} SHAP force HTML(s) found")
else:
    st.sidebar.info("No SHAP force HTML artifacts found (run the XAI notebook)")

if lime_htmls:
    st.sidebar.markdown(f"- {len(lime_htmls)} LIME HTML(s) found")
else:
    st.sidebar.info("No LIME HTML artifacts found (run the XAI notebook)")
if pngs:
    st.sidebar.markdown(f"- {len(pngs)} static plot PNG(s) found")
else:
    st.sidebar.info("No static PNGs found in /results/")

# Tabs
tab1, tab2, tab3 = st.tabs(["Predict", "Explainability (XAI)", "About"])

# ---------- Predict tab ----------
with tab1:
    st.header("Predict a single patient")

    # Load example data (if available)
    demo_df = None
    pima_path = REPO_ROOT / "data" / "pima.csv"
    if pima_path.exists():
        try:
            demo_df = pd.read_csv(pima_path).head(5)
        except (
            FileNotFoundError,
            pd.errors.EmptyDataError,
            pd.errors.ParserError,
            OSError,
        ):
            demo_df = None

    # Collect inputs (features)
    st.markdown("Enter patient features (use reasonable clinical values):")
    cols = st.columns(4)
    # Expected features order: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
    # BMI, DiabetesPedigree, Age
    with cols[0]:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
        glucose = st.number_input(
            "Glucose", min_value=0.0, max_value=300.0, value=120.0, step=1.0
        )
    with cols[1]:
        bp = st.number_input(
            "BloodPressure", min_value=0.0, max_value=200.0, value=70.0, step=1.0
        )
        skin = st.number_input(
            "SkinThickness", min_value=0.0, max_value=100.0, value=20.0, step=1.0
        )
    with cols[2]:
        insulin = st.number_input(
            "Insulin", min_value=0.0, max_value=1000.0, value=79.0, step=1.0
        )
        bmi = st.number_input(
            "BMI", min_value=0.0, max_value=100.0, value=25.0, step=0.1
        )
    with cols[3]:
        dpf = st.number_input(
            "DiabetesPedigree", min_value=0.0, max_value=10.0, value=0.5, step=0.01
        )
        age = st.number_input("Age", min_value=0, max_value=120, value=33)

    if st.button("Predict risk"):
        if model is None:
            st.error(
                "No model available. Place a model file in /models/ and restart the app."
            )
        else:
            # Prepare input in the order used by the model
            features = np.array(
                [[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]], dtype=float
            )
            try:
                # check if model expects scaled input (we assume saved scaler used in training)
                # Prefer to read scaler from models dir if available
                scaler_path = MODELS_DIR / "scaler.joblib"
                if scaler_path.exists():
                    scaler = joblib.load(scaler_path)
                    features_scaled = scaler.transform(
                        pd.DataFrame(
                            features,
                            columns=[
                                "Pregnancies",
                                "Glucose",
                                "BloodPressure",
                                "SkinThickness",
                                "Insulin",
                                "BMI",
                                "DiabetesPedigree",
                                "Age",
                            ],
                        )
                    )
                else:
                    # fallback: feed raw (model might handle internally)
                    features_scaled = features
            except (FileNotFoundError, OSError, ValueError, AttributeError):
                features_scaled = features

            prob = float(model.predict_proba(features_scaled)[:, 1][0])
            pred_label = int(prob >= 0.5)
            sev = severity_bucket(probability=prob)
            color = SEVERITY_COLORS[sev]

            st.metric("Predicted probability (class=1)", f"{prob:.3f}")
            st.markdown(f"**Predicted label:** {pred_label}")
            severity_html = (
                f"**Severity:** <span style='color:{color};font-weight:700'>"
                f"{sev.upper()}</span>"
            )
            st.markdown(severity_html, unsafe_allow_html=True)

            # Offer download of a minimal JSON containing the result
            out = {"probability": prob, "label": pred_label, "severity": sev}
            st.download_button(
                "Download result (JSON)",
                json.dumps(out, indent=2),
                file_name="prediction_result.json",
            )

# ---------- Explainability tab ----------
with tab2:
    st.header("Explainability artifacts (SHAP / LIME)")

    # SHAP force HTML viewer
    st.subheader("SHAP force plots (interactive)")
    if shap_htmls:
        shap_choice = st.selectbox(
            "Select SHAP force plot", [p.name for p in shap_htmls]
        )
        selected = RESULTS_DIR / shap_choice
        render_html_file(selected, height=450)
        st.download_button(
            "Download HTML", data=selected.read_bytes(), file_name=selected.name
        )
    else:
        st.info(
            "No SHAP force HTML found. Run the XAI notebook to generate HTML artifacts "
            "(03_explainability.ipynb)."
        )

    # LIME HTML viewer
    st.subheader("LIME explanations (HTML)")
    if lime_htmls:
        lime_choice = st.selectbox(
            "Select LIME file", [p.name for p in lime_htmls], key="lime_choice"
        )
        selected_lime = RESULTS_DIR / lime_choice
        render_html_file(selected_lime, height=450)
        st.download_button(
            "Download LIME HTML",
            data=selected_lime.read_bytes(),
            file_name=selected_lime.name,
        )
    else:
        st.info(
            "No LIME HTML found. Run the XAI notebook to generate LIME artifacts "
            "(03_explainability.ipynb)."
        )

    # Static PNGs (optional)
    st.subheader("Saved PNG visualizations (static)")
    if pngs:
        sel_png = st.selectbox("Select PNG", [p.name for p in pngs], key="png_choice")
        st.image(RESULTS_DIR / sel_png)
        st.download_button(
            "Download PNG", data=(RESULTS_DIR / sel_png).read_bytes(), file_name=sel_png
        )
    else:
        st.info("No static report PNGs found in /results/")

# ---------- About ----------
with tab3:
    st.header("About this app")
    st.markdown(
        "This app shows model predictions and pre-computed explainability artifacts "
        "(SHAP force HTML, LIME HTML) generated by the XAI notebook "
        "(`03_explainability.ipynb`). Artifacts must exist in the repository `results/` folder."
    )
    st.markdown(
        "**Important:** This application is for demonstration and educational purposes only. "
        "Do not use it for clinical decision-making without proper validation."
    )
