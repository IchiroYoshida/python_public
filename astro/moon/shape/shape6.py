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
import pangle 

location = ephem.Observer()
location.name = 'Fukuoka'
location.lon, location.lat = '130.391', '33.593'
location.date = '2020/06/01 21:00:00' #21:00 JST
location.date -= 9*ephem.hour

moon = ephem.Moon(location)
alpha = moon.elong 
kai = pangle.moon_Pangle(location)

rr = 250

pol_x = []
pol_y = []

for th in range(-90, 100, 10):
    th2 = math.radians(th)   

    x0 = math.cos(th2) * math.cos(alpha)
    y0 = math.sin(th2)
    x1 = math.cos(kai)*x0 - math.sin(kai)*y0
    y1 = math.sin(kai)*x0 + math.cos(kai)*y0
    x2= rr * (x1 + 1) 
    y2 =rr * (y1 + 1)

    pol_x.append(x2)
    pol_y.append(y2)

for th in range(90, -100, -10):
    th2 = math.radians(th) 

    x0 = -math.cos(th2)
    y0 =  math.sin(th2)
    x1 =  math.cos(kai)*x0 - math.sin(kai)*y0
    y1 =  math.sin(kai)*x0 + math.cos(kai)*y0
    x2 =  rr * (x1 + 1)
    y2 =  rr * (y1 + 1)

    pol_x.append(x2)
    pol_y.append(y2)

moon_polygon = list(zip(pol_x, pol_y))

MO = np.array(moon_polygon)

poly = plt.Polygon(MO, alpha = 0.5, fc='#000000')

im = Image.open('./fullmoon.png')
im_list = np.asarray(im)

ax = plt.gca()

ax.add_artist(poly)
ax.set_aspect('equal')
ax.set_title(str(location.date))
ax.axis('off')
plt.imshow(im_list)

plt.show()
