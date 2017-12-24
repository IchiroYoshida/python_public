# Sun rise 2018-01-01  Time -> Positions (JAPAN)
# Inverse of the sunrise equation - finding locations with a given sunrise time on a given day.

from datetime import datetime
import ephem
import numpy as np
import scipy.optimize as spo
from myjavas import PrnJavaScript

DegRad = ephem.pi / 180.

position = ephem.Observer()

position.pressure = 0
position.horizon = '-0:34'
position.elevation = 0.0

sun = ephem.Sun()

#time0 = '2018-01-01 6:51:00'    #Inubousaki JST 
time0 = '2018-01-01 7:30:41.5'  #Shiraho

trise = ephem.Date(time0)- 9.  * ephem.hour               #UT = JST -9hr

def sun_alt(lon, lat, t):
    position.lon, position.lat = str(lon), str(lat)
    position.date = t
    sun.compute(position)

    sun_size_rad = DegRad * float(sun.radius) / 3600.  # Sun apparent radius in radians.
    sun_apparent0 = float(sun.alt) + sun_size_rad  # Add Sun apparent radius in radians. 
    #sun_apparent0 = float(sun.alt)

    return (sun_apparent0)

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
       else:
           lons.append(None)

       lons = [(lon+180)%360.-180 for lon in lons] # wraparound at +/1 180

       longis.append(lons)

PrnJavaScript("sunrise.js",lats,lons)

