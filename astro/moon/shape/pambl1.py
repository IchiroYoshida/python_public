"""
Position Angle of the Moon's Bright Limb
Jean Meeus p.61
Example 13.a
"""

import ephem
import math

location = ephem.Observer()

location.name = 'London'
location.lon = '-0.0014'
location.lat = '51.4778'
location.date = '1979/02/02 21:00:00'

sun  = ephem.Sun(location)
moon = ephem.Moon(location)

cs1 = math.cos(sun.g_dec)*math.sin(sun.g_ra - moon.g_ra)
cs2 = math.cos(moon.g_dec)*math.sin(sun.g_dec)
scc = math.sin(moon.g_dec)*math.cos(sun.g_dec)*math.cos(sun.g_ra - moon.g_ra)


kai = math.atan2(cs1, cs2 - scc)
kai_deg = math.degrees(kai)

if (kai_deg < 0): kai_deg += 360

alpha_sun = math.degrees(sun.g_ra)
delta_sun = math.degrees(sun.g_dec)

alpha_moon = math.degrees(moon.g_ra)
delta_moon = math.degrees(moon.g_dec)

print("Sun R.A. = %8.4f Dec. = %8.4f  Moon R.A. = %8.4f Dec. = %8.4f Kai = %8.4f " % ( \
        alpha_sun, delta_sun, alpha_moon, delta_moon, kai_deg ))
