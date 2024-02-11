'''
Robot 1 2022-05-07
'''
import math
from pandas_datareader import data
import pandas as pd

df = pd.read_csv('data/1545.csv')
df = df.set_index('Date')

# MA(Mean Average) 25days and 75days
df['Ma25'] = df['Close'].rolling(window=25).mean()
df['Ma75'] = df['Close'].rolling(window=75).mean()

df['Signal'] = df['Ma25']/df['Ma75']

# calculate after starting day
df2 = df['2018-01-01':'2021-12-31']

days = df2.index.tolist()
end = len(days)

#Start
Cash = 1000 * 10000
day_data =df2.iloc[0]
SValue = math.floor(day_data['Open'])
SNum = math.floor(Cash/SValue)
Tot_Stock_Value = SValue * SNum
Tot_Cash_Value = Cash - Tot_Stock_Value
Buy = False
Cut = True

daily_res = [days[0],'{:.3f}'.format(day_data['Signal']),
         SValue, SNum, Tot_Stock_Value, Tot_Cash_Value]

for day in range(1,end-1):
    day_data = df2.iloc[day]
    signal = day_data['Signal']
    if (signal >=1.0): #Buy!
        if (Buy):
            SValue = math.floor(day_data['Open'])
            SNum = math.floor(Tot_Cash_Value/SValue)
            Tot_Stock_Value = SValue * SNum
            Tot_Cash_Value -=  Tot_Stock_Value
            Buy = False
            Cut = True
    else:               #Cut!
        if (Cut):
            SValue = math.floor(day_data['Open'])
            Sell_Value = SValue * SNum
            Tot_Cash_Value += Sell_Value
            Tot_Stock_Value = 0
            SNum = 0
            Cut =False
            Buy =True
            
    SValue = math.floor(day_data['Close'])
    Tot_Stock_Value = SValue*SNum
    Tot_Estate = Tot_Stock_Value + Tot_Cash_Value
    
    daily_res.append([days[day],'{:.3f}'.format(day_data['Signal']),
         SValue, SNum, Tot_Stock_Value, Tot_Cash_Value]) 
    
print(daily_res)
