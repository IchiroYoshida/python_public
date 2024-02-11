'''
Simulate Leverage ETF(QLD, TQQQ) from NDX data 
2022-06-04
'''
from pandas_datareader import data
import pandas as pd

Lev = 2.0 #QLD
Value0 = 2.257812976837160 #QLD data

df = pd.read_csv('./data/NASDAQ/NDX2006.csv')
df = df.set_index('Date')

df2 = df['2006-06-21':'2006-12-31']
days = df2.index.tolist()
end = len(days)

#Start
day_data = df2.iloc[0]
ValuePre = day_data['Close']
ValueLev0 = Value0

print(days[0],ValuePre,ValueLev0)

#Loop 
for day in range(1,end):
    day_data = df2.iloc[day]
    ValueClose = day_data['Close']
    dev = (ValueClose - ValuePre)/ValuePre
    Val = ValueLev0 *(1 +Lev * dev) 
    
    print(days[day],ValueClose,dev,Val)
    
    ValuePre = ValueClose
    ValueLev0 = Val
    
    