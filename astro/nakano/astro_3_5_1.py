from __future__ import print_function
"""
# 3-5,6 Wakusei no Ichi keisan <p.73>

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
from ds_planet import DsPlanet

###########

mjd=ModifiedJulianDay(-6,12,25)
jst=JapanStandardTime(22,0,0)
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

        ds= DsPlanet(planet_position,planet)

	ra= planet_angle[planet][0]
	dc= planet_angle[planet][1]

        if (ra<0):
            ra+=PI2

        hour=RadToHr(ra)

        hh=hour[0]
        mm=hour[1]
        ss=hour[2]

        mm+=ss/60.0

        dec=dc*RAD

	print ('%1d %8s %3d %6.2f %6.2f %8.5f' % (planet,name,hh,mm,dec,ds))
