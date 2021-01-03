"""
LIST 3-15 APPEAR <p.82>

#appear.py

           HD, MJD
INPUT    | LG = LONGITUDE
	 | LA = LATITUDE
         | RA = R.A.
         | DC = DECL.
         | RR = TAIKI-SA
         | PP = CHIHEI-SHISA
	 | RD = Radius of planets
         | DS = KYORI(AU)
OUTPUT	 | TA = APPEAR TIME(UNIT OF HOUR)
	 | TD = DISAPP. TIME(UNIT OF HOUR)
         | AL =

appear_rise[ta,al]=AppearRise(mjd,lg,la,ra,dc,rr,rd,ds)
appear_sets[td,al]=AppearSets(mjd,lg,la,ra,dc,rr,rd,ds)


"""
from math import *
from astro import *
from shogen import *

appear_rise = [0.0 for i in range(2)]
appear_sets = [0.0 for i in range(2)]

#appear_rise[ta,al]
def AppearRise(mjd,lg,la,ra,dc,rd,ds):

    lg /= RAD
    la /= RAD

    if (ds>0):
        pp= atan(4.26e-05/ds)
        rd= atan(rd/(1.5e+08*ds))  # Radius/ ds* 1(A.U.)

    else :
        pp=0.0
        rd=0.0

    rr = .0102

    cc= -tan(dc)*tan(la)   #(3.7.3) <p.67>
    ss= sqrt(abs(1-cc*cc))
    h0= atan(ss/cc)

    if (h0<0):
        h0 +=PI

    dh=(rr+rd-pp)/(cos(la)*cos(dc)*sin(h0)) #(3.7.4) <p.67>

    s1=KouseiJiDate(mjd,lg)

    s2 = ra-h0-dh    #(3.7. 7) <p.68>

    ta = s2 -s1
    
    while (ta>PI2):
        TA -= PI2
        
    while (ta<0):
        ta += PI2

    ta /= 1.002738   #(3.7.11) <p.67>
#    ta *= RAD/15.0

    cc =  sin(dc)/cos(la)
    ss = -cos(dc)/sin(h0)
    al = abs(atan(ss/cc))

    if (dc<0):
        al = PI-al

    if (ta>PI2):
        ta -= PI2

#    print('ta = %8.4f' % ta)
    
    appear_rise=[ta,al]

    return appear_rise

def AppearSets(mjd,lg,la,ra,dc,rd,ds):

    lg /= RAD
    la /= RAD

    if (ds>0):
        pp= atan(4.26e-05/ds)
        rd= atan(rd/(1.5e+08*ds))  # Radius/ ds* 1(A.U.)

    else :
        pp=0.0
        rd=0.0

    rr = .0102

    cc= -tan(dc)*tan(la)   #(3.7.3) <p.67>

    ss= sqrt(1-cc*cc)
    h0= atan(ss/cc)

    if (h0<0):
        h0 +=PI

    dh=(rr+rd-pp)/(cos(la)*cos(dc)*sin(h0)) #(3.7.4) <p.67>

    s1=KouseiJiDate(mjd,lg)

    s3 = ra+h0+dh    #(3.7. 8) <p.68>

    td = s3-s1 
 
    while (td>PI2):
        td -= PI2
 
    while (td<0):
        td += PI2

    td /= 1.002738
#    td *= RAD/15.0

    cc =  sin(dc)/cos(la)
    ss = -cos(dc)/sin(h0)
    al = abs(atan(ss/cc))

    if (dc<0):
        al = PI-al

    while (td > PI2):
        td -= PI2
        
    appear_sets=[td,al]

#    print ('td = %8.4f '% td)
    
    return appear_sets 
