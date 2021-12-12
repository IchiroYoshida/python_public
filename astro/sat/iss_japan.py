'''
   ISS track around Japan
   2021-12-21 Ichiro Yoshida
'''
import math
import numpy as np
import ephem
from datetime import datetime
import tle_iss_celestrak as tle
import folium
from observe import *

gsi_tile = "https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png"

tles = tle.TleISS()

folium_map = folium.Map(location=[35.7, 139.7],tiles=gsi_tile, attr='国土地理院地図', zoom_start=5)

iss = ephem.readtle("ISS(ZARYA)", tles[1], tles[2])

date1 = obs.date

Iss_positions = [[0]*2 for i in range(10*12)]

for min in range(0, 10, 1):
    obs.date = date1
    obs.date += min * ephem.minute
    date2 = obs.date
    for sec in range(0, 60, 5):
        obs.date=date2
        obs.date += sec * ephem.second
        iss.compute(obs)
        
        iss_lat =math.degrees(iss.sublat)
        iss_lon =math.degrees(iss.sublong)
        iss_pos = [iss_lat, iss_lon]
        Iss_positions.append(iss_pos)
        del Iss_positions[0]
        
Iss_line = folium.vector_layers.PolyLine(Iss_positions, color='blue', weight=3)

folium_map.add_child(Iss_line)

folium_map.save('ISS20211210.html')

