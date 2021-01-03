"""
Moon shape1
2018-06-23


 r * sin(th)*cos(alpha)

"""

import math

rr = 100

for alpha in range (0, 360, 15):
   for th in range(-90, 100, 10):
       alpha2 = math.radians(alpha)
       th2 = math.radians(th)

       x1 = rr * math.cos(th2) * math.cos(alpha2)
    
       x2 = rr * math.cos(th2)
       y2 = rr * math.sin(th2)

       print ('%4d %3d | ( %6.1f, %6.1f ) -- ( %6.1f, %6.1f )' % (alpha, th, x1, y2, x2, y2))
