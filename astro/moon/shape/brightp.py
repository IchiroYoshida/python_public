"""
position angle of the Moon's bright limb.
2018-07-28

Shape of the moon
"""
import numpy as np
import ephem
import math
import matplotlib.pyplot as plt
from PIL import Image

AU = 1.496e8

YYMM = '2018/06'

location = ephem.Observer()

location.name = 'Tokyo'
location.lon, location.lat = '139.74136', '35.658099'
#location.date = '2018/06/25 12:00:00' #21:00 JST


for day in range(1, 31):
    date0 = str(YYMM) + str('/%02d' % day)
    location.date = str(date0)

    sun  = ephem.Sun(location)
    moon = ephem.Moon(location)
    moon_earth = moon.earth_distance * AU

    alpha = moon.elong 

    ss = math.sin(sun.g_dec)*math.cos(sun.g_dec) \
         - math.cos(sun.g_dec)*math.sin(moon.g_dec)*math.cos(sun.g_ra - moon.g_ra)

    cc = math.cos(sun.g_dec)*math.sin(sun.g_ra - moon.g_ra)

    p = math.atan2(cc, ss)
    p2 = 180 + math.degrees(p)

    print(date0,p2)


