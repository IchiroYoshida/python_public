'''
    plot World countries (csv2 -> Pandas -> plot)
    
    2020-07-07
'''
import os
import math
import matplotlib.pyplot as plt
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

csv2_path = './data/csv0/'
plot_path = './data/plot/'

files = os.listdir(csv2_path)
files.sort()

for file in files:
    country = file.split('.csv')[0]
    read_csv = csv2_path+file
    csv = pd.read_csv(read_csv)
    cont = co.continents[country][0]
    co_col = continent_colors[cont]

    demil = csv[csv['Deaths /1M pop (Ave7)'] > .1]
    demil0 = demil['Deaths /1M pop (Ave7)']
    d0 = demil['Deaths Total(Ave7)']

    Mpop0 = d0 /demil0
    Mpop1 = Mpop0.values.tolist()

    Mpop = Mpop1[-1:]

    if(Mpop):
        d = demil['Deaths Day(Ave7)'] /Mpop 
        x  = len(d.values.tolist())
        X  = np.arange(x)

        D = d.values.tolist() 

        if (country == 'Japan'):
            plt.plot(X,D,color='red',linewidth='3',zorder=1)
        else:
            plt.plot(X,D,color=co_col,zorder=0)

        try:
            xx = X[-1]
            yy = D[-1]
        except IndexError:
            print(xx,yy,country)

        if (country == 'Japan'):
            plt.text(xx, yy, country, fontsize=20)
        else:
            plt.text(xx, yy, country, fontsize=10)

plt.legend(['Deaths/1M pop in '+country])
plt.xlabel('Days')
plt.ylabel('Number')
plt.xlim(0,120)
plt.ylim(0.01,20)
plt.yscale('log')
plt.grid(which="both")
plt.show()
plt.close()
