import sys
import math
import ephem
import datetime
import tide_func
from moon_calc import *
import numpy as np
import data_read2 as dr2

class TideDay(object):
    def __init__(self,data_read, year, month, day):

         pt = tide_func.Port

         pt.hr = np.zeros(60,np.float64)
         pt.pl = np.zeros(60,np.float64)

         pt.name = data_read.name
         pt.lat = data_read.lat
         pt.lng = data_read.lng
         pt.level = data_read.level

         pt.hr = data_read.hr
         pt.pl = data_read.pl

         moon = ephem.Moon()
         pt_eph = ephem.Observer()
         pt_eph.lon = pt.lng
         pt_eph.lat = pt.lat
         pt_eph.elevation = 0.0

         pt.date = str(year)+str('/%02d' % month) + str('/%02d' % day)
         pt_eph.date = str(pt.date+' 9:00')

         date_prn = str(pt.date)
         weekday = get_weekday(pt.date)

         today_moon = Moon(pt_eph)
         today_moon.noon(pt_eph)

         moon_prn = today_moon.tname+str(' %4.1f' % today_moon.moonage)
         today = tide_func.Tide(pt)
         tt = today.wav(pt)

         level = today.tl
         tide = today.tide
         hitide = today.hitide
         lowtide = today.lowtide

         hitide_time = np.array(hitide)[:,0]
         hitide_level = np.array(hitide)[:,1]

         hitide_prn = []
         lowtide_prn = []

         for hi in hitide:
             hitide_prn.append(str(' %5s - %3s'%(hi[0],hi[1])))
         
         for lo in lowtide:
             lowtide_prn.append(str(' %5s - %3s'%(lo[0],lo[1])))

         if len(hitide_prn) < 2 :
             hitide_prn.append(' --:--   ***')
         
         if len(lowtide_prn) < 2 :
             lowtide_prn.append(' --:--  ***')

         print(day,weekday,moon_prn,hitide_prn[0],hitide_prn[1],lowtide_prn[0],lowtide_prn[1])

if __name__ == '__main__':

    dr = dr2.DataRead('00OSE.TD2')

    td = TideDay(dr, 2018, 5, 22)
