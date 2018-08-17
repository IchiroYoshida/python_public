import matplotlib.pyplot as plt
import csv
import numpy as np
import math
import ephem
import planisfunc as plf

offset = np.pi / 50.

class ecliEqu:
    
    def __init__(self, observe, ax, zo, legend):

        lim = 0

        # -------- 赤道を描く

        alt = []
        az = []
        for alpha in range(0, 360, 5):
            al = math.radians(alpha)
            equ0 = ephem.Equatorial(al, 0., epoch='2000')
            equ = ephem.FixedBody()
            equ._ra = equ0.ra
            equ._dec = equ0.dec
            equ.compute(observe)
            alt.append(equ.alt)
            az.append(equ.az)

        ALT = np.array(alt)
        AZ  = np.array(az)

        X, Y = plf.polarXY(AZ, ALT, lim)

        for i in range(1,len(X)):
            dx = math.fabs(X[i]-X[i-1])
            dy = math.fabs(Y[i]-Y[i-1])
            if(dx > math.pi/4 or dy > math.pi/4):
                X = np.roll(X, -i)
                Y = np.roll(Y, -i)

        ax.plot(X, Y, c='white', linestyle='dashed',alpha=0.3, zorder=zo)

        if(legend):
            txtn = int(len(X)/2)
            ax.text(X[txtn] ,Y[txtn]
                    ,'赤道',fontsize=10, color = 'white',alpha = 0.3, zorder= zo)

        # -------- 黄道を描く

        alt = []
        az = []
        for rambda in range(0, 360, 5):
            ram = str(rambda)
            ecl = ephem.Ecliptic(ram, '0')  # 黄道算出
            equ0 = ephem.Equatorial(ecl, epoch='2000')     # 黄道座標を赤道座標に変換
            equ = ephem.FixedBody()
            equ._ra = equ0.ra
            equ._dec = equ0.dec
            equ.compute(observe)
            alt.append(equ.alt)
            az.append(equ.az)

        ALT = np.array(alt)
        AZ  = np.array(az)

        X, Y = plf.polarXY(AZ, ALT, lim)

        for i in range(1,len(X)):
            dx = math.fabs(X[i]-X[i-1])
            dy = math.fabs(Y[i]-Y[i-1])
            if(dx > math.pi/4 or dy > math.pi/4):
                X = np.roll(X, -i)
                Y = np.roll(Y, -i)

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

