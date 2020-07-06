'''
   plot World countries of Deaths/Mil. pop and Deaths Week/Mil.pop
   Days after Deaths/Mil. pop > .1

   2020-05-23

'''
import os
import math
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

import numpy as np
import pandas as pd
import continent as co

continent_colors = {
'Europe':'blueviolet',
'North America':'deepskyblue',
'South America':'royalblue',
'Asia':'springgreen',
'Australia/Oceania':'gold',
'Africa':'chocolate'}

path ='./data/csv2/'
files = os.listdir(path)
files.sort()

for file in files:
    country = file.split('.csv')[0]
    continent = co.continents[country][0]
    co_col = continent_colors[continent]

    if(continent == "Africa"):
        read_csv = path+file
        csv = pd.read_csv(read_csv)

        demil = csv[csv['Deaths /1M pop (Ave7)'] > .1]

        x = demil['Deaths /1M pop (Ave7)'] 
        y = demil['Deaths Weekly(Ave7)/1M pop']

        X = x.values.tolist()
        Y = y.values.tolist()

        plt.plot(X,Y,color=co_col)

        #xx = X[-1]
        #yy = Y[-1]

        #plt.text(xx,yy,country)

plt.xscale('log')
plt.yscale('log')
plt.grid(which='both')
plt.show()
