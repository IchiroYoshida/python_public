"""
	Tokyo skytree 
"""
from numpy import sin,cos,tan,pi
import math
import ephem

xx,yy = [],[]
ll =[]

sky = ephem.Observer()
sky.lon, sky.lat = '139.810700','35.710039'

RAD=180./math.pi

Earth=6378137.0   # (m)
H=450.0           # (m)

sky.date='2016/2/04 0:00' #JST 9:00 AM
sun=ephem.Sun()

lon=float(sky.lon)
lat=float(sky.lat)

def Rambda(delta_x):
	return lon+delta_x/Earth/cos(lat)

def Phai(delta_y):
	return lat+delta_y/Earth

for ti in range(8):
	sun.compute(sky)
	th=float(sun.az)
	l=H /tan(float(sun.alt))
	ll.append(l)
	xx.append(-l*sin(th))
	yy.append(-l*cos(th))
	sky.date += ephem.hour

print ("#Tokyo Sky Tree %.6f, %.6f" %(lat/RAD,lon/RAD))
print ("#Sunset %s" %(sky.next_setting(ephem.Sun())))

for ti in range(8):
	xr=Rambda(xx[ti])
	yr=Phai(yy[ti])

	print ("%.6f, %.6f" % (yr/RAD,xr/RAD))

