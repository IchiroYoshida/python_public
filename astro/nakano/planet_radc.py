"""
planet_radc.py

  INPUT | MJD
        | PLANET
 OUTPUT | planet_radc[ra,dc,ds]

planet_angle[planet][0]=RA
planet_angle[planet][1]=DC

planet_radc[ra,dc,ds]=PlanetRADC(mjd,planet)

"""
from math import *
from astro import *

from mjd import ModifiedJulianDay
from mean_elements import MeanElements
from planet_position import PlanetPosition
from planet_angle import PlanetAngle
from ds_planet import DsPlanet

planet_orbits=[[0 for i in range(8)] for j in range(9)]
planet_position=[[0.0 for i in range(3)] for j in range(9)]
planet_angle=[[0.0 for i in range(2)] for j in range(9)]

planet_radc=[0.0 for i in range(3)]

def PlanetRADC(mjd,planet):

    planet_orbits=MeanElements(mjd)
    planet_position=PlanetPosition(planet_orbits)

#*********************
#(3.4.3):Nisshin zahyou wo Taiyouno Chisinn zahyouni henkan
    for n in range(3):
        planet_position[2][n]= -planet_position[2][n]

#Wakuseino nissinsekidouzahyou wo chisinsekidouzahyouni henkan
    for pl in range(9):
	    if (pl==2):
	        planet_orbits[2][0]="SUN"
	    else:
	        for n in range(3):
		    planet_position[pl][n]+=planet_position[2][n]

#*****************************

    planet_angle=PlanetAngle(planet_position)

    ra= planet_angle[planet][0]
    dc= planet_angle[planet][1]
    ds= DsPlanet(planet_position,planet)
 
    planet_radc[0]= ra
    planet_radc[1]= dc 
    planet_radc[2]= ds

#    print('radc %1d %8.5f %8.5f %8.5f' % (planet,ra,dc,ds))

    return planet_radc

