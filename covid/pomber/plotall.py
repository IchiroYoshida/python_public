'''
   plot World countries (csv2 - plot) 

   2020-05-23
'''
import os
import math
import csv
import matplotlib.pyplot as plt
import numpy as np

path ='./data/csv2/'
files = os.listdir(path)
files.sort()

for file in files:
    csvRow = []
    read_csv = path+file
    with open(read_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            csvRow.append([row][0])
    del csvRow[:2]

    country = file.split('.')[0]
    C1 = []  #Case (Day) bar -- green
    C2 = []  #Case (Day Ave7.) line -- blue
    D1 = []  #Death (Day) bar -- red
    D2 = []  #Death (Day Ave7.) line -- black

    for dat in csvRow:
        date =   dat[0]
        cases1 = dat[5]
        cases2 = dat[6]
        death1 = dat[9]
        death2 = dat[10]

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

    plt.legend(['Cases and Deaths in'+country])
    plt.xlabel('Days')
    plt.ylabel('Number')
    #plt.yscale('log')
    plt.grid(which="both")
    #plt.show()
    save_name = './data/plot/'+country+'.png'
    plt.savefig(save_name)
    plt.close()
