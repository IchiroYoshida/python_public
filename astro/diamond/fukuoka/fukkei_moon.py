"""
    Fukuoka tower sunset 2018-9-4 from Fukkei.
"""

import math
import ephem
import datetime

sky = ephem.Observer()
sky.lon, sky.lat = '130.5451','33.5603'
sky.elevation = 170.9
sky.horizon = '-0:34'

sky_az = float(ephem.degrees('281.4385'))
sky_alt = float(ephem.degrees('2:00:00'))

date0 = '2018/01/01 6:00:00'

moon = ephem.Moon()

for day in range(0, 365, 1):
    sky.date = date0
    sky.date += day
    moon.compute(sky)

    moonset = sky.next_setting(moon)

    sky.date = moonset - ephem.minute*20
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

        if (r1 < 0.1):
            print('Date = %s Moon | Az = %lf Alt = %lf | r1 = %lf ' % (sky.date,moon_az,moon_alt,r1 ))
            
