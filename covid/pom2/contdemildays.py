'''
   plot World countries of Deaths/Mil. pop and Deaths Week/Mil.pop
   Days after Deaths/Mil. pop > .1

   2020-07-09

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

for continent in continents:
    print(continent)

    for file in files:
        country = file.split('.csv')[0]
        cont = co.continents[country][0]
        co_col = continent_colors[cont]

        if (continent == cont):
            read_csv = path+file
            csv = pd.read_csv(read_csv)

            demil0 = csv[csv['Deaths /1M pop (Ave7)'] > .1]
            demil = demil0.dropna()

            if (len(demil)>30):
                x = len(demil)
                y = demil['Deaths /1M pop (Ave7)'] 

                X = np.arange(x)
                Y = y.values.tolist()

                if (country == 'Japan'):
                    plt.plot(X, Y, color='red', linewidth='3',zorder=1)
                else:
                    plt.plot(X,Y,color=co_col,zorder=0)

            try:
                xx = X[-1]
                yy = Y[-1]
            except IndexError:
                print(xx,yy,country)

            if(country == 'Japan'):
                plt.text(xx, yy, country, fontsize=20)
            else:
                plt.text(xx, yy, country, fontsize=10)
    
    con=continent.replace('/','_')
    save_name = './data/con/'+con+'.png'
    title = 'COVID-19  '+continent

    plt.title(title)
    plt.xlabel('Days')
    plt.xlim(0,120)
    plt.ylim(0.1,1500)
    plt.ylabel('Deaths/1M pop.')
    #plt.xscale('log')
    plt.yscale('log')
    plt.grid(which='both')
    #plt.show()
    print(save_name)
    plt.savefig(save_name)
    plt.close()

