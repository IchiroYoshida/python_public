'''
   plot World countries of K val

   2020-06-14

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

path ='./data/csv0/'
files = os.listdir(path)
files.sort()

for file in files:
    country = file.split('.csv')[0]
    continent = co.continents[country][0]
    co_col = continent_colors[continent]

    read_csv = path+file
    csv = pd.read_csv(read_csv)

    demil = csv[csv['Deaths /1M pop (Ave7)'] > .1]

    y = demil['K']
    x = len(y)

    X = np.arange(x)
    Y = y.values.tolist()

    plt.plot(X,Y,color=co_col)
    xx = X[-1]
    yy = Y[-1]
    plt.text(xx,yy,country)

#plt.xscale('log')
#plt.yscale('log')
plt.grid(which='both')
plt.show()

