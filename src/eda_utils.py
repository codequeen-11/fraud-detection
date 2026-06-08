from os import path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def load_data(path):
    """
    Load CSV file safely.
    """

    try:
        df = pd.read_csv(path)

        logging.info(
            f"Dataset loaded successfully: {path}"
        )

        logging.info(
            f"Shape: {df.shape}"
        )

        return df

    except FileNotFoundError:
        logging.error(
            f"File not found: {path}"
        )
        raise

    except pd.errors.EmptyDataError:
        logging.error(
            f"File is empty: {path}"
        )
        raise

    except Exception as e:
        logging.error(
            f"Unexpected error loading file: {e}"
        )
        raise


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