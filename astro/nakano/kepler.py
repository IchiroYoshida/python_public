"""
LIST 2-14 KEPLER <p.41>
# 8500 **** KEPLER 

#kepler.py

INPUT    | EC = ECCENTRICITY
	 | MO = MEAN ANOMALY
OUTPUT	 | SS = SIN(E)
	 | CC = COS(E)
         | FF = COS(E)-EC
kepler[ss,cc,ff]=Kepler(ec,mo)
"""
from math import *

def Kepler(ec,mo):
	a1=0.0
	a2=ec*sin(a1+mo)  #(2.3.12) p.33
	
#	print('%8.7f %8.7f' % (a1,a2))

	while abs(a2-a1)> 1e-5:
		a1=a2
		a2=ec*sin(a1+mo)
#		print('%8.7f %8.7f' %(a1,a2))

	a1=a2+mo

	ss=sin(a1)
	cc=cos(a1)
	ff=cc-ec

	kepler=[ss,cc,ff]

	return kepler

	
