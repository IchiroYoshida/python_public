# 解析を行う形状を0,1値によって表現(Map)する。

from config.init import *
from functions.globals import *

import functions.classShape as shape

rect = shape.Rect(ImageFile)
rect.InitData()              #初期化

print("Map")
for i in range(0,NX+1):
    print(i,Map[i])
