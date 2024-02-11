'''
Simulate Leverage ETF(QLD, TQQQ) from NDX data 
2022-06-05
'''
import pandas as pd

Lev = 3.0 #TQQQ
Cost = 1.08
Val0 = 0.087
#Value0 = 0.431471109390259 #TQQQ data 2010-02-11 ADj. Close

ndx = pd.read_csv('./data/NASDAQ/NDX.csv')
ndx = ndx.set_index('Date')
ndx0 = ndx['1992-01-01':'2010-02-10'] #Simulation period

tq3 = pd.read_csv('./data/NASDAQ/TQQQ.csv')
tq3 = tq3.set_index('Date')

days = ndx0.index.tolist()
end = len(days)

res = []

#Start
day_data = ndx0.iloc[0]
#day_data_tq3 = tq3.iloc[0]

ValuePre = day_data['Adj Close']
ValueLev0 = Val0

res.append([days[0],Val0])

#VAL[]

#Loop 
for day in range(1,end):
    day_data = ndx0.iloc[day]
    
    ValueClose = day_data['Adj Close']
    
    dev = (ValueClose - ValuePre)/ValuePre
    Val = ValueLev0 *(1 +Lev * dev * Cost) 

    #print(days[day],Val)
    res.append([days[day],Val]) 
    
    ValuePre = ValueClose
    ValueLev0 = Val
    
 #Real TQQQ (2010.2.11 - )
days = tq3.index.tolist()
end = len(days)
 
for day in range(0, end):
    day_data = tq3.iloc[day]
     
    ValueClose = day_data['Adj Close']
    
    res.append([days[day],ValueClose])

sim = pd.DataFrame(data=res,columns=['Date','Adj Close'])
sim = sim.set_index('Date')

sim.to_csv('./data/NASDAQ/TQQQs.CSV',index=True)