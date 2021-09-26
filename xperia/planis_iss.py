import matplotlib.pyplot as plt
import numpy as np
import math
import ephem

from observe import *
import milkyway
import sky
import stars
import planets
import constlines
import moon
import ecliequ
import season
import iss

fig, ax = plt.subplots(figsize=(10,10),dpi=100)

ax.set_aspect('equal')
sf = sky.skyfield(obs, ax, zo=0, legend=True)
mi = milkyway.milkyway(obs, ax, zo=1, legend = True)
hi = stars.hip_stars(obs, ax, zo=2, legend=True)
pl = planets.planets(obs, ax, zo=3, legend=True)
cl = constlines.const_line(obs, ax, zo=4, legend=True)
mo = moon.Moon(obs, ax, zo=5, legend=True)
ec = ecliequ.ecliEqu(obs, ax,zo=0,  legend=True)
sl = season.season_line(obs, ax, zo=4, legend=True)
ss = iss.iss(obs, ax, zo=5, legend=True)

ax.axis('off')
plt.show()
