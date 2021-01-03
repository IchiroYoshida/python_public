"""
    暦・潮時表  TD2/TD3 version.
    2019/06/23
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""

import sys
import math
import ephem
import datetime
import func.tide_func as tf 
import numpy as np
import func.TD3read as td
#import func.TD2read as td

year = 2019

moon = ephem.Moon()
sun = ephem.Sun()
pt_eph = ephem.Observer()

pt = tf.Port()
pt.name = td.name
pt.lat = td.lat
pt.lng = td.lng
pt.level = td.level

pt.pl = td.pl
pt.hr = td.hr

for month in range (1, 13):

    moon_rise = {}
    moon_set = {}

    days = tf.month_days(year,month)

    print('\n{:04d} 年'.format(year),'{:>2d} 月'.format(month), pt.name)
    print("  日  潮 月齢 |    満潮 （時刻、潮位cm）  　干潮 （時刻、潮位cm） 　|  日の出、入   |  月の出、入  ")

    # Moon Rise and Set calculation
    for day in range(1,days+1):

        pt_eph.lon = str(pt.lng)
        pt_eph.lat = str(pt.lat)
        pt_eph.elevation = 0.0
        pt_eph.pressure = 0
        pt_eph.horizon = '-0:34'

        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        pt_eph.date = str(date0+' 9:00')  #UT+9hr = JST
        date_location = pt_eph.date

        today_moon = tf.Moon(pt_eph)
        today_moon.rise(pt_eph)
        moon_rise.update({today_moon.index:today_moon})

        pt_eph.date = date_location
        today_moon = tf.Moon(pt_eph)
        today_moon.set(pt_eph)
        moon_set.update({today_moon.index:today_moon})

    # Sun set and rise calculation
    for day in range(1, days+1):

        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        pt_eph.date = str(date0 + ' 9:00')   #UT+9hr ->JST
        weekday = tf.get_weekday(date0)

        date1 = repr(ephem.localtime(pt_eph.date))
        date2 = eval(date1)
        date_str = date2.strftime('%Y%m%d')
        mm = int(date2.strftime('%m'))

        #---- Sun rise ------
        today_sun = tf.Sun(pt_eph)
        today_sun.sun_rise(pt_eph)
        SunRise = today_sun.sun_rise

        #---- Sun set -------
        today_sun = tf.Sun(pt_eph)
        today_sun.sun_set(pt_eph)
        SunSet = today_sun.sun_set

        #---- Tide and Moon age ---
        today_moon = tf.Moon(pt_eph)
        today_moon.noon(pt_eph)
        tide_name = today_moon.tname
        moon_age = str('%3.1f' % today_moon.moonage)

        rise = moon_rise.get(date_str)

        if rise is None:
            rise_str = "--:--"
        else:
            rise_str = rise.hhmm
        
        set = moon_set.get(date_str)

        if set is None:
            set_str = "--:--"
        else:
            set_str = set.hhmm

        pt.date = date0

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

        print('{:2d}'.format(day), weekday, tide_name, '{:>4s}'.format(moon_age),"|",\
                hitide_prn[0],hitide_prn[1],lowtide_prn[0],lowtide_prn[1], "|", \
                SunRise,'-',SunSet, "|", rise_str,'-', set_str)

