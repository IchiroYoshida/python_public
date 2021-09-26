import matplotlib.pyplot as plt
import matplotlib.patches as patches

import numpy as np
import math
import datetime
import ephem
import planisfunc as plf

class Moon:
    def __init__(self, observe, ax, zo, legend):
        d = observe.date
        year = d.datetime().year
        month = d.datetime().month
        hour = d.datetime().hour
        minute = d.datetime().minute

        date0 = str('%4d/%02d/01 %02d:%02d:00' % (year, month, hour, minute))
        date_star = str('%4d/%02d/07 %02d:%02d:00' % (year, month, hour, minute))
        observe.date = date_star
        side = float(observe.sidereal_time()) # Sidereal Time (Radians)
       
        observe.date = date0
        moon = ephem.Moon(observe)

        for m_day in range(0, 30, 1):
            observe.date = date0
            observe.date += m_day
            moon.compute(observe)

            if (moon.alt >0):
                rr = float(moon.radius) * 10.
                alpha = moon.elong
                kai = plf.moon_Pangle(observe)

                pol_x = []
                pol_y = []

                # draw moon shape 
                for th in range(-90, 100, 10):
                    th2 = math.radians(th)

                    x0 = - math.cos(th2) * math.cos(alpha)
                    y0 =   math.sin(th2)
                    x1 =   math.cos(kai)*x0 - math.sin(kai)*y0
                    y1 =   math.sin(kai)*x0 + math.cos(kai)*y0
                    x2 =   rr * (x1 + 1)
                    y2 =   rr * (y1 + 1)

                    pol_x.append(x2)
                    pol_y.append(y2)

                for th in range(90, -100, -10):
                    th2 = math.radians(th)

                    x0 = - math.cos(th2)
                    y0 =   math.sin(th2)
                    x1 =   math.cos(kai)*x0 - math.sin(kai)*y0
                    y1 =   math.sin(kai)*x0 + math.cos(kai)*y0
                    x2 =   rr * (x1 + 1)
                    y2 =   rr * (y1 + 1)

                    pol_x.append(x2)
                    pol_y.append(y2)

                Pol_X = np.array(pol_x)
                Pol_Y = np.array(pol_y)

                Pol_X += moon.ra 
                Pol_Y += moon.dec

                Pol_X = side - Pol_X

                lat = float(observe.lat)
                Pol_AZ, Pol_ALT = plf.equatoHori(lat, Pol_X, Pol_Y)
                Pol_XX, Pol_YY = plf.polarXY(Pol_AZ, Pol_ALT, lim=0)

                if(Pol_XX.any()):
                    Pol_XY = np.array([Pol_XX,Pol_YY]).T

                    mp = patches.Polygon(Pol_XY, closed=True, alpha=1.0, fc='white', zorder=zo)
                    ax.add_patch(mp)

                if (legend):
                    text_offset = np.pi/ 50.

                    d = observe.date
                    MA  = str('%2d' % d.datetime().day)
                    az = np.array(moon.az).reshape(1,)
                    alt = np.array(moon.alt).reshape(1,)

                    txt_x, txt_y = plf.polarXY(az, alt, lim=0)
                    txt_x -= text_offset * 2.5 
                    txt_y -= text_offset * 2
                    
                    if(txt_x):
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
