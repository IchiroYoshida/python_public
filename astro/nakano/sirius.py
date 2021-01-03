#from __future__ import print_function
"""
# Star Set and Rise 

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

#from date import MjdToDate
from mjd import ModifiedJulianDay
# from mean_elements import MeanElements
#from saisa import Saisa
# from planet_radc import PlanetRADC

from appear import *


###########Main

#KYOTO

LG=135.733
LA= 35.017
OB="KYOTO"

#2000/1/1 

YEAR= 2000
MONTH=   1
DAY=     1

#STAR SIRIUS
RA_HH=    6
RA_MM= 45.1
DC= -16.7167

mjd=ModifiedJulianDay(YEAR,MONTH,DAY)

ra  =(RA_HH+RA_MM/60.0)*PI/12.0
dc  =DC/RAD

print("MJD",mjd)

print ra,dc

#saisa=Saisa(ra,dc,0,0,YEAR,MONTH,DAY)
#
#	ra=saisa[0]
#	dc=saisa[1]	

set_rise=SetRise(mjd,LG,LA,ra,dc)

rise=set_rise[0]
set =set_rise[1]
houi=set_rise[2]

houi *= RAD

print rise,set,houi

#	print ('%4d %2d %2d %2d %8.5f %8.5f %8.5f' % (yy,mm,dd,ra_hh,ra_mm,dc,ds))


