import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA = Path(".")  # Change this to the folder containing the CSV files

customers = pd.read_csv(DATA / "customers.csv")
loans = pd.read_csv(DATA / "loans.csv")
repayments = pd.read_csv(DATA / "repayments.csv")
transactions = pd.read_csv(DATA / "transactions.csv")
branches = pd.read_csv(DATA / "branches.csv")

# Start here: profile each table before cleaning it.
for name, frame in {
    "customers": customers,
    "loans": loans,
    "repayments": repayments,
    "transactions": transactions,
    "branches": branches,
}.items():
    print(f"\\n--- {name.upper()} ---")
    print("Shape:", frame.shape)
    print(frame.head())
    print(frame.info())
    print(frame.isna().sum().sort_values(ascending=False).head(10))
