'''
Stock Analysis from ./data/CSV
'''
from pandas_datareader import data
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import pandas as pd
import numpy as np
import math

class Estate:
    def __init__(self):
        self.cash = 1000x10000
        self.stock = 0
        self.total = self.cash + self.stock
class Stock:
    def __init__(self):
        self.volume = 0
        self.value  = 0
        self.total = self.volume * self.value

class Operation:
    def __init__(self):
        self.N = 10

    def sell(self, object):
    def buy(self,)
                
df = pd.read_csv('./data/DOW/DJI2017.csv') 

# MA(Moving Average 25 and 75 days)
df['Ma25'] = df['Close'].rolling(window=25).mean()
df['Ma75'] = df['Close'].rolling(window=75).mean()
df['Ma25&75 Signal'] = df['Ma25']/df['Ma75']

# deviation from Average 75 days
df['Max 75'] = (df['High']/df['Ma75']-1.0)*100
df['Min 75'] = (df['Low']/df['Ma75']-1.0)*100

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

df.to_csv('./data/DOW/DJI2017Ana.csv', index=False)
       