"""
# 2-5 Nanchuu Tentai Sekkei

# LIST 2-1 MJD,JULIAN
# LIST 2-7 KOUSEI-JI(1950) 
"""
from astro import *
from mjd import ModifiedJulianDay

long = 139.745/RAD
#Name = "Tokyo"

#1981/1/1 - 0000 JST

r1 =  ModifiedJulianDay(1981,1,1)

r1 -=0.375

s1=KouseiJiDate(r1,long)
hour=RadToHr(s1)

print "(DATE)",hour[0],hour[1],hour[2]

s1=KouseiJi1950(r1,long)
hour=RadToHr(s1)

print "(1950)",hour[0],hour[1],hour[2]
