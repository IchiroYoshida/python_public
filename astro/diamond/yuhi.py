
"""
油比からの日没の時刻と方位
"""
from numpy import sin,cos,tan,pi
import math
import ephem

yuhi = ephem.Observer()
yuhi.horizon = '-0:34'
yuhi.lon, yuhi.lat = '130.1999','33.5734'
yuhi.elevation = 7. 

sun=ephem.Sun()

RAD=180./math.pi

Earth=6378137.0   # (m)

year = '2018/01/01'

L = 3615.    
H = 365.

direct = 267.5489 #Degrees

angle = math.atan(H/L)


for d in range(365):
    yuhi.date = year
    yuhi.date += d

    sun.compute(yuhi)

    nextset = yuhi.next_setting(sun)
    start = nextset - 60*ephem.minute

    for ti in range(60):
        yuhi.date = start + ti*ephem.minute
        sun.compute(yuhi)
        sun_az = math.degrees(sun.az)
        sun_alt = math.degrees(sun.alt)
        angle2 = math.degrees(angle + sun.radius)
        th = math.fabs(sun_alt - angle2)
        de = math.fabs(sun_az - direct)
        if (th<.25 and de<.25):
            print('Date and time =%s Sun.Az = %f Sun.Alt = %f th =%f de =%f' % (yuhi.date,sun_az,sun_alt,th,de))

