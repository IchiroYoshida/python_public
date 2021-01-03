#KouseiJi.py  from astro.py

def KouseiJi1950(mjd,long): #(2.2.12) p.25,37
    r = .6705199+ 1.002737803*(mjd-40000)+long/PI2
    r = r-int(r)
    r *= PI2
    return r

def KouseiJiDate(mjd,long): #(2.2.11) p.25,37
    r = .671262 + 1.002737909*(mjd-40000)+long/PI2
    r = r-int(r)
    r *= PI2
    return r


