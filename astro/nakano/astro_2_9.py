"""
# 2-8 Rishin Kinten Rikaku <p.42>

"""
from math import *
from astro import PI,PI2,RAD
from kepler import Kepler

ec=0.9

A=100
B=A*sqrt(1-ec*ec)


for m in range (0,370,10):
	mo=m/RAD
	kepler=Kepler(ec,mo)

	x=A*kepler[2]
	y=B*kepler[0]

	print('%3d %6.3f %6.3f' % (m,x,y))


