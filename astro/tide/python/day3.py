import sys
import tide_func
import numpy as np
import data_read
"""
一日の潮位、M2分潮
"""
pt = tide_func.Port()

pt.date = '2018/5/19'

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

levelm2s2 = today.m2s2

m2s2 = levelm2s2[0:72:3]

hr =0
hrs=''
prn_m2s2 =''

for t in range(0,24):
    hrs +=str('%2d ' % t)
    prn_m2s2 +=('%2d ' % round((m2s2[t]+6)/15))

print (hrs)
print (prn_m2s2)
