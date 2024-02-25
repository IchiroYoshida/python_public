'''
Stock Analysis Daily -> Weekly 
2024-02-19
'''

import talib as ta
from pandas_datareader import data
import pandas as pd

agg_dict = {
    "Open":"first",
    "High":"max",
    "Low":"min",
    "Close":"last",
    "Volume":"sum"
}

df = pd.read_csv('./data/SP500/SPX2023.csv')
df['Date'] = pd.to_datetime(df['Date'])

df_week = df.set_index("Date").resample("W").agg(agg_dict)
print(df_week.head(10))