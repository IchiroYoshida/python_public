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

from appear2 import *


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

#mjd -= 1

for day in range(0,365,10):

	today = mjd+day
        today0 = today

	planet_orbits=MeanElements(today)
	rd=planet_orbits[PLANET][7]

        while True:

	    planet_radc=PlanetRADC(today,PLANET)

    	    ra=planet_radc[0]
	    dc=planet_radc[1]
	    ds=planet_radc[2]

	    saisa=Saisa(ra,dc,0,0,YEAR,MONTH,DAY)
    	    ra=saisa[0]
	    dc=saisa[1]

	    appear_rise=AppearRise(today,LG,LA,ra,dc,rd,ds)

    	    tt  =appear_rise[0]

            if (tt < 2e-3):
                break
            else:
                today += tt/24.0

	time1 = today-today0

#        today = today0
        
        while True:
		planet_radc=PlanetRADC(today,PLANET)

		ra=planet_radc[0]
		dc=planet_radc[1]
		ds=planet_radc[2]

		saisa=Saisa(ra,dc,0,0,YEAR,MONTH,DAY)
		ra=saisa[0]
		dc=saisa[1]

		appear_sets=AppearSets(today,LG,LA,ra,dc,rd,ds)

		tt =appear_sets[0]

#                print ('today = %8.4f tt = %8.4f' % (today,tt))

                if (tt < 2e-3):
                    break
                else:
                    today += (tt/24.0)

	houi=appear_rise[1]*RAD

	date=MjdToDate(today0)
	yy=date[0]
	mm=date[1]
	dd=date[2]

	time2=today-today0

	time1 *= 24.0
	time1 -= 15.0

	time2 *= 24.0
	time2 -= 15.0

	h1=int(time1)
	m1=(time1-int(time1))*60.0

	h2=int(time2)
	m2=(time2-int(time2))*60.0

	print ('%4d %2d %2d %3d %5.2f  %3d %5.2f  %6.2f ' % (yy,mm,dd,h1,m1,h2,m2,houi))


