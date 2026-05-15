import sqlite3
import pandas as pd

def save_to_sql(df, db_path="data/db/superstore.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()