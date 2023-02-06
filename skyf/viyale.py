'''
Viyaleta Apgar, Oct 14, 2022
I Made a Sky Map in Python.
This tutorial shows you how to create a sky map /
chart in Python using skyfield library
'''

# datetime libraries
from datetime import datetime
from geopy import Nominatim
from tzwhere import tzwhere
from pytz import timezone, utc
# matplotlib to help display our star map
import matplotlib.pyplot as plt
# skyfield for star data 
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection

# de421 shows position of earth and sun in space
eph = load('de421.bsp')
# hipparcos dataset contains star location data
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

location = 'Times Square, New York, NY'
when = '2023-01-01 00:00'

locator = Nominatim(user_agent='myGeocoder')
location = locator.geocode(location)
lat, long = location.latitude, location.longitude

# convert date string into datetime object
dt = datetime.strptime(when, '%Y-%m-%d %H:%M')
# define datetime and convert to utc based on our timezone
timezone_str = tzwhere.tzwhere().tzNameAt(lat, long)
local = timezone(timezone_str)
# get UTC from local timezone and datetime
local_dt = local.localize(dt, is_dst=None)
utc_dt = local_dt.astimezone(utc)

# find location of earth and sun and set the observer position
sun = eph['sun']
earth = eph['earth']
# define observation time from our UTC datetime
ts = load.timescale()
t = ts.from_datetime(utc_dt)
# define an observer using the world geodetic system data
observer = wgs84.latlon(latitude_degrees=lat, longitude_degrees=long).at(t)
position = observer.from_altaz(alt_degrees=90, az_degrees=0)

ra, dec, distance = observer.radec()
center_object = Star(ra=ra, dec=dec)

center = earth.at(t).observe(center_object)
projection = build_stereographic_projection(center)

star_positions = earth.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projection(star_positions)

chart_size = 10
max_star_size = 100
limiting_magnitude = 10
bright_stars = (stars.magnitude <= limiting_magnitude)
magnitude = stars['magnitude'][bright_stars]

fig, ax = plt.subplots(figsize=(chart_size, chart_size))
 
border = plt.Circle((0, 0), 1, color='navy', fill=True)
ax.add_patch(border)

marker_size = max_star_size * 10 ** (magnitude / -2.5)

ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars],
 s=marker_size, color='white', marker='.', linewidths=0, 
 zorder=2)

horizon = Circle((0, 0), radius=1, transform=ax.transData)
for col in ax.collections:
    col.set_clip_path(horizon)
    
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.axis('off')
plt.show()