"""
    Pearl Fuji --- Yokosuka
"""
from numpy import sin,cos,tan
import math
import ephem

RAD=180/math.pi

pos = ephem.Observer()
pos.lon, pos.lat = '138.7273','35.3609' # Mt. Fuji
pos.elevation = 3770.

pos.date='2019/02/20 6:33' #JST 
pos.date -= 9*ephem.hour #JST->UTC

moon=ephem.Moon()

moon.compute(pos)

th = float(moon.az)*RAD
alt = float(moon.alt)*RAD
r2 = 2.0*float(moon.radius)*RAD
print (" %s --- %.6f %.6f %8.5f " %(pos.date,th,alt,r2))
