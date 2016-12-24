#
# ダクトのプロット
#
#
import numpy as np
import matplotlib.pyplot as plt
from   matplotlib import mlab,cm

def drawParticleRec(object1,object2,elapseTimeN,img):
   ti = str('%6.3f'% elapseTimeN)
   co = str('%06d'% img)
   title = str(ti+' sec')

   num = len(object1.pa)

   X = np.zeros(num)
   Y = np.zeros(num)
   colors = num*[]

   for i in range(0,num-1):
      X=np.append(X,object2.left0.x+object1.pa[i].pos.x * object2.scale.x)
      Y=np.append(Y,object2.left0.y+object1.pa[i].pos.y * object2.scale.y)
      colors.append(object1.pa[i].col)

   import matplotlib.pyplot as plt

   fig,ax = plt.subplots()

   plt.axis([0,object2.size.x,0,object2.size.y])
   plt.title('Particles'+title)
   filename=str('./out/img'+co+'.png')
   plt.scatter(X,Y,c=colors,s=object1.sizeP,edgecolors=colors)
   ax.add_patch(plt.Rectangle(xy=[object2.x11,object2.y11],
         width=object2.obs_width, height=object2.obs_height, edgecolor='g',facecolor='yellow'))
   ax.add_patch(plt.Rectangle(xy=[object2.x21,object2.y21],
         width=object2.obs_width, height=object2.obs_height, edgecolor='g',facecolor='yellow'))
   plt.savefig(filename)
