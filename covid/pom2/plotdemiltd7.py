'''
   plot World countries of Deaths/Mil. pop and Deaths Week/Mil.pop
   Days after Deaths/Mil. pop > .1

   2020-06-17

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

continents = list(continent_colors.keys())

print(continents)
'''
for file in files:
    country = file.split('.csv')[0]
    continent = co.continents[country][0]
    co_col = continent_colors[continent]

    read_csv = path+file
    csv = pd.read_csv(read_csv)

    demil = csv[csv['Deaths /1M pop (Ave7)'] > .1]

    if (len(demil)>10):
        x = demil['Td7']
        y = demil['Deaths /1M pop (Ave7)'] 

        X = x.values.tolist()
        Y = y.values.tolist()

        plt.plot(X,Y,color=co_col)

        try:
            xx = X[-1]
            yy = Y[-1]
        except IndexError:
            print(xx,yy)

        plt.text(xx,yy,country)


plt.xlabel('Doubling Time(days)')
plt.ylabel('Deaths/1M pop.')
plt.xscale('log')
plt.yscale('log')
plt.grid(which='both')
plt.show()
'''

