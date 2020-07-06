'''
    plot World countries (csv2 -> Pandas -> plot)
    
    2020-06-25
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

csv_path = './data/csv2/'
plot_path = './data/plot/'

files = os.listdir(csv_path)
files.sort()

for file in files:
    country = file.split('.csv')[0]
    cont = co.continents[country][0]
    co_col = continent_colors[cont]

    read_csv = csv_path+file
    csv = pd.read_csv(read_csv)

    demil = csv[csv['Deaths /1M pop (Ave7)'] > .1]
    
    deaths = demil['Deaths /1M pop (Ave7)']
    r0     = demil['R0']


    D = deaths.values.tolist()
    R0 = r0.values.tolist()

    if (len(D) > 10):
        y = D[-1]
        x = R0[0]
        print(country,x,y)

        if(country == 'Japan'):
            plt.scatter(x,y, s=70,color='red',zorder=1)
        else:
            plt.scatter(x,y, s=30,color=co_col,zorder=0)

        if (country == 'Japan'):
            plt.text(x,y,country,fontsize=20)
        else:
            plt.text(x,y,country,fontsize=10)

plt.title('COVID-19 2020 Pandemic Deaths/1M pop. and initial R0')
plt.xlabel('R0')
plt.ylabel('Deaths/1M pop.')
plt.xlim(1,10)
plt.ylim(0.1,1000)
plt.yscale('log')
#plt.xscale('log')
plt.grid(which='both')
plt.show()
plt.close()
