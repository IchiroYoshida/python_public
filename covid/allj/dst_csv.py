'''
   dst -> csv

2020-06-30 Ichiro Yoshida
'''
import os
import numpy as np
import pandas as pd

dst_path = './data/dst/'
csv_path = './data/csv/'

files = os.listdir(dst_path)
files.sort()
file = files[-1]

df = pd.read_pickle(dst_path+file)

print(df.tail())
'''
dates = df.index.levels[0].tolist()

print(dates)
for date in dates:
   csv = df.loc[(date)]
   file_name = csv_path+date+'.csv'
   print(file_name)
   csv.to_csv(file_name)
'''
