"""
Julian day

"""
import sys
import math
import ephem
import datetime
import calend_func 
from  moon_calc import *

DJD = 2415020.5

year = 2018

locate_eph = ephem.Observer()

locate_eph.name = 'Tokyo'
locate_eph.lat = 35.40
locate_eph.lon = 139.46
locate_eph.elevation = 0.0

print(year)

for month in range(1, 2):

    rise_dic = {}
    set_dic = {}

    days = calend_func.month_days(year, month)

    print(year, month)

    for d in range(0, days):

        day = d+1

        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        locate_eph.date = str(date0+' 9:00')    # UT+9hr=JST

        print(locate_eph.date)

        today_moon = Moon(locate_eph)
        today_moon.rise(locate_eph)
        rise_dic.update({today_moon.index:today_moon})

        today_moon = Moon(locate_eph)
        today_moon.set(locate_eph)
        set_dic.update({today_moon.index:today_moon})

        today_moon = Moon(locate_eph)
        today_moon.noon(locate_eph)
        ecl_dic.update({today_moon.index:today_moon})

    print('------------------------------------------------------')
    print('  日付　曜日　潮　月齢　月出　月入　日出　日入　')

    time_str = "%H:%M:%S"

    for d in range(0, days):

        day = d+1

        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        locate_eph.date = str(date0+' 9:00')

        jul = float(('%.6f' % ephem.Date(date0))) + DJD
    
        print(year, month, day)

        weekday = get_weekday(date0)

        print(date0,jul,weekday)

        date_str = date0.strftime('%Y%m%d')

        print(date_str)

        # rise = rise_dic.get(date_str)

        # print(rise)

