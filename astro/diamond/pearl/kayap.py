"""
   Mt. Kaya. Pearl Moon
"""

import math
import ephem
from datetime import datetime

yuhi = ephem.Observer()
yuhi.lon = '130.2001'
yuhi.lat = '33.5732'
yuhi.elevation = 3.
yuhi.horizon = '-0:34'

Az_ang  = 264.34 #degree
#Alt_ang  = math.degrees(math.atan(360/3631)) #degree
Alt_ang = 5.65

yuhi.date = '2019/01/01 0:00' #JST 9:00 AM
yuhi.date -= 9*ephem.hour  #JST -> UTC

moon = ephem.Moon()

date0 = yuhi.date

for day in range(365):
    yuhi.date = date0 + day
    moonset = yuhi.next_setting(moon)
    yuhi.date = moonset - ephem.minute*60
    
    date1 = yuhi.date

    for ti in range (0, 60, 1):
        yuhi.date = date1 + ti * ephem.minute
        moon.compute(yuhi)

        MoonAlt = math.degrees(moon.alt)
        MoonAz  = math.degrees(moon.az)

        if (MoonAlt > 2.5 ):
            RangeY = MoonAlt - Alt_ang
            RangeX = MoonAz  - Az_ang
            AbsRangeX = math.fabs(RangeX)
            AbsRangeY = math.fabs(RangeY)

            time1 = yuhi.date + 9*ephem.hour #UTC -> JST
            time1 = ephem.Date(time1).datetime()
            time  = time1.strftime("%m/%d-%H:%M:%S")

            if (AbsRangeX < 1.0):
                if (AbsRangeY < 1.0):
                    print('Date = %s | Y = %6.3f  X = %6.3f' % (time, RangeY, RangeX))
