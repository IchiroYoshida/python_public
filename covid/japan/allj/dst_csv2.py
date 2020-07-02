'''
   dst -> csv2

2020-07-02 Ichiro Yoshida
'''
import os
import numpy as np
import pandas as pd

json_path = './data/json/'
csv_path = './data/csv2/'

files = os.listdir(json_path)
files.sort()
file = files[-1]

df = pd.read_pickle(json_path+file)


df2 = df.swaplevel('date','name')
df3 = df2.droplevel('name_jp').sort_index()

areas = df3.index.levels[0].tolist()
for area in areas:
    csv = df3.loc[(area)]
    file_name = csv_path+area+'.csv'
    print(file_name)
    csv.to_csv(file_name)

