import pandas as pd
import random
from datetime import datetime, timedelta

rows = []

start_date = datetime(2025, 1, 1)

for i in range(365):

    date = start_date + timedelta(days=i)

    # Seasonal temperature pattern
    temperature = round(
        30 + 5 * ((i % 365) / 365) +
        random.uniform(-2, 2),
        1
    )

    # Seasonal humidity pattern
    humidity = round(
        75 - 20 * ((i % 365) / 365) +
        random.uniform(-5, 5),
        1
    )

    # Wind speed variation
    windspeed = round(
        10 + random.uniform(-3, 3),
        1
    )

    rows.append([
        date.strftime("%Y-%m-%d"),
        temperature,
        humidity,
        windspeed
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "Date",
        "temperature",
        "humidity",
        "windspeed"
    ]
)

df.to_csv(
    "weather.csv",
    index=False
)

print("weather.csv created with 365 rows")