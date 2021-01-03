import math
import ephem
from iss_tle import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

obs = ephem.Observer()

date0 = '2019/3/23'

m = Basemap()

m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')
m.drawcoastlines()

lats = []
lons = []
#for hour in range(0, 24, 1):
for hour in range(10, 11, 1):
    obs.date = date0
    obs.date += hour * ephem.hour
    date1 = obs.date
    #for min in range(0, 60, 1):
    for min in range(0, 10, 1):
        obs.date = date1
        obs.date += min * ephem.minute
        iss.compute(obs)
        lats.append(math.degrees(iss.sublat))
        lons.append(math.degrees(iss.sublong))

x, y = m(lons, lats)
m.plot(x, y, 'mo', markersize=2)

#m.plot(x, y, color='m', marker='o', markersize=3)
#m.plot(x, y, marker=None, color='m', markersize=1)

plt.show()
