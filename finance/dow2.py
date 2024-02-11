'''
Dow

'''
from pandas_datareader import data
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import pandas as pd
import numpy as np

df = data.DataReader("^DJI","yahoo",start="2021-01-01",end="2021-12-31")
df.sort_index(inplace=True)

df['Ma25'] = df['Close'].rolling(window=25).mean()
df['Ma75'] = df['Close'].rolling(window=75).mean()

df['Ma25P'] = df['Ma25']/df['Close']
df['Ma75P'] = df['Ma75']/df['Close']

df['Judge'] 
print(df)

#df2=df[['Open','High','Low','Close','Volume']]
#mpf.plot(df2,type='candle',mav=(5,25,75),volume=True)

