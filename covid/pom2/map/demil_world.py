'''
   World coropleth graph of Deaths /1M pop

   2020-07-05 Ichiro Yoshida
'''
import os
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

wm_path = '../data/wmp/'

iso3 = pd.read_csv('../data/code/country_iso3.csv')

files = os.listdir(wm_path)
files.sort()
file = files[-1]

date_str=file.split('_')[1]
year =date_str[:4]
month = date_str[4:6]
day = date_str[6:8]
date = year+'/'+month+'/'+day
#print(date)

wm = pd.read_pickle(wm_path+file)
wm['Deaths/1M pop'] = pd.to_numeric(wm['Deaths/1M pop'], errors='coerce')

wm_iso3 = pd.merge(wm, iso3, left_on = 'Country',
        right_on ='worldmeters country name') .drop(columns='worldmeters country name')

df = wm_iso3[['Deaths/1M pop','iso3']]

world  = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#world = world[(world.pop_est>0) & (world.continent == "Africa")]

world.loc[world['name'] == 'France','iso_a3'] = 'FRA'
world.loc[world['name'] == 'Norway','iso_a3'] = 'NOR'
world.loc[world['name'] == 'Somaliland','iso_a3'] = 'SOM'
world.loc[world['name'] == 'Kosovo','iso_a3'] = 'RKS'

for_plotting = world.merge(df, left_on = 'iso_a3', right_on = 'iso3')

dt = for_plotting[['name','Deaths/1M pop']]

list = dt.values.tolist()

for li in list:
    print(li)

'''
list = for_plotting.value.tolist()

for li in list:
    print(li)

ax = for_plotting.dropna().plot(column='Deaths/1M pop',
        cmap = 'YlGnBu', figsize=(15,9),
        scheme='quantiles', k=3,
        legend = False,
        edgecolor = 'blue' );

fig = ax.get_figure()
cbax = fig.add_axes([0.95, 0.3, 0.03, 0.39])

demil = for_plotting['Deaths/1M pop']   #.dropna()
Max = demil.max()

sm = plt.cm.ScalarMappable(cmap = 'YlGnBu', \
     norm = plt.Normalize(vmin=0.0,
     vmax=Max))

fig.colorbar(sm, cax=cbax, format="%d")

title = '2020 COVID-19 Pandemic '+date+' Deaths/1M pop'
ax.set_title(title, fontdict={'fontsize':25})
ax.set_axis_off()
plt.show()
'''

