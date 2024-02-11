'''
Dow　Lehman Sock 2008-2009
'''
from pandas_datareader import data
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import pandas as pd
import numpy as np

df = data.DataReader("^DJI","yahoo",start="2008-01-01",end="2009-12-31")
df.sort_index(inplace=True)
df2=df[['Open','High','Low','Close','Volume']]

mpf.plot(df2,type='candle',mav=(5,25,75),volume=True)