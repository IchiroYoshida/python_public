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

fig, ax = plt.subplots(figsize=(10, 7))
base = datetime.datetime(2020,3,18)

for file in files:
    country = file.split('.csv')[0]

    read_csv = csv_path+file
    csv = pd.read_csv(read_csv)

    Td7 = csv['Td7']
    D7 = Td7.values.tolist()
    Days  = len(D7)

    dates = np.array([base + datetime.timedelta(days=i) for i in range(Days)])
    locator = mdates.AutoDateLocator(maxticks=30)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    if (country == 'Tokyo'):
        ax.plot(dates, D7,color='red', linewidth ='3', zorder=1)
    if (country == 'Saitama'):
        ax.plot(dates, D7,color='blue', linewidth ='2',zorder=0)
    if (country == 'Kanagawa'):
        ax.plot(dates, D7,color='green', linewidth ='2',zorder=0)
    if (country == 'Chiba'):
        ax.plot(dates, D7,color='black', linewidth ='2',zorder=0)
    if (country == 'Osaka'):
        ax.plot(dates, D7,color='yellow',linewidth ='2',zorder=0)
    if (country == 'Hokkaido'):
        ax.plot(dates, D7,color='cyan',linewidth='2',zorder=0)


    xx = dates[-1]
    yy = D7[-1]
    
    if (country == 'Tokyo'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Saitama'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Kanagawa'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Chiba'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Osaka'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Hokkaido'):
        ax.text(xx,yy,country,fontsize=20)


plt.title('COVID-19 2020 Pandemic in Japan')
plt.xlabel('Day')
plt.ylabel('Td7')
plt.yscale('log')
plt.ylim(1,10000)
plt.grid(which='both')
plt.show()
plt.close()

