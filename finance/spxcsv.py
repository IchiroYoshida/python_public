'''
Yahoo Stock data -> .csv    S&P500 (^SPX)
2024-02=12
'''
import math
from pandas_datareader import data
import pandas as pd

df = data.DataReader("^SPX","stooq",'2023-12-01','2023-12-31')
df.sort_index(inplace=True)
print(df)
#df.to_csv('data/NASDAQ/NDX2023.csv', index=True)
