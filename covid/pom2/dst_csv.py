'''
  dst -> csv 

2020-06-23 Ichiro Yoshida
'''
import os
import numpy as np
import pandas as pd

dst_path = './data/dst/'
csv_path = './data/csv2/'

files = os.listdir(dst_path)
files.sort()
file = files[-1]

df = pd.read_pickle(dst_path+file)
df= pd.read_pickle(dst_path+'20210418_202221.zip')

countries = df.index.levels[0].tolist()

for country in countries:
    csv = df.loc[(country)]
    file_name = csv_path+country+'.csv'
    print(file_name)
    csv.to_csv(file_name)
