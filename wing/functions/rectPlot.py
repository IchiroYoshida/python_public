#
# ダクトのプロット
#

from config.init import *
from functions.globals import *

import numpy as np
import matplotlib.pyplot as plt
from   matplotlib import mlab,cm

def drawMap(object):
   import matplotlib.pyplot as plt

   fig,ax = plt.subplots()

   plt.axis([0,SIZE_X,0,SIZE_Y])
   plt.title('Map')
   plt.gca().set_aspect('equal',adjustable='box')


   for i in range(1,NX):
      for j in range(1,NY):
          if (Map[i,j]):
             ax.add_patch(plt.Rectangle(xy=[i*DX,j*DY],
                width=DX, height=DY, edgecolor='g',facecolor='g'))

   plt.show()
   plt.close(fig)

def drawParticleRec(object,elapseTimeN,img):
   ti = str('%6.3f'% elapseTimeN)
   co = str('%06d'% img)
   title = str(ti+' sec')

   num = len(object.pa)

   X = np.zeros(num)
   Y = np.zeros(num)
   colors = num*[]

   for i in range(0,num-1):
      X=np.append(X,left0.x+object.pa[i].pos.x * scale.x)
      Y=np.append(Y,left0.y+object.pa[i].pos.y * scale.y)
      colors.append(object.pa[i].col)

   import matplotlib.pyplot as plt

   fig,ax = plt.subplots()

   plt.axis([0,SIZE_X,0,SIZE_Y])
   plt.gca().set_aspect('equal',adjustable='box')

   plt.title('Particles'+title)
   filename=str('./out/img'+co+'.png')
   plt.scatter(X,Y,c=colors,s=sizeP,edgecolors=colors)

   for i in range(1,NX):
      for j in range(1,NY):
          if (Type[i,j]):
             ax.add_patch(plt.Rectangle(xy=[i*DX,j*DY],
                width=DX, height=DY, edgecolor='g',facecolor='g'))

   plt.savefig(filename)
   plt.close(fig)

def PlotStreamRec(self,time,img):
    ti=str('%6.3f'% time)
    co=str('%06d'% img)

    fig, ax = plt.subplots()
    plt.gca().set_aspect('equal',adjustable='box')

    X = np.linspace(0,SIZE_X-DX,NX)
    Y = np.linspace(0,SIZE_Y-DY,NY)

    Vx=VelY[:-1,:-1].transpose()
    Vy=VelX[:-1,:-1].transpose()
 
    S=np.sqrt(Vx*Vx+Vy*Vy)
    lw = 2*S/S.max()

    ax.streamplot(X,Y,Vy,Vx, color='b', density=1, linewidth=lw)
   
    for i in range(1,NX):
       for j in range(1,NY):
           if (Type[i,j]):
              ax.add_patch(plt.Rectangle(xy=[i*DX,j*DY],
                 width=DX, height=DY, edgecolor='g',facecolor='g'))

    title =str(ti+' sec')

    plt.axis([0,SIZE_X,0,SIZE_Y])
    plt.title('Stream lines '+title)
    filename=str('./out/img'+co+'.png')
    plt.savefig(filename)
    plt.close(fig)

def PlotQuiverVelRec(self,time,img):
    ti=str('%6.3f'% time)
    co=str('%06d'% img)

    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    plt.gca().set_aspect('equal',adjustable='box')

    x = np.arange(0.,SIZE_X,DX)
    y = np.arange(0.,SIZE_Y,DY)

    X, Y = np.meshgrid(x,y)

    Vx   = VelX[:-1,:-1:].transpose()
    Vy   = VelY[:-1,:-1:].transpose()

    speed= np.sqrt(Vx*Vx+Vy*Vy)
    levels = np.arange(speed.min(),speed.max()*1.01,0.025)
    norm = cm.colors.Normalize(vmax=speed.max(),vmin=speed.min())

    from matplotlib.colors import LinearSegmentedColormap

    def generate_cmap(colors):
        values = range(len(colors))
        vmax = np.ceil(np.max(values))
        color_list = []
        for v, c in zip(values,colors):
            color_list.append((v/vmax,c))
        return LinearSegmentedColormap.from_list('custom_cmap',color_list)

    cmap2 = generate_cmap(['#0000FF','#00FFFF','#00FF00','#FFFF00','#FF0000'])

    cset1 = ax.contourf(X, Y, speed, levels,
             cmap = cmap2,
             norm=norm,
             )
    cset3 = ax.contour(X, Y, speed, (0,),
            colors='g',
            linewidths=1,
            hold='on')

    lw = 5
    ax.quiver(X[::MF, ::MF],Y[::MF, ::MF],Vx[::MF, ::MF]*lw, Vy[::MF, ::MF]*lw,
            pivot='mid',color='black')

    title =str(ti+' sec')

    plt.axis([0,SIZE_X,0,SIZE_Y])
    plt.title('Vel. '+title)
    filename=str('./out/img'+co+'.png')
    plt.savefig(filename)
    plt.close(fig)
