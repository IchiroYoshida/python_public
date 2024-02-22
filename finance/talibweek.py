'''
Stock Analysis Ta-lib (Weekly,Monthly)
2024-02-20
'''
import talib as ta
import mplfinance as mpf

from pandas_datareader import data
import pandas as pd

agg_dict = {
    "Open":"first",
    "High":"max",
    "Low":"min",
    "Close":"last",
    "Volume":"sum"
}

df = pd.read_csv('./data/SP500/SPXALL1974.csv')
df['Date'] = pd.to_datetime(df['Date'])

df_week = df.set_index('Date').resample('M').agg(agg_dict)

close = df_week['Close']
macd, macdsignal, _ = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
rsi14= ta.RSI(close, timeperiod=14)

#df_week.set_index('Date',inplace=True)

apd = [
    mpf.make_addplot(macd, panel=2, color='red', ylabel='MACD'),
    mpf.make_addplot(macdsignal, panel=2, color='blue'),
    mpf.make_addplot(macd - macdsignal, type='bar', panel=2, color='green'),
    mpf.make_addplot(rsi14,panel=3, color='red', ylabel='RSI'),
]

mpf.plot(df_week, title ='S&P500 1974 - 2023 Monthly', mav=(5,25) ,type='candle', yscale='log',volume=True, addplot=apd)