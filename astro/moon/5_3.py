#!/home/ichiro1/anaconda3/bin/python
# -*- coding:utf-8 -*-

"""
5-3 <p.150>
月の出入りの時刻計算
"""
import ephem

moon=ephem.Moon()

tokyo = ephem.Observer()
tokyo.lon, tokyo.lat = '139.745', '35.654'
tokyo.elevation = 0
tokyo.date = '1981/9/1 0:00' #計算開始、JST 9時

date0=tokyo.date

print ('  日付 時刻       月の出　  　月の入    　　方位')
print ('-------------------------------------------------------------------')

for i in range(32):
   tokyo.date = date0 + i

   rise=tokyo.previous_rising(moon,use_center=True)
   set =tokyo.next_setting(moon,use_center=True)
   
   tokyo.date = set
   moon=ephem.Moon(tokyo)
   az  =moon.az 
   alt =moon.alt
   
   print ('%25s %25s %25s %s ' % (tokyo.date,rise,set,az))
