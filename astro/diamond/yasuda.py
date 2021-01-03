#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
  安田講堂（東大本郷）からの日没の時刻と方位
"""
from numpy import sin,cos,tan,pi
import math
import ephem

yasuda = ephem.Observer()
yasuda.lon, yasuda.lat = '139.691694','35.6895' #安田講堂の位置
yasuda.elevation = 39.7 + 25.0                  #安田講堂の高さ、設置面の標高

RAD=180./math.pi

Earth=6378137.0   # (m)

yasuda.date='2016/1/31 7:50' #計算開始時間（世界標準時）
date0=yasuda.date

sun=ephem.Sun()

for ti in range(50):
        yasuda.date = date0 + ephem.second*10.*ti
        sun.compute(yasuda)

	th=float(sun.az)*RAD
	al=float(sun.alt)*RAD

	print ("Time = %s | th=%.2f al=%.2f" % (yasuda.date,th,al))
