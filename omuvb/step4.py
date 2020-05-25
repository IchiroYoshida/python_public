'''
 Correlation coefficient of
 Deaths/Mil.populations and Smoker population(%:2016).

 step4.py

 2020-05-19

'''
import numpy as np
import csv
import math

file = './DeMilSMOKE2016.csv'

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
    Y.append(math.log(float(dat[3])))

a = np.corrcoef(X, Y)[0, 1]

print(a)

