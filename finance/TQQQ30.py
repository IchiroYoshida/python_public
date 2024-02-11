'''
Analyze Leverage ETF(TQQQ) 
2022-06-05
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Cash = 100

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
tq3_buy = tq3['1992.01.01':'1996.12.31'] 
tq3_sim = tq3['2000.01.01':'2021.12.31']

buy = tq3_buy['Adj Close']

days = tq3_sim.index.tolist()
end = len(days)

St=[]
Mean = []
X = []

for day in range(0, end, 250):
    day_data = tq3_sim.iloc[day]
    stvalue = day_data['Adj Close']
    now = (stvalue - buy) * Cash
    st = np.std(now)
    mean = np.mean(now)

    St.append(st)
    Mean.append(mean)
    X.append(day)

ax.errorbar(X, Mean, yerr=St, marker = 'o', capthick=1, capsize=10, lw=1, color='b')

ax.set_xlabel("Buy 1992.1.1-1996.12.31")
ax.set_ylabel("Value")
ax.set_yscale('log')
fig.suptitle("TQQQ Simulation. 2000.1.1- 2021.12.31")
plt.show()