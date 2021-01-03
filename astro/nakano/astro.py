"""
#astro.py
"""
from math import *

PI =3.141592653589793
PI2=    2*PI
RAD=180.0/PI
HR = 12.0/PI

#Taikisa
RR= .0102 #Radian

#Teisuu
K1=.01720209895     # Gauss const. (k)
K4=.91743695        # cos(Epsi)
K5=.39788118        # sin(Epsi)
K6=RAD*3600

#Radius of Earth,Moon,Sun
EARTH_RD = 6378.16
MOON_RD  = 1738.0
SUN_RD   = 695989.0

#AU
AU       = 149597870.0

def fn0(x):
	int(x+.5)
def fnA(x):
	int(x*10+.5)/10
def fnB(x):
	int(x*100+.5)/100
def fnC(x):
	int(x*1000+.5)/1000

def KouseiJi1950(mjd,long): #(2.2.12) p.25,37
    r = .6705199+ 1.002737803*(mjd-40000)+long/PI2
    r = r-int(r)
    r *= PI2
    return r

def KouseiJiDate(mjd,long): #(2.2.11) p.25,37
    r = .671262 + 1.002737909*(mjd-40000)+long/PI2
    r = r-int(r)
    r *= PI2
    return r

def RadToHr(rad):
#hour[hh,mm,ss]=RadToHr(rad)
    s1=rad*HR
    hh=int(s1)
    ss=60*(s1-hh)
    mm=int(ss)
    ss=60*(ss-mm)
    hour=[hh,mm,ss] 
    return hour

def JapanStandardTime(hh,mm,ss):
    return (hh/24.0+mm/1440.0+ss/86400.0)

def UniversalTime(jst):
    return jst-0.37500  #(2.1.1)

def signum(x):
	return -1 if x <0 else 0 if x ==0 else 1
#
def Shogen(ss,cc):

    tt=atan(ss/cc)

#    print ss,cc,tt
    
    if (ss>0):
    	if (cc>0):
		pass    #1 shogen
	else:
		tt+=PI   #2 shogen
    else:
	if (cc>0):
		tt+=PI2   #3 shogen
	else:
		tt+=PI  #4 shogen
#    print tt
    
    return tt

#Section 4 Earth
#List 4-1
#   CHISHIN IDO
#   REM 4400 - <p.123>
#   <4.2.1> p.91 <4.2.2> p.92
def ChishinIdo(la,ht):
    r=atan((.9933055+1.1e-9*ht)*tan(la))
    return r
#List 4-2
#   CHISHIN KYORI
#   REM 4500 - <p.123>
#   <4.2.3> p.92
def ChishinKyori(lat):
    r=EARTH_RD*(.99832707+1.67644e-3*cos(2*lat)-3.52e-6*cos(4*lat))
    return r
#List 4-3
#   CHIRI IDO
#   REM 4600 -
def ChiriIdo(lat):
    r=atan(tan(lat)/.9933055)
    r=ChishinKyori(r)
    return r
#List 4-23
#   KOUDO ZAHYO p.134
#   REM 6200 -
def KoudoZahyo(x):
    xe= x[0]                #<4.5.1> p.108
    ye= x[1]*K4+x[2]*K5
    ze=-x[1]*K5+x[2]*K4

    lp=Shogen(ye,xe)        #<4.5.2> p.108
    cc= ye/sin(lp)
    bp=atan(ze/cc)
    r = sqrt(xe*xe+ye*ye*ze*ze)

    koudo_zahyo=[lp,bp,r]

    return koudo_zahyo


