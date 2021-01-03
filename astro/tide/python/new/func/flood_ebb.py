DAYMINUTE = 1440

import numpy as np
from peakdetect import *

def flood_ebb(time,level):

   """
   flood_ebb.py :  満潮と干潮時刻と潮位の検出

   hitide, lowtide = flood_ebb(time,level)

   time : 時刻（分）
   level: 潮位(cm)

   hitide :  満潮（時刻、潮位）
   lowtide:  干潮（時刻、潮位）

   """

   hitide =[]
   lowtide=[]

   hitide2 = []
   lowtide2 = []

   hitide_time2  = []
   lowtide_time2 = []

   hitide_level2  = []
   lowtide_level2 = []

   #満潮と干潮の判定
   hitides0, lowtides0 = peakdet(level,.5)

   # 満潮処理
   hitide_time0   = np.array(hitides0)[:,0]-40  #時間、計算開始は40分前から
   hitide_level0  = np.array(hitides0)[:,1]     #満潮潮位
   # 満潮時刻と潮位の一日区間（分）を抽出
   hitide_time    = hitide_time0[ (hitide_time0>=0)&(hitide_time0<DAYMINUTE)]
   hitide_level   = hitide_level0[(hitide_time0>=0)&(hitide_time0<DAYMINUTE)]

   # 満潮時刻へ変換
   for ht in hitide_time:
       hitide_time2.append(str('%02d:' % (ht//60))+str('%02d' % (ht%60)))

   # 満潮潮位を整数変換
   for hl in hitide_level:
       hitide_level2.append(int(round(hl)))


   # 干潮処理
   lowtide_time0  = np.array(lowtides0)[:,0]-40
   lowtide_level0 = np.array(lowtides0)[:,1]
   # 干潮時刻と潮位の一日区間（分）を抽出
   lowtide_time   = lowtide_time0[ (lowtide_time0>=0)&(lowtide_time0<DAYMINUTE)]
   lowtide_level  = lowtide_level0[(lowtide_time0>=0)&(lowtide_time0<DAYMINUTE)]

   # 干潮時刻へ変換
   for lt in lowtide_time:
       lowtide_time2.append(str('%02d:' % (lt//60))+str('%02d' % (lt%60)))
   
   # 干潮潮位を整数変換  
   for ll in lowtide_level:
       lowtide_level2.append(int(round(ll)))

   hitide2 = np.c_[hitide_time2 ,hitide_level2 ]
   lowtide2= np.c_[lowtide_time2,lowtide_level2]

   return array(hitide2),array(lowtide2)
