from __future__ import print_function
"""
# 3-11 Taiyoukei Tentai no Koudo, Houi  <p.73>

#LIST 3-12 PLANET NO KODO HOUI 

LIST 2-1 MJD,JULIAN
LIST 2-10 SYOGEN
LIST 2-12 MEAN ELEMENTS
LIST 2-14 KEPLER
LIST 3-6 EPH CONST
LIST 2-9 SAISA
LIST 3-13 KODO HOUI 
"""
planet_radc=[0.0 for i in range(3)]

#planet_orbits=[[0 for i in range(8)] for j in range(9)]
#planet_position=[[0.0 for i in range(3)] for j in range(9)]
#planet_angle=[[0.0 for i in range(2)]for j in range(9)]

from math import *
from astro import *

from mjd import ModifiedJulianDay
#from mean_elements import MeanElements
#from planet_position import PlanetPosition
#from planet_angle import PlanetAngle
from saisa import Saisa
from kodo_houi import KodoHoui
#from ds_planet import DsPlanet

from planet_radc import PlanetRADC

###########Main

#TOKYO

LG=139.745
LA= 35.654
OB="TOKYO"

#1981/1/1 6:30:00 JST

YEAR= 1981
MONTH=   1
DAY=     1

HH= 6
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
 
        saisa=Saisa(ra,dc,0,0,YEAR,MONTH,DAY)
        ra=saisa[0]
        dc=saisa[1]

        kodo_houi=KodoHoui(mjd,LG,LA,ra,dc)
        al=kodo_houi[0]
        hi=kodo_houi[1]

        hour=RadToHr(ra)
        hh=hour[0]
        mm=hour[1]+hour[2]/60.0
        
        dc *= RAD

        d1=int(dc)
        d2=abs(dc-d1)*60.0

        al *= RAD  
 	hi *= RAD
 
        h1=int(hi)
        h2=abs(hi-h1)*60.0

 	print ('%1d %3d %6.2f %3d %4.1f %6.2f %3d %4.1f %8.5f' % (planet,hh,mm,d1,d2,al,h1,h2,ds))
