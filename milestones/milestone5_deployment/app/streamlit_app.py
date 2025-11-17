import streamlit as st
import joblib
import os
import streamlit.components.v1 as components

# -------------------------
# PATHS
# -------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

st.set_page_config(page_title="Diabetes Risk — Explainability Dashboard", layout="wide")
st.title("🔍 Diabetes Risk — XAI Dashboard (Milestone 3)")

# ---------------------------------------------------
# Helper: Load HTML files safely
# ---------------------------------------------------
def load_html(filename, height=450):
    path = os.path.join(RESULTS_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            components.html(f.read(), height=height, scrolling=True)
    else:
        st.warning(f"Artifact not found: **{filename}** — run 03_explainability.ipynb.")

# ---------------------------------------------------
# SECTIONS
# ---------------------------------------------------

st.subheader("📌 Global Explainability (SHAP)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### SHAP Global Bar Plot")
    load_html("shap_global_bar.html")

with col2:
    st.markdown("#### SHAP Beeswarm Plot")
    load_html("shap_global_beeswarm.html")

st.markdown("---")
st.subheader("📌 Local Explainability (SHAP Force Plots)")

case_index = st.number_input("Select test sample index", min_value=0, max_value=999, value=0)

force_filename = f"shap_force_idx_{int(case_index)}.html"
st.markdown(f"#### SHAP Force Plot — Case {int(case_index)}")
load_html(force_filename)

st.markdown("---")
st.subheader("📌 LIME Local Explanations")

lime_filename = f"lime_case_{int(case_index)}.html"
st.markdown(f"#### LIME Explanation — Case {int(case_index)}")
load_html(lime_filename)

st.info("If LIME/SHAP artifacts are missing, run the notebook: **03_explainability.ipynb**")
