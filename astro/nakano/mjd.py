"""
#Modified Julian Day

mjd.py

<p.35> LIST 2-1

INPUT | yy,mm,dd
OUT   | mjd

mjd=ModifiedJulianDay(yy,mm,dd)

"""

def ModifiedJulianDay(yy,mm,dd):

	if mm < 3:
		mm += 12
		yy -= 1

	p5=yy+(mm-1)/12.0+dd/365.25

	if p5 > 1582.78 :
		mjd = int(365.25*yy) \
                     +int(yy/400) \
                     -int(yy/100) \
	             +int(30.59*(mm-2)) \
		     + dd \
	             - 678912    #(2.1.4) 
	elif yy < 0:
		mjd = int(365.25*yy) \
                     +int(30.59*(mm-2)) \
                     + dd \
                     - 678915   #(2.1.6)
	else :
		mjd = int(365.25*yy) \
	             +int(30.59*(mm-2)) \
                     + dd \
                     - 678914    #(2.1.5)

	return mjd

