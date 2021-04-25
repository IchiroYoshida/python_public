import math
import ephem

def moon_Pangle(observer):
    sun  = ephem.Sun(observer)
    moon = ephem.Moon(observer)
    cs1 = math.cos(sun.g_dec)*math.sin(sun.g_ra - moon.g_ra)
    cs2 = math.cos(moon.g_dec)*math.sin(sun.g_dec)
    scc = math.sin(moon.g_dec)*math.cos(sun.g_dec)*math.cos(sun.g_ra - moon.g_ra)

    kai = math.atan2(cs1, cs2 - scc)
    if (kai < 0): kai += 2*math.pi

    deg = kai*math.pi/180
    print(deg,kai)
    return(kai)
