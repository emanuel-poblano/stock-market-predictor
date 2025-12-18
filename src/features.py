import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()  # Fixed indentation
    df["MA_10"] = df["Close"].rolling(10).mean()
    df["MA_50"] = df["Close"].rolling(50).mean()
    df["Daily_Return"] = df["Close"].pct_change()
    df["Volatility"] = df["Daily_Return"].rolling(10).std()
    return df.dropna()
