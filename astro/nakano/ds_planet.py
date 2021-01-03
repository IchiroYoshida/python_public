"""
# ds_planet.py PLANET karano kyori (Chisin Nisshinn)
#
# ds_planet=DsPlanet(planet_position,planet)
"""
from math import *

def DsPlanet(planet_position,planet):

    	x1= planet_position[planet][0]
	x2= planet_position[planet][1]
	x3= planet_position[planet][2]

	ds_planet=sqrt(x1*x1+x2*x2+x3*x3)

        return ds_planet

