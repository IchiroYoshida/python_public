import math
import ephem
from operator import itemgetter
from datetime import datetime
import tle_iss_nasa as tle
from observe import *

sun = ephem.Sun()

obs.date = datetime.now()
obs.date -= 9 * ephem.hour #JST -> UTC
date1 = obs.date

lines = tle.TleIssNasa().exec()
iss = ephem.readtle("ISS(ZARYA)",lines[0],lines[1])

print('Name = %s' % iss.name)
print('Location: %s' % obs.name)
print('Lat = %6.2lf Lon = %6.2lf' % (math.degrees(obs.lat), math.degrees(obs.lon)))

results = []
newline = True

for day in range(0, 30, 1):
    obs.date = date1
    obs.date += day
    date2 = obs.date
    for hour in range(0, 24, 1):
        obs.date = date2
        obs.date += hour * ephem.hour
        date3 = obs.date
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
                        if (newline):
                            if (results):
                                num = len(results)
                                gen = (x for x in results)
                                max_alt = max(results, key = itemgetter(2))

                                iss_start = [x for x in results[0]]
                                iss_end   = [x for x in results[num-1]]
                                print("Start at = %s  Az = %6.2lf " %  (str(iss_start[0]),iss_start[1]))
                                print("Max   at = %s  Az = %6.2lf Alt = %6.2lf " % (str(max_alt[0]),max_alt[1], max_alt[2]))
                                print("End   at = %s  Az = %6.2lf " % (str(iss_end[0]),iss_end[1]))

                            results = []
                            newline = False 

                        obs.date += 9 * ephem.hour
                        results.append([obs.date, az, alt])
                        #print('Date =%s ISS Az=%6.2lf Alt=%6.2lf  Sun Alt = %6.2lf'
                        #        % (obs.date,az,alt,sun_alt))

    newline = True

"""
            if(results):
                print("results = ", results)
                results = []

            if(results):
                gen = (x for x in results)
                max_alt = max(results, key = lambda x: x[2])
                print("Max Alt =", max_alt)
                print("Max Alt at: =", str(max_alt[0]))
                print("Max Alt hight =", str(max_alt[2]))
                results = []
"""

