
db="""
11767,北極星
7588,アケルナル
21421,アルデバラン
24436,リゲル
24608,カペラ
27989,ベテルギウス
30438,カノープス
32349,シリウス
37279,プロキオン
37826,ポルックス
49669,レグルス
60718,アクルックス
62434,ミモザ
65474,スピカ
68702,ハダル
69673,アルクトゥルス
71683,リジル・ケンタウルス
80763,アンタレス
91262,ベガ
97649,アルタイル
102098,デネブ
113368,フォーマルハウト
"""

import numpy as np
import ephem
import stars as hip
import planisfunc as plf

offset = np.pi /100.

class hip20_nameJ:
    def __init__(self, observe, ax, zo, legend):

        nameJ = {}
        s = []
        for line in db.split('\n'):
            try:
                hipno  = line.split(',')[0]
                name   = line.split(',')[1]
                nameJ[hipno]=name
                starz = hip.star(str(hipno))
                s.append(starz)

            except:
                None
        [s[i].compute(observe) for i in range(len(s))]

        NAME = np.array([body.name for body in s])
        ALT  = np.array([float(body.alt) for body in s])
        AZ   = np.array([float(body.az) for body in s])

        lim = np.pi /12.

        X, Y, ret  = plf.polarXY(AZ, ALT, lim, name=NAME)
        NAME = ret['name']

        X += offset
        Y += offset

        for n in range(len(NAME)):
            name  = nameJ[NAME[n]]

            ax.text(X[n], Y[n], name, color='white',
                    fontsize=10, alpha=0.8, zorder=zo )

if __name__ == '__main__':
      import matplotlib.pyplot as plt
      import sky
      from observe import *

      fig, ax = plt.subplots()

      ax.set_aspect('equal')
      sf = sky.skyfield(obs, ax, zo=0, legend=True)
      na = hip20_nameJ(obs, ax, zo=1, legend=True)

      plt.xlim(- np.pi/2., np.pi/2.)
      plt.ylim(- np.pi/2., np.pi/2.)

      ax.axis('off')
      plt.show()
