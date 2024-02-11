'''
NASDAQ 100(^NDX) 2022-06-02 
'''
from pandas_datareader import data
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import pandas as pd
import numpy as np

#end = dt.date.today()
end = dt.date(2022,5,31)

#start = end - dt.timedelta(days=400)
start = dt.date(2019,1,1)

df = data.DataReader("^NDX","yahoo",start,end)
df.sort_index(inplace=True)

# MA(Moving Average 25 and 75 days)
df['Ma25'] = df['Close'].rolling(window=25).mean()
df['Ma75'] = df['Close'].rolling(window=75).mean()
df['Ma25&75 Signal'] = df['Ma25']/df['Ma75']

# MACD(12,26,9) daily ---------------
exp12 = df['Close'].ewm(span=12, adjust=False).mean()
exp26 = df['Close'].ewm(span=26, adjust=False).mean()
df['MACD'] = exp12 - exp26

# Signal
df['MACD Signal'] = df['MACD'].rolling(window=9).mean()

# Histogram (MACD - Signal)
df['MACD Hist'] = df['MACD'] - df['MACD Signal']

# MACD Weekly
exp12w = df['Close'].ewm(span=12*5, adjust=False).mean()
exp26w = df['Close'].ewm(span=26*5, adjust=False).mean()
df['MACDw'] = exp12w - exp26w

#Signal Weekly
df['MACDw Signal'] = df['MACDw'].rolling(window=9).mean()

# Histogram (MACDw - Signalw)
df['MACDw Hist'] = df['MACDw'] - df['MACDw Signal']

# MACD Monthly
exp12m = df['Close'].ewm(span=12*30, adjust=False).mean()
exp26m = df['Close'].ewm(span=26*30, adjust=False).mean()
df['MACDm'] = exp12m - exp26m

#Signal Monthly
df['MACDm Signal'] = df['MACDm'].rolling(window=9).mean()

# Histogram (MACDm - Signalm)
df['MACDm Hist'] = df['MACDm'] - df['MACDm Signal']

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

df.to_csv('data/NDX2.csv', index=True)