"""
	Mt.Kaya Sunset 
"""
from numpy import sin,cos,tan,pi
import math
import ephem

from myjavas import PrnJavaScript

xx,yy = [],[]
ll =[]

lon,lat=[],[]

sky = ephem.Observer()
sky.lon, sky.lat = '130.1610','33.5720'

RAD=180./math.pi

Earth=6378137.0   # (m)
H=365.           # (m)

date=['2018/6/20 0:00',
      '2018/7/20 0:00',
      '2018/8/20 0:00',
      '2018/9/20 0:00',
      '2018/10/20 0:00',
      '2018/11/20 0:00',
      '2018/12/20 0:00'] #JST 9:00 AM

sun=ephem.Sun()

lon_center=float(sky.lon)
lat_center=float(sky.lat)

lon.append(float(sky.lon)*RAD)
lat.append(float(sky.lat)*RAD)


def Rambda(delta_x):
	return (lon_center+delta_x/Earth/cos(lat_center))*RAD

def Phai(delta_y):
	return (lat_center+delta_y/Earth)*RAD

for ti in range(7):
        sky.date=date[ti]
        sun.compute(sky)
        sunset=sky.next_setting(sun)

        sky.date=sunset-ephem.minute*10.
        sun.compute(sky)

        th=float(sun.az)
        l=H /tan(float(sun.alt))
        ll.append(l)
        xx.append(-l*sin(th))
        yy.append(-l*cos(th))

        al=float(sun.alt)*RAD
        th2=th*RAD

        print ("Time = %s | th=%.2f al=%.2f" % (sky.date,th2,al))

for ti in range(len(xx)):
	lon.append(Rambda(xx[ti]))
	lat.append(Phai(yy[ti]))

PrnJavaScript("kaya.js",lat,lon)

