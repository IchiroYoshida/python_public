"""
Moon shape3
2018-06-23

Shape of the moon
"""
import numpy as np
import ephem
import math
import matplotlib.pyplot as plt
from PIL import Image

YYMM = '2018/06'

location = ephem.Observer()

location.name = 'Fukuoka'
location.lon, location.lat = '130.391', '33.593'
#location.date = '2018/06/25 12:00:00' #21:00 JST


for day in range(1, 31):
    date0 = str(YYMM) + str('/%02d' % day)
    location.date = str(date0+' 21:00:00') # JST 21:00
    location.date -= 9. * ephem.hour # JST-> UTC

    sun  = ephem.Sun(location)
    moon = ephem.Moon(location)
    alpha = moon.elong 

    sun_alt = ephem.degrees(ephem.pi - sun.alt)

    print(day,sun_alt)
