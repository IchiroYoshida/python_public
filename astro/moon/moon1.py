"""
	Moon and Sun (Pyephem)
"""

import ephem
import math
from operator import itemgetter

def check_non_zero(x):
   return x > 0

#Date
timetuple = (2015, 3, 20, 8, 10, 00)

#Location
gatech = ephem.Observer()
gatech.lon, gatech.lat = '-1.268304', '51.753101' #SBS Oxford
gatech.date = timetuple

#Objects
sun, moon = ephem.Sun(), ephem.Moon()

#Output list
results=[]

for x in range(0,11000):
   gatech.date=(ephem.date(ephem.date(timetuple)+x*ephem.second))
   sun.compute(gatech)
   moon.compute(gatech)
   r_sun=sun.size/2
   r_moon=moon.size/2
   s=math.degrees(ephem.separation((sun.az, sun.alt), (moon.az,moon.alt)))*60*60

#Calculate the size of the lune in arcsec^2
#http://mathworld.wolfram.com/Lune.html

   if s<(r_moon+r_sun):
      lunedelta=0.25*math.sqrt((r_sun+r_moon+s)*(r_moon+s-r_sun)*(s+r_sun-r_moon)*(r_sun+r_moon-s))
   else:   #If s>r_moon+r_sun there is no eclipse taking place
      lunedelta=None
      percent_eclipse=0

   if lunedelta:
      lune_area=2*lunedelta + r_sun*r_sun*(math.acos(((r_moon*r_moon) \
                -(r_sun*r_sun)-(s*s))/(2*r_sun*s))) \
                - r_moon*r_moon*(math.acos(((r_moon*r_moon) \
                + (s*s) - (r_sun*r_sun))/(2*r_moon*s)))

# Calculate percentage of sun`s disc eclipsed using lune area and sun size
      percent_eclipse=(1-(lune_area/(math.pi*r_sun*r_sun)))*100
# Append to list of lists
      results.append([gatech.date.datetime(),s,sun.size,moon.size,lune_area if lunedelta else 0, percent_eclipse])

print(x)


gen=(x for x in results) ### Find Max percentage of eclipse
max_eclipse=max(gen, key=itemgetter(5))

print("Max eclipse at: " + str(max_eclipse[0]))  ### ...and return the time
print("Max percent: " + '%.2f' % max_eclipse[5]) ### ...and return the percentage

gen=(x for x in results)
print("First contact: " + str(next(x for x in gen if check_non_zero(x[5]))[0])) ### Find first contact...
#print("Last contact: " + str(next(x for x in gen if x[5]==0)[0])) ### ... and last contact
