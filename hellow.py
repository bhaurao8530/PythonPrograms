
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller

# Load your time series data
# You can read data from a CSV file or another source
# Example data is created for illustration purposes.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
dates = pd.date_range(start='2023-01-01', periods=len(data), freq='D')
time_series = pd.Series(data, index=dates)

# Plot the original time series data
plt.figure(figsize=(10, 5))
plt.plot(time_series)
plt.title('Original Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Check for stationarity using the Augmented Dickey-Fuller Test
result = adfuller(time_series)
print("ADF Statistic:", result[0])
print("p-value:", result[1])
print("Critical Values:", result[4])

# If the data is not stationary, difference it
if result[1] > 0.05:
    differenced_series = time_series.diff().dropna()
    plt.figure(figsize=(10, 5))
    plt.plot(differenced_series)
    plt.title('Differenced Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

    # Recheck for stationarity
    result = adfuller(differenced_series)
    print("ADF Statistic after differencing:", result[0])
    print("p-value after differencing:", result[1])
    print("Critical Values after differencing:", result[4])

# Fit an ARIMA model to the time series data
model = ARIMA(time_series, order=(1, 1, 1))
model_fit = model.fit(disp=0)

# Make predictions
forecast_steps = 5
forecast, stderr, conf_int = model_fit.forecast(steps=forecast_steps)

# Plot the forecasted values
plt.figure(figsize=(10, 5))
plt.plot(time_series, label='Original Data')
plt.plot(pd.date_range(start=time_series.index[-1], periods=forecast_steps, freq='D'), forecast, label='Forecast')
plt.fill_between(
    pd.date_range(start=time_series.index[-1], periods=forecast_steps, freq='D'),
    conf_int[:, 0],
    conf_int[:, 1],
    color='k',
    alpha=0.2,
    label='Confidence Interval'
)
plt.title('ARIMA Time Series Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

print("Forecasted values:", forecast)
