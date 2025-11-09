import os
import joblib

# Set project root dynamically (one level up from app/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Paths to model and scaler
MODEL_PATH = os.path.join(PROJECT_ROOT, 'models', 'xgb_final_model.joblib')
SCALER_PATH = os.path.join(PROJECT_ROOT, 'models', 'scaler.joblib')

# Load the model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
import streamlit as st
import numpy as np
import pandas as pd

# --------------------------------------------------------------
# App Configuration
# --------------------------------------------------------------
st.set_page_config(
    page_title="Diabetes Risk XAI App",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Risk Prediction App")
st.markdown("""
Welcome!  
This app uses an **explainable AI (XAI)** model to estimate the risk of diabetes
based on clinical and biometric indicators.  
Please enter patient data in the sidebar to generate a prediction.
""")

# --------------------------------------------------------------
# Sidebar Inputs
# --------------------------------------------------------------
st.sidebar.header("Patient Data Input")

# Define input fields
pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, value=2)
glucose = st.sidebar.number_input("Glucose", min_value=0, max_value=300, value=120)
blood_pressure = st.sidebar.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.sidebar.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.sidebar.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.sidebar.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=35)

# Prepare input data
input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                        insulin, bmi, dpf, age]])
scaled_input = scaler.transform(input_data)

# --------------------------------------------------------------
# Prediction
# --------------------------------------------------------------
if st.sidebar.button("Predict Diabetes Risk"):
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    st.subheader("Prediction Result")
    st.write(f"**Predicted Class:** {'Diabetic' if prediction == 1 else 'Non-Diabetic'}")
    st.write(f"**Probability of Diabetes:** {probability:.2%}")
    st.progress(float(probability))
