import sys
import tide_func
import numpy as np
import data_read
"""
一日の潮位、M2分潮
"""
pt = tide_func.Port()

pt.date = '2017/09/28'

pt.hr = np.zeros(60,np.float64)
pt.pl = np.zeros(60,np.float64)

pt.name = data_read.name
pt.lat  = data_read.lat
pt.lng  = data_read.lng
pt.level= data_read.level

pt.hr   = data_read.hr
pt.pl   = data_read.pl

print(pt.name,pt.date)

today = tide_func.Tide(pt)
today.wav(pt)

level  = today.tl
tide   = today.tide
m2     = today.m2
hitide = today.hitide
lowtide= today.lowtide

hitide_time   = np.array(hitide)[:,0]
hitide_level  = np.array(hitide)[:,1]

lowtide_time  = np.array(lowtide)[:,0]
lowtide_level = np.array(lowtide)[:,1]

print('満潮時刻  = %s' % hitide_time)
print('満潮潮位  = %s' % hitide_level)

print('干潮時刻  = %s' % lowtide_time)
print('干潮潮位  = %s' % lowtide_level)
