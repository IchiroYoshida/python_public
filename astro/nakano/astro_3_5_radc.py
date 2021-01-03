from __future__ import print_function
"""
# 3-5,6 Wakusei no Ichi keisan <p.73>

LIST 2-1 MJD,JULIAN
LIST 2-10 SYOGEN
LIST 2-12 MEAN ELEMENTS
LIST 2-14 KEPLER
"""
planet_radc=[0.0 for i in range(3)]

from math import *
from astro import *

from mjd import ModifiedJulianDay
from planet_radc import PlanetRADC

###########

#2000/1/1 21:30:00 JST

YEAR= 2000
MONTH=   1
DAY=     1

HH=21
MM=30
SS= 0


mjd=ModifiedJulianDay(YEAR,MONTH,DAY)
jst=JapanStandardTime(HH,MM,SS)

ut=UniversalTime(jst)

mjd += ut
print("MJD",mjd)

for planet in range(9):

    planet_radc=PlanetRADC(mjd,planet)

    ra=planet_radc[0]
    dc=planet_radc[1]
    ds=planet_radc[2]
   
    hour =RadToHr(ra)

    hh = hour[0]
    mm = hour[1]
    ss = hour[2]
    mm += ss/60.0

    dc *= RAD
    
    print('%1d %3d %8.5f %8.4f %8.5f' % (planet,hh,mm,dc,ds))

