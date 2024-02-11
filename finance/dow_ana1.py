'''
Dow

'''
from pandas_datareader import data
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import pandas as pd
import numpy as np

df = pd.read_csv('./data/dow2021.csv')

df['Ma25'] = df['Close'].rolling(window=25).mean()
df['Ma75'] = df['Close'].rolling(window=75).mean()

df['Signal'] = df['Ma25']/df['Ma75']

df.to_csv('./data/dow_ana2021.csv', index=False)