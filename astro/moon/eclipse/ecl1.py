import ephem
import math
from operator import itemgetter

def check_non_zero(x):
    return x > 0

def rnd2pi(x):
    return(x - math.floor(x /2*math.pi)*2*math.pi)

# Location
gatech = ephem.Observer()
gatech.lon, gatech.lat = '33.593', '130.390' #Fukuoka
gatech.date ='2018/07/28 3:00:00' #JST
gatech.date -= 9*ephem.hour #JST -> UT
timetuple = gatech.date

# Objects
sun, moon = ephem.Sun(), ephem.Moon()

# Output list
results=[]

for x in range(0,11000):
    gatech.date= (ephem.date(ephem.date(timetuple)+x*ephem.second))
    sun.compute(gatech)
    moon.compute(gatech)
    s_ra  = sun.ra + ephem.pi
    s_dec = - sun.dec
    sep = ephem.separation((s_ra,s_dec), (moon.ra, moon.dec))
    rr  = 0.76 * math.atan(ephem.earth_radius/moon.earth_distance)

    print('x = %d sep =  %f  rr = %f |  Sun = %f %f Moon = %f %f'%(x,sep,rr,s_ra,s_dec,moon.ra,moon.dec))

    #r_sun=sun.size/2
    #r_moon=moon.size/2
    #s=math.degrees(ephem.separation((sun.az, sun.alt), (moon.az, moon.alt)))*60*60
