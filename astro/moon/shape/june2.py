# -*- coding:utf-8 -*-

"""
一月の月の姿
"""
import math
import datetime
import ephem

import numpy as np
import matplotlib.pyplot as plt

year = 2018
month = 6

moon = ephem.Moon()

location = ephem.Observer()

#location.name = '東京'
#location.lon, location.lat = '139.7414', '35.6581'

location.name = '福岡'
location.lon, location.lat = '130.391', '33.593'


days = 30

mul = 5

fig = plt.figure()
ax = plt.axes()

for day in range(1, days+1):
    date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
    location.date = str(date0)
    location.date += 12. * ephem.hour #UT+9hr =JST 21:00

    
    line_x = []
    line_y = []

    moon.compute(location)

    moon_nx = moon.ra
    moon_ny = moon.dec + moon.radius * mul
    point=ephem.FixedBody()
    point._ra  = ephem.hours(moon_nx)
    point._dec = ephem.degrees(moon_ny)
    point.compute(location)
    line_x.append(point.alt)
    line_y.append(point.az)

    moon_sx = moon.ra
    moon_sy = moon.dec - moon.radius * mul
    point=ephem.FixedBody()
    point._ra  = ephem.hours(moon_sx)
    point._dec = ephem.degrees(moon_sy)
    point.compute(location)
    line_x.append(point.alt)
    line_y.append(point.az)

    ax.plot(line_x,line_y,color='r')
plt.show()

