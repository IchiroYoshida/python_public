#!/home/ichiro1/anaconda3/bin/python
# -*- coding:utf-8 -*-

"""
5-4 <p.153>
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

print ('        時刻         地心（赤経、赤緯）距離(Km)　東京（赤経、赤緯) 距離(Km)')
print ('-------------------------------------------------------------------')

for i in range(32):
   tokyo.date = date0 + i
   moon.compute(tokyo.date,epoch='1950')

   dist=moon.earth_distance*ephem.meters_per_au/1000.

#Astrometric Topocentric Position   
   ra1=moon.a_ra
   dec1=moon.a_dec
#Apparent Geocentric Position
   ra2=moon.g_ra
   dec2=moon.g_dec
#Apparent Topocentric Position
   ra3=moon.ra
   dec3=moon.dec

   print ('%s| %s-%s | %s-%s | %s-%s | %8.2f' % (tokyo.date,ra1,dec1,ra2,dec2,ra3,dec3,dist))
