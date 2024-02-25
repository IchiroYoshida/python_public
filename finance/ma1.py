'''
Stock Analysis MA (Moving Average) 
2024-02-24
'''

import talib as ta
from pandas_datareader import data
import pandas as pd

Num = 25

df = pd.read_csv('./data/SP500/SPX2023.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

df['MA'] = ta.MA(df['Close'], timeperiod=Num)
df['Diff'] = (df['Close']- df['MA'] )* 100 / df['Close']

print(df.head(100))