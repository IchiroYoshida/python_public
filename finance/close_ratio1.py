'''
Stock Analysis [Close Ratio]
2024-02-22
'''

import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data
import pandas as pd
from scipy import stats

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df = pd.read_csv('./data/SP500/SPXALL1974.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

df_shift = df.shift(1)
df['Close_ratio'] = (df['Close'] - df_shift['Close']) * 100 / df_shift['Close']

data = df['Close_ratio'].dropna()
desc = data.describe()
print(desc)

mean = desc['mean']
std  = desc['std']


'''
#Q-Q plot
stats.probplot(data, dist="norm", plot=plt)
plt.show()

print(stats.kstest(data, 'norm'))
print(stats.shapiro(data))
'''
plt.hist(data, bins=100, density=True, alpha=0.6, color='b')

#Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean, std)

plt.plot(x, p, color='red', linewidth=2)

Title ="Daily Ratio (%) Histgram. Mean={:.2f} Std={:.2f}".format(mean, std)
ax.grid(color='b', linestyle=':', linewidth=0.3)
ax.set_xlabel("Daily Ratio(%) 1974-2023.")
#ax.set_ylabel("Growth Ratio.")
fig.suptitle(Title)
plt.xlim([-5,5])
plt.show()