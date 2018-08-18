import matplotlib.pyplot as plt
import numpy as np
import math
import ephem

from observe import *
import milkyway
import sky
import stars
import constlines
import ecliequ

fig, ax = plt.subplots(figsize=(20,12),dpi=100)

ax.set_aspect('equal')
sf = sky.skyfield(obs, ax, zo=0)
#mi = milkyway.milkyway(obs, ax, zo=1, legend=False)
hi = stars.hip_stars(obs, ax, zo=2, legend=True)
#cl = constlines.const_line(obs, ax, zo=4, legend=True)
#ec = ecliequ.ecliEqu(obs, ax,zo=0,  legend=True)

ax.axis('on')
plt.xlim([0,360])
plt.ylim([-90,90])

plt.xticks(np.linspace(0, 360, 25))
plt.yticks(np.linspace(-90, 90, 13))

plt.show()
