from config.init import *

#領域定義
INSIDE    = 0
INLET     = 1
OUTLET    = 2
TOP       = 3    
BOTTOM    = 4  
OBS_LEFT  = 5
OBS_TOP   = 6
OBS_RIGHT = 7
OBSTACLE  = 8
OBS_LL    = 9
OBS_UL    =10
OBS_LR    =11
OBS_UR    =12
OBS_BOTTOM=13

#######領域設定関連
DX = SIZE_X/NX    #格子間隔
DY = SIZE_Y/NY

DX2 = DX * DX
DY2 = DY * DY
DD2 = DX2 + DY2 #corner

class Vector2(object):
    def __init__(self,x,y):
       self.x = x
       self.y = y

scale      =  Vector2( 1, 1)            #表示倍率
size       =  Vector2( SIZE_X, SIZE_Y)  #矩形ダクト領域のサイズ（固定）
left0      =  Vector2(  0,  0)          #その左下位置
delta      =  Vector2(  0,  0)          #
ideal      =  0                           #側面理想流体 

import numpy as np

#配列
Prs  = np.zeros((NX+1,NY+1))  #圧力
VelX = np.zeros((NX+1,NY+1))  #staggered格子点のx方向速度
VelY = np.zeros((NX+1,NY+1))  #staggered格子点のy方向速度 
Map  = np.zeros((NX+1,NY+1))  #格子点図形マップ配列
Type = np.zeros((NX+1,NY+1))  #格子点図形のタイプ
Omega= np.zeros((NX+1,NY+1))  #渦度(x,y速度で計算）
VelXgx = np.zeros((NX+1,NY+1)) #x方向速度微分
VelXgy = np.zeros((NX+1,NY+1)) #y方向速度微分
VelYgx = np.zeros((NX+1,NY+1)) #x方向速度微分
VelYgy = np.zeros((NX+1,NY+1)) #y方向速度微分
