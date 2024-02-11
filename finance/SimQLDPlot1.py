'''
Simulate QLD from NDX data 
2022-06-07
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Lev = 2.0 #QLD
Cost = 1.0

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

df = pd.read_csv('./data/NASDAQ/NDX.csv')
df = df.set_index('Date')

df2 = df['2006-06-21':'2021-12-31']

qld = pd.read_csv('./data/NASDAQ/QLD.csv')
qld = qld.set_index('Date')

days = df2.index.tolist()
end = len(days)

#Start
day_data = df2.iloc[0]
day_data_qld = qld.iloc[0]

ValuePre = day_data['Adj Close']
ValueLev0 = day_data_qld['Adj Close']

VAL=[]
QLD=[]
Ratio=[]

#Loop 
for day in range(1,end):
    day_data = df2.iloc[day]
    day_data_qld = qld.iloc[day]
    
    ValueClose = day_data['Adj Close']
    ValueQLD = day_data_qld['Adj Close']
    
    dev = (ValueClose - ValuePre)/ValuePre
    Val = ValueLev0 *(1 +Lev * dev * Cost) 

    VAL.append(Val)
    QLD.append(ValueQLD)
    Ratio.append(Val/ValueQLD)
    
    ValuePre = ValueClose
    ValueLev0 = Val
    
#y=np.array(QLD)
x=np.arange(end-1)
#print(VAL,QLD,Ratio)

#ax.plot(x,Ratio)
ax.plot(x,QLD,label="QLD real")
ax.plot(x,VAL,label ="Simulated")
ax.legend()
ax.set_yscale('log')
plt.grid(which='both')

fig.suptitle("QLD Simulation.   2006.6.21- ")
plt.show()