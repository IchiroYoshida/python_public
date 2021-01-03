from __future__ import print_function
"""
#  5-10 GESHOKU

LIST 2-1 MJD,JULIAN
LIST 2-2 JDATE
LIST 5-2 ARGUMENT OF TRIGONOMETRIC
LIST 5-3 MOON-THETA, RHO, PHI
LIST 5-4 POSITIONS

"""
from math import *
from astro import *

from date import MjdToDate
from mjd import ModifiedJulianDay
from moon import *

###########Main

#TOKYO

LG=139.745
LA= 35.654
OB="TOKYO"

#2015/4/4 

YEAR= 2015
MONTH=   4
DAY=     4

HH= 18
MM=  0
SS=  0

#rd=1738.68   #Moon rd (Km)
#rd=0

la=LA/RAD
lg=LG/RAD

mjd=ModifiedJulianDay(YEAR,MONTH,DAY)
jst=JapanStandardTime(HH,MM,SS)

ut=UniversalTime(jst)

mjd += ut

print("MJD",mjd)

#mjd -= 1

for n in range(0,20):
    
    min1 = n*30
    
    min2 = min1/1440.0

    today = mjd+min2

    moon_position=MoonPosition(today)

    moon_ra=moon_position[0]
    moon_dc=moon_position[1]
    moon_dl=moon_position[2]

    sun_position=SunPosition(today)

    sun_ra =sun_position[0]
    sun_dc =sun_position[1]
    sun_dl =sun_position[2]

    honei_ra = sun_ra+PI     # Sun Shadows <5.7.2> p.159
    honei_dc = -sun_dc

    if (honei_ra> PI2):
        honei_ra -= PI2

    xx = - (moon_ra - honei_ra)*RAD*60.0
    yy = (moon_dc - honei_dc)*RAD*60.0
    
    rr = 0.76*atan(EARTH_RD/moon_dl)*RAD*60.0     # <5.7.3> p.159
    ll = atan(MOON_RD/moon_dl)*RAD*60.0           # <5.7.4> p.159

    date=MjdToDate(today)
    yr=date[0]
    mm=date[1]
    dd=date[2]

    print('%4d %2d %2d | %3d | xx=%8.1f  yy=%8.1f rr=%5.1f ll=%5.1f'% (yr,mm,dd,min1,xx,yy,rr,ll))

