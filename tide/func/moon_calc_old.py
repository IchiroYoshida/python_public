# -*- coding:utf-8 -*-

import ephem
import math
from func.roundTime import *

RAD=180./ephem.pi


"""
曜日
"""
def get_weekday(date):
    import datetime
    weekday=['月','火','水','木','金','土','日']
    d = datetime.datetime.strptime(date,"%Y/%m/%d")
    return weekday[d.weekday()]


"""
月の暦に関する基礎関数
"""
def rnd36(x):
   return (x -math.floor(x / 360) * 360)

def tidename_MoonAge(x):
    Name=['大','中','小','長','若','中','大','中','小','長','若','中']

    if   (x< 2):  return(Name[0])
    elif (x< 6):  return(Name[1])
    elif (x< 9):  return(Name[2])
    elif (x< 10):  return(Name[3])
    elif (x< 11):  return(Name[4])
    elif (x< 13):  return(Name[5])
    elif (x< 17):  return(Name[6])
    elif (x< 21):  return(Name[7])
    elif (x< 24):  return(Name[8])
    elif (x< 25):  return(Name[9])
    elif (x< 26):  return(Name[10])
    elif (x< 28):  return(Name[11])
    else        :  return(Name[0])

def tidename_MIRC(x):
    Name=['大','中','小','長','若','中','大','中','小','長','若','中']

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

def tidename_JMA(x):
    Name=['大','中','小','長','若','中','大','中','小','長','若','中']

    if   (x< 36):  return(Name[0])
    elif (x< 72):  return(Name[1])
    elif (x<108):  return(Name[2])
    elif (x<120):  return(Name[3])
    elif (x<132):  return(Name[4])
    elif (x<168):  return(Name[5])
    elif (x<216):  return(Name[6])
    elif (x<252):  return(Name[7])
    elif (x<288):  return(Name[8])
    elif (x<300):  return(Name[9])
    elif (x<312):  return(Name[10])
    elif (x<348):  return(Name[11])
    else        :  return(Name[0])


#月の出（時刻、方角、地方時、日付）	
class Moon(object):
   def __init__(self,observer):
       moon         = ephem.Moon(observer)
       self.azimuth = 0
       self.alt     = 0
       self.local   = 0
       self.index   = ''
       self.time    = ''
       self.rise_dic ={}

   def rise(self,observer):
       moon         = ephem.Moon(observer)
       observer.date= observer.previous_rising(moon,use_center=True) #月の出（時刻）
       moon         = ephem.Moon(observer) 
       self.azimuth = ephem.degrees(moon.az)*RAD                     #月出、方位角
       self.local   = repr(ephem.localtime(observer.date))           #時刻、日付

       rnd_time     = roundTime(eval(self.local),roundTo=1*60)
       self.index    = rnd_time.strftime('%Y%m%d')
       self.hhmm     = rnd_time.strftime('%H:%M')
       
       #self.rise_dic.update({self.index:self.local})

#月の没（時刻、方角、地方時、日付）
   def set(self,observer):
       moon         = ephem.Moon(observer)
       observer.date= observer.previous_setting(moon,use_center=True) #月の没（時刻）
       moon         = ephem.Moon(observer)
       self.azimuth = ephem.degrees(moon.az)*RAD                     #月没、方位角
       self.local   = repr(ephem.localtime(observer.date))           #時刻、日付

       rnd_time     = roundTime(eval(self.local),roundTo=1*60)
       self.index   = rnd_time.strftime('%Y%m%d')
       self.hhmm    = rnd_time.strftime('%H:%M')

#月と太陽の黄経、黄経差
   def noon(self, observer):
       time  = observer.date
       time0 = repr(ephem.localtime(time))
       time1 = eval(time0)
       time_str = time1.strftime('%Y/%m/%d') #日没時間の日付
       time_JST0 = ' 15:00'   #  0:00 JST 
       time_JST12 = ' 3:00'   #  12:00 JST
       time_JST21 = ' 12:00'   #  21:00 JST
       observer.date = time_str+time_JST21


       #太陽と月の黄経を算出する。
       sun          = ephem.Sun(observer)
       moon         = ephem.Moon(observer)
       ecl_moon     = ephem.Ecliptic(moon)    #月の黄経
       ecl_sun      = ephem.Ecliptic(sun)     #太陽の黄経
       self.ecl_diff  = rnd36((ecl_moon.lon - ecl_sun.lon )*RAD) #月と太陽の黄経差
       self.tname   = tidename_JMA(self.ecl_diff)
       #self.tname    = tidename_MIRC(self.ecl_diff)
       self.index    = time1.strftime('%Y%m%d')

       #12:00 JSTでの月齢を算出する。
       observer.date = time_str+time_JST12
       self.moonage  = observer.date - ephem.previous_new_moon(observer.date)
       #self.tname    = tidename_MoonAge(self.moonage)

# 太陽
class Sun(object):
    def __init__(self, observer):
        sun = ephem.Sun(observer)
        
# 太陽　日の出　その日の日の出時刻(JST)
    def sun_rise(self, observer):
        sun = ephem.Sun(observer)
        sun_rise0 = observer.previous_rising(sun)    #UTC
        sun_rise1 = repr(ephem.localtime(sun_rise0)) #UTC->JST
        sun_rise2 = roundTime(eval(sun_rise1), roundTo = 60) # Round(min)
        self.sun_rise = sun_rise2.strftime('%H:%M')

# 太陽　日没　その日の日没時刻(JST)
    def sun_set(self, observer):
        sun = ephem.Sun(observer)
        sun_set0 = observer.next_setting(sun)        #UTC
        sun_set1 = repr(ephem.localtime(sun_set0))   #UTC-> JST
        sun_set2 = roundTime(eval(sun_set1), roundTo = 60) # Round(min)
        self.sun_set = sun_set2.strftime('%H:%M')

