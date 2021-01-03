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

date_dic={}
rise_dic={}
transit_dic={}
set_dic={}


for i in range(32):
   tokyo.date = date0 + i
   date1 = tokyo.date

   (yy,mm,dd) = date1.triple()
   date1_date=str('%04d' % yy)+str('%02d' % mm)+str('%02d' % dd)
   date_dic.update({date1_date:1})

# 月の出（時刻）
   rise    = tokyo.next_rising(moon,use_center=True)

   (yy,mm,dd)=rise.triple()

   rise_date=str('%04d' % yy)+str('%02d' % mm)+str('%02d' % dd)
   rise_time=rise
   rise_dic.update({rise_date:rise_time})

# 南中（時刻）

   transit = tokyo.next_transit(moon)

   (yy,mm,dd)=transit.triple()

   transit_date=str('%04d' % yy)+str('%02d' % mm)+str('%02d' % dd)
   transit_time=transit
   transit_dic.update({transit_date:transit_time})

# 月の入り（時刻、方位）
   set     = tokyo.next_setting(moon,use_center=True)
 
   (yy,mm,dd)=set.triple()

   set_date=str('%04d' % yy)+str('%02d' % mm)+str('%02d' % dd)
   set_time=set
   set_dic.update({set_date:set_time})


print ('  日付 時刻       月の出　  　月の入    　　方位')
print ('-------------------------------------------------------------------')

for i in range(32):
   tokyo.date = date0 + i

   (yy,mm,dd) = tokyo.date.triple()
   date_str=str('%04d' % yy)+str('%02d' % mm)+str('%02d' % dd)

   date = date_str
   rise = rise_dic.get(date_str)
   transit = transit_dic.get(date_str)
   set = set_dic.get(date_str)

   print(' %9s |  %20s - %20s - %20s |' % (date,rise,transit,set))

