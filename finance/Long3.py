'''
Analyze Leverage ETF(QLD and TQQQ) Funded investment for 10 years.
2022-06-25
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

N = 10000

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# TQQQ ---------------------------------------
tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
days = tq3.index.tolist()
end = len(days)

for t in range(N):
    Results =  []

    day0 = random.randint(0, end-250*11)
    day_data0 = tq3.iloc[day0]
    stvalue0 = day_data0['Adj Close']
    
    day10 = day0 + 250*10 #10 years after.
    day_data10 = tq3.iloc[day10]
    stvalue10 = day_data10['Adj Close']
    #print('\n',day0,stvalue0,day10,stvalue10)
    
    res = (stvalue10 - stvalue0)/stvalue0
    Results.append(res)
    
    # Buy, once a year!
    for year in range(1, 10):
        dd = random.randint(-125,125)
        day = day0 + year*250 + dd
           
        day_data = tq3.iloc[day]
        stvalue = day_data['Adj Close']
        res = (stvalue10 - stvalue)/stvalue0
        #print(day,year,stvalue,res)
        Results.append(res)

    if (t < 1): 
        df = pd.DataFrame(Results)            
    else:
        Re = pd.Series(Results)
        df = pd.concat([df,Re],axis=1)
#print(df)

TQ3_Sum = []
TQ3_St = []

for y in range(10)[::-1]:
    sum = np.sum(df.iloc[y])/N
    st = np.std(df.iloc[y])
    TQ3_Sum.append(sum)
    TQ3_St.append(st)

#print(TQ3_Sum)
# QLD ---------------------------------------
qld = pd.read_csv('./data/NASDAQ/QLDs.csv')
qld = qld.set_index('Date')
days = qld.index.tolist()
end = len(days)

for t in range(N):
    Results =  []

    day0 = random.randint(0, end-250*11)
    day_data0 = qld.iloc[day0]
    stvalue0 = day_data0['Adj Close']
    
    day10 = day0 + 250*10 #10 years after.
    day_data10 = qld.iloc[day10]
    stvalue10 = day_data10['Adj Close']
    #print('\n',day0,stvalue0,day10,stvalue10)
    
    res = (stvalue10 - stvalue0)/stvalue0
    Results.append(res)
    
    # Buy, once a year!
    for year in range(1, 10):
        dd = random.randint(-125,125)
        day = day0 + year*250 + dd
           
        day_data = qld.iloc[day]
        stvalue = day_data['Adj Close']
        res = (stvalue10 - stvalue)/stvalue0
        #print(day,year,stvalue,res)
        Results.append(res)

    if (t < 1): 
        df = pd.DataFrame(Results)            
    else:
        Re = pd.Series(Results)
        df = pd.concat([df,Re],axis=1)
#print(df)

QLD_Sum = []
QLD_St = []

for y in range(10)[::-1]:
    sum = np.sum(df.iloc[y])/N
    st = np.std(df.iloc[y])
    QLD_Sum.append(sum)
    QLD_St.append(st)

#print(QLD_Sum)

#----------------------------------
X = np.arange(1,11)

ax.errorbar(X, TQ3_Sum, yerr=TQ3_St, marker = 'o', capthick=1, capsize=10, lw=1, color='b',label ='TQQQ')
ax.errorbar(X, QLD_Sum, yerr=QLD_St, marker = '*', capthick=1, capsize=10, lw=1, color='r',label ='QLD')
ax.legend()

ax.grid(color='b', linestyle=':', linewidth=0.3)

ax.set_xlabel("1992.1.1-2022.5.31")
ax.set_ylabel("Total times.")
fig.suptitle("TQQQ and QLD Simulation. ")
plt.show()
