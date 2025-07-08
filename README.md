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

- **Understanding the Dynamics Behind the Data**
Time series data reflect processes evolving over time, often influenced by factors like trends (long-term growth or decline), seasonality (regular patterns repeating at fixed intervals), and noise (random fluctuations). Time series models help disentangle these components, revealing the structure hidden in complex temporal data. This understanding is critical to interpreting what is happening in the system, not just what might happen next.
- **Supporting Informed Decision-Making**
Decisions in business and policy often depend on anticipating future conditions. For example, an energy company needs to predict demand to optimize production; retailers want to forecast sales to manage inventory effectively; healthcare providers may monitor patient vitals over time to detect anomalies early. Time series models provide a quantitative foundation for decisions that depend on temporal trends, making strategies more robust and responsive.
- **Enabling Hypothesis Testing and Causal Insights**
Beyond forecasting, time series analysis enables testing hypotheses about the underlying data-generating mechanisms. For instance, are observed changes due to seasonal effects, or external shocks? Does a new marketing campaign affect sales trends? Models can incorporate interventions, identify structural breaks, and help infer causal relationships — aspects that are often hidden without temporal context.
- **Handling Complex Temporal Dependencies**
Time series models explicitly account for autocorrelation — the fact that past values influence future ones — which is ignored in many traditional statistical models. This allows capturing intricate temporal patterns and dependencies that are essential for realistic modeling and accurate forecasting.
- **Adapting to Changing Environments**
Many time series models can incorporate changes in behavior over time, such as evolving trends or shifts in seasonal patterns. This flexibility ensures that models remain relevant even as the underlying processes evolve, which is common in dynamic real-world systems.

---

## 🧰 Tools and Techniques

🔹 ARIMA Family

The ARIMA family of models is one of the most widely used and powerful frameworks for time series analysis, especially when dealing with data that show autocorrelation and non-stationarity.
**ARIMA (AutoRegressive Integrated Moving Average)**

ARIMA models combine three key aspects:
**AutoRegressive (AR)** part: The model explains the current value of the series as a linear combination of its previous values (lags). This captures autocorrelation, or how past values influence the present. The number of lagged terms is denoted by p.
**Integrated (I)** part: This represents differencing the data to make it stationary (i.e., stable mean and variance over time). Differencing removes trends or other non-stationarities. The order of differencing is denoted by d.
**Moving Average (MA)** part: The model also explains the current value based on past forecast errors (residuals). The order of this component is denoted by q.
In short, ARIMA(p, d, q) models the series based on its own past values, past errors, and differences to stabilize the data.

**SARIMA (Seasonal ARIMA)**
Many time series have seasonal patterns that repeat every fixed period (e.g., monthly sales, quarterly GDP). SARIMA extends ARIMA by adding seasonal components that capture this behavior.
- Seasonal autoregressive terms (P) capture dependencies at seasonal lags (e.g., 12 months ago).
- Seasonal differencing (D) removes seasonal trends to achieve stationarity.
- Seasonal moving average terms (Q) capture seasonal noise patterns.
- The seasonal period s defines the length of the seasonality (e.g., s = 12 for monthly data with annual seasonality).
- SARIMAX (Seasonal ARIMA with eXogenous regressors)
This is a further extension of SARIMA that allows inclusion of external variables (exogenous regressors) which might help explain the series. For example, including promotional campaigns, weather variables, or economic indicators as predictors. While not always used, this flexibility allows richer modeling.

⸻

🔹 Model Components Explained

`p` (AR order): Number of lag observations included in the model (how many past values influence the present).
`d` (Differencing order): Number of times the data have been differenced to remove trends and make the series stationary.
`q` (MA order): Number of lagged forecast errors in the prediction equation (how many past errors influence the present).
`P` (Seasonal AR order): Number of seasonal autoregressive terms (lags at multiples of the seasonal period).
`D` (Seasonal differencing order): Number of seasonal differences to remove seasonal trends.
`Q` (Seasonal MA order): Number of seasonal moving average terms (seasonal errors).
`s` (Seasonal period): Number of time steps in one seasonal cycle (e.g., 12 for monthly data with yearly seasonality).

⸻

🧩 Full SARIMAX Model Notation

The full model is represented as:

SARIMAX(p, d, q)(P, D, Q, s)

Where:
	•	The first triplet (p, d, q) models the non-seasonal part.
	•	The second triplet (P, D, Q) along with the seasonal period s models the seasonal component.

Example:
SARIMAX(1, 1, 1)(0, 1, 1, 12) means:
	•	Non-seasonal AR(1), differencing once, MA(1).
	•	Seasonal differencing once, seasonal MA(1) with seasonality of 12 periods (e.g., months).

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

