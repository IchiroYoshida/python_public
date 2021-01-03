"""
潮流予測表　2018.5.17
"""

import sys
import math
import ephem
import datetime
import tide_func
from moon_calc import *
import numpy as np
import data_read

year = 2019

pt = tide_func.Port()

pt.hr = np.zeros(60,np.float64)
pt.pl = np.zeros(60,np.float64)

pt.name = data_read.name 
pt.lat  = data_read.lat
pt.lng  = data_read.lng
pt.level= data_read.level

pt.hr   = data_read.hr
pt.pl   = data_read.pl

moon = ephem.Moon()
pt_eph = ephem.Observer()
pt_eph.lon = pt.lng
pt_eph.lat = pt.lat
pt_eph.elevation = 0.0

print(pt.name,pt.date)

for month in range(6,7):
   days = tide_func.month_days(year,month)

   print (year,month)

   hrs=''

   for hr in range(0,24):
      hrs +=str('%2d ' % hr)
   print('             :%s' % hrs)

   #for d in range(1,days+1):
   for d in range(1,31):

      pt.date = str(year)+str('/%02d' % month)+str('/%02d' % d)
      pt_eph.date = str(pt.date+' 9:00')

      date_prn = str(pt.date)
      weekday  = get_weekday(pt.date)

      today_moon = Moon(pt_eph)
      today_moon.noon(pt_eph)

      moon_prn = today_moon.tname+str(' %4.1f' % today_moon.moonage)

      today = tide_func.Tide(pt)
      today.wav(pt)

      current = today.tl

      cur  = (current[0:72:3]-100)/25

      prn=''
      for c in cur:
         prn += str('%+2d ' % round(c))

      print('%2d %s %s %s' % (d,weekday,moon_prn,prn))
