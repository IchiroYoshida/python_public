"""
# 2-1 JST <---> MJD Conversion

# LIST 2-1 MJD,JULIAN
# LIST 2-2 JDATE
 
"""
import math

from astro import JapanStandardTime,UniversalTime

#import mjd
from mjd import ModifiedJulianDay
from date import MjdToDate

# -4712 / 1 /1 21:00 JST -> MJD

mjd=ModifiedJulianDay(-4712,1,1)

print mjd

jst=JapanStandardTime(21,0,0)
ut=UniversalTime(jst)

mjd += ut

print mjd

date=MjdToDate(mjd)

print date[0],date[1],date[2]


