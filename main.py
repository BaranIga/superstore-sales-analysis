from src.load import load_data
from src.clean import clean_data
from src.transform import transform_data
from src.to_sql import save_to_sql

import pandas as pd

def run():
    df = load_data()
    df = clean_data(df)
    df = transform_data(df)

    df.to_csv("data/cleaned/clean_sales.csv", index=False)
    save_to_sql(df)

run()