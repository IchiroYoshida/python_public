"""
tide.py

2016/07/10

Author: Ichiro Yoshida

潮汐算出 version 1.0
"""
import math
import datetime
import numpy as np

# 基本定数、関数

class lib:
   dr = 0.0174532925199433  # degree to radian 
   rd = 57.29577951308232   # radian to degree
   pi = 3.14159265358979

def fix(x):
   if(x >= 0) :
      return (math.floor(math.fabs(x)))
   else:
      return (-math.floor(math.fabs(x)))

def rnd36(x):
      return (x - math.floor(x / 360) * 360)

def sgn(x):
      if   (x < 0):
          return -1
      elif (x > 0):
          return 1
      else:
          return 0

# 年初からの経過日数 
def tz_serial(year,month,day):
    m = [31,31,28,31,30,31,30,31,31,30,31,30,31] # /* 各月の日数 */

    d = 0
    for  i in range (1,month):
         d += m[i]
    d += day - 1

    # 潮汐計算用通日 tz #
    tz = d + (int)(fix((year + 3) / 4)) - 500
    return tz


class Port(object):
   def __init__(self):
 
      self.name = ""                                   # 港
      self.lat, self.lng  = [0,0]                      # 緯度、経度
      self.level, self.flood, self.ebb = [0,0,0]       # 平均、満潮、干潮の水面高
      self.date = ""                                   # JST (+9hr) UTC 
      self.itv  = 20
   
      self.hr  = np.zeros(40,np.float64)               # 調和定数
      self.pl  = np.zeros(40,np.float64)               # 調和定数

      #self.tl  = np.zeros(285,np.float64)              # 潮位

class Tide(object):
      def __init__(self,port):

         self.name = port.name
         self.lat  = port.lat
         self.lng  = port.lng
         self.itv  = port.itv
         self.date = port.date
         self.level= port.level
         self.hr   = port.hr
         self.pl   = port.pl
         self.tl   = np.zeros(285,np.float64)

      def tide(self,port):
         tstr = str(self.date)
         d = datetime.datetime.strptime(tstr,'%Y/%m/%d')

         year = int(d.year)
         month= int(d.month)
         day  = int(d.day)

         inc = int(24*60*2/self.itv)+2   
         
         nc = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
               2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,4,4,6,6] # 分潮の波数 

         ags = [0.0410686,0.0821373,0.5443747,1.0158958,1.0980331, \
               13.3986609,13.4715145,13.9430356,14.0251729,14.4920521, \
               14.9178647,14.9589314,15.0000000,15.0410686,15.0821353, \
               15.1232059,15.5854433,16.0569644,16.1391017,27.8953548, \
               27.9682084,28.4397295,28.5125831,28.9019669,28.9841042, \
               29.4556253,29.5284789,29.9589333,30.0000000,30.0410667, \
               30.0821373,31.0158958,42.9271398,43.4761563,44.0251729, \
               45.0410686,57.9682084,58.9841042,86.9523127,87.9682084] #  分潮の角速度 

         vl = np.zeros(40,np.float64) #  天文引数 
         f = np.zeros(40,np.float64) #  天文因数 
         v = np.zeros(40,np.float64)
         u = np.zeros(40,np.float64)
         f0 = np.zeros(10,np.float64)
         u0 = np.zeros(10,np.float64)

         tz = tz_serial(year,month,day)

         # 太陽・月の軌道要素 s, h, p, n #
         ty = year - 2000
         s = rnd36(211.728 + rnd36(129.38471 * ty) + rnd36(13.176396 * tz))
         h = rnd36(279.974 + rnd36(-0.23871  * ty) + rnd36(0.985647 * tz))
         p = rnd36(83.298  + rnd36(40.66229  * ty) + rnd36(0.111404 * tz))
         n = rnd36(125.071 + rnd36(-19.32812 * ty) + rnd36(-0.052954 * tz))

         # 天文引数を求める #
         v[0] = h
         v[1] = 2 * h 
         v[2] = s - p
         v[5] = -3 * s + h + p + 270
         v[6] = -3 * s + 3 * h - p + 270
         v[7] = -2 * s + h + 270
         v[8] = -2 * s + 3 * h - 270
         v[9] = -s + h + 90
         v[10] = -2 * h + 192
         v[11] = -h + 270
         v[12] = 180
         v[13] = h + 90
         v[14] = 2 * h + 168
         v[15] = 3 * h + 90
         v[16] = s + h - p +  90
         v[17] = 2 * s - h - 270
         v[18] = 2 * s + h + 90
         v[19] = -4 * s + 2 * h + 2 * p
         v[20] = -4 * s + 4 * h
         v[21] = -3 * s + 2 * h + p
         v[22] = -3 * s + 4 * h - p
         v[23] = -2 * s + 180
         v[24] = -2 * s + 2 * h
         v[25] = -s + p + 180
         v[26] = -s + 2 * h - p + 180
         v[27] = -h + 282
         v[28] = 0
         v[29] = h + 258
         v[30] = 2 * h
         v[31] = 2 * s - 2 * h
         v[32] = -4 * s + 3 * h + 270
         v[33] = -3 * s + 3 * h + 180
         v[34] = -2 * s + 3 * h + 90
         v[35] = h + 90
         v[36] = -4 * s + 4 * h
         v[37] = -2 * s + 2 * h
         v[38] = -6 * s + 6 * h
         v[39] = -4 * s + 4 * h

         n1 = math.sin(n * lib.dr)
         n2 = math.sin(rnd36(n * 2) * lib.dr);
         n3 = math.sin(rnd36(n * 3) * lib.dr);

         u0[0] = 0
         u0[1] = -23.74 * n1 + 2.68 * n2 - 0.38 * n3
         u0[2] = 10.80 * n1 - 1.34 * n2 + 0.19 * n3
         u0[3] = -8.86 * n1 + 0.68 * n2 - 0.07 * n3
         u0[4] = -12.94 * n1 + 1.34 * n2 - 0.19 * n3
         u0[5] = -36.68 * n1 + 4.02 * n2 - 0.57 * n3
         u0[6] = -2.14 * n1
         u0[7] = -17.74 * n1 + 0.68 * n2 - 0.04 * n3

         cu = 1 - 0.2505 * math.cos(p * 2 * lib.dr) \
            - 0.1102 * math.cos((p * 2 - n) * lib.dr) \
            - 0.0156 * math.cos((p * 2 - n * 2) * lib.dr) \
            - 0.0370 * math.cos(n * lib.dr)

         su = -0.2505 * math.sin(p * 2 * lib.dr) \
            - 0.1102 * math.sin((p * 2 - n) * lib.dr) \
            - 0.0156 * math.sin((p * 2 - n * 2) * lib.dr) \
            - 0.0370 * math.sin(n * lib.dr)

         u0[8] = math.atan2(su, cu) * lib.rd

         cu = 2 * math.cos(p * lib.dr) + 0.4 * math.cos((p - n) * lib.dr)
         su = math.sin(p * lib.dr) + 0.2 * math.cos((p - n) * lib.dr)

         u0[9] = math.atan2(su, cu) * lib.rd

         u[0] = 0
         u[1] = 0
         u[2] = 0
         u[3] = -u0[6]
         u[4] = u0[1]
         u[5] = u0[2]
         u[6] = u0[2]
         u[7] = u0[2]
         u[8] = u0[6]
         u[9] = u0[9]
         u[10] = 0
         u[11] = 0
         u[12] = 0
         u[13] = u0[3]
         u[14] = 0
         u[15] = 0
         u[16] = u0[4]
         u[17] = -u0[2]
         u[18] = u0[5]
         u[19] = u0[6]
         u[20] = u0[6]
         u[21] = u0[6]
         u[22] = u0[6]
         u[23] = u0[2]
         u[24] = u0[6]
         u[25] = u0[6]
         u[26] = u0[8]
         u[27] = 0
         u[28] = 0
         u[29] = 0
         u[30] = u0[7]
         u[31] = -u0[6]
         u[32] = u0[6] + u0[2]
         u[33] = u0[6] * 1.5
         u[34] = u0[6] + u0[3]
         u[35] = u0[3]
         u[36] = u0[6] * 2
         u[37] = u0[6]
         u[38] = u0[6] * 3
         u[39] = u0[6] * 2

         zt =135 # 日本標準時

         for i in range (0,40):
            v[i] = rnd36(v[i] + u[i])
            vl[i] =rnd36(v[i] + self.lng * nc[i] - ags[i] * zt / 15)

         #  天文因数 f 

         n1 = math.cos(n * lib.dr)
         n2 = math.cos(rnd36(n * 2) * lib.dr)
         n3 = math.cos(rnd36(n * 3) * lib.dr)

         f0[0] = 1.0000 - 0.1300 * n1 + 0.0013 * n2
         f0[1] = 1.0429 + 0.4135 * n1 - 0.0040 * n2
         f0[2] = 1.0089 + 0.1871 * n1 - 0.0147 * n2 + 0.0014 * n3
         f0[3] = 1.0060 + 0.1150 * n1 - 0.0088 * n2 + 0.0006 * n3
         f0[4] = 1.0129 + 0.1676 * n1 - 0.0170 * n2 + 0.0016 * n3
         f0[5] = 1.1027 + 0.6504 * n1 + 0.0317 * n2 - 0.0014 * n3
         f0[6] = 1.0004 - 0.0373 * n1 + 0.0002 * n2
         f0[7] = 1.0241 + 0.2863 * n1 + 0.0083 * n2 - 0.0015 * n3

         cu = 1 - 0.2505 * math.cos(p * 2 * lib.dr) \
            - 0.1102 * math.cos((p * 2 - n) * lib.dr) \
            - 0.0156 * math.cos((p * 2 - n * 2) * lib.dr) \
            - 0.0370 * math.cos(n * lib.dr)

         su = -0.2505 * math.sin(p * 2 * lib.dr) \
            - 0.1102 * math.sin((p * 2 - n) * lib.dr) \
            - 0.0156 * math.sin((p * 2 - n * 2) * lib.dr) \
            - 0.0370 * math.sin(n * lib.dr)

         arg = math.atan2(su, cu) * lib.rd

         f0[8] = su / math.sin(arg * lib.dr);

         cu = 2 * math.cos(p * lib.dr) \
            + 0.4 * math.cos((p - n) * lib.dr)
         su = math.sin(p * lib.dr) \
            + 0.2 * math.cos((p - n) * lib.dr)
         arg = math.atan2(su, cu) * lib.rd

         f0[9] = cu / math.cos(arg * lib.dr)

         f[0] = 1
         f[1] = 1
         f[2] = f0[0]
         f[3] = f0[6]
         f[4] = f0[1]
         f[5] = f0[2]
         f[6] = f0[2]
         f[7] = f0[2]
         f[8] = f0[6]
         f[9] = f0[9]
         f[10] = 1
         f[11] = 1
         f[12] = 1
         f[13] = f0[3]
         f[14] = 1
         f[15] = 1
         f[16] = f0[4]
         f[17] = f0[2]
         f[18] = f0[5]
         f[19] = f0[6]
         f[20] = f0[6]
         f[21] = f0[6]
         f[22] = f0[6]
         f[23] = f0[2]
         f[24] = f0[6]
         f[25] = f0[6]
         f[26] = f0[8]
         f[27] = 1
         f[28] = 1
         f[29] = 1
         f[30] = f0[7]
         f[31] = f0[6]
         f[32] = f0[6] * f0[2]
         f[33] = math.pow(f0[6], 1.5)
         f[34] = f0[6] * f0[3]
         f[35] = f0[3]
         f[36] = math.pow(f0[6], 2)
         f[37] = f0[6]
         f[38] = math.pow(f0[6], 3)
         f[39] = math.pow(f0[6], 2)

         dcnt  = 0
         cnt   = 0

         for i in range(0,inc+3):
           self.tl[i] = self.level
           for j in range(0,40):
              self.tl[i] += f[j] * self.hr[j] * math.cos((vl[j] \
                          + ags[j] * (i - 2) / (60 / self.itv) - self.pl[j]) * lib.dr)
      
"""
築地（東京）での潮位

<param name="port" value="築地H4,35.40,139.46,120">
<param name="pl" value="151.80,106.30,0.50,15.20,349.80,153.60,0.00,166.60,0.00,193.30,0.00,181.00,76.60,184.40,0.00,0.00,202.00,0.00,0.00,0.00,196.80,158.30,177.00,0.00,162.40,0.00,163.50,198.50,193.00,94.80,183.50,6.60,0.00,170.60,0.00,0.00,145.40,165.20,208.70,0.00">
<param name="hr" value="9.80,3.60,1.60,2.60,1.10,4.00,0.00,18.60,0.00,0.60,0.00,8.20,1.80,24.60,0.00,0.00,1.20,0.00,0.00,0.00,1.50,7.30,2.60,0.00,50.10,0.00,2.20,1.80,23.90,0.20,7.80,1.40,0.00,1.80,0.00,0.00,0.90,2.60,0.40,0.00">
"""
   
pt = Port

pt.name = "築地H4"

pt.lat = 35.40
pt.lng =139.46
pt.level=120
pt.pl = [151.80,106.30,0.50,15.20,349.80,153.60,\
           0.00,166.60,0.00,193.30,0.00,181.00,76.60,\
         184.40,0.00,0.00,202.00,0.00,0.00,0.00,196.80,\
         158.30,177.00,0.00,162.40,0.00,163.50,198.50,\
         193.00,94.80,183.50,6.60,0.00,170.60,0.00,0.00,\
         145.40,165.20,208.70,0.00]

pt.hr = [9.80,3.60,1.60,2.60,1.10,4.00,0.00,18.60,0.00,0.60,\
         0.00,8.20,1.80,24.60,0.00,0.00,1.20,0.00,0.00,0.00,\
         1.50,7.30,2.60,0.00,50.10,0.00,2.20,1.80,23.90,0.20,\
         7.80,1.40,0.00,1.80,0.00,0.00,0.90,2.60,0.40,0.00]

pt.date = '2016/07/11'
pt.itv  = 20
