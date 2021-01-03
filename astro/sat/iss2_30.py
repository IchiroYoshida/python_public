import math
import ephem
from operator import itemgetter
from datetime import datetime
import tle_iss_nasa as tle
from observe import *

def show_results(results):
    num = len(results)
    gen = (x for x in results)
    max_alt = max(results, key = itemgetter(2))

    iss_start = [x for x in results[0]]
    iss_end   = [x for x in results[num-1]]

    start_time = iss_start[0].datetime().strftime("%Y/%m/%d %H:%M")
    start_Az   = str("%3.0lf" % iss_start[1])

    end_time   = iss_end[0].datetime().strftime("%H:%M")
    end_Az     = str("%3.0lf" % iss_end[1])

    max_time   = max_alt[0].datetime().strftime("%H:%M")
    max_Az     = str("%3.0lf" % max_alt[1])
    max_Alt    = str("%3.0lf" % max_alt[2])

    print(" %s : (%s) --> %s : (%s-%s) --> %s : (%s)" % (start_time, start_Az, max_time, max_Az, max_Alt, end_time, end_Az))


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
                                show_results(results)

                            results = []
                            newline = False 

                        obs.date += 9 * ephem.hour
                        results.append([obs.date, az, alt])
                        #print('Date =%s ISS Az=%6.2lf Alt=%6.2lf  Sun Alt = %6.2lf'
                        #        % (obs.date,az,alt,sun_alt))

    newline = True

if(results):
    show_results(results)
