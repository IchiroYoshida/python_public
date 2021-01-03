# -*- coding:utf-8 -*-

"""
月の出、南中、入りの時刻計算  東京(JST:UTC+9hr)
"""
import math
import ephem
import datetime

RAD=180./ephem.pi
AU = 149597870.7  #1AU (Km)

#
def rnd36(x):
   return (x -math.floor(x / 360) * 360)

def tidename(x):
    Name=['大潮','中潮','小潮','長潮','若潮','中潮','大潮','中潮','小潮','長潮','若潮','中潮']

    if   (x< 31):  return(Name[0])
    elif (x< 67):  return(Name[1])
    elif (x<103):  return(Name[2])
    elif (x<115):  return(Name[3])
    elif (x<127):  return(Name[4])
    elif (x<163):  return(Name[5])
    elif (x<211):  return(Name[6])
    elif (x<247):  return(Name[7])
    elif (x<283):  return(Name[8])
    elif (x<295):  return(Name[9])
    elif (x<307):  return(Name[10])
    elif (x<343):  return(Name[11])
    else        :  return(Name[0])

#月の出（時刻、方角、地方時、日付）	
class MoonRise(object):
   def __init__(self,observer):
       moon         = ephem.Moon(observer)
       self.utc     = observer.previous_rising(moon,use_center=True)
       observer.date= self.utc

       moon         = ephem.Moon(observer) 
       self.azimuth = ephem.degrees(moon.az)*RAD 
       self.local   = repr(ephem.localtime(self.utc))
       self.date    = eval(self.local).strftime('%Y%m%d')

#月の南中（時刻、角度、地方時、日付）
class MoonTransit(object):
   def __init__(self,observer):
       moon         = ephem.Moon(observer)
       self.utc     = observer.previous_transit(moon)
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
       self.utc     = observer.previous_setting(moon,use_center=True)
       observer.date= self.utc
       
       moon         = ephem.Moon(observer)
       self.azimuth = ephem.degrees(moon.az)*RAD
       self.local   = repr(ephem.localtime(self.utc))
       self.date    = eval(self.local).strftime('%Y%m%d')

#正午の月と太陽の黄経、黄経差
class Noon(object):
   def __init__(self,observer):
       sun          = ephem.Sun(observer)
       time         = observer.next_setting(sun)
       time0        = repr(ephem.localtime(time))
       time1        = eval(time0)
       time_str     = time1.strftime('%Y/%m/%d')
       time_JST     = ' 3:00'                   # 12:00 JST 
       observer.date    = time_str+time_JST

       sun          = ephem.Sun(observer)
       moon         = ephem.Moon(observer)
       ecl_moon     = ephem.Ecliptic(moon)
       ecl_sun      = ephem.Ecliptic(sun)
       self.ecl_diff  = rnd36((ecl_moon.lon - ecl_sun.lon )*RAD)
       self.tname   = tidename(self.ecl_diff)
       self.date    = time1.strftime('%Y%m%d')

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
   this_rise     = MoonRise(tokyo)

   tokyo.date    = date_tokyo
   this_transit  = MoonTransit(tokyo)

   tokyo.date    = date_tokyo
   this_set      = MoonSet(tokyo)

   tokyo.date    = date_tokyo
   this_noon     = Noon(tokyo)

   rise_dic.update({this_rise.date:this_rise})
   transit_dic.update({this_transit.date:this_transit})
   set_dic.update({this_set.date:this_set})
   ecl_dic.update({this_noon.date:this_noon})

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

   ecl             = ecl_dic.get(date_str)

   if (ecl is None):
      ecl_str     = " ECL none! "
   else:
      ecl_tname   = ecl.tname
      ecl_diff    = ecl.ecl_diff

   print(' %2d %2d | %s = %5.2f |  %s | %s | %s | %s ' % (mm,dd,ecl_tname,ecl_diff,rise_str,transit_str,set_str,transit_dat))
