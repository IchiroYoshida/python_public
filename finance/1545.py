'''
Dow 
'''
from pandas_datareader import data
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import pandas as pd
import numpy as np

end = dt.date.today()
start = end - dt.timedelta(days=400)

df = data.DataReader("1545.T","yahoo",start,end)
df.sort_index(inplace=True)

# MA(Moving Average 25 and 75 days)
df['Ma25'] = df['Close'].rolling(window=25).mean()
df['Ma75'] = df['Close'].rolling(window=75).mean()
df['Ma25&75 Signal'] = df['Ma25']/df['Ma75']

# MACD
exp12 = df['Close'].ewm(span=12, adjust=False).mean()
exp26 = df['Close'].ewm(span=26, adjust=False).mean()
df['MACD'] = exp12 - exp26

# Signal
df['MACD Signal'] = df['MACD'].rolling(window=9).mean()

# Histogram (MACD - Signal)
df['MACD Hist'] = df['MACD'] - df['MACD Signal']

# RSI(Relative Strength Index) -------------------------
df_diff = df['Close'].diff()

df_up, df_down = df_diff.copy(), df_diff.copy()
df_up[df_up < 0] = 0
df_down[df_down >0 ] = 0
df_down = df_down * -1

#Average 14 days
sim14_up = df_up.rolling(window=14).mean()
sim14_down = df_down.rolling(window=14).mean()

# RSI
df['RSI'] = sim14_up / (sim14_up + sim14_down) * 100

# Plot MACD and Signal
add_plot = [mpf.make_addplot(df['MACD'], ylabel='MACD', color='m', panel=1, secondary_y=False),\
        mpf.make_addplot(df['MACD Signal'], color='c', panel=1, secondary_y=False),\
        mpf.make_addplot(df['MACD Hist'], type='bar', color='g', panel=1, secondary_y=True),\
        mpf.make_addplot(df['RSI'], ylabel='RSI', panel=2)]
        
mpf.plot(df,title='1545', type='candle',mav=(25,75),volume=True,\
        addplot=add_plot, volume_panel=3 ,savefig='./data/1545.png')

df.to_csv('data/1545Analyze.csv', index=True)