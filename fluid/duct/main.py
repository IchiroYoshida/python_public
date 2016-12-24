#酒井幸市　著、工学社：「流れ」のシミュレーションを参考
# Section 5; ductFS1_1
#
# レギュラー格子による速度―圧力法（フラクショナル・ステップ法）
#

#--------設定パラメータ----------------
Stop =  1.0     #終了までに計算する秒数 

numMaxP = 8000  #粒子の数
TimeP   =  200  #粒子放出の間隔
sizeP   =    5  #粒子の大きさ
speedCoef =  1.0 #速度調節パラメータ
deltaT       = 0.005
Re           = 5000.0   #レイノルズ数
#---------------------------------------

import numpy as np
import rectPlot 
import nsfunc
import classDF2 as df2
import particle 

elapseTimeN = 0.0
count       =   0
img         =   1

pa = (numMaxP+1)*[]

rect = df2.Rect(Re,deltaT)
part = particle.Particle(pa,numMaxP,sizeP,speedCoef)

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
    nsfunc.calcPoisson(rect) 
    part.calcParticle2D(rect)

    if ((count % 10)==0):
       rectPlot.drawParticleRec(part,rect,elapseTimeN,img)
       img +=1

    elapseTimeN += deltaT
    count +=1


while (elapseTimeN < Stop):
   print("Time = %6.3f"%(elapseTimeN))
   nsfunc.calcPoisson(rect)
   part.calcParticle2D(rect)      # 粒子の位置を求める

   if ((count % 10)==0):
       rectPlot.drawParticleRec(part,rect,elapseTimeN,img)
       img +=1

   elapseTimeN += deltaT
   count += 1
