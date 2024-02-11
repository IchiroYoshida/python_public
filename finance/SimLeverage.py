'''
Simulate QLD from NDX data 
2022-06-07
'''
import pandas as pd

Lev = 2.0 #QLD
Cost = 1.22

#Value0 = 1.98987054824829  #QLD data 2006-06-21 ADj. Close

ndx = pd.read_csv('./data/NASDAQ/NDX.csv')
ndx = ndx.set_index('Date')
ndx0 = ndx['2006-06-21':'2021-12-31'] #Simulation period

qld = pd.read_csv('./data/NASDAQ/QLD.csv')
qld = qld.set_index('Date')

days = ndx0.index.tolist()
end = len(days)

res = []

#Start
day_data = ndx0.iloc[0]
day_data_qld = qld.iloc[0]

ValuePre = day_data['Adj Close']
ValueLev0 = day_data_qld['Adj Close']

print(days[0],ValuePre,ValueLev0)
#res.append(days[0],ValueLev0)

#Loop 
for day in range(1,end):
    day_data = ndx0.iloc[day]
    day_data_qld = qld.iloc[day]

    ValueClose = day_data['Adj Close']
    ValueQLD = day_data_qld['Adj Close']

    dev = (ValueClose - ValuePre)/ValuePre
    Val = ValueLev0 *(1 +Lev * dev * Cost) 

    r = Val /ValueQLD
    print(days[day],ValueQLD,Val,r)
    #res.append([days[day],ValueQLD,Val,r]) 
    
    ValuePre = ValueClose
    ValueLev0 = Val

'''    
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
'''
