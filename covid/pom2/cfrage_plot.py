'''
CFR(Cases fatality rate) and Aged >65 years.

2020-06-18 Ichiro Yoshida
'''
import datetime
import os
import matplotlib.pyplot as plt
import pandas as pd
import continent as co
import abb3

CSV = './data/code/AGE65.csv'
YR ='2018'

ISO3 = './data/code/country_iso3.csv'

age0 = pd.read_csv(CSV, header=2, usecols=['Country Code',YR])
age = age0.dropna()

iso3 = pd.read_csv(ISO3,header=1, names=['Country','wm Country','iso3'])

age_iso3 =iso3.merge(age, left_on ='iso3', right_on = 'Country Code')

continent_colors = {
'Europe':'blueviolet',
'North America':'deepskyblue',
'South America':'royalblue',
'Asia':'springgreen',
'Australia/Oceania':'gold',
'Africa':'chocolate'}

Index=['date', 'confirmed', 'deaths', 'recovered',
       'Cases Total(Ave7)', 'Cases Day', 'Cases Day(Ave7)',
       'Deaths Total(Ave7)', 'Deaths Day', 'Deaths Day(Ave7)',
       'Deaths Weekly(Ave7)/1M pop', 'Deaths /1M pop (Ave7)',
       'Td7', 'R0','K','CFR']

def str2date(d):
   tmp = datetime.datetime.strptime(d,'%Y-%m-%d')
   return datetime.date(tmp.year, tmp.month, tmp.day)

pic_path = './data/dst/'

files = os.listdir(pic_path)
files.sort()

file = files[-1]

df = pd.read_pickle(pic_path+file)

df1 = df.set_index(["Country"])
df1.sort_index(inplace=True)
countries = list(set(list(df1.index)))
countries.sort()

csvRow = []
for country in countries:
    c = df1.loc[country]
    c2 = c.values
    sort_c2 = sorted(c2, key=lambda x: str2date(str(x[0])))
    csv = pd.DataFrame(sort_c2,columns=Index)

    cfr0   = csv['CFR'] *100.
    cfr  = cfr0.values
    csvRow.append([country,cfr[-1]])

date0 = csv['date']
date1 = date0.values
date = date1[-1]

wm_countries0 = age_iso3['wm Country']
wm_countries = wm_countries0.values.tolist()

age_data0 = age_iso3[YR]
age_data = age_data0.values.tolist()

csv2 = pd.DataFrame(csvRow,columns=['Country','CFR'])
csv3 = csv2.dropna()

mer = age_iso3.merge(csv3, left_on='wm Country', right_on='Country')

countries0 = mer['wm Country']
countries = countries0.values.tolist()

age0 = mer[YR]
age = age0.values.tolist()

cfr0 = mer['CFR']
cfr = cfr0.values.tolist()

COUNTRY =[]
X =[]
Y =[]
for i in range(len(countries)):
    country = countries[i]
    age_data = age[i]
    cfr_data = cfr[i]

    COUNTRY.append(country)
    X.append(age_data)
    Y.append(cfr_data)

for count in range(len(COUNTRY)):
    country = COUNTRY[count]
    cont = co.continents[country][0]
    co_col = continent_colors[cont]

    x1 = X[count]
    y1 = Y[count]

    if(country == 'Japan'):
        plt.scatter(x1,y1,color='red',s=50, zorder=2)
        plt.text(x1,y1,country,fontsize=20, weight="bold",zorder=2)
    else:
        plt.scatter(x1,y1,color=co_col,s=20, zorder=1)
        plt.text(x1,y1,country,fontsize=10, zorder=1)

title = 'COVID-19 pandemic '+date+'(UTC)'
plt.title(title)
plt.xlabel('Age >65 %')
plt.ylabel('Case Fatality Rate(CFR) %')
plt.xlim(0,30)
plt.ylim(0.25)
plt.grid(which='both',zorder=0)
plt.show()
plt.close()

