#
# ダクトのプロット
#
#
import numpy as np
import matplotlib.pyplot as plt
from   matplotlib import mlab,cm

def drawMap(object):
   import matplotlib.pyplot as plt

   fig,ax = plt.subplots()

   plt.axis([0,object.size.x,0,object.size.y])
   plt.title('Map')
   plt.gca().set_aspect('equal',adjustable='box')


   for i in range(1,object.NX):
      for j in range(1,object.NY):
          if (object.Map[i,j]):
             ax.add_patch(plt.Rectangle(xy=[i*object.DX,j*object.DY],
                width=object.DX, height=object.DY, edgecolor='g',facecolor='g'))

   plt.show()
 
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
   plt.gca().set_aspect('equal',adjustable='box')

   plt.title('Particles'+title)
   filename=str('./out/img'+co+'.png')
   plt.scatter(X,Y,c=colors,s=object1.sizeP,edgecolors=colors)

   for i in range(1,object2.NX):
      for j in range(1,object2.NY):
          if (object2.Type[i,j]):
             ax.add_patch(plt.Rectangle(xy=[i*object2.DX,j*object2.DY],
                width=object2.DX, height=object2.DY, edgecolor='g',facecolor='g'))

   plt.savefig(filename)

def PlotStreamRec(self,time,img):
    ti=str('%6.3f'% time)
    co=str('%06d'% img)

    fig, ax = plt.subplots()
    plt.gca().set_aspect('equal',adjustable='box')

    X = np.linspace(0,self.size.x-self.DX,self.NX)
    Y = np.linspace(0,self.size.y-self.DY,self.NY)

    Vx=self.VelY[:-1,:-1].transpose()
    Vy=self.VelX[:-1,:-1].transpose()
 
    S=np.sqrt(Vx*Vx+Vy*Vy)
    lw = 2*S/S.max()

    ax.streamplot(X,Y,Vy,Vx, color='b', density=1, linewidth=lw)
   
    for i in range(1,self.NX):
       for j in range(1,self.NY):
           if (self.Type[i,j]):
              ax.add_patch(plt.Rectangle(xy=[i*self.DX,j*self.DY],
                width=self.DX, height=self.DY, edgecolor='g',facecolor='g'))
    
    title =str(ti+' sec')

    plt.axis([0,self.size.x,0,self.size.y])
    plt.title('Stream lines '+title)
    filename=str('./out/img'+co+'.png')
    plt.savefig(filename)

def PlotQuiverVelRec(self,time,img):
    F = 3
    ti=str('%6.3f'% time)
    co=str('%06d'% img)

    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    plt.gca().set_aspect('equal',adjustable='box')

    x = np.arange(0.,self.size.x,self.DX)
    y = np.arange(0.,self.size.y,self.DY)

    X, Y = np.meshgrid(x,y)

    Vx   = self.VelX[:-1,:-1].transpose()
    Vy   = self.VelY[:-1,:-1].transpose()

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
    ax.quiver(X[::F, ::F],Y[::F, ::F],Vx[::F, ::F]*lw, Vy[::F, ::F]*lw,
            pivot='mid',color='black')

    for i in range(1,self.NX):
       for j in range(1,self.NY):
           if (self.Map[i,j]):
              ax.add_patch(plt.Rectangle(xy=[i*self.DX,j*self.DY],
                width=self.DX, height=self.DY, edgecolor='g',facecolor='g'))

    title =str(ti+' sec')

    plt.axis([0,self.size.x,0,self.size.y])
    plt.title('Vel. '+title)
    filename=str('./out/img'+co+'.png')
    plt.savefig(filename)
