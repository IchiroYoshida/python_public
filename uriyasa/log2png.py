'''
 .log -> .png  
2024/09/15
'''
import func.td3 as td
import func.harm60 as h6
import func.MoonEph as ME
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

import os
import csv

name = '石垣'
tide3 = td.TD3(name)

log_files = os.listdir('./LOG')

for logs in log_files[:3]:
    with open('./LOG/'+logs, encoding='utf8', newline='') as l:
        csvreader =csv.reader(l)
        data = [row for row in csvreader][0]
        
        dat = logs.replace('.log','').split('N')
        
        YY = dat[0][:4]  #Year
        MM = dat[0][4:6] #Month
        DD = dat[0][6:]  #Day
        DayNo = dat[1]   #Tanks of the day
        date = YY+'/'+MM+'/'+DD
        
        pt = h6.Tide(tide3,date)
        me = ME.MoonEph(date)
        
        EntT   = data[0]  #Entry
        ExtT   = data[3]  #Exit
        
        date_prn = name+'   '+date+'  '+'  月齢  '+me.moon_age+' 日  '+me.tide_name+'潮' \
          +'\n '+EntT+' - '+ExtT

        print(date_prn)          
        
        
        
