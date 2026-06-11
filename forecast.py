import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.statespace.sarimax import SARIMAX


def forecast_series(series, days):

    model = SARIMAX(
        series,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    fitted = model.fit(
        disp=False
    )

    forecast = fitted.forecast(
        steps=days
    )

    noise = np.random.normal(
        0,
        0.3,
        days
    )

    forecast = forecast + noise

    return forecast


def make_prediction(parameter, month):

    df = pd.read_csv(
        "weather.csv"
    )

    df["Date"] = pd.to_datetime(
        df["Date"]
    )

    month_map = {
        "January":31,
        "February":59,
        "March":90,
        "April":120,
        "May":151,
        "June":181,
        "July":212,
        "August":243,
        "September":273,
        "October":304,
        "November":334,
        "December":365
    }

    target_days = month_map.get(
        month,
        181
    )

    future_dates = pd.date_range(
        start=df["Date"].max() +
        pd.Timedelta(days=1),
        periods=target_days
    )

    if parameter == "all":

        result = pd.DataFrame({
            "Date": future_dates
        })

        plt.figure(
            figsize=(12, 6)
        )

        for metric in [
            "temperature",
            "humidity",
            "windspeed"
        ]:

            forecast = forecast_series(
                df[metric],
                target_days
            )

            result[
                metric
            ] = forecast.values

            plt.plot(
                future_dates,
                forecast,
                label=metric
            )

        plt.legend()
        plt.grid()

        plt.title(
            f"{month} Weather Forecast"
        )

        plt.savefig(
            "output.png"
        )

        plt.close()

        return result.tail(31)

    forecast = forecast_series(
        df[parameter],
        target_days
    )

    result = pd.DataFrame({
        "Date": future_dates,
        parameter: forecast.values
    })

    plt.figure(
        figsize=(12, 6)
    )

    plt.plot(
        df["Date"],
        df[parameter],
        label="Historical"
    )

    plt.plot(
        future_dates,
        forecast,
        '--',
        label="Forecast"
    )

    plt.legend()
    plt.grid()

    plt.title(
        f"{parameter.capitalize()} Forecast"
    )

    plt.savefig(
        "output.png"
    )

    plt.close()

    return result.tail(31)