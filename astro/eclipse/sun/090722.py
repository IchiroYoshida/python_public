#https://www.chromosphere.co.uk/wp-content/blogs.dir/1/files/2015/03/eclipse_percent.py
import ephem
import math
from operator import itemgetter

def check_non_zero(x):
    return x > 0

def lune(s, r_sun, r_moon):

    ## Calculate the size of the lune (http://mathworld.wolfram.com/Lune.html) in arcsec^2
    if s<(r_moon+r_sun):
        lunedelta=0.25*math.sqrt((r_sun+r_moon+s)*(r_moon+s-r_sun)*(s+r_sun-r_moon)*(r_sun+r_moon-s))
    else: ### If s>r_moon+r_sun there is no eclipse taking place
        lunedelta=None
    
    return lunedelta

def percentEclipse(s, r_sun, r_moon):
    lunedelta = lune(s, r_sun, r_moon)

    if lunedelta==None : percent_eclipse = 0

    else :
        lune_area=2*lunedelta \
             + r_sun*r_sun*(math.acos(((r_moon*r_moon)-(r_sun*r_sun)-(s*s))/(2*r_sun*s))) \
             - r_moon*r_moon*(math.acos(((r_moon*r_moon)+(s*s)-(r_sun*r_sun))/(2*r_moon*s)))

        # Calculate percentage of sun's disc eclipsed using lune area and sun size
        percent_eclipse=(1-(lune_area/(math.pi*r_sun*r_sun)))*100 

    return percent_eclipse

# Date
timetuple = (2009, 7, 22, 0, 00, 00)

# Location
gatech = ephem.Observer()
gatech.lon, gatech.lat = '130.198', '33.637' #Keya,Fukuoka, Japan
gatech.date=timetuple

# Objects
sun, moon = ephem.Sun(), ephem.Moon()

# Output list
results=[]

for x in range(0,11000):
    gatech.date= (ephem.date(ephem.date(timetuple)+x*ephem.second))
    sun.compute(gatech)
    moon.compute(gatech)
    r_sun=sun.size/2
    r_moon=moon.size/2
    s=math.degrees(ephem.separation((sun.az, sun.alt), (moon.az, moon.alt)))*60*60
    lunedelta = lune(s, r_sun, r_moon)
    percent_eclipse = percentEclipse(s, r_sun, r_moon)

    results.append([gatech.date.datetime(),s,sun.size,moon.size,lune_area if lunedelta else 0, percent_eclipse]) ### Append to list of lists
gen=(x for x in results) ### Find Max percentage of eclipse...
max_eclipse=max(gen, key=itemgetter(5))
print("Max eclipse at: " + str(max_eclipse[0])) ### ...and return the time
print("Max percent: " + '%.2f' % max_eclipse[5]) ### ...and return the percentage
gen=(x for x in results)
print("First contact: " + str(next(x for x in gen if check_non_zero(x[5]))[0])) # Find first contact...
print("Last contact: " + str(next(x for x in gen if x[5]==0)[0])) ### ...and last contact

