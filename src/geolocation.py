import pandas as pd
import numpy as np


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

    df["ip_address"] = (
        df["ip_address"]
        .astype("int64")
    )

    return df


def prepare_country_data(ip_df):
    """
    Prepare IP-country mapping dataset.
    """
    ip_df = ip_df.copy()

    ip_df["lower_bound_ip_address"] = (
        ip_df["lower_bound_ip_address"]
        .astype("int64")
    )

    ip_df["upper_bound_ip_address"] = (
        ip_df["upper_bound_ip_address"]
        .astype("int64")
    )

    ip_df = ip_df.sort_values(
        "lower_bound_ip_address"
    )

    return ip_df


def map_ip_to_country(fraud_df, country_df):
    """
    Perform range-based IP lookup.
    """

    fraud_df = fraud_df.sort_values(
        "ip_address"
    )

    merged = pd.merge_asof(
        fraud_df,
        country_df,
        left_on="ip_address",
        right_on="lower_bound_ip_address",
        direction="backward"
    )

    merged = merged[
        merged["ip_address"]
        <= merged["upper_bound_ip_address"]
    ]

    return merged


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