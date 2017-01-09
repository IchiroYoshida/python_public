#酒井幸市　著、工学社：「流れ」のシミュレーションを参考
# Section 5; ductFS1_1
#
# レギュラー格子による速度―圧力法（フラクショナル・ステップ法）
#

import init
import numpy as np
import functions.rectPlot as rplt
import functions.nsfunc as ns
import functions.classShape as shape

Stop      = init.Stop
ImageFile = init.ImageFile
speedCoef = init.speedCoef
deltaT    = init.deltaT
Re        = init.Re

elapseTimeN = 0.0
count       =   0
img         =   1

rect = shape.Rect(Re,deltaT,ImageFile)

print("Main start!!")
rect.InitData()              #初期化

while (elapseTimeN < Stop):
   print("Time = %6.3f"%(elapseTimeN))
   ns.calcPoisson(rect)

   if ((count % 10)==0):
       rplt.PlotStreamRec(rect,elapseTimeN,img)
       img +=1

   elapseTimeN += deltaT
   count += 1
