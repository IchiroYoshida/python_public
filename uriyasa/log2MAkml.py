'''
.log -> .csv
2024/09/19
'''
import os
import csv

import func.td3new as td
import func.harm60 as h6
import func.MoonEph as ME
import datetime
import numpy as np
import pandas as pd

LOG = './log/'
col =['Date','Moon Age','Day No.','Start Time','Start Lat.','Start Lng.','End Time','End Lat.','End Lng.','Type']
csvFile= './AllLogs.csv'

log_files = os.listdir(LOG)
log_files.sort()

list=[]
for logs in log_files:  #[:50]:
    with open(LOG+logs, encoding='utf8', newline='') as l:
        csvreader =csv.reader(l)
        data = [row for row in csvreader][0]
        
        dat = logs.replace('.log','').split('N')
        
        YY = dat[0][:4]  #Year
        MM = dat[0][4:6] #Month
        DD = dat[0][6:]  #Day
        DayNo = dat[1]   #Tanks of the day
        date = YY+'/'+MM+'/'+DD
        
        Year = int(YY)

        if (Year < 2023 ):
            tide3 = td.TD3('2011')
        elif (Year == 2023):
            tide3 = td.TD3('2023')
        elif (Year == 2024):
            tide3 = td.TD3('2024')
        else :
            print('TD3 Year ERROR!')
            exit()
        
        pt = h6.Tide(tide3,date)
        me = ME.MoonEph(date)

        MA = '{:.1f}'.format(float(me.moon_age))
        print(date, MA)

        EntT   = data[0]  #Entry
        EntLat = float(data[1])
        EntLng = float(data[2])
        
        ExtT   = data[3]  #Exit
        try:
            ExtLat = float(data[4])
            ExtLng = float(data[5])
            Style = 'D'
        except:
            ExtLat = ''
            ExtLng = ''
            Style = 'A'
        
    list.append([date,MA,DayNo,EntT,EntLat,EntLng,ExtT,ExtLat,ExtLng,Style])

df=pd.DataFrame(data=list,columns=col)
df['Moon Age'] = df['Moon Age'].astype(float)
dfMA = df.sort_values('Moon Age')
dfMA.to_csv(csvFile, index=False)