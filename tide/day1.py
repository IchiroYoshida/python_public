"""
    潮時表  TD2/TD3 version.
    2023/06/13
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""

import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ephem
import datetime
import func.tide_func as tf 
import numpy as np
import func.TD3read as td
#from func.peakdetect import *
from scipy.signal import argrelmin, argrelmax

date = '2023/06/16'
dt = datetime.datetime.strptime(date,'%Y/%m/%d')

pt = tf.Port

pt.name = td.name
pt.lat = td.lat
pt.lng = td.lng
pt.level = td.level
pt.date = date

pt.pl = td.pl
pt.hr = td.hr

#ephem definiction 
moon = ephem.Moon()
pt_eph = ephem.Observer()
pt_eph.long, pt_eph.lat = pt.lng, pt.lat
pt_eph.elevation = 0.0
pt_eph.date = str(pt.date + ' 9:00')

#weekday = tf.get_weekday(pt.date)+' 曜日'
today_moon = tf.Moon(pt_eph)
today_moon.noon(pt_eph)

date_prn = '石垣港   '+date+'  '+today_moon.tname+'潮'+str('    月齢  %4.1f 日' % today_moon.moonage)

today = tf.Tide(pt)
today.wav(pt)

level  = today.tl
tide   = today.tide
hitide = today.hitide
lowtide= today.lowtide

ti = pd.Series(tide, index=pd.date_range(pt.date+"  0:00", pt.date+" 23:59", freq='min'))
print(ti.head())

t2 = ti[(pt.date+"  8:00"):(pt.date+"  19:59")]

#Tide = t2.values.tolist()
Tide = t2.values
#Time = t2.index.tolist()
Time = t2.index
Tmin = datetime.datetime.strptime(pt.date+"  7:45",'%Y/%m/%d %H:%M')
Tmax = datetime.datetime.strptime(pt.date+" 20:15",'%Y/%m/%d %H:%M')

#満潮と干潮
hitides,lowtides = argrelmax(Tide),argrelmin(Tide)
print('満潮=',Tide[hitides],Time[hitides])
print('干潮=',Tide[lowtides],Time[lowtides])


fig, ax = plt.subplots()
ax.plot(Time, Tide)
ax.set_xlim(Tmin,Tmax)
ax.set_xlabel('(時)')
ax.set_ylabel('潮位(cm)')
ax.set_title(date_prn)

ax.grid()
plt.show()

plt.close('all')
