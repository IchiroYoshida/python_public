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

co = 0

for yr in range(1, 600001, 1000):
    date1 = str(yr)
    print(date1)

    obs.date = date1
    obs.epoch = '2000'
    #obs.epoch = obs.date
    co +=1

    count = str('%06d' % co)
    filename = str('./out/'+count+'.png')

    fig, ax = plt.subplots(figsize=(20,12),dpi=100)

    ax.set_aspect('equal')
    sf = sky.skyfield(obs, ax, zo=0)
    #mi = milkyway.milkyway(obs, ax, zo=1, legend=False)
    hi = stars.hip_stars(obs, ax, zo=2, legend=True)
    cl = constlines.const_line(obs, ax, zo=4, legend=True)
    ec = ecliequ.ecliEqu(obs, ax,zo=0,  legend=True)

    ax.axis('on')
    plt.xlim([0,360])
    plt.ylim([-90,90])

    plt.xticks(np.linspace(0, 360, 25))
    plt.yticks(np.linspace(-90, 90, 13))

    plt.savefig(filename)
    plt.close(fig)
