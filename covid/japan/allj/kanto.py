import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csv_path = './data/csv2/'

files = os.listdir(csv_path)
files.sort()

for file in files:
    country = file.split('.csv')[0]

    read_csv = csv_path+file
    csv = pd.read_csv(read_csv)

    Td7 = csv['Td7']
    D7 = Td7.values.tolist()
    x  = len(D7)

    X = np.arange(x)

    if (country == 'Tokyo'):
        plt.plot(X,D7,color='red', linewidth ='3', zorder=1)
    if (country == 'Saitama'):
        plt.plot(X,D7,color='blue', linewidth ='2',zorder=0)
    if (country == 'Kanagawa'):
        plt.plot(X,D7,color='green', linewidth ='2',zorder=0)
    if (country == 'Chiba'):
        plt.plot(X,D7,color='black', linewidth ='2',zorder=0)
    if (country == 'Osaka'):
        plt.plot(X,D7,color='cyan',linewidth ='2',zorder=0)


    #else:
    #    plt.plot(X,D7,zorder=0)

    xx = X[-1]
    yy = D7[-1]
    
    if (country == 'Tokyo'):
        plt.text(xx,yy,country,fontsize=20)
    if (country == 'Saitama'):
        plt.text(xx,yy,country,fontsize=20)

    if (country == 'Kanagawa'):
        plt.text(xx,yy,country,fontsize=20)
    if (country == 'Chiba'):
        plt.text(xx,yy,country,fontsize=20)
    if (country == 'Osaka'):
        plt.text(xx,yy,country,fontsize=20)

plt.title('COVID-19 2020 Pandemic in Japan')
plt.xlabel('Days since 2020/03/18')
plt.ylabel('Td7')
plt.yscale('log')
plt.ylim(1,10000)
plt.grid(which='both')
plt.show()
plt.close()

