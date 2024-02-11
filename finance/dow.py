'''
Dow　Analysis 
'''
from pandas_datareader import data
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import pandas as pd
import numpy as np

df = data.DataReader("^DJI","yahoo",start="2021-01-01",end="2022-05-07")
df.sort_index(inplace=True)
df2=df[['Open','High','Low','Close','Volume']]

# MACD
exp12 = df2['Close'].ewm(span=12, adjust=False).mean()
exp26 = df2['Close'].ewm(span=26, adjust=False).mean()
df2['MACD'] = exp12 - exp26

# Signal
df2['MACD Signal'] = df2['MACD'].rolling(window=9).mean()

# Histogram (MACD - Signal)
df2['MACD Hist'] = df2['MACD'] - df2['MACD Signal']

# RSI(Relative Strength Index) -------------------------
df_diff = df2['Close'].diff()

df_up, df_down = df_diff.copy(), df_diff.copy()
df_up[df_up < 0] = 0
df_down[df_down >0 ] = 0
df_down = df_down * -1

#Average 14 days
sim14_up = df_up.rolling(window=14).mean()
sim14_down = df_down.rolling(window=14).mean()

# RSI
df2['RSI'] = sim14_up / (sim14_up + sim14_down) * 100

# Plot MACD and Signal
add_plot = [mpf.make_addplot(df2['MACD'], ylabel='MACD', color='m', panel=1, secondary_y=False),\
        mpf.make_addplot(df2['MACD Signal'], color='c', panel=1, secondary_y=False),\
        mpf.make_addplot(df2['MACD Hist'], type='bar', color='g', panel=1, secondary_y=True),\
        mpf.make_addplot(df2['RSI'], ylabel='RSI', panel=2)]

mpf.plot(df2,title='Dow 2022', type='candle',mav=(25,75),volume=True,\
        addplot=add_plot, volume_panel=3, savefig='./data/DOW/DJI2022.png')
        