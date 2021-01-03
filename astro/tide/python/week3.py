import sys
import tide_func
import numpy as np
import data_read
"""
一週間の潮位、M2分潮
"""
start = '2016/09/24'

year  = int(start.split('/')[0])
month = int(start.split('/')[1])
day   = int(start.split('/')[2])

days  = tide_func.month_days(year,month)

pt = tide_func.Port()

pt.hr = np.zeros(60,np.float64)
pt.pl = np.zeros(60,np.float64)
week_tide = []

pt.name = data_read.name
pt.lat  = data_read.lat
pt.lng  = data_read.lng
pt.level= data_read.level

pt.hr   = data_read.hr
pt.pl   = data_read.pl

print(pt.name,pt.date)

for d in range(0,7):
    dd=day+d
    if (dd>days):
       month += 1
       dd    -= days
       if (month >12):
           month -= 12
           year  +=  1

    pt.date = str(year)+str('/%02d' % month)+str('/%02d' % dd)

    today = tide_func.Tide(pt)
    today.wav(pt)

    level  = today.tl
    tide   = today.tidem2s2
    #tidem2  = today.tidem2

    week_tide.extend(tide[0:1440:60])

time_hr = np.arange(0,7*24*5,5)

import os
FILE = './labo_data/yonara.txt'
curr = []
curr2 = np.zeros(7*24,np.float64)

try:
  fp = open(FILE,'r')
 
except IOError as e:
  print('Cannot open %s ERR:' % FILE,e.errno)

else:
  for line in fp:
     line1=line.replace('\n','')
     if (line1[0]!='#'):
         lines=line1.split(',')
         curr.extend(map(float,lines))
         curr2 = np.array(curr)
         curr2 = curr2 *10.0

#plot

import pylab as plt
plt.plot(time_hr,week_tide,color='b')
plt.plot(time_hr,curr2,color='r') 
plt.show()
