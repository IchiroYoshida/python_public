'''
MACD AI4 2022-05-31
'''
import math
from pandas_datareader import data
import pandas as pd

Num = 100

class Stock(object):
    def __init__(self, day_stock):
        self.High = math.floor(day_stock['High'])
        self.Low = math.floor(day_stock['Low'])
        self.Open = math.floor(day_stock['Open'])
        self.Close = math.floor(day_stock['Close'])
        self.Volume = day_stock['Volume']
        # Status
        self.Ma25 = day_stock['Ma25']
        self.Ma75 = day_stock['Ma75']
        self.MACD = day_stock['MACD']
        self.MACDSignal = day_stock['MACD Signal']
        self.MACDHist = day_stock['MACD Hist']

df = pd.read_csv('./data/NDX.csv')
df = df.set_index('Date')
    
# calculate after starting day
df2 = df['2019-01-01':'2021-12-31']

days = df2.index.tolist()
end = len(days)

#Start
day_data =df2.iloc[0]

st = Stock(day_data)
Value0=st.Open

StartValue=Value0
MACD_old = 0
ope_flg = 1
gain = 1.

#Loop
for day in range(1, end-1):
    day_data = df2.iloc[day]
    st = Stock(day_data)
    Value = st.Open

    if (ope_flg ==1): #'Buy
        StartValue = Value
        ope_flg = 0
        print('Buy :',days[day],Value,gain)
    elif (ope_flg == -1): #'Sell
        SellValue = Value
        ope_flg = 0
        gain *= SellValue / StartValue 
        print('Sell:',days[day],Value,gain)
        
    st = Stock(day_data)
    MACD = st.MACDHist

    if (MACD >0):
        if (MACD_old <0):
            ope_flg = 1 #'Buy
    else:
        if (MACD_old >0):
            ope_flg = -1 #'Sell

    MACD_old = MACD

gain *= Value / StartValue
hold = Value/Value0
print('Total:',days[day],gain,hold)
