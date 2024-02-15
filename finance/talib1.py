'''
Stock Analysis Ta-lib
2024-02-15
'''
import talib as ta
import mplfinance as mpf
from pandas_datareader import data
import pandas as pd

df = pd.read_csv('./data/SP500/SPX2023.csv')
close = df['Close']
macd, macdsignal, _ = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
rsi14= ta.RSI(close, timeperiod=14)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

apd = [
    mpf.make_addplot(macd, panel=2, color='red', ylabel='MACD'),
    mpf.make_addplot(macdsignal, panel=2, color='blue'),
    mpf.make_addplot(macd - macdsignal, type='bar', panel=2, color='green'),
    mpf.make_addplot(rsi14,panel=3, color='red'),
]

mpf.plot(df, title ='S&P500 2023', mav=(5,25) ,type='candle', volume=True, addplot=apd)