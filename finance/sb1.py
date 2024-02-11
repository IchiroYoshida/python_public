'''
Dow Sell and Buy!

'''
from pandas_datareader import data
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import pandas as pd
import numpy as np

df = pd.read_csv('./data/dow_ana2021.csv')
df.set_index('Date', inplace=True)
days = df.index.tolist()

start = 75
end = len(days)

for day in range(start, end):
    date = days[day]
    data = df.loc[date]
    signal = data['Signal']
    if (signal >=1.0): 
        print(date,"Buy!")
    else:
        print(date,"Cut!")
