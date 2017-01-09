# 解析を行う形状を0,1値によって表現(Map)する。

import init
import functions.classShape as shape

deltaT    = init.deltaT
Re        = init.Re
ImageFile = init.ImageFile

rect = shape.Rect(Re,deltaT,ImageFile)
rect.InitData()              #初期化

print("Map")
for i in range(0,rect.NX+1):
    print(i,rect.Map[i])
