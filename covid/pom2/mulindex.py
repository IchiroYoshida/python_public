'''
  MultiIndex (Pandas)

2020-06-23 Ichiro Yoshida
'''
import os
import numpy as np
import pandas as pd

pic_path = './data/pomber/'

files = os.listdir(pic_path)
files.sort()
file = files[-1]

df = pd.read_pickle(pic_path+file)

countries = df.index.levels[0].tolist()
dates = df.index.levels[1].tolist()

country = countries[20]
date = dates[22]

c1 =df.loc[(country)]
print(country,c1)

