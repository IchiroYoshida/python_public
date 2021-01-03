"""
# shogen.py
#
# LIST 2-10 <p.39>
# 3500- REM *** SYOGEN ***

  INPUT		| SS = SIN VALUE
  		| CC = COS VALUE
  OUTPUT	| TT = 0 DEG TO 360 DEG

tt=Shogen(ss,cc)

"""
from astro import * 
from math import *

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
