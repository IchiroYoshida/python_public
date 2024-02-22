'''
Stock Analysis RSI Hist-Binds 
2024-02-22
'''

import numpy as np
import matplotlib.pyplot as plt
import talib as ta
from pandas_datareader import data
import pandas as pd
from scipy.stats import norm
from scipy.stats import kstest
from scipy import stats

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df = pd.read_csv('./data/SP500/SPXALL1974.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

df['RSI14'] = ta.RSI(df['Close'], timeperiod=14)

data = df['RSI14'].dropna()
desc = data.describe()
print(desc)

#Q-Q plot
stats.probplot(data, dist="norm", plot=plt)
plt.show()

print(kstest(data, 'norm'))

'''
result = stats.shapiro(data)
print(result)

result2 = stats.ks_1samp(data, stats.norm.cdf)
print(result2)

desc = data.describe()
mean = desc['mean']
std  = desc['std']


result1 = stats.shapiro(data)
print(result1)
result2 = stats.ks_1samp(data, stats.norm.cdf)
print(result2)


plt.hist(data, bins=10, density=True, alpha=0.6, color='b')

#Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)

plt.plot(x, p, color='red', linewidth=2)

Title ="RSI Histgram. Mean={:.2f} Std={:.2f}".format(mean, std)
ax.grid(color='b', linestyle=':', linewidth=0.3)
ax.set_xlabel("Daily RSI  1974-2023.")
#ax.set_ylabel("Growth Ratio.")
fig.suptitle(Title)
plt.show()
'''
