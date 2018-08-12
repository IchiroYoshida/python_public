import matplotlib.pyplot as plt
import csv
import numpy as np
import math
import ephem
import planisfunc as plf

offset = np.pi / 50.

class ecliEqu:
    
    def __init__(self, observe, ax, zo, legend):

        side = float(observe.sidereal_time()) #Sidereal Time (Radians)
        the = observe.lat  # 観測地緯度
        lim = np.pi / 36.

        # -------- 赤道を描く

        Ra = []
        Dec = []
        for alpha in range(0, 360, 5):
            al = math.radians(alpha) 
            equ = ephem.Equatorial(al, 0.) # 赤道算出
            Ra.append(equ.ra)
            Dec.append(equ.dec)

        RA  = np.array(Ra)
        DEC = np.array(Dec)

        RA = side - RA  # 赤経を時角に変換

        AZ, ALT = plf.equatoHori(the, RA, DEC)

        X, Y, ret = plf.polarXY(AZ, ALT, lim)

        ax.plot(X, Y, c='white', linestyle='dashed',alpha=0.3, zorder=zo)

        if(legend):
            txtn = int(len(X)/2)
            ax.text(X[txtn] ,Y[txtn]
                    ,'赤道',fontsize=10, color = 'white',alpha = 0.3, zorder= zo)

        # -------- 黄道を描く

        Ra = []
        Dec = []
        for rambda in range(0, 360, 5):
            ram = str(rambda)
            ecl = ephem.Ecliptic(ram, '0')  # 黄道算出
            equ = ephem.Equatorial(ecl)     # 黄道座標を赤道座標に変換
            Ra.append(equ.ra)
            Dec.append(equ.dec)

        RA  = np.array(Ra)
        DEC = np.array(Dec)

        RA = side - RA     # 赤経を時角に変換

        AZ, ALT = plf.equatoHori(the, RA, DEC)

        X, Y, ret  = plf.polarXY(AZ, ALT, lim)

        ax.plot(X, Y, c='yellow', linestyle='dashed',alpha=0.5, zorder=zo)

        if(legend):
            txtn = int(len(X)/2)
            ax.text(X[txtn] ,Y[txtn]
                    ,'黄道',fontsize=10, color = 'yellow', alpha = 0.3, zorder= zo)


if __name__ == '__main__':
     import matplotlib.pyplot as plt
     import sky
     from observe import *

     fig, ax = plt.subplots()
 
     ax.set_aspect('equal')
     sf = sky.skyfield(obs, ax, zo=0, legend=True)
     ec = ecliEqu(obs, ax, zo=1, legend=True)
     ax.axis('off')
     plt.show()

