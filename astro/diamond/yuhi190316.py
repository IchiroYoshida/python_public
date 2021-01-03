
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
yuhi.date = '2019/03/16 17:58:00'
yuhi.date -= 9*ephem.hour

sun=ephem.Sun()

sun.compute(yuhi)

sun_az = math.degrees(sun.az)
sun_alt = math.degrees(sun.alt)

print('Sun.Az = %f Sun.Alt = %f' % (sun_az,sun_alt))

