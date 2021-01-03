"""
# 2-2 Nengetsupi sanshutsu  

# LIST 2-1 MJD,JULIAN
# LIST 2-2 JDATE
 
"""
import math

from astro import JapanStandardTime,UniversalTime

#import mjd
from mjd import ModifiedJulianDay
from date import MjdToDate

# 1982 / 1 /31 9:00 JST -> MJD

mjd=ModifiedJulianDay(1982,1,31)

print mjd

jst=JapanStandardTime(9,0,0)
ut=UniversalTime(jst)

mjd += ut

print mjd

date=MjdToDate(mjd)

print date[0],date[1],date[2]

mjd2 =mjd-10000

date=MjdToDate(mjd2)

print date[0],date[1],date[2]

