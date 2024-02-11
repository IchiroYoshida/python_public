'''
Simulate QLD from NDX data 
2022-06-12
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Lev = 2.0 #QLD
Cost = 1.0
QLD0 = 0.2344  #1992.1.2 -

ndx0 = pd.read_csv('./data/NASDAQ/NDX.csv')
ndx0 = ndx0.set_index('Date')

ndx = ndx0['1992-01-02':'2006-06-21']
days = ndx.index.tolist()
end = len(days)

res = []

day_data = ndx.iloc[0]
ValuePre = day_data['Adj Close']
ValueLev0 = QLD0

res.append([days[0],ValueLev0])
           
#Loop 
for day in range(1,end-1):
    day_data = ndx.iloc[day]
    
    ValueClose = day_data['Adj Close']
    
    dev = (ValueClose - ValuePre)/ValuePre
    Val = ValueLev0 *(1 +Lev * dev * Cost) 

    res.append([days[day],Val])
    
    ValuePre = ValueClose
    ValueLev0 = Val

#Real QLD 2006.6.21 -
qld = pd.read_csv('./data/NASDAQ/QLD.csv')
qld = qld.set_index('Date')

days = qld.index.tolist()
end = len(days)

for day in range(0, end):
    day_data = qld.iloc[day]
    ValueClose = day_data['Adj Close']
    
    res.append([days[day],ValueClose])

sim = pd.DataFrame(data=res, columns=['Date','Adj Close'])
sim = sim.set_index('Date')

sim.to_csv('./data/NASDAQ/QLDs.CSV',index=True)

