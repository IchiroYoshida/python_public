#
# 流体解析関数
#
#

import numpy as np
import copy

class Vector2(object):
    def __init__(self,x,y):
       self.x = x
       self.y = y

def calcPoisson(self):
   #Poissonの方程式を解く
   iteration = 10      #最大繰り返し回数
   tolerance = 0.00001 #許容誤差
   error     = 0.0

   D = np.zeros((self.NX+1,self.NY+1))

   A1  = 0.5 * self.DY2/(self.DX2+self.DY2)
   A2  = 0.5 * self.DX2/(self.DX2+self.DY2)
   A3  = 0.25 * self.DX2 * self.DY2 / (self.DX2 + self.DY2)

   #Navie-Stokes方程式による速度更新
   self.VelX,self.VelXgx,self.VelXgy = methodCIP(self,self.VelX,self.VelXgx,self.VelXgy)
   self.VelY,self.VelYgx,self.VelYgy = methodCIP(self,self.VelY,self.VelYgx,self.VelYgy)

   #Poisson方程式の右辺
   for i in range(1,self.NX):
       for j in range(1,self.NY):
           if(self.Type[i,j] != self.INSIDE): continue
           a = (self.VelX[i+1,j] - self.VelX[i-1,j])/self.DX
           b = (self.VelY[i,j+1] - self.VelY[i,j-1])/self.DY
           D[i,j] = A3*(a + b) /self.deltaT

   # Poissonの方程式を解く
   cnt = 0
   while (cnt < iteration):
      maxError = 0.0
      for i in range (0,self.NX+1):
          for j in range(0,self.NY+1):
              if(self.Type[i,j] == self.INSIDE):continue
              elif(self.Type[i,j] == self.INLET):
                  self.Prs[i,j] = self.Prs[1,j]      # Neumann(流入口)
              elif(self.Type[i,j] == self.OUTLET):
                  self.Prs[i,j] = 0.0                # 流出口
              elif(self.Type[i,j] == self.TOP):
                  self.Prs[i,j] = self.Prs[i,self.NY-1]
              elif(self.Type[i,j] == self.BOTTOM):
                  self.Prs[i,j] = self.Prs[i,1]
              elif(self.Type[i,j] == self.OBS_LEFT):
                  self.Prs[i,j] = self.Prs[i-1,j]
              elif(self.Type[i,j] == self.OBS_RIGHT):
                  self.Prs[i,j] = self.Prs[i+1,j]
              elif(self.Type[i,j] == self.OBS_TOP):
                  self.Prs[i,j] = self.Prs[i,j+1]
              elif(self.Type[i,j] == self.OBS_BOTTOM):
                  self.Prs[i,j] = self.Prs[i,j-1]
              elif(self.Type[i,j] == self.OBS_UL):
                  self.Prs[i,j] = self.Prs[i-1,j+1]
              elif(self.Type[i,j] == self.OBS_UR):
                  self.Prs[i,j] = self.Prs[i+1,j+1]
              elif(self.Type[i,j] == self.OBS_LL):
                  self.Prs[i,j] = self.Prs[i-1,j-1]
              elif(self.Type[i,j] == self.OBS_LR):
                  self.Prs[i,j] = self.Prs[i+1,j-1]

      #反復計算
      for i in range (1,self.NX):
          for j in range(1,self.NY):
              if(self.Type[i,j] != self.INSIDE): continue
              pp = A1 * (self.Prs[i+1,j] + self.Prs[i-1,j]) +\
                   A2 * (self.Prs[i,j+1] + self.Prs[i,j-1]) - D[i,j]
              error = abs(pp - self.Prs[i,j])
              if (error > maxError): maxError = error
              self.Prs[i,j] = pp #更新

      if(maxError < tolerance): break
      cnt += 1

   #print("cnt = %d maxEr = %f"%(cnt,maxError))

   #速度ベクトルの計算
   for i in range(1,self.NX):
      for j in range(1,self.NY):
         if (self.Type[i,j] != self.INSIDE ): continue
         self.VelX[i,j] += - 0.5 * self.deltaT * (self.Prs[i+1,j] - self.Prs[i-1,j]) / self.DX
         self.VelY[i,j] += - 0.5 * self.deltaT * (self.Prs[i,j+1] - self.Prs[i,j-1]) / self.DY

   #渦度を速度から求める
   for i in range(1,self.NX):
      for j in range(1,self.NY):
         self.Omega[i,j] =  0.5 * ((self.VelY[i+1,j] - self.VelY[i-1,j]) / self.DX \
                                -  (self.VelX[i,j+1] - self.VelX[i,j-1]) / self.DY)

         #print('Omega %d , %d = %f'%(i,j,self.Omega[i,j]))

   #流れ関数、渦度の最小値、最大値
   for i in range(1,self.NX):
      for j in range(1,self.NY):
         if(self.Type[i,j] != self.INSIDE): continue
         if(self.Prs[i,j] > self.maxPrs0 ): self.maxPrs0 = self.Prs[i,j]
         if(self.Prs[i,j] < self.minPrs0 ): self.minPrs0 = self.Prs[i,j]
         if(self.Omega[i,j] > self.maxOmg0 ): self.maxOmg0 = self.Omega[i,j]
         if(self.Omega[i,j] < self.minOmg0 ): self.minOmg0 = self.Omega[i,j]

   #print("maxPrs= %f    minPrs= %f"%(self.maxPrs0,self.minPrs0))
   #print("maxOmg= %f    minOmg= %f"%(self.maxOmg0,self.minOmg0))

def methodCIP(self,f,gx,gy):

   newF     = np.zeros((self.NX+1,self.NY+1))
   newGx    = np.zeros((self.NX+1,self.NY+1))
   newGy    = np.zeros((self.NX+1,self.NY+1))

   vx       = np.array(self.VelX)
   vy       = np.array(self.VelY)

   for i in range(1,self.NX):
      for j in range(1,self.NY):
         if (self.Type[i,j] != self.INSIDE): continue

         if (vx[i,j] >= 0.0): sx = int( 1)
         else:                sx = int(-1)

         if (vy[i,j] >= 0.0): sy = int( 1)
         else:                sy = int(-1)

         x = - vx[i,j] * self.deltaT
         y = - vy[i,j] * self.deltaT

         ip = i - int(sx)  #上流点
         jp = j - int(sy)

         dx = sx * self.DX
         dy = sy * self.DY

         dx2 = dx  * dx
         dx3 = dx2 * dx
         dy2 = dy  * dy
         dy3 = dy2 * dy

         c30 = ((gx[ip,j] + gx[i,j]) * dx - 2.0 * (f[i,j] - f[ip,j])) / dx3
         c20 = (3.0 * (f[ip,j] - f[i,j]) + (gx[ip,j] + 2.0 * gx[i,j]) * dx) / dx2
         c03 = ((gy[i,jp] + gy[i,j]) * dy - 2.0 * (f[i,j] - f[i,jp])) / dy3
         c02 = (3.0 * (f[i,jp] - f[i,j]) + (gy[i,jp] + 2.0 * gy[i,j]) * dy) / dy2

         a  = f[i,j] - f[i,jp] - f[ip,j] + f[ip,jp]
         b  = gy[ip,j] - gy[i,j]

         c12 = (-a - b * dy) / (dx * dy2)
         c21 = (-a - (gx[i,jp] - gx[i,j]) * dx) / (dx2*dy)
         c11 = - b / dx + c21 * dx

         newF[i,j] = f[i,j] + ((c30 * x + c21 * y + c20) * x + c11 * y + gx[i,j])* x\
                       + ((c03 * y + c12 * x + c02) * y + gy[i,j]) * y

         newGx[i,j] = gx[i,j] + (3.0 * c30 * x + 2.0 * (c21 * y + c20)) * x + (c12 * y + c11) * y
         newGy[i,j] = gy[i,j] + (3.0 * c03 * y + 2.0 * (c12 * x + c02)) * y + (c21 * x + c11) * x

         #粘性項に中央差分
         newF[i,j] += self.deltaT * ((f[i-1,j] + f[i+1,j] - 2.0 * f[i,j]) / dx2 \
                   +  (f[i,j-1] + f[i,j+1] - 2.0 * f[i,j]) / dy2 ) / self.Re


   for i in range(1,self.NX):
      for j in range(1,self.NY):
         if (self.Type[i,j] != self.INSIDE): continue
         f[i,j]  = newF[i,j]
         gx[i,j] = newGx[i,j]
         gy[i,j] = newGy[i,j]

   return f,gx,gy

