# -*- coding:utf-8 -*-

"""
月と太陽の暦  東京(JST:UTC+9hr)
"""
import math
import ephem
import datetime
from moon_func import *
#from moon_class import *
from moon_calc import *
import calend_func 

year = 2018

moon = ephem.Moon()
sun = ephem.Sun()

tokyo = ephem.Observer()
tokyo.name = '東京'
tokyo.lon, tokyo.lat = '139.7414', '35.6581'
tokyo.elevation = 0.0

for month in range (1, 2):

    rise_dic    = {}
    set_dic     = {}
    ecl_dic     = {}

    days = calend_func.month_days(year, month)

    for d in range(0, days):

       day = d+1

       date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
       tokyo.date = str(date0+' 9:00') #UT+9hr =JST
       date_tokyo = tokyo.date

       today     = Moon(tokyo)
       today.rise(tokyo)
       rise_dic.update({today.index:today})

       tokyo.date= date_tokyo
       today     = Moon(tokyo)
       today.set(tokyo)
       set_dic.update({today.index:today})
   
       tokyo.date= date_tokyo
       today     = Moon(tokyo)
       today.noon(tokyo)
       ecl_dic.update({today.index:today})


    print(year,month,tokyo.name,tokyo.lon,tokyo.lat)

    print('  日  曜　  日出　  日没　 月齢  潮   月出  　月没')
    print('-------------------------------------------------')


    time_str = "%H:%M:%S"

    for d in range(0, days):
        day = d + 1
        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        tokyo.date = str(date0+' 9:00')

        weekday = get_weekday(date0)

        date1  = repr(ephem.localtime(tokyo.date))
        date2  = eval(date1)
        date_str   = date2.strftime('%Y%m%d')
        mm         = int(date2.strftime('%m'))
        dd         = int(date2.strftime('%d'))

        #--- Sun rise -----
        today = Sun(tokyo)
        today.sun_rise(tokyo)
        sun_rise = today.sun_rise

        #--- Sun set -----
        today = Sun(tokyo)
        today.sun_set(tokyo)
        sun_set = today.sun_set

        rise       = rise_dic.get(date_str)

        if (rise is None):
            rise_str     = " --- " 
        else:
            rise_str = rise.hhmm

        set             = set_dic.get(date_str)

        if (set is None):
            set_str     = " --- "
        else:
            set_str     = set.hhmm

        ecl             = ecl_dic.get(date_str)

        if (ecl is None):
            ecl_str     = " ECL none! "
        else:
            ecl_tname   = ecl.tname
            moon_age    = ecl.moonage

        #print(' %2d | %s | %s  %4.1f | %s | %s | %s | %s ' % (dd,weekday,ecl_tname,moon_age,rise_str,set_str,sun_rise,sun_set))

        print(' %2d | %s | %s - %s | %4.1f %s | %s - %s '    %(dd,weekday,sun_rise,sun_set,moon_age,ecl_tname,rise_str,set_str))
