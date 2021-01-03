"""
    Mt. Kaya sunset 2018-9-18 from Kashii kamome bridge.
"""

import math
import ephem
import datetime

sky = ephem.Observer()
sky.lon, sky.lat = '130.4120','33.6460'
sky.elevation = 20.
sky.horizon = '-0:34'

sky_az = float(250.6596)
sky_alt = float(1.)

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

        sun_az = math.degrees(sun.az)
        sun_alt = math.degrees(sun.alt)
        
        delta_az = math.fabs(sky_az - sun_az)
        delta_alt = math.fabs(sky_alt - sun_alt)
        #print(sky.date, sun_az, sun_alt)

        r2 = delta_az * delta_az + delta_alt * delta_alt
        r1 = math.sqrt(r2)

        if (r1 < 0.1):
           print('Date = %s r1 = %lf ' % (sky.date,r1 ))
            
