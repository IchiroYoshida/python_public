# Sun rise 2018-01-01  Time -> Positions (JAPAN)
# Inverse of the sunrise equation - finding locations with a given sunrise time on a given day.

from datetime import datetime
# from time import strptime

# JAPAN Area. E:120 - 135  N: 20 - 46

import ephem
import numpy as np
import scipy.optimize as spo

from myjavas import PrnJavaScript

position = ephem.Observer()
sun = ephem.Sun()

time0 = '2018-01-01 6:47:49'    #JST 


trise = ephem.Date(time0)- 9 * ephem.hour               #UT = JST -9hr

def sun_alt(lon, lat, t):
    position.lon, position.lat = str(lon), str(lat)
    position.date = t
    sun.compute(position)

    return (sun.alt)


# Find position where sunrise.

lats = np.linspace(20, 46 , 27)

longis = []
lons = []
lon0 = 135.

for lat in lats:

       answer, info = spo.brentq(sun_alt, lon0-90, lon0+90,
                                 args=(lat, trise),
                                 full_output = True )

       if info.converged:
           lons.append(answer)
           #print(lat,answer)

       else:
           lons.append(None)

       lons = [(lon+180)%360.-180 for lon in lons] # wraparound at +/1 180

       longis.append(lons)

PrnJavaScript("sunrise.js",lats,lons)

