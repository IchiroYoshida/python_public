'''
 Plot at the day 1>deaths/Mil.populations of Td7  for x axis, 
     and Deaths/Mil.populations on 2020/05/20 for y axis

 step3.py

 2020-05-19

'''
import matplotlib.pyplot as plt
import csv
import math

file = './data/csv/EddRes.csv'

data = []

with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

del data[:1]

Country = []
X = []
Y = []

for dat in data:
    Country.append(dat[0])
    X.append(float(dat[2]))
    Y.append(float(dat[4]))

plt.title("[Td at the day of 1>Deaths/Mil.Pop. and Deaths/Mil.Pop(2020/5/20)]")
plt.ylabel("Deaths/Mil.Pop.")
plt.xlabel("Td")
plt.yscale('log')

Jpn = Country.index('Japan')

for n in range(len(Country)):
    if (n == Jpn):
        plt.scatter(X[n],Y[n],s=20,c="red")
        plt.text(X[n], Y[n], 'JAPAN', color='black', fontsize=15)
    else:
        plt.scatter(X[n],Y[n],s=10,c="green")
        plt.text(X[n], Y[n], Country[n], alpha=0.8, color='black', fontsize=8)

#plt.ylim(0.01,2000)
#plt.xlim(0,50)
plt.grid(which="both")
plt.show()
#plt.savefig('DeMilSMOKE2016.png')
#plt.savefig('DeMilSMOKE2016.svg')
