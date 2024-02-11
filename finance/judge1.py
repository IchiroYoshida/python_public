'''
Judge1 2022-05-08
'''
import math
from pandas_datareader import data
import pandas as pd

df = pd.read_csv('data/DOW/DJI2017Ana.csv')
df = df.set_index('Date')

df['Signal'] = df['Ma25']/df['Ma75']

# calculate after starting day
df2 = df['2021-01-01':'2022-05-01']

days = df2.index.tolist()
end = len(days)
line_MSG =[]
str=''
MACD2= 0

for day in range(end):
    line_MSG.append(days[day])
    
    day_data = df2.iloc[day]
    signal = day_data['Signal']
    value  = day_data['Close']
    Ma25   = day_data['Ma25']
    Ma75   = day_data['Ma75']
    Signal = day_data['Signal']
    Max75 = day_data['Max 75']
    Min75 = day_data['Min 75']
    MACDValue = day_data['MACD']
    MACD = day_data['MACD Hist']
    RSI  = day_data['RSI']
    
    if (signal >=1.0): #Buy!
        str += 'IN'
        if(value >= Ma25):
            str += ' 100%'
        elif (value > Ma75):
            str +=' 75%'
        else:
            str +=' 50%'
        if(Max75 > 7.):
            str +=' +7% Cut!'
    else:
        str += 'OUT'
        if (value <= Ma75):
            str += ' 25%'
        elif (value < Ma25):
            str += ' 50%'
        else:
            str += ' 75%'
        if(Min75 < -7. ):
            str += ' -7% Buy!'
    if (MACD >0 ):
        str += ' MACD Buy!'
    else:
        str += ' MACD Cut!'        
    if(RSI >75):
        str += ' RSI Cut!'
    elif(RSI < 25):
        str += ' RSI Buy!'
    line_MSG.append(str)
    print(line_MSG)
    str=''
    line_MSG=[]