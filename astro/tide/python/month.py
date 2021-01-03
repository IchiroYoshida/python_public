import sys
import math
import ephem
import datetime
import tide_func 
from moon_calc import *
import numpy as np
import data_read 

"""
月間月の暦、潮時表
2016/09/01
"""
table_month = '2016/09'

year  = int(table_month.split('/')[0])
month = int(table_month.split('/')[1])
days  = tide_func.month_days(year,month)

pt = tide_func.Port()

pt.hr = np.zeros(60,np.float64)
pt.pl = np.zeros(60,np.float64)

pt.name = data_read.name
pt.lat  = data_read.lat
pt.lng  = data_read.lng
pt.level= data_read.level

pt.hr   = data_read.hr
pt.pl   = data_read.pl

print(pt.name,table_month)

for d in range(0,days):
    moon=ephem.Moon()

    pt_eph=ephem.Observer()
    pt_eph.lon, pt_eph.lat = pt.lng,pt.lat
    pt_eph.elevation = 0.0

    day = d+1

    pt.date = str(year)+str('/%02d' % month)+str('/%02d' % day)
    pt_eph.date = str(pt.date+' 9:00')

    date_prn = str(pt.date)
    weekday  = get_weekday(pt.date)

    today_moon = Moon(pt_eph)
    today_moon.noon(pt_eph)

    moon_prn = today_moon.tname+str(' %4.1f' % today_moon.moonage)

    today = tide_func.Tide(pt)
    tt= today.wav(pt)

    level  = today.tl
    tide   = today.tide
    hitide = today.hitide
    lowtide= today.lowtide

    hitide_time   = np.array(hitide)[:,0]
    hitide_level  = np.array(hitide)[:,1]

    hitide_prn  = []
    lowtide_prn = []

    for hi in hitide:
       hitide_prn.append(str(' %5s - %3s'%(hi[0],hi[1])))
 
    for lo in lowtide:
       lowtide_prn.append(str(' %5s - %3s'%(lo[0],lo[1])))

    if len(hitide_prn) < 2 :
        hitide_prn.append(' --:--   ***')

    if len(lowtide_prn) < 2 :
       lowtide_prn.append(' --:--   ***')

    print(day,weekday,moon_prn,hitide_prn[0],hitide_prn[1],lowtide_prn[0],lowtide_prn[1])
