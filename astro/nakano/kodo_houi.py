"""
# LIST 3-13 KODO HOUI <p.79>
# 7000- REM *** KODO HOUII ***
# kodo_houi.py

  INPUT     | JD = MJD
            | LG = LONGITUDE
            | LA = LATITUDE
            | RA = R.A.
            | DCL= DECL.
 OUTPUT     | AL = HOUI(FROM SOUTH TO WEST)
            | HI = KOUDO

 kodo_houi[al,hi]=KodoHoui(mjd,lg,la,ra,dc)


"""
from math import *
from astro import *
from shogen import *

def KodoHoui(mjd,lg,la,ra,dc):

    date=KouseiJiDate(mjd,lg)
    hh=date-ra

#   (3.6.2) <p.65>

    cc =  sin(dc)*cos(la)-cos(dc)*sin(la)*cos(hh)
    ss = -cos(dc)*sin(hh)
   
    al=Shogen(ss,cc)

    al += PI   # South ---->0

    if (al> PI2):
	al -= PI2
    if (al<0 ):
	al += PI2

    cc =  -cc/cos(al)
    ss =  sin(dc)*sin(la)+cos(dc)*cos(la)*cos(hh)

    hi=atan(ss/cc)

    kodo_houi=[al,hi]

    return kodo_houi
