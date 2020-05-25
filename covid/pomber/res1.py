'''
   Pomber GitHub World countries (csv2 - plot) 

   2020-05-23
'''
import os
import math
import csv
import matplotlib.pyplot as plt
import numpy as np

path ='./data/csv2/'
out_file = './data/res/daysDMil1.csv'

files = os.listdir(path)
files.sort()

outRow = []
for file in files:
    csvRow = []
    read_csv = path+file
    with open(read_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            csvRow.append([row][0])
    del csvRow[:2]

    country = file.split('.')[0]
        
    for dat in csvRow:
        date =   dat[0]
        td   =   dat[1]
        death =  float(dat[10])
        if (death > 1.):
            outRow.append([country,date,td])
            break

with open(out_file,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Country','date','Td(days)'])
    writer.writerows(outRow)
