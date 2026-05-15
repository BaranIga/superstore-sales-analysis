import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    df = df.drop_duplicates()

    df = df.dropna()

    return df