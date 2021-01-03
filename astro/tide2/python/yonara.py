"""
    ヨナラ水道　潮流表（主要４分潮）
    2019/07/14
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""

import sys
import math
import ephem
import datetime
import func.tide_func as tf
import numpy as np
import func.TD2read as td

class CurrentTable(object):
    def __init__(self, observer):
        observer = tf.Port()
        self.lat = observer.lat
        self.lng = observer.lng
        self.level = observer.level
        self.pl = observer.pl
        self.hr = observer.hr

    def show(year, month, observer):
        days = tf.month_days(year, month)

        hrs=''

        for hr in range(0,24):
            hrs +=str('%2d ' % hr)
        print('             :%s' % hrs)

        for day in range(1, days+1):

            moon=ephem.Moon()
            pt_eph = ephem.Observer()
            pt_eph.lon = str(observer.lng)
            pt_eph.lat = str(observer.lat)
            pt_eph.elevation = 0.0
            
            observer.date = str(year)+str('/%02d' % month)+str('/%02d' % day)
            pt_eph.date = str(observer.date+' 9:00')

            date_prn = str(observer.date)
            weekday  = tf.get_weekday(observer.date)

            today_moon = tf.Moon(pt_eph)
            today_moon.noon(pt_eph)
            moon_prn = today_moon.tname+str(' %4.1f' % today_moon.moonage)

            today = tf.Tide(observer)
            today.wav(observer)

            current = today.t4

            cur  = (current[0:72:3]+25)/25

            prn=''

            for c in cur:
                prn += str('%+2d ' % round(c))

            print('%2d %s %s %s' % (day, weekday, moon_prn, prn))


"""
Main
"""

CurrentTable(td)

for month in range(5, 7):
    CurrentTable.show(2018, month, td)

