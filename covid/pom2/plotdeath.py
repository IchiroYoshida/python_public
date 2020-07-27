'''
    plot World countries (csv2 -> Pandas -> plot)
    
    2020-06-24
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

csv_path = './data/csv0/'
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

    D = deaths.values.tolist()
    x = len(D)

    if(x):
        X  = np.arange(x)
       
        if(country == 'Japan'):
            plt.plot(X,D,color='red',linewidth='3',zorder=1)
        else:
            plt.plot(X,D,color=co_col,zorder=0)

        try:
            xx = X[-1]
            yy = D[-1]
        except IndexError:
            print(xx,yy, country)

        if (country == 'Japan'):
            plt.text(xx,yy,country,fontsize=20)
        else:
            plt.text(xx,yy,country,fontsize=10)

plt.title('COVID-19 2020 Pandemic Deaths/1M pop.')
plt.xlabel('Days since Deaths 1.0> 10M pop.')
plt.ylabel('Deaths/1M pop.')
plt.xlim(0,120)
plt.ylim(0.1,1000)
plt.yscale('log')
plt.grid(which='both')
plt.show()
plt.close()
