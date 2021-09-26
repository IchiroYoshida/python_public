import matplotlib.pyplot as plt
import numpy as np
import math
import datetime
import ephem
import sky
import planisfunc as plf

Planet  = ['Mercury','Venus','Mars','Jupiter','Saturn']
PlanetJ = {'Mercury':'水星','Venus':'金星','Mars':'火星','Jupiter':'木星','Saturn':'土星'}

offset = np.pi /50.

class planets:
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

        if (legend):
            observe.date = date0
            observe.date += 30  #Planets position at the end of the month.(30)

            s = [eval('ephem.'+body+'()') for body in Planet]
            [s[i].compute(observe) for i in range(len(s))]

            NAME = np.array(Planet)
            RA = np.array([float(body.ra) for body in s])
            DEC = np.array([float(body.dec) for body in s])

            RA = side - RA

            lat = float(observe.lat)
            AZ, ALT = plf.equatoHori(lat, RA, DEC)
            X, Y, ret = plf.polarXY(AZ, ALT, lim=0, name=NAME)
            NAME = ret['name']

            Y -= offset

            for n in range(len(NAME)):
                nameJ = PlanetJ[NAME[n]]
                ax.text(X[n], Y[n], nameJ, color='white',
                        fontsize=12, alpha=0.9, zorder=zo)

        # Monthly  movement of the planets.
        date0 = str('%4d/%02d/01 %02d:%02d:00' % (year, month, hour, minute))

        for i in range(len(s)):
            if (s[i].name == 'Mercury' or s[i].name == 'Venus'):
                Ra = []
                Dec = []
                for day in range(0, 27, 1):
                    observe.date = date0
                    observe.date += day

                    s[i].compute(observe)

                    ra = float(s[i].ra)
                    dec  = float(s[i].dec)

                    Ra.append(ra)
                    Dec.append(dec)

                RA = np.array(Ra)
                DEC  = np.array(Dec)

                RA = side - RA

                lat = float(observe.lat)
                AZ, ALT = plf.equatoHori(lat, RA, DEC)
                X, Y = plf.polarXY(AZ, ALT, lim=0)

                if (X.any()):
                    ax.plot(X, Y, '-', lw=2, color='red', alpha=1, zorder=zo)

                # quiver (arrow head)
                Ra = []
                Dec = []
                for day in range(26, 32, 5):
                    observe.date = date0
                    observe.date += day

                    s[i].compute(observe)

                    ra = float(s[i].ra)
                    dec  = float(s[i].dec)

                    Ra.append(ra)
                    Dec.append(dec)

                RA = np.array(Ra)
                DEC  = np.array(Dec)

                RA = side -RA

                lat = float(observe.lat)
                AZ, ALT = plf.equatoHori(lat, RA, DEC)
                X, Y = plf.polarXY(AZ, ALT, lim=0)

                if (len(X)>1):
                    x0, x1 = X[0], X[1:][0]
                    y0, y1 = Y[0], Y[1:][0] 
                    dx = x1 - x0
                    dy = y1 - y0

                    ax.arrow(x0, y0, dx, dy, width=0.01,  color='red', alpha=1, zorder=zo)

            else :     # Mars, Saturn, Jupiter
                Ra = []
                Dec = []
                for day in range(0, 31, 15):
                    observe.date = date0
                    observe.date += day

                    s[i].compute(observe)

                    ra = float(s[i].a_ra)
                    dec  = float(s[i].a_dec)

                    Ra.append(ra)
                    Dec.append(dec)

                RA = np.array(Ra)
                DEC  = np.array(Dec)

                RA = side -RA

                lat = float(observe.lat)
                AZ, ALT = plf.equatoHori(lat, RA, DEC)
                X, Y = plf.polarXY(AZ, ALT, lim=0)

                if (len(X)>1):
                    x0, x1 = X[0], X[1:][0]
                    y0, y1 = Y[0], Y[1:][0] 
                    dx = x1 - x0
                    dy = y1 - y0

                    ax.arrow(x0, y0, dx, dy, width=0.01,  color='red', alpha=1, zorder=zo)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import sky
    import ecliequ
    from observe import *

    fig, ax = plt.subplots()

    ax.set_aspect('equal')
    sf = sky.skyfield(obs,ax,zo=0,legend=True)
    pl = planets(obs,ax,zo=1,legend=True)
    ax.axis('off')
    plt.xlim([-np.pi/2, np.pi/2])
    plt.ylim([-np.pi/2, np.pi/2])

    plt.show()
