'''
Stock Analysis MA (Moving Average) 
2024-02-24
'''

import talib as ta
from pandas_datareader import data
import pandas as pd
import random

N = 10

df = pd.read_csv('./data/SP500/SPX2023.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

df['MA'] = ta.MA(df['Close'], timeperiod=25)
df['Diff'] = ((df['Close']- df['MA'] )* 100 / df['Close']).dropna()

df2=df[df['Diff'] >=1.0]
day2 = df2.index.tolist()
sample = sorted(random.sample(day2,N))