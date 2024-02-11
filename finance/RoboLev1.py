'''
Analyze Leverage ETF(TQQQ) from NDX data 
2022-06-05
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
tq3 = tq3['2003-01-01':'2015.12.31'] #Lheman Shock 2003-2015

days = tq3.index.tolist()

St=[]
Mean= []
X = []
for period in range(10,1000,100):
    end = len(days) - period
    Ratio = []
    #Loop
    for day in range(0,end):
        day_data0 = tq3.iloc[day]
        Value0 = day_data0['Adj Close']
        day_data1 = tq3.iloc[day+period]
        Value1 = day_data1['Adj Close']
        r = Value1/Value0
        Ratio.append(r)

    st = np.std(Ratio)
    mean = np.mean(Ratio)
  
    St.append(st)
    Mean.append(mean)
    X.append(period)
    
ax.plot(X, Mean)
ax.errorbar(X, Mean, yerr=St, marker = 'o', capthick=1, capsize=10, lw=1, color='r')

ax.set_xlabel("Hold days")
ax.set_ylabel("Yield ratio")
ax.set_ylim(0,6)
fig.suptitle("TQQQ Yield ratio Simulation.   2003 - 2015")
plt.show()

