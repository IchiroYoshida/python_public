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

    R0 = csv['Rt']
    R0v = R0.values.tolist()
    Days = len(R0v)

    dates = np.array([base + datetime.timedelta(days=i) for i in range(Days)])
    locator = mdates.AutoDateLocator(maxticks=30)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    if (country == 'Tokyo'):
        ax.plot(dates,R0v,color='red', linewidth ='3', zorder=1)
    if (country == 'Osaka'):
        ax.plot(dates,R0v,color='blue', linewidth ='2',zorder=0)
    if (country == 'Hyogo'):
        ax.plot(dates,R0v,color='steelblue', linewidth ='2',zorder=0)
    if (country == 'Okinawa'):
        ax.plot(dates,R0v,color='darkred', linewidth ='2',zorder=0)
    if (country == 'Okayama'):
        ax.plot(dates,R0v,color='gold', linewidth ='2',zorder=0)
    if (country == 'Hiroshima'):
        ax.plot(dates,R0v,color='y', linewidth ='2',zorder=0)
    if (country == 'Aichi'):
        ax.plot(dates,R0v,color='m', linewidth ='2',zorder=0)
    if (country == 'Fukuoka'):
        ax.plot(dates,R0v,color='green', linewidth ='2',zorder=0)
    if (country == 'Hokkaido'):
        ax.plot(dates,R0v,color='cyan',linewidth ='2',zorder=0)
    if (country == 'Kyoto'):
        ax.plot(dates,R0v,color='navy',linewidth ='2',zorder=0) 
    if (country == 'Zenkoku'):
        ax.plot(dates,R0v,color='black',linewidth ='4',linestyle = 'dashed',zorder=0)

    xx = dates[-1]
    yy = R0v[-1]
    
    if (country == 'Tokyo'):
        ax.text(xx,yy,'東京',fontsize=20)
    if (country == 'Osaka'):
        ax.text(xx,yy,'大阪',fontsize=20)
    if (country == 'Fukuoka'):
        ax.text(xx,yy,'福岡',fontsize=20)
    if (country == 'Aichi'):
        ax.text(xx,yy,'愛知',fontsize=20)
    if (country == 'Hokkaido'):
        ax.text(xx,yy,'北海道',fontsize=20)
    if (country == 'Zenkoku'):
        ax.text(xx,yy,'全国',fontsize=25)
    if (country == 'Kyoto'):
        ax.text(xx,yy,'京都',fontsize=20)
    if (country == 'Hyogo'):
        ax.text(xx,yy,'兵庫',fontsize=20)
    if (country == 'Okayama'):
        ax.text(xx,yy,'岡山',fontsize=20)
    if (country == 'Hiroshima'):
        ax.text(xx,yy,'広島',fontsize=20)
    if (country == 'Okinawa'):
        ax.text(xx,yy,'沖縄',fontsize=20)
         
        

plt.title('緊急事態宣言区域の実効再生算数(Rt)の推移',fontsize=30)
plt.ylabel('Rt',fontsize=20)
#plt.yscale('log')
plt.ylim(0,3.0)

plt.grid(which='both')

plt.show()
plt.close()
