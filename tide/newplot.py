"""
    New Tide plot. 
    2023/06/20
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""
import func.td3 as td
import func.harm60 as h6
import func.MoonEph as ME
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

name = '石垣'
date = '2023/06/20'

td3 = td.TD3(name)
pt = h6.Tide(td3,date)
me = ME.MoonEph(date)

date_prn = name+date+'  '+me.tide_name+'潮'+'  月齢  '+me.moon_age+' 日'
t2 = pt.tide[(date+"  8:00"):(date+"  20:00")]
Tide = t2.values
Time = t2.index

eb2 = pt.ebb[(date+"  8:00"):(date+"  20:00")]
fl2 = pt.flow[(date+"  8:00"):(date+"  20:00")]

EbbLevels = eb2.values
EbbTimes  = eb2.index
FlowLevels = fl2.values
FlowTimes  = fl2.index

Tmin = datetime.datetime.strptime(date+"  7:45",'%Y/%m/%d %H:%M')
Tmax = datetime.datetime.strptime(date+" 20:15",'%Y/%m/%d %H:%M')

fig, ax = plt.subplots()
ax.plot(Time, Tide)
ax.set_xlim(Tmin,Tmax)
ax.set_xlabel('(時)')
ax.set_ylabel('潮位(cm)')
ax.set_title(date_prn)
formatter = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(formatter)

offset = 5
for time, level in zip(EbbTimes, EbbLevels):
    print('time=',time)
    StrTime =time.strftime('%H:%M')
    StrLevel = '{:.0f}'.format(level)+' (cm)'
    ax.text(time, level-offset, StrTime)
    ax.text(time, level+offset, StrLevel)

for time, level in zip(FlowTimes, FlowLevels):
    StrTime =time.strftime('%H:%M')
    StrLevel = '{:.0f}'.format(level)+' (cm)'
    ax.text(time, level-offset, StrTime)
    ax.text(time, level+offset, StrLevel)

ax.grid()
plt.show()

plt.close('all')
