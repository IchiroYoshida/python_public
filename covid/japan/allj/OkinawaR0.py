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

fig, ax  = plt.subplots(constrained_layout=True,figsize=(10,7))
base = datetime.datetime(2020, 3, 18)

for file in files:
    country = file.split('.csv')[0]

    read_csv = csv_path+file
    csv = pd.read_csv(read_csv)

    R0 = csv['R0']
    R0v = R0.values.tolist()
    Days = len(R0v)

    dates = np.array([base + datetime.timedelta(days=i) for i in range(Days)])
    locator = mdates.AutoDateLocator(maxticks=30)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    if (country == 'Tokyo'):
        ax.plot(dates,R0v,color='red', linewidth ='3', zorder=1)
    if (country == 'Okinawa'):
        ax.plot(dates,R0v,color='blue', linewidth ='2',zorder=0)
    if (country == 'Zenkoku'):
        ax.plot(dates,R0v,color='black',linewidth ='4',linestyle = 'dashed',zorder=0)

    xx = dates[-1]
    yy = R0v[-1]
    
    if (country == 'Tokyo'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Okinawa'):
        ax.text(xx,yy,country,fontsize=20)
    if (country == 'Zenkoku'):
        ax.text(xx,yy,country,fontsize=25)


plt.title('2020 COVID-19 Pandemic in Japan',fontsize=30)
plt.ylabel('R0',fontsize=20)
#plt.yscale('log')
plt.ylim(0,10)
plt.yticks(np.arange(0,10,1.0))

plt.grid(which='both')

plt.show()
plt.close()

