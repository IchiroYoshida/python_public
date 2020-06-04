'''
 Plot deaths/Mil.populations for y axis, and TBC pop.(2018) for x axis

 plotcont.py

 2020-06-04

'''
import matplotlib.pyplot as plt
import csv
import math
import continent as co

continent_colors = {
'Europe':'blueviolet',
'North America':'deepskyblue',
'South America':'royalblue',
'Asia':'springgreen',
'Australia/Oceania':'gold',
'Africa':'chocolate'}

file = './DeMilTBC2018.csv'

data = []

with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

del data[:1]

Country = []
Code = []
X = []
Y = []
Continent_col = []

for dat in data:
    xx = float(dat[2])
    yy = float(dat[3])
    if (xx>0):
        try:
            continent = co.continents[dat[0]][0]
            co_col = continent_colors[continent]
            Continent_col.append(co_col)
            Country.append(dat[0])
            X.append(xx)
            Y.append(yy)
        except KeyError:
            continue

plt.title("[Deaths/Mil.Pop. and Incidence of tuberculosis (per 100,000 people) 2018]")
plt.ylabel("Deaths/Mil.Pop.")
plt.xlabel("Incidence of tuberculosis (per 100,000 people) 2018")
plt.yscale('log')
plt.xscale('log')

Jpn = Country.index('Japan')

for n in range(len(Country)):
    if (n == Jpn):
        plt.scatter(X[n],Y[n],s=50,c="red")
        plt.text(X[n], Y[n], 'JAPAN', color='black', fontsize=15,weight='bold')
    else:
        plt.scatter(X[n],Y[n],s=20,c=Continent_col[n])
        plt.text(X[n], Y[n], Country[n], alpha=1.0, color='black', fontsize=10)

plt.ylim(0.1,1000)
plt.xlim(0.1,1000)
plt.grid(which="both")
plt.show()
#plt.savefig('DeMilTBC2018.png')
#plt.savefig('DeMilTBC2018.svg')

