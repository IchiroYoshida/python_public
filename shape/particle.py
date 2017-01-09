#酒井幸市　著、工学社：「流れ」と「波」のシミュレーション（I/O Books）を参考
#
# レギュラー格子による速度―圧力法（フラクショナル・ステップ法）
#
# 粒子を用いて流体アニメーションを表示する。

import init
import numpy as np
import functions.rectPlot as rplt
import functions.nsfunc as ns
import functions.classShape as shape
import functions.particle as prt

Stop      = init.Stop
ImageFile = init.ImageFile
speedCoef = init.speedCoef
deltaT    = init.deltaT
Re        = init.Re
sizeP     = init.sizeP
numMaxP   = init.numP
TimeP     = init.TimeP

elapseTimeN = 0.0
count       =   0
img         =   1

pa = (numMaxP+1)*[]

rect = shape.Rect(Re,deltaT,ImageFile)
part = prt.Particle(pa,numMaxP,sizeP,speedCoef)

print("Main start!!")
rect.InitData()              #初期化
part.initParticle2D(rect)    #粒子アニメーションの初期化

repeat = int(numMaxP/TimeP)

for t in range(0,TimeP):
    for n in range(0,repeat):
        i=t*repeat+n
        part.counts += 1
        part.resetParticle2D(rect,i)

    print("TimeInit = %6.3f"%(elapseTimeN))
    ns.calcPoisson(rect) 
    part.calcParticle2D(rect)

    if ((count % 10)==0):
       rplt.drawParticleRec(part,rect,elapseTimeN,img)
       img +=1

    elapseTimeN += deltaT
    count +=1


while (elapseTimeN < Stop):
   print("Time = %6.3f"%(elapseTimeN))
   ns.calcPoisson(rect)
   part.calcParticle2D(rect)      # 粒子の位置を求める

   if ((count % 10)==0):
       rplt.drawParticleRec(part,rect,elapseTimeN,img)
       img +=1

   elapseTimeN += deltaT
   count += 1
