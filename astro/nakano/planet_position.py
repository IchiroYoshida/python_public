"""
planet_position.py

  INPUT | planet_orbits[planet][6]
 OUTPUT | planet_position[planet][3](x,y,z)

planet_position=PlanetPosition(planet_orbits)

"""
from math import *
from astro import *

from eph_const import EphConst
from kepler import Kepler

pp=[[0.0 for i in range(3)] for j in range(9)]
eph_const=[[0.0 for i in range(3)] for j in range(2)]

#planet_orbits=[[0 for i in range(8)] for j in range(9)]

def PlanetPosition(planet_orbits):

	for planet in range(9):

    		ec   =planet_orbits[planet][1]
    		mo   =planet_orbits[planet][2]
    		pe   =planet_orbits[planet][3]
    		nd   =planet_orbits[planet][4]
    		ic   =planet_orbits[planet][5]
    		aa   =planet_orbits[planet][6]

    		mo=PI2*(mo/PI2-int(mo/PI2))

    		if pe<0:
        		pe += PI2
    
    		eph_const=EphConst(pe,nd,ic)

    		mo=mo/PI2
    		mo=PI2*(mo-int(mo))

    		kepler=Kepler(ec,mo)

    		ss=kepler[0]
    		cc=kepler[1]
    		ff=kepler[2]

    		bb=aa*sqrt(1-ec*ec)  #(2.3.6) p.31

    		for n in range(3):
			fn=aa*eph_const[0][n]
    			qn=bb*eph_const[1][n]

			pp[planet][n]=ff*fn+ss*qn
	
	return pp

