from __future__ import print_function
"""
#  5-6 MOON NO ICHI

LIST 2-1 MJD,JULIAN
LIST 2-2 JDATE
LIST 2-7 KOUSEI-JI (DATE)
LIST 2-10 SHOGEN
LIST 4-1 CHISIN IDO
LIST 4-2 CHISIN KYORI
LIST 5-2 ARGUMENT OF TRIGONOMETRIC
LIST 5-3 MOON-THETA, RHO, PHI
LIST 5-4 POSITIONS

"""
from math import *
from astro import *

from date import MjdToDate
from mjd import ModifiedJulianDay
from moon import *

from shisa import *

observe_position=[0.0 for i in range(3)]

###########Main
#TOKYO

LG=139.745
LA= 35.654
HT=  0.0

OB="TOKYO"

#1981/9/1 

YEAR= 1981
MONTH=   9
DAY=     1

HH=21
MM=00
SS= 0

la=LA/RAD
lg=LG/RAD
ht=HT

observe_position[0]=la
observe_position[1]=lg
observe_position[2]=ht

mjd=ModifiedJulianDay(YEAR,MONTH,DAY)
jst=JapanStandardTime(HH,MM,SS)

ut=UniversalTime(jst)

mjd += ut

print("MJD",mjd)

print(' Date(JST)    R.A.  (Date)    Decl.     Distance                     ')

for day in range(0,32,1):
        #<5.2.14>
	today = mjd+day

        moon_position=MoonPosition(today)

        #<5.2.1> - <5.2.13>
        ra=moon_position[0]
        dc=moon_position[1]
        dl=moon_position[2]
        
        if (ra<0):
            ra += PI2

        shisa=Shisa(today,moon_position,observe_position)
        ra2=shisa[0]
        dc2=shisa[1]
        dl2=shisa[2]

        dc  *= RAD
        dc2 *= RAD

#        print('ra1 %8.4f ra2  %8.4f     dc %8.4f  dc2  %8.4f'% (ra,ra2,dc,dc2))
        
        date1=MjdToDate(today)
        yy =date1[0]
        mm =date1[1]
        dd =date1[2]


        hour = RadToHr(ra)
        hh1 = hour[0]
        ms1 = hour[1]
        ss1 = hour[2]
 
        ms1 += ss1/60.0

        hour = RadToHr(ra2)
        hh2 = hour[0]
        ms2 = hour[1]
        ss2 = hour[2]
 
        ms2 += ss2/60.0

        dc1h = int(dc)
        dc1m = abs(dc-dc1h)*60.0

        if (dc<0):
            sg1 = '-'
        else:
	    sg1 = '+'

        dc2h = int(dc2)
        dc2m = abs(dc2-dc2h)*60.0

        if (dc2<0):
            sg2 = '-'
        else:
	    sg2 = '+'

        print('%4d %2d %2d | %2d %5.2f  %s %3d %5.2f  %3d    %2d %6.2f   %s  %4d  %5.1f   %5d '  % (yy,mm,dd,hh1,ms1,sg1,dc1h,dc1m,dl,hh2,ms2,sg2,dc2h,dc2m,dl2))
