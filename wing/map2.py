#解析を行う物体形状をグラッフィクで表示する。

from config.init import *
from functions.globals import *

import functions.classShape as shape
import functions.rectPlot as rplot

rect = shape.Rect(ImageFile)
rect.InitData()              #初期化

rplot.drawMap(rect)
