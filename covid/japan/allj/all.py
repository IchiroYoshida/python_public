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
    else:
        plt.plot(X,D7,zorder=0)

    xx = X[-1]
    yy = D7[-1]
    
    if (country == 'Tokyo'):
        plt.text(xx,yy,country,fontsize=20)
    else:
        plt.text(xx,yy,country,fontsize=10)

plt.title('COVID-19 2020 Pandemic in Japan')
plt.xlabel('Days since 2020/03/18')
plt.ylabel('Td7')
plt.yscale('log')
plt.ylim(1,5000)
plt.grid(which='both')
plt.show()
plt.close()

