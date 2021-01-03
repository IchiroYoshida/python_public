
"""
    Mt. Fuji Pearl  2019-2-28
"""

import math
import ephem
from datetime import datetime
from googlejav import PrnJavaScript

Earth_R =  6378137.
H       =  3776.

sky = ephem.Observer()
sky.lon, sky.lat = '138.7274','35.3606'
sky.horizon = '-0:34'
sky.date = '2019/02/20 6:30:00'
sky.elevation = H
sky.date -= 9.*ephem.hour

xx, yy = [], []
ll = []
lon, lat = [], []

moon = ephem.Moon()

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

moon.compute(sky)

moonset = sky.next_setting(moon)

sky.date = moonset - ephem.minute*30
date0 = sky.date

for ti in range(0, 30, 1):
    sky.date = date0 + ti * ephem.minute
    moon.compute(sky)

    if (math.degrees(moon.alt)>2.5):
        th = float(moon.az) # + moon.radius
        l  = H /math.tan(float(moon.alt))

        ll.append(l)
        xx.append(-l*math.sin(th))
        yy.append(-l*math.cos(th))

        date1 = sky.date + 9*ephem.hour #UTC-> JST
        date1 = ephem.Date(date1).datetime()

        Az  = math.degrees(moon.az)
        Alt = math.degrees(moon.alt)
        time = date1.strftime("%m/%d-%H:%M:%S")

        print('Time = %s | Az =%6.3f  Alt =%6.3f' %(time , Az, Alt))

for i in range(len(xx)):
    lon.append(Rambda(xx[i]))
    lat.append(Phai(yy[i]))

PrnJavaScript('pearl.html',lat,lon)

