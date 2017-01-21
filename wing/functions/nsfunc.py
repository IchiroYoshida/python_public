#
# 流体解析関数
#

from config.init import *
from functions.globals import *

import numpy as np
from numba import jit,jitclass,f8,float32

@jit('f8[:,:],f8[:,:],f8[:,:]',nopython=True)
def Poisson(VelX,VelY,Prs):

   iteration = 10      #最大繰り返し回数
   tolerance = 0.00001 #許容誤差
   error     = 0.0
 
   D     = np.zeros((NX+1,NY+1),dtype=np.float64)

   DX2 = DX * DX
   DY2 = DY * DY

   A1  =  0.5 * DY2/(DX2+DY2)
   A2  =  0.5 * DX2/(DX2+DY2)
   A3  = 0.25 * DX2 * DY2 / (DX2 + DY2)

   #Poisson方程式の右辺
   for i in range(1,NX):
       for j in range(1,NY):
           if(Type[i,j] != INSIDE): continue
           a = (VelX[i+1,j] - VelX[i-1,j])/DX
           b = (VelY[i,j+1] - VelY[i,j-1])/DY
           D[i,j] = A3*(a + b) /deltaT

   # Poissonの方程式を解く
   cnt = 0
   while (cnt < iteration):
      maxError = 0.0
      for i in range (0,NX+1):
          for j in range(0,NY+1):
              if(Type[i,j] == INSIDE):continue
              elif(Type[i,j] == INLET):
                  Prs[i,j] = Prs[1,j]      # Neumann(流入口)
              elif(Type[i,j] == OUTLET):
                  Prs[i,j] = 0.0           # 流出口
              elif(Type[i,j] == TOP):
                  Prs[i,j] = Prs[i,NY-1]
              elif(Type[i,j] == BOTTOM):
                  Prs[i,j] = Prs[i,1]
              elif(Type[i,j] == OBS_LEFT):
                  Prs[i,j] = Prs[i-1,j]
              elif(Type[i,j] == OBS_RIGHT):
                  Prs[i,j] = Prs[i+1,j]
              elif(Type[i,j] == OBS_TOP):
                  Prs[i,j] = Prs[i,j+1]
              elif(Type[i,j] == OBS_BOTTOM):
                  Prs[i,j] = Prs[i,j-1]
              elif(Type[i,j] == OBS_UL):
                  Prs[i,j] = Prs[i-1,j+1]
              elif(Type[i,j] == OBS_UR):
                  Prs[i,j] = Prs[i+1,j+1]
              elif(Type[i,j] == OBS_LL):
                  Prs[i,j] = Prs[i-1,j-1]
              elif(Type[i,j] == OBS_LR):
                  Prs[i,j] = Prs[i+1,j-1]

      #反復計算
      for i in range (1,NX):
          for j in range(1,NY):
              if(Type[i,j] != INSIDE): continue
              pp = A1 * (Prs[i+1,j] + Prs[i-1,j]) +\
                   A2 * (Prs[i,j+1] + Prs[i,j-1]) - D[i,j]
              error = abs(pp - Prs[i,j])
              if (error > maxError): maxError = error
              Prs[i,j] = pp #更新

      if(maxError < tolerance): break
      cnt += 1

   #速度ベクトルの計算
   for i in range(1,NX):
      for j in range(1,NY):
         if (Type[i,j] != INSIDE ): continue
         VelX[i,j] += - 0.5 * deltaT * (Prs[i+1,j] - Prs[i-1,j]) / DX
         VelY[i,j] += - 0.5 * deltaT * (Prs[i,j+1] - Prs[i,j-1]) / DY

@jit('f8[:,:],f8[:,:],f8[:,:]',nopython=True)
def methodCIP(f,gx,gy):

   newF     = np.zeros((NX+1,NY+1),dtype=np.float64)
   newGx    = np.zeros((NX+1,NY+1),dtype=np.float64)
   newGy    = np.zeros((NX+1,NY+1),dtype=np.float64)

   for i in range(1,NX):
      for j in range(1,NY):
         if (Type[i,j] != INSIDE): continue

         if (VelX[i,j] >= 0.0): sx = int( 1)
         else:                  sx = int(-1)

         if (VelY[i,j] >= 0.0): sy = int( 1)
         else:                  sy = int(-1)

         x = - VelX[i,j] * deltaT
         y = - VelY[i,j] * deltaT

         ip = i - int(sx)  #上流点
         jp = j - int(sy)

         dx = sx * DX
         dy = sy * DY

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
         newF[i,j] += deltaT * ((f[i-1,j] + f[i+1,j] - 2.0 * f[i,j]) / dx2 \
                   +  (f[i,j-1] + f[i,j+1] - 2.0 * f[i,j]) / dy2 ) / Re


   for i in range(1,NX):
      for j in range(1,NY):
         if (Type[i,j] != INSIDE): continue
         f[i,j]  = newF[i,j]
         gx[i,j] = newGx[i,j]
         gy[i,j] = newGy[i,j]

def calcPoisson(self):
   global VelX,VelY,VelXgx,VelXgy,VelYgx,VelYgy,Prs

   #Navier-Stokes方程式による速度更新
   methodCIP(VelX,VelXgx,VelXgy)
   methodCIP(VelY,VelYgx,VelYgy)

   #Poisson式を解く
   Poisson(VelX,VelY,Prs)
