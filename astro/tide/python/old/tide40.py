"""
tide.pl

2016/07/10

Author: Ichiro Yoshida

潮汐算出 version 1.0
"""
import math
import datetime
import numpy as np
from scipy.interpolate import interp1d
from flood_ebb import *

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

# 月の日数
def month_days(year,month):
    if (month < 0 or month > 12): return (-1)
    d = 0

    m = [31,31,28,31,30,31,30,31,31,30,31,30,31] # /* 各月の日数 */

    if ((year % 4 == 0 and year % 100 !=0) or year % 400 == 0 ): # 閏年
         m[2] = 29
    
    return (m[month])


# 年初からの経過日数 
def day_serial(year,month,day):
    d = 0
    m = [31,31,28,31,30,31,30,31,31,30,31,30,31] # /* 各月の日数 */

    if ((year % 4 == 0 and year % 100 !=0) or year % 400 == 0 ): # 閏年
         m[2] = 29
    
    for  i in range (1,month):
         d += m[i]
    d += day - 1

    return d

class Port(object):
   def __init__(self):
 
      self.name = ""                                   # 港
      self.lat, self.lng  = [0,0]                      # 緯度、経度
      self.level, self.flood, self.ebb = [0,0,0]       # 平均、満潮、干潮の水面高
      self.date = ""                                   # JST (+9hr) UTC 
  
      self.hr  = np.zeros(40,np.float64)               # 調和定数（振幅）
      self.pl  = np.zeros(40,np.float64)               # 調和定数（遅角）
      
class Tide(object):
      def __init__(self,port):
         itv       = 20                                #計算間隔２０分
         self.name = port.name
         self.lat  = port.lat
         self.lng  = port.lng
         self.date = port.date
         self.level= port.level
         self.hr   = port.hr
         self.pl   = port.pl
         self.inc = int(24*60/itv)+2   #１日（２４時間x６０分／計算間隔）の計算回数
         self.tl  = np.zeros(self.inc+3,np.float64)

         #----------------------
         self.hitide = []
         self.lowtide= []
         #self.tide   = np.zeros(1440,np.float64)
        
      def tide(self,port):
         itv  = 20 
        
         ags  = np.zeros(40,np.float64)

         tstr = str(self.date)
         d = datetime.datetime.strptime(tstr,'%Y/%m/%d')

         year = int(d.year)
         month= int(d.month)
         day  = int(d.day)

         nc = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
               2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,4,4,6,6]  # 分潮の波数 (cycle of constituent) 

         #angular speed  分潮の角速度

         ags[0] =  0.0410686          #Sa
         ags[1] =  0.0821373          #Ssa
         ags[2] =  0.5443747          #Mm
         ags[3] =  1.0158958          #MSf
         ags[4] =  1.0980331          #Mf
         ags[5] = 13.3986609          #Q1
         ags[6] = 13.4715145          #Rho1
         ags[7] = 13.9430356          #O1
         ags[8] = 14.0251729          #MP1
         ags[9] = 14.4920521          #M1
         ags[10] = 14.9178647         #Pi1
         ags[11] = 14.9589314         #P1
         ags[12] = 15.0000000         #S1
         ags[13] = 15.0410686         #K1
         ags[14] = 15.0821353         #Psi1
         ags[15] = 15.1232059          #Phi1
         ags[16] = 15.5854433          #J1
         ags[17] = 16.0569644          #SO1
         ags[18] = 16.1391017          #OO1
         ags[19] = 27.8953548          #2N2
         ags[20] = 27.9682084          #Mu2
         ags[21] = 28.4397295          #N2
         ags[22] = 28.5125831          #Nu2
         ags[23] = 28.9019669          #OP2
         ags[24] = 28.9841042          #M2
         ags[25] = 29.4556253          #Lam2
         ags[26] = 29.5284789          #L2
         ags[27] = 29.9589333          #T2
         ags[28] = 30.0000000          #S2
         ags[29] = 30.0410667          #R2
         ags[30] = 30.0821373          #K2
         ags[31] = 31.0158958          #2SM2
         ags[32] = 42.9271398          #MO3
         ags[33] = 43.4761563          #M3
         ags[34] = 44.0251729          #MK3
         ags[35] = 45.0410686          #SK3
         ags[36] = 57.9682084          #M4
         ags[37] = 58.9841042          #MS4
         ags[38] = 86.9523127          #M6
         ags[39] = 87.9682084          #2MS6
 
         vl = np.zeros(40,np.float64) #  天文引数 
         f = np.zeros(40,np.float64) #  天文因数 
         v = np.zeros(40,np.float64)
         u = np.zeros(40,np.float64)
         f0 = np.zeros(10,np.float64)
         u0 = np.zeros(10,np.float64)

         d = day_serial(year,month,day)
         # 潮汐計算用通日 tz #
         tz = d + int(fix((year + 3) / 4)) - 500

         # 太陽・月の軌道要素 s, h, p, n #
         ty = year - 2000
         s = rnd36( 211.728 + rnd36( 129.38471 * ty) + rnd36( 13.176396 * tz)) #月の平均黄経
         h = rnd36( 279.974 + rnd36(  -0.23871 * ty) + rnd36(  0.985647 * tz)) #太陽の平均黄経
         p = rnd36(  83.298 + rnd36(  40.66229 * ty) + rnd36(  0.111404 * tz)) #月の近地点の平均黄経
         n = rnd36( 125.071 + rnd36( -19.32812 * ty) + rnd36( -0.052954 * tz)) #月の昇交点の平均黄経

         # 天文引数を求める #
         # 海上保安庁　書誌第７４２号　日本沿岸　潮汐調和定数表　第１表
         v[0] = h
         v[1] = 2 * h 
         v[2] = s - p
         v[3] = 2 * s - 2 * h
         v[4] = 2 * s
         v[5] = -3 * s + h + p + 270
         v[6] = -3 * s + 3 * h - p + 270
         v[7] = -2 * s + h + 270
         v[8] = -2 * s + 3 * h - 270
         v[9] = -s + h + 90
         #v[10] = -2 * h + 192    # S58
         v[10] = -2 * h + 193     # H4
         v[11] = -h + 270
         v[12] = 180
         v[13] = h + 90
         v[14] = 2 * h + 168
         v[15] = 3 * h + 90
         v[16] = s + h - p +  90
         #v[17] = 2 * s - h - 270  # S58
         v[17] = 2 * s - h + 90    # H4
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

         s1 = math.sin(      n      * lib.dr)
         s2 = math.sin(rnd36(n * 2) * lib.dr)
         s3 = math.sin(rnd36(n * 3) * lib.dr)

         u0[0] =   0
         u0[1] = -23.74 * s1 + 2.68 * s2 - 0.38 * s3
         u0[2] =  10.80 * s1 - 1.34 * s2 + 0.19 * s3
         u0[3] =  -8.86 * s1 + 0.68 * s2 - 0.07 * s3
         u0[4] = -12.94 * s1 + 1.34 * s2 - 0.19 * s3
         u0[5] = -36.68 * s1 + 4.02 * s2 - 0.57 * s3
         u0[6] =  -2.14 * s1
         u0[7] = -17.74 * s1 + 0.68 * s2 - 0.04 * s3

         cu = 1 - 0.2505 * math.cos( p * 2 * lib.dr) \
                - 0.1102 * math.cos((p * 2 - n) * lib.dr) \
                - 0.0156 * math.cos((p * 2 - n * 2) * lib.dr) \
                - 0.0370 * math.cos(n * lib.dr)

         su =   - 0.2505 * math.sin(p * 2 * lib.dr) \
                - 0.1102 * math.sin((p * 2 - n) * lib.dr) \
                - 0.0156 * math.sin((p * 2 - n * 2) * lib.dr) \
                - 0.0370 * math.sin(n * lib.dr)

         u0[8] = math.atan2(su, cu) * lib.rd

         cu =    2 * math.cos(p * lib.dr) \
             + 0.4 * math.cos((p - n) * lib.dr)

         su =        math.sin(p * lib.dr)\
             + 0.2 * math.cos((p - n) * lib.dr)

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

         # 海上保安庁　書誌７４２号　日本沿岸　潮汐調和定数表　第２表
         f0[0] = 1.0000 - 0.1300 * n1 + 0.0013 * n2
         f0[1] = 1.0429 + 0.4135 * n1 - 0.0040 * n2
         f0[2] = 1.0089 + 0.1871 * n1 - 0.0147 * n2 + 0.0014 * n3
         f0[3] = 1.0060 + 0.1150 * n1 - 0.0088 * n2 + 0.0006 * n3
         f0[4] = 1.0129 + 0.1676 * n1 - 0.0170 * n2 + 0.0016 * n3
         f0[5] = 1.1027 + 0.6504 * n1 + 0.0317 * n2 - 0.0014 * n3
         f0[6] = 1.0004 - 0.0373 * n1 + 0.0002 * n2
         f0[7] = 1.0241 + 0.2863 * n1 + 0.0083 * n2 - 0.0015 * n3

         # L2
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

         # Mi
         cu = 2 * math.cos(p * lib.dr) \
            + 0.4 * math.cos((p - n) * lib.dr)
         su = math.sin(p * lib.dr) \
            + 0.2 * math.cos((p - n) * lib.dr)
         arg = math.atan2(su, cu) * lib.rd

         f0[9] = cu / math.cos(arg * lib.dr)

# tTidePredict.CoefficF;

         f[0] = 1                       #Sa
         f[1] = 1                       #Ssa
         f[2] = f0[0]                   #Mm
         f[3] = f0[6]                   #MSf
         f[4] = f0[1]                   #Mf
         f[5] = f0[2]                   #Q1
         f[6] = f0[2]                   #Rho1
         f[7] = f0[2]                   #O1
         f[8] = f0[6]                   #MP1
         f[9] = f0[9]                   #M1
         f[10] = 1                      #Pi1
         f[11] = 1                      #P1
         f[12] = 1                      #S1
         f[13] = f0[3]                  #K1
         f[14] = 1                      #Psi1
         f[15] = 1                      #Phi1
         f[16] = f0[4]                  #J1
         f[17] = f0[2]                  #SO1
         f[18] = f0[5]                  #OO1
         f[19] = f0[6]                  #2N2
         f[20] = f0[6]                  #Mu2
         f[21] = f0[6]                  #N2
         f[22] = f0[6]                  #Nu2
         f[23] = f0[2]                  #OP2
         f[24] = f0[6]                  #M2
         f[25] = f0[6]                  #Lam2
         f[26] = f0[8]                  #L2
         f[27] = 1                      #T2
         f[28] = 1                      #S2
         f[29] = 1                      #R2
         f[30] = f0[7]                  #K2
         f[31] = f0[6]                  #2SM2
         f[32] = f0[6] * f0[2]          #MO3
         f[33] = math.pow(f0[6], 1.5)   #M3
         f[34] = f0[6] * f0[3]          #MK3
         f[35] = f0[3]                  #SK3
         f[36] = math.pow(f0[6], 2)     #M4
         f[37] = f0[6]                  #MS4
         f[38] = math.pow(f0[6], 3)     #M6
         f[39] = math.pow(f0[6], 2)     #2MS6

         dcnt  = 0
         cnt   = 0

         #hr[]:振幅、ags[]：角速度、pl[]：遅角
         for i in range(0,self.inc+3):
           self.tl[i] = self.level
           for j in range(0,40):
              self.tl[i] += f[j] * self.hr[j] * math.cos((vl[j] \
                          + ags[j] * (i - 2) / (60 /itv) \
                          - self.pl[j]) * lib.dr)

         #補間し１分毎の潮位を算出
         len_tl=len(self.tl)
         range_tl = -40+20*len_tl
         time       = np.arange(-40,range_tl,20)
         func_level = interp1d(time,self.tl,kind='cubic')

         func_time = np.arange(-40,1480,1)
         func_tide = func_level(func_time)

         #満潮と干潮（時刻：分、潮位）
         self.hitide, self.lowtide = flood_ebb(func_time,func_tide)

         self.tide = func_tide[40:1480]
