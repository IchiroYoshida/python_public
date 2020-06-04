'''
 Correlation coefficient of
 Deaths/Mil.populations and TBC population(%:2018).

 step4.py

 2020-06-04

'''
import numpy as np
import csv
import math
from scipy.stats import pearsonr

file = './DeMilTBC2018.csv'

data = []

with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

del data[:1]

X = []
Y = []

for dat in data:
    xx = float(dat[2])
    yy = float(dat[3])
    if (xx>0):
        X.append(math.log(xx))
        Y.append(math.log(yy))

val,p = pearsonr(X, Y)

print('Corrcoef val %f p val %f'%(val, p))


