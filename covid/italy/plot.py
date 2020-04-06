'''
   plot Italy

   2020-03-28
'''
import math
import csv
import matplotlib.pyplot as plt
import numpy as np

read_csv = './data/Italy.csv'

csvRow = []

with open(read_csv) as f:
    reader = csv.reader(f)
    for row in reader:
        csvRow.append([row][0])
del csvRow[:2]

C = []

for dat in csvRow:
    date = dat[0]
    cases = dat[1]
    deaths = dat[2]
    C.append(int(cases))

X = range(len(csvRow))

for n in range(len(C)):
    plt.scatter(X[n],C[n],s=10,c="pink", linewidth="2", edgecolors="red")

plt.legend(['Cases in Italy'])
plt.xlabel('Days')
plt.ylabel('Cases')
#plt.yscale('log')
plt.grid(which="both")
plt.show()
