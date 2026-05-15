import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month

    df["profit_margin"] = df["profit"] / df["sales"]

    df["is_loss"] = df["profit"] < 0

    return df