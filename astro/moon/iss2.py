import math
import time
from datetime import datetime
import ephem
 
degrees_per_radian = 180.0 / math.pi

home = ephem.Observer()
home.lon = '137.213507'   # +E
home.lat = '36.695933'      # +N
home.elevation = 10. # meters
home.date= '2016/3/21 14:06:40' #JST 23:06

moon=ephem.Moon()

# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
        '1 25544U 98067A   16165.54018716  .00016717  00000-0  10270-3 0  9008',
        '2 25544  51.6441  76.2279 0000507 322.3584  37.7533 15.54548251  4412'
          )

time0=home.date

for  ti in range (300):
      home.date =time0 +  ephem.second/10.*ti
      iss.compute(home)
      moon.compute(home)

      print('Time %f ISS %10.5f-%10.5f | MOON %10.5f-%10.5f' % (home.date,iss.alt,iss.az,moon.alt,moon.az))
