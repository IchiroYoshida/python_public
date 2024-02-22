'''
Stock Analysis RSI(Weekly)
2024-02-20
'''

import matplotlib.pyplot as plt
import talib as ta
from pandas_datareader import data
import pandas as pd
import random

agg_dict = {
    "Open":"first",
    "High":"max",
    "Low":"min",
    "Close":"last",
    "Volume":"sum"   
}

N = 500
period = 1500
RSI=[]
Ratio=[]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df = pd.read_csv('./data/SP500/SPXALL1974.csv')
df['Date'] = pd.to_datetime(df['Date'])

df_week = df.set_index('Date').resample('W').agg(agg_dict)

df_week['RSI14'] = ta.RSI(df_week['Close'], timeperiod=14)

df0 = df_week['1975.01.01':'1989.12.31']
week0 = df0.index.tolist()
sample = sorted(random.sample(week0,N))

dfs = df0.loc[sample]
dfsweeks = dfs.index.tolist()

for week in dfsweeks:
    key = df_week.index.get_loc(week)
    val0  = df_week.iloc[key]['Close']
    rsi0  = df_week.iloc[key]['RSI14']
    val1 = df_week.iloc[key+period]['Close']
    ratio = val1/val0
    
    RSI.append(rsi0)
    Ratio.append(ratio)

df_rsi = pd.DataFrame(RSI, columns=['RSI'])
df_rat = pd.DataFrame(Ratio, columns=['Ratio'])
co = pd.concat([df_rsi, df_rat], axis=1)
corr = co.corr()['RSI']['Ratio']

plt.scatter(RSI,Ratio,c='red')

Title ="RSI and Growth ratio corelation. Corr."+'{:.2f}'.format(corr)+' '+'{}'.format(period)

ax.grid(color='b', linestyle=':', linewidth=0.3)

ax.set_xlabel("RSI 1975.1.1 - 1999.12.31")
ax.set_ylabel("Growth Ratio.")
fig.suptitle(Title)
plt.show()
