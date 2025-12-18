# 📈 Stock Market Predictor

An end-to-end **Python stock price prediction project** that pulls real market data, performs feature engineering, trains a machine learning model, and predicts the **next-day closing price** of a stock.

This project is designed to be **portfolio-ready, interview-friendly, and beginner-to-intermediate ML focused**.

---

## 🚀 Project Overview

The goal of this project is to demonstrate a realistic data science workflow:

1. Collect historical stock data
2. Perform exploratory data analysis (EDA)
3. Engineer technical indicators
4. Train a machine learning model
5. Evaluate performance
6. Predict the next closing price

⚠️ This project is **educational** and **not financial advice**.

---

## 🧠 Skills Demonstrated

* Python programming
* Data collection using APIs
* Data cleaning & feature engineering
* Time-series awareness
* Machine learning (Linear Regression)
* Model evaluation
* Modular project structure
* Debugging & environment management

---

## 🧰 Tech Stack

* Python 3.10+
* pandas
* numpy
* scikit-learn
* yfinance
* matplotlib

---

## 📂 Project Structure

```
stock-market-predictor/
│
├── data/
│   └── stock_data.csv
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_eda.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── features.py
│   ├── model.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📥 Data Source

Stock data is pulled from **Yahoo Finance** using the `yfinance` Python library.

Example:

* Ticker: `AAPL`
* Date range: 2015 → Present

---

## ⚙️ Feature Engineering

The following features are created:

* **MA_10** – 10-day moving average
* **MA_50** – 50-day moving average
* **Daily_Return** – Percentage change of closing price
* **Volatility** – Rolling standard deviation of returns

These features are commonly used in quantitative finance.

---

## 🤖 Model

* **Algorithm**: Linear Regression (scikit-learn)
* **Target**: Closing price
* **Train/Test Split**: Time-based (no shuffling)

Why Linear Regression?

* Simple and interpretable
* Strong baseline model
* Easy to explain in interviews

---

## 📊 Evaluation Metrics

* **MAE (Mean Absolute Error)**
* **R² Score**

These metrics help assess prediction accuracy and explanatory power.

---

## 🔮 Example Output

```
Predicted next closing price: $182.47
```

(Note: Prices will vary depending on market conditions.)

---

## ▶️ How to Run

### 1️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the project

```bash
python main.py
```

---

## 🧪 Notebooks

* **01_data_collection.ipynb** – Download and save stock data
* **02_eda.ipynb** – Visualize trends and moving averages
* **03_modeling.ipynb** – Train and evaluate the ML model

---

## ⚠️ Limitations

* Stock prices are highly stochastic
* Linear regression cannot capture complex market behavior
* No macroeconomic or sentiment data included
* Past performance ≠ future results

---

## 🚀 Future Improvements

* LSTM / RNN deep learning model
* Technical indicators (RSI, MACD)
* Multi-stock prediction
* Backtesting trading strategies
* Streamlit dashboard
* Automated daily predictions

---

## 💬 Interview Talking Point

> “I built an end-to-end stock prediction system that focuses on clean data pipelines, feature engineering, and realistic evaluation rather than overpromising predictive accuracy.”

---

## 📜 Disclaimer

This project is for **educational purposes only** and does not constitute financial or investment advice.

---

⭐ If you found this project useful, feel free to star the repo!
