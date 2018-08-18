import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import ephem

mpl.rc('font', family='Noto Sans CJK JP')
mpl.rcParams['font.weight'] = 'bold'

class skyfield:
    def __init__(self,obs, ax, zo):

        ti = ephem.Date(obs.date)
        ax.grid(color='white',linestyle=':')
        ax.text(120, 95, ti, color = 'k',
            fontsize=15, alpha = 1.0, zorder=zo)

        ax.patch.set_facecolor('#191970')
            

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    from observe import *

    fig, ax = plt.subplots(figsize=(10,4),dpi=100)

    ax.set_aspect('equal')
    sf = skyfield(obs, ax, zo=0)
    ax.axis('on')

    plt.xlim([0,360])
    plt.ylim([-90,90])

    plt.xticks(np.linspace(0, 360, 25))
    plt.yticks(np.linspace(-90, 90, 13))

    plt.show()
