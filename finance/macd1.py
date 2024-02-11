'''
MACD Judge1 2022-05-31
'''
import math
from pandas_datareader import data
import pandas as pd

df = pd.read_csv('data/NDX.csv')
df = df.set_index('Date')

# calculate after starting day
df2 = df['2019-02-01':'2022-05-31']

days = df2.index.tolist()
end = len(days)
line_MSG =[]
str=''
MACD_old =0

for day in range(end):
    line_MSG.append(days[day])
    
    day_data = df2.iloc[day]
    value  = day_data['Close']
    Ma25   = day_data['Ma25']
    Ma75   = day_data['Ma75']
    MACDValue = day_data['MACD']
    MACD = day_data['MACD Hist']

    if (MACD >0):
        if (MACD_old < 0):
            str += 'MACD Buy'
    else:
        if (MACD_old > 0):
            str += 'MACD Sell'
    
    line_MSG.append(str)
    print(line_MSG)
    str=''
    line_MSG=[]
    MACD_old = MACD
