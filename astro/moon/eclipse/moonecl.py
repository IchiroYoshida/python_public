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
#gatech.date ='2021/05/26 18:00:00' #JST
gatech.date = '2022/11/08 18:00:00' #JST
gatech.date -= 9*ephem.hour #JST -> UT
timetuple = gatech.date

# Objects
sun, moon = ephem.Sun(), ephem.Moon()

X = []
Y = []

for x in range(0,600,30):
    gatech.date= (ephem.date(ephem.date(timetuple)+x*ephem.minute))
    sun.compute(gatech)
    moon.compute(gatech)

    shadow_ra  = sun.g_ra + ephem.pi
    shadow_dec = - sun.g_dec

    xx = - (moon.g_ra  - shadow_ra ) 
    yy =   (moon.g_dec - shadow_dec)

    sun_earth  = sun.earth_distance * AU
    sun_radius = ephem.sun_radius/1000.

    earth_radius = ephem.earth_radius/1000.  # Km
    moon_earth = moon.earth_distance * AU    # Km
    
    A = earth_radius - moon_earth/sun_earth * (sun_radius - earth_radius)
    B = moon_earth/sun_earth * (sun_radius + earth_radius) + earth_radius

    A_rad = math.atan(A/moon_earth)  # Umbra
    B_rad = math.atan(B/moon_earth)  # Periumbra

    r_moon  = moon.radius
    s = ephem.separation((shadow_ra, shadow_dec), (moon.g_ra, moon.g_dec)) 
 
    rr = B_rad + r_moon

    if (s < rr ):
        #print('Time = %s Sep = %f'%(gatech.date, s))

        X.append(xx)
        Y.append(yy)

fig, ax = plt.subplots()

for i in range(len(X)):
    c = patches.Circle(xy=(X[i], Y[i]), radius = r_moon, fc='y', ec='k',zorder= 0)
    ax.add_patch(c)

shadow1 = patches.Circle(xy=(0, 0), radius = A_rad, fc='k',alpha=0.6,zorder = 0)
ax.add_patch(shadow1)

shadow2 = patches.Circle(xy=(0, 0), radius = B_rad, fc='k',alpha=0.3,zorder = 0)
ax.add_patch(shadow2)

plt.xlim(-0.05,0.05)
plt.ylim(-0.05,0.05)

#ax.scatter(X,Y)
ax.set_aspect('equal')
ax.axis('off')

plt.show()
