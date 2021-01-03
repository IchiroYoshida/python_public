import numpy as np
import hakata

#実測データの読み込み
#Real tide data Hakata port 2016/07/21
from res_160721 import *
real_time = np.arange(0,60*24,5) # 計測は５分間隔
#

# 気象庁(2016/07/21) 博多
from JMA_160721 import *
jma_time  = np.arange(0,60*24,60) #１時間毎

# 描画
import pylab as plt
#
plt.plot(real_time,real_level,color='r')  #実測データを赤でプロット
plt.plot(jma_time ,jma       ,'go') #気象庁予測値を緑でプロット

time = np.arange(0,len(hakata.tide),1)
plt.plot(time,hakata.tide,color='b') #予測値を青でプロット

plt.scatter(np.array(hakata.hitide)[:,0], np.array(hakata.hitide)[:,1],s=100,marker='*',color='g')
plt.scatter(np.array(hakata.lowtide)[:,0], np.array(hakata.lowtide)[:,1],s=100,marker='o',color='m')

print (hakata.hitide,hakata.lowtide)

plt.show()
