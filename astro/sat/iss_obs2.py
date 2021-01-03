import math
import ephem
from operator import itemgetter
import datetime
import tle_iss_nasa as tle
from observe import *

results=[]

sun = ephem.Sun()

date1 = obs.date

lines = tle.TleIssNasa().exec()
iss = ephem.readtle("ISS(ZARYA)", lines[0], lines[1])

print('Location: %s' % obs.name)
print('Lat = {:f}; Lon = {:f}'.format(math.degrees(obs.lat), math.degrees(obs.lon)))

for min in range(0, 15, 1):
    obs.date = date1
    obs.date += min * ephem.minute
    date2 = obs.date
    for sec in range(0, 60, 5):
        obs.date=date2
        obs.date += sec * ephem.second
        iss.compute(obs)
        sun.compute(obs)
        az = math.degrees(iss.az)
        alt = math.degrees(iss.alt)
        ecl=iss.eclipsed
        sun_alt = math.degrees(sun.alt)
        date3 = obs.date + 9*ephem.hour #UTC-> JST
        date4 = ephem.date(date3)

        if(alt > 0):
            if(sun_alt < - 5):
                if(ecl is False):
                    results +=[date4, az, alt]
                    print('Date =%s ISS Az=%lf Alt=%lf'
                           % (date4,az,alt))
                    if ( sec == 0 ):
                         print(date4)

        print("results =",results)

        gen=(x for x in results)
        max_alt=max(gen, key=itemgetter(2))
        #print("results =",results)
        print("max Alt =",max_alt)
        print("max Alt at: =",str(max_alt[0]))
        print("max Alt hight =",str(max_alt[2]))
