import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    df = pd.read_csv(path)
    print(f"Shape: {df.shape}")
    return df


def dataset_overview(df):
    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicates")
    print(df.duplicated().sum())

    display(df.head())


def missing_value_report(df):
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100

    report = pd.DataFrame({
        "missing_count": missing,
        "missing_pct": missing_pct
    })

    return report[report["missing_count"] > 0]