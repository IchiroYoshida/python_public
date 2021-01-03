#!/home/ichiro1/anaconda3/bin/python
# -*- coding:utf-8 -*-

"""
5-1 <p.147>
１ヶ月分の月の位置計算
"""
import ephem

moon=ephem.Moon()

tokyo = ephem.Observer()
tokyo.lon, tokyo.lat = '139.745', '35.654'
tokyo.elevation = 0
tokyo.date = '1981/9/1 12:00' #計算開始、JST 21時

date0=tokyo.date

moon= ephem.Moon()

print ('        時刻                   赤経　　　　　赤緯  　　距離(Km)')
print ('-------------------------------------------------------------------')

for i in range(32):
   tokyo.date = date0 + i
   moon.compute(tokyo.date,epoch='1950')

   dist=moon.earth_distance*ephem.meters_per_au/1000
   ra=moon.ra
   dec=moon.dec

   print ('%25s %15s %15s %8.2f' % (tokyo.date,ra,dec,dist))


