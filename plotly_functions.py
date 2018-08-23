import pandas as pd
import pandas_datareader.data as web
import numpy as np
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='alexzhou04', api_key='mmhM6t0GevuwXdsNhuS1')

def calcReturns(df_stock_price):
    df_close = df_stock_price['Close']
    df_returns = df_close / df_close.shift(1) - 1
    return df_returns

if __name__ == "__main__":
    """
    Practicing pandas data frame in Python.
    Our data set will be BBY's stock price
    """

    # Read BBY stock price
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime.now()
    df_bby = web.DataReader("BBY", "morningstar", start, end)
    df_bby['Returns'] = calcReturns(df_bby)
    df_bby = df_bby.dropna(subset = ["Returns"])
    volatility = np.std(df_bby["Returns"])
    avg_return = np.mean(df_bby["Returns"])
    df_bby_final = pd.DataFrame({'id': range(1, len(df_bby.index) + 1),
                                 'Returns': sorted(df_bby['Returns'])})
    trace = go.Scatter(x=df_bby_final['id'],
                       y=df_bby_final['Returns'],
                       mode='markers',
                       name='markers'
                       )
    layout = {
        'shapes': [
            {
                'type': 'line',
                'x0': 1,
                'x1': len(df_bby.index),
                'y0': avg_return + volatility,
                'y1': avg_return + volatility,
                'line': {
                    'color': 'rgb(55, 128, 191)',
                    'width': 3,
                }
            },
            {
                'type': 'line',
                'x0': 1,
                'x1': len(df_bby.index),
                'y0': avg_return - volatility,
                'y1': avg_return - volatility,
                'line': {
                    'color': 'rgb(55, 128, 191)',
                    'width': 3,
                }
            },
            {
                'type': 'line',
                'x0': 1,
                'x1': len(df_bby.index),
                'y0': avg_return - volatility,
                'y1': avg_return - volatility,
                'line': {
                    'color': 'rgb(55, 128, 191)',
                    'width': 3,
                }
            },
            {
                'type': 'line',
                'x0': 1,
                'x1': len(df_bby.index),
                'y0': avg_return,
                'y1': avg_return,
                'line': {
                    'color': 'rgb(128, 0, 128)',
                    'width': 3,
                    'dash': 'dot',
                }
            }
        ]
    }

    data = [trace]

    fig = {
        'data': data,
        'layout': layout,
    }
    py.plot(fig, filename='scatter-mode')
