import ephem
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

AU = 1.496e8

# Location
gatech = ephem.Observer()
gatech.name = 'Fukuoka'
gatech.lon, gatech.lat = '33.593', '130.390' #Fukuoka
gatech.date ='2018/07/28 3:00:00' #JST
gatech.date -= 9*ephem.hour #JST -> UT
timetuple = gatech.date

# Objects
sun, moon = ephem.Sun(), ephem.Moon()

sun.compute(gatech)
moon.compute(gatech)

L  = sun.earth_distance * AU
R  = ephem.sun_radius/1000.

r = ephem.earth_radius/1000.  # Km
l = moon.earth_distance * AU    # Km

m = r * L /(R - r) -l

b2 = (l + m)*(l + m) - r*r

a = m * r /math.sqrt(b2)

print('l = %f a = %f m = %f' % (l,a,m))

