import pandas as pd
from prophet import Prophet
import pickle


def run_prophet(product):

    fields = ['date',product]
    temp_dataset = pd.read_csv('./data/organize_basic_df.csv',usecols=fields)
    temp_dataset.columns = ['ds','y']
    model = Prophet(weekly_seasonality=True,daily_seasonality = True)
    model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
    model.fit(temp_dataset)
    future = model.make_future_dataframe(periods=28,include_history=False)
    forecast = model.predict(future)
    return [product,forecast]
