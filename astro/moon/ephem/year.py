# -*- coding:utf-8 -*-

"""
月の出、南中、入りの時刻計算  東京(JST:UTC+9hr)
"""
import math
import ephem
import datetime
import moon_days 
from moon_func import *
from moon_class import *

year = 2018

location_eph = ephem.Observer()
location_eph.lon, location_eph.lat = '139.7414', '35.681'
location_eph.elevation = 0.0
#location.date = '2016/7/1 9:00' #UT 0:00 JST= UT +9hr
location_eph.name = 'Tokyo'
location_date = ''

print(location_eph.name,year)

for month in range (1,2):
    days = moon_days.month_days(year,month)

    print (year, month)

    rise_dic    = {}
    set_dic     = {}
    ecl_dic     = {}

    for d in range(0,days):

        moon = ephem.Moon()
        location_eph = ephem.Observer()

        day = d + 1

        location_date = str(year)+str('/%02d' % month)+str('/%02d' % day)
        location_eph.date = str(location_date + ' 9:00')

        date_prn = str(location_date)
        weekday = get_weekday(location_date)

        today_moon = Moon(location_eph)
        today_moon.noon(location_eph)

        moon_prn = today_moon.tname+str(' %4.1f' % today_moon.moonage)

        today     = Moon(location_eph)
        rise_dic.update({today.index:today})

        today     = Moon(location_eph)
        today.set(location_eph)
        set_dic.update({today.index:today})
   
        today     = Moon(location_eph)
        today.noon(location_eph)
        ecl_dic.update({today.index:today})
  
    print(rise_dic)

    print('　日付    潮   月齢　  月の出　    　月の入')
    print('-------------------------------------------')

    time_str = "%H:%M:%S"

    for d in range(0,days):
       date1  = repr(ephem.localtime(location_eph.date))
       date2  = eval(date1) + datetime.timedelta(days=d)
       date_str   = date2.strftime('%Y%m%d')
       mm         = int(date2.strftime('%m'))
       dd         = int(date2.strftime('%d'))

       print(date1,date2,date_str,mm,dd)

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

       print(' %2d %2d | %s  %4.1f | %s | %s |' % (mm,dd,ecl_tname,moon_age,rise_str,set_str))

