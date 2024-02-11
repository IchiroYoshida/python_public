'''
Simulate Leverage ETF(QLD, TQQQ) from NDX data 
2022-06-05

IT Bubble corruption
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Cash  = 100

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

tq3 = pd.read_csv('./data/NASDAQ/TQQQs.csv')
tq3 = tq3.set_index('Date')
tq3 = tq3['2009-07-01':] #Buy at the top!

#print(tq3)
start = tq3.iloc[0]['Adj Close']
Mul = Cash/start

Estate = Mul * tq3['Adj Close']

X=np.arange(len(Estate))

ax.plot(X, Estate,color='g')
ax.set_yscale('log')
plt.grid(which='both')

fig.suptitle("TQQQ Simulation.   2009.7.1 - ")
plt.show()