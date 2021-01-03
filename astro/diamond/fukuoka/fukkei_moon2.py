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

date0 = '2018/01/01 6:00:00'

moon = ephem.Moon()

for day in range(0, 365, 1):
    sky.date = date0
    sky.date += day
    moon.compute(sky)

    moonset = sky.next_setting(moon)

    sky.date = moonset - ephem.minute*20
    date1 = sky.date

    for ti in range(0, 15, 1):
        sky.date = date1 + ti * ephem.minute
        moon.compute(sky)

        moon_az = float(moon.az)
        moon_alt = float(moon.alt)

        moon_az = math.degrees(moon_az)
        moon_alt = math.degrees(moon_alt)
    
        sky.date += 9.0 * ephem.hour

        year = sky.date.datetime().year
        month = sky.date.datetime().month
        day = sky.date.datetime().day

        start = datetime.datetime(year, month, day, 8, 30, 0)
        end = datetime.datetime(year, month, day, 17,15,0)
        time = sky.date.datetime()

        if (time > start and time < end):
            if (moon_alt > 0):
                print('Date = %s Moon | Az = %lf Alt = %lf ' % (sky.date,moon_az,moon_alt))
