'''
Yahoo Stock data -> .csv    NASDAQ100(^NDX)
2022-06-04
'''
import math
from pandas_datareader import data
import pandas as pd

df = data.DataReader("^NDX","stooq",'2023-12-01','2023-12-31')
df.sort_index(inplace=True)
print(df)
#df.to_csv('data/NASDAQ/NDX2023.csv', index=True)
