'''
 Correlation coefficient of
 1>deaths/Mil.pop. of Td7 and Deaths/Mil. pop. on 2020/05/20

 corr1.py

 2020-05-24

'''
import numpy as np
import csv
import math

file = './data/csv/EddRes.csv'

data = []

with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

del data[:1]

X = []
Y = []

for dat in data:
    X.append((float(dat[2])))
    Y.append(math.log(float(dat[4])))

a = np.corrcoef(X, Y)[0, 1]

print(a)

