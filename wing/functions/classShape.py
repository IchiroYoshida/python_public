from config.init import *
from functions.globals import *

import cv2
import numpy as np
from scipy import ndimage

#
# classShape
# 
# 解析領域構造体
#
class Rect(object):
   def __init__(self,ImageFile):
      self.img        =  ImageFile
      print('read image =',self.img)

   def MapData(self):
      shape = cv2.imread(self.img)
      shape_gray = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)
      _, shape_binary = cv2.threshold(shape_gray,
              150,255, cv2.THRESH_BINARY)
      shape_binary = cv2.bitwise_not(shape_binary)
      print('shape =',shape_binary.shape)
      new_shape = np.array(shape_binary[::2, ::2].transpose())
      rot_shape = ndimage.rotate(new_shape,AOA,mode = 'constant')

      (X,Y) = rot_shape.shape
      print('analyze =',X,Y)

      for i in range(0,X):
         for j in range(0,Y):
             if (rot_shape[i,j]>1):Map[i+Map_X,Y-j+Map_Y]=1

   def MapType(self):
      map = [0,0,0,0]
      type= [0,0,0,0]
      tmp = [0,0,0,0]

      for i in range(0,NX-1):
          for j in range(0,NY-1):

              map[0] = Map[i  ,j+1]
              map[1] = Map[i  ,j  ]
              map[2] = Map[i+1,j+1]
              map[3] = Map[i+1,j  ]

              if   ( map == [0,0,0,0] ):
                 type = [INSIDE,INSIDE,INSIDE,INSIDE]
              elif ( map == [0,0,0,1] ):
                 type = [OBS_UL,OBS_LEFT,OBS_TOP,OBSTACLE]
              elif ( map == [0,0,1,0] ):
                 type = [OBS_LEFT,OBS_LL,OBSTACLE,OBS_BOTTOM]
              elif ( map == [0,0,1,1] ):
                 type = [OBS_LEFT,OBS_LEFT,OBSTACLE,OBSTACLE]
              elif ( map == [0,1,0,0] ):
                 type = [OBS_TOP,OBSTACLE,OBS_UR,OBS_RIGHT]
              elif ( map == [0,1,0,1] ):
                 type = [OBS_TOP,OBSTACLE,OBS_TOP,OBSTACLE]
              elif ( map == [0,1,1,0] ):
                 type = [OBS_UL,OBSTACLE,OBSTACLE,OBS_LR]
              elif ( map == [0,1,1,1] ):
                 type = [OBS_UL,OBSTACLE,OBSTACLE,OBSTACLE]
              elif ( map == [1,0,0,0] ):
                 type = [OBSTACLE,OBS_BOTTOM,OBS_RIGHT,OBS_LR]
              elif ( map == [1,0,0,1] ):
                 type = [OBSTACLE,OBS_LL,OBS_UR,OBSTACLE]
              elif ( map == [1,0,1,0] ):
                 type = [OBSTACLE,OBS_BOTTOM,OBSTACLE,OBS_BOTTOM]
              elif ( map == [1,0,1,1] ):
                 type = [OBSTACLE,OBS_LL,OBSTACLE,OBSTACLE]
              elif ( map == [1,1,0,0] ):
                 type = [OBSTACLE,OBSTACLE,OBS_RIGHT,OBS_RIGHT]
              elif ( map == [1,1,0,1] ):
                 type = [OBSTACLE,OBSTACLE,OBS_UR,OBSTACLE]
              elif ( map == [1,1,1,0] ):
                 type = [OBSTACLE,OBSTACLE,OBSTACLE,OBS_LR]
              elif ( map == [1,1,1,1] ):
                 type = [OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE]

              tmp[0] = Type[i  ,j+1]
              if (type[0] < tmp[0]): type[0]=tmp[0]
              tmp[1] = Type[i  ,j  ]
              if (type[1] < tmp[1]): type[1]=tmp[1]
              tmp[2] = Type[i+1,j+1]
              if (type[2] < tmp[2]): type[2]=tmp[2]
              tmp[3] = Type[i+1,j  ]
              if (type[3] < tmp[3]): type[3]=tmp[3]

              Type[i  ,j+1]=type[0]
              Type[i  ,j  ]=type[1]
              Type[i+1,j+1]=type[2]
              Type[i+1,j  ]=type[3]

   #初期設定　　　格子点のタイプ
   def InitData(self):
      Rect.MapData(self)
      Rect.MapType(self)

      for i in range(0,NX+1):
          for j in range(0,NY+1):
             if (j== 0):
                Type[i,j] = BOTTOM     #下側壁面
             elif(j== NY):
                Type[i,j] = TOP        #上側壁面
             elif(i== 0):
                Type[i,j] = INLET      #流入端
             elif(i== NX):
                Type[i,j]= OUTLET      #流出端

      #初期値
      #入口・出口は流速1.0、圧力Prsの初期条件
      for i in range(0,NX+1):
         for j in range(0,NY+1):
            t=Type[i,j]
            if(t  == TOP):             #上壁
                vx    = ideal
            elif(t == BOTTOM):         #下壁
                vx    = ideal
            elif(t == OBS_LEFT):
                vx    = 0.0
            elif(t == OBS_RIGHT):
                vx    = 0.0
            elif(t == OBS_TOP):
                vx    = 0.0
            elif(t == OBS_BOTTOM):
                vx    = 0.0
            elif(t == OBS_LL):
                vx    = 0.0
            elif(t == OBS_UL):
                vx    = 0.0
            elif(t == OBS_LR):
                vx    = 0.0
            elif(t == OBS_UR):
                vx    = 0.0
            elif(t == OBSTACLE):
                vx    = 0.0
            else:
                vx    = 1.0

            VelX[i,j] = vx
