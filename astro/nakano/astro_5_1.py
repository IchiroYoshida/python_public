#from __future__ import print_function
"""
# 5_1,2 Tsuki no Ichi keisan <p.169>

LIST 2-1 MJD,JULIAN
LIST 2-2 JDATE

"""

from math import *
from astro import *

from mjd import ModifiedJulianDay
from date import MjdToDate

from moon import *

###########

#1981/9/1 21:00:00 JST

YEAR= 1981
MONTH=   9
DAY=     1

HH=21
MM=00
SS= 0


mjd=ModifiedJulianDay(YEAR,MONTH,DAY)
jst=JapanStandardTime(HH,MM,SS)

ut=UniversalTime(jst)

mjd += ut
print("MJD",mjd)

print " Date(JST)    R.A.  (Date)    Decl.     Distance"

for day in range(32):
   
    date=mjd+day

    moon_position=MoonPosition(date)
    ra=moon_position[0]
    dc=moon_position[1]
    dl=moon_position[2]

    hour = RadToHr(ra)
    hh = hour[0]
    ms = hour[1]
    ss = hour[2]
    
    ms += ss/60.0
 
    dc *= RAD

    today=MjdToDate(date)

    yy =today[0]
    mm =today[1]
    dd =today[2]

    d1 = int(dc)
    d2 = abs(dc-d1)*60.0

    if (dc<0):
	sg = '-'
    else:
	sg = '+'

    print ('%4d %2d %2d |   %2d %6.2f   %s %4d %5.1f    %5d' % (yy,mm,dd,hh,ms,sg,d1,d2,dl))
