"""
    潮時表  TD2/TD3 version.
    2019/06/23
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""

import sys
import math
import ephem
import datetime
import func.tide_func as tf 
#from func.moon_calc import *
import numpy as np
import func.TD3read as td
#import func.TD2read as td

year = 2019

pt = tf.Port

pt.name = td.name
pt.lat = td.lat
pt.lng = td.lng
pt.level = td.level

pt.pl = td.pl
pt.hr = td.hr

for month in range (1,13):
    days = tf.month_days(year,month)

    print (year,month)

    for day in range(1,days+1):
    #for day in range(1,3):

        moon=ephem.Moon()

        pt_eph=ephem.Observer()
        pt_eph.lon, pt_eph.lat = pt.lng,pt.lat
        pt_eph.elevation = 0.0

        pt.date = str(year)+str('/%02d' % month)+str('/%02d' % day)
        pt_eph.date = str(pt.date+' 9:00')

        date_prn = str(pt.date)
        weekday  = tf.get_weekday(pt.date)

        today_moon = tf.Moon(pt_eph)
        today_moon.noon(pt_eph)

        moon_prn = today_moon.tname+str(' %4.1f' % today_moon.moonage)

        today = tf.Tide(pt)
        today.wav(pt)

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

        print('{0:2d}'.format(day),weekday,moon_prn,hitide_prn[0],hitide_prn[1],lowtide_prn[0],lowtide_prn[1])
