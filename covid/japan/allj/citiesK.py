import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import matplotlib.dates as mdates

csv_path = './data/csv2/'

files = os.listdir(csv_path)
files.sort()

fig, ax = plt.subplots(constrained_layout=True,figsize=(10,7))
base = datetime.datetime(2020,3,18)

for file in files:
    country = file.split('.csv')[0]

    read_csv = csv_path+file
    csv = pd.read_csv(read_csv)

    Kval0 = csv['K']
    Kval = Kval0.values.tolist()
    Days = len(Kval)

    dates = np.array([base + datetime.timedelta(days=i) for i in range(Days)])
    locator = mdates.AutoDateLocator(maxticks=30)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    if (country == 'Tokyo'):
        ax.plot(dates,Kval,color='red', linewidth ='3', zorder=1)
    if (country == 'Osaka'):
        ax.plot(dates,Kval,color='blue', linewidth ='2',zorder=0)
    if (country == 'Aichi'):
        ax.plot(dates,Kval,color='green', linewidth ='2',zorder=0)
    if (country == 'Fukuoka'):
        ax.plot(dates,Kval,color='black', linewidth ='2',zorder=0)
    if (country == 'Hokkaido'):
        ax.plot(dates,Kval,color='cyan',linewidth ='2',zorder=0)

    xx = dates[-1]
    yy = Kval[-1]
    
    if (country == 'Tokyo'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Osaka'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Fukuoka'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Aichi'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Hokkaido'):
        ax.text(xx,yy,country,fontsize=20)

plt.title('2020 COVID-19  Pandemic in Japan Kval',fontsize=30)
plt.ylabel('Kval',fontsize=20)
plt.yscale('log')
plt.ylim(0.0001,1)
plt.grid(which='both')
plt.show()
plt.close()

