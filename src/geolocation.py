import pandas as pd
import numpy as np
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def prepare_fraud_data(df):
    """
    Prepare fraud dataset for IP mapping.
    """
    df = df.copy()

    df["ip_address"] = (
        pd.to_numeric(
            df["ip_address"],
            errors="coerce"
        )
    )

    df = df.dropna(subset=["ip_address"])

    
def convert_ip_column(df):
    """
    Convert IP addresses safely.
    """

    df = df.copy()

    try:

        df["ip_address"] = pd.to_numeric(
            df["ip_address"],
            errors="coerce"
        )

        invalid_ips = (
            df["ip_address"]
            .isnull()
            .sum()
        )

        if invalid_ips > 0:

            logging.warning(
                f"{invalid_ips} invalid IP addresses found."
            )

            df = df.dropna(
                subset=["ip_address"]
            )

        df["ip_address"] = (
            df["ip_address"]
            .astype("int64")
        )

        return df

    except KeyError:
        raise KeyError(
            "Column 'ip_address' not found."
        )

    except Exception as e:
        logging.error(
            f"IP conversion failed: {e}"
        )
        raise

    

def prepare_country_data(ip_df):

    required_columns = [
        "lower_bound_ip_address",
        "upper_bound_ip_address",
        "country"
    ]

    missing_cols = [
        col for col in required_columns
        if col not in ip_df.columns
    ]

    if missing_cols:
        raise ValueError(
            f"Missing required columns: {missing_cols}"
        )

    try:

        ip_df = ip_df.copy()

        ip_df["lower_bound_ip_address"] = (
            pd.to_numeric(
                ip_df["lower_bound_ip_address"],
                errors="coerce"
            )
        )

        ip_df["upper_bound_ip_address"] = (
            pd.to_numeric(
                ip_df["upper_bound_ip_address"],
                errors="coerce"
            )
        )

        ip_df = ip_df.dropna()

        return ip_df

    except Exception as e:

        logging.error(
            f"Country dataset preparation failed: {e}"
        )

        raise    
 

def map_ip_to_country(
    fraud_df,
    country_df
):

    try:

        merged = pd.merge_asof(
            fraud_df.sort_values("ip_address"),
            country_df.sort_values(
                "lower_bound_ip_address"
            ),
            left_on="ip_address",
            right_on="lower_bound_ip_address",
            direction="backward"
        )

        merged = merged[
            merged["ip_address"]
            <= merged["upper_bound_ip_address"]
        ]

        unmatched = (
            merged["country"]
            .isnull()
            .sum()
        )

        logging.info(
            f"Unmatched IPs: {unmatched}"
        )

        return merged

    except Exception as e:

        logging.error(
            f"Country mapping failed: {e}"
        )

        raise

def fraud_by_country(df):
    """
    Fraud count by country.
    """
    return (
        df.groupby("country")["class"]
        .sum()
        .sort_values(ascending=False)
    )


def fraud_rate_by_country(df):
    """
    Fraud rate by country.
    """
    return (
        df.groupby("country")["class"]
        .mean()
        .sort_values(ascending=False)
    )


def transaction_count_by_country(df):
    """
    Transaction count by country.
    """
    return (
        df["country"]
        .value_counts()
    )