"""
石垣　固有値（２０１６年）　主要４分潮
"""
import numpy as np
import tide
pt = tide.Port

pt.name = "石垣"

pt.lat   =  24.20  #緯度
pt.lng   = 124.10  #経度
pt.level = 107     #平均潮位（cm）

pt.pl = np.zeros(4,np.float64)
pt.hr = np.zeros(4,np.float64)

# 調和定数（遅角）      分潮
pt.pl[0] = 199.36    #10    O1
pt.pl[1] = 221.35    #17    K1
pt.pl[2] = 193.52    #31    M2
pt.pl[3] = 216.23    #36    S2 

# 調和定数（振幅）
pt.hr[0] = 16.93     #10    O1
pt.hr[1] = 19.81     #17    K1
pt.hr[2] = 44.24     #31    M2
pt.hr[3] = 19.49     #36    S2
