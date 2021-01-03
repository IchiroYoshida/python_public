"""
    Fukuoka tower and Venus 2018-8-29
"""

import math
import ephem
import datetime

sky = ephem.Observer()
#sky.lon, sky.lat = '130.351472','33.593312'
sky.lon, sky.lat = '130.3881','33.5880'
sky.horizon = '-0:34'

sky_az = float(ephem.degrees('279:40:05.7'))
sky_alt = float(ephem.degrees('2:31:52.3')+1.66) # Top of the tower
#Distance 3450.686 m

date0 = '2018/01/01 6:00:00'

venus = ephem.Venus()

for day in range(0, 365, 1):
    sky.date = date0
    sky.date += day
    venus.compute(sky)

    venusset = sky.next_setting(venus)

    sky.date = venusset - ephem.minute*30
    date1 = sky.date

    for ti in range(0, 20, 1):
        sky.date = date1 + ti * ephem.minute
        venus.compute(sky)

        venus_az = float(venus.az)
        venus_alt = float(venus.alt)

        delta_az = math.fabs(sky_az - venus_az)
        delta_alt = math.fabs(sky_alt - venus_alt)

        r2 = delta_az * delta_az + delta_alt * delta_alt
        r1 = math.sqrt(r2)

        #if (r1 < 0.005):
        if (r1 < 2):

            print('Date = %s r1 = %lf ' % (sky.date,r1 ))
            
