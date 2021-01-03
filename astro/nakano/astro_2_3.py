"""
# 2-3 Julius and Glegorio joint check 1582  
# LIST 2-1 MJD,JULIAN
 
"""
#import math

#import mjd
from mjd import ModifiedJulianDay

days=[1,2,3,4,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

for i in days:

	mjd=ModifiedJulianDay(1582,10,i)+2400000.5
	print 1582,10,i,mjd	

