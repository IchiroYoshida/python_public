import sys
import math
import ephem
import datetime
import tide_func
from moon_calc import *
import numpy as np
import data_read
"""
ヨナラ水道の一日の潮流
"""
year = 2018
month = 6
day  = 1

pt = tide_func.Port()

pt.hr = np.zeros(60,np.float64)
pt.pl = np.zeros(60,np.float64)

pt.name = data_read.name 
pt.lat  = data_read.lat
pt.lng  = data_read.lng
pt.level= data_read.level

pt.hr   = data_read.hr
pt.pl   = data_read.pl

moon = ephem.Moon()
pt_eph = ephem.Observer()
pt_eph.lon = pt.lng
pt_eph.lat = pt.lat
pt_eph.elevation = 0.0

print(pt.name,pt.date)

print (year,month, day)

pt.date = str(year)+str('/%02d' % month)+str('/%02d' % day)

today = tide_func.Tide(pt)
today.wav(pt)

current = today.m2s2

print(current)

