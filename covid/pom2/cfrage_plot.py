'''
CFR(Cases fatality rate) and Aged >65 years.

2020-06-18 Ichiro Yoshida
'''
import os
import matplotlib.pyplot as plt
import pandas as pd
import continent as co

CSV = './data/code/AGE65.csv'
YR ='2018'

ISO3 = './data/code/country_iso3.csv'

age0 = pd.read_csv(CSV, header=2, usecols=['Country Code',YR])
age = age0.dropna()

iso3_org = pd.read_csv(ISO3,header=1, names=['Country','wm Country','iso3'])
iso3 = iso3_org[['wm Country','iso3']]

age_iso3 =iso3.merge(age, left_on ='iso3', right_on = 'Country Code').drop(columns='Country Code')

continent_colors = {
'Europe':'blueviolet',
'North America':'deepskyblue',
'South America':'royalblue',
'Asia':'springgreen',
'Australia/Oceania':'gold',
'Africa':'chocolate'}

pic_path = './data/dst/'

files = os.listdir(pic_path)
files.sort()

file = files[-1]

df = pd.read_pickle(pic_path+file)

countries = df.index.levels[0].tolist()

csvRow = []
for country in countries:
    data = df.loc[(country)]
    cfr0 = data['CFR'] * 100.
    cfr = cfr0.values.tolist()
    cfrate = cfr[-1]
    csvRow.append([country, cfrate])

csv0 = pd.DataFrame(csvRow, columns=['Country','CFR'])
csv = csv0.dropna()

age_data0 = age_iso3[YR]
age_data = age_data0.values.tolist()

mer = age_iso3.merge(csv, left_on='wm Country', right_on='Country')

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

date ='2020/07/05'

title = 'COVID-19 pandemic '+date+'(UTC)'
plt.title(title)
plt.xlabel('Age >65 %')
plt.ylabel('Case Fatality Rate(CFR) %')
plt.xlim(0,30)
plt.ylim(0,20)
plt.grid(which='both',zorder=0)
plt.show()
plt.close()

