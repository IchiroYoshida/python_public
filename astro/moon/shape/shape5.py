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

location = ephem.Observer()

location.name = 'Fukuoka'
location.lon, location.lat = '130.391', '33.593'
location.date = '2021/04/25 12:00:00' #21:00 JST

moon = ephem.Moon(location)
alpha = moon.elong 

rr = 250

pol_x = []
pol_y = []

for th in range(-90, 100, 10):
    th2 = math.radians(th)

    x1 = rr * math.cos(th2) * math.cos(alpha) + rr
    y2 = rr * math.sin(th2) + rr

    pol_x.append(x1)
    pol_y.append(y2)

for th in range(90, -100, -10):
    th2 = math.radians(th)

    x2 = -rr * math.cos(th2) + rr
    y2 =  rr * math.sin(th2) + rr

    pol_x.append(x2)
    pol_y.append(y2)

moon_polygon = list(zip(pol_x, pol_y))

#print(moon_polygon.shape)
MO = np.array(moon_polygon)

#poly = plt.Polygon(moon_polygon, alpha = 0.5, fc='#000000')
poly = plt.Polygon(MO, alpha = 0.5, fc='#000000')

im = Image.open('./fullmoon.png')
im_list = np.asarray(im)

ax = plt.gca()

ax.add_artist(poly)
ax.set_aspect('equal')
ax.set_title('Moon 2018/06/24 21:00:00 JST')
ax.axis('off')
plt.imshow(im_list)

plt.show()
