'''
    plot Japanese areas (csv2 -> Pandas -> plot)
    
    2020-07-23
'''
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import matplotlib.dates as mdates

csv2_path = './data/csv2/'
plot_path = './data/plot/'

files = os.listdir(csv2_path)
files.sort()

for file in files:

    fig, ax = plt.subplots(constrained_layout=True, figsize=(12,10))
    base = datetime.datetime(2020,3,18)

    country = file.split('.csv')[0]
    read_csv = csv2_path+file
    csv = pd.read_csv(read_csv)
    c1 = csv['Cases Day'] 
    c2 = csv['Cases Day(Ave7)']   
    d1 = csv['Deaths Day']        
    d2 = csv['Deaths Day(Ave7)'] 

    Days  = len(c1.values.tolist())
    dates = np.array([base + datetime.timedelta(days=i) for i in range(Days)])
    locator = mdates.AutoDateLocator(maxticks=30)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    C1 = c1.values.tolist()  # green
    C2 = c2.values.tolist()  # blue
    D1 = d1.values.tolist()  # red
    D2 = d2.values.tolist()  # black

    ax.bar(dates,C1,linewidth=4,color="green")
    ax.bar(dates,D1,linewidth=4,color="red")
    ax.plot(dates,C2,linestyle="solid",linewidth=2,color="blue")
    ax.plot(dates,D2,linestyle="solid",linewidth=2,color="black")

    title = '2020 COVID-19 Pandemic cases and deaths in '+ country
    plt.title(title,fontsize=30)
    #plt.xlabel('Days')
    plt.ylabel('Cases',fontsize=20)
    #plt.yscale('log')
    plt.grid(which="both")
    #plt.show()
    save_name = './data/plot/'+country+'.png'
    print(save_name)
    plt.savefig(save_name)
    plt.close()

