#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
東京都庁舎の日没時の影 
"""
from numpy import sin,cos,tan,pi
import math
import ephem

from myjavas import PrnJavaScript

xx,yy = [],[]
ll =[]

lon,lat=[],[]

sky = ephem.Observer()
sky.lon, sky.lat = '139.691787','35.689213'

RAD=180./math.pi

Earth=6378137.0   # (m)
H=243.0           # (m)


"""
date=['2016/6/20 0:00',
      '2016/7/20 0:00',
      '2016/8/20 0:00',
      '2016/9/20 0:00',
      '2016/10/20 0:00',
      '2016/11/20 0:00',
      '2016/12/20 0:00'] #JST 9:00 AM
"""
sky.date='2016/1/31 7:53' #計算開始時間（世界標準時）
date0=sky.date

sun=ephem.Sun()

lon_center=float(sky.lon)
lat_center=float(sky.lat)

lon.append(float(sky.lon)*RAD)
lat.append(float(sky.lat)*RAD)


def Rambda(delta_x):
	return (lon_center+delta_x/Earth/cos(lat_center))*RAD

def Phai(delta_y):
	return (lat_center+delta_y/Earth)*RAD

for ti in range(15):
        sky.date = date0 + ephem.second*10.*ti
        sun.compute(sky)

	th=float(sun.az)
	l=H /tan(float(sun.alt))
	ll.append(l)
	xx.append(-l*sin(th))
	yy.append(-l*cos(th))

	al=float(sun.alt)*RAD
	th2=th*RAD

	print ("Time = %s | th=%.2f al=%.2f" % (sky.date,th2,al))

for ti in range(len(xx)):

	lon.append(Rambda(xx[ti]))
	lat.append(Phai(yy[ti]))

PrnJavaScript("tochou.js",lat,lon)

