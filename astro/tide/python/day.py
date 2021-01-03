import sys
import tide_func
import numpy as np
import data_read
"""
一日の潮位、M2分潮
"""
pt = tide_func.Port()

pt.date = '2009/5/4'

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

level     = today.tl
levelm2   = today.m2

tide     = today.tide
tidem2   = today.tidem2

hitide  = today.hitide
lowtide = today.lowtide

hitidem2   = today.hitidem2
lowtidem2  = today.lowtidem2

m2 = ((levelm2[0:72:3])+15.)/35.

hr =0
hrs=''
prn='' 

for m in m2:
    hrs +=str('%2d ' % hr )
    hr  +=1
    prn +=str('%2d ' % int(round(m)))

print (hrs)
print (prn)

#---------------
hitide_time   = np.array(hitide)[:,0]
hitide_level  = np.array(hitide)[:,1]

lowtide_time  = np.array(lowtide)[:,0]
lowtide_level = np.array(lowtide)[:,1]

print('満潮時刻  = %s' % hitide_time)
print('満潮潮位  = %s' % hitide_level)

print('干潮時刻  = %s' % lowtide_time)
print('干潮潮位  = %s' % lowtide_level)

#M2分潮　潮位

hitide_timem2   = np.array(hitidem2)[:,0]
hitide_levelm2  = np.array(hitidem2)[:,1]

lowtide_timem2  = np.array(lowtidem2)[:,0]
lowtide_levelm2 = np.array(lowtidem2)[:,1]

print('満潮時刻(M2)  = %s' % hitide_timem2)
print('満潮潮位(M2)  = %s' % hitide_levelm2)

print('干潮時刻(M2)  = %s' % lowtide_timem2)
print('干潮潮位(M2)  = %s' % lowtide_levelm2)


