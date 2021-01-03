"""
	Sun shadow plot 
"""
from numpy import sin,cos,tan
import ephem

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xx,yy = [],[]

kaisei = ephem.Observer()
kaisei.lon, kaisei.lat = '130.5954','33.76314'

kaisei.date='2015/11/29 0:00' #JST 9:00 AM
sun=ephem.Sun()
T=7

for ti in range(T):
	sun.compute(kaisei)
	th=float(sun.az)
	l=1. /tan(float(sun.alt))
	xx.append(-l*sin(th))
	yy.append( l*cos(th))
	kaisei.date += ephem.hour

#Plot figure

fig=plt.figure()
ax = fig.add_subplot(111,autoscale_on=False, xlim=(-5,5),ylim=(-5,5))
ax.grid()

plt.plot(xx,yy,"g-")

line_x,line_y=[],[]

for ti in range(T):
	line_x.append(0.0)
	line_y.append(0.0)

	line_x.append(xx[ti])
	line_y.append(yy[ti])

	plt.plot(line_x,line_y,"ro-")

plt.show()
