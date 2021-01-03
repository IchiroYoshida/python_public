import tide_new
import numpy as np
"""
福岡（博多港東浜）での潮位
"""

pt = tide_new.Port

pt.name = "博多船H4"

pt.lat =33.36
pt.lng =130.24
pt.level=110

pt.pl = np.zeros(40,np.float64)
pt.hr = np.zeros(40,np.float64)

# 調和定数（遅角）      分潮
pt.pl[0]  = 150.80    # Sa
pt.pl[1]  = 304.40    # Ssa
pt.pl[2]  =  44.70    # Mm
pt.pl[3]  =   0.70    # MSf
pt.pl[4]  = 174.00    # Mf
pt.pl[5]  = 233.30    # Q1
pt.pl[6]  = 252.00    # Rho1
#pt.pl[7]  = 246.70    # O1
pt.pl[7]  = 248.12    # O1 (2016)
pt.pl[8]  = 169.90    # MP1
pt.pl[9]  = 259.50    # M1
pt.pl[10] = 325.80    # Pi1
pt.pl[11] = 263.90    # P1
pt.pl[12] =  64.20    # S1
#pt.pl[13] = 265.60    # K1
pt.pl[13] = 266.41    # K1 (2016)
pt.pl[14] =  26.40    # Psi1
pt.pl[15] = 304.80    # Phi1
pt.pl[16] = 269.70    # J1
pt.pl[17] = 235.30    # SO1
pt.pl[18] = 300.10    # OO1
pt.pl[19] = 264.00    # 2N2
pt.pl[20] = 263.30    # Mu2
pt.pl[21] = 272.80    # N2
pt.pl[22] = 274.80    # Nu2
pt.pl[23] = 245.20    # OP2
#pt.pl[24] = 277.20    # M2
pt.pl[24] = 278.94    # M2 (2016)
pt.pl[25] = 258.00    # Lam2
pt.pl[26] = 255.30    # L2
pt.pl[27] = 304.20    # T2
#pt.pl[28] = 302.10    # S2
pt.pl[28] = 302.96    # S2 (2016)
pt.pl[29] = 263.60    # R2
pt.pl[30] = 293.90    # K2
pt.pl[31] =  66.80    # 2SM2
pt.pl[32] = 136.10    # MO3
pt.pl[33] =   2.10    # M3
pt.pl[34] = 131.00    # MK3
pt.pl[35] = 187.00    # SK3
pt.pl[36] = 203.90    # M4
pt.pl[37] = 239.00    # MS4
pt.pl[38] = 230.70    # M6
pt.pl[39] = 277.00    # 2MS6

# 調和定数（振幅）
pt.hr[0]  = 19.40     # Sa
pt.hr[1]  =  1.50     # Ssa
pt.hr[2]  =  1.30     # Mm
pt.hr[3]  =  0.50     # MSf
pt.hr[4]  =  0.50     # Mf
pt.hr[5]  =  3.20     # Q1
pt.hr[6]  =  0.60     # Rho1
#pt.hr[7]  = 13.80     # O1
pt.hr[7]  = 13.99      # O1 (2016)
pt.hr[8]  =  0.40     # MP1
pt.hr[9]  =  0.60     # M1
pt.hr[10] =  0.20     # Pi1
pt.hr[11] =  4.80     # P1
pt.hr[12] =  0.50     # S1
#pt.hr[13] = 14.90     # K1
pt.hr[13] =  14.81    # K1 (2016)
pt.hr[14] =  0.00     # Psi1
pt.hr[15] =  0.20     # Phi1
pt.hr[16] =  0.70     # J1
pt.hr[17] =  0.10     # SO1
pt.hr[18] =  0.40     # OO1
pt.hr[19] =  2.00     # 2N2
pt.hr[20] =  2.80     # Mu2
pt.hr[21] = 11.00     # N2
pt.hr[22] =  1.70     # Nu2
pt.hr[23] =  0.30     # OP2
#pt.hr[24] = 53.90     # M2
pt.hr[24] = 50.92     # M2 (2016)
pt.hr[25] =  0.40     # Lam2 
pt.hr[26] =  1.60     # L2
pt.hr[27] =  1.80     # T2
#pt.hr[28] = 25.60     # S2
pt.hr[28] = 24.27     # S2
pt.hr[29] =  0.80     # R2
pt.hr[30] =  7.20     # K2
pt.hr[31] =  0.50     # 2SM2
pt.hr[32] =  0.50     # MO3
pt.hr[33] =  1.70     # M3
pt.hr[34] =  0.70     # MK3
pt.hr[35] =  0.70     # SK3
pt.hr[36] =  1.40     # M4
pt.hr[37] =  1.50     # MS4
pt.hr[38] =  0.20     # M6
pt.hr[39] =  0.30     # 2MS6

pt.date = '2016/07/21'
pt.itv  = 20

today = tide_new.Tide(pt)

tt = today.tide(pt)

# --------

DayMinute = int(24*60)
DayTimes  = int(DayMinute/pt.itv)

level  = today.tl
tide   = today.tide
hitide = today.hitide
lowtide= today.lowtide

print (level)
print (tide)
print (hitide)
print (lowtide)


"""
from scipy import interpolate
#import numpy as np

level_interpolate = np.zeros(DayMinute,np.float64)

time = np.arange(0,len(level)*pt.itv,pt.itv)
#level_func = interpolate.interp1d(time,level)
level_func = interpolate.lagrange(time,level)

ti = np.arange(0,DayMinute,1)
level_interpolate = level_func(ti)

import peakdetect

maxtab, mintab = peakdetect.peakdet(level_interpolate,10)

print (maxtab,mintab)

import pylab as plt

#plt.plot(time,level,'o',color='red')
plt.plot(ti,level_interpolate,color='blue')
#plt.scatter(np.array(maxtab)[:,0], np.array(maxtab)[:,1],marker='o', color='green')
x1=np.array(maxtab)[:,0]
y1=np.array(maxtab)[:,1]

plt.scatter(x1,y1,marker='*',color='g')
#plt.scatter(np.array(mintab)[:,0], np.array(mintab)[:,1],marker='o', color='yellow')
x2=np.array(mintab)[:,0]
y2=np.array(mintab)[:,1]

plt.scatter(x2,y2,marker='o',color='m')

plt.show()
"""

