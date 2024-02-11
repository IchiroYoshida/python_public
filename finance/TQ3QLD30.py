'''
Analyze Leverage ETF(QLD and TQQQ) 
2022-06-12
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Cash = 100

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# TQQQ ---------------------------------------
tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
tq3_buy = tq3['1992.01.01':'1996.12.31'] 
tq3_sim = tq3['2000.01.01':'2021.12.31']

buy = tq3_buy['Adj Close']

days = tq3_sim.index.tolist()
end = len(days)

TQ3_St=[]
TQ3_Mean = []
TQ3_X = []

for day in range(0, end, 250):
    day_data = tq3_sim.iloc[day]
    stvalue = day_data['Adj Close']
    now = (stvalue - buy) * Cash
    st = np.std(now)
    mean = np.mean(now)

    TQ3_St.append(st)
    TQ3_Mean.append(mean)
    TQ3_X.append(day)

#----------------------------------------TQQQ 

#QLD ----------------------------------------
qld = pd.read_csv('./data/NASDAQ/QLDs.csv')
qld = qld.set_index('Date')
qld_buy = qld['1992.01.01':'1996.12.31'] 
qld_sim = qld['2000.01.01':'2021.12.31']

buy = qld_buy['Adj Close']

days = qld_sim.index.tolist()
end = len(days)

QLD_St=[]
QLD_Mean = []
QLD_X = []

for day in range(0, end, 250):
    day_data = qld_sim.iloc[day]
    stvalue = day_data['Adj Close']
    now = (stvalue - buy) * Cash
    st = np.std(now)
    mean = np.mean(now)

    QLD_St.append(st)
    QLD_Mean.append(mean)
    QLD_X.append(day)

#----------------------------------------QLD 
ax.errorbar(TQ3_X, TQ3_Mean, yerr=TQ3_St, marker = 'o', capthick=1, capsize=10, lw=1, color='b',label ='TQQQ')
ax.errorbar(QLD_X, QLD_Mean, yerr=QLD_St, marker = '*', capthick=1, capsize=10, lw=1, color='r',label ='QLD')
#ax.plot(TQ3_X,TQ3_Mean,label = "TQQQ")
#ax.plot(QLD_X,QLD_Mean,label = "QLD")
ax.legend()
ax.grid(color='b', linestyle=':', linewidth=0.3)
ax.set_xlabel("Buy 1992.1.1-1996.12.31")
ax.set_ylabel("Value")
ax.set_yscale('log')
fig.suptitle("TQQQ and QLD Simulation. 2000.1.1- 2021.12.31")
plt.show()