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

data = df['Diff']

desc = data.describe(percentiles=[.1,.9])
mean = desc['mean']
std  = desc['std']

print(mean,std)

plt.hist(data, bins=100, density=True, alpha=0.6, color='b')

Title ="Deviation (%) from MA25 Histgram. Mean={:.2f} Std={:.2f}".format(mean, std)
ax.grid(color='b', linestyle=':', linewidth=0.3)
#ax.set_xlim([-10,10])

ax.set_xlabel("Daily  1974-2018.")
#ax.set_ylabel("Growth Ratio.")
fig.suptitle(Title)
plt.show()
