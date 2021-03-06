'''
    plot Japanese areas (csv2 -> Pandas -> plot)
    
    2020-07-02
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

    C1 = c1.values.tolist()  # green
    C2 = c2.values.tolist()  # blue
    D1 = d1.values.tolist()  # red
    D2 = d2.values.tolist()  # black

    plt.bar(X,C1,linewidth=4,color="green")
    plt.bar(X,D1,linewidth=4,color="red")
    plt.plot(X,C2,linestyle="solid",linewidth=2,color="blue")
    plt.plot(X,D2,linestyle="solid",linewidth=2,color="black")

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

