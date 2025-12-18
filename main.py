import yfinance as yf
from src.features import add_features
from src.model import StockModel


# Download data
df = yf.download("AAPL", start="2015-01-01")


# Add features
df = add_features(df)


X = df[["MA_10", "MA_50", "Volatility"]]
y = df["Close"]


# Train model
model = StockModel()
model.train(X, y)


# Predict next day
latest_features = X.iloc[-1:].values
prediction = model.predict(latest_features)


print("Predicted next closing price:", round(float(prediction[0]), 2))
