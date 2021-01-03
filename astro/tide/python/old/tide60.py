"""
tide.pl

2016/09/11 ６０分潮計算

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
  
      self.hr  = np.zeros(60,np.float64)               # 調和定数（振幅）
      self.pl  = np.zeros(60,np.float64)               # 調和定数（遅角）

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

         self.hitide = []
         self.lowtide= []
        
      def tide(self,port):
         itv  = 20 
       
         nc   = np.zeros(60,np.float64)
         ags  = np.zeros(60,np.float64)

         tstr = str(self.date)
         d = datetime.datetime.strptime(tstr,'%Y/%m/%d')

         year = int(d.year)
         month= int(d.month)
         day  = int(d.day)

         # *****   海上保安庁　日本沿岸　潮汐調和定数表　第１表   *****

         # 分潮の波数 (cycle of constituent)

         nc[0] = 0                    # 1    	Sa
         nc[1] = 0                    # 2 	Ssa
         nc[2] = 0                    # 3       Mm
         nc[3] = 0                    # 4       MSf
         nc[4] = 0                    # 5       Mf
         nc[5] = 1                    # 6       2Q1
         nc[6] = 1                    # 7       Sig1
         nc[7] = 1                    # 8       Q1
         nc[8] = 1                    # 9       Rho1
         nc[9] = 1                    #10       O1
         nc[10]= 1                    #11       MP1
         nc[11]= 1                    #12       M1
         nc[12]= 1                    #13       Chi1
         nc[13]= 1                    #14       Pi1
         nc[14]= 1                    #15       P1
         nc[15]= 1                    #16       S1
         nc[16]= 1                    #17       K1
         nc[17]= 1                    #18       Psi1
         nc[18]= 1                    #19       Phi1
         nc[19]= 1                    #20       The1
         nc[20]= 1                    #21       J1
         nc[21]= 1                    #22       SO1
         nc[22]= 1                    #23       OO1
         nc[23]= 2                    #24       OQ2
         nc[24]= 2                    #25       MNS2
         nc[25]= 2                    #26       2N2
         nc[26]= 2                    #27       Mu2
         nc[27]= 2                    #28       N2
         nc[28]= 2                    #29       Nu2
         nc[29]= 2                    #30       OP2
         nc[30]= 2                    #31       M2
         nc[31]= 2                    #32       MKS2
         nc[32]= 2                    #33       Lam2
         nc[33]= 2                    #34       L2
         nc[34]= 2                    #35       T2
         nc[35]= 2                    #36       S2
         nc[36]= 2                    #37       R2
         nc[37]= 2                    #38       K2
         nc[38]= 2                    #39       MSN2
         nc[39]= 2                    #40       KJ2
         nc[40]= 2                    #41       2SM2
         nc[41]= 3                    #42       MO3
         nc[42]= 3                    #43       M3
         nc[43]= 3                    #44       SO3
         nc[44]= 3                    #45       MK3
         nc[45]= 3                    #46       SK3
         nc[46]= 4                    #47       MN4
         nc[47]= 4                    #48       M4
         nc[48]= 4                    #49       SN4
         nc[49]= 4                    #50       MS4
         nc[50]= 4                    #51       MK4
         nc[51]= 4                    #52       S4
         nc[52]= 4                    #53       SK4
         nc[53]= 6                    #54       2MN6
         nc[54]= 6                    #55       M6
         nc[55]= 6                    #56       MSN6
         nc[56]= 6                    #57       2MS6
         nc[57]= 6                    #58       2MK6
         nc[58]= 6                    #59       2SM6
         nc[59]= 6                    #60       MSK6


         #angular speed  分潮の角速度

         ags[0] =  0.0410686          # 1       Sa
         ags[1] =  0.0821373          # 2       Ssa
         ags[2] =  0.5443747          # 3       Mm
         ags[3] =  1.0158958          # 4       MSf
         ags[4] =  1.0980331          # 5       Mf
         ags[5] = 12.8542862          # 6       2Q1
         ags[6] = 12.9271398          # 7       Sig1
         ags[7] = 13.3986609          # 8       Q1
         ags[8] = 13.4715145          # 9       Rho1
         ags[9] = 13.9430356          #10       O1
         ags[10]= 14.0251729          #11       MP1
         ags[11]= 14.4920521          #12       M1
         ags[12]= 14.5695476          #13       Chi1
         ags[13]= 14.9178647          #14       Pi1
         ags[14]= 14.9589314          #15       P1
         ags[15]= 15.0000000          #16       S1
         ags[16]= 15.0410686          #17       K1
         ags[17]= 15.0821353          #18       Psi1
         ags[18]= 15.1232059          #19       Phi1
         ags[19]= 15.5125897          #20       The1
         ags[20]= 15.5854433          #21       J1
         ags[21]= 16.0569644          #22       SO1
         ags[22]= 16.1391017          #23       OO1
         ags[23]= 27.3416964          #24       OQ2
         ags[24]= 27.4238337          #25       MNS2
         ags[25]= 27.8953548          #26       2N2
         ags[26]= 27.9682084          #27       Mu2
         ags[27]= 28.4397295          #28       N2
         ags[28]= 28.5125831          #29       Nu2
         ags[29]= 28.9019669          #30       OP2
         ags[30]= 28.9841042          #31       M2
         ags[31]= 29.0662415          #32       MKS2
         ags[32]= 29.4556253          #33       Lam2
         ags[33]= 29.5284789          #34       L2
         ags[34]= 29.9589333          #35       T2
         ags[35]= 30.0000000          #36       S2
         ags[36]= 30.0410667          #37       R2
         ags[37]= 30.0821373          #38       K2
         ags[38]= 30.5443747          #39       MSN2
         ags[39]= 30.6265120          #40       KJ2
         ags[40]= 31.0158958          #41       2SM2
         ags[41]= 42.9271398          #42       MO3
         ags[42]= 43.4761563          #43       M3
         ags[43]= 43.9430356          #44       SO3
         ags[44]= 44.0251729          #45       MK3
         ags[45]= 45.0410686          #46       SK3
         ags[46]= 57.4238337          #47       MN4
         ags[47]= 57.9682084          #48       M4
         ags[48]= 58.4397295          #49       SN4
         ags[49]= 58.9841042          #50       MS4
         ags[50]= 59.0662415          #51       MK4
         ags[51]= 60.0000000          #52       S4
         ags[52]= 60.0821373          #53       SK4
         ags[53]= 86.4079380          #54       2MN6
         ags[54]= 86.9523127          #55       M6
         ags[55]= 87.4238337          #56       MSN6
         ags[56]= 87.9682084          #57       2MS6
         ags[57]= 88.0503457          #58       2MK6
         ags[58]= 88.9841042          #59       2SM6
         ags[59]= 89.0662415          #60       MSK6
 
         vl = np.zeros(60,np.float64) #  天文引数 
         f = np.zeros(60,np.float64) #  天文因数 
         v = np.zeros(60,np.float64)
         u = np.zeros(60,np.float64)
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

         # 海上保安庁　書誌第７４２号　日本沿岸　潮汐調和定数表　第１表

         v[0] =          h                # 1     Sa
         v[1] =        2*h                # 2     Ssa
         v[2] =    s         -p           # 3     Mm
         v[3] =  2*s  -2*h                # 4     MSf
         v[4] =  2*s                      # 5     Mf
         v[5] = -4*s    +h +2*p +270      # 6     2Q1
         v[6] = -4*s  +3*h      +270      # 7     Sig1
         v[7] = -3*s  +  h +  p +270      # 8     Q1
         v[8] = -3*s  +3*h -  p +270      # 9     Rho1
         v[9] = -2*s  +  h      +270      #10     O1
         v[10]= -2*s  +3*h      + 90      #11     MP1
         v[11]= -  s  +  h      + 90      #12     M1
         v[12]= -  s  +3*h -  p + 90      #13     Ki1
         v[13]=       -2*h      +193      #14     Pi1
         v[14]=       -  h      +270      #15     P1
         v[15]=                 +180      #16     S1
         v[16]=       +  h      + 90      #17     K1
         v[17]=       +2*h      +167      #18     Psi1
         v[18]=       +3*h      + 90      #19     Phi1
         v[19]=    s  -  h +  p + 90      #20     The1
         v[20]=    s  +  h -  p + 90      #21     J1
         v[21]=  2*s  -  h      + 90      #22     SO1
         v[22]=  2*s  +  h      + 90      #23     OO1
         v[23]= -5*s  +2*h +  p +180      #24     OQ2
         v[24]= -5*s  +4*h +  p           #25     MNS2
         v[25]= -4*s  +2*h +2*p           #26     2N2
         v[26]= -4*s  +4*h                #27     Mu2
         v[27]= -3*s  +2*h +  p           #28     N2
         v[28]= -3*s  +4*h -  p           #29     Nu2
         v[29]= -2*s            +180      #30     OP2
         v[30]= -2*s  +2*h                #31     M2
         v[31]= -2*s  +4*h                #32     MKS2
         v[32]= -  s       +  p +180      #33     Ram2
         v[33]= -  s  +2*h -  p +180      #34     L2
         v[34]=       -  h      +283      #35     T2
         v[35]= 0                         #36     S2
         v[36]=       +  h      +257      #37     R2
         v[37]=       +2*h                #38     K2
         v[38]=    s       -  p           #39     MSN2
         v[39]=    s  +2*h -  p +180      #40     KJ2
         v[40]=  2*s  -2*h                #41     2SM2
         v[41]= -4*s  +3*h      +270      #42     MO3
         v[42]= -3*s  +3*h      +180      #43     M3
         v[43]= -2*s  +  h      +270      #44     SO3
         v[44]= -2*s  +3*h      + 90      #45     MK3
         v[45]=       +  h      + 90      #46     SK3
         v[46]= -5*s  +4*h +  p           #47     MN4
         v[47]= -4*s  +4*h                #48     M4
         v[48]= -3*s  +2*h +  p           #49     SN4
         v[49]= -2*s  +2*h                #50     MS4
         v[50]= -2*s  +4*h                #51     MK4
         v[51]= 0                         #52     S4
         v[52]=       +2*h                #53     SK4
         v[53]= -7*s  +6*h +  p           #54     2MN6
         v[54]= -6*s  +6*h                #55     M6
         v[55]= -5*s  +4*h +  p           #56     MSN6
         v[56]= -4*s  +4*h                #57     2MS6
         v[57]= -4*s  +6*h                #58     2MK6
         v[58]= -2*s  +2*h                #59     2SM6
         v[59]= -2*s  +4*h                #60     MSK6


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

         # Nの補正　　（第２表　uiの係数）

         u[0] =      0         # 1    Sa
         u[1] =      0         # 2    Ssa
         u[2] =  u0[0]         # 3    Mm
         u[3] = -u0[6]         # 4    MSf
         u[4] =  u0[1]         # 5    Mf
         u[5] =  u0[2]         # 6    2Q1
         u[6] =  u0[2]         # 7    Sig1
         u[7] =  u0[2]         # 8    Q1
         u[8] =  u0[2]         # 9    Rho1
         u[9] =  u0[2]         #10    O1
         u[10] = u0[6]         #11    MP1
         u[11] = u0[9]         #12    M1
         u[12] = u0[4]         #13    Ki1
         u[13] =     0         #14    Pi1
         u[14] =     0         #15    P1
         u[15] =     0         #16    S1
         u[16] = u0[3]         #17    K1
         u[17] =     0         #18    Psi1
         u[18] =     0         #19    Phi1
         u[19] = u0[4]         #20    The1
         u[20] = u0[4]         #21    J1
         u[21] =-u0[2]         #22    SO1
         u[22] = u0[5]         #23    OO1
         u[23] = u0[2] * 2     #24    OQ2
         u[24] = u0[6] * 2     #25    MNS2
         u[25] = u0[6]         #26    2N2
         u[26] = u0[6]         #27    Mu2
         u[27] = u0[6]         #28    N2
         u[28] = u0[6]         #29    Nu2
         u[29] = u0[2]         #30    OP2
         u[30] = u0[6]         #31    M2
         u[31] = u0[6]+u0[7]   #32    MKS2
         u[32] = u0[6]         #33    Lam2
         u[33] = u0[8]         #34    L2
         u[34] = 0             #35    T2
         u[35] = 0             #36    S2
         u[36] = 0             #37    R2
         u[37] = u0[7]         #38    K2
         u[38] = u0[6] * 2     #39    MSN2
         u[39] = u0[3] + u0[4] #40    KJ2
         u[40] =-u0[6]         #41    2SM2
         u[41] = u0[6] + u0[2] #42    MO3
         u[42] = u0[6] * 1.5   #43    M3
         u[44] = u0[6] + u0[3] #45    MK3
         u[45] = u0[3]         #46    SK3
         u[46] = u0[6] * 2     #47    MN4
         u[47] = u0[6] * 2     #48    M4
         u[48] = u0[6]         #49    SN4
         u[49] = u0[6]         #50    MS4
         u[50] = u0[6]+u0[7]   #51    MK4
         u[51] = 0             #52    S4
         u[52] = u0[7]         #53    SK4
         u[53] = u0[6] * 3     #54    2MN6
         u[54] = u0[6] * 3     #55    M6
         u[55] = u0[6] * 2     #56    MSN6
         u[56] = u0[6] * 2         #57    2MS6
         u[57] = u0[6] * 2 +u0[7]  #58    2MK6
         u[58] = u0[6]             #59    2SM6
         u[59] = u0[6] + u0[7]     #60    MSK6

         zt =135 # 日本標準時

         for i in range (0,60):
            v[i] = rnd36(v[i] + u[i])
            vl[i] =rnd36(v[i] + float(self.lng) * nc[i] - ags[i] * zt / 15)

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

         # Nの補正（第２表 fiの係数） 

         f[0]  = 1                       # 1     Sa
         f[1]  = 1                       # 2     Ssa
         f[2]  = f0[0]                   # 3     Mm
         f[3]  = f0[6]                   # 4     MSf
         f[4]  = f0[1]                   # 5     Mf
         f[5]  = f0[2]                   # 6     2Q1
         f[6]  = f0[2]                   # 7     Sig1
         f[7]  = f0[2]                   # 8     Q1
         f[8]  = f0[2]                   # 9     Rho1
         f[9]  = f0[2]                   #10     O1
         f[10] = f0[6]                   #11     MP1
         f[11] = f0[9]                   #12     M1
         f[12] = f0[4]                   #13     Ki1
         f[13] = 1                       #14     Pi1
         f[14] = 1                       #15     P1
         f[15] = 1                       #16     S1
         f[16] = f0[3]                   #17     K1
         f[17] = 1                       #18     Psi1
         f[18] = 1                       #19     Phi1
         f[19] = f0[4]                   #20     The1
         f[20] = f0[4]                   #21     J1
         f[21] = f0[2]                   #22     SO1
         f[22] = f0[5]                   #23     OO1
         f[23] = f0[2]*f0[2]             #24     OQ2
         f[24] = f0[6]*f0[6]             #25     MNS2
         f[25] = f0[6]                   #26     2N2
         f[26] = f0[6]                   #27     Mu2
         f[27] = f0[6]                   #28     N2
         f[28] = f0[6]                   #29     Nu2
         f[29] = f0[2]                   #30     OP2
         f[30] = f0[6]                   #31     M2
         f[31] = f0[6]*f0[7]             #32     MKS2
         f[32] = f0[6]                   #33     Lam2
         f[33] = f0[8]                   #34     L2
         f[34] = 1                       #35     T2
         f[35] = 1                       #36     S2
         f[36] = 1                       #37     R2
         f[37] = f0[7]                   #38     K2
         f[38] = f0[6]*f0[6]             #39     MSN2
         f[39] = f0[3]*f0[4]             #40     KJ2
         f[40] = f0[6]                   #41     2SM2
         f[41] = f0[6] * f0[2]           #42     MO3
         f[42] = math.pow(f0[6], 1.5)    #43     M3
         f[43] = f0[2]                   #44     SO3
         f[44] = f0[6] * f0[3]           #45     MK3
         f[45] = f0[3]                   #46     SK3
         f[46] = f0[6] * f0[6]           #47     MN4
         f[47] = f0[6] * f0[6]           #48     M4
         f[48] = f0[6]                   #49     SN4
         f[49] = f0[6]                   #50     MS4
         f[50] = f0[6] * f0[7]           #51     MK4
         f[51] = 1                       #52     S4
         f[52] = f0[7]                   #53     SK4
         f[53] = f0[6]*f0[6]*f0[6]       #54     2MN6
         f[54] = f0[6]*f0[6]*f0[6]       #55     M6
         f[55] = f0[6]*f0[6]             #56     MSN6
         f[56] = f0[6]*f0[6]             #57     2MS6
         f[57] = f0[6]*f0[6]*f0[7]       #58     2MK6
         f[58] = f0[6]                   #59     2SM6
         f[59] = f0[6]*f0[7]             #60     MSK6

         dcnt  = 0
         cnt   = 0

         #hr[]:振幅、ags[]：角速度、pl[]：遅角
         for i in range(0,self.inc+3):
           self.tl[i] = self.level

           for j in range(0,60):
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
