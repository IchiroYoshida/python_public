'''
    plot World countries (csv2 -> Pandas -> plot)
    
    2020-07-11
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

#files = ['Japan.csv']

for file in files:
    country = file.split('.csv')[0]
    read_csv = csv2_path+file
    csv = pd.read_csv(read_csv)
    cont = co.continents[country][0]
    co_col = continent_colors[cont]

    demil = csv[csv['Deaths /1M pop (Ave7)'] > .1]
    drate0 = demil['Death rate 2Weeks']
    drate = drate0.values.tolist()

    if(len(drate)>30):
        x  = len(drate)
        X  = np.arange(x)
        Y = drate

        if (country == 'Japan'):
            plt.plot(X,Y,color='red',linewidth='3',zorder=1)
        else:
            plt.plot(X,Y,color=co_col,zorder=0)

        try:
            xx = X[-1]
            yy = Y[-1]
        except IndexError:
            print(xx,yy,country)

        if (country == 'Japan'):
            plt.text(xx, yy, country, fontsize=20)
        else:
            plt.text(xx, yy, country, fontsize=10)

plt.legend(['Deaths rate '])
plt.xlabel('Days')
plt.ylabel('Death rate')
plt.xlim(50,140)
plt.ylim(0.001,1.)
#plt.ylim(0,0.2)
plt.yscale('log')
plt.grid(which="both")
plt.show()
plt.close()

