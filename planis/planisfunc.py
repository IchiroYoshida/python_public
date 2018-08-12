import numpy as np
import math

np.seterr(divide='ignore', invalid='ignore')

def rnd2pi(x):
    return (x - np.floor(x /2*np.pi) * 2*np.pi)

def equatoHori(th, RA, DEC):
     h = math.sin(th)*np.sin(DEC) + math.cos(th)*np.cos(RA)*np.cos(DEC)
     ALT = np.arcsin(h)
 
     cc = - np.sin(DEC)*math.cos(th) + np.cos(RA)*math.sin(th)*np.cos(DEC)
     ss = np.cos(DEC)*np.sin(RA)
     AZ = np.arctan2(ss, cc) + np.pi
 
     return AZ, ALT

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
   
     ret = {}

     if ('size' in kwargs): ret = {'size': SIZE}
     if ('name' in kwargs): ret.update({'name':NAME})

     return X, Y, ret
