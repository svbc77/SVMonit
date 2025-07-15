
import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html
from utils import load_data, forecast_price

app = Dash(__name__)
server = app.server

df = load_data()

# Grafico MVRV
mvrv_fig = go.Figure()
mvrv_fig.add_trace(go.Scatter(x=df['date'], y=df['mvrv_total'], mode='lines+markers', name='MVRV Totale'))
mvrv_fig.add_trace(go.Scatter(x=df['date'], y=df['sth_mvrv'], mode='lines+markers', name='STH-MVRV'))
mvrv_fig.add_trace(go.Scatter(x=df['date'], y=df['lth_mvrv'], mode='lines+markers', name='LTH-MVRV'))
mvrv_fig.update_layout(title='Andamento MVRV', xaxis_title='Data', yaxis_title='Valore')

# Previsione
forecast = forecast_price(df)
forecast_fig = go.Figure()
forecast_fig.add_trace(go.Scatter(x=forecast.index, y=forecast, mode='lines', name='Forecast'))
forecast_fig.update_layout(title='Previsione Prezzo BTC a 6 mesi')

app.layout = html.Div([
    html.H1("Dashboard Bitcoin completa"),
    dcc.Graph(figure=mvrv_fig),
    dcc.Graph(figure=forecast_fig)
])

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=10000)
