import numpy as np
import day 

# 描画
import pylab as plt
#

time = np.arange(0,len(day.tide),1)
plt.plot(time,day.tide,color='b') #天文潮位を青でプロット
plt.plot(time,day.tidem2,color='r') #M2分潮を赤でプロット
plt.show()
