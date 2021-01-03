import csv

f = open('201804.csv','r')

dataReader = csv.reader(f)


for row in dataReader:
    print(row[0],row[1],row[2])


