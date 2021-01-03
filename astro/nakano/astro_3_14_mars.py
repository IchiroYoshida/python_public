from __future__ import print_function
"""
# 3-12,3-13 Sun and Planets Set and Rise <p.80>

LIST 2-1 MJD,JULIAN
LIST 2-2 JDATE
LIST 2-7 KOUSEI-JI (DATE)
LIST 2-9 SAISA
LIST 2-10 SYOGEN
LIST 2-12 MEAN ELEMENTS
LIST 2-14 KEPLER
LIST 3-6 EPH CONST
"""
planet_orbits=[[0 for i in range(8)] for j in range(9)]
planet_radc=[0.0 for i in range(3)]

from math import *
from astro import *

from date import MjdToDate
from mjd import ModifiedJulianDay
from mean_elements import MeanElements
from saisa import Saisa
from planet_radc import PlanetRADC

from appear import *


###########Main

#TOKYO

LG=139.745
LA= 35.654
OB="TOKYO"

#1981/1/1 6:30:00 JST

YEAR= 1981
MONTH=   1
DAY=     1


#PLANET MARS 
PLANET= 3

mjd=ModifiedJulianDay(YEAR,MONTH,DAY)

print("MJD",mjd)

for day in range(0,365,10):

	today = mjd+day

	planet_orbits=MeanElements(today)
	rd=planet_orbits[PLANET][7]

	planet_radc=PlanetRADC(today,PLANET)

	ra=planet_radc[0]
	dc=planet_radc[1]
	ds=planet_radc[2]

	#print(ra,dc,ds)
 
	saisa=Saisa(ra,dc,0,0,YEAR,MONTH,DAY)


	ra=saisa[0]
	dc=saisa[1]

	#print(ra,dc)

	appear=Appear(today,LG,LA,ra,dc,rd,ds)

	ta1  =appear[0]
	td1  =appear[1]
	houi =appear[2]*RAD

	date=MjdToDate(today)
	yy=date[0]
	mm=date[1]
	dd=date[2]

	print ('%4d %2d %2d %8.5f %8.5f houi=%8.5f' % (yy,mm,dd,ta1,td1,houi))



