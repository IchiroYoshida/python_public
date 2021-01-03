"""
# 2-6 Kousei no Saisa keisan

# LIST 2-9 SAISA
# LIST 2-10 SYOGEN 
"""
from astro import PI,PI2,RAD
from saisa import Saisa
from math import *

yy=300
ra=200.63875
dc=-10.90083
pr=-4.4
pd=-3.3
la=50

ra = ra/RAD
dc = dc/RAD
la = la/RAD

r1=ra
d1=dc

for y in range(yy,1700,100):
	ty=y+.25

	p1=pr
	p2=pd

	saisa=Saisa(r1,d1,p1,p2,ty)

	ra=saisa[0]
	dc=saisa[1]

	cc=sin(dc)/cos(la)
	ss=sqrt(1-cc*cc)
	al=atan2(ss,cc)
	if al<0 :
		al += PI

	al=al*RAD
	ra=ra*RAD+360
	dc=dc*RAD

	print y,ra,dc,al


