'''
Yahoo Stock data -> .csv    S&P500 (^SPX)
2024-02-20
'''
from pandas_datareader import data
import pandas as pd

df = data.DataReader("^SPX","stooq",'1974-01-01','2023-12-31')
df.sort_index(inplace=True)
#print(df)
df.to_csv('./data/SP500/SPXALL1974.csv', index=True)