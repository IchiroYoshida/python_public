"""
   Mt. Kaya  sunset 2018-8-23
"""

import math
import ephem
from myjavas import PrnJavaScript

Earth_R =  6378137.
H       =  365. 

sky = ephem.Observer()
sky.lon, sky.lat = '130.1610','33.5720'
sky.horizon = '-0:34'
sky.date = '2018/9/19'

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

        print('Time = %s | az =%s alt =%s' %(sky.date,sun.az,sun.alt))

for i in range(len(xx)):
    lon.append(Rambda(xx[i]))
    lat.append(Phai(yy[i]))

PrnJavaScript('kaya.js',lat,lon)

