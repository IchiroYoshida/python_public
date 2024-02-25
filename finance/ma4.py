'''
Stock Analysis MA (Moving Average) 
2024-02-25
'''

import matplotlib.pyplot as plt
import talib as ta
from pandas_datareader import data
import pandas as pd
import random
import numpy as np
from scipy import stats

N = 100
period = 7250

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df = pd.read_csv('./data/SP500/SPXALL2023.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

df['MA'] = ta.MA(df['Close'], timeperiod=200)
df['Diff'] = ((df['Close']- df['MA'] )* 100 / df['Close']).dropna()

#------1
df1 = df['1985.04.01':'1994.03.31']
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

dev = pd.Series(Dev1)
rat = pd.Series(Ratio1)
cor = dev.corr(rat)

plt.scatter(Dev1, Ratio1, color='blue')
#------------------1
#---2
df2 = df['1985.04.01':'1994.03.31']
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

dev = pd.Series(Dev2)
rat = pd.Series(Ratio2)
cor = dev.corr(rat)

plt.scatter(Dev2, Ratio2, color='red')
#------------------1

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

Title ="Deviation from MA200 (%) and Growth ratio corelation. Corr."+'{:.2f}'.format(cor)+' '+'{}'.format(period)

ax.grid(color='b', linestyle=':', linewidth=0.3)

ax.set_xlabel("Deviation from MA200 Daily 1985.4.1 - 1994.3.31")
ax.set_ylabel("Growth Ratio.")
fig.suptitle(Title)
plt.show()