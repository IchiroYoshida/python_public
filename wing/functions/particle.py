#
# 粒子表示
#
from config.init import *
from functions.globals import *

import numpy as np
import functions.nsfunc as ns
#import functions.classShape as shape

from numpy.random import *

class Particle2D(object):
   def __init__(self):
      self.pos = Vector2(0,0)
      self.vel = Vector2(0,0)
      self.col = ''

class Particle(object):
   def __init__(self):
      self.pa = (numP+1)*[]
      self.counts    = 0

      for i in range(0,numP+1):
         self.pa.append(Particle2D())

   def resetParticle2D(self,i):
       self.pa[i].pos.x = 0.01 #左端(left0)からの位置
       if (i % 2 ==0):
          self.pa[i].pos.y = rand()*SIZE_Y/2*.8+SIZE_Y/2
          self.pa[i].col   = "red"
       else:
          self.pa[i].pos.y = SIZE_Y/2-rand()*SIZE_Y/2*.8
          self.pa[i].col   = "blue"

   def initParticle2D(self):
      for i in range(0,numP):
         self.resetParticle2D(i)

   def getVelocityParticle2D(self,pos):
       vel = Vector2(0,0)

       I,J  = 0,0

       for i in range(0,NX):
           if ((i * DX < pos.x) and ((i+1) * DX > pos.x)): 
              I = i
              break
       for j in range(0,NY):
           if ((j * DY < pos.y) and ((j+1) * DY > pos.y)):
              J = j
              break
       a = pos.x / DX - I
       b = pos.y / DY - J
 
       #格子点の速度を線形補間
       vel.x = (1.0 - b) * ((1.0 - a) * VelX[I,J] + a * VelX[I+1,J]) +\
               b * ((1.0 - a) * VelX[I,J+1] + a * VelX[I+1,J+1])

       vel.y = (1.0 - b) * ((1.0 - a) * VelY[I,J] + a * VelY[I+1,J]) +\
               b * ((1.0 - a) * VelY[I,J+1] + a * VelY[I+1,J+1])

       return vel

   def getPosMesh(self,pos):
        I,J = 0,0
        for i in range(0,NX):
            if ((i * DX < pos.x) and ((i+1) * DX > pos.x)):
               I = i
               break
        for j in range(0,NY):
            if ((j * DY < pos.y) and ((j+1) * DY > pos.y)):
               J = j
               break
        return I,J

   def calcParticle2D(self):
      vel = Vector2(0,0)

      for i in range(0,numP):
          po  = Vector2(self.pa[i].pos.x,self.pa[i].pos.y)
          vel = self.getVelocityParticle2D(po)

          x0 = self.pa[i].pos.x
          y0 = self.pa[i].pos.y

          self.pa[i].pos.x += vel.x * deltaT * speedCoef
          self.pa[i].pos.y += vel.y * deltaT * speedCoef

          if (self.pa[i].pos.x > SIZE_X):
             self.resetParticle2D(i)
