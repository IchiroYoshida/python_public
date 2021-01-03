"""
# LIST 5-2 ARGUMENT OF TRIGONOMETRIC

INPUT    | tt TA = JULIAN CENTURIES FROM 1900 JAN 0.5

OUTPUT   |  ArgTri [0] |A ; MEAN ANOMALY OF MOON
         |         [1] |B ; ARGUMENT LATITUDE OF MOON
         |         [2] |C ; MEAN LONGITUDE OF MOON
                   [3] |D ; ELONGATION OF MOON FROM SUN
                   [4] |E ; LONGITUDE OF THE EARTH
                   [5] |G ; MEAN ANOMALY OF SUN
                   [6] |J ; MEAN ANOMALY OF JUPITER
                   [7] |L ; MEAN LONGITUDE OF SUN
                   [8] |M ; MEAN ANOMALY OF MARS
                   [9] |N ; LONGITUDE OF ASCENDING NODE OF MOON'S ORBIT
                   [10]|V ; MEAN ANOMALY OF VENUS
                   [11]|W ; MEAN LONGITUDE OF VENUS
"""
from math import *
from astro import *

arg=[0.0 for n in range(12)]

def MoonTime(mjd):
    time=(mjd-15019.5)/36525  #<5.2.14> 1900/1/1
    return time

#Degree to Rad
def fnr(x1):
    x=PI2*(x1/360.0-int(x1/360.0))
    return x

def ArgTri(mjd):

    tt=MoonTime(mjd)
    t1=tt
    t2=tt*tt

#Degree (0-360)
    arg[0] = 296.104608 + 477000*t1 + 198.849108*t1 + 9.192e-3*t2
    arg[1] =  11.250889 + 483120*t1 +  82.02515*t1  - 3.211e-3*t2
    arg[2] = 270.43416  + 480960*t1 + 307.883142*t1 - 1.133e-3*t2
    arg[3] = 350.737486 + 444960*t1 + 307.114217*t1 - 1.436e-3*t2
    arg[4] =  98.998753 +  35640*t1 + 359.372886*t1
    arg[5] = 358.475833 + 35999.04975*t1 - 1.5e-4*t2
    arg[6] = 225.444651 +   2880*t1 + 154.906654*t1
    arg[7] = 279.696678 + 36000.76892*t1 + 3.03e-4*t2
    arg[8] = 319.529425 +  19080*t1 +  59.8585*t1 + 1.81e-4*t2
    arg[9] = 259.183275 -   1800*t1  - 134.142008*t1 + 2.078e-3*t2
    arg[10]= 212.603219 +  58320*t1 + 197.803875*t1 + 1.286e-3*t2
    arg[11]= 342.767053 +  58320*t1 + 199.211911*t1 + 3.1e-4*t2

#Degree to Rad
    for n in range(12):
        arg[n] = fnr(arg[n])
        
    return arg

"""
# LIST 5-3 MOON-THETA,RHO,PHI
# 9000 **** MOON-THETA
"""
moon=[0.0 for n in range(3)]

def Moon(mjd):
    
    tt=MoonTime(mjd)
    arg=ArgTri(mjd)

    A = arg[0]    # MEAN ANOMALY OF MOON
    B = arg[1]    # ARGUMENT LATITUDE OF MOON
    C = arg[2]    # MEAN LONGITUDE OF MOON
    D = arg[3]    # ELONGATION OF MOON FROM SUN
    E = arg[4]    # LONGITUDE OF THE EARTH
    G = arg[5]    # MEAN ANOMALY OF SUN
    J = arg[6]    # MEAN ANOMALY OF JUPITER
    L = arg[7]    # MEAN LONGITUDE OF SUN
    M = arg[8]    # MEAN ANOMALY OF MARS
    N = arg[9]    # LONGITUDE OF ASCENDING NODE OF MOON'S ORBIT
    V = arg[10]   # MEAN ANOMALY OF VENUS
    W = arg[11]   # MEAN LONGITUDE OF VENUS


    mx  = -1.01e-3*sin(A+B-4*D)     \
          -1.02e-3*sin(A-B-4*D-N)   \
          -1.03e-3*tt*sin(A-B-N)    \
          -1.07e-3*sin(A-G-B-2*D-N) \
          -1.21e-3*sin(2*A-B-4*D-N) \
          +1.3e-3*sin(3*A+B+N)      \
          -1.31e-3*sin(A+B-N)       \
          +1.36e-3*sin(A+B-D+N)     \
          -1.45e-3*sin(G+B)         \
          -1.49e-3*sin(A+G-B-2*D)   \
          +1.57e-3*sin(G-B+D-N)     \
          -1.59e-3*sin(G-B)         \
          +1.84e-3*sin(A-G+B-2*D+N) \
	  -1.94e-3*sin(B-2*D-N)     \
          -1.96e-3*sin(G-B+2*D-N)   \
          +2e-3*sin(B-D)            \
          -2.05e-3*sin(A+G-B)       \
          +2.35e-3*sin(A-G-B)       \
          +2.46e-3*sin(A-3*B-N)     \
          -2.62e-3*sin(2*A+B-2*D)   \
          -2.83e-3*sin(A+G+B-2*D)   \
          -3.39e-3*sin(G-B-2*D-N)   \
          +3.45e-3*sin(A-B+N)       \
          -3.47e-3*sin(G-B+2*D)     \
          -3.83e-3*sin(B+D+N)       \
          -4.11e-3*sin(A+G+B+N)     \
          -4.42e-3*sin(2*A-B-2*D-N) \
          +4.49e-3*sin(A-B+2*D)     \
          -4.56e-3*sin(3*B-2*D+N)   \
          +4.66e-3*sin(A+B+2*D+N)   \
          +4.9e-3*sin(2*A-B)        \
          +5.61e-3*sin(2*A+B)       \
          +5.64e-3*sin(A-G+B+N)     \
          -6.38e-3*sin(A+G-B-N)     \
          -7.13e-3*sin(A+G-B-2*D-N) \
          -9.29e-3*sin(G+B-2*D)     \
          -9.47e-3*sin(2*A-B-N)     \
          +9.65e-3*sin(A-G-B-N)     \
          +9.7e-3*sin(B+2*D)        \
          +.01064*sin(B-D+N)        \
          -.0125*tt*sin(B+N)        \
          -.01434*sin(G+B-2*D+N)    \
          -.01652*sin(A+G+B-2*D+N)  \
          -.01868*sin(2*A+B-2*D+N)  \
          +.027*sin(2*A+B+N)        \
          -.02994*sin(A-B-2*D)      \
          -.03759*sin(G+B+N)        \
          -.03982*sin(G-B-N)        \
          +.04732*sin(B+2*D+N)      \
          -.04771*sin(B-N)          \
          -.06505*sin(A+B-2*D)      \
          +.13622*sin(A+B)          \
          -.14511*sin(A-B-2*D-N)    \
          -.18354*sin(B-2*D)        \
          -.20017*sin(B-2*D+N)      \
          -.38899*sin(A+B-2*D+N)    \
          +.40248*sin(A-B)          \
          +.65973*sin(A+B+N)        \
          +1.96763*sin(A-B-N)       \
          +4.95372*sin(B)           \
          +23.89684*sin(B+N)        

#9100 **** MOON-RHO ****

    my  =  .05491*cos(2*A+G)        \
          +.0629 *cos(A+D)          \
          -.06444*cos(4*D)          \
          -.06652*cos(2*A-G)        \
          -.07369*cos(G-4*D)        \
          +.08119*cos(A-3*D)        \
          -.09261*cos(A+4*D)        \
          +.10177*cos(A-2*B+2*D)    \
          +.10225*cos(A+G+2*D)      \
          -.10243*cos(A+2*G-2*D)    \
          -.12291*cos(2*B)          \
          -.12291*cos(2*A-2*B)      \
          -.12428*cos(A+G-4*D)      \
          -.14986*cos(3*A)          \
          -.1607 *cos(A-G+2*D)      \
          -.16949*cos(A-D)          \
          +.17697*cos(A+2*B-2*D)    \
          -.18815*cos(2*A-4*D)      \
          -.19482*cos(2*G-2*D)      \
          +.22383*cos(2*B-2*D)      \
          +.22594*cos(3*A-2*D)      \
          +.24454*cos(2*A+G-2*D)    \
          -.31717*cos(G+D)          \
          -.36333*cos(A-4*D)        \
          +.47999*cos(A-G-2*D)      \
          +.63844*cos(G+2*D)        \
          +.8617*cos(G)             \
          +1.50534*cos(A-2*B)       \
          -1.67417*cos(A+2*D)       \
          +1.99463*cos(A+G)         \
          +2.07579*cos(D)           \
          -2.455  *cos(A-G)         \
          -2.74067*cos(A+G-2*D)     \
          -3.83002*cos(G-2*D)       \
          -5.37817*cos(2*A)         \
          +6.60763*cos(2*A-2*D)     \
          -53.97626*cos(2*D)        \
          -68.62152*cos(A-2*D)      \
          -395.13669*cos(A)         \
          +3649.33705               

# 9200 **** MOON-PHI ****

    mz  = -1e-3*sin(A-G-2*B-2*N)    \
          -1e-3*sin(A+G-4*D)        \
          +1e-3*sin(2*A-G)          \
          +1.02e-3*sin(A-G+2*D)     \
          -1.06e-3*sin(2*A-2*B-N)   \
          -1.06e-3*sin(2*A+N)       \
          -1.09e-3*sin(A+2*B-2*D)   \
          -1.1e-3 *sin(2*B-D+2*N)    \
          +1.12e-3*sin(4*D)         \
          -1.22e-3*sin(2*A-N)       \
          -1.22e-3*sin(2*A+2*B+N)   \
          +1.49e-3*sin(G+2*B-2*D+2*N) \
          -1.57e-3*sin(2*A-4*D)     \
          +1.71e-3*sin(A+G+2*B-2*D+2*N) \
          -1.75e-3*sin(2*A+G-2*D)   \
          -1.9e-3 *sin(2*G-2*D)     \
          +1.93e-3*cos(A+16*E-18*W) \
          +1.94e-3*sin(2*A+2*B-2*D+2*N) \
          +2.01e-3*sin(G-2*D-N)     \
          +2.01e-3*sin(G+2*B-2*D+N) \
          -2.07e-3*sin(A+2*G-2*D)   \
          -2.1e-3 *sin(2*G)         \
          -2.13e-3*sin(2*D-N)       \
          -2.13e-3*sin(2*B+2*D+N)   \
          -2.15e-3*sin(3*A-2*D)     \
          -2.47e-3*sin(A-4*D)       \
          -2.53e-3*sin(A-2*B+2*D)   \
          +2.79e-3*tt*sin(2*B+2*N)  \
          -2.8e-3 *sin(2*A+2*B+2*N) \
          +3.12e-3*sin(3*A)         \
          -3.17e-3*sin(A+2*B)       \
          -3.5e-3 *sin(A+16*E-18*W) \
          +3.9e-3 *sin(G+2*B+2*N)   \
          +4.13e-3*sin(G-2*B-2*N)   \
          -4.9e-3*sin(2*N)          \
          -4.91e-3*sin(2*B+2*D+2*N) \
          +5.04e-3*sin(G+D)         \
          +5.16e-3*sin(A-D)         \
          -6.21e-3*sin(G+2*D)       \
          +6.48e-3*sin(A-2*B-2*D-N) \
          +6.48e-3*sin(A-2*D+N)     \
          +7e-3   *sin(A-G-2*D)     \
          +.01122 *sin(A+2*D)       \
          +.0141  *sin(A-2*D-N)     \
          +.0141  *sin(A+2*B-2*D+N) \
          +.01424 *sin(A-2*B)       \
          +.01506 *sin(A-2*B-2*D-2*N) \
          -.01567 *sin(2*B-2*D)     \
          +.02077 *sin(2*B-2*D+2*N) \
          -.02527 *sin(A+G)         \
          -.02952 *sin(A-N)         \
          -.02952 *sin(A+2*B+N)     \
          -.03487 *sin(D)           \
          +.03684 *sin(A-G)         \
          -.03983 *sin(2*D+N)       \
          +.03983 *sin(2*B-2*D+N)   \
          +.04037 *sin(A+2*B-2*D+2*N) \
          +.04221 *sin(2*A)         \
          -.04273 *sin(G-2*D)       \
          -.05566 *sin(2*A-2*D)     \
          -.05697 *sin(A+G-2*D)     \
          -.06846 *sin(A+2*B+2*N)   \
          -.08724 *sin(A-2*B-N)     \
          -.08724 *sin(A+N)         \
          -.11463 *sin(2*B)         \
          -.18647 *sin(G)           \
          -.20417 *sin(A-2*B-2*N)   \
          +.59616 *sin(2*D)         \
          +1.07142 *sin(N)          \
          -1.07447 *sin(2*B+N)      \
          -1.28658 *sin(A-2*D)      \
          -2.4797  *sin(2*B+2*N)    \
          +6.32962 *sin(A)

    moon=[mx,my,mz]

    return moon
#
# LIST 5-11 <p.180>
#
# SUN-THETA,RHO,PHI
#
# 9500 -
def Sun(mjd):

    ta=MoonTime(mjd)
    arg=ArgTri(mjd)

    A = arg[0]    # MEAN ANOMALY OF MOON
    B = arg[1]    # ARGUMENT LATITUDE OF MOON
    C = arg[2]    # MEAN LONGITUDE OF MOON
    D = arg[3]    # ELONGATION OF MOON FROM SUN
    E = arg[4]    # LONGITUDE OF THE EARTH
    G = arg[5]    # MEAN ANOMALY OF SUN
    J = arg[6]    # MEAN ANOMALY OF JUPITER
    L = arg[7]    # MEAN LONGITUDE OF SUN
    M = arg[8]    # MEAN ANOMALY OF MARS
    N = arg[9]    # LONGITUDE OF ASCENDING NODE OF MOON'S ORBIT
    V = arg[10]   # MEAN ANOMALY OF VENUS
    W = arg[11]   # MEAN LONGITUDE OF VENUS


# 9500 **** SUN-THETA ****
   
    sx =    -1e-5*ta*sin(G+L)  \
       - 1e-5*cos(G-L-J)      \
       - 1.4e-5*sin(2*G-L)    \
       - 3e-5*ta*sin(G-L)     \
       - 3.9e-5*sin(N-L)      \
       - 4e-5*cos(L)          \
       + 4.2e-5*sin(2*G+L)    \
       - 2.08e-4*ta*sin(L)    \
       + 3.334e-3*sin(G+L)    \
       + 9.999e-3*sin(G-L)    \
       + .39793*sin(L)

# 9520 **** SUN-RHO ****

    sy =  2.7e-5*sin(2*G-2*V) \
       - 3.3e-5*sin(G-J)      \
       + 8.4e-5*ta*cos(G)     \
       - 1.4e-4*cos(2*G)      \
       - .033503*cos(G)       \
       + 1.000421

# 9540 **** SUN-PHI ****

    sz = - 1.7e-5*cos(2*G-2*V) \
       - 1.9e-5*sin(G-V)       \
       + 2.4e-5*sin(4*G-8*M+3*J) \
       - 2.5e-5*cos(G-J)       \
       + 3e-5*sin(C-L)         \
       + 4.6e-5*ta*sin(2*L)    \
       + 6.801e-5*sin(2*G)     \
       - 7.9e-5*sin(N)         \
       - 8e-5*ta*sin(G)        \
       - 9.5e-5                \
       - 3.46e-4*sin(G+2*L)    \
       - 1.038e-3*sin(G-2*L)   \
       + .032116*sin(G)        \
       - .041295*sin(2*L)      

#    print('ta= %8.4f sx %8.4f    sy %8.4f     sz %8.4f' % (ta,sx,sy,sz))
    
    sun=[sx,sy,sz]

    return sun

# moon_position[ra,dc,dl]=MoonPosition(moon)
#
# LIST 5-4 <p.172>
# POSITIONS 
# 9300 -
#
def MoonPosition(mjd):

    arg=ArgTri(mjd)
    moon=Moon(mjd)

    r1=moon[0]
    r2=moon[1]
    r3=moon[2]

    r0=arg[2]   # C:  MEAN LONGITUDE OF MOON

    ss=r3/sqrt(r2-r1*r1)  #<5.2.16> p.146
    cc=sqrt(1-ss*ss)
    ra=r0+atan(ss/cc)

    if (ra > PI2):
        ra -= PI2
    if (ra < 0):
	ra += PI2
 
    ss=r1/sqrt(r2)
    cc=sqrt(1-ss*ss)
    dc=atan(ss/cc)
    dl=sqrt(r2)
    
    dl *=EARTH_RD     #Delta -> Km
    
    moon_position=[ra,dc,dl]

    return moon_position
#
# sun_position[ra,dc,dl]=SunPosition(mjd)
# 
# LIST 5-4 modified <p.172>
# POSITIONS
# 9300 -
def SunPosition(mjd):

    arg=ArgTri(mjd)
    sun=Sun(mjd)

    r1=sun[0]
    r2=sun[1]
    r3=sun[2]

    r0=arg[7]      # L: MEAN LONGITUDE OF SUN

#    print('r1 %8.4f  r2 %8.4f  r3 %8.4f     r0 %8.4f' % (r1,r2,r3,r0))
    
    ss=r3/sqrt(r2-r1*r1)  #<5.2.16> alpha p.146
    cc=sqrt(1-ss*ss)
    ra=r0+atan(ss/cc)

    if (ra > PI2):
        ra -= PI2
    if (ra < 0):
	ra += PI2
 
    ss=r1/sqrt(r2)     #<5.2.16> delta p.146
    cc=sqrt(1-ss*ss)
    dc=atan(ss/cc)
    dl=sqrt(r2)        #dl (AU)
    
    sun_position=[ra,dc,dl]

    return sun_position

# LIST 5-9 GETSU-REI <p.178>
#
# ge=Getsurei(mjd)
def Getsurei(mjd):

    tt=MoonTime(mjd)

    arg=ArgTri(mjd)
    eg=arg[3]   # D:

    ge= eg/PI2*29.4

    return ge




