'''
Simulate Leverage ETF(QLD, TQQQ) from NDX data 
2022-06-04
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Lev = 3.0 #TQQQ
Cost = 1.08

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#x = pd.date_range(start='2010-02-01',end='2011-12-31',freq='M')

df = pd.read_csv('./data/NASDAQ/NDX2010.csv')
df = df.set_index('Date')

df2 = df['2010-02-11':'2022-05-31']

tq3 = pd.read_csv('./data/NASDAQ/TQQQ.csv')
tq3 = tq3.set_index('Date')

days = df2.index.tolist()
end = len(days)

#Start
day_data = df2.iloc[0]
day_data_tq3 = tq3.iloc[0]

ValuePre = day_data['Adj Close']
ValueLev0 = day_data_tq3['Adj Close']

VAL=[]
TQ3=[]
Ratio=[]

#Loop 
for day in range(1,end):
    day_data = df2.iloc[day]
    day_data_tq3 = tq3.iloc[day]
    
    ValueClose = day_data['Adj Close']
    ValueTQ3 = day_data_tq3['Adj Close']
    
    dev = (ValueClose - ValuePre)/ValuePre
    Val = ValueLev0 *(1 +Lev * dev * Cost) 

    VAL.append(Val)
    TQ3.append(ValueTQ3)
    Ratio.append(Val/ValueTQ3)
    
    ValuePre = ValueClose
    ValueLev0 = Val
    
y=np.array(TQ3)
x=np.arange(end-1)

ax.plot(x,y,label="TQQQ real")
ax.plot(x,VAL,label ="Simulated")
ax.legend()
ax.set_yscale('log')
plt.grid(which='both')

fig.suptitle("TQQQ Simulation.   2010.2.11- ")
plt.show()