import math
import numpy as np
import ephem
from datetime import datetime
#from iss_tle import *
import tle_iss_nasa as tle
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from observe import *

obj = tle.TleIssNasa()
tles = obj.exec()

utc_time = obs.date.datetime()
lines = tle.tle_utc(utc_time, tles)
iss = ephem.readtle("ISS(ZARYA)", lines[0], lines[1])


fig = plt.figure(figsize=(8,10))

m = Basemap(projection='merc',
            resolution='h',
            llcrnrlon=122,
            llcrnrlat=23,
            urcrnrlon=160,
            urcrnrlat=47)

m.drawcoastlines(color='lightgray')
m.drawcountries(color='lightgray')
m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary(fill_color='aqua')
m.drawparallels(np.arange(23.0, 47.1, 2.0), labels = [1,0,0,0],fontsize=12)
m.drawmeridians(np.arange(122, 160.1, 2.0), labels = [0,0,0,1],fontsize=12)

date1 = obs.date

lats = []
lons = []

for min in range(0, 10, 1):
    obs.date = date1
    obs.date += min * ephem.minute
    date2 = obs.date
    for sec in range(0, 60, 5):
        obs.date=date2
        obs.date += sec * ephem.second
        iss.compute(obs)
        lats.append(math.degrees(iss.sublat))
        lons.append(math.degrees(iss.sublong))
    #print(lons, lats)

x, y = m(lons, lats)
m.plot(x, y, 'mo', markersize=2)

plt.show()
