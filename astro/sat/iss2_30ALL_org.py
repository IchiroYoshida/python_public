import math
import ephem
from operator import itemgetter
from datetime import datetime
import tle_iss_nasa as tle
#from observe import *

"""
観測都市、緯度、経度
"""

db = """
福岡,33.5904,130.4017
東京,35.7090,139.7320
大阪,34.69,135.50
松山,33.85,132.73
那覇,26.2123,127.6792
石垣,24.3321,124.1640
"""

def show_results(results):
    num = len(results)
    # print("num = %d" % num)

    gen = (x for x in results)
    max_alt = max(results, key = itemgetter(2))
    if (max_alt[2] > 30. ):
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

for lines in db.strip().split('\n'):
    line = lines.split(',')
    city = str(line[0])
    lat  = str(line[1])
    lon  = str(line[2])
    observe_cities.append([str(city), str(lat), str(lon)])


lines = tle.TleIssNasa().exec()
iss = ephem.readtle("ISS(ZARYA)",lines[0],lines[1])

for city in observe_cities: 
    print("\nName  %s  Lat.= %s Lon.= %s " % (city[0],city[1],city[2]))
    print("         時刻            出（方位)          最高点（方位、高度）                没（方位）")

    obs.name = str(city[0])
    obs.lat  = str(city[1])
    obs.lon  = str(city[2])

    #sun = ephem.Sun()

    obs.date = datetime.now()
    obs.date -= 9 * ephem.hour #JST -> UTC
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

            newline = True

    if(results):
        show_results(results)
