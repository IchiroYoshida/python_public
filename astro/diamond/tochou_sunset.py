#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
  東京都庁舎からの日没の時刻と方位
"""
from numpy import sin,cos,tan,pi
import math
import ephem

tochou = ephem.Observer()
tochou.lon, tochou.lat = '139.691787','35.689213' #東京都庁の位置
tochou.elevation = 243. + 41.2  #都庁舎の高さ、設置面の標高

RAD=180./math.pi

Earth=6378137.0   # (m)

tochou.date='2014/02/01 7:50' #計算開始時間（世界標準時）
date0=tochou.date

sun=ephem.Sun()

for ti in range(50):
        tochou.date = date0 + ephem.second*10.*ti
        sun.compute(tochou)

	th=float(sun.az)*RAD
	al=float(sun.alt)*RAD

	print ("Time = %s | th=%.2f al=%.2f" % (tochou.date,th,al))
