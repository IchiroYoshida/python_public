import math
import ephem
from operator import itemgetter
from datetime import datetime
import tle_iss_nasa as tle
#from observe import *

"""
City, lat. lon.
"""

db = """
Fukuoka (UTC+9hours),33.5904,130.4017
Tokyo   (UTC+9hours),35.7090,139.7320
Seattle (UTC-8hours),47.6129,-122.4824
UMF Observatory (UTC-5),44.730,-70.140
Brugge  (UTC+1hour),51.2640,3.1153
Edive   (UTC+7hours),8.6663,98.2521
Jakarta (UTC+7hours),-5.7773,106.1161
Manila  (UTC+8hours),14.5965,120.9445
"""

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

    print(" %s  (%s) ---> %s (%s , %s) ---> %s (%s)" % (start_time, start_Az, max_time, max_Az, max_Alt, end_time, end_Az))

observe_cities = []
obs = ephem.Observer()
sun = ephem.Sun()

obj = tle.TleIssNasa()
tles = obj.exec()

for lines in db.strip().split('\n'):
    line = lines.split(',')
    city = str(line[0])
    lat  = str(line[1])
    lon  = str(line[2])
    observe_cities.append([str(city), str(lat), str(lon)])

for city in observe_cities: 
    print("\nLocation:  %s  Lat.= %s Lon.= %s " % (city[0],city[1],city[2]))
    print("  Date   Appear(Deg.)        Max(Alt.)      Set(Deg.)")

    obs.name = str(city[0])
    obs.lat  = str(city[1])
    obs.lon  = str(city[2])

    #obs.date = datetime.now()
    #obs.date -= 9 * ephem.hour #JST -> UTC
    obs.date = "2019/8/1 00:00:00"
    date1 = obs.date

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
                            if (newline):
                                if (results):
                                    show_results(results)

                                results = []
                                newline = False 

                            results.append([obs.date, az, alt])

            newline = True

    if(results):
        show_results(results)
