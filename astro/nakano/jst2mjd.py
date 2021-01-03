# JST MJD Convert pp.36 2-1
#

import math

#Tdays = [31,28,31,30,31,30,31,30,31,31,30,31,30,31]

def func_day(hour,min,sec):
	return (hour*3600+min*600+sec)/86400 

def func_mjd(yy,mm,dd):

	if mm < 3:
		mm += 12
		yy -= 1

	p5=yy+(mm-1)/12+dd/365.25

	if p5 > 1582.78 :
		mjd = int(365.25*yy) \
                     +int(yy/400) \
                     -int(yy/100) \
	             +int(30.59*(mm-2)) \
		     + dd \
	             - 678912 
	elif yy < 0:
		mjd = int(365.25*yy) \
                     +int(30.59*(mm-2)) \
                     + dd \
                     - 678915
	else :
		mjd = int(365.25*yy) \
	             +int(30.59*(mm-2)) \
                     + dd \
                     - 678914

	return mjd

def signum(x):
	return -1 if x <0 else 0 if x ==0 else 1

mjd=func_mjd(1925,10,20)
print mjd

