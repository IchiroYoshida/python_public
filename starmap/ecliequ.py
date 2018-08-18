import matplotlib.pyplot as plt
import numpy as np
import math
import ephem

offset = 10 

class ecliEqu:
    
    def __init__(self, observe, ax, zo, legend):

        # -------- 黄道を描く

        ra = []
        dec = []
        for rambda in range(0, 360, 5):
            ram = str(rambda)
            ecl = ephem.Ecliptic(ram, '0')  # 黄道算出
            equ0 = ephem.Equatorial(ecl, epoch='2000')     # 黄道座標を赤道座標に変換
            equ = ephem.FixedBody()
            equ.compute(observe)
            ra.append(equ.a_ra)
            dec.append(equ.a_dec)

        RA  = np.array(ra)
        DEC = np.array(dec)

        X = np.degrees(RA)
        Y = np.degrees(DEC)

        ax.plot(X, Y, c='yellow', linestyle='dashed',alpha=0.5, zorder=zo)

        if(legend):
            txtn = int(len(X)/2)
            ax.text(X[txtn] ,Y[txtn]
                    ,'黄道',fontsize=10, color = 'yellow', alpha = 0.3, zorder= zo)


if __name__ == '__main__':
     import matplotlib.pyplot as plt
     import sky
     from observe import *

     fig, ax = plt.subplots(figsize=(10,4),dpi=100)

     ax.set_aspect('equal')
     sf = sky.skyfield(obs,ax,zo=0)
     ec = ecliEqu(obs,ax,zo=1,legend=True)

     ax.axis('on')
     plt.xlim([0,360])
     plt.ylim([-90,90])

     plt.xticks(np.linspace(0, 360, 25))
     plt.yticks(np.linspace(-90, 90, 13))

     plt.show()
