'''
 Plot UVB(J/m2)  for x axis, 
     and Deaths/Mil.populations on 2020/05/20 for y axis

 plot2.py

 2020-05-24

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
    X.append(float(dat[3]))
    Y.append(float(dat[4]))

plt.title("[UVB(EDD:J/m2) and Deaths/Mil.Pop(2020/5/20)]")
plt.ylabel("Deaths/Mil.Pop.")
plt.xlabel("UVB(EDD:J/m2)")
plt.yscale('log')

Jpn = Country.index('Japan')

for n in range(len(Country)):
    if (n == Jpn):
        plt.scatter(X[n],Y[n],s=20,c="red")
        plt.text(X[n], Y[n], 'JAPAN', color='black', fontsize=15)
    else:
        plt.scatter(X[n],Y[n],s=10,c="green")
        plt.text(X[n], Y[n], Country[n], alpha=0.8, color='black', fontsize=8)

plt.ylim(1,2000)
plt.xlim(0,8000)
plt.grid(which="both")
plt.show()
#plt.savefig('DeMilSMOKE2016.png')
#plt.savefig('DeMilSMOKE2016.svg')
