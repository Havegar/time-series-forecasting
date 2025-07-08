import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from math import sqrt
import os

def run_sarimax_gridsearch(series, d=2, D=1, s=12, save=True):
    """
    Realiza búsqueda de hiperparámetros SARIMAX y evalúa por RMSE y BIC.
    
    Args:
        series (pd.Series): Serie temporal (índice datetime, valores numéricos).
        d (int): Orden de diferenciación ARIMA.
        D (int): Orden de diferenciación estacional.
        s (int): Periodo estacional (e.g. 12 para datos mensuales).
        save (bool): Si True, guarda los resultados en carpeta outputs/.

    Returns:
        Tuple (best_rmse_model, best_bic_model, results_df)
    """
    
    # 1. División train/test (85%/15%)
    split_idx = int(len(series) * 0.85)
    train = series[:split_idx]
    test = series[split_idx:]
    
    # 2. Rango de hiperparámetros
    p = q = range(0, 3)
    P = Q = range(0, 3)

    results = []

    for order in [(i, d, j) for i in p for j in q]:
        for seasonal_order in [(k, D, l, s) for k in P for l in Q]:
            try:
                model = SARIMAX(train,
                                order=order,
                                seasonal_order=seasonal_order,
                                enforce_stationarity=False,
                                enforce_invertibility=False)
                fit_result = model.fit(disp=False)

                forecast = fit_result.forecast(steps=len(test))
                rmse = sqrt(mean_squared_error(test, forecast))

                results.append({
                    'order': order,
                    'seasonal_order': seasonal_order,
                    'rmse': rmse,
                    'bic': fit_result.bic
                })

            except Exception:
                continue

    # 3. Crear DataFrame con resultados
    results_df = pd.DataFrame(results)

    # 4. Seleccionar mejores modelos
    best_rmse = results_df.loc[results_df['rmse'].idxmin()]
    best_bic = results_df.loc[results_df['bic'].idxmin()]

    # 5. Guardar archivos si se solicita
    if save:
        os.makedirs("outputs", exist_ok=True)
        results_df.to_csv("outputs/sarimax_grid_results.csv", index=False)

        # Entrenar el mejor modelo para predicción final
        model = SARIMAX(train,
                        order=best_rmse['order'],
                        seasonal_order=best_rmse['seasonal_order'],
                        enforce_stationarity=False,
                        enforce_invertibility=False)
        fit_result = model.fit(disp=False)
        forecast = fit_result.forecast(steps=len(test))

        forecast_df = pd.DataFrame({
            'actual': test.values,
            'forecast': forecast.values
        }, index=test.index)

        forecast_df.to_csv("outputs/forecast_best_rmse.csv")

    else:
        # Si save=False, aún entrenamos para retornar forecast
        model = SARIMAX(train,
                        order=best_rmse['order'],
                        seasonal_order=best_rmse['seasonal_order'],
                        enforce_stationarity=False,
                        enforce_invertibility=False)
        fit_result = model.fit(disp=False)
        forecast = fit_result.forecast(steps=len(test))

    # ✅ Return fuera del if
    return best_rmse, best_bic, results_df, train, test, forecast,fit_result