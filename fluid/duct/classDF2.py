import nsfunc
import numpy as np

#
# classDF2
# 
# 解析領域構造体
#
class Rect(object):
   def __init__(self,Re,deltaT):
      #領域定義
      self.INSIDE    = 0
      self.INLET     = 1
      self.OUTLET    = 2
      self.TOP       = 3
      self.BOTTOM    = 4
      self.OBS_LEFT  = 5
      self.OBS_TOP   = 6
      self.OBS_RIGHT = 7
      self.OBSTACLE  = 8
      self.OBS_LL    = 9
      self.OBS_UL    =10
      self.OBS_LR    =11
      self.OBS_UR    =12
      self.OBS_BOTTOM=13

      self.scale      =  nsfunc.Vector2( 1, 1)    #表示倍率
      self.nMeshX     =  80                       #x方向分割数（固定）
      self.nMeshY     =  40                       #y方向分割数（固定）
      self.size       =  nsfunc.Vector2(  2,  1)  #矩形ダクト領域のサイズ（固定）
      self.left0      =  nsfunc.Vector2(  0,  0)  #その左下位置
      self.delta      =  nsfunc.Vector2(  0,  0)  #
      self.ideal      =   0                       #側面理想流体

      self.obs_nX1    =  15     #左端から障害物１中心までの距離（格子間隔の整数倍）
      self.obs_nY1    =  10     #下端から障害物１中心までの距離（格子間隔の整数倍）
      self.obs_nX2    =  30     #左端から障害物２中心までの距離（格子間隔の整数倍）
      self.obs_nY2    =  25     #下端から障害物２中心までの距離（格子間隔の整数倍）

      self.obs_nWX    =   8     #障害物の厚さ（ｘ方向、格子間隔の整数倍）
      self.obs_nWY    =  10     #障害物の幅（ｙ方向、格子間隔の整数倍） 

      self.Re         =  Re
      self.deltaT     =  deltaT

      #障害物共通（座標）
      self.obs_width  = self.obs_nWX/self.nMeshX*self.size.x    #障害物厚さ(x方向）
      self.obs_height = self.obs_nWY/self.nMeshY*self.size.y    #障害物高さ(y方向)

      #障害物１（格子）  
      self.nX11 = self.obs_nX1 - self.obs_nWX/2    #障害物１　左端
      self.nX12 = self.nX11 + self.obs_nWX         #          右端
      self.nY11 = self.obs_nY1 - self.obs_nWY/2    #          下端
      self.nY12 = self.nY11 + self.obs_nWY         #          上端

      #障害物１（座標）
      self.center1x = self.obs_nX1/self.nMeshX*self.size.x     #障害物１中心 
      self.center1y = self.obs_nY1/self.nMeshY*self.size.y
      self.x11 = self.center1x-self.obs_width/2                #障害物１左端
      self.x12 = self.center1x+self.obs_width/2                #        右端
      self.y11 = self.center1y-self.obs_height/2               #        下端
      self.y12 = self.center1y+self.obs_height/2               #        上端

      #障害物２（格子）  
      self.nX21 = self.obs_nX2 - self.obs_nWX/2    #障害物２　左端
      self.nX22 = self.nX21 + self.obs_nWX         #          右端
      self.nY21 = self.obs_nY2 - self.obs_nWY/2    #          下端
      self.nY22 = self.nY21 + self.obs_nWY         #          上端

      #障害物２
      self.center2x = self.obs_nX2/self.nMeshX*self.size.x     #障害物２中心 
      self.center2y = self.obs_nY2/self.nMeshY*self.size.y     
      self.x21 = self.center2x-self.obs_width/2                #        左端
      self.x22 = self.center2x+self.obs_width/2                #        右端
      self.y21 = self.center2y-self.obs_height/2               #        下端
      self.y22 = self.center2y+self.obs_height/2               #        上端

      #######領域設定関連
      self.NX = self.nMeshX
      self.NY = self.nMeshY
      self.DX = self.size.x/self.NX    #格子間隔
      self.DY = self.size.y/self.NY

      self.DX2 = self.DX * self.DX
      self.DY2 = self.DY * self.DY
      self.DD2 = self.DX2 + self.DY2 #corner

      self.maxPrs  =   0.5
      self.minPrs  = - 0.5
      self.maxOmg  =  20.0
      self.minOmg  = -20.0

      self.maxPrs0 = 0.0
      self.minPrs0 = 0.0
      self.maxOmg0 = 0.0
      self.minOmg0 = 0.0

      #配列
      self.Prs  = np.zeros((self.NX+1,self.NY+1))  #圧力
      self.VelX = np.zeros((self.NX+1,self.NY+1))  #staggered格子点のx方向速度
      self.VelY = np.zeros((self.NX+1,self.NY+1))  #staggered格子点のy方向速度 
      self.Type = np.zeros((self.NX+1,self.NY+1))  #格子点のタイプ
      self.Omega= np.zeros((self.NX+1,self.NY+1))  #渦度(x,y速度で計算）
      self.VelXgx = np.zeros((self.NX+1,self.NY+1)) #x方向速度微分
      self.VelXgy = np.zeros((self.NX+1,self.NY+1)) #y方向速度微分
      self.VelYgx = np.zeros((self.NX+1,self.NY+1)) #x方向速度微分
      self.VelYgy = np.zeros((self.NX+1,self.NY+1)) #y方向速度微分


   #初期設定　　　格子点のタイプ
   def InitData(self):
      for i in range(0,self.NX+1):
          for j in range(0,self.NY+1):
             self.Type[i,j] = self.INSIDE          #内点
             if (j== 0):
                self.Type[i,j] = self.BOTTOM     #下側壁面
             elif(j== self.NY):
                self.Type[i,j] = self.TOP        #上側壁面
             elif(i== 0):
                self.Type[i,j] = self.INLET      #流入端
             elif(i== self.NX):
                self.Type[i,j]= self.OUTLET      #流出端
             #障害物１
             elif(i== self.nX11 and j > self.nY11 and j < self.nY12):
                self.Type[i,j]= self.OBS_LEFT    #障害物１左端
             elif(i== self.nX12 and j > self.nY11 and j < self.nY12):
                self.Type[i,j]= self.OBS_RIGHT   #障害物１右端
             elif(i > self.nX11  and i < self.nX12 and j == self.nY12):
                self.Type[i,j]= self.OBS_TOP     #障害物１上端
             elif(i > self.nX11 and i < self.nX12 and j == self.nY11):
                self.Type[i,j]= self.OBS_BOTTOM  #障害物１下端
             elif(i > self.nX11 and i < self.nX12 and j > self.nY11 and j < self.nY12):
                self.Type[i,j]= self.OBSTACLE    #障害物１内部
             #corner
             elif(i == self.nX11 and j == self.nY11):
                self.Type[i,j] = self.OBS_LL    
             elif(i == self.nX11 and j == self.nY12):
                self.Type[i,j] = self.OBS_UL
             elif(i == self.nX12 and j == self.nY11):
                self.Type[i,j] = self.OBS_LR
             elif(i == self.nX12 and j == self.nY12):
                self.Type[i,j] = self.OBS_UR
             #障害物２
             elif(i== self.nX21 and j > self.nY21 and j < self.nY22):
                self.Type[i,j]= self.OBS_LEFT    #障害物２左端
             elif(i== self.nX22 and j > self.nY21 and j < self.nY22):
                self.Type[i,j]= self.OBS_RIGHT   #障害物２右端
             elif(i > self.nX21  and i < self.nX22 and j == self.nY22):
                self.Type[i,j]= self.OBS_TOP     #障害物２上端
             elif(i > self.nX21 and i < self.nX22 and j == self.nY21):
                self.Type[i,j]= self.OBS_BOTTOM  #障害物２下端
             elif(i > self.nX21 and i < self.nX22 and j > self.nY21 and j < self.nY22):
                self.Type[i,j]= self.OBSTACLE    #障害物２内部
             #corner
             elif(i == self.nX21 and j == self.nY21):
                self.Type[i,j] = self.OBS_LL    
             elif(i == self.nX21 and j == self.nY22):
                self.Type[i,j] = self.OBS_UL
             elif(i == self.nX22 and j == self.nY21):
                self.Type[i,j] = self.OBS_LR
             elif(i == self.nX22 and j == self.nY22):
                self.Type[i,j] = self.OBS_UR
      

      #初期値
      #入口・出口は流速1.0、圧力Prsの初期条件
      for i in range(0,self.NX+1):
         for j in range(0,self.NY+1):
            t=self.Type[i,j]
            if(t  == self.TOP):             #上壁
                vx    = self.ideal
            elif(t == self.BOTTOM):         #下壁
                vx    = self.ideal
            elif(t == self.OBS_LEFT):
                vx    = 0.0
            elif(t == self.OBS_RIGHT):
                vx    = 0.0
            elif(t == self.OBS_TOP):
                vx    = 0.0
            elif(t == self.OBS_BOTTOM):
                vx    = 0.0
            elif(t == self.OBS_LL):
                vx    = 0.0
            elif(t == self.OBS_UL):
                vx    = 0.0
            elif(t == self.OBS_LR):
                vx    = 0.0
            elif(t == self.OBS_UR):
                vx    = 0.0
            else:
                vx    = 1.0

            self.VelX[i,j] = vx
