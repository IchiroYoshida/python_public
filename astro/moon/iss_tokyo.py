import math
import time
from datetime import datetime
import ephem
 
degrees_per_radian = 180.0 / math.pi

home = ephem.Observer()
#Tokyo 
home.lon = '139.70'   # +E
home.lat = '35.69'      # +N
home.elevation = 10. # meters
home.date= '2016/6/16 10:54:30' #JST 19:54

# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
        '1 25544U 98067A   16165.54018716  .00016717  00000-0  10270-3 0  9008',
        '2 25544  51.6441  76.2279 0000507 322.3584  37.7533 15.54548251  4412'
          )

time0=home.date

for  ti in range (300):
      home.date =time0 +  ephem.second*ti
      iss.compute(home)

      alt=iss.alt*degrees_per_radian
      az =iss.az*degrees_per_radian

      print('Time %s ISS %10.5f-%10.5f ' % (home.date,alt,az))
