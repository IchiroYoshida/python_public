'''
Stock Analysis Daily -> Weekly 
2024-02-19
'''

import talib as ta
from pandas_datareader import data
import pandas as pd

agg_dict = {
    "Open":"first",
    "High":"max",
    "Low":"min",
    "Close":"last",
    "Volume":"sum"
}

df = pd.read_csv('./data/SP500/SPX2023.csv')
df['Date'] = pd.to_datetime(df['Date'])

df_week = df.set_index("Date").resample("W").agg(agg_dict)
print(df_week.head(10))

'''
df = df['2010.01.01':'2023.12.31']
df['RSI14'] = ta.RSI(df['Close'], timeperiod=14)

df0 = df['2010.04.01':'2019.03.31']
day0 = df0.index.tolist()
sample = sorted(random.sample(day0,N))

dfs = df0.loc[sample]
dfsdays = dfs.index.tolist()

for day in dfsdays:
    key = df.index.get_loc(day)
    val0  = df.iloc[key]['Close']
    rsi0  = df.iloc[key]['RSI14']
    val1 = df.iloc[key+period]['Close']
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

ax.set_xlabel("RSI 2010.4.1 - 2019.3.31")
ax.set_ylabel("Growth Ratio.")
fig.suptitle(Title)
plt.show()
'''
