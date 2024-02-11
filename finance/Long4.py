'''
Analyze Leverage ETF(QLD and TQQQ) Funded investment for 10 years.
Bottom fishing pattern.
2022-06-26
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

N = 1000

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# TQQQ ---------------------------------------
tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
tq0 = tq3['2008.10.1':'2009.9.30']
tq1 = tq3['2009.10.1':'2022.5.31']

days0 = tq0.index.tolist()
end0 = len(days0)
days1 = tq1.index.tolist()
end1 = len(days1)

for t in range(N):
    Stocks =  []

    day0 = random.randint(0, end0-20*10)
    day_data0 = tq0.iloc[day0]
    stvalue0 = day_data0['Adj Close']
    Stocks.append(stvalue0)
    
    # Buy, 10 times per a month.
    for buy in range(1, 10):
        dd = random.randint(-10,10)
        day = day0 + buy*20 + dd
           
        day_data = tq0.iloc[day]
        stvalue = day_data['Adj Close']
        Stocks.append(stvalue)
    stave = np.mean(Stocks)

    Val = []
    for day in range(250,end1,250):
        day_data = tq1.iloc[day]
        stvalue = day_data['Adj Close']
        val = (stvalue - stave)/stave
        Val.append(val)
    
    if (t < 1):
        df = pd.DataFrame(Val)
    else:
        Re = pd.Series(Val)
        df = pd.concat([df,Re],axis=1)

#print(df)

TQ3_Mean = []
TQ3_St = []

for y in range(12):
    mean = np.mean(df.iloc[y])
    st = np.std(df.iloc[y])
    TQ3_Mean.append(mean)
    TQ3_St.append(st)
  
# QLD ---------------------------------------
qld = pd.read_csv('./data/NASDAQ/QLDs.csv')
qld = qld.set_index('Date')
ql0 = qld['2008.10.1':'2009.9.30']
ql1 = qld['2009.10.1':'2022.5.31']

days0 = ql0.index.tolist()
end0 = len(days0)
days1 = ql1.index.tolist()
end1 = len(days1)

for t in range(N):
    Stocks =  []

    day0 = random.randint(0, end0-20*10)
    day_data0 = ql0.iloc[day0]
    stvalue0 = day_data0['Adj Close']
    Stocks.append(stvalue0)
    
    # Buy, 10 times per a month.
    for buy in range(1, 10):
        dd = random.randint(-10,10)
        day = day0 + buy*20 + dd
           
        day_data = ql0.iloc[day]
        stvalue = day_data['Adj Close']
        Stocks.append(stvalue)
    stave = np.mean(Stocks)

    Val = []
    for day in range(250,end1,250):
        day_data = ql1.iloc[day]
        stvalue = day_data['Adj Close']
        val = (stvalue - stave)/stave
        Val.append(val)
    
    if (t < 1):
        df = pd.DataFrame(Val)
    else:
        Re = pd.Series(Val)
        df = pd.concat([df,Re],axis=1)

QLD_Mean = []
QLD_St = []

for y in range(12):
    mean = np.mean(df.iloc[y])
    st = np.std(df.iloc[y])
    QLD_Mean.append(mean)
    QLD_St.append(st)
  
X = np.arange(1,13)

ax.errorbar(X, TQ3_Mean, yerr=TQ3_St, marker = 'o', capthick=1, capsize=10, lw=1, color='b',label ='TQQQ')
ax.errorbar(X, QLD_Mean, yerr=QLD_St, marker = '*', capthick=1, capsize=10, lw=1, color='r',label ='QLD')
ax.legend()

ax.grid(color='b', linestyle=':', linewidth=0.3)

ax.set_xlabel("Buy 10 times. 2008.10.1-2009.9.30   (Years after)")
ax.set_ylabel("Total times.")
fig.suptitle("TQQQ and QLD Simulation. ")
plt.yscale('log')
plt.show()