#!/home/ichiro1/anaconda3/bin/python
# -*- coding:utf-8 -*-

"""
月の出、南中、入りの時刻計算
"""
import ephem

RAD=180./ephem.pi

moon=ephem.Moon()

tokyo = ephem.Observer()
tokyo.lon, tokyo.lat = '139.7414', '35.6581'
tokyo.elevation = 0.0
tokyo.date = '2018/1/1 0:00' #計算開始、JST=UT+ 9時

date0=tokyo.date

print ('  日付 時刻       月の出　  　月の入    　　方位')
print ('-------------------------------------------------------------------')

for i in range(32):
   tokyo.date = date0 + i
   date1 = tokyo.date

   yy,mm,dd = date1.tuple()[0],date1.tuple()[1],date1.tuple()[2]

# 月の出（時刻、方位）
   rise    = tokyo.next_rising(moon,use_center=True)

   tokyo.date = rise
   moon = ephem.Moon(tokyo)
   rise_az = ephem.degrees(moon.az)*RAD

   rise_yy,rise_mm,rise_dd   = rise.tuple()[0],rise.tuple()[1],rise.tuple()[2]
   rise_hr,rise_min,rise_sec = rise.tuple()[3],rise.tuple()[4],rise.tuple()[5]

   rise_hr += 9. #UT->JST

   if (rise_hr >= 24):
       rise_dd +=  1
       rise_hr -= 24

# 南中（時刻、高度）
   transit = tokyo.next_transit(moon)

   tokyo.date = transit
   moon = ephem.Moon(tokyo)
   transit_alt = ephem.degrees(moon.alt)*RAD

   transit_yy,transit_mm,transit_dd   = transit.tuple()[0],transit.tuple()[1],transit.tuple()[2]
   transit_hr,transit_min,transit_sec = transit.tuple()[3],transit.tuple()[4],transit.tuple()[5]

   transit_hr += 9. #UT->JST

   if (transit_hr >= 24 ):
      transit_dd +=  1
      transit_hr -= 24

# 月の入り（時刻、方位）
   set     = tokyo.next_setting(moon,use_center=True)
  
   tokyo.date = set
   moon = ephem.Moon(tokyo)
   set_az = ephem.degrees(moon.az)*RAD
 
   set_yy,set_mm,set_dd   = set.tuple()[0],set.tuple()[1],set.tuple()[2]
   set_hr,set_min,set_sec = set.tuple()[3],set.tuple()[4],set.tuple()[5]
 
   set_hr += 9. #UT->JST

   if (set_hr >=24 ):
       set_dd +=  1
       set_hr -= 24
   
   print ('%4s %2s %2s | %2d:%2d:%5.2f - %6.2f | %2d:%2d:%5.2f - %6.2f | %2d:%2d:%5.2f - %6.2f ' % \
         (yy,mm,dd,rise_hr,rise_min,rise_sec,rise_az, \
          transit_hr,transit_min,transit_sec,transit_alt, \
          set_hr,set_min,set_sec,set_az))
