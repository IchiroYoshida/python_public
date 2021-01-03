"""
planet_angle.py

  INPUT | planet_position
 OUTPUT | planet_angle 

planet_angle[planet][0]=RA
planet_angle[planet][1]=DC

planet_angle=PlanetAngle(planet_position)

"""
from math import *
from astro import *

planet_angle=[[0.0 for i in range(2)] for j in range(9)]

def PlanetAngle(planet_position):

	for planet in range(9):
		#(3.4.5) p.59 
 		c1 = planet_position[planet][0]
		s1 = planet_position[planet][1]
		ra = atan2(s1,c1)

                if (ra<0):
                    ra += PI2
                    
		#ra:wakusei sekkei, dc:wakusei sekii

		#print("cc,ss,ra  %8.4f %8.4f %8.4f" % (cc,ss,ra))

		c2 = planet_position[planet][0]/cos(ra)
		s2 = planet_position[planet][2]
		dc = atan2(s2,c2)

		#print("cc,ss,dc  %8.4f %8.4f %8.4f" % (cc,ss,dc))

		planet_angle[planet][0]=ra
		planet_angle[planet][1]=dc

		#print("RA and DC %d %8.4f %8.4f" % (planet,ra,dc))

	return planet_angle

