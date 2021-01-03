import numpy as np
import day2 

# 描画
import pylab as plt
#

time = np.arange(0,len(day2.tide),1)
plt.plot(time,day2.tide,color='b') #天文潮位を青でプロット
plt.plot(time,day2.tidem2,color='r') #M2分潮を赤でプロット
plt.plot(time,day2.tides2,color='m') #S2
plt.plot(time,day2.tidem2s2,color='g')

plt.show()
