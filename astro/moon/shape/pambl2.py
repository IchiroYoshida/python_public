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
location.date = '2019/01/01 00:00:00'

date0 = location.date

for day in range (0, 360):
    location.date = date0 + day

    sun  = ephem.Sun(location)
    moon = ephem.Moon(location)

    cs1 = math.cos(sun.g_dec)*math.sin(sun.g_ra - moon.g_ra)
    cs2 = math.cos(moon.g_dec)*math.sin(sun.g_dec)
    scc = math.sin(moon.g_dec)*math.cos(sun.g_dec)*math.cos(sun.g_ra - moon.g_ra)


    kai = math.atan2(cs1, cs2 - scc) + math.pi
    if (kai < 0): kai += 2*math.pi
    kai_deg = math.degrees(kai)

    print("%s   Kai = %8.4f " % (location.date, kai_deg))
