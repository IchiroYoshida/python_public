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
cc0 = cc.drop_duplicates()

subset = cc0[['Latitude (average)','Longitude (average)']]
positions = [tuple(x) for x in subset.values]

dd =[]
for position in positions:
    dist = vincenty(Wuhan_city, position)
    dd.append(dist)
    print(dist,position)

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

print(wm_iso3_subset.head(5))
print(new_cc.head(5))

wm_cc0 = pd.merge(wm_iso3_subset, new_cc, on = 'iso3')
wm_cc = wm_cc0.drop_duplicates()

print(wm_cc.head())

