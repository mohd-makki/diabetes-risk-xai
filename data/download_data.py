"""Download the Pima Indians Diabetes dataset and save it locally."""

import os
import pandas as pd

# Ensure the 'data' folder exists
os.makedirs("data", exist_ok=True)

# Dataset URL (from UCI Repository)
URL = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"


# Column names based on dataset documentation
cols = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigree",
    "Age",
    "Outcome"
]

# Load and save dataset
df = pd.read_csv(URL, header=None, names=cols)
df.to_csv("data/pima.csv", index=False)
print("✅ Dataset downloaded successfully!")
print("Saved as: data/pima.csv")
print("Shape:", df.shape)
print(df.head())
