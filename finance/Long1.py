'''
Analyze Leverage ETF(QLD and TQQQ) 
2022-06-12
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

Cash = 100
Total = 0

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# TQQQ ---------------------------------------
tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
days = tq3.index.tolist()
end = len(days)

for t in range(250):
    Now = []
    Org = []
    Buy =  []

    # Buy, once a year!
    for year in range(0, end-250, 250):
        dd = random.randint(0,250)
    
        day = year + dd
        day_data = tq3.iloc[day]
        stvalue = day_data['Adj Close']
        Total += Cash
        
        Buy.append([day,stvalue,Total])

    Col = []
    
    for day in range(0, end, 250):
        day_data = tq3.iloc[day]
        val = day_data['Adj Close']
    
        total_now = 0
        #total_all = 0
    
        for buy in Buy:
            buy_day = buy[0]
            buy_val = buy[1]
            buy_total = buy[2]
        
            if (day > buy_day):
                total_now += val/buy_val * Cash
                #total_all += Cash
        
        Now.append(total_now)
    
    if (t < 1): 
        df = pd.DataFrame(Now,columns=[t])            
    else:
        df[t] = Now
        
years = len(df)

TQ3_Mean = []
TQ3_St = []

for y in range(years):
    mean = np.mean(df.iloc[y])
    st = np.std(df.iloc[y])
    TQ3_Mean.append(mean)
    TQ3_St.append(st)

# QLD ---------------------------------------
qld = pd.read_csv('./data/NASDAQ/QLDs.csv')
qld = qld.set_index('Date')
days = qld.index.tolist()
end = len(days)

for t in range(250):
    Now = []
    Org = []
    Buy =  []

    # Buy, once a year!
    for year in range(0, end-250, 250):
        dd = random.randint(0,250)
    
        day = year + dd
        day_data = qld.iloc[day]
        stvalue = day_data['Adj Close']
        Total += Cash
        
        Buy.append([day,stvalue,Total])

    Col = []
    
    for day in range(0, end, 250):
        day_data = qld.iloc[day]
        val = day_data['Adj Close']
    
        total_now = 0
        #total_all = 0
    
        for buy in Buy:
            buy_day = buy[0]
            buy_val = buy[1]
            buy_total = buy[2]
        
            if (day > buy_day):
                total_now += val/buy_val * Cash
                #total_all += Cash
        
        Now.append(total_now)
    
    if (t < 1): 
        df = pd.DataFrame(Now,columns=[t])            
    else:
        df[t] = Now
        
years = len(df)

QLD_Mean = []
QLD_St = []

for y in range(years):
    mean = np.mean(df.iloc[y])
    st = np.std(df.iloc[y])
    #print(y,mean,st)
    QLD_Mean.append(mean)
    QLD_St.append(st)

X = np.arange(years)

ax.errorbar(X, TQ3_Mean, yerr=TQ3_St, marker = 'o', capthick=1, capsize=10, lw=1, color='b',label ='TQQQ')
ax.errorbar(X, QLD_Mean, yerr=QLD_St, marker = '*', capthick=1, capsize=10, lw=1, color='r',label ='QLD')
ax.legend()

ax.grid(color='b', linestyle=':', linewidth=0.3)

ax.set_xlabel("Buy every years from 1992.1.1-2021.12.31")
ax.set_ylabel("Value")
ax.set_yscale('log')
fig.suptitle("TQQQ and QLD Simulation. ")
plt.show()
