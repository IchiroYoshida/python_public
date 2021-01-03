"""
    暦・潮時表  TD2/TD3 (TEX) version.
    2019/07/13
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""
TEX = True

import sys
import math
import ephem
import datetime
import func.tide_func as tf 
import numpy as np
#import func.TD3read as td
import func.TD2read as td

class TideTable(object):
    def __init__(self, observer):
        observer = tf.Port()
        self.name = observer.name
        self.lat = observer.lat
        self.lng = observer.lng
        self.level = observer.level
        self.pl = observer.pl
        self.hr = observer.hr

        if (TEX):
            print("\\documentclass[12pt,a4j]{jsarticle}")
            print("\\begin{document}")
            print("\\pagestyle{empty}")

    def show(year,month, observer):
        days = tf.month_days(year,month)

        if (TEX):
            print(" \\begin{table}[htbp]")
            print(" \\begin{center}")
            print(" \\begin{tabular}{lcc}")
            print(" \\LARGE{{{:>s}}}".format(observer.name),\
                  " & \\large{{ {:4d} 年 }} & \\large{{ {:>2d} 月}} \\\\".format(year, month))
            print(" \\end{tabular}")
            print(" \\end{center}")
            print("    \\begin{center}")
            print("    \\begin{tabular}{|rc|cr|ccrccr|ccrccr|}")
            print("    \\hline")
            print("    \\multicolumn{2}{|c|}{日（曜）} & \\multicolumn{2}{c|}{潮（月齢）} & \\multicolumn{6}{c|}{満潮時刻　―　潮位(cm)} & \\multicolumn{6}{c|}{干潮時刻　―　潮位(cm)} \\\\")
            print(" \\hline")

        for day in range(1,days+1):

            moon=ephem.Moon()
            pt_eph=ephem.Observer()
            pt_eph.lon = str(observer.lng)
            pt_eph.lat = str(observer.lat)
            pt_eph.elevation = 0.0

            observer.date = str(year)+str('/%02d' % month)+str('/%02d' % day)
            pt_eph.date = str(observer.date+' 9:00')

            date_prn = str(observer.date)
            weekday  = tf.get_weekday(observer.date)

            today_moon = tf.Moon(pt_eph)
            today_moon.noon(pt_eph)

            today = tf.Tide(observer)
            today.wav(observer)

            level  = today.tl
            tide   = today.tide
            hitide = today.hitide
            lowtide= today.lowtide

            hitide_time   = np.array(hitide)[:,0]
            hitide_level  = np.array(hitide)[:,1]

            hitide_prn  = []
            lowtide_prn = []

            if (TEX):
                line_prn = []

                for hi in hitide:
                    hitide_prn.append(str(' %5s &-& %3s '%(hi[0],hi[1])))
 
                for lo in lowtide:
                    lowtide_prn.append(str(' %5s &-& %3s '%(lo[0],lo[1])))

                if len(hitide_prn) < 2 :
                    hitide_prn.append(' --:-- &-&~~~~~')

                if len(lowtide_prn) < 2 :
                    lowtide_prn.append(' --:-- &-&~~~~~')

                print('{:>2} &'.format(day),\
                      '{:>s} &'.format(weekday),\
                      '{:>s} &'.format(today_moon.tname),\
                      '{:>4.1f} &'.format(today_moon.moonage),\
                      '{:>s} &'.format(hitide_prn[0]),\
                      '{:>s} &'.format(hitide_prn[1]),\
                      '{:>s} &'.format(lowtide_prn[0]),\
                      '{:>s} \\\\'.format(lowtide_prn[1]))

        if(TEX):
            print("   \\hline")
            print("   \\end{tabular}")
            print("   \\end{center}")
            print("\\end{table}")
            print("\\newpage")

class TideEphemTable(object):
    def __init__(self, observer):
        observer = tf.Port()
        self.name = observer.name
        self.lat = observer.lat
        self.lng = observer.lng
        self.level = observer.level
        self.pl = observer.pl
        self.hr = observer.hr

        if (TEX):
            print("\\documentclass[12pt,a4j]{jsarticle}")
            print("\\usepackage{graphicx}")
            print("\\begin{document}")
            print("\\pagestyle{empty}")

    def show(year, month, observer):
        days = tf.month_days(year, month)

        moon_rise = {}
        moon_set = {}

        if (TEX):
            print(" \\begin{table}[htbp]")
            print(" \\begin{center}")
            print(" \\begin{tabular}{lcc}")
            print(" \\LARGE{{{:>s}}}".format(observer.name),\
                  " & \\large{{{:4d} 年}} & \\large{{{:>2d} 月}} \\\\".format(year, month))
            print(" \\end{tabular}")
            print(" \\end{center}")
            print(" \\begin{center}")
            print("    \\scalebox{0.7}[1.0]{")
            print("    \\begin{tabular}{|rc|cr|ccrccr|ccrccr|ccc|ccc|}")
            print("    \\hline")
            print("    \\multicolumn{2}{|c|}{日（曜）} &",\
                      "\\multicolumn{2}{c|}{潮（月齢）} &",\
                      "\\multicolumn{6}{c|}{満潮（時刻、潮位 cm）} &",\
                      "\\multicolumn{6}{c|}{干潮（時刻、潮位 cm）} &",\
                      "\\multicolumn{3}{c|}{日の出−入} & ",\
                      "\\multicolumn{3}{c|}{月の出−入}\\\\")
            print(" \\hline")

        # Moon Rise and Set calculation
        for day in range(1,days+1):

            pt_eph = ephem.Observer()
            pt_eph.lon = str(observer.lng)
            pt_eph.lat = str(observer.lat)
            pt_eph.elevation = 0.0
            pt_eph.pressure = 0
            pt_eph.horizon = '-0:34'

            date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
            pt_eph.date = str(date0+' 9:00')  #UT+9hr = JST
            date_location = pt_eph.date

            today_moon = tf.Moon(pt_eph)
            today_moon.rise(pt_eph)
            moon_rise.update({today_moon.index:today_moon})

            pt_eph.date = date_location
            today_moon = tf.Moon(pt_eph)
            today_moon.set(pt_eph)
            moon_set.update({today_moon.index:today_moon})

        # Sun set and rise calculation
        for day in range(1, days+1):

            date0 = str(year)+str('/%02d' % month)+str('/%02d' % day)
            pt_eph.date = str(date0 + ' 9:00')   #UT+9hr ->JST
            weekday = tf.get_weekday(date0)

            date1 = repr(ephem.localtime(pt_eph.date))
            date2 = eval(date1)
            date_str = date2.strftime('%Y%m%d')
            mm = int(date2.strftime('%m'))

            #---- Sun rise ------
            today_sun = tf.Sun(pt_eph)
            today_sun.sun_rise(pt_eph)
            SunRise = today_sun.sun_rise

            #---- Sun set -------
            today_sun = tf.Sun(pt_eph)
            today_sun.sun_set(pt_eph)
            SunSet = today_sun.sun_set

            #---- Tide and Moon age ---
            today_moon = tf.Moon(pt_eph)
            today_moon.noon(pt_eph)
            tide_name = today_moon.tname
            moon_age = str('%3.1f' % today_moon.moonage)

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

            observer.date = date0

            today = tf.Tide(observer)
            today.wav(observer)

            level  = today.tl
            tide   = today.tide
            hitide = today.hitide
            lowtide= today.lowtide

            hitide_time   = np.array(hitide)[:,0]
            hitide_level  = np.array(hitide)[:,1]

            hitide_prn  = []
            lowtide_prn = []

            if (TEX):
                for hi in hitide:
                    hitide_prn.append(str(' %5s &-& %3s'%(hi[0],hi[1])))
 
                for lo in lowtide:
                    lowtide_prn.append(str(' %5s &-& %3s'%(lo[0],lo[1])))

                if len(hitide_prn) < 2 :
                    hitide_prn.append(' --:-- &-&~~~~~')

                if len(lowtide_prn) < 2 :
                    lowtide_prn.append(' --:-- &-&~~~~~')

                print('{:>2} &'.format(day),\
                      '{:>s} &'.format(weekday),\
                      '{:>s} &'.format(today_moon.tname),\
                      '{:>4.1f} &'.format(today_moon.moonage),\
                      '{:>s} &'.format(hitide_prn[0]),\
                      '{:>s} &'.format(hitide_prn[1]),\
                      '{:>s} &'.format(lowtide_prn[0]),\
                      '{:>s} &'.format(lowtide_prn[1]),\
                      '{:>s} &'.format(SunRise),\
                      '-& {:>s} &'.format(SunSet),\
                      '{:>s} &'.format(rise_str),\
                      '-& {:>s} \\\\'.format(set_str))

        if(TEX):
            print("   \\hline")
            print("   \\end{tabular}}")
            print("   \\end{center}")
            print("\\end{table}")
            print("\\newpage")

"""
Main
"""

TideEphemTable(td)

for month in range(7, 13):
    TideEphemTable.show(2019, month, td)

for year in range(2020, 2022):
    for month in range(1, 13):
        TideEphemTable.show(year, month, td)

if (TEX):
    print("\\end{document}")
