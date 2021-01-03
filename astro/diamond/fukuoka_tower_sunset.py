"""
    Fukuoka Tower Sunset 
"""
from numpy import sin,cos,tan
import math
import ephem

RAD=180/math.pi

patios = ephem.Observer()
patios.lon, patios.lat = '130.351472','33.593312'

patios.date='2016/01/01 0:00' #JST 9:00 AM
sun=ephem.Sun()

date0=patios.date

for day in range (365):
    patios.date=date0+day
    sunset=patios.next_setting(sun)
    patios.date=sunset - ephem.minute*20.
    #patios.date=sunset
    sun.compute(patios)

    th=float(sun.az)*RAD
    alt=float(sun.alt)*RAD

    print (" %s --- %.3f %.3f " %(patios.date,th,alt))
