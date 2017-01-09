#解析を行う物体形状をグラッフィクで表示する。

import init
import functions.classShape as shape
import functions.rectPlot as rplot

deltaT    = init.deltaT
Re        = init.Re
ImageFile = init.ImageFile

rect = shape.Rect(Re,deltaT,ImageFile)
rect.InitData()              #初期化

rplot.drawMap(rect)
