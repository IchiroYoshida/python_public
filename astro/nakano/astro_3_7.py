from __future__ import print_function
"""
# 3-5,6 Wakusei no Ichi keisan <p.73>
# 3-7   Saisa hosei

LIST 2-1 MJD,JULIAN
LIST 2-10 SYOGEN
LIST 2-12 MEAN ELEMENTS
LIST 2-14 KEPLER
"""
planet_orbits=[[0 for i in range(8)] for j in range(9)]
planet_position=[[0.0 for i in range(3)] for j in range(9)]
planet_angle=[[0.0 for i in range(2)]for j in range(9)]

from math import *
from astro import *

from mjd import ModifiedJulianDay
from mean_elements import MeanElements
from planet_position import PlanetPosition
from planet_angle import PlanetAngle
from saisa import Saisa

def ty_saisa(yy,mm,dd):
    ty= yy+(mm-1)/12.0+dd/365.0
    return ty

###########

mjd=ModifiedJulianDay(2000,1,1)

ty=ty_saisa(2000,1,1)


jst=JapanStandardTime(21,30,0)
ut=UniversalTime(jst)

mjd += ut
print("MJD",mjd)

planet_orbits=MeanElements(mjd)
planet_position=PlanetPosition(planet_orbits)

"""
print ("step1")
for planet in range(9):
	print("%d" % planet,end="")
	for n in range(3):
		p1=planet_position[planet][n]
		print (" %8.4f" % p1,end="")
	print(" ")
"""

#*********************
#(3.4.3):Nisshin zahyou wo Taiyouno Chisinn zahyouni henkan
for n in range(3):
    planet_position[2][n]= -planet_position[2][n]

#Wakuseino nissinsekidouzahyou wo chisinsekidouzahyouni henkan
for planet in range(9):
	if (planet==2):
	    pass
	else:
	    for n in range(3):
		planet_position[planet][n]+=planet_position[2][n]

#*****************************
"""
print ("step2")
for planet in range(9):
	print("%d" % planet,end="")
	for n in range(3):
		p1=planet_position[planet][n]
		print (" %8.4f" % p1,end="")
	print(" ")
"""

planet_angle=PlanetAngle(planet_position)

for planet in range(9):
	
	name =planet_orbits[planet][0]

	if (planet==2):
		name ="SUN"

	x1= planet_position[planet][0]
	x2= planet_position[planet][1]
	x3= planet_position[planet][2]

	ds=sqrt(x1*x1+x2*x2+x3*x3)

	#radian -->> hh,mm,ss angle -->> deg.

	ra= planet_angle[planet][0]
	dc= planet_angle[planet][1]

        saisa=Saisa(ra,dc,0,0,ty)
        ra=saisa[0]
        dc=saisa[1]

	#print("ra ,dc, ds: %d %8.4f %8.4f %8.4f" % (planet,ra,dc,ds))

	deg=ra*RAD
	dec=dc*RAD

        if (deg<0):
            deg+=360.0

#	print("deg dec  %d %-8.5f %-8.5f ds: %-8.5f" % (planet,deg,dec,ds))

        r1=deg/15.0
        d1=dec

	rhh=int(r1)
	rmm=60*(r1-rhh)
	
	dhh=int(d1)
	dmm=60*(d1-dhh)

	print ('%1d %8s %+03d %8.5f %+03d %8.5f %8.5f' % (planet,name,rhh,rmm,dhh,dmm,ds))
