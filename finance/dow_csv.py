'''
Dow

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

df2.to_csv('data/LehmanShock.csv', index=True)
