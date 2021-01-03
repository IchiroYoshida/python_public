"""
    Taiken-Houi  Fuji ---> Kawasaki (Tokorozawa)
"""
from numpy import sin,cos,tan,pi,arcsin
from math import acos

RAD=pi/180.

Earth     = 6378137.0   # (m)
Fuji_H    =    3800.0   # (m)

A_lon, A_lat = '138.730993','35.362900'   #Fuji 
B_lon, B_lat = '139.517931','35.797846'   #Tokorozawa

a1 =float(A_lon)*RAD
b1= float(A_lat)*RAD

a2 =float(B_lon)*RAD
b2= float(B_lat)*RAD

c1 =cos(b2)*sin(a2-a1)
c2 =cos(b1)*sin(b2)-sin(b1)*cos(a2)*cos(a2-a1)
u1 =sin(b1)*sin(b2)+cos(b1)*cos(b2)*cos(a2-a1)

u =acos(u1)

L=Earth*u

sin_th=c1/sin(u)
th=arcsin(sin_th)/RAD

print ("L= %.6f,th= %.6f" % (L,th))

