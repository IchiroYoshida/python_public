'''
Analyze Leverage ETF(TQQQ) from NDX data 
2022-06-05
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Units = 500
step = 10
interest = Units/250

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
tq3 = tq3['2006-01-01':'2015.12.31'] #

days = tq3.index.tolist()
end= len(days) - Units

St=[]
Mean= []
X = []

Ratio = []

#Loop
for day in range(0,end,1):
    day_data0 = tq3.iloc[day]
    Value0 = day_data0['Adj Close']
    day_data1 = tq3.iloc[day+Units]
    Value1 = day_data1['Adj Close']
    r = Value1/Value0
    Ratio.append(r)
    
for day in range(0,end,step*5):
    R = Ratio[day:day+Units]
    st = np.std(R)
    gain = (np.mean(R) - 1.0 )/interest * 100 # %
    St.append(st)
    Mean.append(gain)
    
X = np.arange(0,end,step*5)

ax.plot(X, Mean)
ax.errorbar(X, Mean, yerr=St, marker = 'o', capthick=1, capsize=10, lw=1, color='g')

ax.set_xlabel("Days 2009-")
ax.set_ylabel("Gain (%)")
#ax.set_ylim(0,6)
fig.suptitle("TQQQ Simulation. 1000 days yield  2009 - ")
plt.show()

