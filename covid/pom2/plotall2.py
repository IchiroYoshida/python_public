'''
    plot World countries (csv2 -> Pandas -> plot)
    
    2020-07-25
'''
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import matplotlib.dates as mdates

csv2_path = './data/csv2/'
plot_path = './data/plot2/'

files = os.listdir(csv2_path)
files.sort()

#files = ['Brazil.csv']

for file in files:
    country = file.split('.csv')[0]
    read_csv = csv2_path+file
    csv = pd.read_csv(read_csv)

    demil = csv[csv['Deaths /1M pop (Ave7)'] > .1]
    if(len(demil)>10):
        date0 = demil['date']
        date = date0.values.tolist()
        date_str = date[0].split('-')
        base = datetime.datetime(int(date_str[0]),
                int(date_str[1]),
                int(date_str[2]))
        fig, ax = plt.subplots(constrained_layout=True, figsize=(10, 7))

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

            Days  = len(c1.values.tolist())

            dates = np.array([base + datetime.timedelta(days=i) for i in range(Days)])
            locator = mdates.AutoDateLocator(maxticks=30)
            formatter = mdates.ConciseDateFormatter(locator)
            ax.xaxis.set_major_locator(locator)
            ax.xaxis.set_major_formatter(formatter)

            C1 = c1.values.tolist()  
            C2 = c2.values.tolist()
            D1 = d1.values.tolist() 
            D2 = d2.values.tolist() 

            ax.bar(dates,C1,linewidth=4)
            ax.bar(dates,D1,linewidth=4)
            ax.plot(dates,C2,linestyle="solid",linewidth=2)
            ax.plot(dates,D2,linestyle="solid",linewidth=2)

            title = '2020 COVID-19 Pandemic Cases and Deahts/1M pop. in '+country
            plt.title(title,fontsize=20)
            plt.legend('Cases and Deaths')
            plt.ylabel('Number/1M pop')
            #plt.yscale('log')
            plt.grid(which="both")
            #plt.show()
            save_name = plot_path+country+'.png'
            print(save_name)
            plt.savefig(save_name)
            plt.close()

