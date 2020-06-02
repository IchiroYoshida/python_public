'''
   plot World countries (csv2 - plot) 

   Days after Deaths./Mil.pop > 1 

   2020-05-23
'''
import os
import math
import csv
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
plt.style.use('seaborn-colorblind')

import numpy as np
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
    csvRow = []
    read_csv = path+file
    with open(read_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            csvRow.append([row][0])
    del csvRow[:2]

    country = file.split('.csv')[0]
    continent = co.continents[country][0]
    co_col = continent_colors[continent]

    D = [] #Death
    
    for dat in csvRow:
        date = dat[0]
        death = float(dat[11])
        if (death > 1.):
            D.append(float(death))
    if(len(D)):
        if(continent == 'Asia'):
            X = range(len(D))
            plt.plot(X,D,color=co_col)
            xx = len(D)
            yy = D[-1]
            plt.text(xx,yy,country)
plt.ylim(1,200)
plt.xlim(0,90)
plt.yscale('log')
plt.grid(which='both')
plt.show()
plt.close()

