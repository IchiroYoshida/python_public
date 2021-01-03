#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
　大圏方位と角度の計算 :富士山頂、東京都庁、安田講堂
"""
from numpy import sin,cos,tan,pi,arcsin
from math import acos,atan

RAD=pi/180.

Earth_R =6378137.0         # (m)
#Fuji_H  =   3776.0           # (m)
TMGB_H  =    243.4  +41.2
Yasuda_H=     39.7  +25.0

Fuji_H=TMGB_H - Yasuda_H

#A_lon, A_lat = '138.727365'  ,'35.360628'   #富士山（公式）
#A_lon, A_lat = '138.730963'  ,'35.362894'   #富士山（火口中央、測定）


#A_lon, A_lat = '139.691694'   ,'35.6895'    #東京都庁（公式）
#A_lon, A_lat = '139.691717'   ,'35.689522'    #東京都庁（測定）
A_lon, A_lat = '139.691787'   ,'35.689213'    #東京都庁（南庁舎）



B_lon, B_lat = '139.761944'   ,'35.713333' #安田講堂

a1 =float(A_lon)*RAD
b1= float(A_lat)*RAD

a2 =float(B_lon)*RAD
b2= float(B_lat)*RAD

c1 =cos(b2)*sin(a2-a1)
c2 =cos(b1)*sin(b2)-sin(b1)*cos(a2)*cos(a2-a1)
u1 =sin(b1)*sin(b2)+cos(b1)*cos(b2)*cos(a2-a1)

u =acos(u1)
u2 = u/RAD

L=Earth_R*u
h2=(Fuji_H+Earth_R)*cos(u)-Earth_R
L2=(Fuji_H+Earth_R)*sin(u)

sin_th=c1/sin(u)
th=arcsin(sin_th)/RAD

Fuji_deg=atan(h2/L2)/RAD

print ("L= %.6f L2= %.6f  |u2 = %.6f | h2= %.6f   |deg = %.6f  |th= %.6f" % (L,L2,u2,h2,Fuji_deg,th))

