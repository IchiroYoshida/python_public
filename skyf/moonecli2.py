from skyfield.api import load
from pytz import timezone
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Location and time
# 初期時刻設定
ts = load.timescale()
t = ts.utc(2022, 11, 8, 9, 0, range(0, 15000))
tz = timezone('Asia/Tokyo')

# 太陽・月・地球
eph = load('de421.bsp')
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

# 太陽・月の位置計算
sun_app = earth.at(t).observe(sun).apparent()
moon_app = earth.at(t).observe(moon).apparent()

# 太陽・月の見かけの大きさ計算
r_sun = 696000
sun_dist = sun_app.distance().km
sun_rad = np.arctan2(r_sun, sun_dist)

r_moon = 1737
moon_dist = moon_app.distance().km
moon_rad = np.arctan2(r_moon, moon_dist)

# 視差・本影の視半径計算
r_earth = 6378
parallax_sun = r_earth / sun_dist
parallax_moon = r_earth / moon_dist
umbra = (parallax_moon - sun_rad + parallax_sun) * 51/50




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