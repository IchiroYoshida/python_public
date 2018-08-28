"""
Seasonaly events of the stars.
"""

events="""
春の大曲線,67301,69673,65474
春の大三角,69673,65474,57632,69673
夏の大三角,102098,97649,91262,102098
秋の四辺形,113963,113881,677,1067,113963
冬の大三角,32349,37279,27989,32349
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import ephem
import stars as hip
import planisfunc as plf

class season_line:
    def __init__(self, observe, ax, zo, legend):
  
        EventName = []
        Event1 = []
        Event2 = []

        for event in events.split('\n'):
            try:
                if (event):
                    name = event.split(',')[0]
                    EventName.append(name)

                    hips = event.split(',')[1::]

                    while(len(hips)>1):
                        starz1 = hip.star(hips[0])
                        starz2 = hip.star(hips[1])
                        Event1.append(starz1)
                        Event2.append(starz2)
                        del hips[0]

            except:
                None

        [Event1[i].compute(observe) for i in range(len(Event1))]
        [Event2[i].compute(observe) for i in range(len(Event2))]

        AZ1  = np.array([float(body.az) for body in Event1])
        ALT1 = np.array([float(body.alt) for body in Event1])
        AZ2  = np.array([float(body.az) for body in Event2])
        ALT2 = np.array([float(body.alt) for body in Event2])

        lim = np.pi /72.

        AZ3  = AZ1[np.where((ALT1 > lim) & (ALT2 > lim))]
        ALT3 = ALT1[np.where((ALT1 > lim) & (ALT2 > lim))]
        AZ4  = AZ2[np.where((ALT1 > lim) & (ALT2 > lim))]
        ALT4 = ALT2[np.where((ALT1 > lim) & (ALT2 > lim))]

        X1, Y1 = plf.polarXY(AZ3, ALT3, lim)
        X2, Y2 = plf.polarXY(AZ4, ALT4, lim)

        for i in range(len(X1)):
            plt.plot([X1[i], X2[i]],[Y1[i], Y2[i]], 'y:', alpha = 1, zorder = zo)

        if(legend):
            
            Name= []
            Events= []
            for event in events.split('\n'):
                try:
                    if (event):
                        name = event.split(',')[0]
                        Name.append(name)

                        hips = event.split(',')[1::]
                        Events.append(hips)

                except:
                    None

            for i in range(len(Name)):
                Event = [hip.star(Events[i][j]) for j in range(len(Events[i]))]
                [Event[j].compute(observe) for j in range(len(Event))]

                AZ  = np.array([float(body.az) for body in Event])
                ALT = np.array([float(body.alt) for body in Event])

                lim = np.pi /72.

                AZ  = AZ[np.where(ALT > lim)]
                ALT = ALT[np.where(ALT > lim)]

                X, Y = plf.polarXY(AZ, ALT, lim)
                
                if(X.any()):
                    Xtxt = np.mean(X)
                    Ytxt = np.mean(Y)

                    ax.text(Xtxt, Ytxt, Name[i], fontsize =12, color = 'y', alpha = 1, zorder = zo) 

if __name__=='__main__':
    import matplotlib.pyplot as plt
    import sky
    from observe import *
 
    fig, ax = plt.subplots()
 
    ax.set_aspect('equal')
    sf = sky.skyfield(obs, ax, zo=0, legend=True)
    sl = season_line(obs, ax, zo=0, legend=True)
    ax.axis('off')
    plt.show()
