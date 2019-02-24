
db="""
11767,Polaris
7588,Achernar
21421,Aldebaran
24436,Rigel
24608,Capella
27989,Betelgeuse
30438,Canopus
32349,Sirius
37279,Procyon
37826,Pollux
49669,Regulus
60718,Acrux
62434,Mimosa
65474,Spica
68702,Hadar
69673,Arcturus
71683,Rigil Kent
80763,Antares
91262,Vega
97649,Altair
102098,Daneb
113368,Fomalhaut
"""

import numpy as np
import ephem
import stars as hip
import planisfunc as plf

offset = np.pi /100.

class hip20_nameE:
    def __init__(self, observe, ax, zo, legend):

        nameE = {}
        s = []
        for line in db.split('\n'):
            try:
                hipno  = line.split(',')[0]
                name   = line.split(',')[1]
                nameE[hipno]=name
                starz = hip.star(str(hipno))
                s.append(starz)

            except:
                None
        [s[i].compute(observe) for i in range(len(s))]

        NAME = np.array([body.name for body in s])
        ALT  = np.array([float(body.alt) for body in s])
        AZ   = np.array([float(body.az) for body in s])

        lim = np.pi /12.

        X, Y, ret  = plf.polarXY(AZ, ALT, lim, name=NAME)
        NAME = ret['name']

        X += offset
        Y += offset

        for n in range(len(NAME)):
            name  = nameE[NAME[n]]

            ax.text(X[n], Y[n], name, color='white',
                    fontsize=10, alpha=0.8, zorder=zo )

if __name__ == '__main__':
      import matplotlib.pyplot as plt
      import sky
      from observe import *

      fig, ax = plt.subplots()

      ax.set_aspect('equal')
      sf = sky.skyfield(obs, ax, zo=0, legend=True)
      na = hip20_nameE(obs, ax, zo=1, legend=True)

      plt.xlim(- np.pi/2., np.pi/2.)
      plt.ylim(- np.pi/2., np.pi/2.)

      ax.axis('off')
      plt.show()
