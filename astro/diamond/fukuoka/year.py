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

date0 = '2019/01/01 6:00:00'

sun = ephem.Sun()

for day in range(0, 365, 1):
    sky.date = date0
    sky.date += day
    sun.compute(sky)

    sunset = sky.next_setting(sun)

    sky.date = sunset - ephem.minute*30
    date1 = sky.date

    for ti in range(0, 20, 1):
        sky.date = date1 + ti * ephem.minute
        sun.compute(sky)

        sun_az = float(sun.az)
        sun_alt = float(sun.alt)

        delta_az = math.fabs(sky_az - sun_az)
        delta_alt = math.fabs(sky_alt - sun_alt)

        r2 = delta_az * delta_az + delta_alt * delta_alt
        r1 = math.sqrt(r2)

        if (r1 < 0.005):
            print('Date = %s r1 = %lf ' % (sky.date,r1 ))
            
