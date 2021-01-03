"""
# saisa2.py
#
# LIST 2-9 <p.38>
# 6000- REM *** SAISA ***
 
  INPUT     | R1 = RA
            | D1 = DC
            | TY = FINAL EPOCH
            | EP = INITIAL EPOCH
            |    = UNIT OF YEAR
            | P1 = RA PROPER MOTION
            | P2 = DC PROPER MOTION
            |    = UNIT OF 100 YEARS
            |    = UNIT OF ARC SEC.
 OUTPUT     | RA = FINAL R.A.
            | DC = FINAL DECL.

saisa[ra,dc]=Saisa(r1,d1,p1,p2,ty)

"""
from math import *
from astro import *

def Saisa2(r1,d1,p1,p2,mjd):

	ty= (mjd-33282)/365.0

#        ty= yy+(mm-1)/12.0+dd/365.0

	ep=1950

	t0=(ep-1900)/100
	t1=(ty-ep)/100
	t2=t1*t1
	t3=t2*t1

	x1=(2304.25+1.396*t0)*t1+.302*t2+.018*t3
	x2=x1+.791*t2
	x3=(2004.682-.853*t0)*t1-.426*t2-.042*t3

	p1=p1/(RAD*3600)
	p2=p2/(RAD*3600)

	x1=x1/(RAD*3600)
	x2=x2/(RAD*3600)
	x3=x3/(RAD*3600)

	r2=r1+p1*t1
	d2=d1+p2*t1

	ss=cos(d2)*sin(r2+x1)
	cc=cos(x3)*cos(d2)*cos(r2+x1)-sin(x3)*sin(d2)

	tt=atan2(ss,cc)

	r3=tt

	cc=ss/sin(r3)
	ss=cos(x3)*sin(d2)+sin(x3)*cos(d2)*cos(r2+x1)

	dc=atan2(ss,cc)

	ra=r3+x2

        if (ra<0):
            ra += PI2
            
	saisa=[ra,dc]

	return saisa

