'''
    plot World countries (csv2 -> Pandas -> plot)
    
    2020-07-25
'''
import os
import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import matplotlib.dates as mdates
import continent as co

csv_path = './data/csv2/'

continent_colors = {
'Europe':'blueviolet',
'North America':'deepskyblue',
'South America':'royalblue',
'Asia':'springgreen',
'Australia/Oceania':'gold',
'Africa':'chocolate'}

#fig, ax = plt.subplots(constrained_layout=True, figsize=(10, 7))
fig, ax = plt.subplots(figsize=(10, 7))
base = datetime.datetime(2020,1,22)

countries = []
with open('country.txt') as f:
    reader = csv.reader(f)
    for row in reader:
        countries.append(row)

for country0 in countries:
    country = country0[0]
    read_csv = csv_path+country+'.csv'
    csv = pd.read_csv(read_csv)
    cont = co.continents[country][0]
    co_col = continent_colors[cont]

    drate0 = csv['Death rate 2Weeks']   #.dropna()
    drate = drate0.values.tolist()
    Days = len(drate)

    dates = np.array([base + datetime.timedelta(days=i) for i in range(Days)])
    locator = mdates.AutoDateLocator(maxticks=30)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    if (country == 'Japan'):
        ax.plot(dates,drate,color='red',linewidth='3',zorder=1)
    else:
        ax.plot(dates,drate,color=co_col,zorder=0)

    try:
        xx = dates[-1]
        yy = drate[-1]
    except IndexError:
        print(xx,yy,country)

    if (country == 'Japan'):
        ax.text(xx, yy, country, fontsize=20)
    else:
        ax.text(xx, yy, country, fontsize=10)

plt.title('2020 COVID-19 Pandemic death rate ',fontsize=30)
plt.ylabel('Death rate')

plt.xlim(datetime.datetime(2020,6,1),)
#plt.xlim(20,200)
#plt.ylim(0.001,1.)
plt.ylim(0,0.25)
#plt.yscale('log')
plt.grid(which="both")
plt.show()
plt.close()

