# -*- coding:utf-8 -*-

"""
月の出、南中、入りの時刻計算  東京(JST:UTC+9hr)
"""
import math
import ephem
import datetime

from moon_func import *

#月の出（時刻、方角、地方時、日付）	
class Moon(object):
   def __init__(self,observer):
       moon         = ephem.Moon(observer)
       self.azimuth = 0
       self.alt     = 0
       self.local   = 0
       self.index   = ''
       self.time    = ''

   def rise(self,observer):
       moon         = ephem.Moon(observer)
       observer.date= observer.previous_rising(moon,use_center=True) #月の出（時刻）
       moon         = ephem.Moon(observer) 
       self.azimuth = ephem.degrees(moon.az)*RAD                     #月出、方位角
       self.local   = repr(ephem.localtime(observer.date))           #時刻、日付
       self.index    = eval(self.local).strftime('%Y%m%d')
       self.time     = observer.date

#月の南中（時刻、角度、地方時、日付）
   def transit(self,observer):
       moon         = ephem.Moon(observer)
       observer.date= observer.previous_transit(moon)                #月の南中（時刻）

       moon         = ephem.Moon(observer)   
       self.alt     = ephem.degrees(moon.alt)*RAD                    #月の南中高度
       self.local   = repr(ephem.localtime(observer.date))           #時刻、日付
       self.index   = eval(self.local).strftime('%Y%m%d')
       self.time    = observer.date

       self.radius  = moon.radius                                    #月の大きさ
       self.dist    = moon.earth_distance*AU                         #月の距離 
       self.phase   = moon.moon_phase                                #月の輝面(%)

#月の没（時刻、方角、地方時、日付）
   def set(self,observer):
       moon         = ephem.Moon(observer)
       observer.date= observer.previous_setting(moon,use_center=True) #月の没（時刻）
     
       moon         = ephem.Moon(observer)
       self.azimuth = ephem.degrees(moon.az)*RAD                     #月没、方位角
       self.local   = repr(ephem.localtime(observer.date))           #時刻、日付
       self.index   = eval(self.local).strftime('%Y%m%d')
       self.time    = observer.date

#月と太陽の黄経、黄経差
   def noon(self,observer):
       sun          = ephem.Sun(observer)
       time         = observer.next_setting(sun)              #日没時間算出
       time0        = repr(ephem.localtime(time))
       time1        = eval(time0)
       time_str     = time1.strftime('%Y/%m/%d')             #上記日没時間の日付
       time_JST0     = ' 15:00'                              #  0:00 JST 
       time_JST12    = ' 3:00'                               #  12:00 JST
       observer.date    = time_str+time_JST0

       #0:00 JSTでの太陽と月の黄経を算出する。
       sun          = ephem.Sun(observer)
       moon         = ephem.Moon(observer)
       ecl_moon     = ephem.Ecliptic(moon)                       #月の黄経
       ecl_sun      = ephem.Ecliptic(sun)                        #太陽の黄経
       self.ecl_diff  = rnd36((ecl_moon.lon - ecl_sun.lon )*RAD) #月と太陽の黄経差
       self.tname   = tidename_JMA(self.ecl_diff)
       self.index    = time1.strftime('%Y%m%d')

       #12:00 JSTでの月齢を算出する。
       observer.date = time_str+time_JST12
       pnm           = ephem.previous_new_moon(observer.date)
       self.moonage  = observer.date - pnm

moon=ephem.Moon()

tokyo = ephem.Observer()
tokyo.lon, tokyo.lat = '139.7414', '35.681'
tokyo.elevation = 0.0
tokyo.date = '2016/7/1 9:00' #UT 0:00 JST= UT +9hr

date0 = tokyo.date

rise_dic    = {}
transit_dic = {}
set_dic     = {}
ecl_dic     = {}

for i in range(31):
   date_tokyo    = date0 + i

   tokyo.date    = date_tokyo     
   today     = Moon(tokyo)
   today.rise(tokyo)
   rise_dic.update({today.index:today})

   tokyo.date= date_tokyo
   today     = Moon(tokyo)
   today.transit(tokyo)
   transit_dic.update({today.index:today})

   tokyo.date= date_tokyo
   today     = Moon(tokyo)
   today.set(tokyo)
   set_dic.update({today.index:today})
   
   tokyo.date= date_tokyo
   today     = Moon(tokyo)
   today.noon(tokyo)
   ecl_dic.update({today.index:today})
   
print('　日付    潮   月齢　  月の出　    　月の入')
print('-------------------------------------------')

time_str = "%H:%M:%S"

for i in range(31):
   date1  = repr(ephem.localtime(date0))
   date2  = eval(date1) + datetime.timedelta(days=i)
   date_str   = date2.strftime('%Y%m%d')
   mm         = int(date2.strftime('%m'))
   dd         = int(date2.strftime('%d'))

   rise       = rise_dic.get(date_str)

   if (rise is None):
      rise_str     = "   ---   " 
   else:
      rise_time    = eval(rise.local).strftime(time_str)
      rise_str     = str('%s ' % (rise_time))

   set             = set_dic.get(date_str)

   if (set is None):
      set_str     = "   ---   "
   else:
      set_time     = eval(set.local).strftime(time_str)
      set_str      = str('%s ' % (set_time))

   ecl             = ecl_dic.get(date_str)

   if (ecl is None):
      ecl_str     = " ECL none! "
   else:
      ecl_tname   = ecl.tname
      ecl_diff    = ecl.ecl_diff
      moon_age    = ecl.moonage

   print(' %2d %2d | %s  %4.1f | %s | %s |' % (mm,dd,ecl_tname,moon_age,rise_str,set_str))

