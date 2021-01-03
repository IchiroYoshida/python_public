#!/home/ichiro1/anaconda3/bin/python
# -*- coding:utf-8 -*-

"""
月の出、南中、入りの時刻計算  東京(JST:UTC+9hr)
"""
import ephem
import datetime

RAD=180./ephem.pi
AU = 149597870.7  #1AU (Km)

#月の出（時刻、方角、地方時、日付）	
class MoonRise(object):
   def __init__(self,observer):
       moon         = ephem.Moon(observer)
       self.utc     = observer.next_rising(moon,use_center=True)
       observer.date= self.utc

       moon         = ephem.Moon(observer) 
       self.azimuth = ephem.degrees(moon.az)*RAD 
       self.local   = repr(ephem.localtime(self.utc))
       self.date    = eval(self.local).strftime('%Y%m%d')

#月の南中（時刻、角度、地方時、日付）
class MoonTransit(object):
   def __init__(self,observer):
       moon         = ephem.Moon(observer)
       self.utc     = observer.next_transit(moon)
       observer.date= self.utc

       moon         = ephem.Moon(observer)   
       self.alt     = ephem.degrees(moon.alt)*RAD
       self.local   = repr(ephem.localtime(self.utc))
       self.date    = eval(self.local).strftime('%Y%m%d')

       self.radius  = moon.radius
       self.dist    = moon.earth_distance*AU
       self.phase   = moon.moon_phase

#月の没（時刻、方角、地方時、日付）
class MoonSet(object):
   def __init__(self,observer):
       moon         = ephem.Moon(observer)
       self.utc     = observer.next_setting(moon,use_center=True)
       observer.date= self.utc
       
       moon         = ephem.Moon(observer)
       self.azimuth = ephem.degrees(moon.az)*RAD
       self.local   = repr(ephem.localtime(self.utc))
       self.date    = eval(self.local).strftime('%Y%m%d')

moon=ephem.Moon()

tokyo = ephem.Observer()
tokyo.lon, tokyo.lat = '139.7414', '35.681'
tokyo.elevation = 0.0
tokyo.date = '2016/5/31 15:00' #計算開始、UT 0:00 JST=UT+ 9hr

date0 = tokyo.date

rise_dic    = {}
transit_dic = {}
set_dic     = {}

for i in range(31):
   tokyo.date    = date0 + i     

   this_rise     = MoonRise(tokyo)
   this_transit  = MoonTransit(tokyo)
   this_set      = MoonSet(tokyo)

   rise_dic.update({this_rise.date:this_rise})
   transit_dic.update({this_transit.date:this_transit})
   set_dic.update({this_set.date:this_set})

print('　日付  時刻　　月の出　＜方位＞　南中　＜高度＞　月の入　＜方位＞')
print('------------------------------------------------------------------')

time_str = "%H:%M:%S"

for i in range(31):
   date1  = repr(ephem.localtime(date0))
   date2  = eval(date1) + datetime.timedelta(days=i)
   date_str   = date2.strftime('%Y%m%d')
   mm         = int(date2.strftime('%m'))
   dd         = int(date2.strftime('%d'))

   rise       = rise_dic.get(date_str)
 
   if (rise is None):
      rise_str     = "   -----------   " 
   else:
      rise_time    = eval(rise.local).strftime(time_str)
      rise_azimuth = rise.azimuth
      rise_str     = str('%s -- %5.1f' % (rise_time,rise_azimuth))

   transit      = transit_dic.get(date_str)
   
   if (transit is None):
      transit_str  = "   ----------   "
      transit_dat  = "  *** *** *** "

   else:
      transit_time = eval(transit.local).strftime(time_str)
      transit_alt  = transit.alt
      transit_str  = str('%s -- %4.1f' %(transit_time,transit_alt))
      transit_dat  = str('%f - %f - %f' %(transit.radius,transit.dist,transit.phase))
   
   set             = set_dic.get(date_str)

   if (set is None):
      set_str     = "   ----------   "
   else:
      set_time     = eval(set.local).strftime(time_str)
      set_azimuth  = set.azimuth
      set_str      = str('%s -- %5.1f' % (set_time,set_azimuth))
 
   print(' %2d %2d  |  %s | %s | %s | %s ' % (mm,dd,rise_str,transit_str,set_str,transit_dat))
