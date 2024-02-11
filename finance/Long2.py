'''
Analyze Leverage ETF(QLD and TQQQ) interest rate / year
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
    Interests =  []

    day0 = random.randint(0, end-250*11)
    day_data0 = tq3.iloc[day0]
    stvalue0 = day_data0['Adj Close']
    
    # Buy, once a year!
    for year in range(1, 11):
        dd = random.randint(-125,125)
        day = day0 + year*250 + dd
        
        day_data = tq3.iloc[day]
        stvalue = day_data['Adj Close']
        interest = (stvalue - stvalue0)/year * 100
        Interests.append(interest)

    if (t < 1): 
        df = pd.DataFrame(Interests,columns=[0])            
    else:
        IN = pd.Series(Interests)
        df = pd.concat([df,IN],axis=1)
#print(df)


TQ3_Mean = []
TQ3_St = []

for y in range(10):
    mean = np.mean(df.iloc[y])
    st = np.std(df.iloc[y])
    TQ3_Mean.append(mean)
    TQ3_St.append(st)
    

# QLD ---------------------------------------
qld = pd.read_csv('./data/NASDAQ/QLDs.csv')
qld = qld.set_index('Date')
days = qld.index.tolist()
end = len(days)

for t in range(N):
    Interests =  []

    day0 = random.randint(0, end-250*11)
    day_data0 = qld.iloc[day0]
    stvalue0 = day_data0['Adj Close']
    
    # Buy, once a year!
    for year in range(1, 11):
        dd = random.randint(-125,125)
        day = day0 + year*250 + dd
        
        day_data = qld.iloc[day]
        stvalue = day_data['Adj Close']
        interest = (stvalue - stvalue0)/year * 100
        Interests.append(interest)

    if (t < 1): 
        df = pd.DataFrame(Interests,columns=[0])            
    else:
        IN = pd.Series(Interests)
        df = pd.concat([df,IN],axis=1)
    
QLD_Mean = []
QLD_St = []

for y in range(10):
    mean = np.mean(df.iloc[y])
    st = np.std(df.iloc[y])
    QLD_Mean.append(mean)
    QLD_St.append(st)

X = np.arange(1,11)

ax.errorbar(X, TQ3_Mean, yerr=TQ3_St, marker = 'o', capthick=1, capsize=10, lw=1, color='b',label ='TQQQ')
ax.errorbar(X, QLD_Mean, yerr=QLD_St, marker = '*', capthick=1, capsize=10, lw=1, color='r',label ='QLD')
ax.legend()

ax.grid(color='b', linestyle=':', linewidth=0.3)

ax.set_xlabel("1992.1.1-2022.5.31")
ax.set_ylabel("Interest / year (%)")
fig.suptitle("TQQQ and QLD Simulation. ")
plt.show()
