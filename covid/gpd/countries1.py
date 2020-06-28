'''
Distance from Wuhan and each countries.

20200-06-27 Ichiro Yoshida
'''
import os
import numpy as np
import pandas as pd
from vincenty import vincenty

Wuhan_city =(30.593,114.3053)

countries_coordinates = './countries_codes_and_coordinates.csv'
wm_path = '../pom2/data/wmp/'
iso3_csv = '../pom2/data/code/country_iso3.csv'

iso3 = pd.read_csv(iso3_csv)

cc = pd.read_csv(countries_coordinates, header=1, usecols=['Country','Alpha-3 code',
    'Latitude (average)','Longitude (average)'])

subset = cc[['Latitude (average)','Longitude (average)']]
positions = [tuple(x) for x in subset.values]

dd =[]
for position in positions:
    dist = vincenty(Wuhan_city, position)
    dd.append(dist)

Dist = np.array(dd)

cc['Distance']=Dist

new_cc = cc[['Alpha-3 code','Distance']]

#---- World meters data ----
files = os.listdir(wm_path)
files.sort()
file = files[-1]

wm = pd.read_pickle(wm_path+file)
wm_iso3 = pd.merge(wm, iso3, left_on = 'Country',
        right_on = 'worldmeters country name').drop(columns='worldmeters country name')

wm_iso3_subset = wm_iso3[['Country','Deaths/1M pop','iso3']]
wm_iso3_sort = wm_iso3_subset.sort_values('iso3')

new_cc_sort = new_cc.sort_values('Alpha-3 code')

print(wm_iso3_sort.columns)
print(new_cc_sort.columns)

print(wm_iso3_sort.head(10))
print(new_cc_sort.head(10))

wm_cc = pd.merge(wm_iso3_sort, new_cc, left_on = 'iso3',
        right_on = 'Alpha-3 code').drop(columns='Alpha-3 code')

print(wm_cc.head())
