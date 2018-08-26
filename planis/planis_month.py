import matplotlib.pyplot as plt
import numpy as np
import math
import ephem
import datetime

from observe import *
import milkyway
import sky
import stars
import planets_month
import constlines
import moon_month
import ecliequ
import season

d = obs.date

year = d.datetime().year
month = d.datetime().month

date0 = str('%4d/%02d/07 12:00:00' % (year,month))   #UTC -> JST 21:00:00
obs.date = date0

fig, ax = plt.subplots(figsize=(10,10),dpi=100)

ax.set_aspect('equal')

obs.date = date0
sf = sky.skyfield(obs, ax, zo=0, legend=True)
mi = milkyway.milkyway(obs, ax, zo=1, legend = True)
hi = stars.hip_stars(obs, ax, zo=2, legend=True)
cl = constlines.const_line(obs, ax, zo=4, legend=True)
ec = ecliequ.ecliEqu(obs, ax,zo=0,  legend=True)
sl = season.season_line(obs, ax, zo=4, legend=True)

obs.date = date0
pl = planets_month.planets(obs, ax, zo=3, legend=True)
obs.date = date0
mo = moon_month.Moon(obs, ax, zo=5, legend=True)
ax.axis('off')
plt.show()
