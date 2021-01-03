from __future__ import print_function
"""
#  5-8 GETSU-REI

LIST 2-1 MJD,JULIAN
LIST 2-2 JDATE
LIST 2-7 KOUSEI-JI (DATE)
LIST 3-15 APPEAR
LIST 5-2 ARGUMENT OF TRIGONOMETRIC
LIST 5-3 MOON-THETA, RHO, PHI
LIST 5-4 POSITIONS

"""
planet_orbits=[[0 for i in range(8)] for j in range(9)]
planet_radc=[0.0 for i in range(3)]

from math import *
from astro import *

from date import MjdToDate
from mjd import ModifiedJulianDay
from moon import *
from appear2 import *


###########Main

#TOKYO

LG=139.745
LA= 35.654
OB="TOKYO"

#1981/9/1 

YEAR= 1981
MONTH=   9
DAY=     1

#rd=1738.68   #Moon rd (Km)
rd=0

mjd=ModifiedJulianDay(YEAR,MONTH,DAY)

print("MJD",mjd)

mjd -= 1


for day in range(0,32,1):

	today0 = mjd+day
        today  = today0

        while True:

            moon_position=MoonPosition(today)

	    ra=moon_position[0]
	    dc=moon_position[1]
	    ds=moon_position[2]
            ds /= 149597870       # (Km --> A.U.)
            
    	    appear_rise=AppearRise(today,LG,LA,ra,dc,rd,ds)

	    tt  =appear_rise[0]

	    if (tt < 2e-3):
                break
            else:
                today += tt/PI2
               
        time1 = today-today0
        today  = today0
        
        while True:

                moon_position=MoonPosition(today)

		ra=moon_position[0]
		dc=moon_position[1]
		ds=moon_position[2]

		appear_sets=AppearSets(today,LG,LA,ra,dc,rd,ds)

		tt =appear_sets[0]
                
                if (tt < 2e-3):
                        break
                else:
                        today += tt/PI2

	time2 =today-today0

	houi=appear_rise[1]*RAD

	date=MjdToDate(today0)
	yy=date[0]
	mm=date[1]
	dd=date[2]

        ge=Getsurei(today0)
        
	time1 *= 24.0
	time1 +=  9.0

	time2 *= 24.0
	time2 +=  9.0

#        print('time1 = %8.4f  time2 = %8.4f' % (time1,time2))
    
        if (time1 < 35.0):
	    h1=int(time1)
	    m1=(time1-int(time1))*60.0
        
            appear=str('%2d' % h1)+str(' %5.2f' % m1)

        else:
            appear="--------"

        if (time2 < 35.0):
	    h2=int(time2)
	    m2=(time2-int(time2))*60.0
            
            sets=str('%2d' % h2)+str('  %5.2f' % m2)

        else:
            sets="---------"

        print('%4d %2d %2d %s %s  | %3.1f'% (yy,mm,dd,appear,sets,ge))

#        print ('%4d %2d %2d time1 = %8.4f  time2 = %8.4f' % (yy,mm,dd,time1,time2))
        
#	print ('%4d %2d %2d %3d %5.2f  %3d %5.2f  %6.2f ' % (yy,mm,dd,h1,m1,h2,m2,houi))


