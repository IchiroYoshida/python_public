'''
Simulate Leverage ETF(QLD, TQQQ) from NDX data 
2022-06-05
'''
import pandas as pd

Lev = 3.0 #TQQQ
Cost = 1.08
#Val0 = 0.087
#Value0 = 0.431471109390259 #TQQQ data 2010-02-11 ADj. Close

ndx = pd.read_csv('./data/NASDAQ/NDX.csv')
ndx = ndx.set_index('Date')
ndx0 = ndx['2010-02-11':'2011-12-31'] #Simulation period

tq3 = pd.read_csv('./data/NASDAQ/TQQQ.csv')  #2010.2.11 -
tq3 = tq3.set_index('Date')

days = ndx0.index.tolist()
end = len(days)

#Start
day_data = ndx0.iloc[0]
day_data_tq3 = tq3.iloc[0]

ValuePre = day_data['Adj Close']
ValueLev0 = day_data_tq3['Adj Close']

#Loop 
for day in range(1,end):
    day_data = ndx0.iloc[day]
    day_data_tq3 = tq3.iloc[day]

    ValueClose = day_data['Adj Close']
    ValueTQQQ = day_data_tq3['Adj Close']

    dev = (ValueClose - ValuePre)/ValuePre
    Val = ValueLev0 *(1 +Lev * dev * Cost) 

    r = Val /ValueTQQQ

    print(days[day],Val,ValueTQQQ,r)
    
    ValuePre = ValueClose
    ValueLev0 = Val