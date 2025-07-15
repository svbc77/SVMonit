
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def load_data():
    df = pd.read_csv('sample_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

def forecast_price(df):
    df = df.dropna()
    df['price'] = df['price'].astype(float)
    series = df.set_index('date')['price']
    last_date = series.index[-1]
    future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=180)
    forecast = pd.Series(np.poly1d(np.polyfit(range(len(series)), series, 2))(range(len(series), len(series) + 180)), index=future_dates)
    return forecast
