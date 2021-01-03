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
#from saisa import Saisa
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


#PLANET SUN
PLANET= 2

mjd=ModifiedJulianDay(YEAR,MONTH,DAY)

print("MJD",mjd)

planet_orbits=MeanElements(mjd)
rd=planet_orbits[PLANET][7]

planet_radc=PlanetRADC(mjd,PLANET)

ra=planet_radc[0]
dc=planet_radc[1]
ds=planet_radc[2]

rah = ra*12.0/PI
dc1 = dc*RAD

print(rah,dc1,ds)
 
#saisa=Saisa(ra,dc,0,0,YEAR,MONTH,DAY)

#	ra=saisa[0]
#	dc=saisa[1]

#print(ra,dc)

appear_rise=AppearRise(mjd,LG,LA,ra,dc,RR,rd,ds)

ta1  =appear_rise[0]
rise=appear_rise[1]
rise *= RAD

date=MjdToDate(mjd)
yy=date[0]
mm=date[1]
dd=date[2]

print ('%4d %2d %2d %8.5f houi=%8.5f' % (yy,mm,dd,ta1,rise))

