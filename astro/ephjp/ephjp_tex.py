# -*- coding:utf-8 -*-

"""
月と太陽の暦(TEX版)  Ichiro Yoshida
2017/12/12
"""
import datetime
import ephem
import eph_func as ephf

year = 2019 

moon = ephem.Moon()
sun = ephem.Sun()

location = ephem.Observer()

location.name = '東京'
location.lon, location.lat = '139.7414', '35.6581'

location.pressure = 0
location.horizon = '-0:34'

location.elevation = 0.0

# tex -----------
print("\\documentclass[a4j,10pt]{jsarticle}")
print("\\begin{document}")
print("\\pagestyle{empty}")
print("\\begin{center}")

for month in range(1, 2):

    moon_rise = {}
    moon_set = {}

    days = ephf.month_days(year, month)

    for day in range(1, days+1):

        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        location.date = str(date0+' 9:00') #UT+9hr =JST
        date_location = location.date

        today = ephf.Moon(location)
        today.rise(location)
        moon_rise.update({today.index:today})

        location.date = date_location
        today = ephf.Moon(location)
        today.set(location)
        moon_set.update({today.index:today})
   
    # tex -----
    print("{\\large %4d 年 %2d 月}" % (year, month))
    print("{\\Large 　　　太陽と月の暦   （%s） }" % location.name)
    print("\\begin{table}[ht]")
    print("\\begin{center}")
    print("\\begin{tabular}{|rc|ccc|rc|ccc|}")
    print("\\hline")
    print("\\multicolumn{2}{|c|}{日（曜）} & \\multicolumn{3}{c|}")
    print("{日出　―　日没} & \\multicolumn{2}{c|}{月齢（潮）} & ")
    print("\\multicolumn{3}{c|}{月出　―　月没}\\\\")
    print("\\hline")

    for day in range(1, days+1):
        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        location.date = str(date0+' 9:00')

        weekday = ephf.get_weekday(date0)

        date1 = repr(ephem.localtime(location.date))
        date2 = eval(date1)
        date_str = date2.strftime('%Y%m%d')
        mm = int(date2.strftime('%m'))

        #--- 日出の時刻 -----
        today = ephf.Sun(location)
        today.sun_rise(location)
        sun_rise = today.sun_rise

        #--- 日没の時刻 -----
        today = ephf.Sun(location)
        today.sun_set(location)
        sun_set = today.sun_set

        #--- 潮名と月齢  -----
        today = ephf.Moon(location)
        today.noon(location)
        tide_name = today.tname
        moon_age = today.moonage

        rise = moon_rise.get(date_str)

        if rise is None:
            rise_str = "--:--" 
        else:
            rise_str = rise.hhmm

        set = moon_set.get(date_str)

        if set is None:
            set_str = "--:--"
        else:
            set_str = set.hhmm

        print(' %2d & %s & %s &-& %s & %4.1f & %s & %s &-& %s \\\\' \
                %(day, weekday, sun_rise, sun_set, moon_age, tide_name, rise_str, set_str))

    # tex ----------
    print("\\hline")
    print("\\end{tabular}")
    print("\\end{center}")
    print("\\end{table}")
    print("\\newpage")

# tex ------------
print("\\end{center}")
print("\\end{document}")
