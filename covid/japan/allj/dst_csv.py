'''
   dst -> csv

2020-06-30 Ichiro Yoshida
'''
import os
import numpy as np
import pandas as pd

json_path = './data/json/'
csv_path = './data/csv/'

files = os.listdir(json_path)
files.sort()
file = files[-1]

df = pd.read_pickle(json_path+file)

print(df.head(50))

dates = df.index.levels[0].tolist()

print(dates)
for date in dates:
   print(date)
   csv = df.loc[(date)]
   file_name = csv_path+date+'.csv'
   print(file_name)
   csv.to_csv(file_name)

