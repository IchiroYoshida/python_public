import math
import ephem
import datetime
import tide_func
from moon_calc import *
import numpy as np
import data_read

year = 2018

class TideDay(object):
     def __init__(self):
          self.serial_day = 0
          self.weekday = ''
          self.moon_age = ''
          self.tide_age = ''
          self.high_tide = ''
          self.low_tide = ''

class TideYear(object):
     def __init__(self,object,year,location):
          self.year = year
          self.location = location

          self.day_data = (365+1)*[]

          for i in range (0,365+1):
              self.day_data.append(TideDay())

     def calcTideData(self,object):
          for month in range (1,13):
               month_days = tide_func.month_days(self.year,month)

               print(self.year,month)

               for d in range(0,month_days):

                    moon = ephem.Moon()

                    pt_eph = ephem.Observer()
                    pt_eph.lon, pt_eph.lat = pt.lng, pt.lat
                    pt_eph.elevation = 0.0

                    day = d + 1

                    pt.date = str(self.year)+('/%02d' % month)+str('/%02d' % day)
                    pt_eph.date = str(pt.date + ' 9:00')

                    date_prn = str(pt.date)

                    today_moon = Moon(pt_eph)
                    today_moon.noon(pt_eph)

                    moon_prn = today_moon.tname + str(' %4.1f' % today_moon.moonage)
                    today = tide_func.Tide(pt)
                    tt = today.wav(pt)

                    level = today.tl
                    tide = today.tide
                    hitide = today.hitide
                    lowtide = today.lowtide

                    hitide_prn = []
                    lowtide_prn = []

                    for hi in hitide:
                         hitide_prn.append(str(' %5s - %3s' % (hi[0],hi[1])))
                    for lo in lowtide:
                         lowtide_prn.append(str(' %5s - %3s' % (lo[0],lo[1])))
                    if len(hitide_prn) < 2 :
                         hitide_prn.append(' --:--   ***')
                    
                    if len(lowtide_prn) < 2:
                         lowtide_prn.append(' --:--   ****')

                    #print(day,weekday,moon_prn,hitide_prn[0],hitide_prn[1],lowtide_prn[0],lowtide_prn[1])

