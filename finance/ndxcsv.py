'''
Yahoo Stock data -> .csv    NASDAQ100(^NDX)
2024-02-11
'''
import math
import datetime
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd

symbol = '^NDX'
start = datetime.datetime(2023,12,1)
end = datetime.datetime(2023,12,31)

yf.pdr_override()

data = pdr.get_data_yahoo(tickers=symbol,start=start,end=end)

print(data)

#df.sort_index(inplace=True)
#df.to_csv('data/NASDAQ/NDX2023.csv', index=True)
