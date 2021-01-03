"""
Moon shape3
2018-06-23

Shape of the moon
"""
import numpy as np
import ephem
import math
import matplotlib.pyplot as plt
from PIL import Image

RAD = 180. / ephem.pi

location = ephem.Observer()

location.name = 'Fukuoka'
location.lon, location.lat = '130.391', '33.593'
location.date = '2019/02/23 12:00:00' #21:00 JST

def rnd36(x):
    return (x - math.floor(x / 360) * 360)

sun = ephem.Sun(location)
moon = ephem.Moon(location)

ecl_moon = ephem.Ecliptic(moon)
ecl_sun = ephem.Ecliptic(sun)

alpha = rnd36((ecl_moon.lon - ecl_sun.lon)*RAD)

rr = 250

#circ = plt.Circle((250, 250), rr, alpha = 0.8, fc='#770000')

pol_x = []
pol_y = []

for th in range(-90, 100, 10):
    alpha2 = math.radians(alpha)
    th2 = math.radians(th)

    x1 = rr * math.cos(th2) * math.cos(alpha2) + 250
    y2 = rr * math.sin(th2) + 250

    pol_x.append(x1)
    pol_y.append(y2)

for th in range(90, -100, -10):
    th2 = math.radians(th)

    x2 = rr * math.cos(th2) + 250
    y2 = rr * math.sin(th2) + 250

    pol_x.append(x2)
    pol_y.append(y2)

moon_polygon = list(zip(pol_x, pol_y))

poly = plt.Polygon(moon_polygon, alpha = 0.8, fc='#888888')

im = Image.open('./fullmoon.png')
im_list = np.asarray(im)

ax = plt.gca()

#ax.add_artist(circ)
ax.add_artist(poly)
ax.set_xlim(0, 500); ax.set_ylim(0, 500)
ax.set_aspect('equal')
ax.set_title('Moon shape plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
plt.imshow(im_list)
plt.show()
