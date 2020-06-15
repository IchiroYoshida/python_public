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

    c1 = csv['Cases Day']         
    c2 = csv['Cases Day(Ave7)']   
    d1 = csv['Deaths Day']        
    d2 = csv['Deaths Day(Ave7)'] 

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

    plt.legend(['Cases and Deaths in '+country])
    plt.xlabel('Days')
    plt.ylabel('Number')
    #plt.yscale('log')
    plt.grid(which="both")
    #plt.show()
    save_name = './data/plot/'+country+'.png'
    print(save_name)
    plt.savefig(save_name)
    plt.close()

