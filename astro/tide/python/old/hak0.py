import numpy as np
import hakata


# 描画
import pylab as plt

time = np.arange(0,len(hakata.tide),1)
plt.plot(time,hakata.tide,color='b') #予測値を青でプロット

plt.show()
