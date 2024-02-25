'''
Stock Analysis RSI 
2024-02-15
'''

import matplotlib.pyplot as plt
import talib as ta
from pandas_datareader import data
import pandas as pd
import random

N = 1000
period = 7250
#period = 10

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df = pd.read_csv('./data/SP500/SPXALL2023.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

df['MA'] = ta.MA(df['Close'], timeperiod=200)
df['Diff'] = ((df['Close']- df['MA'] )* 100 / df['Close']).dropna()

df0 = df['1985.04.01':'1994.03.31']
day0 = df0.index.tolist()
sample = sorted(random.sample(day0,N))

dfs = df0.loc[sample].dropna()
dfsdays = dfs.index.tolist()

Dev = []
Ratio = []

for day in dfsdays:
    key = df.index.get_loc(day)
    Dev.append(df.iloc[key]['Diff'])
    Ratio.append(df.iloc[key+period]['Close']/df.iloc[key]['Close'])

dev = pd.Series(Dev)
rat = pd.Series(Ratio)

res = dev.corr(rat)

plt.scatter(Dev, Ratio, color='red')

Title ="Deviation from MA200 (%) and Growth ratio corelation. Corr."+'{:.2f}'.format(res)+' '+'{}'.format(period)

ax.grid(color='b', linestyle=':', linewidth=0.3)

ax.set_xlabel("Deviation from MA200 Daily 1985.4.1 - 1994.3.31")
ax.set_ylabel("Growth Ratio.")
fig.suptitle(Title)
plt.show()