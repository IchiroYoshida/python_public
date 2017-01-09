# 解析を行う形状の境界パラメータを設定(Type)する。

import init
import functions.classShape as shape

deltaT    = init.deltaT
Re        = init.Re
ImageFile = init.ImageFile

rect = shape.Rect(Re,deltaT)
rect.InitData()              #初期化

print("Type")
for i in range(0,rect.NX):
    map=''
    for j in range(0,rect.NY):
        map +=str('%2d '%(int(rect.Type[i,j])))
    print('%2d %s'%(i,map))
