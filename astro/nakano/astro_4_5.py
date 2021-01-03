"""
# LIST 4-5 CHIRI-IDO,CHISIN-IDO,CHISIN-KYORI

# LIST 4-1 CHISIN IDO
# LIST 4-1 CHISIN KYORI

"""

from math import *
from astro import *

###########Main
#TOKYO

LG=139.745
LA= 35.654
HT=  0.0

OB="TOKYO"

for i in range (0,90,5):

    la = i/RAD

    r1=ChishinIdo(la,HT)

    r0=ChishinKyori(la)

    dr = la-r1

    print('%8.4f   %8.4f   %8.4f   %8.4f  '% (la*RAD,r1*RAD,dr*RAD,r0))
    
