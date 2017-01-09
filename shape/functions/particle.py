#
# 粒子表示
#
import numpy as np
import functions.nsfunc as ns
import functions.classShape as shape

from numpy.random import *

class Particle2D(object):
   def __init__(self):
      self.pos = ns.Vector2(0,0)
      self.vel = ns.Vector2(0,0)
      self.col = ''

class Particle(object):
   def __init__(self,object,numP,size,speed):
      self.pa = (numP+1)*[]
      self.numMaxP = numP
      self.sizeP   = size
      self.speedCoef = speed
      self.counts    = 0

      for i in range(0,self.numMaxP+1):
         self.pa.append(Particle2D())

   def resetParticle2D(self,object,i):
       self.pa[i].pos.x = 0.01 #左端(left0)からの位置
       if (i % 2 ==0):
          self.pa[i].pos.y = rand()*object.size.y/2*.8+object.size.y/2
          self.pa[i].col   = "red"
       else:
          self.pa[i].pos.y = object.size.y/2-rand()*object.size.y/2*.8
          self.pa[i].col   = "blue"

   def initParticle2D(self,object):
      for i in range(0,self.numMaxP):
         self.resetParticle2D(object,i)

   def getVelocityParticle2D(self,object,pos):
       vel = ns.Vector2(0,0)

       I,J  = 0,0

       for i in range(0,object.NX):
           if ((i * object.DX < pos.x) and ((i+1) * object.DX > pos.x)): 
              I = i
              break
       for j in range(0,object.NY):
           if ((j * object.DY < pos.y) and ((j+1) * object.DY > pos.y)):
              J = j
              break
       a = pos.x / object.DX - I
       b = pos.y / object.DY - J
 
       #格子点の速度を線形補間
       vel.x = (1.0 - b) * ((1.0 - a) * object.VelX[I,J] + a * object.VelX[I+1,J]) +\
               b * ((1.0 - a) * object.VelX[I,J+1] + a * object.VelX[I+1,J+1])

       vel.y = (1.0 - b) * ((1.0 - a) * object.VelY[I,J] + a * object.VelY[I+1,J]) +\
               b * ((1.0 - a) * object.VelY[I,J+1] + a * object.VelY[I+1,J+1])

       return vel

   def getPosMesh(self,object,pos):
        I,J = 0,0
        for i in range(0,object.NX):
            if ((i * object.DX < pos.x) and ((i+1) * object.DX > pos.x)):
               I = i
               break
        for j in range(0,object.NY):
            if ((j * object.DY < pos.y) and ((j+1) * object.DY > pos.y)):
               J = j
               break
        return I,J

   def calcParticle2D(self,object):
      vel = ns.Vector2(0,0)

      for i in range(0,self.numMaxP):
          po = ns.Vector2(self.pa[i].pos.x,self.pa[i].pos.y)
          vel = self.getVelocityParticle2D(object,po)

          x0 = self.pa[i].pos.x
          y0 = self.pa[i].pos.y

          self.pa[i].pos.x += vel.x * object.deltaT * self.speedCoef
          self.pa[i].pos.y += vel.y * object.deltaT * self.speedCoef

          if (self.pa[i].pos.x > object.size.x):
             self.resetParticle2D(object,i)
