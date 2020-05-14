'''
Correlation coefficient of
deaths/Mil.populations  and latitude.

 2020-05-14 Ichiro Yoshida
'''
import numpy as np
import csv
import math

file = './world.csv'

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
    X.append(math.log(float(dat[3])))
    Y.append(math.fabs(math.cos(math.radians(float(dat[4])))))
    del day_data[:1]

a = np.corrcoef(X, Y)[0, 1]
print(a)

