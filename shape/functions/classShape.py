import functions.nsfunc as ns
import cv2
import numpy as np
#
# classShape
# 
# 解析領域構造体
#
class Rect(object):
   def __init__(self,Re,deltaT,ImageFile):
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

      self.scale      =  ns.Vector2( 1, 1)    #表示倍率
      self.nMeshX     =  100                       #x方向分割数（固定）
      self.nMeshY     =  50                    #y方向分割数（固定）
      self.size       =  ns.Vector2( 3.0, 1.5)  #矩形ダクト領域のサイズ（固定）
      self.left0      =  ns.Vector2(  0,  0)  #その左下位置
      self.delta      =  ns.Vector2(  0,  0)  #
      self.ideal      =   0                       #側面理想流体

      self.Re         =  Re
      self.deltaT     =  deltaT
      self.img        =  './data/images/'+ImageFile
      print('read image =',self.img)

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
      self.Map  = np.zeros((self.NX+1,self.NY+1))  #格子点図形マップ配列
      self.Type = np.zeros((self.NX+1,self.NY+1))  #格子点図形のタイプ
      self.Omega= np.zeros((self.NX+1,self.NY+1))  #渦度(x,y速度で計算）
      self.VelXgx = np.zeros((self.NX+1,self.NY+1)) #x方向速度微分
      self.VelXgy = np.zeros((self.NX+1,self.NY+1)) #y方向速度微分
      self.VelYgx = np.zeros((self.NX+1,self.NY+1)) #x方向速度微分
      self.VelYgy = np.zeros((self.NX+1,self.NY+1)) #y方向速度微分

   def MapData(self):
      #coins = cv2.imread('./data/images/prius.jpg')
      shape = cv2.imread(self.img)
      shape_gray = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)
      shape_gauss = cv2.GaussianBlur(shape_gray, (5,5), 0)
      _, shape_binary = cv2.threshold(shape_gauss,
              150,255, cv2.THRESH_BINARY)
      shape_binary = cv2.bitwise_not(shape_binary)
      print('shape =',shape_binary.shape)
      new_shape = np.array(shape_binary[::4, ::4].transpose())

      (X,Y) = new_shape.shape
      print('analyze =',X,Y)

      for i in range(0,X):
          for j in range(0,Y):
              if (new_shape[i,j]>1):self.Map[i+3,Y-j+4]=1


   def MapType(self):
      map = [0,0,0,0]
      type= [0,0,0,0]
      tmp = [0,0,0,0]

      for i in range(0,self.NX-1):
          for j in range(0,self.NY-1):

              map[0] = self.Map[i  ,j+1]
              map[1] = self.Map[i  ,j  ]
              map[2] = self.Map[i+1,j+1]
              map[3] = self.Map[i+1,j  ]

              if   ( map == [0,0,0,0] ):
                 type = [self.INSIDE,self.INSIDE,self.INSIDE,self.INSIDE]
              elif ( map == [0,0,0,1] ):
                 type = [self.OBS_UL,self.OBS_LEFT,self.OBS_TOP,self.OBSTACLE]
              elif ( map == [0,0,1,0] ):
                 type = [self.OBS_LEFT,self.OBS_LL,self.OBSTACLE,self.OBS_BOTTOM]
              elif ( map == [0,0,1,1] ):
                 type = [self.OBS_LEFT,self.OBS_LEFT,self.OBSTACLE,self.OBSTACLE]
              elif ( map == [0,1,0,0] ):
                 type = [self.OBS_TOP,self.OBSTACLE,self.OBS_UR,self.OBS_RIGHT]
              elif ( map == [0,1,0,1] ):
                 type = [self.OBS_TOP,self.OBSTACLE,self.OBS_TOP,self.OBSTACLE]
              elif ( map == [0,1,1,0] ):
                 type = [self.OBS_UL,self.OBSTACLE,self.OBSTACLE,self.OBS_LR]
              elif ( map == [0,1,1,1] ):
                 type = [self.OBS_UL,self.OBSTACLE,self.OBSTACLE,self.OBSTACLE]
              elif ( map == [1,0,0,0] ):
                 type = [self.OBSTACLE,self.OBS_BOTTOM,self.OBS_RIGHT,self.OBS_LR]
              elif ( map == [1,0,0,1] ):
                 type = [self.OBSTACLE,self.OBS_LL,self.OBS_UR,self.OBSTACLE]
              elif ( map == [1,0,1,0] ):
                 type = [self.OBSTACLE,self.OBS_BOTTOM,self.OBSTACLE,self.OBS_BOTTOM]
              elif ( map == [1,0,1,1] ):
                 type = [self.OBSTACLE,self.OBS_LL,self.OBSTACLE,self.OBSTACLE]
              elif ( map == [1,1,0,0] ):
                 type = [self.OBSTACLE,self.OBSTACLE,self.OBS_RIGHT,self.OBS_RIGHT]
              elif ( map == [1,1,0,1] ):
                 type = [self.OBSTACLE,self.OBSTACLE,self.OBS_UR,self.OBSTACLE]
              elif ( map == [1,1,1,0] ):
                 type = [self.OBSTACLE,self.OBSTACLE,self.OBSTACLE,self.OBS_LR]
              elif ( map == [1,1,1,1] ):
                 type = [self.OBSTACLE,self.OBSTACLE,self.OBSTACLE,self.OBSTACLE]

              tmp[0] = self.Type[i  ,j+1]
              if (type[0] < tmp[0]): type[0]=tmp[0]
              tmp[1] = self.Type[i  ,j  ]
              if (type[1] < tmp[1]): type[1]=tmp[1]
              tmp[2] = self.Type[i+1,j+1]
              if (type[2] < tmp[2]): type[2]=tmp[2]
              tmp[3] = self.Type[i+1,j  ]
              if (type[3] < tmp[3]): type[3]=tmp[3]

              self.Type[i  ,j+1]=type[0]
              self.Type[i  ,j  ]=type[1]
              self.Type[i+1,j+1]=type[2]
              self.Type[i+1,j  ]=type[3]

   #初期設定　　　格子点のタイプ
   def InitData(self):
      Rect.MapData(self)
      Rect.MapType(self)

      for i in range(0,self.NX+1):
          for j in range(0,self.NY+1):
             if (j== 0):
                self.Type[i,j] = self.BOTTOM     #下側壁面
             elif(j== self.NY):
                self.Type[i,j] = self.TOP        #上側壁面
             elif(i== 0):
                self.Type[i,j] = self.INLET      #流入端
             elif(i== self.NX):
                self.Type[i,j]= self.OUTLET      #流出端

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
