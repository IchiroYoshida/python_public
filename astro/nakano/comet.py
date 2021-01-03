"""
comet.py

CometRADC(mjd,comet)

comet_radc=CometRADC(mjd,comet)
"""

from math import *
from astro import *
from mjd import *

from mean_elements import *
from eph_const import *
from shogen import *
from kepler import Kepler
from planet_position import *

planet_orbits=[[0 for i in range(8)] for j in range(9)]
planet_position=[[0.0 for i in range(3)] for j in range(9)]
comet_position=[0.0 for i in range(4)]

def CometRADC(mjd,comet):

    mjd2 = mjd

    while True:
         comet_earth=CometEarth(mjd,comet)
   
         dl1 = comet_earth[3]
         mjd2 -= 5.776e-3 * dl1 # koukousa

         comet_earth=CometEarth(mjd2,comet)
       
         dl2 = comet_earth[3]

	 if abs(dl1-dl2)<1e-3:
	     break
    	 else:
	     mjd2 -= 5.776e-3 *dl2

    Comet_x = comet_earth[0]
    Comet_y = comet_earth[1]
    Comet_z = comet_earth[2]

    Comet_ds = comet_earth[3]

    comet_position=CometPosition(mjd2,comet)
    Comet_sun =comet_position[3]

#********* Angle

    c1 = Comet_x
    s1 = Comet_y
    ra = Shogen(s1,c1)

    if (ra<0):
        ra += PI2

    c2 = Comet_x/cos(ra)
    s2 = Comet_z
    dc = atan(s2*c2)

    comet_radc=[ra,dc,Comet_ds,Comet_sun]

#    print comet_radc

    return comet_radc


"""
comet_earth=CometEarth(mjd,comet)

"""
def CometEarth(mjd,comet):

    comet_position=CometPosition(mjd,comet)
    planet_orbits=MeanElements(mjd)
    planet_position=PlanetPosition(planet_orbits)
 
    Earth_x=planet_position[2][0]   #Sun centered Earth [x,y,z](AU)
    Earth_y=planet_position[2][1]
    Earth_z=planet_position[2][2]

#    print(' Earth[x,y,z]=%6.2f %6.2f %6.2f' % (Earth_x,Earth_y,Earth_z))

    Earth_ds=sqrt(Earth_x*Earth_x+Earth_y*Earth_y+Earth_z*Earth_z)

    Comet_x = comet_position[0]     #Sun centered Comet [x,y,z](AU)
    Comet_y = comet_position[1]
    Comet_z = comet_position[2]
    Sun_Comet_ds = comet_position[3]  #Sun--->Comet distance (AU)

#    print('Comet[x,y,z]=%6.2f %6.2f %6.2f' % (Comet_x,Comet_y,Comet_z))

    Comet_x -= Earth_x
    Comet_y -= Earth_y
    Comet_z -= Earth_z 	       #Earth centered position of Comet[x,y,z](AU)

    Earth_Comet_ds=sqrt(Comet_x*Comet_x + Comet_y * Comet_y + Comet_z * Comet_z)

#    print('Earth -> Comet (AU) |  x=%8.4f  y=%8.4f  z=%8.4f  ds=%8.4f' % (Comet_x,Comet_y,Comet_z,Earth_Comet_ds))

    comet_earth=[Comet_x,Comet_y,Comet_z,Earth_Comet_ds]

    return comet_earth


"""
comet_position=CometPosition(mjd,comet)


"""
def CometPosition(mjd,comet):

    comet_pe=comet[6]/RAD
    comet_nd=comet[7]/RAD
    comet_ic=comet[8]/RAD

    eph_const=EphConst(comet_pe,comet_nd,comet_ic)

    px = eph_const[0][0]  #F(1)
    qx = eph_const[1][0]  #Q(1)
    py = eph_const[0][1]  #F(2)
    qy = eph_const[1][1]  #Q(2)
    pz = eph_const[0][2]  #F(3)
    qz = eph_const[1][2]  #Q(3)
   
    nearly_parabolic=NearlyParabolic(mjd,comet)
    cc = nearly_parabolic[0]
    ss = nearly_parabolic[1]
    v  = nearly_parabolic[2]

    Comet_x = px*cc + qx*ss    #<6.2.14-17>
    Comet_y = py*cc + qy*ss
    Comet_z = pz*cc + pz*ss    #Sun centered position of Comet[x,y,z]

    Sun_Comet_ds = sqrt(Comet_x * Comet_x + Comet_y * Comet_y + Comet_z * Comet_z)

    comet_position=[Comet_x,Comet_y,Comet_z,Sun_Comet_ds]

    return comet_position

"""
#
# LIST 6-3 NEARLY PARABOLIC <p.203>
# 8600 -
# 
# INPUT mjd
#       ec  : Eccentricity
	q   : q

  OUTPUT  ss = r * cos(V)
  	  cc = r * sin(V)
	  V

nearly_parabolic[ss,cc,V] 
"""
def NearlyParabolic(mjd,comet):

    ec = comet[5]
    q  = comet[4]

    yy = comet[1]
    mm = comet[2]
    dd = comet[3]

    tt = ModifiedJulianDay(yy,mm,dd)
    
    r1 = 1.0+9.0*ec
				#<6.2.1>
    aa = sqrt(.1*r1)
    bb = 5.0*(1.0-ec)/r1	#<6.2.2>
    cc = sqrt(5.0*(1.0+ec)/r1)  #<6.2.3>

    b  = 1.0
    a0 = 0.0

    while 1:
        u = b*aa*K1*(mjd-tt)/(sqrt(2)*q**1.5)       #<6.2.4> p.190	
    	r2 = 1.0
    
        while 1:
            v = (u+2.0*r2**3/3.0)/(1+r2*r2)     #<6.2.7> p.191

	    if abs(v-r2)>1.0e-6 :
                r2 = v
            else :
                break
	
	a = bb*v*v                        #  <6.2.8> p.191
	a2 = a*a
	a3 = a*a*a

	b = 1-.017142857*a2-0.003809524*a3   #  <6.2.9> p.191
                    
        if abs(a-a0)>1.0e-6 :
             a0 = a
        else :
             break

    c = 1.0 + .4*a+.21714286*a2+.12495238*a3      #  <6.2.10> p.191
    d = 1.0 -  a  +.2*a2+5.71429e-3*a3            #  <6.2.11> p.191

    qd = q*d                                      #<6.2.13> p.191

    v  = cc*c*v
    cc = qd*(1.0-v*v)
    ss = 2.0*qd*v
    v  = 2.0*atan(v)

    nearly_parabolic=[cc,ss,v]

    return nearly_parabolic
