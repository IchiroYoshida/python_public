import numpy as np
import math
import ephem

np.seterr(divide='ignore', invalid='ignore')

def moon_Pangle(observer):
     sun  = ephem.Sun(observer)
     moon = ephem.Moon(observer)
     cs1  = math.cos(sun.g_dec)*math.sin(sun.g_ra - moon.g_ra)
     cs2  = math.cos(moon.g_dec)*math.sin(sun.g_dec)
     scc  = math.sin(moon.g_dec)*math.cos(sun.g_dec)*math.cos(sun.g_ra - moon.g_ra)

     kai = math.atan2(cs1, cs2 - scc) + math.pi/2.

     if (kai < 0): kai += 2*math.pi

     return(kai)

def equatoHori(th, RA, DEC):
     h = math.sin(th)*np.sin(DEC) + math.cos(th)*np.cos(RA)*np.cos(DEC)
     ALT = np.arcsin(h)
 
     cc = - np.sin(DEC)*math.cos(th) + np.cos(RA)*math.sin(th)*np.cos(DEC)
     ss = np.cos(DEC)*np.sin(RA)
     AZ = np.arctan2(ss, cc) + np.pi
 
     return AZ, ALT

def polar(az, alt):
     r = np.pi /2. - alt
     x = - r * np.sin(az)
     y =   r * np.cos(az)
     return x, y

def polarXY(AZ, ALT, lim,  **kwargs):
     if ('size' in kwargs): SIZE = kwargs['size']
     if ('name' in kwargs): NAME = kwargs['name']

     if('size' in kwargs): SIZE = SIZE[np.where(ALT > lim)]
     if('name' in kwargs): NAME = NAME[np.where(ALT > lim)]
     AZ   = AZ[np.where(ALT >lim)]
     ALT  = ALT[np.where(ALT >lim)]

     R = np.pi /2. - ALT
     X = - R * np.sin(AZ)
     Y =   R * np.cos(AZ)

     if (kwargs):
         ret = {}
         if ('size' in kwargs): ret = {'size': SIZE}
         if ('name' in kwargs): ret.update({'name':NAME})

         return X, Y, ret

     else:
         return X, Y
