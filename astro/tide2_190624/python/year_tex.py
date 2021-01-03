"""
    潮時表  TD2/TD3 (LaTeX) version.
    2019/06/23
    Ichiro Yoshida (yoshida.ichi@gmail.com)
"""
import sys
import math
import ephem
import datetime
import func.tide_func as tf
from func.moon_calc import *
import numpy as np
import func.TD3read as td
#import func.TD2read as td

year = 2019

pt = tf.Port

pt.name = td.name
pt.lat = td.lat
pt.lng = td.lng
pt.level = td.level

pt.pl = td.pl
pt.hr = td.hr

#--------------------------------------------------
print("\\documentclass[12pt,a4j]{jsarticle}")
print("\\begin{document}")
print("\\pagestyle{empty}")
#--------------------------------------------------

for month in range(1, 4):
    days = tf.month_days(year, month)

    print(" \\begin{table}[htbp]")
    print(" \\begin{tabular}{lcc}")
    print(" {\\LARGE %s } & {\\large %4d 年} & {\\large %2d 月}\\" % (pt.name, year, month))
    print(" \\end{tabular}")
    print(" \\begin{center}")
    print("    \\begin{tabular}{|rc|cr|ccrccr|ccrccr|}")
    print("    \\hline")
    print("    \\multicolumn{2}{|c|}{日（曜）} & \\multicolumn{2}{c|}{潮（月齢）} & \\multicolumn{6}{c|}{満潮時刻　―　潮位(cm)} & \\multicolumn{6}{c|}{干潮時刻　―　潮位(cm)} \\\\")
    print(" \\hline")

    for day in range(1, days+1):

        moon=ephem.Moon()

        pt_eph=ephem.Observer()
        pt_eph.lon, pt_eph.lat = pt.lng,pt.lat
        pt_eph.elevation = 0.0

        pt.date = str(year)+str('/%02d' % month)+str('/%02d' % day)
        pt_eph.date = str(pt.date+' 9:00')

        date_prn = str(pt.date)
        weekday  = get_weekday(pt.date)

        today_moon = Moon(pt_eph)
        today_moon.noon(pt_eph)

        moon_prn = today_moon.tname+str(' & %4.1f' % today_moon.moonage)

        today = tf.Tide(pt)
        today.wav(pt)

        level  = today.tl
        tide   = today.tide
        hitide = today.hitide
        lowtide= today.lowtide

        hitide_time   = np.array(hitide)[:,0]
        hitide_level  = np.array(hitide)[:,1]

        hitide_prn  = []
        lowtide_prn = []

        for hi in hitide:
           hitide_prn.append(str(' %5s &-& %3s '%(hi[0],hi[1])))
 
        for lo in lowtide:
           lowtide_prn.append(str(' %5s &-& %3s '%(lo[0],lo[1])))


        if len(hitide_prn) < 2 :
            hitide_prn.append(' --:-- &-&~~~~~')

        if len(lowtide_prn) < 2 :
           lowtide_prn.append(' --:-- &-&~~~~~')

        print("%2d & %s & %s & %s & %s &  %s &  %s \\\\" %(day,weekday,moon_prn,hitide_prn[0],hitide_prn[1],lowtide_prn[0],lowtide_prn[1]))

    print("   \\hline")
    print("   \\end{tabular}")
    print("   \\end{center}")
    print("\\end{table}")
    print("\\newpage")

#----------------------------------
print("\\end{document}")
