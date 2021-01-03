"""
Moon shape2
2018-06-23


 r * sin(th)*cos(alpha)

"""

import math
import matplotlib.pyplot as plt

rr = 100

circ = plt.Circle((0, 0), rr, alpha = 0.8, fc='#770000')

alpha = math.radians(30.)
kai   = math.radians(60.)

pol_x = []
pol_y = []

for th in range(-90, 100, 10):
    th2 = math.radians(th)

    x0 = math.cos(th2) * math.cos(alpha)
    y0 = math.sin(th2)
    x1 = math.cos(kai)*x0 - math.sin(kai)*y0
    y1 = math.sin(kai)*x0 + math.cos(kai)*y0
    x2 = rr * x1 
    y2 = rr * y1 

    pol_x.append(x2)
    pol_y.append(y2)

for th in range(90, -100, -10):
    th2 = math.radians(th)

    x0 = math.cos(th2)
    y0 = math.sin(th2)
    x1 = math.cos(kai)*x0 - math.sin(kai)*y0
    y1 = math.sin(kai)*x0 + math.cos(kai)*y0
    x2 = rr * x1
    y2 = rr * y1

    pol_x.append(x2)
    pol_y.append(y2)

moon_polygon = list(zip(pol_x, pol_y))

poly = plt.Polygon(moon_polygon, fc='yellow')


ax = plt.gca()
ax.add_artist(circ)
ax.add_artist(poly)
ax.set_xlim(-rr, rr); ax.set_ylim(-rr, rr)
ax.set_aspect('equal')
ax.set_title('Moon shape plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
plt.show()

