'''
 Plot Td(doubling time) for x axis, deaths/Mil.populations for y axis

 2020-03-25 Ichiro Yoshida
'''
import matplotlib.pyplot as plt
import csv
import math

path = './td7/'
file = 'Mil20200401.csv'

data = []

with open(path+file) as f:
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
Deaths = []

del day_data[:1]
while len(day_data):
    dat = day_data[:1][0]
    Country.append(dat[0])
    deaths = (math.log(int(dat[1])))*2.
    Deaths.append(int(deaths))
    X.append(float(1./float(dat[2])))
    Y.append(float(dat[3]))
    del day_data[:1]

plt.title("[1/Td / deaths/Mil.Pop. 2020/04/01]")
plt.xlabel("1/Td(Doubling time days)")
plt.ylabel("deaths/Mil.Pop.")
plt.yscale('log')
plt.xscale('log')

for n in range(len(Country)):
    plt.scatter(X[n],Y[n],s=Deaths[n],c="pink", linewidth="2", edgecolors="red")
    plt.text(X[n], Y[n], Country[n], color='black', fontsize=10)

plt.grid(which="both")
plt.show()

