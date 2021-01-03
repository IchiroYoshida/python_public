import math
import ephem
from datetime import datetime
import tle_iss_nasa as tle
from observe import *

sun = ephem.Sun()

obs.date = datetime.now()
obs.date -= 9 * ephem.hour #JST -> UTC
date1 = obs.date

obj = tle.TleIssNasa()
tles = obj.exec()

utc_time = obs.date.datetime()
lines = tle.tle_utc(utc_time, tles)
iss = ephem.readtle("ISS(ZARYA)",lines[0],lines[1])

print('Name = %s' % iss.name)
print('Location: %s' % obs.name)
print('Lat = %6.2lf Lon = %6.2lf' % (math.degrees(obs.lat), math.degrees(obs.lon)))

for day in range(0, 30, 1):
    obs.date = date1
    obs.date += day
    date2 = obs.date

    for hour in range(0, 24, 1):
        obs.date = date2
        obs.date += hour * ephem.hour
        date3 = obs.date

        utc_time = obs.date.datetime()
        lines = tle.tle_utc(utc_time, tles)
        iss = ephem.readtle("ISS(ZARYA)", lines[0], lines[1])

        for min in range(0, 60, 1):
            obs.date=date3
            obs.date += min * ephem.minute

            iss.compute(obs)
            sun.compute(obs)
            az = math.degrees(iss.az)
            alt = math.degrees(iss.alt)
            ecl=iss.eclipsed
            sun_alt = math.degrees(sun.alt)

            if(ecl is False):
                if(alt>10.):
                    if(sun_alt < -5.):
                        obs.date += 9 * ephem.hour
                        print('Date =%s ISS Az=%6.2lf Alt=%6.2lf  Sun Alt = %6.2lf'
                                % (obs.date,az,alt,sun_alt))
