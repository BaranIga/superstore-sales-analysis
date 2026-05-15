import pandas as pd

def load_data(path="data/raw/sample-superstore.csv"):
    df = pd.read_csv(path, encoding="latin1")
    return df