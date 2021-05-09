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
    Rval0 = csv['Rt']
    #print(Rval0.head())

    Rval = Rval0.values.tolist()
    Days = len(Rval)

    dates = np.array([base + datetime.timedelta(days=i) for i in range(Days)])
    locator = mdates.AutoDateLocator(maxticks=30)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    if (country == 'Tokyo'):
        ax.plot(dates,Rval,color='red', linewidth ='3', zorder=1)

    xx = dates[-1]
    yy = Rval[-1]
    
    if (country == 'Tokyo'):
        ax.text(xx,yy,country,fontsize=20)

plt.title('2020 COVID-19  Pandemic in Japan R0',fontsize=30)
plt.ylabel('R0',fontsize=20)
#plt.yscale('log')
plt.ylim(0,2)
plt.grid(which='both')
plt.show()
plt.close()
