# 📈 Time Series Forecasting with SARIMAX

This project explores the modeling and forecasting of time series data using classical statistical methods, with a focus on **SARIMAX (Seasonal ARIMA with Exogenous Variables)**.

It aims to balance **inference and prediction**, providing a clean, modular, and reproducible implementation that emphasizes both **model interpretability** and **forecasting accuracy**.

---

## 🌟 Project Objectives

- Model a real-world univariate time series (monthly air passengers)
- Understand the theoretical underpinnings of ARIMA/SARIMA/SARIMAX models
- Explore model selection using both **inferential** and **predictive** criteria
- Evaluate models based on residual analysis and forecasting error
- Forecast future values and visualize seasonal trends

---

## 🧠 Why Time Series Models Matter

Time series forecasting is essential across many industries — from finance and energy to retail and health. A good time series model not only provides accurate forecasts but also:

- Helps understand underlying patterns (trend, seasonality, noise)
- Supports decision-making grounded in temporal dynamics
- Enables hypothesis testing about the data-generating process

---

## 🧰 Tools and Techniques

### 🔹 ARIMA Family

- **ARIMA (AutoRegressive Integrated Moving Average)**\
  Captures autocorrelation and non-stationarity.
- **SARIMA (Seasonal ARIMA)**\
  Adds seasonal autoregressive and moving average components.
- **SARIMAX**\
  Extends SARIMA to include exogenous variables (not used here but framework-ready).

### 🔹 Model Components

- `p`, `d`, `q`: Non-seasonal ARIMA terms (autoregressive, differencing, moving average)
- `P`, `D`, `Q`, `s`: Seasonal counterparts + seasonal period `s` (e.g., 12 for monthly data)
- The full model is written as: SARIMAX(p, d, q)(P, D, Q, s)

---

## 🔎 Model Selection: Inference vs Prediction

We compare models using two complementary goals:

- **Inference**: Understanding the structure of the series using information criteria\
  → Optimized using **BIC (Bayesian Information Criterion)**

- **Prediction**: Minimizing forecast error on unseen data\
  → Evaluated using **RMSE (Root Mean Squared Error)** on a test set

---

## 🧪 Diagnostics and Stationarity

Before fitting models, the following steps are performed:

- **Dickey-Fuller test** (ADF):\
  Checks for stationarity; if the p-value is low, the series is stationary.

- **Autocorrelation Function (ACF)** and **Partial Autocorrelation Function (PACF)**:\
  Used to identify potential values of `p` and `q`, and detect seasonality patterns.

- **Residual analysis**:\
  After fitting, residuals are checked for normality, autocorrelation, and zero mean.

---

## 📂 Project Structure

```
time-series-forecasting/
├── data/
│   └── raw/
│       └── AirPassengers.csv
├── notebooks/
│   └── eda_and_modeling.ipynb
├── outputs/
│   ├── sarimax_grid_results.csv
│   └── forecast_best_rmse.csv
├── src/
│   └── modeling.py
├── requirements.txt
└── README.md
```

---

## 📊 Results

- Models are selected using a **grid search** over SARIMAX hyperparameters.
- Both **inference (BIC)** and **prediction (RMSE)** are reported.
- Best model forecasts are plotted and compared against the test set.
- Final model is trained on the full series to forecast future values.

---

## 📌 Future Work

- Include exogenous variables (X) for SARIMAX
- Extend to multivariate time series
- Compare with machine learning methods (e.g., XGBoost, LSTM)
- Deploy via API or interactive dashboard

---

## 🛆 Requirements

All dependencies are listed in `requirements.txt`. To install:

```bash
pip install -r requirements.txt
```

---

## ✍️ Author

**Henry Vega** – [Havegar on GitHub](https://github.com/Havegar)\
Passionate about data, astronomy, and understanding the hidden patterns in time.

---

## 📘 References

- Box, G. E. P., Jenkins, G. M., Reinsel, G. C. (2015). *Time Series Analysis: Forecasting and Control*.
- Shumway, R. H., & Stoffer, D. S. (2017). Time Series Analysis and Its Applications: With R Examples (4th ed.). Springer.
- Hyndman, R. J., & Athanasopoulos, G. (2018). *Forecasting: Principles and Practice*.
- [Statsmodels Documentation](https://www.statsmodels.org/stable/tsa.html)

