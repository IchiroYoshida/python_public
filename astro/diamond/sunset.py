"""
	Tokyo skytree 
"""
from numpy import sin,cos,tan,pi
import ephem

xx,yy = [],[]
ll =[]

sky = ephem.Observer()
sky.lon, sky.lat = '139.8106','35.71004'

RAD=pi/180.

Earth=6378137.0   # (m)
H=634.0           # (m)

sky.date='2015/12/06 7:00' #JST 16:00 PM
sun=ephem.Sun()

lon=float(sky.lon)
lat=float(sky.lat)

print ("#Tokyo Sky Tree %.6f, %.6f" %(lat/RAD,lon/RAD))
print ("#Sunset %s" %(sky.next_setting(ephem.Sun())))


def Rambda(delta_x):
	return lon+delta_x/Earth/cos(lat)

def Phai(delta_y):
	return lat+delta_y/Earth

for ti in range(5):
	sun.compute(sky)
	th=float(sun.az)
	l=H /tan(float(sun.alt))
	ll.append(l)
	xx.append(-l*sin(th))
	yy.append(-l*cos(th))
	sky.date += ephem.minute*5

for ti in range(5):
	xr=Rambda(xx[ti])
	yr=Phai(yy[ti])

	print ("%.6f, %.6f" % (yr/RAD,xr/RAD))

