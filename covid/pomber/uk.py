'''
   plot World 

   2020-05-06
'''
import math
import csv
import matplotlib.pyplot as plt
import numpy as np

read_csv = './data/csv2/United Kingdom.csv'

csvRow = []

with open(read_csv) as f:
    reader = csv.reader(f)
    for row in reader:
        csvRow.append([row][0])
del csvRow[:2]

C1 = []  #Case (Day) bar -- green
C2 = []  #Case (Day Ave7.) line -- blue
D1 = []  #Death (Day) bar -- red
D2 = []  #Death (Day Ave7.) line -- black

for dat in csvRow:
    date =   dat[0]
    cases1 = dat[4]
    cases2 = dat[5]
    death1 = dat[8]
    death2 = dat[9]

    C1.append(int(cases1))
    C2.append(float(cases2))
    D1.append(int(death1))
    D2.append(float(death2))

X = range(len(csvRow))

for n in range(len(C1)):
    plt.bar(X[n],C1[n], color = "green", linewidth=4)
for n in range(len(D1)):
    plt.bar(X[n],D1[n], color = "red", linewidth=4)
plt.plot(X,C2,linestyle="solid",linewidth=2,color="blue")
plt.plot(X,D2,linestyle="solid",linewidth=2,color="black")

plt.legend(['Cases and Deaths in UK.'])
plt.xlabel('Days')
plt.ylabel('Number')
#plt.yscale('log')
plt.grid(which="both")
plt.show()

