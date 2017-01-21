#酒井幸市　著、工学社：「流れ」と「波」のシミュレーション（I/O Books）を参考
#
# レギュラー格子による速度―圧力法（フラクショナル・ステップ法）
#
#速度ベクトル、速度の大きさを背景表示する。

from config.init import *

from timeit import default_timer as timer
import numpy as np
import functions.rectPlot as rplt
import functions.nsfunc   as ns
import functions.classShape as shape

elapseTimeN = 0.0
count       =   0
img         =   1

rect = shape.Rect(ImageFile)

print("Main start!!")
rect.InitData()              #初期化

start_time = timer()
while (elapseTimeN < Stop):
   print("Time = %6.3f"%(elapseTimeN))
   ns.calcPoisson(rect)

   if ((count % 10)==0):
       rplt.PlotQuiverVelRec(rect,elapseTimeN,img)
       img +=1

   elapseTimeN += deltaT
   count += 1

end_time=timer()

print(end_time - start_time)

