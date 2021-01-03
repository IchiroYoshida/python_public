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

appear = [0.0 for i in range(2)]

#appear_rise = [0.0 for i in range(2)]
#appear_sets = [0.0 for i in range(2)]

#appear[rise,set,houi]=Appear()
def Appear(mjd,lg,la,ra,dc,rd,ds):

    lg /= RAD
    la /= RAD

#    print('Appear today %8.4f LG=%8.4f LA=%8.4f ra=%8.4f dc=%8.4f rd=%8.4f ds=%8.4f' % (mjd,lg,la,ra,dc,rd,ds))

    if (ds>0):
        pp= atan(4.26e-05/ds)
        rd= atan(rd/(1.5e+08*ds))  # Radius/ ds* 1(A.U.)

#	print('pp=%8.5f rd=%8.5f' % (pp,rd))

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
#    print ('h0= %8.4f dh= %8.4f' % (h0,dh))

    s1=KouseiJiDate(mjd,lg)

    s2 = ra-h0-dh    #(3.7. 7) <p.68>
    s3 = ra+h0+dh    #(3.7. 8) <p.68>

#    print('ra=%8.4f h0=%8.4f dh=%8.4f' % (ra,h0,dh)) 
 
#    print ('s1=%8.4f s2=%8.4f  s3=%8.4f' % (s1,s2,s3))

    ta = s2-s1
    td = s3-s1 
 
    while (ta < 0):
        ta += PI2

    while (td < 0):
        td += PI2

#    print ('post ta=%8.4f  td=%8.4f' % (ta,td))


    ta /= 1.002738   #(3.7.11) <p.67>
    ta *= RAD/15.0

    td /= 1.002738
    td *= RAD/15.0

    if (ta>24.0):
        ta -= 24.0

    if (td>24.0):
        td -= 24.0

    cc =  sin(dc)/cos(la)
    ss = -cos(dc)/sin(h0)
    al = abs(atan(ss/cc))

    if (dc<0):
        al = PI-al

    appear=[ta,td,al]

    return appear


