#!/home/ichiro1/anaconda3/bin/python
# -*- coding:utf-8 -*-

"""
月の出、南中、入りの時刻計算
"""
import ephem

RAD=180./ephem.pi

moon=ephem.Moon()

tokyo = ephem.Observer()
tokyo.lon, tokyo.lat = '139.7414', '35.681'
tokyo.elevation = 0.0
tokyo.date = '2016/6/1 0:00' #計算開始、UT 0:00 JST=UT+ 9hr

date0=tokyo.date 

print ('  日付 時刻       月の出　  　月の入    　　方位')
print ('-------------------------------------------------------------------')

date_dic={}
rise_dic={}
transit_dic={}
set_dic={}


for i in range(32):
   tokyo.date = date0 + i
   date1 = tokyo.date

   yy,mm,dd = date1.tuple()[0],date1.tuple()[1],date1.tuple()[2]
   date1_date=str('%04d' % yy)+str('%02d' % mm)+str('%02d' % dd)
   date_dic.update({date1_date:1})

# 月の出（時刻）
   rise    = tokyo.next_rising(moon,use_center=True)

   rise_yy,rise_mm,rise_dd   = rise.tuple()[0],rise.tuple()[1],rise.tuple()[2]
   rise_hr,rise_min,rise_sec = rise.tuple()[3],rise.tuple()[4],rise.tuple()[5]

   rise_date=str('%04d' % rise_yy)+str('%02d' % rise_mm)+str('%02d' % rise_dd)
   rise_time=rise
   rise_dic.update({rise_date:rise_time})

# 南中（時刻）

   transit = tokyo.next_transit(moon)

   transit_yy,transit_mm,transit_dd   = transit.tuple()[0],transit.tuple()[1],transit.tuple()[2]
   transit_hr,transit_min,transit_sec = transit.tuple()[3],transit.tuple()[4],transit.tuple()[5]

   transit_date=str('%04d' % rise_yy)+str('%02d' % rise_mm)+str('%02d' % rise_dd)
   transit_time=transit
   transit_dic.update({transit_date:transit_time})

# 月の入り（時刻、方位）
   set     = tokyo.next_setting(moon,use_center=True)
  
   set_yy,set_mm,set_dd   = set.tuple()[0],set.tuple()[1],set.tuple()[2]
   set_hr,set_min,set_sec = set.tuple()[3],set.tuple()[4],set.tuple()[5]

   set_date=str('%04d' % set_yy)+str('%02d' % set_mm)+str('%02d' % set_dd)
   set_time=set
   set_dic.update({set_date:set_time})


for i in range(32):
   tokyo.date = date0 + i
   date1 = tokyo.date

   yy,mm,dd = date1.tuple()[0],date1.tuple()[1],date1.tuple()[2]
   date=str('%04d' % yy)+str('%02d' % mm)+str('%02d' % dd)

   print (date)
   print (rise_dic.get(date))
   print (transit_dic.get(date))
   print (set_dic.get(date))


