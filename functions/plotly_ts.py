import yfinance as yf
import plotly.expresse as px

def plot(ticker:str):

    data = yf.download(ticker, period='max', multi_level_index=False)
    df = data.reset_index()[['Date', 'close']]

    fig = px.line(df, x = 'Date', y = 'Close', title = f'historico de {ticker}')
    return fig