import yfinance as yf
import plotly.express as px

def plot(ticker:str):
    '''
    Plot a time series.

    args:
        ticker(str): The company ticker.

    return:
        A plotly time series.
    '''
    data = yf.download(ticker, period='max', multi_level_index=False)
    df = data.reset_index()[['Date', 'close']]

    fig = px.line(df, x = 'Date', y = 'Close', title = f'historico de {ticker}')
    return fig