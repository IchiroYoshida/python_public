from __future__ import print_function
"""
# LIST 6-1 COMET PREDICTION <p.201>

#LIST 3-12 PLANET NO KODO HOUI 

LIST 2-1 MJD,JULIAN
LIST 2-10 SYOGEN
LIST 2-12 MEAN ELEMENTS
LIST 2-14 KEPLER
LIST 3-6 EPH CONST
LIST 2-9 SAISA
LIST 3-13 KODO HOUI 
"""
comet_radc=[0.0 for i in range(4)]
comet=[0.0 for i in range(11)]

#planet_orbits=[[0 for i in range(8)] for j in range(9)]
#planet_position=[[0.0 for i in range(3)] for j in range(9)]

from math import *
from astro import *

from mjd import ModifiedJulianDay
from date import *
from eph_const import *
from saisa import Saisa
from kodo_houi import KodoHoui

from planet_radc import PlanetRADC
from comet import *

###########Main

#TOKYO

LG=139.745
LA= 35.654
OB="TOKYO"

#1985/7/24 

YEAR= 1985
MONTH=   7
DAY=    24

#YEAR = 1986
#MONTH=    3
#DAY  =   10

#DATA COMET HALLEY
comet[0]='Comet Halley'  # name
comet[1]= 1986           #orbit_yy
comet[2]=    2           #orbit_mm
comet[3]=    9.6613      #orbit_dd
comet[4]=    0.587096    #orbit_q  
comet[5]=    0.967267    #orbit_ec
comet[6]=  111.8534      #orbit_pe
comet[7]=   58.1531      #orbit_nd
comet[8]=  162.2378      #orbit_ic
comet[9]=    5.2         #orbit_m1
comet[10]=   0.2         #orbit_tl


mjd=ModifiedJulianDay(YEAR,MONTH,DAY)
print("MJD",mjd)

lg =LG/RAD
la =LA/RAD

for days in range(0,365,10):
    
        date = mjd + days

	date2= MjdToDate(date)
	date2_yy=date2[0]
	date2_mm=date2[1]
	date2_dd=date2[2]

	comet_radc=CometRADC(date,comet)

    	ra=comet_radc[0]
    	dc=comet_radc[1]
    	ds=comet_radc[2]
	dl=comet_radc[3]
 
        saisa=Saisa(ra,dc,0,0,date2_yy,date2_mm,date2_dd)
        ra=saisa[0]
        dc=saisa[1]

        kodo_houi=KodoHoui(date,lg,la,ra,dc)
        al=kodo_houi[0]
        hi=kodo_houi[1]

#        hour=RadToHr(ra)
#        hh=hour[0]
#        mm=hour[1]+hour[2]/60.0
        
	ra *= RAD
        dc *= RAD

        d1=int(dc)
        d2=abs(dc-d1)*60.0

        al *= RAD  
 	hi *= RAD
 
        h1=int(hi)
        h2=abs(hi-h1)*60.0

	print ('%4d %3d %3d| %6.2f %6.2f   %6.3f  %6.3f' %  (date2_yy,date2_mm,date2_dd,ra,dc,ds,dl))

# 	print ('%4d %3d %3d|%3d %6.2f %3d %4.1f %6.2f %4.1f %8.5f' % (date2_yy,date2_mm,date2_dd,mm,d1,d2,al,h1,h2,ds))
