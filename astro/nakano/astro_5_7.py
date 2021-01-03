from __future__ import print_function
"""
#  5-7 MOON NO KOUDO HOUI (Section 5-6) <p.175>

LIST 2-1 MJD,JULIAN
LIST 2-2 JDATE
LIST 2-7 KOUSEI-JI (DATE)
LIST 2-10 SHOGEN
LIST 3-13 KODO HOUI
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
from kodo_houi import *
from moon import *

###########Main
#TOKYO

LG=139.745
LA= 35.654
HT=  0.0

OB="TOKYO"

#1981/9/1 

YEAR= 1981
MONTH=   9
DAY=    13

HH=17
MM=00
SS= 0

la=LA/RAD
lg=LG/RAD
ht=HT


mjd=ModifiedJulianDay(YEAR,MONTH,DAY)
jst=JapanStandardTime(HH,MM,SS)

#day3=(HH+MM/60.0)/24.0

ut=UniversalTime(jst)

mjd += ut

print("MJD",mjd)

print(' Date(JST)    R.A.  (Date)    Decl.     Distance                     ')

for n in range(0,12):

        min1 = n*30

        min2 = min1/1440.0

        today = mjd+min2 



        #<5.2.14>

#        moont=MoonTime(today)
        moon_position=MoonPosition(today)

        #<5.2.1> - <5.2.13>
        ra=moon_position[0]
        dc=moon_position[1]
        dl=moon_position[2]
        
        if (ra<0):
            ra += PI2

	r0=ChishinKyori(la)
        fi=ChishinIdo(la,ht)
	
        s1=KouseiJiDate(mjd,lg)

        x0 =  r0*cos(fi)*cos(s1)        #<5.4.1>
        y0 =  r0*cos(fi)*sin(s1)
        z0 =  r0*sin(fi)

        xx =  dl*cos(dc)*cos(ra)
        yy =  dl*cos(dc)*sin(ra)
        zz =  dl*sin(dc)

        X = xx - x0
        Y = yy - y0
        Z = zz - z0

        dl2 = sqrt(X*X+Y*Y+Z*Z)
        
        ra2 = Shogen(Y,X)
        dc2 = atan(Z/(Y/sin(ra2)))

        kodo_houi=KodoHoui(today,lg,la,ra2,dc2)

        al = kodo_houi[0]
        hi = kodo_houi[1]

        dc2 *= RAD
        al  *= RAD
        hi  *= RAD

#        print('ra1 %8.4f ra2  %8.4f     dc %8.4f  dc2  %8.4f'% (ra,ra2,dc,dc2))
        
        date1=MjdToDate(today)
        yy =date1[0]
        mm =date1[1]
        dd =date1[2]


        hour = RadToHr(ra2)
        hh = hour[0]
        ms = hour[1]
        ss = hour[2]
 
        ms += ss/60.0

        dh = int(dc2)
        dm = abs(dc2-dh)*60.0

        if (dc2<0):
            sg = '-'
        else:
	    sg = '+'

        print('%4d %2d %2d  %3d | %2d %6.2f   %s %3d %4.1f %5.1f   %4.1f %5d'  % (yy,mm,dd,min1,hh,ms,sg,dh,dm,al,hi,dl2))
