"""
    Fukuoka tower sunset 2018-8-23
"""

import math
import ephem
import datetime

sky = ephem.Observer()
#sky.lon, sky.lat = '130.351472','33.593312'
sky.lon, sky.lat = '130.3881','33.5880'
sky.horizon = '-0:34'

sky_az = float(ephem.degrees('279:40:05.7'))
sky_alt = float(ephem.degrees('2:31:52.3'))

date0 = '2018/09/03 0:00:00'

moon = ephem.Moon()

sky.date = date0
moon.compute(sky)

moonset = sky.next_setting(moon)

sky.date = moonset - ephem.minute*30
date1 = sky.date

for ti in range(0, 20, 1):
    sky.date = date1 + ti * ephem.minute
    moon.compute(sky)

    moon_az = float(moon.az)
    moon_alt = float(moon.alt)

    delta_az = math.fabs(sky_az - moon_az)
    delta_alt = math.fabs(sky_alt - moon_alt)

    r2 = delta_az * delta_az + delta_alt * delta_alt
    r1 = math.sqrt(r2)

    moon_az = math.degrees(moon_az)
    moon_alt = math.degrees(moon_alt)

    print('Date = %s Az = %lf Alt =%lf r1 = %lf ' % (sky.date,moon_az,moon_alt,r1 ))
