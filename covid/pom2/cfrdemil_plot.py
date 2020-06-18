'''
Pickle Data -> countries.csv (Pandas)

2020-06-16 Ichiro Yoshida
'''
import datetime
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

    demil0 = csv['Deaths /1M pop (Ave7)']
    cfr0   = csv['CFR'] *100.
    demil = demil0.values
    cfr  = cfr0.values
    csvRow.append([country,demil[-1],cfr[-1]])

date0 = csv['date']
date1 = date0.values
date = date1[-1]

csv2 = pd.DataFrame(csvRow,columns=['Country','Deaths/1M pop','CFR'])
csv3 = csv2.dropna()

x = csv3['CFR']
y = csv3['Deaths/1M pop']
country0 = csv3['Country']

X = x.values.tolist()
Y = y.values.tolist()
countries = country0.values.tolist()

for count in range(len(countries)):
    country = countries[count]
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
plt.xlabel('Case Fatality Rate(CFR) %')
plt.ylabel('Deaths/1M pop.')
plt.yscale('log')
plt.xlim(0,25)
plt.ylim(0.1,2000)
plt.grid(which='both',zorder=0)
plt.show()
plt.close()
