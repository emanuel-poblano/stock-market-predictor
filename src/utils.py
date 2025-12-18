import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, index_col="Date", parse_dates=True)