#
# LIST 5-6 MOON NO ICHI <p.173>
#
# shisa.py  
#
# INPUT 
# mjd
# moon_position[ra0,dc0,dl0]
# observe_position[la,lg,ht]
#
# shisa[ra,dc,dl]=Shisa(mjd,moon_position,observe_position)

from math import *
from astro import *

def Shisa(mjd,moon_position,observe_position):

	la=observe_position[0]
	lg=observe_position[1]
	ht=observe_position[2]

        ra=moon_position[0]
        dc=moon_position[1]
        dl=moon_position[2]
        
        if (ra<0):
            ra += PI2

	r0=ChishinKyori(la)
        fi=ChishinIdo(la,ht)
	
        s1=KouseiJiDate(mjd,lg)

        x0 =  r0*cos(fi)*cos(s1)        #<5.4.1>
        y0 =  r0*cos(fi)*sin(s1)
        z0 =  r0*sin(fi)

        xx =  dl*cos(dc)*cos(ra)
        yy =  dl*cos(dc)*sin(ra)
        zz =  dl*sin(dc)

        X = xx - x0
        Y = yy - y0
        Z = zz - z0

        dl2 = sqrt(X*X+Y*Y+Z*Z)
        
        ra2 = Shogen(Y,X)
        dc2 = atan(Z/(Y/sin(ra2)))

	shisa=[ra2,dc2,dl2]

	return shisa

