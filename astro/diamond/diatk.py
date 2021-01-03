"""
	Diamond Fuji and Tokyo skytree 
"""
from numpy import sin,cos,tan,pi
import math
import ephem

xx,yy = [],[]
ll =[]

tokyo_sky = ephem.Observer()
tokyo_sky.lon, tokyo_sky.lat = '139.810700','35.710039'

RAD=180./math.pi

Earth=6378137.0   # (m)
H=450.0           # (m)

tokyo_sky.date='2016/2/04 0:00' #JST 9:00 AM
sun=ephem.Sun()

sunset=tokyo_sky.next_setting(sun)
date0=sunset - ephem.minute*34.

lon=float(tokyo_sky.lon)
lat=float(tokyo_sky.lat)

def Rambda(delta_x):
	return lon+delta_x/Earth/cos(lat)

def Phai(delta_y):
	return lat+delta_y/Earth

for ti in range(0,20,5):
        tokyo_sky.date=date0+ephem.minute*ti
        print (" %s --" % tokyo_sky.date)
        
	sun.compute(tokyo_sky)
	th=float(sun.az)
	l=H /tan(float(sun.alt))
	ll.append(l)
	xx.append(-l*sin(th))
	yy.append(-l*cos(th))

for ti in range(4):
	xr=Rambda(xx[ti])
	yr=Phai(yy[ti])

	print ("%.6f, %.6f" % (yr*RAD,xr*RAD))

