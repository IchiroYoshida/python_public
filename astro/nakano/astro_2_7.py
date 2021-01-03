"""
# 2-7 Orbital elements of each planets.

# PLANET NO ICHI 
"""

planet_orbits=[[0 for i in range(8)] for j in range(9)]

from math import *
from astro import PI,PI2,RAD

from mjd import ModifiedJulianDay
from mean_elements import MeanElements

mjd=ModifiedJulianDay(2000,1,1)

planet_orbits=MeanElements(mjd)

print ('No.   Name     e        M        Peri.      As.Node.         Inc.        Axis.')

for planet in range(9):

    name=planet_orbits[planet][0]
    e   =planet_orbits[planet][1]
    m   =planet_orbits[planet][2]
    p   =planet_orbits[planet][3]
    n   =planet_orbits[planet][4]
    i   =planet_orbits[planet][5]
    a   =planet_orbits[planet][6]

    m=PI2*(m/PI2-int(m/PI2))

    if p<0:
        p += PI2
    
    m=m*RAD
    p=p*RAD
    n=n*RAD
    i=i*RAD


    print ('%1d %8s %.6f %10.6f %10.6f %10.6f %10.6f %10.6f' % (planet,name,e,m,p,n,i,a))
    
    

