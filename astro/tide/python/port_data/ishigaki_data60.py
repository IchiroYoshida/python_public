"""
石垣　固有値（２０１６年）　６０分潮
"""
import numpy as np
import tide_func as tide
pt = tide.Port

pt.name = "石垣"

pt.lat   =  24.20  #緯度
pt.lng   = 124.10  #経度
pt.level = 107     #平均潮位（cm）

pt.pl = np.zeros(60,np.float64)
pt.hr = np.zeros(60,np.float64)

# 調和定数（遅角）      分潮
pt.pl[0]  = 135.19    # 1    Sa
pt.pl[1]  = 308.50    # 2    Ssa
pt.pl[2]  =  54.88    # 3    Mm
pt.pl[3]  = 300.78    # 4    MSf
pt.pl[4]  =  27.10    # 5    Mf
pt.pl[5]  = 165.77    # 6    2Q1
pt.pl[6]  = 175.36    # 7    Sig1
pt.pl[7]  = 187.05    # 8    Q1
pt.pl[8]  = 177.07    # 9    Rho1
pt.pl[9]  = 199.36    #10    O1
pt.pl[10] = 248.57    #11    MP1
pt.pl[11] = 202.98    #12    M1
pt.pl[12] = 210.24    #13    Ki1
pt.pl[13] = 215.11    #14    Pi1
pt.pl[14] = 217.86    #15    P1
pt.pl[15] = 227.12    #16    S1
pt.pl[16] = 221.35    #17    K1
pt.pl[17] = 228.48    #18    Psi1
pt.pl[18] = 204.45    #19    Phi1
pt.pl[19] = 240.16    #20    The1
pt.pl[20] = 235.94    #21    J1
pt.pl[21] = 274.68    #22    SO1
pt.pl[22] = 253.39    #23    OO1
pt.pl[23] = 251.97    #24    OQ2
pt.pl[24] = 176.30    #25    MNS2
pt.pl[25] = 171.88    #26    2N2
pt.pl[26] = 179.83    #27    Mu2
pt.pl[27] = 185.45    #28    N2
pt.pl[28] = 185.39    #29    Nu2
pt.pl[29] = 277.49    #30    OP2
pt.pl[30] = 193.52    #31    M2
pt.pl[31] =  42.08    #31    M2
pt.pl[32] = 185.10    #33    Lam2
pt.pl[33] = 194.01    #34    L2
pt.pl[34] = 211.53    #35    T2
pt.pl[35] = 216.23    #36    S2 
pt.pl[36] = 228.71    #37    R2
pt.pl[37] = 211.92    #38    K2
pt.pl[38] = 353.08    #39    MSN2
pt.pl[39] =  43.27    #40    KJ2
pt.pl[40] = 163.78    #41    2SM2
pt.pl[41] = 328.89    #42    MO3
pt.pl[42] = 200.64    #43    M3
pt.pl[43] = 283.21    #44    SO3
pt.pl[44] = 294.31    #45    MK3
pt.pl[45] = 319.69    #46    SK3
pt.pl[46] = 309.61    #47    MN4
pt.pl[47] = 315.22    #48    M4
pt.pl[48] = 280.38    #49    SN4
pt.pl[49] = 313.16    #50    MS4
pt.pl[50] = 329.08    #51    MK4
pt.pl[51] = 344.96    #52    S4
pt.pl[52] = 328.38    #53    SK4
pt.pl[53] = 205.66    #54    2MN6
pt.pl[54] = 218.12    #55    M6
pt.pl[55] = 252.20    #56    MSN6
pt.pl[56] = 258.16    #57    2MS6
pt.pl[57] = 253.89    #58    2MK6
pt.pl[58] = 289.57    #59    2SM6
pt.pl[59] = 313.02    #60    MSK6


# 調和定数（振幅）
pt.hr[0]  = 17.04     # 1    Sa
pt.hr[1]  =  4.06     # 2    Ssa
pt.hr[2]  =  0.91     # 3    Mm
pt.hr[3]  =  0.72     # 4    MSf
pt.hr[4]  =  0.38     # 5    Mf
pt.hr[5]  =  0.47     # 6   2Q1
pt.hr[6]  =  0.60     # 7   Sig1
pt.hr[7]  =  3.44     # 8    Q1
pt.hr[8]  =  0.62     # 9    Rho1
pt.hr[9]  = 16.93     #10    O1
pt.hr[10] =  0.31     #11    MP1
pt.hr[11] =  0.77     #12    M1
pt.hr[12] =  0.26     #13   Ki1
pt.hr[13] =  0.45     #14    Pi1
pt.hr[14] =  6.35     #15    P1
pt.hr[15] =  0.14     #16    S1
pt.hr[16] = 19.81     #17    K1
pt.hr[17] =  0.19     #18    Psi1
pt.hr[18] =  0.39     #19    Phi1
pt.hr[19] =  0.21     #20   The1
pt.hr[20] =  1.06     #21    J1
pt.hr[21] =  0.25     #22    SO1
pt.hr[22] =  0.52     #23    OO1
pt.hr[23] =  0.08     #24    OQ2
pt.hr[24] =  0.34     #25    MNS2
pt.hr[25] =  1.25     #26    2N2
pt.hr[26] =  1.56     #27    Mu2
pt.hr[27] =  8.87     #28    N2
pt.hr[28] =  1.65     #29    Nu2
pt.hr[29] =  0.40     #30    OP2
pt.hr[30] = 44.24     #31    M2
pt.hr[31] =  0.02     #32    MKS2
pt.hr[32] =  0.27     #33    Lam2 
pt.hr[33] =  1.13     #34    L2
pt.hr[34] =  1.14     #35    T2
pt.hr[35] = 19.49     #36    S2
pt.hr[36] =  0.12     #37    R2
pt.hr[37] =  5.28     #38    K2
pt.hr[38] =  0.09     #39    MSN2  
pt.hr[39] =  0.37     #40    KJ2
pt.hr[40] =  0.04     #41    2SM2
pt.hr[41] =  0.22     #42    MO3
pt.hr[42] =  0.76     #43    M3
pt.hr[43] =  0.09     #44    SO3
pt.hr[44] =  0.24     #45    MK3
pt.hr[45] =  0.13     #46    SK3
pt.hr[46] =  0.21     #47    MN4
pt.hr[47] =  0.46     #48    M4
pt.hr[48] =  0.10     #49    SN4
pt.hr[49] =  0.40     #50    MS4
pt.hr[50] =  0.14     #51    MK4
pt.hr[51] =  0.10     #52    S4
pt.hr[52] =  0.08     #53    SK4
pt.hr[53] =  0.14     #54    2MN6
pt.hr[54] =  0.26     #55    M6
pt.hr[55] =  0.03     #56    MSN6
pt.hr[56] =  0.24     #57    2MS6
pt.hr[57] =  0.09     #58    2MK6
pt.hr[58] =  0.07     #59    2SM6
pt.hr[59] =  0.05     #60    MSK6

