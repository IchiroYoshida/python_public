# -*- coding:utf-8 -*-

"""
月の出、南中、入りの時刻計算  福岡(JST:UTC+9hr)
"""
import math
import ephem
import datetime
import calend_func
from moon_func import *
from moon_class import *

moon = ephem.Moon()
tokyo = ephem.Observer()

tokyo.name = 'Tokyo'
tokyo.lon, tokyo.lat = '139.7414', '35.6581'
tokyo.elevation = 0.0

year = 2018

#date0 = tokyo.date

for month in range(1, 2):
    rise_dic    = {}
    set_dic     = {}
    ecl_dic     = {}

    days = calend_func.month_days(year, month)

    #print(year,month)

    for d in range(0, days):
        day = d+1

        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        tokyo.date = str(date0+' 9:00') #UT+9hr=JST
        date_tokyo = tokyo.date

        #print(tokyo.date)

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
   
    print('　日付    潮   月齢　  月の出　    　月の入')
    print('-------------------------------------------')

    time_str = "%H:%M:%S"

    for d in range(0, days):
        day = d+1
        date0  = str(year)+str('/%02d' % month)+str('/%02d' % day)
        tokyo.date = str(date0+' 9:00')
        date1  = repr(ephem.localtime(tokyo.date))
        date2  = eval(date1)

        date_str   = date2.strftime('%Y%m%d')
        mm         = int(date2.strftime('%m'))
        dd         = int(date2.strftime('%d'))
        #date_str = date2

        print(date_str)

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

        #ecl_tname = ecl.tname
        #moon_age = ecl.moonage

        print(' %2d %2d | %s  %4.1f | %s | %s |' % (mm,dd,ecl_tname,moon_age,rise_str,set_str))

