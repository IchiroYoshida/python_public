"""
    Fukuoka tower sunset 2018-8-23
"""

import math
import ephem
from datetime import datetime
from googlejav import PrnJavaScript

Earth_R =  6378137.
H       =  234.

sky = ephem.Observer()
sky.lon, sky.lat = '130.351472','33.593312'
sky.horizon = '-0:34'
sky.date = '2019/02/26'

xx, yy = [], []
ll = []
lon, lat = [], []

sun = ephem.Sun()

lon_center=math.degrees(float(sky.lon))
lat_center=math.degrees(float(sky.lat))

print(lon_center,lat_center)

lon.append(lon_center)
lat.append(lat_center)

def Rambda(delta_x):
    cos = math.cos(float(sky.lat))
    ram = lon_center + math.degrees(delta_x/Earth_R/cos)
    return(ram)

def Phai(delta_y):
    pha = lat_center + math.degrees(delta_y/Earth_R)
    return(pha)

sun.compute(sky)

sunset = sky.next_setting(sun)

sky.date = sunset - ephem.minute*60
date0 = sky.date

for ti in range(0, 60, 1):
    sky.date = date0 + ti * ephem.minute
    sun.compute(sky)

    if (math.degrees(sun.alt)>.5):
        th = float(sun.az) + sun.radius
        l  = H /math.tan(float(sun.alt))

        ll.append(l)
        xx.append(-l*math.sin(th))
        yy.append(-l*math.cos(th))

        date1 = sky.date + 9*ephem.hour #UTC-> JST
        date1 = ephem.Date(date1).datetime()

        Az  = math.degrees(sun.az)
        Alt = math.degrees(sun.alt)
        time = date1.strftime("%m/%d-%H:%M:%S")

        print('Time = %s | Az =%6.3f  Alt =%6.3f' %(time , Az, Alt))

for i in range(len(xx)):
    lon.append(Rambda(xx[i]))
    lat.append(Phai(yy[i]))

PrnJavaScript('towerv3.html',lat,lon)

