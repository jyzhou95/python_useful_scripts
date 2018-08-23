import pandas as pd
import numpy as np
import datetime


def funcSimulatePnl(vec_symbols, start, end):
    lst_dates = [start + datetime.timedelta(days=x) for x in range((end-start).days + 1)]

    df_pnl = pd.DataFrame({"Date": np.tile(lst_dates, 3),
                           "Symbol": np.repeat(vec_symbols, len(lst_dates)),
                           "PnL": np.random.randint(-100, 100, len(np.tile(lst_dates, 3)))})
    return df_pnl


def funcAggregateBySymbolYear(df_pnl):
    df_pnl['Year'] = pd.DatetimeIndex(df_pnl['Date']).year
    df_pnl_sum = df_pnl.groupby(['Symbol', 'Year']).sum()
    return df_pnl_sum



if __name__ == "__main__":
    lst_symbols = ["AAPL", "GOOG", "SPY"]
    start_date = datetime.datetime(2008, 1, 1)
    end_date = datetime.datetime.now()
    df_simulated_pnl = funcSimulatePnl(lst_symbols, start_date, end_date)
    df_simulated_pnl_sum = funcAggregateBySymbolYear(df_simulated_pnl)
    print(df_simulated_pnl.sort_values(['PnL']))


