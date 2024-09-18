'''
 .log -> .png  
2024/09/15
'''
import func.td3new as td
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

LOG = './LOG/2023log/'
PNG = './PNG/2023png/'

name = '石垣'
year = '2023'
tide3 = td.TD3(year)

log_files = os.listdir(LOG)
log_files.sort()

for logs in log_files:
    with open(LOG+logs, encoding='utf8', newline='') as l:
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
        #print(date_prn)

        t2 = pt.tide[(date+"  8:00"):(date+"  20:00")]
        t_dive = pt.tide[(date+' '+EntT):(date+' '+ExtT)]

        eb2 = pt.ebb[(date+"  8:00"):(date+"  20:00")]
        fl2 = pt.flow[(date+"  8:00"):(date+"  20:00")]

        EbbLevels = eb2.values
        EbbTimes  = eb2.index
        FlowLevels = fl2.values
        FlowTimes  = fl2.index

        Tmin = datetime.datetime.strptime(date+"  7:45",'%Y/%m/%d %H:%M')
        Tmax = datetime.datetime.strptime(date+" 20:15",'%Y/%m/%d %H:%M')

        fig, ax = plt.subplots()
        sns.lineplot(data=t2, color = 'blue', linewidth =2, ax = ax)
        sns.lineplot(data=t_dive, color = 'red', linewidth =5, ax = ax)

        ax.set_xlim(Tmin,Tmax)
        ax.set_xlabel('(時)')
        ax.set_ylabel('潮位(cm)')
        ax.set_title(date_prn)
        formatter = mdates.DateFormatter('%H:%M')
        ax.xaxis.set_major_formatter(formatter)

        offset = 5 
        td =datetime.timedelta(minutes=30)

        #08:00 Left
        ti = datetime.datetime.strptime(date+ "   8:00",'%Y/%m/%d %H:%M')
        hi = t2[(date + "  8:00")]
        StrLevel ='{:.0f}'.format(hi)+' (cm)'
        ax.text(ti, hi-offset, StrLevel)

        #20:00 Right
        ti = datetime.datetime.strptime(date+ "  20:00",'%Y/%m/%d %H:%M')
        hi = t2[(date + " 20:00")]
        StrLevel ='{:.0f}'.format(hi)+' (cm)'
        ax.text(ti, hi-offset, StrLevel)
                                   
        #干潮の表示
        for time, level in zip(EbbTimes, EbbLevels):
            StrTime =time.strftime('%H:%M')
            StrLevel = '{:.0f}'.format(level)+' (cm)'
            ax.text(time-td, level-offset, StrTime)
            ax.text(time-td, level+offset, StrLevel)

        #満潮の表示
        for time, level in zip(FlowTimes, FlowLevels):
            StrTime =time.strftime('%H:%M')
            StrLevel = '{:.0f}'.format(level)+' (cm)'
            ax.text(time-td, level-offset, StrTime)
            ax.text(time-td, level+offset, StrLevel)

        ax.grid()
        #plt.show()
        FName=dat[0]+'N'+DayNo
        plt.savefig(PNG+FName+'.png')
        plt.close('all')