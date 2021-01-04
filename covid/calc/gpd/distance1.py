'''
Distance from Wuhan and each countries.

20200-06-27 Ichiro Yoshida
'''
import os
import numpy as np
import pandas as pd
from vincenty import vincenty
import matplotlib.pyplot as plt
import continent as co

continent_colors = {
'Europe':'blueviolet',
'North America':'deepskyblue',
'South America':'royalblue',
'Asia':'springgreen',
'Australia/Oceania':'gold',
'Africa':'chocolate'}

Wuhan_city =(30.593,114.3053)

countries_coordinates = './countries_codes_and_coordinates.csv'
wm_path = '../pom2/data/wmp/'
iso3_csv = '../pom2/data/code/country_iso3.csv'

iso3 = pd.read_csv(iso3_csv)

cc = pd.read_csv(countries_coordinates, header=1, usecols=['Country','Alpha-3 code',
    'Latitude (average)','Longitude (average)'])
cc0 = cc.drop_duplicates()

subset = cc0[['Latitude (average)','Longitude (average)']]
positions = [tuple(x) for x in subset.values]

dd =[]
for position in positions:
    dist = vincenty(Wuhan_city, position)
    dd.append(dist)

Dist = np.array(dd)
cc0['Distance']=Dist

new_cc0 = cc0[['Alpha-3 code','Distance']]

new_cc = new_cc0.rename(columns={'Alpha-3 code':'iso3'})

#---- World meters data ----
files = os.listdir(wm_path)
files.sort()
file = files[-1]

wm = pd.read_pickle(wm_path+file)
wm_iso3 = pd.merge(wm, iso3, left_on = 'Country',
        right_on = 'worldmeters country name').drop(columns='worldmeters country name')

wm_iso3_0 = wm_iso3[['Country','Deaths/1M pop','iso3']]
wm_iso3_subset = wm_iso3_0.drop_duplicates()
wm_cc0 = pd.merge(wm_iso3_subset, new_cc, on = 'iso3')
wm_cc = wm_cc0.drop_duplicates()

Countries = wm_cc['Country']
countries = Countries.values.tolist()

DeathMil = wm_cc['Deaths/1M pop']
demil = DeathMil.values.tolist()
Distances = wm_cc['Distance']
distances = Distances.values.tolist()

for idx in range(len(countries)):
    country = countries[idx]
    cont = co.continents[country][0]
    co_col = continent_colors[cont]

    x = distances[idx]
    s = demil[idx]

    if(s):
        y = float(s)
        if (country == 'Japan'):
            plt.scatter(x, y, color='red', s=50, zorder=2)
            plt.text(x,y,country,fontsize=20, weight="bold",zorder=2)
        else:
            plt.scatter(x, y, color=co_col, s=20, zorder=1)
            plt.text(x, y, country, fontsize=10, zorder=1)

title = '2020 COVID-19 pandemic'
plt.xlabel('Distance from Wuhan (Km)')
plt.ylabel('Deaths/1M pop')
plt.yscale('log')
plt.xlim(0,20000)
plt.ylim(0.1,2000)
plt.grid(which='both', zorder=0)
plt.show()
plt.close()
