'''
 Plot deaths/Mil.populations for y axis, and Age65 pop.(%:2018) for x axis

 step3.py

 2020-06-04

'''
import matplotlib.pyplot as plt
import csv
import math

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

for dat in data:
    Country.append(dat[0])
    X.append(float(dat[2]))
    Y.append(float(dat[3]))

plt.title("[Deaths/Mil.Pop. and Incidence of tuberculosis (per 100,000 people) 2018]")
plt.ylabel("Deaths/Mil.Pop.")
plt.xlabel("Incidence of tuberculosis (per 100,000 people) 2018")
plt.yscale('log')
plt.xscale('log')

Jpn = Country.index('Japan')

for n in range(len(Country)):
    if (n == Jpn):
        plt.scatter(X[n],Y[n],s=20,c="red")
        plt.text(X[n], Y[n], 'JAPAN', color='black', fontsize=15)
    else:
        plt.scatter(X[n],Y[n],s=10,c="green")
        plt.text(X[n], Y[n], Country[n], alpha=0.8, color='black', fontsize=8)

plt.ylim(0.1,1000)
plt.xlim(0.1,1000)
plt.grid(which="both")
#plt.show()
plt.savefig('DeMilTBC2018.png')
plt.savefig('DeMilTBC2018.svg')
