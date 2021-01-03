#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
　大圏方位と角度の計算(LatLon) :富士山頂、東京都庁、安田講堂
"""
from numpy import sin,cos,tan,pi,arcsin
from math import acos,atan
from LatLon import *

RAD=pi/180.

Earth_R =6378137.0         # 地球の半径(m)

#富士山（山頂周辺)
Fuji_P1 = LatLon(35.366678,138.729569)  #白山岳（測定、3755.2m）
Fuji_P2 = LatLon(35.362828,138.730803)  #火口中央（測定、3537.2m)
Fuji_P3 = LatLon(35.360245,138.732326)  #山頂郵便局（測定、m）
Fuji_P4 = LatLon(35.360658,138.727348)  #剣ヶ峰（測定、3773m)

Fuji_H  =   3776.0           # (m)

#富士山（裾 3000m）
Fuji_P5 = LatLon(35.377075,138.725245)
Fuji_P6 = LatLon(35.348093,138.735952)


##### 東京都庁舎 ######
Tochou_NP1 = LatLon(35.689921,139.691607) #北
Tochou_NP2 = LatLon(35.689699,139.691672) #北
Tochou_SP1 = LatLon(35.689311,139.691747) #南
Tochou_SP2 = LatLon(35.689084,139.691817) #南
Tochou_C   = LatLon(35.689522,139.691786) #中央

Tochou_H  =    243.4  +41.2

##### 安田講堂 ########
Yasuda = LatLon(35.713397,139.762053) #時計台

Yasuda_H =     39.7  +25.0



#---LatLon calc　　富士山１--->安田講堂
distance_P1  = Yasuda.distance(Fuji_P1)  #WGS84 distance in (km)
heading_P1   = Yasuda.heading_initial(Fuji_P1) #WGS84 Ellipsoid
heading_P1   += 360.

print ("Fuji P1 --> Distance = %.2f  Heading = %.2f" % (distance_P1,heading_P1))

L= distance_P1 *1000.
u= L/Earth_R
u2 = u/RAD

h2=(Fuji_H+Earth_R+Yasuda_H)*cos(u)-(Earth_R+Yasuda_H)
deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　富士山２--->安田講堂
distance_P2  = Yasuda.distance(Fuji_P2)  #WGS84 distance in (km)
heading_P2   = Yasuda.heading_initial(Fuji_P2) #WGS84 Ellipsoid
heading_P2   += 360.

print ("Fuji P2 --> Distance = %.2f  Heading = %.2f" % (distance_P2,heading_P2))

L= distance_P2 *1000.
u= L/Earth_R
u2 = u/RAD

h2=(Fuji_H+Earth_R+Yasuda_H)*cos(u)-(Earth_R+Yasuda_H)
deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　富士山３--->安田講堂
distance_P3  = Yasuda.distance(Fuji_P3)  #WGS84 distance in (km)
heading_P3   = Yasuda.heading_initial(Fuji_P3) #WGS84 Ellipsoid
heading_P3   += 360.

print ("Fuji P3 --> Distance = %.2f  Heading = %.2f" % (distance_P3,heading_P3))

L= distance_P3 *1000.
u= L/Earth_R
u2 = u/RAD

h2=(Fuji_H+Earth_R+Yasuda_H)*cos(u)-(Earth_R+Yasuda_H)
deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　富士山４--->安田講堂
distance_P4  = Yasuda.distance(Fuji_P4)  #WGS84 distance in (km)
heading_P4   = Yasuda.heading_initial(Fuji_P4) #WGS84 Ellipsoid
heading_P4   += 360.

print ("Fuji P4 --> Distance = %.2f  Heading = %.2f" % (distance_P4,heading_P4))

L= distance_P4 *1000.
u= L/Earth_R
u2 = u/RAD

h2=(Fuji_H+Earth_R+Yasuda_H)*cos(u)-(Earth_R+Yasuda_H)
deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　富士山５（裾）--->安田講堂
distance_P5  = Yasuda.distance(Fuji_P5)  #WGS84 distance in (km)
heading_P5   = Yasuda.heading_initial(Fuji_P5) #WGS84 Ellipsoid
heading_P5   += 360.

print ("Fuji P5 --> Distance = %.2f  Heading = %.2f" % (distance_P5,heading_P5))

L= distance_P5 *1000.
u= L/Earth_R
u2 = u/RAD

Fuji_H = 3000.

h2=(Fuji_H+Earth_R+Yasuda_H)*cos(u)-(Earth_R+Yasuda_H)
deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　富士山６（裾）--->安田講堂
distance_P6  = Yasuda.distance(Fuji_P6)  #WGS84 distance in (km)
heading_P6   = Yasuda.heading_initial(Fuji_P6) #WGS84 Ellipsoid
heading_P6   += 360.

print ("Fuji P6 --> Distance = %.2f  Heading = %.2f" % (distance_P6,heading_P6))

L= distance_P6 *1000.
u= L/Earth_R
u2 = u/RAD

Fuji_H = 3000.

h2=(Fuji_H+Earth_R+Yasuda_H)*cos(u)-(Earth_R+Yasuda_H)
deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　都庁（北）１--->安田講堂
distance  = Yasuda.distance(Tochou_NP1)  #WGS84 distance in (km)
heading   = Yasuda.heading_initial(Tochou_NP1) #WGS84 Ellipsoid
heading   += 360.

print ("Tochou NP1 --> Distance = %.2f  Heading = %.2f" % (distance,heading))

L= distance *1000. 
u= L/(Earth_R+Yasuda_H)
u2 = u/RAD

t1=(Tochou_H+Earth_R)*cos(u)
t2=(Earth_R+Yasuda_H)

h2=t1-t2

deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　都庁（北）２--->安田講堂
distance  = Yasuda.distance(Tochou_NP2)  #WGS84 distance in (km)
heading   = Yasuda.heading_initial(Tochou_NP2) #WGS84 Ellipsoid
heading   += 360.

print ("Tochou NP2 --> Distance = %.2f  Heading = %.2f" % (distance,heading))

L= distance *1000. 
u= L/(Earth_R+Yasuda_H)
u2 = u/RAD

t1=(Tochou_H+Earth_R)*cos(u)
t2=(Earth_R+Yasuda_H)

h2=t1-t2

deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　都庁（南）１--->安田講堂
distance  = Yasuda.distance(Tochou_SP1)  #WGS84 distance in (km)
heading   = Yasuda.heading_initial(Tochou_SP1) #WGS84 Ellipsoid
heading   += 360.

print ("Tochou SP1 --> Distance = %.2f  Heading = %.2f" % (distance,heading))

L= distance *1000. 
u= L/(Earth_R+Yasuda_H)
u2 = u/RAD

t1=(Tochou_H+Earth_R)*cos(u)
t2=(Earth_R+Yasuda_H)

h2=t1-t2

deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　都庁（南）２-->安田講堂
distance  = Yasuda.distance(Tochou_SP2)  #WGS84 distance in (km)
heading   = Yasuda.heading_initial(Tochou_SP2) #WGS84 Ellipsoid
heading   += 360.

print ("Tochou SP2 --> Distance = %.2f  Heading = %.2f" % (distance,heading))

L= distance *1000. 
u= L/(Earth_R+Yasuda_H)
u2 = u/RAD

t1=(Tochou_H+Earth_R)*cos(u)
t2=(Earth_R+Yasuda_H)

h2=t1-t2

deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))

#---LatLon calc　　都庁（中央）-->安田講堂
distance  = Yasuda.distance(Tochou_C)  #WGS84 distance in (km)
heading   = Yasuda.heading_initial(Tochou_C) #WGS84 Ellipsoid
heading   += 360.

print ("Tochou SP2 --> Distance = %.2f  Heading = %.2f" % (distance,heading))

L= distance *1000. 
u= L/(Earth_R+Yasuda_H)
u2 = u/RAD

t1=(Tochou_H+Earth_R)*cos(u)
t2=(Earth_R+Yasuda_H)

h2=t1-t2

deg=atan(h2/L)/RAD

print ("u2 = %.6f | h2= %.6f   |deg = %.6f " % (u2,h2,deg))












