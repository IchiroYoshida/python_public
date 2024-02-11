'''
Yahoo Stock data -> .csv
'''
from pandas_datareader import data
import pandas as pd

df = data.DataReader("^DJI","yahoo",'2017-01-01','2022-05-01')
df.sort_index(inplace=True)

df.to_csv('data/DOW/DJI2017.csv', index=True)
