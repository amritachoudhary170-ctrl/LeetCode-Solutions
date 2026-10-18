import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')

    prev = weather['temperature'].shift(1)
    prev_date = weather['recordDate'].shift(1)

    mask = (
        (weather['temperature'] > prev) &
        ((weather['recordDate'] - prev_date).dt.days == 1)
    )

    return weather.loc[mask, ['id']]