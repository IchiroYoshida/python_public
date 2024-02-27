'''
Stock Analysis MA (Moving Average) 
2024-02-27
'''

import matplotlib.pyplot as plt
import talib as ta
from pandas_datareader import data
import pandas as pd
import random
import numpy as np
from scipy import stats

N = 500
period = 250*5 #5Years

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df = pd.read_csv('./data/SP500/SPXALL1974.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

df['MA'] = ta.MA(df['Close'], timeperiod=200)
df['Diff'] = ((df['Close']- df['MA'] )* 100 / df['Close']).dropna()

#------ 1 random
df1 = df['1974.04.01':'2018.03.31']
day1 = df1.index.tolist()
sample1 = sorted(random.sample(day1,N))

dfs = df1.loc[sample1].dropna()
dfsdays = dfs.index.tolist()

Dev1 = []
Ratio1 = []

for day in dfsdays:
    key = df.index.get_loc(day)
    Dev1.append(df.iloc[key]['Diff'])
    Ratio1.append(df.iloc[key+period]['Close']/df.iloc[key]['Close'])

plt.scatter(Dev1, Ratio1, c='C7', alpha= 0.8)
#------------------1
#---2
df2 = df['1974.04.01':'2018.03.31']
df2 = df2[df2['Diff'] > 10.0]
day2 = df2.index.tolist()
sample2 = sorted(random.sample(day2,N))

dfs = df2.loc[sample2].dropna()
dfsdays = dfs.index.tolist()

Dev2 = []
Ratio2 = []

for day in dfsdays:
    key = df.index.get_loc(day)
    Dev2.append(df.iloc[key]['Diff'])
    Ratio2.append(df.iloc[key+period]['Close']/df.iloc[key]['Close'])

plt.scatter(Dev2, Ratio2, c='C9', alpha= 0.3)
#------------------2

#---3
df3 = df['1974.04.01':'2018.03.31']
df3 = df3[df3['Diff'] < -10.0]
day3 = df3.index.tolist()
sample3 = sorted(random.sample(day3,N))

dfs = df3.loc[sample3].dropna()
dfsdays = dfs.index.tolist()

Dev3 = []
Ratio3 = []

for day in dfsdays:
    key = df.index.get_loc(day)
    Dev3.append(df.iloc[key]['Diff'])
    Ratio3.append(df.iloc[key+period]['Close']/df.iloc[key]['Close'])

plt.scatter(Dev3, Ratio3, c='C3', alpha= 0.3)
#------------------2


#------F
Ver1 = np.var(Ratio1, ddof=1)
Ver2 = np.var(Ratio2, ddof=1)
Mean1 = np.mean(Ratio1)
Mean2 = np.mean(Ratio2)

L1 = len(Ratio1)
L2 = len(Ratio2)
f = Ver1/Ver2
oneside_pval1 = stats.f.cdf(f, L1, L2) 
oneside_pval2 = stats.f.sf(f, L1, L2)
twoside_pval = min(oneside_pval1, oneside_pval2) *2
print('Mean1',Mean1)
print('Mean2',Mean2)
print('F:    ', round(f, 3))
print('p-value: ', round(twoside_pval, 4))
res=stats.ttest_ind(Ratio1, Ratio2, equal_var=False)
print(res)

Title ="Deviation from MA200 (%) and Growth ratio."

ax.grid(color='b', linestyle=':', linewidth=0.3)

ax.set_xlabel("Deviation from MA200 Daily 1985.4.1 - 1994.3.31")
ax.set_ylabel("Growth Ratio.")
fig.suptitle(Title)
plt.show()