import numpy as np
import math
import ephem
import datetime
import tle_iss_new as tle
from observe import *
import planisfunc as plf

sun = ephem.Sun()

offset = np.pi /50.

class iss:
    def __init__(self, observe, ax, zo, legend):

        date1 = observe.date

        lines = tle.TleIssNasa().exec()
        iss = ephem.readtle("ISS(ZARYA)", lines[0], lines[1])

        Az = []
        Alt = []
        for min in range(0, 15, 1):
            observe.date = date1
            observe.date += min * ephem.minute
            date2 = observe.date

            for sec in range(0, 60, 5):
                observe.date = date2
                observe.date += sec * ephem.second
                iss.compute(observe)
                iss_alt = float(iss.alt)
                iss_az = float(iss.az)
                sun.compute(observe)
                sun_alt = math.degrees(sun.alt)

                if(iss_alt > 0):
                    if(sun_alt < - 5):
                        if(iss.eclipsed is False):
                            Az.append(iss_az)
                            Alt.append(iss_alt)
                            if ( sec == 0 and legend ):
                                if(math.degrees(iss.alt) > 10):
                                    utc = observe.date + ephem.second
                                    utc = ephem.date(utc)

                                    hour_str = utc.datetime().hour
                                    min_str = utc.datetime().minute

                                    time = str('%02d:%02d:00' % (hour_str,min_str))

                                    x, y = plf.polar(iss_az,iss_alt)
                                    ax.plot(x, y, 'w*', markersize=15)
                                    x += offset
                                    y -= offset
                                    ax.text(x, y, time, color='white',
                                            fontsize=12, alpha=1.0, zorder=zo)

        AZ = np.array(Az)
        ALT = np.array(Alt)
        X,Y = plf.polarXY(AZ, ALT, lim=0)
       
        if (X.any()):
            ax.plot(X, Y, '-', lw=3, color='white', alpha=1.0, zorder=zo)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import sky
    from observe import *

    fig, ax = plt.subplots()

    ax.set_aspect('equal')
    sf = sky.skyfield(obs, ax, zo=0, legend=True)
    ss = iss(obs, ax, zo=1, legend=True)
    ax.axis('off')
    plt.xlim([-np.pi/2, np.pi/2])
    plt.ylim([-np.pi/2, np.pi/2])

    plt.show()
