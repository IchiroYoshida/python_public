"""
	Sun
"""
from numpy import sin,cos,tan
import ephem

xx,yy = [],[]

kaisei = ephem.Observer()
kaisei.lon, kaisei.lat = '130.5954','33.76314'

kaisei.date='2015/11/29 0:00' #JST 9:00 AM
sun=ephem.Sun()

for ti in range(8):
	sun.compute(kaisei)
	th=float(sun.az)
	l=1. /tan(float(sun.alt))
	xx.append(l*sin(th))
	yy.append(l*cos(th))
	kaisei.date += ephem.hour

print xx,yy


