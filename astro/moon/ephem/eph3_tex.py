# -*- coding:utf-8 -*-

"""
月と太陽の暦(TEX)
2017/12/10
"""
import ephem
from moon_func import *
from moon_calc import *
import calend_func

year = 2018

moon = ephem.Moon()
sun = ephem.Sun()

location = ephem.Observer()

location.name = '福岡'
location.lon, location.lat = '130.4000', '33.5833'

location.elevation = 0.0

# tex -----------
print("\\documentclass[12pt.a4j]{jsarticle}")
print("\\begin{document}")
print("\\pagestyle{empty}")
print("\\begin{center}")

for month in range(1, 13):

    rise_dic    = {}
    set_dic     = {}
    ecl_dic     = {}

    days = calend_func.month_days(year, month)

    for d in range(0, days):

       day = d+1

       date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
       location.date = str(date0+' 9:00') #UT+9hr =JST
       date_location = location.date

       today     = Moon(location)
       today.rise(location)
       rise_dic.update({today.index:today})

       location.date= date_location
       today     = Moon(location)
       today.set(location)
       set_dic.update({today.index:today})
   
       location.date= date_location
       today     = Moon(location)
       today.noon(location)
       ecl_dic.update({today.index:today})

    # tex -----

    print("  {\\large %4d 年 %2d 月}" % (year, month))
    print("  {\\Large 　　　太陽と月の暦   （%s） }" % location.name)
    print("  \\begin{table}[ht]")
    print("  \\begin{center}")
    print("     \\begin{tabular}{|rc|ccc|rc|ccc|}")
    print("     \\hline")
    print("     \\multicolumn{2}{|c|}{日（曜）} & \\multicolumn{3}{c|}{日出　―　日没} & \\multicolumn{2}{c|}{月齢（潮）} & \\multicolumn{3}{c|}{月出　―　月没}\\\\")
    print("     \\hline")

    for d in range(0, days):
        day = d + 1
        date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
        location.date = str(date0+' 9:00')

        weekday = get_weekday(date0)

        date1  = repr(ephem.localtime(location.date))
        date2  = eval(date1)
        date_str   = date2.strftime('%Y%m%d')
        mm         = int(date2.strftime('%m'))
        dd         = int(date2.strftime('%d'))

        #--- Sun rise -----
        today = Sun(location)
        today.sun_rise(location)
        sun_rise = today.sun_rise

        #--- Sun set -----
        today = Sun(location)
        today.sun_set(location)
        sun_set = today.sun_set

        rise       = rise_dic.get(date_str)

        if (rise is None):
            rise_str     = " --:-- " 
        else:
            rise_str = rise.hhmm

        set             = set_dic.get(date_str)

        if (set is None):
            set_str     = " --:-- "
        else:
            set_str     = set.hhmm

        ecl             = ecl_dic.get(date_str)

        if (ecl is None):
            ecl_str     = " ECL none! "
        else:
            ecl_tname   = ecl.tname
            moon_age    = ecl.moonage

        print(' %2d & %s & %s &-& %s & %4.1f & %s & %s &-& %s \\\\'    %(dd,weekday,sun_rise,sun_set,moon_age,ecl_tname,rise_str,set_str))

    print("    \\hline")
    print("    \\end{tabular}")
    print("    \\end{center}")
    print("\\end{table}")
    print("\\newpage")

print("\\end{center}")
print("\\end{document}")

