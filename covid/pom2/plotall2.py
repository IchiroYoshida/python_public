'''
    plot World countries (csv2 -> Pandas -> plot)
    
    2020-06-14
'''
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csv2_path = './data/csv2/'
plot_path = './data/plot/'

files = os.listdir(csv2_path)
files.sort()

for file in files:
    country = file.split('.csv')[0]
    read_csv = csv2_path+file
    csv = pd.read_csv(read_csv)

    demil = csv[csv['Deaths /1M pop (Ave7)'] > .1]

    demil0 = demil['Deaths /1M pop (Ave7)']
    d0 = demil['Deaths Total(Ave7)']

    Mpop0 = d0 /demil0
    Mpop1 = Mpop0.values.tolist()

    Mpop = Mpop1[-1:]

    if(Mpop):
        c1 = demil['Cases Day'] / Mpop         
        c2 = demil['Cases Day(Ave7)'] /Mpop  
        d1 = demil['Deaths Day'] /Mpop
        d2 = demil['Deaths Day(Ave7)'] /Mpop 

        x  = len(c1.values.tolist())
        X  = np.arange(x)

        C1 = c1.values.tolist()  
        C2 = c2.values.tolist()
        D1 = d1.values.tolist() 
        D2 = d2.values.tolist() 

        plt.bar(X,C1,linewidth=4)
        plt.bar(X,D1,linewidth=4)
        plt.plot(X,C2,linestyle="solid",linewidth=2)
        plt.plot(X,D2,linestyle="solid",linewidth=2)

        plt.legend(['Cases and Deaths/1M pop in '+country])
        plt.xlabel('Days')
        plt.ylabel('Number')
        #plt.yscale('log')
        plt.grid(which="both")
        #plt.show()
        save_name = './data/plot2/'+country+'.png'
        print(save_name)
        plt.savefig(save_name)
        plt.close()
