import numpy as np
import hakata

#実測データの読み込み
#Real tide data Hakata port 2016/07/25
from labo_data.res_160725 import *
real_time = np.arange(0,60*24,5) # 計測は５分間隔
#

# 描画
import pylab as plt
#
plt.plot(real_time,real_level,color='r')  #実測データを赤でプロット

time = np.arange(0,len(hakata.tide),1)
plt.plot(time,hakata.tide,color='b') #予測値を青でプロット

plt.show()
