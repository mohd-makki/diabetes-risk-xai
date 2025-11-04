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
    "Outcome",
]

# Load and save dataset
df = pd.read_csv(URL, header=None, names=cols)
df.to_csv("data/pima.csv", index=False)
print("✅ Dataset downloaded successfully!")
print("Saved as: data/pima.csv")
print("Shape:", df.shape)
print(df.head())

# --- Quick integrity check ---
print("\n🔍 Quick Data Integrity Check:")
print("Number of missing values per column:")
print(df.isnull().sum())

# Check for basic stats (helps verify numeric ranges)
print("\nSummary statistics:")
print(df.describe())

# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")

if duplicates > 0:
    print("Consider removing duplicates for cleaner data.")
# End of script
