# """
# GPS sattelite tracking in Python using pyEphem
#
#
import numpy as np
import pylab as plt
import ephem
import datetime
#from datetime import datetime
# Setup lat long of telescope
oxford = ephem.Observer()
oxford.lat = np.deg2rad(51.75)
oxford.long = np.deg2rad(-1.259)
oxford.date = datetime.datetime.now()
# Load Satellite TLE data.

#l1 = 'GPS-BIIF-1'
#l2 = '1 36585U 10022A   12102.71732698 -.00000026  00000-0  10000-3 0  7813'
#l3 = '2 36585  55.4685  55.7745 0013418  26.7546 333.2981  2.00556192 13724' 

l1 = 'ISS (ZARYA)'             
l2 = '1 25544U 98067A   15070.56770882  .00012045  00000-0  18273-3 0  9992'
l3 = '2 25544  51.6461 211.6443 0008831  89.8543   2.0120 15.55021160932840'

biif1 = ephem.readtle(l1,l2,l3)

# Make some datetimes
midnight = datetime.datetime.replace(datetime.datetime.now(), hour=0)
dt  = [midnight + datetime.timedelta(minutes=20*x) for x in range(0, 24*3)]

# Compute satellite locations at each datetime
sat_alt, sat_az = [], []
for date in dt:
    oxford.date = date
    biif1.compute(oxford)
    sat_alt.append(np.rad2deg(biif1.alt))
    sat_az.append(np.rad2deg(biif1.az))
# Plot satellite tracks
plt.subplot(211)
plt.plot(dt, sat_alt)
plt.ylabel("Altitude (deg)")
plt.xticks(rotation=25)
plt.subplot(212)
plt.plot(dt, sat_az)
plt.ylabel("Azimuth (deg)")
plt.xticks(rotation=25)
plt.show()

# Plot satellite track in polar coordinates
plt.polar(np.deg2rad(sat_az), 90-np.array(sat_alt))
plt.ylim(0,90)
plt.show()

