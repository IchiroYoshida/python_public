from __future__ import print_function
"""
#  5-12 NISYOKU

LIST 2-1 MJD,JULIAN
LIST 2-2 JDATE
LIST 2-7 KOUSEI-JI (DATE)
LIST 2-10 SHOGEN
LIST 4-1 CHISIN IDO
LIST 4-2 CHISIN KYORI
LIST 5-2 ARGUMENT OF TRIGONOMETRIC
LIST 5-3 MOON-THETA, RHO, PHI
LIST 5-4 POSITIONS
LIST 5-6 MOON NO ICHI
LIST 5-11 SUN-THETA, RHO, PHI

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

#1981/7/31 

YEAR= 1981
MONTH=   7
DAY=    31

#11:45 -
HH=11
MM=45
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

for min1 in range(0,200,5):
        #<5.2.14>
	min2 = min1/1440.0
        
        today = mjd+min2

        moon_position=MoonPosition(today)

        shisa=Shisa(today,moon_position,observe_position)

        moon_ra = shisa[0]
        moon_dc = shisa[1]
        moon_dl = shisa[2]

        sun_position=SunPosition(today)

        sun_ra =sun_position[0]
        sun_dc =sun_position[1]
        sun_dl =sun_position[2]*AU     # (AU -> km)

        xx = -(moon_ra - sun_ra)*RAD*60.0
        yy =  (moon_dc - sun_dc)*RAD*60.0
        
        rr = atan(SUN_RD/sun_dl)*RAD*60.0
        ll = atan(MOON_RD/moon_dl)*RAD*60.0

        sb = (rr+ll-sqrt(xx*xx+yy*yy))/(2*rr)

        date=MjdToDate(today)

        yr=date[0]
        mm=date[1]
        dd=date[2]

        print('%4d %2d %2d | %3d | xx=%5.1f  yy=%5.1f rr=%5.2f ll=%5.2f sb=%7.2f'% (yr,mm,dd,min1,xx,yy,rr,ll,sb))



