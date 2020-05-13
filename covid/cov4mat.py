'''
 Plot deaths/Mil.populations for x axis, and plot latitude for y axis

 2020-05-13 Ichiro Yoshida
'''
import matplotlib.pyplot as plt
import csv
import math

file = './COVID_LAT.csv'

data = []

with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
    day_data = []
    while len(data):
        line = data[:1]
        for lin in line[0]:
            date_str=lin.split(' ')[0]
        day_data.append(line[0])
        del data[:1]
    del day_data[:1]

Country=[]
X=[]
Y=[]

del day_data[:1]
while len(day_data):
    dat = day_data[:1][0]
    Country.append(dat[0])
    X.append(float(dat[3]))
    Y.append(float(dat[4]))
    del day_data[:1]

plt.title("[Deaths/Mil.Pop. and Latitude 2020/05/13]")
plt.xlabel("Deaths/Mil.Pop.")
plt.ylabel("Latitude")
#plt.yscale('log')
plt.xscale('log')

for n in range(len(Country)):
    plt.scatter(X[n],Y[n],c="pink", linewidth="2", edgecolors="red")
    plt.text(X[n], Y[n], Country[n], color='black', fontsize=10)

plt.grid(which="both")
plt.show()

