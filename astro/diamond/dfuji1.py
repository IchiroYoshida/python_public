"""
    Diamond Fuji --- Tokyo Skytree	
"""
from numpy import sin,cos,tan
import math
import ephem

RAD=180/math.pi

tokyo_sky = ephem.Observer()
tokyo_sky.lon, tokyo_sky.lat = '139.810700','35.710039'

tokyo_sky.date='2016/01/01 0:00' #JST 9:00 AM
sun=ephem.Sun()

date0=tokyo_sky.date

for day in range (365):
    tokyo_sky.date=date0+day
    sunset=tokyo_sky.next_setting(sun)
    tokyo_sky.date=sunset - ephem.minute*14
    sun.compute(tokyo_sky)

    th=float(sun.az)*RAD
    alt=float(sun.alt)*RAD

    print (" %s --- %.3f %.3f" %(tokyo_sky.date,th,alt))
