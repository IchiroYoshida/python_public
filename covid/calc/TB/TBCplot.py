'''
 Plot deaths/Mil.populations for y axis, and TBC pop.(2018) for x axis

 2020-06-28

'''
import os
import matplotlib.pyplot as plt
import pandas as pd
import continent as co

continent_colors = {
'Europe':'blueviolet',
'North America':'deepskyblue',
'South America':'royalblue',
'Asia':'springgreen',
'Australia/Oceania':'gold',
'Africa':'chocolate'}

pic_path = '../pom2/data/wmp/'
CSV = './TBC.csv'
YR = '2018'
ISO3 = '../pom2/data/code/country_iso3.csv'

files = os.listdir(pic_path)
files.sort()
file=files[-1]

wm0 = pd.read_pickle(pic_path+file)
wm = wm0[['Country','Deaths/1M pop']]

tbc0 = pd.read_csv(CSV, header=2, usecols=['Country Code',YR])
tbc = tbc0.dropna()

iso3_org = pd.read_csv(ISO3, header=1, names=['Country','wm Country','iso3'])
iso3 = iso3_org[['wm Country','iso3']]

tbc_iso3 = iso3.merge(tbc, left_on = 'iso3', right_on = 'Country Code').drop(columns=['iso3','Country Code'])

total0 = tbc_iso3.merge(wm, left_on='wm Country', right_on='Country').drop(columns='wm Country')
total = total0.dropna()

countries0 = total['Country']
countries = countries0.values.tolist()

dat_tbc0 = total['2018']
dat_tbc = dat_tbc0.values.tolist()

demil0 = total['Deaths/1M pop']
demil = demil0.values.tolist()

for idx in range(len(countries)):
    country = countries[idx]
    cont = co.continents[country][0]
    co_col = continent_colors[cont]

    x = float(dat_tbc[idx])
    s = demil[idx]

    if(s):
        y = float(s)
        print(country,x,y)

        if (country == 'Japan'):
            plt.scatter(x,y,color='red',s=60, zorder=2)
            plt.text(x,y,country,fontsize=20, weight="bold",zorder=2)
        else:
            plt.scatter(x,y,color=co_col,s=30, zorder=1)
            plt.text(x,y,country,fontsize=10, zorder=1)

plt.title("[Deaths/Mil.Pop. and Incidence of tuberculosis (per 100,000 people) 2018]")
plt.ylabel("Deaths/Mil.Pop.")
plt.xlabel("Incidence of tuberculosis (per 100,000 people) 2018")
plt.yscale('log')
plt.xscale('log')
plt.xlim(0.1,1000)
plt.ylim(0.1,1000)
plt.grid(which='both',zorder=0)
plt.show()
plt.close()
