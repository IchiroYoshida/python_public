import matplotlib.pyplot as plt
import matplotlib as mpl
import ephem
import numpy as np
import math

offset = np.pi/24.

mpl.rc('font', family='Noto Sans CJK JP')
mpl.rcParams['font.weight'] = 'bold'

class skyfield:
    def __init__(self, observer, ax, zo, legend):
       sun = ephem.Sun()
       sun.compute(observer)

       if (math.degrees(sun.alt) < -10.0):
           circle = plt.Circle(xy=(0, 0),
                   radius=np.pi/2.,fc="#191970",alpha=1.0,zorder=zo)
           ax.add_patch(circle)
            
           if (legend):
               Location = observer.name
               Lon  = '経度：'+str(observer.lon)
               Lat  = '緯度：'+str(observer.lat)
               time = observer.date + 9*ephem.hour #UTC -> JST
               #time = observer.date     # UTC
               ti = ephem.Date(time)

               ax.text(0 - offset, np.pi/2.+offset,'北', color='k',
                   fontsize=15, alpha = 1.0, zorder=zo)
               ax.text(np.pi/2.+offset, 0 - offset,'西', color='k',
                   fontsize=15, alpha = 1.0, zorder=zo)
               ax.text(0 - offset, - np.pi/2. -offset,'南', color='k',
                   fontsize=15, alpha = 1.0, zorder=zo)
               ax.text(-np.pi/2. -2*offset, 0 - offset,'東', color='k',
                   fontsize=15, alpha = 1.0, zorder=zo)

               ax.text(-np.pi/2 - offset, + np.pi/2 + offset,Location, color='k',
                   fontsize=15, alpha = 1.0, zorder=zo)
               ax.text( 5*offset, + np.pi/2,ti, color='k',
                   fontsize=15, alpha = 1.0, zorder=zo)
               ax.text(-np.pi/2 - offset, + np.pi/2 - offset, Lon, color='k',
                   fontsize=10, alpha=1.0, zorder=zo)
               ax.text(-np.pi/2 - offset, + np.pi/2 - 2*offset, Lat, color='k',
                   fontsize=10, alpha=1.0, zorder=zo)
       else:
           print('Sun.alt > -15')
           exit 

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    from observe import *

    fig, ax = plt.subplots()

    ax.set_aspect('equal')
    sf = skyfield(obs, ax, zo=0, legend=True)
    ax.axis('off')
    plt.xlim([-np.pi/2.-3*offset,np.pi/2.+3*offset])
    plt.ylim([-np.pi/2.-3*offset,np.pi/2.+3*offset])

    plt.show()
