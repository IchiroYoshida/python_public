# -*- coding:utf-8 -*-

"""
一月の月の姿
"""
import math
import datetime
import ephem

year = 2018
month = 6

moon = ephem.Moon()

location = ephem.Observer()

#location.name = '東京'
#location.lon, location.lat = '139.7414', '35.6581'

location.name = '福岡'
location.lon, location.lat = '130.391', '33.593'

print(year, month)

days = 30

for day in range(1, days+1):
    date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
    location.date = str(date0)
    location.date += 12. * ephem.hour #UT+9hr =JST 21:00

    moon.compute(location)

    moon_nx = moon.ra
    moon_ny = moon.dec + moon.radius

    moon_sx = moon.ra
    moon_sy = moon.dec - moon.radius

    print(' %2d | (%8.6lf,%8.6lf) -- (%8.6lf,%8.6lf)' % (day,
        moon_nx, moon_ny, moon_sx, moon_sy))
