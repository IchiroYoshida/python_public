'''
Analyze Leverage ETF(TQQQ) 
2022-06-05
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
tq3 = tq3['2009-07-01':'2021.12.31'] 

days = tq3.index.tolist()

St=[]
Mean = []
X = []

for period in range(50,1200,50):
    end = len(days) - period
    interest = period / 250
    Gain = []

    #Loop
    for day in range(0,end):
        day_data0 = tq3.iloc[day]
        Value0 = day_data0['Adj Close']
        day_data1 = tq3.iloc[day+period]
        Value1 = day_data1['Adj Close']
        r = Value1/Value0
        gain = (r - 1.0)/interest * 100
        Gain.append(gain)

    st = np.std(Gain)
    mean = np.mean(Gain)
  
    St.append(st)
    Mean.append(mean)
    X.append(period)
    
ax.plot(X, Mean)
ax.errorbar(X, Mean, yerr=St, marker = 'o', capthick=1, capsize=10, lw=1, color='b')

ax.set_xlabel("Hold days")
ax.set_ylabel("Gain/Year (%)")
#ax.set_ylim(0,6)
fig.suptitle("TQQQ Simulation. 2009.7.1- 2021.12.31")
plt.show()