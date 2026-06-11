import pandas as pd
import numpy as np

from scripts.logger import logger


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    date_cols = ["order_date", "ship_date"]

    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    float_cols = ["sales", "profit", "discount"]

    for col in float_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    int_cols = ["quantity"]

    for col in int_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    logger.info(
        f"Missing values:\n{df.isnull().sum()}"
    )

    df = df.dropna(subset=["order_date", "sales"])

    df["quantity"] = df["quantity"].fillna(
        df["quantity"].median()
    )

    df["postal_code"] = (
        df["postal_code"]
        .astype(str)
    )

    logger.info(
        f"Data cleaned. Rows after cleaning: {len(df)}"
    )

    return df


def engineer_features(df):

    df["delivery_days"] = (
        df["ship_date"] - df["order_date"]
    ).dt.days

    df["order_year"] = df["order_date"].dt.year

    df["order_month"] = df["order_date"].dt.month

    df["order_month_name"] = (
        df["order_date"].dt.month_name()
    )

    df["order_quarter"] = (
        df["order_date"].dt.quarter
    )

    df["profit_margin"] = np.where(
        df["sales"] != 0,
        df["profit"] / df["sales"],
        np.nan
    )

    df["is_profitable"] = (
        df["profit"] > 0
    )

    logger.info(
        "Feature engineering completed"
    )
    
    return df