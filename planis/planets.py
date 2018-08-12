import matplotlib.pyplot as plt
import numpy as np
import math
import ephem
import sky
import planisfunc as plf

Planet  = ['Sun','Mercury','Venus','Mars','Jupiter','Saturn']
PlanetJ = {'Sun':'太陽','Mercury':'水星','Venus':'金星','Mars':'火星','Jupiter':'木星','Saturn':'土星'}

offset = np.pi /50.

class planets:
    def __init__(self,observe,ax, zo,legend):
        s = []
        for body in Planet:
            s.append(eval('ephem.'+body+'()'))
    
        for i in range(len(s)):
            s[i].compute(observe)
   
        NAME = np.array(Planet)
        ALT = np.array([float(body.alt) for body in s])
        AZ  = np.array([float(body.az) for body in s])
        MAG = np.array([body.mag for body in s])
        SIZE = (5 - MAG) ** 1.5 * 4

        X, Y, ret = plf.polarXY(AZ, ALT, lim=0, name=NAME, size=SIZE)
        NAME = ret['name']
        SIZE = ret['size']

        ax.scatter(X, Y, SIZE, c='red',alpha=0.9, zorder=zo)

        if (legend):
            X += offset
            Y += offset
            for n in range(len(NAME)):
                nameJ = PlanetJ[NAME[n]]
                ax.text(X[n], Y[n], nameJ, color='white',
                        fontsize=12, alpha=0.9, zorder=zo)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import sky
    from observe import *

    fig, ax = plt.subplots()

    ax.set_aspect('equal')
    sf = sky.skyfield(obs,ax,zo=0,legend=True)
    pl = planets(obs,ax,zo=1,legend=True)
    ax.axis('off')
    plt.show()
