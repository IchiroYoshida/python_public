#!/home/ichiro1/anaconda3/bin/python
# -*- coding:utf-8 -*-

"""
月の出、南中、入りの時刻計算  東京(JST:UTC+9hr)
"""
import ephem

import datetime

#import pytz
#from dateutil import parser
#from datetime import datetime

RAD=180./ephem.pi

moon=ephem.Moon()

tokyo = ephem.Observer()
tokyo.lon, tokyo.lat = '139.7414', '35.681'
tokyo.elevation = 0.0
tokyo.date = '2016/5/31 15:00' #計算開始、UT 0:00 JST=UT+ 9hr

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

   rise_utc      = tokyo.next_rising(moon,use_center=True)
   rise_local    = ephem.localtime(rise_utc)
   rise_dic.update({rise_local.strftime("%Y%m%d"):rise_local})

# 南中（時刻）

   transit_utc   = tokyo.next_transit(moon)
   transit_local = ephem.localtime(transit_utc)

   transit_dic.update({transit_local.strftime("%Y%m%d"):transit_local})

# 月の入り（時刻、方位）
   set_utc     = tokyo.next_setting(moon,use_center=True)
   set_local   = ephem.localtime(set_utc)

   set_dic.update({set_local.strftime("%Y%m%d"):set_local})


print ('  日付 時刻       月の出　  　月の入    　　方位')
print ('-------------------------------------------------------------------')

time_str ="%H:%M:%S"

for i in range(32):
   tokyo.date = date0 + i

   (yy,mm,dd) = tokyo.date.triple()
   date_str=str('%04d' % yy)+str('%02d' % mm)+str('%02d' % dd)

   date = date_str
 
   rise = repr(rise_dic.get(date))
   if (rise == 'None'):
          rise2 = "******"
   else:
          rise2 =  eval(rise).strftime(time_str)

   transit = repr(transit_dic.get(date_str))
   if (transit == 'None'):
          transit2 = "+++++++"
   else:
          transit2 = eval(transit).strftime(time_str)

   set = repr(set_dic.get(date_str))
   if (set == 'None'):
          set2 = "------"
   else:
          set2 = eval(set).strftime(time_str)

   print(' %9s |  %10s   | %10s  | %10s  |' % (date,rise2,transit2,set2))

