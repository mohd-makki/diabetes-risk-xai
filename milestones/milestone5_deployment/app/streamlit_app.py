# milestones/milestone5_deployment/app/streamlit_app.py
"""
Streamlit app to demo Diabetes Risk XAI artifacts:
- Loads the best available model (xgb_tuned -> xgb_final_model -> logreg_baseline)
- Loads scaler if present
- Shows prediction + probability + severity
- Embeds SHAP/LIME HTML artifacts from the repository results/ folder
"""

from pathlib import Path
import joblib
import json
from typing import Optional, Dict
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

# -------------------------
# Paths (robust)
# -------------------------
# File lives at: .../milestones/milestone5_deployment/app/streamlit_app.py
REPO_ROOT = Path(__file__).resolve().parents[3]  # repo root
MODELS_DIR = REPO_ROOT / "models"
RESULTS_DIR = REPO_ROOT / "results"
DATA_DIR = REPO_ROOT / "data"


# -------------------------
# Helper utilities
# -------------------------
def safe_load_joblib(p: Path):
    if p.exists():
        try:
            return joblib.load(p)
        except Exception as e:
            st.warning(f"Failed to load {p.name}: {e}")
            return None
    return None


def find_best_model(models_dir: Path) -> Optional[Path]:
    # priority list
    candidates = [
        "xgb_tuned.joblib",
        "xgb_final_model.joblib",
        "logreg_baseline.joblib",
    ]
    for name in candidates:
        p = models_dir / name
        if p.exists():
            return p
    # fallback: any .joblib in models dir
    for p in models_dir.glob("*.joblib"):
        return p
    return None


def list_html_artifacts(results_dir: Path, prefix: str):
    return sorted(results_dir.glob(f"{prefix}*.html"))


def list_png_artifacts(results_dir: Path, pattern: str):
    return sorted(results_dir.glob(pattern))


def severity_label(prob: float, thresholds: Dict[str, float]):
    # thresholds: {"high":0.75, "moderate":0.5, "low":0.25}
    if prob >= thresholds["high"]:
        return "High", "🔴"
    if prob >= thresholds["moderate"]:
        return "Moderate", "🟠"
    if prob >= thresholds["low"]:
        return "Low", "🟡"
    return "Minimal", "🟢"


# -------------------------
# App config
# -------------------------
st.set_page_config(page_title="Diabetes Risk (XAI) — Demo", layout="wide")
st.title("Diabetes Risk Prediction — Explainable AI Demo")

col1, col2 = st.columns([2, 1])

# -------------------------
# Load model & scaler
# -------------------------
with col2:
    st.header("Model status")
    model_path = find_best_model(MODELS_DIR)
    scaler_path = MODELS_DIR / "scaler.joblib"

    if model_path is None:
        st.error(
            "No model artifact found in models/ — please run Milestone pipelines and save model artifacts there."
        )
        st.stop()

    model = safe_load_joblib(model_path)
    scaler = safe_load_joblib(scaler_path)

    st.success(f"Loaded model: {model_path.name}")
    if scaler is not None:
        st.info("Scaler loaded and will be applied to inputs.")
    else:
        st.info(
            "No scaler found — raw inputs will be passed to the model (ensure consistent feature scale)."
        )

    # default feature names (common order for Pima dataset)
    default_feature_names = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigree",
        "Age",
    ]
    # Try to infer from model if possible
    try:
        if hasattr(model, "feature_names_in_"):
            feature_names = list(model.feature_names_in_)
        else:
            feature_names = default_feature_names
    except Exception:
        feature_names = default_feature_names

    st.write("Feature order used:", feature_names)

# -------------------------
# Severity thresholds (customizable)
# -------------------------
SEVERITY_THRESHOLDS = {"high": 0.75, "moderate": 0.50, "low": 0.25}

# -------------------------
# Prediction UI
# -------------------------
with col1:
    st.header("Predict a sample")
    st.markdown("Enter feature values (use realistic clinical ranges).")

    # Build a form for inputs
    with st.form("predict_form"):
        inputs = {}
        for feat in feature_names:
            # choose sensible defaults
            if feat.lower().startswith("preg"):
                val = st.number_input(
                    feat, min_value=0.0, max_value=20.0, value=0.0, step=1.0
                )
            elif feat.lower() in ("age",):
                val = st.number_input(
                    feat, min_value=0.0, max_value=120.0, value=30.0, step=1.0
                )
            elif feat.lower() in (
                "glucose",
                "bloodpressure",
                "skin thickness",
                "insulin",
                "bmi",
            ):
                val = st.number_input(feat, min_value=0.0, max_value=1000.0, value=50.0)
            else:
                val = st.number_input(feat, value=0.0)
            inputs[feat] = float(val)
        submitted = st.form_submit_button("Predict")

    if submitted:
        X_in = pd.DataFrame([inputs])[feature_names]  # ensure ordering
        # apply scaler if available
        try:
            if scaler is not None:
                X_proc = scaler.transform(X_in)
            else:
                X_proc = X_in.values
        except Exception as e:
            st.error(f"Error applying scaler: {e}")
            X_proc = X_in.values

        # Predict
        try:
            # handle classifiers with predict_proba or decision_function
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(X_proc)[0, 1]
            elif hasattr(model, "predict"):
                # fallback: model.predict may give class label; attempt decision_function then sigmoid
                pred_raw = model.predict(X_proc)[0]
                proba = float(pred_raw)
            else:
                st.error("Model does not support probability predictions.")
                proba = 0.0

            label, icon = severity_label(proba, SEVERITY_THRESHOLDS)
            st.metric("Predicted risk (probability)", f"{proba:.3f}")
            st.markdown(f"**Severity**: {icon} **{label}**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# -------------------------
# Show available XAI artifacts
# -------------------------
st.subheader("Explainability artifacts (from results/)")
col_a, col_b = st.columns(2)

# SHAP force HTMLs
shap_htmls = list_html_artifacts(RESULTS_DIR, "shap_force_case_")
lime_htmls = list_html_artifacts(RESULTS_DIR, "lime_case_")
shap_pngs = list_png_artifacts(RESULTS_DIR, "shap_summary_*.png")
other_pngs = list_png_artifacts(RESULTS_DIR, "*.png")

with col_a:
    st.markdown("#### SHAP force plots (interactive)")
    if shap_htmls:
        choices = [p.name for p in shap_htmls]
        pick = st.selectbox("Choose SHAP force HTML", choices, key="shap_force")
        if pick:
            path = RESULTS_DIR / pick
            try:
                html = path.read_text(encoding="utf-8")
                components.html(html, height=420, scrolling=True)
            except Exception as e:
                st.error(f"Failed to load {pick}: {e}")
    else:
        st.info(
            "No SHAP force HTML files found in results/ (e.g. shap_force_case_3.html)"
        )

with col_b:
    st.markdown("#### LIME HTML outputs")
    if lime_htmls:
        choices = [p.name for p in lime_htmls]
        pick = st.selectbox("Choose LIME HTML", choices, key="lime")
        if pick:
            path = RESULTS_DIR / pick
            try:
                html = path.read_text(encoding="utf-8")
                components.html(html, height=420, scrolling=True)
            except Exception as e:
                st.error(f"Failed to load {pick}: {e}")
    else:
        st.info("No LIME HTML files found in results/ (e.g. lime_case_3.html)")

# Static PNGs (SHAP summary / calibration)
st.markdown("#### Static images (summary plots)")
if shap_pngs:
    for p in shap_pngs:
        st.image(str(p), caption=p.name)
elif other_pngs:
    for p in other_pngs:
        st.image(str(p), caption=p.name)
else:
    st.info("No PNG artifacts found in results/")

# -------------------------
# Show metadata & summary
# -------------------------
meta_path = RESULTS_DIR / "xai_metadata.json"
if meta_path.exists():
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        st.sidebar.header("XAI metadata")
        st.sidebar.json(meta)
    except Exception:
        st.sidebar.text("Failed to read xai_metadata.json")

# quick download of summary text if exists
summary_txt = RESULTS_DIR / "xai_summary.txt"
if summary_txt.exists():
    with open(summary_txt, "r", encoding="utf-8") as f:
        text = f.read()
    st.markdown("#### XAI Summary")
    st.text(
        text[:1000]
        + (
            "...\n(see full summary in results/xai_summary.txt)"
            if len(text) > 1000
            else ""
        )
    )

st.markdown("---")
st.caption(
    f"Repo root: {REPO_ROOT} — Models dir: {MODELS_DIR} — Results dir: {RESULTS_DIR}"
)
