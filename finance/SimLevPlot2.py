'''
Simulate Leverage ETF(QLD, TQQQ) from NDX data 
2022-06-04
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Cash  = 100

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')

start = tq3.iloc[0]['Adj Close']
Mul = Cash/start

Estate = Mul * tq3['Adj Close']

X=np.arange(len(Estate))

ax.plot(X, Estate)
ax.set_yscale('log')
plt.grid(which='both')

fig.suptitle("TQQQ Simulation.   1992.1.2 -  ")
plt.show()
