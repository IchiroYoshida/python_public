import matplotlib.pyplot as plt
import matplotlib.patches as patches

import numpy as np
import math
import ephem
import planisfunc as plf

class Moon:
    def __init__(self, observe, ax, zo, legend):
        moon = ephem.Moon(observe)

        if (moon.alt >0):
            rr = float(moon.radius) * 10.
            alpha = moon.elong
            side = float(observe.sidereal_time()) # Sidereal Time (Radians)

            pol_x = []
            pol_y = []

            # draw moon shape 
            for th in range(-90, 100, 10):
                th2 = math.radians(th)

                x1 = - rr * math.cos(th2) * math.cos(alpha)
                y2 =   rr * math.sin(th2)

                pol_x.append(x1)
                pol_y.append(y2)

            for th in range(90, -100, -10):
                th2 = math.radians(th)
 
                x2 = - rr * math.cos(th2)
                y2 =   rr * math.sin(th2)

                pol_x.append(x2)
                pol_y.append(y2)

            Pol_X = np.array(pol_x)
            Pol_Y = np.array(pol_y)

            Pol_X += moon.ra 
            Pol_Y += moon.dec

            Pol_X = side - Pol_X

            Pol_AZ, Pol_ALT = plf.equatoHori(observe.lat, Pol_X, Pol_Y)

            Pol_XX, Pol_YY, ret = plf.polarXY(Pol_AZ, Pol_ALT, lim=0)
            
            Pol_XY = np.array([Pol_XX,Pol_YY]).T

            mp = patches.Polygon(Pol_XY, closed=True, alpha=1.0, fc='white', zorder=zo)
            ax.add_patch(mp)

            if (legend):
                text_offset = np.pi/ 50.

                moonAge = observe.date - ephem.previous_new_moon(observe.date)

                MA = str('%3.1f' % moonAge)
                az = np.array(moon.az).reshape(1,)
                alt = np.array(moon.alt).reshape(1,)

                txt_x, txt_y, ret = plf.polarXY(az, alt, lim=0)
                txt_x -= text_offset * 2.5 
                txt_y -= text_offset * 2

                ax.text(txt_x, txt_y, MA, color='white', fontsize=12, alpha=1, zorder=zo)

    
if __name__ == '__main__':
     import matplotlib.pyplot as plt
     import sky
     from observe import *

     fig, ax = plt.subplots()

     ax.set_aspect('equal')
     sf = sky.skyfield(obs, ax, zo=0, legend=True)
     mo = Moon(obs, ax, zo=1,legend=True)
     ax.axis('off')
     plt.xlim(- np.pi/2. , np.pi/2.)
     plt.ylim(- np.pi/2. , np.pi/2.)
     plt.show()
