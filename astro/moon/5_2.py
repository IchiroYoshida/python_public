#!/home/ichiro1/anaconda3/bin/python
# -*- coding:utf-8 -*-

"""
5-2 <p.148>
30分おきの月の位置計算
"""
AU=149597870.7   #1AU (Km)

import ephem

moon=ephem.Moon()
moon.compute('1981/9/1 12:00',epoch='1950') #JST=21:00

tokyo = ephem.Observer()
tokyo.lon, tokyo.lat = '139.745', '35.654'
tokyo.elevation = 0
tokyo.date = '1981/9/24 7:00' #計算開始、JST 16時

date0=tokyo.date

moon= ephem.Moon()

print ('        時刻                   赤経　　　　　赤緯  　　距離(Km)')
print ('-------------------------------------------------------------------')

for i in range(32):
   tokyo.date = date0 + ephem.minute*30*i
   moon.compute(tokyo.date,epoch='1950')

   dist=moon.earth_distance*AU
   ra=moon.ra
   dec=moon.dec

   print ('%25s %15s %15s %8.2f' % (tokyo.date,ra,dec,dist))


